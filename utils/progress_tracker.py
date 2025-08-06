"""
Progress tracking utilities for monitoring study performance
"""
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import streamlit as st

class ProgressTracker:
    def __init__(self, data_file: str = "study_progress.json"):
        self.data_file = data_file
        self.data = self._load_data()
    
    def _load_data(self) -> Dict[str, Any]:
        """Load progress data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        
        # Return default structure
        return {
            "sessions": [],
            "flashcard_stats": {},
            "test_results": [],
            "topic_performance": {},
            "study_streak": 0,
            "last_study_date": None
        }
    
    def _save_data(self):
        """Save progress data to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2, default=str)
        except IOError:
            st.error("Could not save progress data")
    
    def start_session(self) -> str:
        """Start a new study session"""
        session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        session = {
            "session_id": session_id,
            "start_time": datetime.now().isoformat(),
            "end_time": None,
            "flashcards_studied": 0,
            "tests_taken": 0,
            "test_scores": [],
            "topics_covered": set(),
            "duration": 0
        }
        
        self.data["sessions"].append(session)
        return session_id
    
    def end_session(self, session_id: str):
        """End a study session"""
        for session in self.data["sessions"]:
            if session["session_id"] == session_id:
                session["end_time"] = datetime.now().isoformat()
                start_time = datetime.fromisoformat(session["start_time"])
                end_time = datetime.fromisoformat(session["end_time"])
                session["duration"] = (end_time - start_time).total_seconds() / 60  # in minutes
                session["topics_covered"] = list(session.get("topics_covered", set()))
                break
        
        self._update_study_streak()
        self._save_data()
    
    def record_flashcard_study(self, session_id: str, term: str, correct: bool, response_time: float = None):
        """Record flashcard study activity"""
        # Update session
        for session in self.data["sessions"]:
            if session["session_id"] == session_id:
                session["flashcards_studied"] += 1
                break
        
        # Update flashcard stats
        if term not in self.data["flashcard_stats"]:
            self.data["flashcard_stats"][term] = {
                "times_studied": 0,
                "times_correct": 0,
                "last_studied": None,
                "difficulty_level": 1,
                "next_review": None
            }
        
        stats = self.data["flashcard_stats"][term]
        stats["times_studied"] += 1
        stats["last_studied"] = datetime.now().isoformat()
        
        if correct:
            stats["times_correct"] += 1
            # Increase difficulty (space out reviews more)
            stats["difficulty_level"] = min(5, stats["difficulty_level"] + 1)
        else:
            # Decrease difficulty (review sooner)
            stats["difficulty_level"] = max(1, stats["difficulty_level"] - 1)
        
        # Calculate next review date based on spaced repetition
        days_until_review = stats["difficulty_level"] * 2
        stats["next_review"] = (datetime.now() + timedelta(days=days_until_review)).isoformat()
        
        self._save_data()
    
    def record_test_result(self, session_id: str, topic: str, score: float, total_questions: int, correct_answers: int):
        """Record test results"""
        # Update session
        for session in self.data["sessions"]:
            if session["session_id"] == session_id:
                session["tests_taken"] += 1
                session["test_scores"].append(score)
                if isinstance(session.get("topics_covered"), set):
                    session["topics_covered"].add(topic)
                else:
                    topics = set(session.get("topics_covered", []))
                    topics.add(topic)
                    session["topics_covered"] = topics
                break
        
        # Record detailed test result
        test_result = {
            "session_id": session_id,
            "date": datetime.now().isoformat(),
            "topic": topic,
            "score": score,
            "total_questions": total_questions,
            "correct_answers": correct_answers,
            "accuracy": (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        }
        
        self.data["test_results"].append(test_result)
        
        # Update topic performance
        if topic not in self.data["topic_performance"]:
            self.data["topic_performance"][topic] = {
                "total_tests": 0,
                "total_score": 0,
                "best_score": 0,
                "recent_scores": [],
                "improvement_trend": 0
            }
        
        topic_perf = self.data["topic_performance"][topic]
        topic_perf["total_tests"] += 1
        topic_perf["total_score"] += score
        topic_perf["best_score"] = max(topic_perf["best_score"], score)
        topic_perf["recent_scores"].append(score)
        
        # Keep only last 10 scores for trend analysis
        if len(topic_perf["recent_scores"]) > 10:
            topic_perf["recent_scores"] = topic_perf["recent_scores"][-10:]
        
        # Calculate improvement trend
        if len(topic_perf["recent_scores"]) >= 2:
            recent = topic_perf["recent_scores"][-3:]  # Last 3 scores
            older = topic_perf["recent_scores"][:-3] if len(topic_perf["recent_scores"]) > 3 else []
            
            if older:
                recent_avg = sum(recent) / len(recent)
                older_avg = sum(older) / len(older)
                topic_perf["improvement_trend"] = recent_avg - older_avg
        
        self._save_data()
    
    def get_flashcards_for_review(self, limit: int = 10) -> List[str]:
        """Get flashcards that need review based on spaced repetition"""
        now = datetime.now()
        due_cards = []
        
        for term, stats in self.data["flashcard_stats"].items():
            if stats["next_review"]:
                next_review = datetime.fromisoformat(stats["next_review"])
                if next_review <= now:
                    due_cards.append((term, stats["difficulty_level"]))
        
        # Sort by difficulty (easier cards first)
        due_cards.sort(key=lambda x: x[1])
        
        return [term for term, _ in due_cards[:limit]]
    
    def get_topic_performance(self, topic: str) -> Optional[Dict[str, Any]]:
        """Get performance statistics for a specific topic"""
        return self.data["topic_performance"].get(topic)
    
    def get_overall_stats(self) -> Dict[str, Any]:
        """Get overall study statistics"""
        total_sessions = len(self.data["sessions"])
        total_flashcards = sum(session.get("flashcards_studied", 0) for session in self.data["sessions"])
        total_tests = len(self.data["test_results"])
        
        if self.data["test_results"]:
            avg_score = sum(result["score"] for result in self.data["test_results"]) / len(self.data["test_results"])
            best_score = max(result["score"] for result in self.data["test_results"])
        else:
            avg_score = 0
            best_score = 0
        
        total_study_time = sum(session.get("duration", 0) for session in self.data["sessions"])
        
        return {
            "total_sessions": total_sessions,
            "total_flashcards_studied": total_flashcards,
            "total_tests_taken": total_tests,
            "average_test_score": avg_score,
            "best_test_score": best_score,
            "total_study_time": total_study_time,
            "study_streak": self.data["study_streak"],
            "last_study_date": self.data["last_study_date"]
        }
    
    def get_recent_sessions(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get recent study sessions"""
        sessions = sorted(self.data["sessions"], key=lambda x: x["start_time"], reverse=True)
        
        result = []
        for session in sessions[:limit]:
            if session.get("end_time"):
                result.append({
                    "session_id": session["session_id"],
                    "date": datetime.fromisoformat(session["start_time"]).strftime("%Y-%m-%d %H:%M"),
                    "duration": round(session.get("duration", 0), 1),
                    "flashcards_studied": session.get("flashcards_studied", 0),
                    "test_scores": session.get("test_scores", [])
                })
        
        return result
    
    def get_all_sessions(self) -> List[Dict[str, Any]]:
        """Get all study sessions"""
        return self.data["sessions"]
    
    def _update_study_streak(self):
        """Update the study streak counter"""
        today = datetime.now().date()
        last_date = None
        
        if self.data["last_study_date"]:
            last_date = datetime.fromisoformat(self.data["last_study_date"]).date()
        
        if last_date is None:
            # First study session
            self.data["study_streak"] = 1
        elif last_date == today:
            # Already studied today, no change to streak
            pass
        elif last_date == today - timedelta(days=1):
            # Studied yesterday, increment streak
            self.data["study_streak"] += 1
        else:
            # Gap in studying, reset streak
            self.data["study_streak"] = 1
        
        self.data["last_study_date"] = today.isoformat()
