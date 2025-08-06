"""
Analytics and progress tracking component
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from utils.progress_tracker import ProgressTracker

def analytics_dashboard():
    st.header("📊 Analytics Dashboard")
    
    progress_tracker = st.session_state.progress_tracker
    
    # Overall statistics
    stats = progress_tracker.get_overall_stats()
    
    st.subheader("📈 Overall Performance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Study Sessions",
            stats['total_sessions'],
            help="Total number of completed study sessions"
        )
    
    with col2:
        st.metric(
            "Flashcards Studied",
            stats['total_flashcards_studied'],
            help="Total flashcards reviewed across all sessions"
        )
    
    with col3:
        st.metric(
            "Tests Taken",
            stats['total_tests_taken'],
            help="Total number of practice tests completed"
        )
    
    with col4:
        st.metric(
            "Study Streak",
            f"{stats['study_streak']} days",
            help="Current consecutive days of studying"
        )
    
    # Study time and performance metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Total Study Time",
            f"{stats['total_study_time']:.1f} hours",
            help="Total time spent in study sessions"
        )
    
    with col2:
        if stats['total_tests_taken'] > 0:
            st.metric(
                "Average Test Score",
                f"{stats['average_test_score']:.1f}%",
                help="Average score across all tests"
            )
        else:
            st.metric("Average Test Score", "No tests yet")
    
    with col3:
        if stats['total_tests_taken'] > 0:
            st.metric(
                "Best Test Score",
                f"{stats['best_test_score']:.1f}%",
                help="Highest score achieved on any test"
            )
        else:
            st.metric("Best Test Score", "No tests yet")
    
    # Topic Performance Analysis
    st.markdown("---")
    st.subheader("🎯 Topic Performance Analysis")
    
    topic_data = []
    for topic, perf in progress_tracker.data.get('topic_performance', {}).items():
        if perf['total_tests'] > 0:
            avg_score = perf['total_score'] / perf['total_tests']
            topic_data.append({
                'Topic': topic,
                'Average Score': avg_score,
                'Best Score': perf['best_score'],
                'Tests Taken': perf['total_tests'],
                'Improvement Trend': perf['improvement_trend']
            })
    
    if topic_data:
        df_topics = pd.DataFrame(topic_data)
        
        # Topic performance chart
        fig_topics = px.bar(
            df_topics,
            x='Topic',
            y='Average Score',
            title='Average Score by Topic',
            text='Average Score',
            color='Average Score',
            color_continuous_scale='RdYlGn'
        )
        fig_topics.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig_topics.update_layout(showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig_topics, use_container_width=True)
        
        # Improvement trends
        st.subheader("📈 Improvement Trends")
        
        # Create improvement indicator
        for _, row in df_topics.iterrows():
            trend = row['Improvement Trend']
            trend_icon = "📈" if trend > 0 else "📉" if trend < 0 else "➡️"
            trend_text = f"+{trend:.1f}%" if trend > 0 else f"{trend:.1f}%" if trend < 0 else "No change"
            
            st.write(f"{trend_icon} **{row['Topic']}**: {trend_text} ({row['Tests Taken']} tests)")
    
    else:
        st.info("Take some tests to see topic performance analysis!")
    
    # Study Progress Over Time
    st.markdown("---")
    st.subheader("📅 Study Progress Over Time")
    
    sessions = progress_tracker.get_all_sessions()
    if sessions:
        # Prepare data for time series
        session_data = []
        for session in sessions:
            if session.get('end_time'):
                date = datetime.fromisoformat(session['start_time']).date()
                session_data.append({
                    'Date': date,
                    'Duration': session.get('duration', 0),
                    'Flashcards': session.get('flashcards_studied', 0),
                    'Tests': session.get('tests_taken', 0)
                })
        
        if session_data:
            df_sessions = pd.DataFrame(session_data)
            
            # Group by date and sum
            daily_stats = df_sessions.groupby('Date').agg({
                'Duration': 'sum',
                'Flashcards': 'sum',
                'Tests': 'sum'
            }).reset_index()
            
            # Study time over time
            fig_time = px.line(
                daily_stats,
                x='Date',
                y='Duration',
                title='Daily Study Time (minutes)',
                markers=True
            )
            st.plotly_chart(fig_time, use_container_width=True)
            
            # Activity heatmap
            col1, col2 = st.columns(2)
            
            with col1:
                fig_flashcards = px.bar(
                    daily_stats.tail(14),  # Last 14 days
                    x='Date',
                    y='Flashcards',
                    title='Flashcards Studied (Last 14 Days)'
                )
                st.plotly_chart(fig_flashcards, use_container_width=True)
            
            with col2:
                fig_tests = px.bar(
                    daily_stats.tail(14),  # Last 14 days
                    x='Date',
                    y='Tests',
                    title='Tests Taken (Last 14 Days)'
                )
                st.plotly_chart(fig_tests, use_container_width=True)
    
    else:
        st.info("Start studying to see your progress over time!")
    
    # Test Results Timeline
    st.markdown("---")
    st.subheader("📝 Test Results Timeline")
    
    test_results = progress_tracker.data.get('test_results', [])
    if test_results:
        # Prepare test results data
        results_data = []
        for result in test_results:
            date = datetime.fromisoformat(result['date'])
            results_data.append({
                'Date': date,
                'Topic': result['topic'],
                'Score': result['score'],
                'Accuracy': result['accuracy']
            })
        
        df_results = pd.DataFrame(results_data)
        
        # Score progression over time
        fig_progression = px.scatter(
            df_results,
            x='Date',
            y='Score',
            color='Topic',
            title='Test Score Progression',
            hover_data=['Accuracy']
        )
        st.plotly_chart(fig_progression, use_container_width=True)
        
        # Recent test results table
        st.subheader("📋 Recent Test Results")
        recent_results = df_results.tail(10).sort_values('Date', ascending=False)
        
        st.dataframe(
            recent_results[['Date', 'Topic', 'Score', 'Accuracy']],
            use_container_width=True,
            hide_index=True,
            column_config={
                'Date': st.column_config.DatetimeColumn('Date', format='MMM DD, YYYY HH:mm'),
                'Score': st.column_config.NumberColumn('Score (%)', format='%.1f'),
                'Accuracy': st.column_config.NumberColumn('Accuracy (%)', format='%.1f')
            }
        )
    
    else:
        st.info("Take some tests to see your results timeline!")
    
    # Flashcard Review Analytics
    st.markdown("---")
    st.subheader("🔄 Flashcard Review Analytics")
    
    flashcard_stats = progress_tracker.data.get('flashcard_stats', {})
    if flashcard_stats:
        # Prepare flashcard data
        card_data = []
        for term, stats in flashcard_stats.items():
            accuracy = (stats['times_correct'] / stats['times_studied']) * 100 if stats['times_studied'] > 0 else 0
            card_data.append({
                'Term': term,
                'Times Studied': stats['times_studied'],
                'Times Correct': stats['times_correct'],
                'Accuracy': accuracy,
                'Difficulty Level': stats['difficulty_level']
            })
        
        df_cards = pd.DataFrame(card_data)
        
        # Cards needing review
        now = datetime.now()
        due_cards = []
        
        for term, stats in flashcard_stats.items():
            if stats.get('next_review'):
                next_review = datetime.fromisoformat(stats['next_review'])
                if next_review <= now:
                    due_cards.append(term)
        
        st.info(f"📅 {len(due_cards)} flashcards are due for review")
        
        # Flashcard performance distribution
        fig_cards = px.histogram(
            df_cards,
            x='Accuracy',
            nbins=10,
            title='Flashcard Accuracy Distribution',
            labels={'count': 'Number of Cards'}
        )
        st.plotly_chart(fig_cards, use_container_width=True)
        
        # Most challenging cards
        challenging_cards = df_cards[df_cards['Accuracy'] < 70].sort_values('Accuracy', ascending=True)
        
        if not challenging_cards.empty:
            st.subheader("🎯 Cards That Need More Practice")
            st.dataframe(
                challenging_cards[['Term', 'Accuracy', 'Times Studied']].head(10),
                use_container_width=True,
                hide_index=True,
                column_config={
                    'Accuracy': st.column_config.NumberColumn('Accuracy (%)', format='%.1f')
                }
            )
    
    else:
        st.info("Study some flashcards to see review analytics!")
    
    # Export functionality
    st.markdown("---")
    st.subheader("📤 Export Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Export Progress Data", use_container_width=True):
            # Create comprehensive progress report
            progress_data = {
                'overall_stats': stats,
                'topic_performance': progress_tracker.data.get('topic_performance', {}),
                'recent_sessions': progress_tracker.get_recent_sessions(20),
                'test_results': test_results[-20:] if test_results else [],
                'flashcard_stats': flashcard_stats
            }
            
            import json
            progress_json = json.dumps(progress_data, indent=2, default=str)
            st.download_button(
                label="📥 Download Progress Report (JSON)",
                data=progress_json,
                file_name=f"agentic_ai_progress_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
    
    with col2:
        if test_results:
            df_export = pd.DataFrame(test_results)
            csv = df_export.to_csv(index=False)
            
            st.download_button(
                label="📥 Download Test Results (CSV)",
                data=csv,
                file_name=f"test_results_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
