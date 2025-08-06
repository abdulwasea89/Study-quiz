"""
Mock test component for practice exams
"""
import streamlit as st
import time
from datetime import datetime, timedelta
from utils.test_generator import TestGenerator
from utils.progress_tracker import ProgressTracker

def mock_test_system():
    st.header("📝 Mock Test System")
    
    # Initialize test generator
    if 'test_generator' not in st.session_state:
        st.session_state.test_generator = TestGenerator()
    
    # Initialize test session state
    if 'test_session' not in st.session_state:
        st.session_state.test_session = {
            'active': False,
            'questions': [],
            'current_question': 0,
            'answers': {},
            'start_time': None,
            'time_limit': None,
            'session_id': None,
            'test_type': None
        }
    
    test_gen = st.session_state.test_generator
    progress_tracker = st.session_state.progress_tracker
    
    if not st.session_state.test_session['active']:
        _show_test_setup(test_gen, progress_tracker)
    else:
        _show_active_test(test_gen, progress_tracker)

def _show_test_setup(test_gen, progress_tracker):
    """Show test configuration and setup"""
    st.subheader("🎯 Choose Your Test Type")
    
    test_type = st.selectbox(
        "Select test format:",
        ["🎓 Full Mock Test (120 questions)", "📚 Topic-Specific Test", "⚡ Quick Practice (20 questions)", "🎯 Difficulty-Based Test", "🚀 Framework-Based Test", "🧠 PhD-Level Test", "🏆 Certification Test", "🔧 Custom Test"]
    )
    
    if test_type == "🎓 Full Mock Test (120 questions)":
        st.info("Complete practice exam covering all topics with standard distribution")
        
        # Show topic distribution
        st.subheader("Question Distribution by Topic:")
        topics = test_gen.topics
        total_weight = sum(topics.values())
        
        for topic, weight in topics.items():
            percentage = (weight / total_weight) * 100
            st.write(f"• **{topic}**: {weight} questions ({percentage:.1f}%)")
        
        # Time limit
        time_limit = st.selectbox("Time limit:", ["⏰ 2 hours (120 min)", "🚀 1.5 hours (90 min)", "⚡ 1 hour (60 min)", "🔄 No limit"])
        
        if st.button("🚀 Start Full Mock Test", type="primary", use_container_width=True):
            time_minutes = None
            if "120 min" in time_limit:
                time_minutes = 120
            elif "90 min" in time_limit:
                time_minutes = 90
            elif "60 min" in time_limit:
                time_minutes = 60
            
            questions = test_gen.generate_mock_test(120)
            _start_test(questions, time_minutes, "Full Mock Test", progress_tracker)
    
    elif test_type == "📚 Topic-Specific Test":
        st.info("Focus on a specific topic area")
        
        available_topics = test_gen.get_available_topics()
        selected_topic = st.selectbox("Choose topic:", available_topics)
        
        question_count = test_gen.get_topic_question_count(selected_topic)
        max_questions = min(question_count * 3, 30)  # Allow repetition up to 30 questions
        
        num_questions = st.slider(
            f"Number of questions (max {max_questions}):", 
            5, max_questions, min(10, max_questions)
        )
        
        time_limit = st.selectbox("Time limit:", ["⏰ 30 minutes", "🚀 20 minutes", "⚡ 15 minutes", "🔄 No limit"])
        
        if st.button(f"🚀 Start {selected_topic} Test", type="primary", use_container_width=True):
            time_minutes = None
            if "30 minutes" in time_limit:
                time_minutes = 30
            elif "20 minutes" in time_limit:
                time_minutes = 20
            elif "15 minutes" in time_limit:
                time_minutes = 15
            
            questions = test_gen.generate_topic_test(selected_topic, num_questions)
            _start_test(questions, time_minutes, f"{selected_topic} Test", progress_tracker)
    
    elif test_type == "⚡ Quick Practice (20 questions)":
        st.info("Quick practice session with mixed topics")
        
        time_limit = st.selectbox("Time limit:", ["⏰ 20 minutes", "🚀 15 minutes", "⚡ 10 minutes", "🔄 No limit"])
        
        if st.button("🚀 Start Quick Practice", type="primary", use_container_width=True):
            time_minutes = None
            if "20 minutes" in time_limit:
                time_minutes = 20
            elif "15 minutes" in time_limit:
                time_minutes = 15
            elif "10 minutes" in time_limit:
                time_minutes = 10
            
            questions = test_gen.generate_mock_test(20)
            _start_test(questions, time_minutes, "Quick Practice", progress_tracker)
    
    elif test_type == "🎯 Difficulty-Based Test":
        st.info("Test yourself at specific difficulty levels")
        
        available_difficulties = test_gen.get_available_difficulties()
        selected_difficulty = st.selectbox("Choose difficulty level:", available_difficulties)
        
        # Show difficulty description
        difficulty_descriptions = test_gen.difficulty_levels
        if selected_difficulty in difficulty_descriptions:
            st.write(f"**{selected_difficulty}**: {difficulty_descriptions[selected_difficulty]}")
        
        num_questions = st.slider("Number of questions:", 10, 100, 50)
        time_limit = st.selectbox("Time limit:", ["⏰ No limit", f"🚀 {num_questions} minutes", f"⚡ {num_questions//2} minutes"])
        
        if st.button(f"🚀 Start {selected_difficulty} Level Test", type="primary", use_container_width=True):
            time_minutes = None
            if f"{num_questions} minutes" in time_limit:
                time_minutes = num_questions
            elif f"{num_questions//2} minutes" in time_limit:
                time_minutes = num_questions // 2
            
            questions = test_gen.generate_difficulty_test(selected_difficulty, num_questions)
            if questions:
                _start_test(questions, time_minutes, f"{selected_difficulty} Level Test", progress_tracker)
            else:
                st.error(f"No questions available for {selected_difficulty} difficulty level.")
    
    elif test_type == "🚀 Framework-Based Test":
        st.info("Test yourself on specific frameworks with customizable difficulty")
        
        available_frameworks = test_gen.get_available_frameworks()
        selected_framework = st.selectbox("Choose framework:", available_frameworks)
        
        # Show framework description
        framework_descriptions = {
            "Building Effective Agents": "Test your knowledge of agent architecture, design patterns, memory systems, and tool integration",
            "Model Context Protocol (MCP)": "Assess your understanding of MCP fundamentals, transport layers, and protocol implementation",
            "OpenAI Agents SDK": "Evaluate your skills with OpenAI's production-ready agent framework"
        }
        
        if selected_framework in framework_descriptions:
            st.write(f"**{selected_framework}**: {framework_descriptions[selected_framework]}")
        
        col1, col2 = st.columns(2)
        with col1:
            available_difficulties = test_gen.get_available_difficulties()
            selected_difficulty = st.selectbox("Choose difficulty level:", ["All Levels"] + available_difficulties)
        
        with col2:
            num_questions = st.slider("Number of questions:", 10, 100, 50)
        
        time_limit = st.selectbox("Time limit:", ["⏰ No limit", f"🚀 {num_questions} minutes", f"⚡ {num_questions//2} minutes"])
        
        if st.button(f"🚀 Start {selected_framework} Test", type="primary", use_container_width=True):
            time_minutes = None
            if f"{num_questions} minutes" in time_limit:
                time_minutes = num_questions
            elif f"{num_questions//2} minutes" in time_limit:
                time_minutes = num_questions // 2
            
            questions = test_gen.generate_framework_test(selected_framework, selected_difficulty, num_questions)
            if questions:
                test_name = f"{selected_framework} - {selected_difficulty}" if selected_difficulty != "All Levels" else selected_framework
                _start_test(questions, time_minutes, test_name, progress_tracker)
            else:
                st.error(f"No questions available for {selected_framework} with {selected_difficulty} difficulty.")
    
    elif test_type == "🧠 PhD-Level Test":
        st.info("Ultra-detailed questions with comprehensive theoretical depth - PhD level complexity")
        st.warning("⚠️ These questions require deep understanding of theoretical concepts, advanced architectures, and research-level knowledge")
        
        # Framework selection for PhD test
        framework_options = ["All Frameworks", "Building Effective Agents", "Model Context Protocol (MCP)", "OpenAI Agents SDK"]
        selected_framework = st.selectbox("Choose framework focus:", framework_options)
        
        # Difficulty selection
        phd_difficulties = ["PhD", "God Level"]
        selected_difficulty = st.selectbox("Choose difficulty level:", phd_difficulties)
        
        num_questions = st.slider("Number of questions:", 5, 50, 25)
        time_limit = st.selectbox("Time limit:", [
            "⏰ No limit",
            f"🔥 {num_questions * 3} minutes (3 min/question)",
            f"🚀 {num_questions * 2} minutes (2 min/question)"
        ])
        
        # Show sample PhD question complexity
        with st.expander("📖 See PhD Question Complexity Example"):
            st.markdown("""
            **Sample PhD-Level Question:**
            
            "In designing a temporal knowledge graph system like Graphiti for long-term episodic memory in agents, 
            how would you implement efficient temporal reasoning that handles both absolute timestamps and relative 
            temporal relationships, while maintaining causal consistency and enabling counterfactual reasoning?"
            
            **PhD questions test:**
            - Advanced system architecture design
            - Theoretical computer science concepts
            - Research-level implementation details
            - Integration of multiple complex domains
            """)
        
        if st.button(f"🧠 Start PhD-Level Test ({selected_difficulty})", type="primary", use_container_width=True):
            time_minutes = None
            if f"{num_questions * 3} minutes" in time_limit:
                time_minutes = num_questions * 3
            elif f"{num_questions * 2} minutes" in time_limit:
                time_minutes = num_questions * 2
            
            # Generate PhD-level test
            questions = test_gen.generate_phd_test(
                framework=selected_framework.replace(" Frameworks", ""),
                difficulty=selected_difficulty,
                num_questions=num_questions
            )
            
            if questions:
                test_name = f"PhD-Level {selected_framework} ({selected_difficulty})"
                _start_test(questions, time_minutes, test_name, progress_tracker)
            else:
                st.error("PhD-level content not available. Please check that advanced content is loaded.")
    
    elif test_type == "🏆 Certification Test":
        st.info("Comprehensive certification-style tests with progressive difficulty distribution")
        st.success("✨ Includes all difficulty levels: Normal (20%) → Intermediate (25%) → Advanced (25%) → PhD (20%) → God Level (10%)")
        
        # Framework selection
        cert_frameworks = ["Building Effective Agents", "Model Context Protocol (MCP)", "OpenAI Agents SDK"]
        selected_framework = st.selectbox("Choose certification framework:", cert_frameworks)
        
        # Test length options
        test_length_options = {
            "🎯 Standard (60 questions - 90 min)": 60,
            "🔥 Professional (120 questions - 180 min)": 120,  
            "🏆 Expert (180 questions - 270 min)": 180
        }
        
        selected_length = st.selectbox("Choose certification level:", list(test_length_options.keys()))
        num_questions = test_length_options[selected_length]
        
        # Show question distribution
        with st.expander("📊 Question Distribution"):
            st.markdown(f"""
            **Total Questions: {num_questions}**
            - Normal: {int(num_questions * 0.20)} questions (20%) - Foundational concepts
            - Intermediate: {int(num_questions * 0.25)} questions (25%) - Applied knowledge  
            - Advanced: {int(num_questions * 0.25)} questions (25%) - Complex scenarios
            - PhD: {int(num_questions * 0.20)} questions (20%) - Theoretical depth
            - God Level: {int(num_questions * 0.10)} questions (10%) - Research-level mastery
            """)
        
        # Time limit based on question count
        default_time = int(num_questions * 1.5)  # 1.5 minutes per question
        time_options = [
            "⏰ No limit",
            f"🎯 Recommended ({default_time} min - 1.5 min/question)",
            f"🚀 Fast track ({num_questions} min - 1 min/question)"
        ]
        time_limit = st.selectbox("Time limit:", time_options)
        
        if st.button(f"🏆 Start {selected_framework} Certification", type="primary", use_container_width=True):
            time_minutes = None
            if f"Recommended ({default_time} min" in time_limit:
                time_minutes = default_time
            elif f"Fast track ({num_questions} min" in time_limit:
                time_minutes = num_questions
            
            # Generate comprehensive certification test
            questions = test_gen.generate_comprehensive_certification_test(selected_framework, num_questions)
            
            if questions:
                test_name = f"{selected_framework} Certification ({num_questions}Q)"
                _start_test(questions, time_minutes, test_name, progress_tracker)
            else:
                st.error("Could not generate certification test. Please ensure all content is properly loaded.")
    
    else:  # Custom Test
        st.info("Create a custom test with your preferred topic distribution")
        
        st.subheader("Customize Question Distribution:")
        topics = test_gen.get_available_topics()
        custom_distribution = {}
        total_questions = 0
        
        for topic in topics:
            max_for_topic = test_gen.get_topic_question_count(topic) * 2
            num = st.number_input(f"{topic}:", min_value=0, max_value=max_for_topic, value=0, key=f"custom_{topic}")
            if num > 0:
                custom_distribution[topic] = num
                total_questions += num
        
        if total_questions > 0:
            st.write(f"**Total questions: {total_questions}**")
            
            time_options = ["🔄 No limit", f"⏰ {total_questions} minutes", f"🚀 {total_questions//2} minutes"]
            time_limit = st.selectbox("Time limit:", time_options)
            
            if st.button(f"🚀 Start Custom Test ({total_questions} questions)", type="primary", use_container_width=True):
                time_minutes = None
                if f"{total_questions} minutes" in time_limit:
                    time_minutes = total_questions
                elif f"{total_questions//2} minutes" in time_limit:
                    time_minutes = total_questions // 2
                
                questions = test_gen.generate_mock_test(total_questions, custom_distribution)
                _start_test(questions, time_minutes, "Custom Test", progress_tracker)
        else:
            st.warning("Please select at least one question for each topic you want to include.")

def _start_test(questions, time_limit_minutes, test_type, progress_tracker):
    """Start a new test session"""
    session_id = progress_tracker.start_session()
    
    st.session_state.test_session.update({
        'active': True,
        'questions': questions,
        'current_question': 0,
        'answers': {},
        'start_time': datetime.now(),
        'time_limit': timedelta(minutes=time_limit_minutes) if time_limit_minutes else None,
        'session_id': session_id,
        'test_type': test_type
    })
    
    st.rerun()

def _show_active_test(test_gen, progress_tracker):
    """Show the active test interface"""
    session = st.session_state.test_session
    
    # Check time limit
    if session['time_limit']:
        elapsed = datetime.now() - session['start_time']
        remaining = session['time_limit'] - elapsed
        
        if remaining.total_seconds() <= 0:
            st.error("⏰ Time's up! Submitting your test...")
            _submit_test(progress_tracker)
            return
        
        # Show timer
        hours, remainder = divmod(int(remaining.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if hours > 0:
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            time_str = f"{minutes:02d}:{seconds:02d}"
        
        if remaining.total_seconds() < 300:  # Less than 5 minutes
            st.error(f"⏰ Time remaining: {time_str}")
        elif remaining.total_seconds() < 600:  # Less than 10 minutes
            st.warning(f"⏰ Time remaining: {time_str}")
        else:
            st.info(f"⏰ Time remaining: {time_str}")
    
    # Progress
    current_q = session['current_question']
    total_q = len(session['questions'])
    progress = (current_q + 1) / total_q
    
    st.progress(progress, text=f"Question {current_q + 1} of {total_q}")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅️ Previous", disabled=(current_q == 0)):
            session['current_question'] = max(0, current_q - 1)
            st.rerun()
    
    with col3:
        if current_q < total_q - 1:
            if st.button("➡️ Next"):
                session['current_question'] = min(total_q - 1, current_q + 1)
                st.rerun()
        else:
            if st.button("✅ Submit Test", type="primary"):
                _submit_test(progress_tracker)
                return
    
    # Current question
    if current_q < len(session['questions']):
        question = session['questions'][current_q]
        
        st.markdown("---")
        st.markdown(f"### Question {current_q + 1}")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**Topic:** {question['topic']}")
        with col2:
            difficulty = question.get('difficulty', 'Normal')
            if difficulty == "Normal":
                st.markdown("🟢 **Normal**")
            elif difficulty == "Intermediate":
                st.markdown("🟡 **Intermediate**")
            elif difficulty == "Advanced":
                st.markdown("🟠 **Advanced**")
            elif difficulty == "PhD":
                st.markdown("🔴 **PhD**")
            else:  # God Level
                st.markdown("🟣 **God Level**")
        
        st.markdown(f"{question['question']}")
        
        # Answer options
        options = question['options']
        current_answer = session['answers'].get(current_q)
        
        selected = st.radio(
            "Select your answer:",
            options,
            index=current_answer if current_answer is not None else None,
            key=f"question_{current_q}"
        )
        
        # Save answer
        if selected:
            session['answers'][current_q] = options.index(selected)
    
    # Question navigation grid
    st.markdown("---")
    st.subheader("Quick Navigation")
    
    # Create grid of question buttons
    cols_per_row = 10
    questions = session['questions']
    
    for row_start in range(0, len(questions), cols_per_row):
        cols = st.columns(cols_per_row)
        for i in range(cols_per_row):
            q_idx = row_start + i
            if q_idx < len(questions):
                with cols[i]:
                    # Determine button style based on status
                    if q_idx == current_q:
                        button_type = "primary"
                        label = f"🎯{q_idx + 1}"
                    elif q_idx in session['answers']:
                        button_type = "secondary"
                        label = f"✅{q_idx + 1}"
                    else:
                        button_type = None
                        label = f"{q_idx + 1}"
                    
                    button_kwargs = {"key": f"nav_{q_idx}", "use_container_width": True}
                    if button_type:
                        button_kwargs["type"] = button_type
                    
                    if st.button(label, **button_kwargs):
                        session['current_question'] = q_idx
                        st.rerun()
    
    # Summary
    answered = len(session['answers'])
    unanswered = total_q - answered
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Answered", answered)
    with col2:
        st.metric("Remaining", unanswered)

def _submit_test(progress_tracker):
    """Submit the test and show results"""
    session = st.session_state.test_session
    questions = session['questions']
    answers = session['answers']
    
    # Calculate score
    correct_answers = 0
    total_questions = len(questions)
    topic_performance = {}
    
    for i, question in enumerate(questions):
        user_answer = answers.get(i)
        correct_answer = question['correct']
        topic = question['topic']
        
        if topic not in topic_performance:
            topic_performance[topic] = {'correct': 0, 'total': 0}
        
        topic_performance[topic]['total'] += 1
        
        if user_answer is not None and user_answer == correct_answer:
            correct_answers += 1
            topic_performance[topic]['correct'] += 1
    
    # Calculate overall score
    score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    
    # Record results
    for topic, perf in topic_performance.items():
        topic_score = (perf['correct'] / perf['total']) * 100 if perf['total'] > 0 else 0
        progress_tracker.record_test_result(
            session['session_id'],
            topic,
            topic_score,
            perf['total'],
            perf['correct']
        )
    
    # Update current session stats
    st.session_state.current_study_session['tests_taken'] += 1
    st.session_state.current_study_session['correct_answers'] += correct_answers
    st.session_state.current_study_session['total_questions'] += total_questions
    
    # End session
    progress_tracker.end_session(session['session_id'])
    
    # Show results
    st.success("🎉 Test Completed!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Overall Score", f"{score:.1f}%")
    with col2:
        st.metric("Correct Answers", f"{correct_answers}/{total_questions}")
    with col3:
        elapsed = datetime.now() - session['start_time']
        minutes = int(elapsed.total_seconds() / 60)
        st.metric("Time Taken", f"{minutes} minutes")
    
    # Topic breakdown
    st.subheader("📊 Performance by Topic")
    for topic, perf in topic_performance.items():
        topic_score = (perf['correct'] / perf['total']) * 100 if perf['total'] > 0 else 0
        st.write(f"**{topic}**: {perf['correct']}/{perf['total']} ({topic_score:.1f}%)")
    
    # Detailed review
    if st.checkbox("📝 Show detailed review"):
        st.subheader("Question Review")
        
        for i, question in enumerate(questions):
            user_answer = answers.get(i)
            correct_answer = question['correct']
            is_correct = user_answer is not None and user_answer == correct_answer
            
            with st.expander(f"Question {i + 1} {'✅' if is_correct else '❌'}"):
                st.write(f"**Topic:** {question['topic']}")
                st.write(f"**Question:** {question['question']}")
                
                for j, option in enumerate(question['options']):
                    if j == correct_answer:
                        st.write(f"✅ {option} (Correct Answer)")
                    elif j == user_answer:
                        st.write(f"❌ {option} (Your Answer)")
                    else:
                        st.write(f"• {option}")
                
                if 'explanation' in question:
                    st.info(f"**Explanation:** {question['explanation']}")
    
    # Reset test session
    if st.button("🔄 Take Another Test", use_container_width=True):
        st.session_state.test_session = {
            'active': False,
            'questions': [],
            'current_question': 0,
            'answers': {},
            'start_time': None,
            'time_limit': None,
            'session_id': None,
            'test_type': None
        }
        st.rerun()
