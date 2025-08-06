"""
Live Dashboard Component with Real-Time Updates and Accurate Information
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import time

def live_performance_dashboard():
    """Live dashboard with real-time performance metrics"""
    st.subheader("🔴 Live Performance Dashboard")
    
    # Real-time status indicator
    status_col1, status_col2, status_col3 = st.columns([1, 1, 2])
    
    with status_col1:
        st.markdown("🟢 **Live Status**: Active")
    
    with status_col2:
        st.markdown(f"⏰ **Last Update**: {datetime.now().strftime('%H:%M:%S')}")
    
    with status_col3:
        if st.button("🔄 Force Refresh", help="Manually refresh all live data"):
            st.rerun()
    
    # Get real-time data from session state
    progress_tracker = st.session_state.get('progress_tracker')
    if not progress_tracker:
        st.warning("No data available. Start studying to see live metrics!")
        return
    
    # Live metrics display
    current_stats = progress_tracker.get_current_session_stats()
    
    # Real-time metrics row
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.metric(
            label="Session Duration",
            value=f"{current_stats.get('duration', 0):.1f} min",
            delta=f"+{current_stats.get('delta_duration', 0):.1f}",
            help="Current study session time"
        )
    
    with metric_col2:
        st.metric(
            label="Questions Answered",
            value=current_stats.get('questions_answered', 0),
            delta=current_stats.get('delta_questions', 0),
            help="Questions answered in current session"
        )
    
    with metric_col3:
        current_accuracy = current_stats.get('current_accuracy', 0)
        st.metric(
            label="Current Accuracy",
            value=f"{current_accuracy:.1f}%",
            delta=f"{current_stats.get('delta_accuracy', 0):+.1f}%",
            help="Accuracy in current session"
        )
    
    with metric_col4:
        streak = current_stats.get('correct_streak', 0)
        st.metric(
            label="Correct Streak",
            value=streak,
            delta=current_stats.get('delta_streak', 0),
            help="Current streak of correct answers"
        )
    
    # Live progress visualization
    st.markdown("### 📈 Live Progress Visualization")
    
    # Create real-time performance chart
    session_data = progress_tracker.get_live_session_data()
    if session_data:
        df = pd.DataFrame(session_data)
        
        # Live accuracy trend
        fig_live = go.Figure()
        fig_live.add_trace(go.Scatter(
            x=df.index,
            y=df['accuracy'],
            mode='lines+markers',
            name='Live Accuracy',
            line=dict(color='#00ff00', width=3),
            marker=dict(size=6)
        ))
        
        # Add moving average
        if len(df) >= 5:
            df['moving_avg'] = df['accuracy'].rolling(window=5).mean()
            fig_live.add_trace(go.Scatter(
                x=df.index,
                y=df['moving_avg'],
                mode='lines',
                name='5-Question Average',
                line=dict(color='#ff6600', width=2, dash='dash')
            ))
        
        fig_live.update_layout(
            title='Real-Time Accuracy Tracking',
            title_x=0.5,
            xaxis_title='Question Number',
            yaxis_title='Accuracy (%)',
            plot_bgcolor='rgba(0,0,0,0.05)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400
        )
        
        st.plotly_chart(fig_live, use_container_width=True, key="live_accuracy")
    
    # Framework performance comparison
    st.markdown("### 🎯 Framework Performance Comparison (Real-Time)")
    
    framework_data = progress_tracker.get_framework_performance()
    if framework_data:
        df_frameworks = pd.DataFrame(framework_data)
        
        # Create radar chart for framework comparison
        frameworks = df_frameworks['framework'].tolist()
        scores = df_frameworks['average_score'].tolist()
        
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=scores,
            theta=frameworks,
            fill='toself',
            name='Performance',
            line_color='rgb(0, 120, 255)',
            fillcolor='rgba(0, 120, 255, 0.2)'
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            title='Framework Performance Radar',
            title_x=0.5,
            height=500
        )
        
        st.plotly_chart(fig_radar, use_container_width=True, key="framework_radar")
        
        # Framework comparison table
        st.dataframe(
            df_frameworks,
            use_container_width=True,
            column_config={
                "framework": "Framework",
                "average_score": st.column_config.ProgressColumn(
                    "Average Score",
                    help="Average score for this framework",
                    min_value=0,
                    max_value=100,
                    format="%.1f%%"
                ),
                "questions_answered": "Questions",
                "best_score": "Best Score (%)"
            }
        )

def real_time_difficulty_analysis():
    """Real-time analysis of performance across difficulty levels"""
    st.markdown("### 🎚️ Difficulty Level Performance (Live)")
    
    progress_tracker = st.session_state.get('progress_tracker')
    if not progress_tracker:
        return
    
    difficulty_data = progress_tracker.get_difficulty_performance()
    if difficulty_data:
        df_diff = pd.DataFrame(difficulty_data)
        
        # Create difficulty progression chart
        fig_diff = px.bar(
            df_diff,
            x='difficulty',
            y='average_score',
            color='average_score',
            color_continuous_scale='Viridis',
            title='Performance by Difficulty Level',
            text='average_score'
        )
        
        fig_diff.update_traces(
            texttemplate='%{text:.1f}%',
            textposition='outside'
        )
        
        fig_diff.update_layout(
            title_x=0.5,
            xaxis_title='Difficulty Level',
            yaxis_title='Average Score (%)',
            showlegend=False
        )
        
        st.plotly_chart(fig_diff, use_container_width=True, key="difficulty_analysis")
        
        # Difficulty recommendations
        st.markdown("#### 💡 Personalized Recommendations")
        
        recommendations = progress_tracker.get_difficulty_recommendations()
        for rec in recommendations:
            if rec['type'] == 'focus':
                st.info(f"🎯 **Focus Area**: {rec['message']}")
            elif rec['type'] == 'challenge':
                st.success(f"🚀 **Ready for Challenge**: {rec['message']}")
            elif rec['type'] == 'review':
                st.warning(f"📚 **Review Needed**: {rec['message']}")

def study_session_timeline():
    """Live timeline of current study session"""
    st.markdown("### ⏱️ Current Session Timeline")
    
    progress_tracker = st.session_state.get('progress_tracker')
    if not progress_tracker:
        return
    
    timeline_data = progress_tracker.get_session_timeline()
    if timeline_data:
        # Create timeline visualization
        df_timeline = pd.DataFrame(timeline_data)
        
        fig_timeline = px.timeline(
            df_timeline,
            x_start='start_time',
            x_end='end_time',
            y='activity',
            color='result',
            title='Study Session Activity Timeline',
            hover_data=['details']
        )
        
        fig_timeline.update_layout(
            title_x=0.5,
            height=300,
            xaxis_title='Time',
            yaxis_title='Activity'
        )
        
        st.plotly_chart(fig_timeline, use_container_width=True, key="session_timeline")

def show_live_dashboard():
    """Main function to display the complete live dashboard"""
    st.header("🔴 Live Analytics Dashboard")
    st.markdown("Real-time performance tracking with accurate, up-to-date information")
    
    # Add tabs for different live views
    tab1, tab2, tab3 = st.tabs(["📊 Live Metrics", "🎯 Difficulty Analysis", "⏱️ Session Timeline"])
    
    with tab1:
        live_performance_dashboard()
    
    with tab2:
        real_time_difficulty_analysis()
    
    with tab3:
        study_session_timeline()
    
    # Auto-refresh every 30 seconds if enabled
    if st.session_state.get('auto_refresh_enabled', False):
        time.sleep(30)
        st.rerun()