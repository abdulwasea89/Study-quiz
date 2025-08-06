import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

# Import custom components
from components.flashcards import flashcard_system
from components.mock_test import mock_test_system
from components.analytics import analytics_dashboard
from components.live_dashboard import show_live_dashboard
from components.documentation import show_comprehensive_docs
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
    
    # Handle quick navigation from dashboard
    if 'quick_nav' in st.session_state:
        default_page = st.session_state.quick_nav
        del st.session_state.quick_nav
    else:
        default_page = "📚 Dashboard"
    
    page = st.sidebar.selectbox(
        "Choose your study mode:",
        ["📚 Dashboard", "🔄 Flashcards", "📝 Mock Tests", "📊 Analytics", "🔴 Live Dashboard", "📋 Summary Sheets", "🔗 Learning Resources", "📖 Documentation"],
        index=["📚 Dashboard", "🔄 Flashcards", "📝 Mock Tests", "📊 Analytics", "🔴 Live Dashboard", "📋 Summary Sheets", "🔗 Learning Resources", "📖 Documentation"].index(default_page) if default_page in ["📚 Dashboard", "🔄 Flashcards", "📝 Mock Tests", "📊 Analytics", "🔴 Live Dashboard", "📋 Summary Sheets", "🔗 Learning Resources", "📖 Documentation"] else 0
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
    elif page == "🔴 Live Dashboard":
        show_live_dashboard()
    elif page == "📋 Summary Sheets":
        show_summary_sheets()
    elif page == "🔗 Learning Resources":
        show_learning_resources()
    elif page == "📖 Documentation":
        show_comprehensive_docs()

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
            st.session_state.quick_nav = "🔄 Flashcards"
            st.rerun()
    
    with col2:
        if st.button("📝 Take Practice Test", use_container_width=True):
            st.session_state.quick_nav = "📝 Mock Tests"
            st.rerun()
    
    with col3:
        if st.button("📊 View Progress", use_container_width=True):
            st.session_state.quick_nav = "📊 Analytics"
            st.rerun()
    
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
    flashcard_items = list(flashcards.items())
    df = pd.DataFrame(flashcard_items, columns=["Term", "Definition"])
    
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

def show_learning_resources():
    st.header("🔗 Learning Resources")
    st.markdown("Comprehensive study materials for Building Effective Agents and Model Context Protocol")
    
    # Building Effective Agents Resources
    st.subheader("📚 Building Effective Agents")
    st.markdown("**Level 2 Certification Exam**: 120 Questions, 3 Hours, Advanced Level")
    
    with st.expander("📖 Study Materials - Building Effective Agents"):
        resources = [
            ("Building Effective Agents Article", "https://www.anthropic.com/engineering/building-effective-agents"),
            ("Workflows and Agents", "https://github.com/panaversity/learn-agentic-ai/tree/main/04_building_effective_agents/01_agents_workflows"),
            ("Building Blocks - LLM Augmentation", "https://github.com/panaversity/learn-agentic-ai/tree/main/04_building_effective_agents/02_building_blocks"),
            ("Design Patterns", "https://github.com/panaversity/learn-agentic-ai/tree/main/04_building_effective_agents/03_design_patterns"),
            ("Agentic Memory, Neo4j AuraDB & Knowledge Graph", "https://github.com/panaversity/learn-agentic-ai/tree/main/04_building_effective_agents/04_augumentation_memory"),
            ("Graphiti Learning Path", "https://github.com/panaversity/learn-agentic-ai/tree/main/04_building_effective_agents/04_augumentation_memory/06_graphiti_learning_path"),
            ("Augmentation Retrieval", "https://github.com/panaversity/learn-agentic-ai/tree/main/04_building_effective_agents/05_augumention_retrival"),
            ("Agentic Payments and Economy", "https://github.com/panaversity/learn-agentic-ai/tree/main/04_building_effective_agents/06_payments_economy")
        ]
        
        for title, url in resources:
            st.markdown(f"- **{title}**: [View Resource]({url})")
    
    # Model Context Protocol Resources
    st.subheader("🔧 Model Context Protocol (MCP)")
    st.markdown("**Level 2 Certification Exam**: 100 Questions, 2 Hours, Advanced Level")
    
    with st.expander("📖 Study Materials - Model Context Protocol"):
        mcp_resources = [
            ("HTTP Theory", "https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/01_http_theory"),
            ("REST Architecture", "https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/02_rest"),
            ("JSON-RPC Protocol", "https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/03_json_rpc"),
            ("Anthropic MCP Fundamentals Course", "https://anthropic.skilljar.com/introduction-to-model-context-protocol"),
            ("MCP Fundamental Primitives", "https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives"),
            ("Anthropic MCP Advanced Course", "https://anthropic.skilljar.com/model-context-protocol-advanced-topics"),
            ("MCP Capabilities and Transport", "https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/05_capabilities_and_transport"),
            ("MCP with OpenAI Agents SDK", "https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/06_openai_agents_sdk_integration")
        ]
        
        for title, url in mcp_resources:
            st.markdown(f"- **{title}**: [View Resource]({url})")
    
    # OpenAI Agents SDK Resources
    st.subheader("🤖 OpenAI Agents SDK")
    st.markdown("**Production-Ready Agent Framework**: Complete toolkit for building agentic AI applications")
    
    with st.expander("📖 Study Materials - OpenAI Agents SDK"):
        openai_resources = [
            ("OpenAI Agents Python Documentation", "https://openai.github.io/openai-agents-python"),
            ("OpenAI Agents GitHub Repository", "https://github.com/openai/openai-agents-python"),
            ("Agents SDK Installation Guide", "https://openai.github.io/openai-agents-python/#installation"),
            ("Hello World Example", "https://openai.github.io/openai-agents-python/#hello-world-example"),
            ("Function Tools Documentation", "https://openai.github.io/openai-agents-python/tools/"),
            ("Multi-Agent Handoffs Guide", "https://openai.github.io/openai-agents-python/handoffs/"),
            ("Guardrails and Validation", "https://openai.github.io/openai-agents-python/guardrails/"),
            ("Session Management", "https://openai.github.io/openai-agents-python/sessions/"),
            ("Tracing and Monitoring", "https://openai.github.io/openai-agents-python/tracing/")
        ]
        
        for title, url in openai_resources:
            st.markdown(f"- **{title}**: [View Resource]({url})")
    
    # Study Plan
    st.subheader("📋 Recommended Study Plan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### For Beginners 🧑‍💻")
        beginner_steps = [
            "Start with **Building Effective Agents** core concepts",
            "Learn **OpenAI Agents SDK** fundamentals and installation",
            "Study **Model Context Protocol (MCP)** basics",
            "Practice **Agent Design Patterns** with examples",
            "Explore **LLM Augmentation** (Retrieval, Tools, Memory)",
            "Implement **Multi-Agent Systems** and handoffs",
            "Master **Knowledge Graphs & Neo4j** integration",
            "Apply **RAG and Retrieval** techniques",
            "Understand **Agentic Payments** and economy integration",
            "Build **Production-Ready** agent applications"
        ]
        
        for i, step in enumerate(beginner_steps, 1):
            st.write(f"{i}. {step}")
    
    with col2:
        st.markdown("### Difficulty Progression 📈")
        from data.study_data import get_difficulty_levels
        difficulty_info = get_difficulty_levels()
        
        for level, description in difficulty_info.items():
            if level == "Normal":
                icon = "🟢"
            elif level == "Intermediate":
                icon = "🟡"
            elif level == "Advanced":
                icon = "🟠"
            elif level == "PhD":
                icon = "🔴"
            else:  # God Level
                icon = "🟣"
            
            st.write(f"{icon} **{level}**: {description}")
    
    # Quick Links
    st.markdown("---")
    st.subheader("🚀 Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📝 Take MCP Quiz", use_container_width=True):
            st.session_state.quick_nav = "📝 Mock Tests"
            st.rerun()
    
    with col2:
        if st.button("🔄 Study Flashcards", use_container_width=True):
            st.session_state.quick_nav = "🔄 Flashcards"
            st.rerun()
    
    with col3:
        if st.button("📊 View Progress", use_container_width=True):
            st.session_state.quick_nav = "📊 Analytics"
            st.rerun()

if __name__ == "__main__":
    main()
