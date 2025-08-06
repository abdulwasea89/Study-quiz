"""
Study data module containing flashcards, topics, and summary information
"""

def get_topics():
    """Return the topics and their estimated number of questions for mock tests"""
    return {
        # OpenAI Agents SDK Topics (Enhanced)
        "Agent Fundamentals": 25,
        "Tools and Function Calling": 30,
        "Handoffs and Multi-Agent Systems": 25,
        "Sessions and Memory Management": 20,
        "Guardrails and Security": 20,
        "Production Deployment": 15,
        "Advanced Patterns": 15,
        
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
        # OpenAI Agents SDK Enhanced Flashcards
        "OpenAI Agents SDK": "A lightweight, production-ready Python framework for building multi-agent workflows with agents, handoffs, guardrails, and sessions.",
        "Agent (OpenAI SDK)": "An LLM equipped with instructions, tools, and the ability to take autonomous actions in a loop until tasks are completed.",
        "Handoffs": "Mechanism allowing agents to transfer complete control to other specialized agents, passing full conversation history and context.",
        "Guardrails": "Input and output validation systems that ensure agent safety, prevent harmful requests, and maintain policy compliance.",
        "Sessions": "Automatic conversation history management system that maintains context across multiple agent interactions without manual state handling.",
        "Function Tools": "Python functions converted to agent tools with automatic schema generation and Pydantic validation.",
        "Hosted Tools": "OpenAI-managed tools like WebSearch, CodeInterpreter, and FileSearch that run on LLM servers alongside AI models.",
        "Agents as Tools": "Pattern where agents can be used as tools by other agents, maintaining orchestrator control while leveraging specialist capabilities.",
        "Tool Composition": "Advanced techniques for combining multiple tools: sequential chaining, parallel execution, and conditional selection.",
        "Agent Orchestration": "Managing complex multi-agent workflows with coordination patterns, conflict resolution, and failure recovery.",
        "Context Window Optimization": "Strategies for managing conversation history within model limits through compression, sliding windows, and selective retention.",
        "Agent Tracing": "Built-in monitoring system that captures agent decisions, tool calls, performance metrics, and workflow visualization.",
        "Production Deployment": "Enterprise patterns for agent systems: containerization, auto-scaling, circuit breakers, and blue-green deployments.",
        "Multi-Model Support": "SDK compatibility with OpenAI models and 100+ other LLMs through Chat Completions-style APIs.",
        "Structured Outputs": "Using Pydantic models to force agents to return data in specific formats for reliable system integration.",
        "Async Agent Execution": "Non-blocking agent operations using Python's asyncio for high-concurrency applications.",
        "Agent Security": "Comprehensive security including API key management, input validation, output filtering, and audit logging.",
        "Tool Error Handling": "Robust error management with custom failure functions, automatic retries, and graceful degradation.",
        "Agent Lifecycle Management": "Complete process of agent creation, initialization, execution monitoring, and graceful shutdown.",
        "Dynamic Instructions": "Runtime modification of agent instructions based on context, user preferences, or environmental conditions.",
        
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
        "Stdio Transport": "Communication method using standard input/output streams, commonly used for local MCP connections.",
        
        # OpenAI Agents SDK Flashcards
        "OpenAI Agents SDK": "Production-ready framework for building agentic AI applications, evolved from the experimental Swarm framework.",
        "Agent Primitives": "Four core components: Agents (LLMs with instructions), Handoffs (delegation), Guardrails (validation), Sessions (conversation history).",
        "Agent Runner": "Execution engine that handles calling tools, sending results to LLM, and looping until completion.",
        "Function Tools": "Python functions automatically converted to agent tools with schema generation and Pydantic validation.",
        "Agent Handoffs": "Mechanism for delegating tasks between specialized agents using Handoff(agent=target_agent, context=info).",
        "Agent Sessions": "Automatic conversation history management across multiple agent runs, eliminating manual state handling.",
        "Agent Guardrails": "Input validation system that runs checks in parallel, breaking early if validation fails.",
        "Agent Tracing": "Built-in monitoring for visualization, debugging, evaluation, fine-tuning, and distillation.",
        "Parallel Tool Calls": "Feature enabling concurrent execution of multiple tools using parallel_tool_calls=True.",
        "Session Persistence": "Ability to save and load conversation state using session.save() and Session.load() methods.",
        "Memory Strategy": "Configurable approach for handling context window overflow (sliding_window, truncation, etc.).",
        "Temperature Control": "Parameter controlling response randomness - lower values (0.1) for deterministic, higher for creative.",
        "Context Window": "Maximum token limit for conversation history, configurable per session with automatic management.",
        "Schema Generation": "Automatic creation of tool schemas from Python function signatures and docstrings.",
        "Pydantic Integration": "Seamless validation using Pydantic models for both tool parameters and guardrail checks.",
        "Agent Instructions": "System prompts that define agent behavior, capabilities, and response patterns.",
        "Multi-Agent Coordination": "Patterns like coordinator-worker for managing specialized agents in complex workflows.",
        "Agent Loop Control": "Built-in system that manages tool execution, LLM interaction, and conversation flow.",
        "Error Handling": "Comprehensive error management with retry logic, validation failures, and graceful degradation.",
        "Production Ready": "Enterprise-grade features including tracing, monitoring, security, and scalability considerations."
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
        "Learning Resources": ["Anthropic Skilljar", "GitHub Repositories", "Documentation", "Code Examples"],
        
        # OpenAI Agents SDK Summary
        "OpenAI Agents Core Primitives": ["Agents", "Handoffs", "Guardrails", "Sessions"],
        "Agent Architecture Components": ["Instructions", "Tools", "Model Configuration", "Temperature Control"],
        "Tool Integration Methods": ["Function Tools", "Schema Generation", "Pydantic Validation", "Parallel Execution"],
        "Multi-Agent Patterns": ["Coordinator-Worker", "Handoff Delegation", "Specialized Agents", "Context Passing"],
        "Session Management": ["Conversation History", "Persistence", "Memory Strategy", "Context Window"],
        "Security and Validation": ["Input Guardrails", "Custom Validators", "Error Handling", "Safety Checks"],
        "Monitoring and Debugging": ["Built-in Tracing", "Performance Monitoring", "Evaluation Tools", "Fine-tuning"],
        "Production Features": ["Scalability", "Error Recovery", "Enterprise Integration", "Deployment Ready"]
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
        ],
        
        "OpenAI Agents SDK Fundamentals": [
            {
                "question": "What are the four core primitives of the OpenAI Agents SDK?",
                "options": ["Models, Tools, Memory, Sessions", "Agents, Handoffs, Guardrails, Sessions", "Clients, Servers, Resources, Tools", "Functions, Classes, Objects, Methods"],
                "correct": 1,
                "explanation": "The OpenAI Agents SDK has four core primitives: Agents (LLMs with instructions), Handoffs (delegation), Guardrails (validation), and Sessions (conversation history).",
                "difficulty": "Normal",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How do you install the OpenAI Agents SDK?",
                "options": ["npm install openai-agents", "pip install openai-agents", "conda install openai-agents", "yarn add openai-agents"],
                "correct": 1,
                "explanation": "The OpenAI Agents SDK is installed using pip: pip install openai-agents",
                "difficulty": "Normal",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What is the primary difference between OpenAI Agents SDK and Swarm?",
                "options": ["Different programming language", "Agents SDK is production-ready", "Swarm is faster", "No difference"],
                "correct": 1,
                "explanation": "The OpenAI Agents SDK is a production-ready upgrade of the experimental Swarm framework.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "Which of these is NOT a design principle of the OpenAI Agents SDK?",
                "options": ["Enough features to be worth using", "Few enough primitives to learn quickly", "Works great out of the box", "Requires extensive configuration"],
                "correct": 3,
                "explanation": "The SDK is designed to work great out of the box with minimal configuration, not requiring extensive setup.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            }
        ],
        
        "OpenAI Agents Implementation": [
            {
                "question": "What is the correct way to create a basic agent?",
                "options": [
                    "Agent(name='Assistant')",
                    "Agent(name='Assistant', instructions='You are helpful')",
                    "new Agent('Assistant', 'helpful')",
                    "create_agent('Assistant')"
                ],
                "correct": 1,
                "explanation": "A basic agent requires both a name and instructions: Agent(name='Assistant', instructions='You are helpful')",
                "difficulty": "Normal",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How do you run an agent synchronously?",
                "options": ["agent.run(message)", "Runner.run_sync(agent, message)", "agent.execute_sync(message)", "run_agent(agent, message)"],
                "correct": 1,
                "explanation": "Use Runner.run_sync(agent, message) to run an agent synchronously.",
                "difficulty": "Normal",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What parameter controls the randomness of agent responses?",
                "options": ["randomness", "temperature", "creativity", "variance"],
                "correct": 1,
                "explanation": "The temperature parameter controls the randomness/creativity of LLM responses.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "Which model parameter would you use for more deterministic responses?",
                "options": ["temperature=1.0", "temperature=0.1", "temperature=2.0", "temperature=0.5"],
                "correct": 1,
                "explanation": "Lower temperature values (like 0.1) produce more deterministic, focused responses.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            }
        ],
        
        "OpenAI Tools and Functions": [
            {
                "question": "How are Python functions converted to agent tools?",
                "options": ["Manual schema writing", "Automatic schema generation", "XML configuration", "JSON templates"],
                "correct": 1,
                "explanation": "The SDK automatically generates schemas from Python function signatures and docstrings.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What library is used for function parameter validation?",
                "options": ["marshmallow", "cerberus", "pydantic", "jsonschema"],
                "correct": 2,
                "explanation": "The SDK uses Pydantic for automatic function parameter validation.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What should a tool function return?",
                "options": ["Always a dictionary", "Always a string", "Any JSON-serializable type", "Only integers"],
                "correct": 2,
                "explanation": "Tool functions should return any JSON-serializable type that can be sent back to the LLM.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How do you enable parallel tool calls?",
                "options": ["parallel_tools=True", "parallel_tool_calls=True", "enable_parallel=True", "concurrent=True"],
                "correct": 1,
                "explanation": "Set parallel_tool_calls=True in the Agent configuration to enable parallel execution.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            }
        ],
        
        "OpenAI Handoffs and Multi-Agent": [
            {
                "question": "What is the purpose of a Handoff?",
                "options": ["Error handling", "Agent delegation", "Memory management", "Tool execution"],
                "correct": 1,
                "explanation": "Handoffs allow agents to delegate tasks to other specialized agents.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How do you create a handoff to another agent?",
                "options": ["transfer(agent)", "Handoff(agent=target_agent)", "delegate(agent)", "switch_to(agent)"],
                "correct": 1,
                "explanation": "Create handoffs using Handoff(agent=target_agent) with optional context.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What information can be passed during a handoff?",
                "options": ["Only agent name", "Agent and context", "Just the message", "Agent credentials"],
                "correct": 1,
                "explanation": "Handoffs can include the target agent and contextual information to continue the conversation.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "In a multi-agent system, which pattern is most efficient for coordinated workflows?",
                "options": ["Sequential execution", "Coordinator-worker pattern", "Broadcast pattern", "Random selection"],
                "correct": 1,
                "explanation": "The coordinator-worker pattern efficiently manages specialized agents for different tasks.",
                "difficulty": "PhD",
                "framework": "OpenAI Agents SDK"
            }
        ],
        
        "OpenAI Sessions and State": [
            {
                "question": "What does a Session automatically manage?",
                "options": ["Tool execution", "Conversation history", "Agent creation", "Error handling"],
                "correct": 1,
                "explanation": "Sessions automatically maintain conversation history across multiple agent runs.",
                "difficulty": "Normal",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How do you create a persistent session?",
                "options": ["Session(persistent=True)", "Session.create_persistent()", "session.save(filename)", "PersistentSession()"],
                "correct": 2,
                "explanation": "Use session.save(filename) to persist a session to disk for later loading.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What happens when a session context window is exceeded?",
                "options": ["Error thrown", "Oldest messages removed", "Session resets", "Depends on memory_strategy"],
                "correct": 3,
                "explanation": "The behavior depends on the configured memory_strategy (sliding_window, etc.).",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "Which session parameter controls maximum conversation length?",
                "options": ["max_length", "max_turns", "conversation_limit", "turn_limit"],
                "correct": 1,
                "explanation": "The max_turns parameter limits the number of conversation turns in a session.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            }
        ],
        
        "OpenAI Guardrails and Security": [
            {
                "question": "What is the primary purpose of Guardrails?",
                "options": ["Performance optimization", "Input validation", "Output formatting", "Error logging"],
                "correct": 1,
                "explanation": "Guardrails validate inputs to agents and can break execution early if validation fails.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How do you create a custom guardrail?",
                "options": ["@guardrail decorator", "Guardrail(validator=func)", "guardrail_function()", "validate_input()"],
                "correct": 1,
                "explanation": "Create guardrails using Guardrail(validator=validation_function) with custom logic.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "When do guardrails execute?",
                "options": ["After agent response", "Before agent processing", "During tool execution", "At session end"],
                "correct": 1,
                "explanation": "Guardrails run before agent processing to validate inputs and prevent invalid requests.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What validation library integrates well with guardrails?",
                "options": ["jsonschema", "pydantic", "marshmallow", "cerberus"],
                "correct": 1,
                "explanation": "Pydantic models integrate seamlessly with guardrail validation functions.",
                "difficulty": "PhD",
                "framework": "OpenAI Agents SDK"
            }
        ],
        
        "OpenAI Tracing and Monitoring": [
            {
                "question": "What does the built-in tracing feature provide?",
                "options": ["Code debugging only", "Performance metrics only", "Visualization and debugging", "Error logs only"],
                "correct": 2,
                "explanation": "Built-in tracing provides visualization, debugging, and monitoring capabilities for agent workflows.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How do you enable tracing for an agent?",
                "options": ["agent.enable_tracing()", "enable_tracing(project_name)", "trace=True in Agent()", "Runner.trace()"],
                "correct": 1,
                "explanation": "Use enable_tracing(project_name) to enable automatic tracing for all agent operations.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What can you do with traced data?",
                "options": ["Evaluation only", "Fine-tuning only", "Evaluation, fine-tuning, and distillation", "Debugging only"],
                "correct": 2,
                "explanation": "Traced data can be used for evaluation, fine-tuning models, and distillation processes.",
                "difficulty": "PhD",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "Which decorator enables custom function tracing?",
                "options": ["@trace", "@trace_function", "@monitor", "@track"],
                "correct": 1,
                "explanation": "Use @trace_function decorator to automatically trace custom function calls.",
                "difficulty": "God Level",
                "framework": "OpenAI Agents SDK"
            }
        ]
    }
