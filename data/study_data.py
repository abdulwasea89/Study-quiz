"""
Study data module containing flashcards, topics, and summary information
"""

def get_topics():
    """Return the topics and their estimated number of questions for mock tests"""
    return {
        # Building Effective Agents Topics
        "Workflows vs Agents": 15,
        "LLM Augmentation": 20,
        "Design Patterns": 25,
        "Agentic Memory & Knowledge Graphs": 20,
        "Graphiti": 10,
        "Augmentation Retrieval": 15,
        "Agentic Payments & Economy": 15,
        
        # Model Context Protocol Topics
        "HTTP Fundamentals": 15,
        "REST Architecture": 15,
        "JSON-RPC 2.0": 20,
        "MCP Fundamental Primitives": 25,
        "Advanced MCP Topics": 20,
        "MCP OpenAI Integration": 15,
    }

def get_flashcards():
    """Return flashcard term-definition pairs"""
    return {
        # Building Effective Agents Concepts
        "RAG (Retrieval-Augmented Generation)": "Combines retrieval from external sources with LLM generation to produce grounded responses.",
        "Planner-Worker Pattern": "A design pattern where a planner agent creates and delegates subtasks to worker agents.",
        "MERGE in Cypher": "Creates a node if it does not exist, avoids duplication in knowledge graphs.",
        "Graphiti": "A tool that tracks events, builds ontologies, and supports temporal knowledge graphs from unstructured data.",
        "Tool Use in Agents": "Allows LLMs to perform actions like API calls, database queries, or file manipulations.",
        "Semantic Search": "Search technique using vector similarity based on meaning rather than exact keyword matching.",
        "Agentic Economy": "Concept where autonomous agents participate in economic activities via APIs, often securely through protocols like MCP.",
        "Vector Embeddings": "Numerical representations of text that capture semantic meaning for similarity comparisons.",
        "Knowledge Graph": "A structured representation of entities and relationships, often used for semantic reasoning.",
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
        "Safety Mechanisms": "Built-in controls to prevent harmful or unintended agent behaviors.",
        
        # Model Context Protocol (MCP) Concepts
        "Model Context Protocol (MCP)": "A protocol that enables seamless integration between AI applications and external data sources through a standardized interface.",
        "MCP Client": "The application (like Claude Desktop) that initiates connections and requests resources from MCP servers.",
        "MCP Server": "A program that exposes specific capabilities (resources, tools, prompts) to MCP clients.",
        "Transport Agnostic": "MCP's ability to work over different communication channels (stdio, HTTP, WebSocket) without changing the core protocol.",
        "JSON-RPC 2.0": "The underlying protocol MCP uses for structured communication between clients and servers.",
        "HTTP Request-Response": "Stateless communication pattern where each request contains all necessary information for processing.",
        "REST Principles": "Architectural constraints including statelessness, uniform interface, and resource identification through URIs.",
        "URI (Uniform Resource Identifier)": "A string that uniquely identifies a resource in REST architecture.",
        "HTTP Status Codes": "Three-digit codes that indicate the outcome of HTTP requests (200 OK, 404 Not Found, 500 Internal Server Error).",
        "JSON-RPC Request": "A call to a remote method that expects a response, containing id, method, and params.",
        "JSON-RPC Notification": "A call to a remote method that does not expect a response, lacking an id field.",
        "MCP Resources": "Data sources that servers expose to clients (files, database records, API responses).",
        "MCP Tools": "Functions that clients can invoke on servers to perform actions or computations.",
        "MCP Prompts": "Pre-written prompt templates that servers can provide to clients.",
        "ListTools": "MCP method that allows clients to discover what tools are available on a server.",
        "CallTool": "MCP method that allows clients to execute a specific tool with parameters.",
        "Sampling": "Advanced MCP feature that allows servers to request LLM completions from clients.",
        "Logging": "MCP capability for servers to send log messages to clients for debugging and monitoring.",
        "Progress Notifications": "MCP feature that allows long-running operations to report their progress to clients.",
        "Security Roots": "MCP security mechanism that restricts server access to specific directories or resources.",
        "Stateless HTTP": "HTTP transport mode where each request is independent, requiring authentication and context in every call.",
        "OpenAI Agents SDK": "Framework that integrates MCP capabilities for building AI agents with external tool access.",
        "CORS (Cross-Origin Resource Sharing)": "Web security feature that controls how web pages access resources from different domains.",
        "WebSocket": "Full-duplex communication protocol that maintains persistent connections between client and server.",
        "Stdio Transport": "Communication method using standard input/output streams, commonly used for local MCP connections."
    }

def get_summary_data():
    """Return summary data for creating reference sheets"""
    return {
        # Building Effective Agents Summary
        "Components of Agentic Systems": ["Retrieval", "Tools", "Memory", "Planning", "Execution", "Evaluation"],
        "Common Agent Design Patterns": ["Routing", "Prompt Chaining", "Parallelization", "Planner-Worker", "Evaluator-Optimizer", "Reflection", "Delegation"],
        "Memory Tools": ["Neo4j", "Graphiti", "Vector Databases", "Knowledge Graphs", "Temporal Storage"],
        "Agent Capabilities": ["Search", "Tool Use", "Reflection", "Delegation", "Learning", "Adaptation"],
        "Secure Economy Integration": ["Stripe API", "MCP Tool Call", "User Trust Mechanisms", "Authentication", "Authorization"],
        "LLM Augmentation Techniques": ["RAG", "Fine-tuning", "Prompt Engineering", "Chain of Thought", "Few-shot Learning"],
        "Evaluation Approaches": ["Human Feedback", "Automated Metrics", "A/B Testing", "Performance Benchmarks"],
        
        # Model Context Protocol Summary
        "MCP Core Components": ["MCP Client", "MCP Server", "Resources", "Tools", "Prompts"],
        "MCP Transport Layers": ["Stdio", "HTTP", "WebSocket", "Server-Sent Events"],
        "HTTP Methods": ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
        "HTTP Status Code Categories": ["1xx Informational", "2xx Success", "3xx Redirection", "4xx Client Error", "5xx Server Error"],
        "REST Principles": ["Statelessness", "Uniform Interface", "Resource Identification", "HATEOAS", "Cacheability"],
        "JSON-RPC 2.0 Elements": ["Request", "Response", "Notification", "Error", "Batch"],
        "MCP Security Features": ["Security Roots", "Authentication", "Authorization", "Access Control"],
        "Advanced MCP Capabilities": ["Sampling", "Logging", "Progress Notifications", "Resource Updates"],
        "Learning Resources": ["Anthropic Skilljar", "GitHub Repositories", "Documentation", "Code Examples"]
    }

def get_difficulty_levels():
    """Return available difficulty levels"""
    return {
        "Normal": "Basic understanding of concepts",
        "Intermediate": "Practical application knowledge", 
        "Advanced": "Deep technical understanding",
        "PhD": "Research-level expertise",
        "God Level": "Master-level comprehensive knowledge"
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
                "explanation": "Agentic economy involves autonomous agents participating in economic activities.",
                "difficulty": "Normal"
            },
            {
                "question": "Which protocol is mentioned for secure agent interactions?",
                "options": ["HTTP", "MCP", "FTP", "SMTP"],
                "correct": 1,
                "explanation": "MCP (Model Context Protocol) enables secure agent interactions.",
                "difficulty": "Intermediate"
            },
            {
                "question": "What is the primary challenge in agentic payments?",
                "options": ["Speed", "Security and trust", "Cost", "Availability"],
                "correct": 1,
                "explanation": "Building user trust and ensuring security are critical to prevent fraud in agentic payment systems.",
                "difficulty": "Advanced"
            }
        ],
        
        # Model Context Protocol Topics
        "HTTP Fundamentals": [
            {
                "question": "What does HTTP stand for?",
                "options": ["HyperText Transfer Protocol", "High Transfer Text Protocol", "Host Transfer Text Protocol", "HyperText Template Protocol"],
                "correct": 0,
                "explanation": "HTTP stands for HyperText Transfer Protocol, the foundation of web communication.",
                "difficulty": "Normal"
            },
            {
                "question": "Which HTTP method is used to retrieve data?",
                "options": ["POST", "PUT", "GET", "DELETE"],
                "correct": 2,
                "explanation": "GET is the HTTP method used to retrieve data from a server.",
                "difficulty": "Normal"
            },
            {
                "question": "What does HTTP status code 404 indicate?",
                "options": ["Server error", "Not found", "Unauthorized", "Bad request"],
                "correct": 1,
                "explanation": "HTTP 404 indicates that the requested resource was not found on the server.",
                "difficulty": "Intermediate"
            },
            {
                "question": "What is the fundamental characteristic of HTTP?",
                "options": ["Stateful", "Stateless", "Persistent", "Encrypted"],
                "correct": 1,
                "explanation": "HTTP is stateless, meaning each request is independent and contains all necessary information.",
                "difficulty": "Advanced"
            }
        ],
        
        "REST Architecture": [
            {
                "question": "What does REST stand for?",
                "options": ["Representational State Transfer", "Remote State Transfer", "Real State Transfer", "Rapid State Transfer"],
                "correct": 0,
                "explanation": "REST stands for Representational State Transfer, an architectural style for web services.",
                "difficulty": "Normal"
            },
            {
                "question": "Which is a key principle of REST?",
                "options": ["Stateful communication", "Complex interfaces", "Statelessness", "Protocol dependence"],
                "correct": 2,
                "explanation": "Statelessness is a fundamental principle of REST architecture.",
                "difficulty": "Intermediate"
            },
            {
                "question": "How are resources identified in REST?",
                "options": ["By database IDs", "By URIs", "By IP addresses", "By port numbers"],
                "correct": 1,
                "explanation": "Resources in REST are uniquely identified using URIs (Uniform Resource Identifiers).",
                "difficulty": "Advanced"
            },
            {
                "question": "What is the HATEOAS principle in REST?",
                "options": ["HTTP As Text Exchange Over Asynchronous Systems", "Hypermedia As The Engine Of Application State", "HyperText Application Transfer Over Asynchronous Systems", "HTTP Application Transfer Engine Over Asynchronous State"],
                "correct": 1,
                "explanation": "HATEOAS means that a client interacts with a REST application entirely through hypermedia provided dynamically by application servers.",
                "difficulty": "PhD"
            }
        ],
        
        "JSON-RPC 2.0": [
            {
                "question": "What is JSON-RPC?",
                "options": ["A database format", "A remote procedure call protocol", "A web framework", "A programming language"],
                "correct": 1,
                "explanation": "JSON-RPC is a remote procedure call protocol encoded in JSON.",
                "difficulty": "Normal"
            },
            {
                "question": "What distinguishes a JSON-RPC Request from a Notification?",
                "options": ["The method name", "The presence of an id field", "The parameter format", "The JSON structure"],
                "correct": 1,
                "explanation": "Requests have an id field and expect responses, while Notifications do not have an id and expect no response.",
                "difficulty": "Intermediate"
            },
            {
                "question": "What is the current version of JSON-RPC used by MCP?",
                "options": ["1.0", "2.0", "3.0", "2.1"],
                "correct": 1,
                "explanation": "MCP uses JSON-RPC 2.0 specification for communication.",
                "difficulty": "Advanced"
            },
            {
                "question": "Which field is forbidden in JSON-RPC method names starting with 'rpc.'?",
                "options": ["params", "id", "All method names", "Reserved for protocol extensions"],
                "correct": 3,
                "explanation": "Method names beginning with 'rpc.' are reserved for rpc-internal methods and protocol extensions.",
                "difficulty": "God Level"
            }
        ],
        
        "MCP Fundamental Primitives": [
            {
                "question": "What does MCP stand for?",
                "options": ["Multi-Client Protocol", "Model Context Protocol", "Message Communication Protocol", "Machine Control Protocol"],
                "correct": 1,
                "explanation": "MCP stands for Model Context Protocol, enabling integration between AI applications and external data sources.",
                "difficulty": "Normal"
            },
            {
                "question": "What are the two main roles in MCP architecture?",
                "options": ["Server and Database", "Client and Server", "Host and Guest", "Producer and Consumer"],
                "correct": 1,
                "explanation": "MCP architecture consists of MCP Clients (like Claude Desktop) and MCP Servers that expose capabilities.",
                "difficulty": "Intermediate"
            },
            {
                "question": "What does 'transport agnostic' mean in MCP context?",
                "options": ["It only works over HTTP", "It can work over different communication channels", "It requires specific hardware", "It needs internet connection"],
                "correct": 1,
                "explanation": "Transport agnostic means MCP can work over stdio, HTTP, WebSocket, or other transport layers.",
                "difficulty": "Advanced"
            },
            {
                "question": "What is the primary problem MCP solves?",
                "options": ["Slow internet", "Integration complexity between AI and external systems", "Database performance", "User interface design"],
                "correct": 1,
                "explanation": "MCP standardizes how AI applications connect to and interact with external data sources and tools.",
                "difficulty": "PhD"
            }
        ],
        
        "Advanced MCP Topics": [
            {
                "question": "What is MCP sampling?",
                "options": ["Data collection method", "Servers requesting LLM completions from clients", "Random selection process", "Quality control technique"],
                "correct": 1,
                "explanation": "Sampling allows MCP servers to request LLM completions from clients for advanced workflows.",
                "difficulty": "Advanced"
            },
            {
                "question": "What are MCP security roots?",
                "options": ["Password protection", "Encryption keys", "Directory access restrictions", "User authentication"],
                "correct": 2,
                "explanation": "Security roots restrict MCP server access to specific directories or file system areas.",
                "difficulty": "PhD"
            },
            {
                "question": "In stateless HTTP MCP transport, what must each request include?",
                "options": ["Session cookies", "Authentication and full context", "Previous request history", "Connection credentials"],
                "correct": 1,
                "explanation": "Stateless HTTP requires each request to be self-contained with authentication and context.",
                "difficulty": "God Level"
            }
        ],
        
        "MCP OpenAI Integration": [
            {
                "question": "What is the OpenAI Agents SDK?",
                "options": ["A database system", "Framework for building AI agents with external tool access", "Web browser", "Programming language"],
                "correct": 1,
                "explanation": "The OpenAI Agents SDK provides a framework for building AI agents that can integrate with MCP capabilities.",
                "difficulty": "Intermediate"
            },
            {
                "question": "How does MCP integration benefit OpenAI agents?",
                "options": ["Faster processing", "Access to external tools and data", "Better UI design", "Lower costs"],
                "correct": 1,
                "explanation": "MCP integration allows OpenAI agents to securely access external tools, databases, and APIs.",
                "difficulty": "Advanced"
            },
            {
                "question": "What protocol does MCP use for OpenAI agent communication?",
                "options": ["HTTP only", "WebSocket only", "JSON-RPC over various transports", "Custom binary protocol"],
                "correct": 2,
                "explanation": "MCP uses JSON-RPC 2.0 which can run over multiple transport layers including HTTP and WebSocket.",
                "difficulty": "God Level"
            }
        ]
    }
