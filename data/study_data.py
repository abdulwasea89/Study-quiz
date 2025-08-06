"""
Study data module containing flashcards, topics, and summary information
"""

def get_topics():
    """Return the topics and their estimated number of questions for mock tests"""
    return {
        "Workflows vs Agents": 15,
        "LLM Augmentation": 20,
        "Design Patterns": 25,
        "Agentic Memory & Knowledge Graphs": 20,
        "Graphiti": 10,
        "Augmentation Retrieval": 15,
        "Agentic Payments & Economy": 15,
    }

def get_flashcards():
    """Return flashcard term-definition pairs"""
    return {
        "RAG (Retrieval-Augmented Generation)": "Combines retrieval from external sources with LLM generation to produce grounded responses.",
        "Planner-Worker Pattern": "A design pattern where a planner agent creates and delegates subtasks to worker agents.",
        "MERGE in Cypher": "Creates a node if it does not exist, avoids duplication in knowledge graphs.",
        "Graphiti": "A tool that tracks events, builds ontologies, and supports temporal knowledge graphs from unstructured data.",
        "Tool Use in Agents": "Allows LLMs to perform actions like API calls, database queries, or file manipulations.",
        "Semantic Search": "Search technique using vector similarity based on meaning rather than exact keyword matching.",
        "Agentic Economy": "Concept where autonomous agents participate in economic activities via APIs, often securely through protocols like MCP.",
        "Vector Embeddings": "Numerical representations of text that capture semantic meaning for similarity comparisons.",
        "Knowledge Graph": "A structured representation of entities and their relationships, often used for semantic reasoning.",
        "Multi-Agent Systems": "Systems where multiple autonomous agents interact to solve complex problems collaboratively.",
        "Prompt Engineering": "The practice of designing effective prompts to guide LLM behavior and outputs.",
        "Chain of Thought": "A reasoning technique where LLMs break down complex problems into step-by-step thinking.",
        "Few-Shot Learning": "Training approach where models learn from a small number of examples.",
        "Retrieval Systems": "Components that find and return relevant information from large datasets or knowledge bases.",
        "Agent Memory": "Persistent storage systems that allow agents to remember past interactions and learnings.",
        "Tool Calling": "The ability of LLMs to invoke external functions, APIs, or services during conversation.",
        "Reflection Pattern": "Design pattern where agents evaluate their own outputs and reasoning processes.",
        "Delegation Pattern": "Architectural approach where higher-level agents assign tasks to specialized sub-agents.",
        "Evaluation Metrics": "Quantitative measures used to assess agent performance and response quality.",
        "Safety Mechanisms": "Built-in controls to prevent harmful or unintended agent behaviors."
    }

def get_summary_data():
    """Return summary data for creating reference sheets"""
    return {
        "Components of Agentic Systems": ["Retrieval", "Tools", "Memory", "Planning", "Execution", "Evaluation"],
        "Common Agent Design Patterns": ["Routing", "Prompt Chaining", "Parallelization", "Planner-Worker", "Evaluator-Optimizer", "Reflection", "Delegation"],
        "Memory Tools": ["Neo4j", "Graphiti", "Vector Databases", "Knowledge Graphs", "Temporal Storage"],
        "Agent Capabilities": ["Search", "Tool Use", "Reflection", "Delegation", "Learning", "Adaptation"],
        "Secure Economy Integration": ["Stripe API", "MCP Tool Call", "User Trust Mechanisms", "Authentication", "Authorization"],
        "LLM Augmentation Techniques": ["RAG", "Fine-tuning", "Prompt Engineering", "Chain of Thought", "Few-shot Learning"],
        "Evaluation Approaches": ["Human Feedback", "Automated Metrics", "A/B Testing", "Performance Benchmarks"]
    }

def get_questions_by_topic():
    """Return sample questions organized by topic for mock tests"""
    return {
        "Workflows vs Agents": [
            {
                "question": "What is the main difference between workflows and agents?",
                "options": ["Workflows are static, agents are dynamic", "Workflows are faster", "Agents cannot use tools", "No difference"],
                "correct": 0,
                "explanation": "Workflows follow predefined paths while agents make dynamic decisions based on context."
            },
            {
                "question": "Which approach is better for unpredictable tasks?",
                "options": ["Workflows", "Agents", "Both equally", "Neither"],
                "correct": 1,
                "explanation": "Agents can adapt to unpredictable situations better than rigid workflows."
            },
            {
                "question": "What is a key advantage of workflow-based systems?",
                "options": ["Flexibility", "Predictability", "Intelligence", "Creativity"],
                "correct": 1,
                "explanation": "Workflows provide predictable, consistent execution paths."
            }
        ],
        "LLM Augmentation": [
            {
                "question": "What does RAG stand for?",
                "options": ["Random Access Generation", "Retrieval-Augmented Generation", "Rapid Agent Growth", "Real-time Algorithm Generation"],
                "correct": 1,
                "explanation": "RAG combines retrieval from external sources with LLM generation."
            },
            {
                "question": "Which technique helps LLMs think step-by-step?",
                "options": ["Chain of Thought", "Vector Search", "Fine-tuning", "Prompt Injection"],
                "correct": 0,
                "explanation": "Chain of Thought prompting encourages step-by-step reasoning."
            }
        ],
        "Design Patterns": [
            {
                "question": "In the Planner-Worker pattern, what does the planner do?",
                "options": ["Executes all tasks", "Creates and delegates subtasks", "Stores memory", "Evaluates results"],
                "correct": 1,
                "explanation": "The planner creates subtasks and delegates them to worker agents."
            },
            {
                "question": "What is the purpose of the Reflection pattern?",
                "options": ["To copy data", "To evaluate own outputs", "To delegate tasks", "To store information"],
                "correct": 1,
                "explanation": "Reflection allows agents to evaluate and improve their own reasoning."
            }
        ],
        "Agentic Memory & Knowledge Graphs": [
            {
                "question": "What is the purpose of MERGE in Cypher?",
                "options": ["Delete nodes", "Create nodes avoiding duplication", "Update relationships", "Query data"],
                "correct": 1,
                "explanation": "MERGE creates nodes only if they don't already exist, preventing duplicates."
            },
            {
                "question": "What do knowledge graphs primarily store?",
                "options": ["Raw text", "Entities and relationships", "Images", "Code"],
                "correct": 1,
                "explanation": "Knowledge graphs store structured information about entities and their relationships."
            }
        ],
        "Graphiti": [
            {
                "question": "What is Graphiti primarily used for?",
                "options": ["Image processing", "Temporal knowledge graphs", "Code compilation", "Data encryption"],
                "correct": 1,
                "explanation": "Graphiti tracks events and builds temporal knowledge graphs from unstructured data."
            }
        ],
        "Augmentation Retrieval": [
            {
                "question": "What is semantic search based on?",
                "options": ["Exact keyword matching", "Vector similarity", "Random selection", "Alphabetical order"],
                "correct": 1,
                "explanation": "Semantic search uses vector similarity to find content based on meaning."
            },
            {
                "question": "What are vector embeddings?",
                "options": ["Text files", "Numerical representations of text", "Image formats", "Database schemas"],
                "correct": 1,
                "explanation": "Vector embeddings convert text into numerical representations that capture semantic meaning."
            }
        ],
        "Agentic Payments & Economy": [
            {
                "question": "What is an agentic economy?",
                "options": ["A type of database", "Autonomous agents in economic activities", "A programming language", "A testing framework"],
                "correct": 1,
                "explanation": "Agentic economy involves autonomous agents participating in economic activities."
            },
            {
                "question": "Which protocol is mentioned for secure agent interactions?",
                "options": ["HTTP", "MCP", "FTP", "SMTP"],
                "correct": 1,
                "explanation": "MCP (Model Context Protocol) enables secure agent interactions."
            }
        ]
    }
