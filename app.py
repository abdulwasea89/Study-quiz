import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

# Import custom components
from components.flashcards import flashcard_system
from components.mock_test import mock_test_system
from components.analytics import analytics_dashboard
from data.study_data import get_flashcards, get_topics, get_summary_data
from utils.progress_tracker import ProgressTracker

# Page configuration
st.set_page_config(
    page_title="Agentic AI Study Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

if 'current_study_session' not in st.session_state:
    st.session_state.current_study_session = {
        'start_time': datetime.now(),
        'flashcards_studied': 0,
        'tests_taken': 0,
        'correct_answers': 0,
        'total_questions': 0
    }

def main():
    st.title("🤖 Agentic AI Study Hub")
    st.markdown("---")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose your study mode:",
        ["📚 Dashboard", "🔄 Flashcards", "📝 Mock Tests", "📊 Analytics", "📋 Summary Sheets"]
    )
    
    # Display current session stats in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Current Session")
    session = st.session_state.current_study_session
    st.sidebar.metric("Flashcards Studied", session['flashcards_studied'])
    st.sidebar.metric("Tests Taken", session['tests_taken'])
    if session['total_questions'] > 0:
        accuracy = (session['correct_answers'] / session['total_questions']) * 100
        st.sidebar.metric("Session Accuracy", f"{accuracy:.1f}%")
    
    # Main content area
    if page == "📚 Dashboard":
        show_dashboard()
    elif page == "🔄 Flashcards":
        flashcard_system()
    elif page == "📝 Mock Tests":
        mock_test_system()
    elif page == "📊 Analytics":
        analytics_dashboard()
    elif page == "📋 Summary Sheets":
        show_summary_sheets()

def show_dashboard():
    st.header("Welcome to Your Agentic AI Study Hub")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Total Flashcards", 
            len(get_flashcards()),
            help="Available flashcards for study"
        )
    
    with col2:
        st.metric(
            "Study Topics", 
            len(get_topics()),
            help="Different topic areas covered"
        )
    
    with col3:
        total_sessions = len(st.session_state.progress_tracker.get_all_sessions())
        st.metric(
            "Study Sessions", 
            total_sessions,
            help="Total completed study sessions"
        )
    
    st.markdown("---")
    
    # Quick start options
    st.subheader("Quick Start")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Start Flashcard Review", use_container_width=True):
            st.switch_page("app.py")
            st.session_state.page = "🔄 Flashcards"
    
    with col2:
        if st.button("📝 Take Practice Test", use_container_width=True):
            st.switch_page("app.py")
            st.session_state.page = "📝 Mock Tests"
    
    with col3:
        if st.button("📊 View Progress", use_container_width=True):
            st.switch_page("app.py")
            st.session_state.page = "📊 Analytics"
    
    # Recent activity
    st.markdown("---")
    st.subheader("Recent Activity")
    
    recent_sessions = st.session_state.progress_tracker.get_recent_sessions(5)
    if recent_sessions:
        for session in recent_sessions:
            with st.expander(f"Session {session['session_id']} - {session['date']}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Duration:** {session['duration']} minutes")
                with col2:
                    st.write(f"**Flashcards:** {session['flashcards_studied']}")
                with col3:
                    if session['test_scores']:
                        avg_score = sum(session['test_scores']) / len(session['test_scores'])
                        st.write(f"**Avg Score:** {avg_score:.1f}%")
    else:
        st.info("No study sessions yet. Start studying to see your progress!")

def show_summary_sheets():
    st.header("📋 Summary Sheets")
    st.markdown("Quick reference guides for key concepts")
    
    summary_data = get_summary_data()
    
    # Create tabs for different summary categories
    tabs = st.tabs(list(summary_data.keys()))
    
    for i, (category, items) in enumerate(summary_data.items()):
        with tabs[i]:
            st.subheader(f"{category}")
            
            # Display items as cards
            cols = st.columns(2)
            for j, item in enumerate(items):
                with cols[j % 2]:
                    st.info(f"• {item}")
    
    # Display flashcards as a reference table
    st.markdown("---")
    st.subheader("📚 Flashcard Reference")
    
    flashcards = get_flashcards()
    df = pd.DataFrame(list(flashcards.items()), columns=["Term", "Definition"])
    
    # Add search functionality
    search_term = st.text_input("🔍 Search flashcards:", placeholder="Enter term or keyword...")
    
    if search_term:
        mask = df['Term'].str.contains(search_term, case=False) | \
               df['Definition'].str.contains(search_term, case=False)
        df = df[mask]
    
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Term": st.column_config.TextColumn("Term", width="medium"),
            "Definition": st.column_config.TextColumn("Definition", width="large")
        }
    )

if __name__ == "__main__":
    main()
