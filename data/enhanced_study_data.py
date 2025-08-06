"""
Enhanced study data with progressive question complexity and comprehensive content
"""

def get_progressive_openai_sdk_questions():
    """Progressive questions from basic understanding to complex implementation"""
    return {
        "OpenAI SDK Foundation - Level 1 (Basic Understanding)": [
            {
                "question": "What does OpenAI stand for and what is its primary focus?",
                "options": [
                    "Open Artificial Intelligence - focused on making AI accessible and beneficial",
                    "OpenAI Initiative - focused on proprietary AI development", 
                    "Open AI Integration - focused on connecting different AI systems",
                    "OpenAI Institute - focused on AI research only"
                ],
                "correct": 0,
                "explanation": "OpenAI stands for Open Artificial Intelligence and focuses on developing artificial general intelligence (AGI) that benefits all of humanity.",
                "difficulty": "Normal",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What is the OpenAI Agents SDK designed to help developers build?",
                "options": [
                    "Web applications with database connections",
                    "AI agents that can take actions and use tools",
                    "Machine learning models from scratch", 
                    "Mobile applications with voice features"
                ],
                "correct": 1,
                "explanation": "The OpenAI Agents SDK is specifically designed to help developers build AI agents that can take actions, use tools, and collaborate with other agents.",
                "difficulty": "Normal",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "Why would someone choose the OpenAI Agents SDK over building agents from scratch?",
                "options": [
                    "It's completely free with no limitations",
                    "It provides pre-built components like agent loops, handoffs, and sessions",
                    "It only works with OpenAI models",
                    "It requires no programming knowledge"
                ],
                "correct": 1,
                "explanation": "The SDK provides essential pre-built components like agent loops, handoffs, sessions, and guardrails, making agent development much faster and more reliable.",
                "difficulty": "Normal", 
                "framework": "OpenAI Agents SDK"
            }
        ],

        "OpenAI SDK Foundation - Level 2 (Component Understanding)": [
            {
                "question": "What are the four core building blocks that make the OpenAI Agents SDK powerful?",
                "options": [
                    "Models, Databases, APIs, Interfaces",
                    "Agents, Handoffs, Guardrails, Sessions",
                    "Functions, Classes, Methods, Objects",
                    "Input, Processing, Output, Storage"
                ],
                "correct": 1,
                "explanation": "The four core primitives are: Agents (LLMs with instructions and tools), Handoffs (agent delegation), Guardrails (input validation), and Sessions (conversation history management).",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How does an Agent differ from a simple API call to an LLM?",
                "options": [
                    "Agents cost more money to run",
                    "Agents can use tools, maintain context, and take multiple actions autonomously",
                    "Agents only work with specific models",
                    "There is no difference between them"
                ],
                "correct": 1,
                "explanation": "An Agent is equipped with instructions, tools, and the ability to take multiple actions in a loop, making decisions and using tools until a task is complete, unlike a simple API call.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "What happens when an Agent needs specialized knowledge it doesn't have?",
                "options": [
                    "It stops working and returns an error",
                    "It makes up the information",
                    "It uses Handoffs to delegate to specialized agents",
                    "It searches the internet automatically"
                ],
                "correct": 2,
                "explanation": "Handoffs allow agents to delegate tasks to other specialized agents, ensuring that the right expertise is applied to each part of a complex task.",
                "difficulty": "Intermediate",
                "framework": "OpenAI Agents SDK"
            }
        ],

        "OpenAI SDK Architecture - Level 3 (System Design)": [
            {
                "question": "In a customer service system, how would you design the agent architecture using the OpenAI SDK?",
                "options": [
                    "One large agent that handles everything",
                    "A triage agent that uses handoffs to route to billing, technical, and refund specialists",
                    "Separate applications for each type of request",
                    "Multiple copies of the same general agent"
                ],
                "correct": 1,
                "explanation": "The recommended pattern is a triage agent that analyzes requests and hands off to specialized agents (billing, technical, refunds) using the handoff mechanism for efficient task distribution.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "Why might you implement Guardrails in a production agent system?",
                "options": [
                    "To make the system run faster",
                    "To validate inputs and prevent harmful or inappropriate requests before they reach agents",
                    "To store conversation history",
                    "To connect to external APIs"
                ],
                "correct": 1,
                "explanation": "Guardrails act as safety mechanisms that validate inputs, check for policy violations, and can prevent harmful requests from being processed by agents, ensuring system safety and compliance.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How do Sessions benefit multi-turn conversations in an agent system?",
                "options": [
                    "They make conversations faster",
                    "They automatically manage conversation history and context across multiple agent interactions",
                    "They allow multiple users to chat simultaneously",
                    "They translate conversations to different languages"
                ],
                "correct": 1,
                "explanation": "Sessions automatically maintain conversation history and context, allowing agents to remember previous interactions, maintain user preferences, and provide consistent experiences across multiple turns.",
                "difficulty": "Advanced",
                "framework": "OpenAI Agents SDK"
            }
        ],

        "OpenAI SDK Implementation - Level 4 (Practical Application)": [
            {
                "question": "When implementing a function tool that calls an external API, what considerations are most critical for production use?",
                "options": [
                    "Making the function as short as possible",
                    "Error handling, rate limiting, timeout management, and security",
                    "Using only synchronous operations",
                    "Avoiding any external dependencies"
                ],
                "correct": 1,
                "explanation": "Production function tools must handle errors gracefully, respect API rate limits, manage timeouts, secure API keys, and provide meaningful feedback to agents when external services fail.",
                "difficulty": "PhD",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "In a complex workflow where Agent A hands off to Agent B, which then needs to collaborate with Agent C, what's the most efficient implementation pattern?",
                "options": [
                    "Chain handoffs: A → B → C in sequence",
                    "Agent B uses Agent C as a tool while maintaining control",
                    "All agents run in parallel processing the same input",
                    "Create a single super-agent that combines all capabilities"
                ],
                "correct": 1,
                "explanation": "Using Agent C as a tool allows Agent B to maintain control and context while leveraging Agent C's specialized capabilities, providing better coordination than sequential handoffs.",
                "difficulty": "PhD",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "How would you optimize session management in a high-concurrency agent system serving thousands of users?",
                "options": [
                    "Store all sessions in memory for fast access",
                    "Use persistent storage with session pooling and context window optimization",
                    "Limit each user to one session at a time",
                    "Restart sessions after every interaction"
                ],
                "correct": 1,
                "explanation": "High-concurrency systems need persistent session storage (database/Redis), session pooling to manage resources, context window optimization to control memory usage, and possibly session sharding.",
                "difficulty": "God Level",
                "framework": "OpenAI Agents SDK"
            }
        ],

        "OpenAI SDK Mastery - Level 5 (Expert Implementation)": [
            {
                "question": "You're building a financial analysis agent system where accuracy is critical and hallucinations must be minimized. How would you architect this using the OpenAI SDK?",
                "options": [
                    "Use one general agent with access to all financial data",
                    "Implement multi-layer validation with specialized agents, guardrails for input/output validation, tools for verified data sources, and human-in-the-loop for critical decisions",
                    "Rely on the LLM's built-in financial knowledge",
                    "Use only simple API calls without agents"
                ],
                "correct": 1,
                "explanation": "Critical systems require: specialized agents for different analysis types, input/output guardrails for validation, tools that access only verified data sources, confidence scoring, and human review workflows for high-stakes decisions.",
                "difficulty": "God Level",
                "framework": "OpenAI Agents SDK"
            },
            {
                "question": "When designing a research agent system that needs to maintain data lineage and provide audit trails, what architectural patterns should you implement?",
                "options": [
                    "Simple logging of final outputs only",
                    "Comprehensive tracing with tool call logging, source attribution, agent decision tracking, and session persistence with metadata",
                    "Store only the final research results",
                    "Use separate systems for audit and functionality"
                ],
                "correct": 1,
                "explanation": "Audit-ready systems need: comprehensive tracing of all agent actions, tool call logging with timestamps, source attribution for all information, agent decision rationale tracking, and persistent sessions with rich metadata.",
                "difficulty": "God Level",
                "framework": "OpenAI Agents SDK"
            }
        ]
    }

def get_enhanced_building_agents_questions():
    """Enhanced Building Effective Agents questions with progressive complexity"""
    return {
        "Agent Fundamentals - Understanding Core Concepts": [
            {
                "question": "What fundamentally distinguishes an AI agent from a traditional software application?",
                "options": [
                    "Agents use artificial intelligence while applications don't",
                    "Agents can autonomously make decisions and adapt their behavior based on their environment",
                    "Agents are always connected to the internet",
                    "Agents only work with text data"
                ],
                "correct": 1,
                "explanation": "AI agents have autonomy - they can perceive their environment, make decisions, and take actions to achieve goals, adapting their behavior dynamically rather than following fixed program logic.",
                "difficulty": "Normal",
                "framework": "Building Effective Agents"
            },
            {
                "question": "Why do modern AI agents need 'augmentation' beyond just the core language model?",
                "options": [
                    "To make them faster",
                    "Because LLMs alone have limitations: no access to real-time data, can't take actions, and have knowledge cutoffs",
                    "To make them cheaper to run",
                    "Because it's required by OpenAI"
                ],
                "correct": 1,
                "explanation": "LLMs have inherent limitations: knowledge cutoff dates, inability to access real-time information, no capacity to take actions in the world, and limited working memory. Augmentation addresses these limitations.",
                "difficulty": "Intermediate",
                "framework": "Building Effective Agents"
            }
        ],

        "Agent Architecture Patterns - Design Principles": [
            {
                "question": "In the Orchestrator-Worker pattern, what is the primary responsibility of the orchestrator agent?",
                "options": [
                    "To do all the actual work itself",
                    "To analyze complex tasks, break them into subtasks, and coordinate worker agents",
                    "To store data permanently",
                    "To handle user interface interactions"
                ],
                "correct": 1,
                "explanation": "The orchestrator analyzes incoming requests, decomposes complex tasks into manageable subtasks, assigns appropriate worker agents, and coordinates their efforts to achieve the overall goal.",
                "difficulty": "Advanced",
                "framework": "Building Effective Agents"
            },
            {
                "question": "When would you choose Prompt Chaining over Parallelization in an agent system?",
                "options": [
                    "When you want faster execution",
                    "When later steps depend on the results of earlier steps, requiring sequential processing",
                    "When you have unlimited computing resources",
                    "When working with image data only"
                ],
                "correct": 1,
                "explanation": "Prompt chaining is ideal when tasks have dependencies - each step builds on the previous one's output. Parallelization is better for independent tasks that can run simultaneously.",
                "difficulty": "Advanced",
                "framework": "Building Effective Agents"
            }
        ],

        "Memory and Knowledge Systems - Advanced Implementation": [
            {
                "question": "How does Graphiti's temporal knowledge graph approach differ from traditional vector databases for agent memory?",
                "options": [
                    "It's just faster storage",
                    "It captures not just what happened, but when it happened and the relationships between events over time",
                    "It only works with text data",
                    "It requires less storage space"
                ],
                "correct": 1,
                "explanation": "Graphiti builds temporal knowledge graphs that track events, relationships, and their evolution over time, providing richer context for agents compared to vector databases that primarily do semantic similarity matching.",
                "difficulty": "PhD",
                "framework": "Building Effective Agents"
            },
            {
                "question": "In a production agent system handling sensitive customer data, how would you implement secure memory management using Neo4j?",
                "options": [
                    "Store all data in plaintext for easy access",
                    "Implement encryption at rest, role-based access control, data anonymization, and audit logging with retention policies",
                    "Use only in-memory storage",
                    "Avoid storing any data permanently"
                ],
                "correct": 1,
                "explanation": "Secure memory systems require: encryption at rest and in transit, role-based access controls, data anonymization/pseudonymization, comprehensive audit logging, retention policies, and compliance with data protection regulations.",
                "difficulty": "God Level",
                "framework": "Building Effective Agents"
            }
        ]
    }

def get_enhanced_mcp_questions():
    """Enhanced MCP questions with comprehensive Level 2 certification content"""
    return {
        "HTTP Fundamentals - Level 1": [
            {
                "question": "What does HTTP stand for and what is its primary purpose in web communication?",
                "options": [
                    "HyperText Transfer Protocol - for transferring hypertext documents between web servers and clients",
                    "High-Tech Transfer Protocol - for high-speed data transfer",
                    "HyperText Transport Protocol - for secure communications",
                    "Hybrid Transfer Protocol - for mixed media transfer"
                ],
                "correct": 0,
                "explanation": "HTTP (HyperText Transfer Protocol) is the foundation of data communication on the World Wide Web, defining how messages are formatted and transmitted between web servers and clients.",
                "difficulty": "Normal",
                "framework": "Model Context Protocol (MCP)"
            },
            {
                "question": "In the HTTP request-response cycle, what happens when a client sends a GET request?",
                "options": [
                    "The server deletes the requested resource",
                    "The server retrieves and returns the requested resource without modifying it",
                    "The server creates a new resource",
                    "The server updates an existing resource"
                ],
                "correct": 1,
                "explanation": "GET requests are idempotent and safe - they retrieve data without causing any side effects on the server, making them cacheable and suitable for repeated calls.",
                "difficulty": "Normal",
                "framework": "Model Context Protocol (MCP)"
            }
        ],

        "REST Architecture Principles - Level 2": [
            {
                "question": "Why is statelessness a core principle of REST architecture, and how does it benefit system design?",
                "options": [
                    "It makes the system faster by reducing server load",
                    "Each request contains all necessary information, enabling better scalability, reliability, and simplified server design",
                    "It reduces the amount of data transmitted",
                    "It makes the API more secure by default"
                ],
                "correct": 1,
                "explanation": "Statelessness means each request is self-contained, allowing servers to be simplified, scaled horizontally, and made more reliable since no session state needs to be maintained between requests.",
                "difficulty": "Intermediate",
                "framework": "Model Context Protocol (MCP)"
            },
            {
                "question": "How should URI design follow REST principles for resource identification and manipulation?",
                "options": [
                    "URIs should include action verbs like /getUser or /deleteProduct",
                    "URIs should identify resources using nouns, with HTTP methods defining actions: /users/123 with GET, PUT, DELETE",
                    "URIs should be as short as possible regardless of clarity",
                    "URIs should include implementation details like database table names"
                ],
                "correct": 1,
                "explanation": "REST URIs should identify resources (nouns) while HTTP methods define actions (verbs). This separation creates a uniform interface that's intuitive and consistent across the API.",
                "difficulty": "Intermediate",
                "framework": "Model Context Protocol (MCP)"
            }
        ],

        "JSON-RPC 2.0 Protocol - Level 3": [
            {
                "question": "What is the fundamental difference between JSON-RPC Requests and Notifications, and when would you use each?",
                "options": [
                    "Requests are faster than Notifications",
                    "Requests expect a response and include an 'id' field, while Notifications don't expect responses and omit the 'id' field",
                    "Notifications are more secure than Requests",
                    "There is no difference between them"
                ],
                "correct": 1,
                "explanation": "Requests include an 'id' field and expect a response, enabling request-response patterns. Notifications omit the 'id' and are fire-and-forget, useful for events or commands where no response is needed.",
                "difficulty": "Advanced",
                "framework": "Model Context Protocol (MCP)"
            },
            {
                "question": "How does JSON-RPC 2.0 handle batch requests, and what are the advantages of this approach?",
                "options": [
                    "Batch requests are not supported in JSON-RPC 2.0",
                    "Multiple requests can be sent in a single JSON array, reducing network overhead and allowing parallel processing",
                    "Batch requests require a special header",
                    "Only notifications can be batched, not requests"
                ],
                "correct": 1,
                "explanation": "JSON-RPC 2.0 supports batching by sending an array of request objects, reducing network round trips, improving performance, and enabling servers to process requests in parallel while maintaining proper response ordering.",
                "difficulty": "Advanced",
                "framework": "Model Context Protocol (MCP)"
            }
        ],

        "MCP Fundamental Primitives - Level 4": [
            {
                "question": "In MCP architecture, how does the Client-Server relationship work, and what problem does this solve in AI agent systems?",
                "options": [
                    "MCP clients always run on the same machine as servers",
                    "MCP clients (like Claude Desktop) connect to MCP servers to access external capabilities in a standardized, secure way",
                    "MCP servers are only used for data storage",
                    "MCP clients and servers are the same thing"
                ],
                "correct": 1,
                "explanation": "MCP creates a standardized protocol where AI applications (clients) can securely connect to external services (servers) without requiring custom integrations for each service, solving the integration complexity problem.",
                "difficulty": "PhD",
                "framework": "Model Context Protocol (MCP)"
            },
            {
                "question": "What does 'transport agnostic' mean in MCP context, and why is this architectural decision important?",
                "options": [
                    "MCP only works with HTTP transport",
                    "MCP protocol can work over different communication layers (stdio, HTTP, WebSocket) without changing core functionality",
                    "MCP automatically chooses the best transport method",
                    "Transport agnostic means MCP doesn't use any transport layer"
                ],
                "correct": 1,
                "explanation": "Transport agnostic design allows MCP to work over various communication channels while maintaining the same protocol semantics, providing flexibility in deployment scenarios and integration methods.",
                "difficulty": "PhD",
                "framework": "Model Context Protocol (MCP)"
            }
        ],

        "Advanced MCP Implementation - Level 5": [
            {
                "question": "How do MCP security roots work, and what are the implications for different transport configurations?",
                "options": [
                    "Security roots are only cosmetic features",
                    "Security roots define trusted execution boundaries and have different implications for stateless HTTP vs persistent connections",
                    "Security roots are the same as file system roots",
                    "Security roots are only used for authentication"
                ],
                "correct": 1,
                "explanation": "Security roots establish cryptographic trust boundaries, with different security models for stateless HTTP (per-request verification) vs persistent connections (session-based trust), affecting performance and security trade-offs.",
                "difficulty": "God Level",
                "framework": "Model Context Protocol (MCP)"
            },
            {
                "question": "In a production MCP deployment with sampling and progress notifications, how would you design the architecture for high availability and performance?",
                "options": [
                    "Use a single server for simplicity",
                    "Implement load balancing, request routing, progress state management, and sampling result caching with failure recovery",
                    "Only use HTTP transport for reliability",
                    "Disable all advanced features for stability"
                ],
                "correct": 1,
                "explanation": "Production MCP systems need sophisticated architecture: load balancers for server distribution, state management for progress tracking, caching layers for sampling results, and robust failure recovery mechanisms.",
                "difficulty": "God Level",
                "framework": "Model Context Protocol (MCP)"
            }
        ],

        "MCP OpenAI Integration - Level 5": [
            {
                "question": "How does MCP integration with OpenAI Agents SDK enable new capabilities, and what are the architectural considerations?",
                "options": [
                    "MCP just replaces OpenAI's built-in tools",
                    "MCP enables OpenAI agents to access external systems through standardized interfaces while maintaining security and observability",
                    "MCP and OpenAI agents cannot work together",
                    "MCP only provides data storage for OpenAI agents"
                ],
                "correct": 1,
                "explanation": "MCP integration allows OpenAI agents to securely access external capabilities (databases, APIs, tools) through standardized interfaces, enabling complex workflows while maintaining proper security boundaries and observability.",
                "difficulty": "God Level",
                "framework": "Model Context Protocol (MCP)"
            },
            {
                "question": "When implementing MCP with OpenAI agents for financial services, what are the critical considerations for compliance and security?",
                "options": [
                    "Only consider data encryption",
                    "Implement comprehensive logging, access controls, data residency compliance, audit trails, and secure credential management",
                    "Use default security settings",
                    "Focus only on performance optimization"
                ],
                "correct": 1,
                "explanation": "Financial services require strict compliance: comprehensive audit logging, fine-grained access controls, data residency requirements, complete audit trails, secure credential management, and regulatory compliance (SOX, PCI-DSS, GDPR).",
                "difficulty": "God Level",
                "framework": "Model Context Protocol (MCP)"
            }
        ],

        "Advanced MCP Protocol Implementation": [
            {
                "question": "How would you design an MCP server to handle high-frequency trading data with sub-millisecond latency requirements?",
                "options": [
                    "Use standard HTTP with caching",
                    "Implement memory-mapped files, zero-copy operations, custom binary protocol over TCP, and lock-free data structures",
                    "Use a simple database connection",
                    "Rely on cloud services for speed"
                ],
                "correct": 1,
                "explanation": "Sub-millisecond latency requires advanced techniques: memory-mapped files for data access, zero-copy network operations, custom binary protocols instead of JSON-RPC, lock-free concurrent data structures, and CPU affinity optimization.",
                "difficulty": "God Level",
                "framework": "Model Context Protocol (MCP)"
            },
            {
                "question": "In a distributed MCP deployment across multiple data centers, how would you handle consistency and availability trade-offs?",
                "options": [
                    "Always prioritize consistency over availability",
                    "Implement eventual consistency with conflict resolution, regional failover, and context-aware routing based on CAP theorem principles",
                    "Use synchronous replication everywhere",
                    "Ignore consistency issues"
                ],
                "correct": 1,
                "explanation": "Distributed MCP systems need CAP theorem awareness: eventual consistency for performance, sophisticated conflict resolution algorithms, regional failover strategies, context-aware request routing, and careful consistency vs availability trade-offs based on use case requirements.",
                "difficulty": "God Level",
                "framework": "Model Context Protocol (MCP)"
            }
        ]
    }

def get_comprehensive_framework_concepts():
    """Comprehensive concepts for all frameworks with detailed explanations"""
    return {
        # OpenAI Agents SDK Advanced Concepts
        "Agent Lifecycle Management": "Complete process of agent creation, initialization, execution, monitoring, error handling, and graceful shutdown in production systems.",
        
        "Tool Composition Patterns": "Advanced techniques for combining multiple tools: sequential tool chaining, parallel tool execution, conditional tool selection, and dynamic tool discovery.",
        
        "Context Window Optimization": "Strategies for managing conversation history within model context limits: context compression, sliding windows, selective history retention, and intelligent summarization.",
        
        "Multi-Agent Choreography": "Orchestrating complex workflows involving multiple specialized agents: coordination patterns, conflict resolution, load balancing, and failure recovery.",
        
        "Agent Observability": "Comprehensive monitoring including performance metrics, decision tracing, tool usage analytics, error tracking, and business outcome measurement.",
        
        "Production Deployment Patterns": "Enterprise patterns for agent deployment: containerization, auto-scaling, load balancing, circuit breakers, and blue-green deployments.",
        
        # Building Effective Agents Advanced
        "Agentic Reasoning Loops": "Multi-step reasoning processes where agents analyze, plan, execute, evaluate, and refine their approach iteratively until goals are achieved.",
        
        "Knowledge Graph Construction": "Dynamic building of knowledge graphs from unstructured data, automatic ontology discovery, entity resolution, and relationship extraction.",
        
        "Temporal Reasoning Systems": "Agent capabilities for understanding time-dependent relationships, event sequences, causality, and temporal constraints in decision making.",
        
        "Economic Agent Interactions": "Implementing agent-based economic systems with payment processing, resource allocation, market mechanisms, and trust management.",
        
        "Adaptive Learning Mechanisms": "Systems for agents to learn from experience, improve performance over time, and adapt to changing environments and requirements.",
        
        # MCP Advanced Implementation
        "MCP Security Architecture": "Multi-layered security model including transport security, authentication protocols, authorization mechanisms, and audit systems for enterprise MCP deployments.",
        
        "Protocol Extension Mechanisms": "Methods for extending MCP with custom capabilities, transport layers, resource types, and tool categories while maintaining compatibility.",
        
        "MCP Server Clustering": "Patterns for building scalable MCP server architectures with load distribution, failover, data consistency, and high availability.",
        
        "Cross-Protocol Integration": "Techniques for integrating MCP with other protocols and systems: REST APIs, GraphQL, gRPC, and legacy system integration.",
        
        "Dynamic Resource Discovery": "Advanced MCP features for dynamic service discovery, capability negotiation, and adaptive resource binding in distributed systems."
    }

# Import PhD-level content  
try:
    from .phd_level_study_data import (
        PHD_ALL_QUESTIONS, PHD_FLASHCARDS as PHD_CARDS,
        PHD_TOPIC_DEFINITIONS as PHD_TOPICS,
        get_phd_questions_by_difficulty, get_phd_questions_by_framework,
        get_phd_questions_by_topic
    )
    PHD_QUESTIONS_POOL = PHD_ALL_QUESTIONS
    HAS_PHD_CONTENT = True
except ImportError:
    PHD_QUESTIONS_POOL = []
    PHD_CARDS = []
    PHD_TOPICS = {}
    HAS_PHD_CONTENT = False

# Create enhanced collections function
def get_enhanced_flashcards():
    """Get enhanced flashcards including PhD-level content if available"""
    from .study_data import get_flashcards
    
    # Start with base flashcards
    base_flashcards = get_flashcards()
    enhanced_flashcards = list(base_flashcards.items())  # Convert dict to list of tuples
    
    # Add PhD content if available
    if HAS_PHD_CONTENT:
        for card in PHD_CARDS:
            enhanced_flashcards.append((card.get('front', ''), card.get('back', '')))
    
    # Convert back to dict format
    return dict(enhanced_flashcards)

def get_enhanced_topic_definitions():
    """Get enhanced topic definitions including PhD-level topics if available"""
    # Start with base topic definitions from the function above
    enhanced_definitions = get_all_topic_definitions()
    
    # Add PhD topic definitions if available
    if HAS_PHD_CONTENT:
        for topic, definition in PHD_TOPICS.items():
            if topic not in enhanced_definitions:
                enhanced_definitions[topic] = definition
    
    return enhanced_definitions