# Overview

The Agentic AI Study Hub is a comprehensive learning platform built with Streamlit that helps users study artificial intelligence concepts, focusing on both Building Effective Agents and Model Context Protocol (MCP). The application provides an interactive study experience through flashcards, mock tests with multiple difficulty levels, analytics tracking, summary sheets, and learning resources. It supports different learning modes including spaced repetition, random review, and structured testing with progress tracking capabilities. The platform now includes 5 difficulty levels (Normal, Intermediate, Advanced, PhD, God Level) and comprehensive MCP certification content.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
The application uses Streamlit as the primary web framework, providing a multi-page interface with sidebar navigation. The main entry point (`app.py`) orchestrates the entire application flow and manages session state across different study modes. The interface is organized into distinct study modes: Dashboard, Flashcards, Mock Tests, Analytics, Summary Sheets, Learning Resources, and comprehensive Documentation with framework selection capabilities.

## Component-Based Design
The system follows a modular component architecture with separate modules for different functionalities:

- **Flashcard System** (`components/flashcards.py`): Implements spaced repetition learning with multiple study modes including random review, full deck study, and custom selection
- **Mock Test System** (`components/mock_test.py`): Provides comprehensive testing capabilities with full mock exams, topic-specific tests, difficulty-based tests, framework-based tests, and quick practice sessions
- **Analytics Dashboard** (`components/analytics.py`): Tracks and visualizes learning progress with performance metrics and study streaks
- **Test Generator** (`utils/test_generator.py`): Handles dynamic test creation with customizable question distribution across topics, frameworks, and difficulty levels
- **Documentation System** (`components/documentation.py`): Comprehensive knowledge base covering Building Effective Agents, Model Context Protocol, and OpenAI Agents SDK with framework and difficulty filtering

## Data Management
The application uses a file-based data storage approach with JSON for persistence:

- **Static Study Content**: Flashcards and topic definitions are stored in `data/study_data.py` as Python dictionaries
- **Progress Tracking**: User progress, session data, and performance metrics are managed through the `ProgressTracker` class with JSON file persistence
- **Session State**: Streamlit's session state manages temporary data for active study sessions, current flashcard progress, and test states

## Learning Algorithm Implementation
The system implements spaced repetition algorithms for optimized learning:

- **Adaptive Scheduling**: Cards are scheduled for review based on user performance and retention patterns
- **Performance Analytics**: Tracks correct/incorrect responses, study streaks, and topic-specific performance
- **Personalized Study Paths**: Recommends content based on individual progress and weak areas

## Test Generation System
The mock test functionality provides flexible assessment options:

- **Dynamic Question Selection**: Generates tests with configurable question distribution across AI topics
- **Multiple Test Formats**: Supports full mock exams (120 questions), topic-specific tests, quick practice sessions, and custom configurations
- **Performance Evaluation**: Tracks test results and provides detailed analytics on topic-wise performance

# External Dependencies

## Core Framework
- **Streamlit**: Primary web application framework for building the interactive interface
- **Pandas**: Data manipulation and analysis for handling study data and progress metrics
- **Plotly**: Interactive visualization library for analytics charts and progress graphs

## Utility Libraries
- **JSON**: Built-in Python module for data persistence and configuration management
- **DateTime**: Built-in Python module for session timing, progress tracking, and scheduling
- **Random**: Built-in Python module for question shuffling and random study mode selection
- **OS**: Built-in Python module for file system operations and data persistence

## Development Tools
- **caas_jupyter_tools**: Development utility for data display during prototyping (referenced in attached assets)

The application is designed to be self-contained with minimal external dependencies, focusing on local data storage and computation rather than cloud services or external APIs.