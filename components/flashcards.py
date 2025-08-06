"""
Flashcard study component with spaced repetition
"""
import streamlit as st
import random
from datetime import datetime
from data.study_data import get_flashcards
from utils.progress_tracker import ProgressTracker

def flashcard_system():
    st.header("🔄 Flashcard Study System")
    
    # Initialize session state for flashcard study
    if 'flashcard_session' not in st.session_state:
        st.session_state.flashcard_session = {
            'active': False,
            'current_card': None,
            'cards_to_study': [],
            'cards_studied': 0,
            'correct_count': 0,
            'show_answer': False,
            'session_id': None
        }
    
    flashcards = get_flashcards()
    progress_tracker = st.session_state.progress_tracker
    
    # Study mode selection
    study_mode = st.selectbox(
        "Choose study mode:",
        ["📅 Spaced Repetition (Recommended)", "🔀 Random Review", "📚 All Cards", "🎯 Custom Selection"]
    )
    
    # Get cards based on study mode
    if study_mode == "📅 Spaced Repetition (Recommended)":
        st.info("Studying cards that are due for review based on your performance")
        cards_to_study = progress_tracker.get_flashcards_for_review(20)
        
        # If no cards are due, add some random ones
        if not cards_to_study:
            st.warning("No cards are due for review! Adding some random cards for practice.")
            all_terms = list(flashcards.keys())
            cards_to_study = random.sample(all_terms, min(10, len(all_terms)))
    
    elif study_mode == "🔀 Random Review":
        num_cards = st.slider("Number of cards to study:", 5, len(flashcards), 10)
        all_terms = list(flashcards.keys())
        cards_to_study = random.sample(all_terms, min(num_cards, len(all_terms)))
    
    elif study_mode == "📚 All Cards":
        cards_to_study = list(flashcards.keys())
        st.info(f"Studying all {len(cards_to_study)} flashcards")
    
    else:  # Custom Selection
        st.subheader("Select cards to study:")
        selected_terms = []
        
        # Create checkboxes for each flashcard
        cols = st.columns(2)
        for i, term in enumerate(flashcards.keys()):
            with cols[i % 2]:
                if st.checkbox(term, key=f"card_select_{i}"):
                    selected_terms.append(term)
        
        cards_to_study = selected_terms
        
        if not cards_to_study:
            st.warning("Please select at least one card to study.")
            return
    
    # Start study session button
    if not st.session_state.flashcard_session['active'] and cards_to_study:
        if st.button("🚀 Start Studying", type="primary", use_container_width=True):
            # Start new session
            session_id = progress_tracker.start_session()
            
            st.session_state.flashcard_session.update({
                'active': True,
                'cards_to_study': cards_to_study.copy(),
                'current_card': None,
                'cards_studied': 0,
                'correct_count': 0,
                'show_answer': False,
                'session_id': session_id
            })
            
            # Shuffle the cards
            random.shuffle(st.session_state.flashcard_session['cards_to_study'])
            st.rerun()
    
    # Active study session
    if st.session_state.flashcard_session['active']:
        session = st.session_state.flashcard_session
        
        # Progress bar
        total_cards = len(cards_to_study)
        progress = session['cards_studied'] / total_cards if total_cards > 0 else 0
        st.progress(progress, text=f"Progress: {session['cards_studied']}/{total_cards} cards")
        
        # Display current card
        if session['cards_to_study']:
            if session['current_card'] is None:
                session['current_card'] = session['cards_to_study'].pop(0)
            
            current_term = session['current_card']
            current_definition = flashcards[current_term]
            
            # Card display
            st.markdown("---")
            
            if not session['show_answer']:
                # Show term, hide definition
                st.markdown(f"### 📝 Term:")
                st.markdown(f"**{current_term}**")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💡 Show Answer", use_container_width=True):
                        session['show_answer'] = True
                        st.rerun()
                
                with col2:
                    if st.button("⏭️ Skip Card", use_container_width=True):
                        # Record as incorrect and move to next
                        progress_tracker.record_flashcard_study(
                            session['session_id'], 
                            current_term, 
                            False
                        )
                        _next_card()
            
            else:
                # Show both term and definition
                st.markdown(f"### 📝 Term:")
                st.markdown(f"**{current_term}**")
                
                st.markdown(f"### 💡 Definition:")
                st.info(current_definition)
                
                st.markdown("### How well did you know this?")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if st.button("❌ Didn't Know", use_container_width=True, type="secondary"):
                        progress_tracker.record_flashcard_study(
                            session['session_id'], 
                            current_term, 
                            False
                        )
                        _next_card()
                
                with col2:
                    if st.button("🤔 Partially Knew", use_container_width=True):
                        progress_tracker.record_flashcard_study(
                            session['session_id'], 
                            current_term, 
                            False
                        )
                        _next_card()
                
                with col3:
                    if st.button("✅ Knew It!", use_container_width=True, type="primary"):
                        progress_tracker.record_flashcard_study(
                            session['session_id'], 
                            current_term, 
                            True
                        )
                        session['correct_count'] += 1
                        _next_card()
        
        else:
            # Session complete
            _complete_session()
    
    # Display study statistics
    if not st.session_state.flashcard_session['active']:
        st.markdown("---")
        st.subheader("📊 Your Flashcard Progress")
        
        stats = progress_tracker.get_overall_stats()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Cards Studied", stats['total_flashcards_studied'])
        with col2:
            st.metric("Study Sessions", stats['total_sessions'])
        with col3:
            st.metric("Study Streak", f"{stats['study_streak']} days")

def _next_card():
    """Move to the next flashcard"""
    session = st.session_state.flashcard_session
    session['cards_studied'] += 1
    session['current_card'] = None
    session['show_answer'] = False
    
    # Update current session stats
    st.session_state.current_study_session['flashcards_studied'] += 1
    
    st.rerun()

def _complete_session():
    """Complete the flashcard study session"""
    session = st.session_state.flashcard_session
    progress_tracker = st.session_state.progress_tracker
    
    # End the session
    progress_tracker.end_session(session['session_id'])
    
    # Show completion message
    st.success("🎉 Study Session Complete!")
    
    accuracy = (session['correct_count'] / session['cards_studied']) * 100 if session['cards_studied'] > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Cards Studied", session['cards_studied'])
    with col2:
        st.metric("Known Cards", session['correct_count'])
    with col3:
        st.metric("Accuracy", f"{accuracy:.1f}%")
    
    if st.button("🔄 Study More Cards", use_container_width=True):
        st.session_state.flashcard_session['active'] = False
        st.rerun()
    
    # Reset session
    st.session_state.flashcard_session = {
        'active': False,
        'current_card': None,
        'cards_to_study': [],
        'cards_studied': 0,
        'correct_count': 0,
        'show_answer': False,
        'session_id': None
    }
