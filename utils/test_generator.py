"""
Test generation utilities for creating mock tests
"""
import random
from typing import Dict, List, Any, Optional
from data.study_data import get_topics, get_questions_by_topic, get_difficulty_levels

class TestGenerator:
    def __init__(self):
        self.topics = get_topics()
        self.questions_pool = get_questions_by_topic()
        self.difficulty_levels = get_difficulty_levels()
        self.frameworks = {
            "Building Effective Agents": ["Agent Architecture", "Design Patterns", "Memory Systems", "Tool Integration", "Retrieval Systems", "Economic Integration"],
            "Model Context Protocol (MCP)": ["MCP Fundamentals", "Transport Layers", "HTTP Theory", "REST Architecture", "JSON-RPC", "Security", "MCP OpenAI Integration"],
            "OpenAI Agents SDK": ["OpenAI Agents SDK Fundamentals", "OpenAI Agents Implementation", "OpenAI Tools and Functions", "OpenAI Handoffs and Multi-Agent", "OpenAI Sessions and State", "OpenAI Guardrails and Security", "OpenAI Tracing and Monitoring"]
        }
    
    def generate_mock_test(self, total_questions: int = 120, custom_distribution: Optional[Dict[str, int]] = None) -> List[Dict[str, Any]]:
        """
        Generate a mock test with specified number of questions
        
        Args:
            total_questions: Total number of questions for the test
            custom_distribution: Custom distribution of questions per topic
        
        Returns:
            List of question dictionaries
        """
        if custom_distribution is None:
            # Use default distribution from topics
            distribution = self._calculate_distribution(total_questions)
        else:
            distribution = custom_distribution
        
        test_questions = []
        
        for topic, num_questions in distribution.items():
            if topic in self.questions_pool:
                topic_questions = self.questions_pool[topic]
                
                # If we need more questions than available, repeat some
                if num_questions > len(topic_questions):
                    selected = topic_questions * (num_questions // len(topic_questions) + 1)
                    selected = selected[:num_questions]
                else:
                    selected = random.sample(topic_questions, min(num_questions, len(topic_questions)))
                
                # Add topic information to each question
                for question in selected:
                    question_copy = question.copy()
                    question_copy['topic'] = topic
                    test_questions.append(question_copy)
        
        # Shuffle the final test questions
        random.shuffle(test_questions)
        
        # Add question numbers
        for i, question in enumerate(test_questions, 1):
            question['question_number'] = i
        
        return test_questions
    
    def _calculate_distribution(self, total_questions: int) -> Dict[str, int]:
        """Calculate question distribution based on topic weights"""
        total_weight = sum(self.topics.values())
        distribution = {}
        
        for topic, weight in self.topics.items():
            questions_for_topic = round((weight / total_weight) * total_questions)
            distribution[topic] = questions_for_topic
        
        # Adjust for rounding errors
        current_total = sum(distribution.values())
        if current_total != total_questions:
            # Add or remove questions from the largest topic
            largest_topic = max(distribution.keys(), key=lambda k: distribution[k])
            distribution[largest_topic] = max(0, distribution[largest_topic] + (total_questions - current_total))
        
        return distribution
    
    def generate_framework_test(self, framework: str, difficulty: str = None, num_questions: int = 50) -> List[Dict[str, Any]]:
        """Generate test for specific framework and difficulty"""
        if framework not in self.frameworks:
            return []
        
        relevant_topics = self.frameworks[framework]
        test_questions = []
        
        for topic in relevant_topics:
            if topic in self.questions_pool:
                topic_questions = self.questions_pool[topic]
                
                # Filter by difficulty if specified
                if difficulty and difficulty != "All Levels":
                    topic_questions = [q for q in topic_questions if q.get('difficulty') == difficulty]
                
                # Add framework questions
                for question in topic_questions:
                    question_copy = question.copy()
                    question_copy['topic'] = topic
                    question_copy['framework'] = framework
                    test_questions.append(question_copy)
        
        # Limit to requested number
        if len(test_questions) > num_questions:
            test_questions = random.sample(test_questions, num_questions)
        
        random.shuffle(test_questions)
        
        for i, question in enumerate(test_questions, 1):
            question['question_number'] = i
        
        return test_questions
    
    def get_available_frameworks(self) -> List[str]:
        """Get list of available frameworks"""
        return list(self.frameworks.keys())
    
    def get_framework_topics(self, framework: str) -> List[str]:
        """Get topics for a specific framework"""
        return self.frameworks.get(framework, [])
    
    def generate_topic_test(self, topic: str, num_questions: int = 10) -> List[Dict[str, Any]]:
        """Generate a test focused on a specific topic"""
        if topic not in self.questions_pool:
            return []
        
        topic_questions = self.questions_pool[topic]
        
        # Select questions (with repetition if needed)
        if num_questions > len(topic_questions):
            selected = topic_questions * (num_questions // len(topic_questions) + 1)
            selected = selected[:num_questions]
        else:
            selected = random.sample(topic_questions, min(num_questions, len(topic_questions)))
        
        # Add metadata
        for i, question in enumerate(selected, 1):
            question['topic'] = topic
            question['question_number'] = i
        
        random.shuffle(selected)
        return selected
    
    def get_available_topics(self) -> List[str]:
        """Get list of available topics for testing"""
        return list(self.topics.keys())
    
    def get_topic_question_count(self, topic: str) -> int:
        """Get number of available questions for a topic"""
        return len(self.questions_pool.get(topic, []))
    
    def filter_questions_by_difficulty(self, questions: List[Dict[str, Any]], difficulty: str) -> List[Dict[str, Any]]:
        """Filter questions by difficulty level"""
        if difficulty == "All":
            return questions
        
        filtered = [q for q in questions if q.get('difficulty', 'Normal') == difficulty]
        
        # If no questions found for specific difficulty, fall back to all questions
        if not filtered:
            return questions
        
        return filtered
    
    def generate_difficulty_test(self, difficulty: str, total_questions: int = 50) -> List[Dict[str, Any]]:
        """Generate a test focused on a specific difficulty level"""
        all_questions = []
        
        # Collect all questions from all topics
        for topic, questions in self.questions_pool.items():
            filtered_questions = self.filter_questions_by_difficulty(questions, difficulty)
            for question in filtered_questions:
                question_copy = question.copy()
                question_copy['topic'] = topic
                all_questions.append(question_copy)
        
        if not all_questions:
            return []
        
        # Select random questions up to the total requested
        if total_questions >= len(all_questions):
            selected = all_questions.copy()
        else:
            selected = random.sample(all_questions, total_questions)
        
        # Add question numbers and shuffle
        random.shuffle(selected)
        for i, question in enumerate(selected, 1):
            question['question_number'] = i
        
        return selected
    
    def get_available_difficulties(self) -> List[str]:
        """Get list of available difficulty levels"""
        return list(self.difficulty_levels.keys())
