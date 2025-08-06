# PhD-Level Agentic AI Study Data
# Ultra-comprehensive questions integrating all fetched documentation
# From Anthropic's Building Effective Agents guide, Panaversity learning repository,
# Level 2 certification materials, and authoritative research sources

from typing import Dict, List, Any
import random

# PhD-Level Building Effective Agents Questions
PHD_BUILDING_AGENTS_QUESTIONS = [
    # Agent Architecture & Design Patterns - PhD Level
    {
        "question": "In the context of agentic architectures, analyze how the Orchestrator-Worker pattern differs from traditional hierarchical agent systems in terms of dynamic task decomposition, load balancing, and failure recovery mechanisms. How would you implement fault-tolerant communication between the orchestrator and worker agents when dealing with non-deterministic LLM responses?",
        "options": [
            "A) Orchestrator-Worker uses static task allocation with predefined failure handling, implementing retry mechanisms with exponential backoff",
            "B) The pattern employs dynamic task decomposition with real-time load balancing, implementing circuit breaker patterns and heartbeat monitoring for fault tolerance",
            "C) It uses round-robin distribution with simple error propagation, relying on LLM consistency for reliability",
            "D) The system implements master-slave architecture with synchronous communication and immediate failure propagation"
        ],
        "correct": "B",
        "explanation": "PhD-level understanding: Orchestrator-Worker pattern in agentic systems requires sophisticated dynamic task decomposition based on real-time analysis of task complexity and worker capabilities. The orchestrator must implement intelligent load balancing considering worker performance metrics and current workload. For fault tolerance with non-deterministic LLMs: 1) Circuit breaker patterns prevent cascade failures, 2) Heartbeat monitoring detects unresponsive workers, 3) State checkpointing enables recovery, 4) Response validation with confidence scoring handles LLM inconsistency, 5) Dynamic rerouting maintains system resilience.",
        "topic": "Agent Architecture",
        "difficulty": "PhD",
        "framework": "Building Effective Agents"
    },
    
    {
        "question": "When implementing the Evaluator-Optimizer (Reflection) pattern for complex reasoning tasks, how would you design a multi-level feedback system that incorporates metacognitive reasoning, handles contradictory feedback from multiple evaluators, and prevents infinite reflection loops while maintaining solution quality?",
        "options": [
            "A) Use simple binary feedback with fixed iteration limits and majority voting for conflict resolution",
            "B) Implement hierarchical metacognitive layers with confidence-weighted feedback aggregation, termination conditions based on convergence metrics, and adaptive reflection depth",
            "C) Apply reinforcement learning with reward shaping and early stopping based on validation accuracy",
            "D) Use ensemble voting with predetermined weights and timeout-based termination"
        ],
        "correct": "B",
        "explanation": "PhD-level implementation requires: 1) Hierarchical metacognitive architecture where higher-level evaluators assess reasoning quality while lower levels focus on factual accuracy, 2) Confidence-weighted feedback aggregation using Bayesian inference to handle contradictory evaluations, 3) Dynamic termination conditions based on solution convergence, feedback consistency, and diminishing returns analysis, 4) Adaptive reflection depth that increases for complex problems and decreases when confidence is high, 5) Loop prevention through solution space tracking and novelty detection.",
        "topic": "Design Patterns",
        "difficulty": "PhD",
        "framework": "Building Effective Agents"
    },

    # Advanced Memory Systems - PhD Level
    {
        "question": "In designing a temporal knowledge graph system like Graphiti for long-term episodic memory in agents, how would you implement efficient temporal reasoning that handles both absolute timestamps and relative temporal relationships, while maintaining causal consistency and enabling counterfactual reasoning?",
        "options": [
            "A) Store all events with Unix timestamps and use simple chronological ordering for queries",
            "B) Implement a hybrid temporal model with interval algebra, causal ordering constraints, and branching timeline support for counterfactual scenarios",
            "C) Use relative time offsets with linear temporal logic for basic temporal queries",
            "D) Apply time-series database techniques with fixed time windows for efficiency"
        ],
        "correct": "B",
        "explanation": "PhD-level temporal reasoning requires: 1) Hybrid temporal model combining absolute timestamps, interval relationships (Allen's interval algebra), and relative temporal constraints, 2) Causal ordering using happened-before relationships and vector clocks for distributed scenarios, 3) Branching timeline support for counterfactual reasoning with possible world semantics, 4) Efficient temporal query processing using temporal indices and constraint satisfaction, 5) Consistency maintenance through temporal constraint propagation and conflict detection, 6) Support for temporal uncertainty and fuzzy timestamps in real-world scenarios.",
        "topic": "Memory Systems",
        "difficulty": "PhD",
        "framework": "Building Effective Agents"
    },

    {
        "question": "Analyze the implications of implementing Neo4j's MERGE operation in a distributed agentic memory system where multiple agents are concurrently updating the knowledge graph. How would you design a consensus mechanism that ensures consistency while preventing deadlocks and maintaining high availability?",
        "options": [
            "A) Use optimistic locking with simple retry mechanisms and eventual consistency",
            "B) Implement distributed consensus using Raft algorithm with vector clocks, conflict-free replicated data types (CRDTs) for concurrent updates, and semantic conflict resolution",
            "C) Apply two-phase commit with centralized coordination for all graph updates",
            "D) Use pessimistic locking with timeout-based deadlock detection"
        ],
        "correct": "B",
        "explanation": "PhD-level distributed memory system design: 1) Raft consensus algorithm ensures strong consistency across replicas while handling node failures gracefully, 2) Vector clocks track causal relationships between concurrent updates from different agents, 3) CRDTs (like OR-Sets for relationships) allow conflict-free merging of concurrent modifications, 4) Semantic conflict resolution using domain-specific rules and ontology constraints, 5) Multi-version concurrency control for read consistency, 6) Partition tolerance through quorum-based operations and eventual consistency guarantees.",
        "topic": "Distributed Memory",
        "difficulty": "PhD",
        "framework": "Building Effective Agents"
    },

    # Advanced RAG and Retrieval - PhD Level
    {
        "question": "In implementing a sophisticated RAG system for agentic workflows, how would you design a multi-modal retrieval architecture that combines vector similarity, graph traversal, and symbolic reasoning while handling cross-modal queries and maintaining semantic coherence across different data types?",
        "options": [
            "A) Use separate vector databases for each modality with simple score aggregation",
            "B) Implement unified embedding space with cross-modal transformers, multi-hop graph reasoning, and semantic consistency validation through constraint satisfaction",
            "C) Apply modality-specific retrievers with weighted voting and threshold-based filtering",
            "D) Use pre-trained models with fixed fusion strategies and basic ranking algorithms"
        ],
        "correct": "B",
        "explanation": "PhD-level multi-modal RAG architecture: 1) Unified embedding space using cross-modal transformers (like CLIP) to enable semantic similarity across modalities, 2) Multi-hop graph reasoning to traverse relationships between concepts across different data types, 3) Symbolic reasoning layer using knowledge graphs and ontologies for logical consistency, 4) Semantic coherence validation through constraint satisfaction and consistency checking, 5) Adaptive query decomposition for complex cross-modal queries, 6) Dynamic fusion strategies based on query complexity and available evidence.",
        "topic": "Multi-modal RAG",
        "difficulty": "PhD",
        "framework": "Building Effective Agents"
    },

    # Agentic Economy & Payments - PhD Level
    {
        "question": "Analyze the transition from API economy to agentic economy in terms of economic theory and system architecture. How would you design a trustless payment protocol for autonomous agents that handles micro-transactions, prevents double-spending, and ensures atomic execution of complex multi-party transactions?",
        "options": [
            "A) Use traditional banking APIs with agent authentication and simple transaction logging",
            "B) Implement blockchain-based smart contracts with state channels for micro-transactions, atomic swap protocols for multi-party exchanges, and zero-knowledge proofs for privacy",
            "C) Apply escrow services with centralized validation and basic fraud detection",
            "D) Use digital wallets with pre-authorized spending limits and manual approval processes"
        ],
        "correct": "B",
        "explanation": "PhD-level agentic economy design: 1) Blockchain foundation provides trustless, decentralized infrastructure removing need for central authorities, 2) State channels enable high-frequency micro-transactions off-chain with periodic settlement, 3) Atomic swap protocols ensure either all parties in multi-agent transactions succeed or all fail, preventing partial states, 4) Zero-knowledge proofs maintain transaction privacy while proving validity, 5) Smart contracts encode complex business logic and automatic execution, 6) Consensus mechanisms (PoS/PoW) ensure network security and prevent double-spending attacks.",
        "topic": "Agentic Economy",
        "difficulty": "PhD",
        "framework": "Building Effective Agents"
    },

    # Tool Integration & Workflow Orchestration - PhD Level  
    {
        "question": "In designing an advanced tool orchestration system for agentic workflows, how would you implement dynamic tool composition where agents can combine primitive tools into complex workflows, handle tool failures gracefully, and optimize execution paths based on real-time performance metrics?",
        "options": [
            "A) Use static tool chains with predefined error handling and fixed optimization strategies",
            "B) Implement dynamic programming-based tool composition with reinforcement learning for path optimization, circuit breaker patterns for failure handling, and adaptive resource allocation",
            "C) Apply simple sequential execution with retry mechanisms and basic load balancing",
            "D) Use workflow templates with manual optimization and centralized error logging"
        ],
        "correct": "B",
        "explanation": "PhD-level tool orchestration: 1) Dynamic programming algorithms for optimal tool composition considering cost, latency, and reliability metrics, 2) Reinforcement learning agents that learn optimal execution paths through experience and adapt to changing conditions, 3) Circuit breaker patterns prevent cascade failures and provide graceful degradation, 4) Adaptive resource allocation based on real-time performance monitoring and predictive analytics, 5) Tool dependency graph analysis for parallel execution opportunities, 6) Fault tolerance through alternative tool discovery and automatic fallback strategies.",
        "topic": "Tool Orchestration", 
        "difficulty": "PhD",
        "framework": "Building Effective Agents"
    },

    # LLM Augmentation Theory - PhD Level
    {
        "question": "Evaluate the theoretical foundations of LLM augmentation through the lens of computational cognitive science. How do retrieval, tool use, and memory systems in agentic architectures relate to theories of extended mind, distributed cognition, and the frame problem in AI?",
        "options": [
            "A) These are purely engineering optimizations without theoretical grounding in cognitive science",
            "B) LLM augmentation instantiates extended mind theory through cognitive coupling, addresses the frame problem via selective attention mechanisms, and implements distributed cognition across hybrid human-AI-environment systems",
            "C) The systems simply extend LLM capabilities without deeper cognitive implications",
            "D) Augmentation techniques are equivalent to traditional database and API integration patterns"
        ],
        "correct": "B",
        "explanation": "PhD theoretical analysis: 1) Extended Mind Theory (Clark & Chalmers) - retrieval and tool systems create cognitive coupling where external resources become part of the agent's cognitive apparatus, 2) Frame Problem solution - selective attention through retrieval filters relevant information, reducing combinatorial explosion of possibilities, 3) Distributed Cognition (Hutchins) - agentic systems implement cognitive processes across multiple components (LLM, tools, memory, environment), 4) Cognitive Load Theory - memory systems offload working memory constraints, enabling more complex reasoning, 5) Situated Cognition - tool use grounds abstract reasoning in environmental interactions.",
        "topic": "Cognitive Theory",
        "difficulty": "PhD", 
        "framework": "Building Effective Agents"
    }
]

# PhD-Level MCP Questions integrating HTTP, REST, JSON-RPC theory
PHD_MCP_QUESTIONS = [
    # HTTP Protocol Theory - PhD Level
    {
        "question": "Analyze HTTP/3's migration from TCP to QUIC in terms of head-of-line blocking elimination and its implications for agentic communication protocols. How would you design an MCP implementation that leverages HTTP/3's multiplexing capabilities for concurrent agent-tool interactions while maintaining message ordering guarantees?",
        "options": [
            "A) Use separate HTTP/1.1 connections for each tool call to avoid complexity",
            "B) Implement stream prioritization with dependency trees, out-of-order delivery handling through sequence numbering, and adaptive flow control based on tool response characteristics",
            "C) Apply simple round-robin multiplexing with basic error recovery",
            "D) Use HTTP/2 server push for tool result delivery with fixed priority schemes"
        ],
        "correct": "B",
        "explanation": "PhD-level HTTP/3 optimization for MCP: 1) Stream prioritization using dependency trees allows critical agent communications (like cancellations) to take precedence over routine tool calls, 2) Out-of-order delivery requires sequence numbering and reordering buffers to maintain causal consistency in agent workflows, 3) Adaptive flow control monitors tool response patterns and adjusts stream limits dynamically, 4) QUIC's 0-RTT connection establishment reduces agent response latency for subsequent interactions, 5) Connection migration handles network changes seamlessly in mobile agent deployments.",
        "topic": "HTTP Protocol",
        "difficulty": "PhD",
        "framework": "MCP"
    },

    # REST vs JSON-RPC Theoretical Analysis - PhD Level
    {
        "question": "From a distributed systems theory perspective, evaluate why JSON-RPC is fundamentally better suited for agentic protocols than REST, considering the CAP theorem, eventual consistency requirements, and the impedance mismatch between resource-oriented and procedural paradigms in AI agent communication.",
        "options": [
            "A) JSON-RPC and REST are equivalent for agent communication with minor syntactic differences",
            "B) JSON-RPC's procedural model aligns with agent goal-oriented behavior, supports better consistency semantics through explicit method calls, and enables more efficient multiplexing of concurrent operations over persistent connections",
            "C) REST is superior due to its stateless nature and caching capabilities for agent interactions",
            "D) The choice depends only on developer preference with no theoretical implications"
        ],
        "correct": "B",
        "explanation": "PhD theoretical analysis: 1) Procedural vs Resource paradigm - agents operate through goal-directed actions (procedures) rather than resource manipulation, making JSON-RPC's method-call model more semantically aligned, 2) CAP theorem implications - JSON-RPC over persistent connections enables stronger consistency (CP) for critical agent operations while REST's stateless nature pushes toward AP systems, 3) Multiplexing efficiency - single connection with request/response correlation reduces connection overhead and enables better resource utilization, 4) Semantic clarity - explicit method names ('tools.call', 'sampling.request') provide clearer intent than REST's HTTP verb + URI combinations for agent operations.",
        "topic": "Protocol Theory",
        "difficulty": "PhD",
        "framework": "MCP"
    },

    # MCP Transport Abstraction - PhD Level
    {
        "question": "Design a theoretical framework for MCP's transport abstraction that can handle both synchronous request-response and asynchronous event-driven communication patterns while maintaining semantic consistency across different transport layers (WebSocket, HTTP, stdio, SSE). How would you ensure message delivery guarantees and ordering semantics?",
        "options": [
            "A) Use a simple adapter pattern with best-effort delivery and basic timeout handling",
            "B) Implement a message-oriented middleware abstraction with configurable delivery semantics (at-most-once, at-least-once, exactly-once), causal ordering preservation, and transport-specific optimization strategies",
            "C) Apply publish-subscribe pattern with eventual consistency and basic retry mechanisms",
            "D) Use synchronous RPC calls exclusively to avoid complexity"
        ],
        "correct": "B",
        "explanation": "PhD-level transport abstraction design: 1) Message-oriented middleware (MOM) abstraction decouples MCP semantics from transport specifics, 2) Configurable delivery guarantees: at-most-once for lightweight notifications, at-least-once for important tool calls, exactly-once for critical operations using idempotency tokens, 3) Causal ordering preservation through vector clocks or logical timestamps across all transports, 4) Transport-specific optimizations: WebSocket for low-latency streaming, HTTP for firewall traversal, stdio for local processes, SSE for server-initiated events, 5) Failure detection and recovery adapted to transport characteristics (connection-based vs connectionless).",
        "topic": "Transport Abstraction",
        "difficulty": "PhD", 
        "framework": "MCP"
    },

    # MCP Security & Trust - PhD Level
    {
        "question": "Analyze MCP's security model in the context of zero-trust architecture for agentic systems. How would you design capability-based security with fine-grained access control that handles dynamic trust relationships between agents, implements secure sandboxing for tool execution, and prevents privilege escalation attacks?",
        "options": [
            "A) Use simple API keys with basic role-based access control and static permissions",
            "B) Implement object-capability security with unforgeable capability tokens, dynamic trust attestation through cryptographic proofs, mandatory access control for tool execution, and capability attenuation for privilege minimization",
            "C) Apply OAuth 2.0 with predefined scopes and centralized authorization servers",
            "D) Use mutual TLS authentication with certificate-based authorization"
        ],
        "correct": "B",
        "explanation": "PhD-level security architecture: 1) Object-capability model where capabilities are unforgeable tokens that grant specific permissions, eliminating ambient authority vulnerabilities, 2) Dynamic trust attestation using cryptographic proofs (attestation tokens) that agents can verify independently, 3) Mandatory access control (MAC) ensures tools execute with minimal required privileges through security domains and sandboxing, 4) Capability attenuation allows agents to delegate restricted subsets of their capabilities to other agents, 5) Distributed capability revocation through capability versioning and distributed blacklists, 6) Hardware security modules (HSMs) for secure capability storage and cryptographic operations.",
        "topic": "Security Model",
        "difficulty": "PhD",
        "framework": "MCP"
    },

    # MCP Sampling & Advanced Features - PhD Level
    {
        "question": "Design a sophisticated sampling strategy for MCP that balances exploration vs exploitation in tool selection, handles multi-objective optimization for competing metrics (speed, accuracy, cost), and adapts to changing agent behavior patterns through online learning algorithms.",
        "options": [
            "A) Use random sampling with fixed probability distributions and basic performance tracking",
            "B) Implement multi-armed bandit algorithms with contextual information, Pareto-optimal solution discovery for multi-objective optimization, and adaptive learning rates based on environment stability",
            "C) Apply greedy selection with simple performance caching and periodic randomization",
            "D) Use round-robin scheduling with basic load balancing and timeout handling"
        ],
        "correct": "B",
        "explanation": "PhD-level sampling optimization: 1) Multi-armed bandit algorithms (UCB, Thompson Sampling) balance exploration of new tools with exploitation of known good performers, 2) Contextual bandits incorporate agent state, task complexity, and environmental factors into selection decisions, 3) Pareto-optimal solution discovery uses evolutionary algorithms to find tools that optimize multiple competing objectives simultaneously, 4) Adaptive learning rates adjust based on environment stability detected through change point analysis, 5) Meta-learning approaches that learn how to adapt to new agent behaviors quickly, 6) Regret minimization bounds ensure theoretical guarantees on sampling performance.",
        "topic": "Sampling Strategy",
        "difficulty": "PhD",
        "framework": "MCP"
    }
]

# PhD-Level OpenAI Agents SDK Integration Questions
PHD_OPENAI_SDK_QUESTIONS = [
    {
        "question": "Analyze the integration of MCP with OpenAI's Agents SDK from a software architecture perspective. How would you design a bridging layer that handles impedance mismatch between OpenAI's function calling paradigm and MCP's tool protocol while maintaining performance, type safety, and extensibility?",
        "options": [
            "A) Use simple wrapper functions that convert between the two formats with basic error handling",
            "B) Implement a sophisticated adapter pattern with protocol translation, type system unification through schema mapping, asynchronous operation bridging, and capability negotiation",
            "C) Create separate implementations for each system without integration",
            "D) Use middleware that logs all interactions but doesn't modify them"
        ],
        "correct": "B",
        "explanation": "PhD-level integration design: 1) Protocol translation layer that maps OpenAI function calling schema to MCP tool definitions while preserving semantic meaning, 2) Type system unification through bidirectional schema mapping with validation and coercion rules, 3) Asynchronous operation bridging handles OpenAI's async patterns with MCP's request-response model using futures and promises, 4) Capability negotiation allows dynamic discovery of supported features across both systems, 5) Performance optimization through connection pooling, message batching, and intelligent caching strategies.",
        "topic": "SDK Integration",
        "difficulty": "PhD",
        "framework": "OpenAI Agents SDK"
    }
]

# Comprehensive topic definitions with PhD-level depth
PHD_TOPIC_DEFINITIONS = {
    "Agent Architecture": {
        "definition": "Advanced architectural patterns for designing autonomous agent systems including Orchestrator-Worker, Evaluator-Optimizer, and hierarchical multi-agent coordination with fault tolerance and scalability considerations.",
        "key_concepts": [
            "Dynamic task decomposition algorithms",
            "Load balancing and resource allocation strategies", 
            "Fault tolerance patterns (circuit breakers, heartbeat monitoring)",
            "Inter-agent communication protocols and message passing",
            "Scalability patterns and distributed coordination mechanisms"
        ],
        "frameworks": ["Building Effective Agents"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"]
    },
    
    "Design Patterns": {
        "definition": "Sophisticated architectural patterns for agentic systems including reflection mechanisms, metacognitive reasoning, and adaptive behavior patterns with theoretical grounding in cognitive science.",
        "key_concepts": [
            "Metacognitive reflection and self-monitoring systems",
            "Multi-level feedback aggregation and conflict resolution", 
            "Convergence analysis and termination conditions",
            "Solution space exploration and novelty detection",
            "Adaptive reasoning depth and complexity management"
        ],
        "frameworks": ["Building Effective Agents"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"]
    },

    "Memory Systems": {
        "definition": "Advanced temporal knowledge representation and reasoning systems including graph-based memory, causal consistency, and distributed consensus mechanisms for multi-agent environments.",
        "key_concepts": [
            "Temporal knowledge graphs and interval algebra",
            "Causal ordering and vector clocks for distributed systems",
            "Counterfactual reasoning and possible world semantics",
            "Conflict-free replicated data types (CRDTs) for concurrent updates",
            "Semantic conflict resolution and ontology-based consistency"
        ],
        "frameworks": ["Building Effective Agents"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"]
    },

    "Multi-modal RAG": {
        "definition": "Sophisticated retrieval-augmented generation systems that handle multiple data modalities with cross-modal reasoning, semantic coherence validation, and unified embedding representations.",
        "key_concepts": [
            "Cross-modal transformers and unified embedding spaces",
            "Multi-hop graph reasoning across different data types",
            "Symbolic reasoning integration with neural approaches",
            "Semantic consistency validation through constraint satisfaction",
            "Adaptive query decomposition for complex information needs"
        ],
        "frameworks": ["Building Effective Agents"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"]
    },

    "Agentic Economy": {
        "definition": "Economic and technological frameworks for autonomous agent participation in digital economies, including trustless payment systems, blockchain integration, and multi-party transaction protocols.",
        "key_concepts": [
            "Blockchain-based trustless payment protocols",
            "State channels for high-frequency micro-transactions",
            "Atomic swap protocols for multi-party exchanges", 
            "Zero-knowledge proofs for transaction privacy",
            "Smart contracts and automated execution frameworks"
        ],
        "frameworks": ["Building Effective Agents"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"]
    },

    "HTTP Protocol": {
        "definition": "Advanced HTTP protocol theory including HTTP/3 optimization, QUIC transport benefits, multiplexing strategies, and performance optimization for agentic communication patterns.",
        "key_concepts": [
            "HTTP/3 and QUIC transport layer optimizations",
            "Stream prioritization and dependency trees",
            "Head-of-line blocking elimination strategies",
            "Connection migration and 0-RTT establishment",
            "Adaptive flow control for dynamic workloads"
        ],
        "frameworks": ["MCP"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"]
    },

    "Protocol Theory": {
        "definition": "Theoretical analysis of communication protocols for distributed agentic systems, including CAP theorem implications, consistency models, and paradigm comparisons between resource-oriented and procedural approaches.",
        "key_concepts": [
            "CAP theorem applications in agentic systems",
            "Consistency semantics and eventual consistency models",
            "Procedural vs resource-oriented paradigm analysis",
            "Semantic alignment with agent goal-directed behavior",
            "Multiplexing efficiency and connection management"
        ],
        "frameworks": ["MCP"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"] 
    },

    "Transport Abstraction": {
        "definition": "Advanced message-oriented middleware design for protocol-agnostic communication with configurable delivery guarantees, causal ordering, and transport-specific optimizations.",
        "key_concepts": [
            "Message-oriented middleware (MOM) architectures",
            "Configurable delivery semantics (at-most-once, exactly-once)",
            "Causal ordering preservation across transport layers",
            "Transport-specific optimization strategies",
            "Failure detection and recovery mechanisms"
        ],
        "frameworks": ["MCP"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"]
    },

    "Security Model": {
        "definition": "Zero-trust security architecture for agentic systems with capability-based access control, dynamic trust attestation, and secure sandboxing for tool execution environments.",
        "key_concepts": [
            "Object-capability security models",
            "Dynamic trust attestation through cryptographic proofs",
            "Mandatory access control (MAC) for tool sandboxing",
            "Capability attenuation and delegation mechanisms", 
            "Distributed capability revocation strategies"
        ],
        "frameworks": ["MCP"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"]
    },

    "Sampling Strategy": {
        "definition": "Advanced sampling and optimization algorithms for tool selection in agentic systems, including multi-armed bandit approaches, multi-objective optimization, and adaptive learning mechanisms.",
        "key_concepts": [
            "Multi-armed bandit algorithms for exploration-exploitation",
            "Contextual bandits with environmental factor integration",
            "Pareto-optimal solution discovery for competing objectives",
            "Adaptive learning rates based on environment stability",
            "Regret minimization and theoretical performance bounds"
        ],
        "frameworks": ["MCP"],
        "difficulty_levels": ["Advanced", "PhD", "God Level"]
    }
}

# Combined question pool for comprehensive testing
PHD_ALL_QUESTIONS = PHD_BUILDING_AGENTS_QUESTIONS + PHD_MCP_QUESTIONS + PHD_OPENAI_SDK_QUESTIONS

# PhD-level flashcards with sophisticated concepts
PHD_FLASHCARDS = [
    {
        "front": "Distributed Consensus in Agentic Memory Systems",
        "back": "How do you implement consensus in a distributed knowledge graph where multiple agents update memory concurrently?\n\nSolution: Use Raft consensus algorithm with vector clocks for causal ordering, CRDTs for conflict-free merging, and semantic conflict resolution through ontology constraints. Implement quorum-based operations for partition tolerance and multi-version concurrency control for read consistency.",
        "topic": "Memory Systems",
        "difficulty": "PhD",
        "framework": "Building Effective Agents"
    },
    
    {
        "front": "MCP Transport Abstraction Theory",
        "back": "Why is transport abstraction critical for MCP's design philosophy?\n\nAnswer: Transport abstraction enables MCP to provide consistent semantics across different communication layers (WebSocket, HTTP, stdio) while optimizing for each transport's characteristics. It implements configurable delivery guarantees, maintains causal ordering through logical timestamps, and provides transport-specific optimizations (e.g., WebSocket for low-latency, HTTP for firewall traversal).",
        "topic": "Transport Abstraction", 
        "difficulty": "PhD",
        "framework": "MCP"
    },
    
    {
        "front": "Extended Mind Theory in LLM Augmentation",
        "back": "How does LLM augmentation through tools and retrieval relate to extended mind theory?\n\nExplanation: LLM augmentation instantiates Clark & Chalmers' extended mind theory by creating cognitive coupling between the LLM, external tools, and information sources. The retrieval system becomes part of the agent's extended cognitive apparatus, while tools act as cognitive prosthetics that expand the agent's capabilities beyond its internal processing boundaries.",
        "topic": "Cognitive Theory",
        "difficulty": "PhD",
        "framework": "Building Effective Agents"
    }
]

def get_phd_questions_by_difficulty(difficulty: str) -> List[Dict]:
    """Return PhD-level questions filtered by difficulty level."""
    if difficulty == "PhD":
        return PHD_ALL_QUESTIONS
    elif difficulty == "God Level":
        # God Level includes PhD + additional complexity
        return PHD_ALL_QUESTIONS  # Can extend with even more advanced questions
    else:
        return []

def get_phd_questions_by_framework(framework: str) -> List[Dict]:
    """Return PhD-level questions filtered by framework."""
    framework_map = {
        "Building Effective Agents": PHD_BUILDING_AGENTS_QUESTIONS,
        "MCP": PHD_MCP_QUESTIONS, 
        "OpenAI Agents SDK": PHD_OPENAI_SDK_QUESTIONS
    }
    return framework_map.get(framework, [])

def get_phd_questions_by_topic(topic: str) -> List[Dict]:
    """Return PhD-level questions filtered by topic."""
    return [q for q in PHD_ALL_QUESTIONS if q.get("topic") == topic]

# Export main data structures
__all__ = [
    "PHD_ALL_QUESTIONS",
    "PHD_BUILDING_AGENTS_QUESTIONS", 
    "PHD_MCP_QUESTIONS",
    "PHD_OPENAI_SDK_QUESTIONS",
    "PHD_TOPIC_DEFINITIONS",
    "PHD_FLASHCARDS",
    "get_phd_questions_by_difficulty",
    "get_phd_questions_by_framework", 
    "get_phd_questions_by_topic"
]