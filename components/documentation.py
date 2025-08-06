import streamlit as st
import pandas as pd
from data.study_data import get_difficulty_levels

def show_comprehensive_docs():
    """Display comprehensive documentation with framework selection and difficulty levels"""
    st.header("📚 Comprehensive Agentic AI Documentation")
    st.markdown("Complete knowledge base covering every point and scenario for Building Effective Agents, Model Context Protocol, and OpenAI Agents SDK")
    
    # Framework Selection
    st.sidebar.subheader("🔧 Framework Selection")
    framework = st.sidebar.selectbox(
        "Choose your framework:",
        ["All Frameworks", "Building Effective Agents", "Model Context Protocol (MCP)", "OpenAI Agents SDK"]
    )
    
    # Difficulty Level Selection
    st.sidebar.subheader("📊 Difficulty Level")
    difficulty_levels = list(get_difficulty_levels().keys())
    selected_difficulty = st.sidebar.selectbox(
        "Choose difficulty level:",
        ["All Levels"] + difficulty_levels
    )
    
    # Search functionality
    search_term = st.text_input("🔍 Search documentation:", placeholder="Enter keywords to search...")
    
    # Display content based on selections
    _display_documentation_content(framework, selected_difficulty, search_term)

def _display_documentation_content(framework, difficulty, search_term):
    """Display filtered documentation content"""
    
    if framework == "All Frameworks" or framework == "Building Effective Agents":
        _show_building_effective_agents_docs(difficulty, search_term)
    
    if framework == "All Frameworks" or framework == "Model Context Protocol (MCP)":
        _show_mcp_docs(difficulty, search_term)
    
    if framework == "All Frameworks" or framework == "OpenAI Agents SDK":
        _show_openai_agents_docs(difficulty, search_term)

def _show_building_effective_agents_docs(difficulty, search_term):
    """Comprehensive Building Effective Agents documentation"""
    st.subheader("🏗️ Building Effective Agents - Complete Documentation")
    
    # Core Concepts
    with st.expander("🧠 Core Concepts and Fundamentals", expanded=True):
        st.markdown("""
        ### Agent Architecture Overview
        
        **What is an Agentic System?**
        An agentic system is an AI application that can:
        - Make autonomous decisions
        - Use tools to interact with the environment
        - Maintain memory across interactions
        - Plan and execute multi-step tasks
        - Learn and adapt from experience
        
        **Core Components:**
        1. **LLM (Large Language Model)**: The reasoning engine
        2. **Tools**: External capabilities (APIs, databases, file systems)
        3. **Memory**: Short-term (conversation) and long-term (persistent storage)
        4. **Planning**: Task decomposition and execution strategy
        5. **Evaluation**: Performance assessment and feedback loops
        """)
        
        if difficulty != "Normal" and difficulty != "All Levels":
            st.markdown("""
            ### Advanced Architecture Patterns
            
            **Multi-Agent Systems:**
            - Hierarchical agent structures
            - Peer-to-peer agent communication
            - Specialized agent roles (researcher, executor, evaluator)
            
            **Hybrid Approaches:**
            - Symbolic + Neural reasoning
            - Rule-based + LLM decision making
            - Traditional ML + Agent frameworks
            """)
    
    # Design Patterns
    with st.expander("🎨 Design Patterns and Implementation Strategies"):
        st.markdown("""
        ### Essential Design Patterns
        
        **1. Routing Pattern**
        ```python
        def route_request(user_input):
            if "weather" in user_input:
                return weather_agent
            elif "calendar" in user_input:
                return calendar_agent
            else:
                return general_agent
        ```
        
        **2. Prompt Chaining**
        - Sequential prompt execution
        - Context passing between chains
        - Error handling and retry mechanisms
        
        **3. Parallelization**
        - Concurrent tool execution
        - Parallel agent processing
        - Result aggregation strategies
        
        **4. Planner-Worker Pattern**
        - Planning agent creates task breakdown
        - Worker agents execute specific tasks
        - Coordinator manages workflow
        
        **5. Evaluator-Optimizer**
        - Performance monitoring
        - Continuous improvement loops
        - A/B testing frameworks
        
        **6. Reflection Pattern**
        - Self-assessment capabilities
        - Learning from mistakes
        - Performance optimization
        
        **7. Delegation Pattern**
        - Task handoff mechanisms
        - Specialized agent selection
        - Context preservation
        """)
        
        if difficulty in ["Advanced", "PhD", "God Level"] or difficulty == "All Levels":
            st.markdown("""
            ### Advanced Implementation Scenarios
            
            **Enterprise Integration:**
            - Multi-tenant agent systems
            - Enterprise security patterns
            - Scalability considerations
            - Monitoring and observability
            
            **Edge Cases and Error Handling:**
            - Network failure recovery
            - Tool unavailability scenarios
            - Memory overflow handling
            - Infinite loop prevention
            """)
    
    # Memory Systems
    with st.expander("🧠 Memory Systems and Knowledge Management"):
        st.markdown("""
        ### Memory Architecture Types
        
        **1. Vector Databases**
        - Embedding-based retrieval
        - Semantic similarity search
        - Popular implementations: Pinecone, Weaviate, ChromaDB
        
        **2. Graph Databases (Neo4j)**
        ```cypher
        CREATE (agent:Agent {name: "Assistant"})
        CREATE (memory:Memory {content: "User prefers concise responses"})
        CREATE (agent)-[:REMEMBERS]->(memory)
        ```
        
        **3. Temporal Knowledge (Graphiti)**
        - Time-aware knowledge representation
        - Event sequencing and causality
        - Temporal reasoning capabilities
        
        **4. Hybrid Memory Systems**
        - Combined vector + graph storage
        - Multi-modal memory (text, images, audio)
        - Hierarchical memory structures
        """)
        
        if difficulty in ["PhD", "God Level"] or difficulty == "All Levels":
            st.markdown("""
            ### Advanced Memory Patterns
            
            **Memory Consolidation:**
            - Short-term to long-term transfer
            - Memory compression techniques
            - Forgetting mechanisms
            
            **Distributed Memory:**
            - Multi-agent shared memory
            - Consensus mechanisms
            - Conflict resolution strategies
            """)
    
    # Tools and Augmentation
    with st.expander("🔧 Tools and LLM Augmentation"):
        st.markdown("""
        ### Tool Integration Strategies
        
        **1. Function Calling**
        ```python
        def get_weather(location: str) -> str:
            # Weather API integration
            return f"Weather in {location}: Sunny, 72°F"
        
        tools = [get_weather]
        agent = Agent(tools=tools)
        ```
        
        **2. API Integration**
        - REST API connections
        - GraphQL queries
        - Webhook handling
        - Rate limiting and retry logic
        
        **3. Database Operations**
        - SQL query generation
        - NoSQL document operations
        - Transaction management
        - Data validation
        
        **4. File System Operations**
        - File reading/writing
        - Directory traversal
        - Permission handling
        - Backup and versioning
        """)
    
    # Retrieval Systems
    with st.expander("🔍 Retrieval and RAG Implementation"):
        st.markdown("""
        ### Retrieval-Augmented Generation (RAG)
        
        **Basic RAG Pipeline:**
        1. Document ingestion and chunking
        2. Embedding generation
        3. Vector storage
        4. Query processing
        5. Similarity search
        6. Context injection
        7. Response generation
        
        **Advanced RAG Techniques:**
        - Multi-query retrieval
        - Re-ranking strategies
        - Contextual compression
        - Adaptive chunk sizing
        
        **Implementation Example:**
        ```python
        def rag_pipeline(query, vector_db):
            # Embed query
            query_embedding = embed(query)
            
            # Retrieve relevant chunks
            chunks = vector_db.similarity_search(query_embedding, k=5)
            
            # Generate response with context
            context = "\\n".join(chunks)
            response = llm.generate(f"Context: {context}\\nQuery: {query}")
            
            return response
        ```
        """)
    
    # Economy and Payments
    with st.expander("💰 Agentic Economy and Payment Integration"):
        st.markdown("""
        ### Payment System Integration
        
        **Stripe Integration:**
        ```python
        import stripe
        
        def process_payment(amount, currency="usd"):
            stripe.api_key = "your_secret_key"
            
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                automatic_payment_methods={'enabled': True}
            )
            
            return payment_intent
        ```
        
        **Economic Models:**
        - Pay-per-use agents
        - Subscription-based access
        - Performance-based pricing
        - Token-based economies
        
        **Trust and Security:**
        - Authentication mechanisms
        - Authorization patterns
        - Audit trails
        - Fraud detection
        """)

def _show_mcp_docs(difficulty, search_term):
    """Comprehensive Model Context Protocol documentation"""
    st.subheader("🔧 Model Context Protocol (MCP) - Complete Documentation")
    
    # Protocol Fundamentals
    with st.expander("🌐 Protocol Fundamentals and Architecture", expanded=True):
        st.markdown("""
        ### What is Model Context Protocol?
        
        MCP is a standardized protocol for connecting AI models with external data sources and tools. It enables:
        - Seamless integration between LLMs and external systems
        - Standardized communication patterns
        - Scalable architecture for AI applications
        - Secure data access and tool execution
        
        ### Core Components
        
        **1. MCP Client**
        - Initiates connections to MCP servers
        - Manages protocol sessions
        - Handles authentication and security
        
        **2. MCP Server**
        - Exposes resources, tools, and prompts
        - Implements protocol handlers
        - Manages data access and permissions
        
        **3. Resources**
        - Static or dynamic content
        - File systems, databases, APIs
        - Structured data representations
        
        **4. Tools**
        - Executable functions
        - External API calls
        - System operations
        
        **5. Prompts**
        - Reusable prompt templates
        - Parameterized instructions
        - Context-aware prompts
        """)
    
    # Transport Layers
    with st.expander("🚀 Transport Layers and Communication"):
        st.markdown("""
        ### Transport Layer Options
        
        **1. Standard I/O (Stdio)**
        ```python
        # Client-side stdio connection
        import asyncio
        from mcp import ClientSession, StdioClientTransport
        
        async def connect_stdio():
            transport = StdioClientTransport()
            session = ClientSession(transport)
            await session.initialize()
        ```
        
        **2. HTTP Transport**
        ```python
        # HTTP-based MCP server
        from mcp.server import Server
        from mcp.server.transport.http import HTTPTransport
        
        server = Server("example-server")
        transport = HTTPTransport("http://localhost:8000")
        ```
        
        **3. WebSocket Transport**
        - Real-time bidirectional communication
        - Persistent connections
        - Low latency interactions
        
        **4. Server-Sent Events (SSE)**
        - Unidirectional server-to-client streaming
        - Progress notifications
        - Live updates
        """)
    
    # HTTP Theory Deep Dive
    with st.expander("📡 HTTP Theory and Implementation"):
        st.markdown("""
        ### HTTP Methods and Status Codes
        
        **HTTP Methods:**
        - **GET**: Retrieve data (idempotent, cacheable)
        - **POST**: Create new resources (non-idempotent)
        - **PUT**: Update/replace resources (idempotent)
        - **PATCH**: Partial updates (idempotent)
        - **DELETE**: Remove resources (idempotent)
        - **HEAD**: Get headers only (metadata)
        - **OPTIONS**: Get allowed methods (CORS)
        
        **Status Code Categories:**
        - **1xx Informational**: Request received, processing
        - **2xx Success**: Request successful
        - **3xx Redirection**: Further action needed
        - **4xx Client Error**: Client-side error
        - **5xx Server Error**: Server-side error
        
        **Common Status Codes:**
        ```
        200 OK - Success
        201 Created - Resource created
        400 Bad Request - Invalid request
        401 Unauthorized - Authentication required
        403 Forbidden - Access denied
        404 Not Found - Resource not found
        500 Internal Server Error - Server error
        ```
        """)
    
    # REST Architecture
    with st.expander("🏛️ REST Architecture Principles"):
        st.markdown("""
        ### REST Principles
        
        **1. Statelessness**
        - Each request contains all necessary information
        - No server-side session storage
        - Improved scalability and reliability
        
        **2. Uniform Interface**
        - Consistent API design
        - Resource identification in requests
        - Self-descriptive messages
        - HATEOAS (Hypermedia as the Engine of Application State)
        
        **3. Resource Identification**
        ```
        GET /api/users/123          # Get specific user
        POST /api/users             # Create new user
        PUT /api/users/123          # Update user
        DELETE /api/users/123       # Delete user
        ```
        
        **4. Cacheability**
        - Responses should be cacheable
        - Cache-Control headers
        - ETags for conditional requests
        
        **5. Client-Server Architecture**
        - Separation of concerns
        - Independent evolution
        - Portability and scalability
        """)
    
    # JSON-RPC Implementation
    with st.expander("📋 JSON-RPC 2.0 Protocol"):
        st.markdown("""
        ### JSON-RPC 2.0 Specification
        
        **Request Format:**
        ```json
        {
            "jsonrpc": "2.0",
            "method": "getUser",
            "params": {"id": 123},
            "id": 1
        }
        ```
        
        **Response Format:**
        ```json
        {
            "jsonrpc": "2.0",
            "result": {"name": "John", "id": 123},
            "id": 1
        }
        ```
        
        **Error Response:**
        ```json
        {
            "jsonrpc": "2.0",
            "error": {
                "code": -32600,
                "message": "Invalid Request"
            },
            "id": null
        }
        ```
        
        **Batch Requests:**
        ```json
        [
            {"jsonrpc": "2.0", "method": "getUser", "params": {"id": 1}, "id": 1},
            {"jsonrpc": "2.0", "method": "getUser", "params": {"id": 2}, "id": 2}
        ]
        ```
        """)
    
    # Security and Advanced Features
    with st.expander("🔒 Security and Advanced Capabilities"):
        st.markdown("""
        ### Security Features
        
        **1. Security Roots**
        - Trusted execution environments
        - Cryptographic verification
        - Secure communication channels
        
        **2. Authentication Methods**
        - API key authentication
        - OAuth 2.0 flows
        - JWT tokens
        - Mutual TLS (mTLS)
        
        **3. Authorization Patterns**
        - Role-based access control (RBAC)
        - Resource-level permissions
        - Dynamic access policies
        
        ### Advanced Capabilities
        
        **1. Sampling**
        - LLM response sampling
        - Temperature control
        - Top-k and top-p sampling
        
        **2. Logging and Monitoring**
        ```python
        import logging
        from mcp.server import Server
        
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("mcp-server")
        
        @server.tool("example_tool")
        async def example_tool(arg: str):
            logger.info(f"Tool called with: {arg}")
            return f"Result: {arg}"
        ```
        
        **3. Progress Notifications**
        - Real-time progress updates
        - Long-running operation status
        - Cancellation support
        
        **4. Resource Updates**
        - Dynamic resource discovery
        - Live data synchronization
        - Event-driven updates
        """)

def _show_openai_agents_docs(difficulty, search_term):
    """Comprehensive OpenAI Agents SDK documentation"""
    st.subheader("🤖 OpenAI Agents SDK - Complete Documentation")
    
    # SDK Overview
    with st.expander("🚀 SDK Overview and Getting Started", expanded=True):
        st.markdown("""
        ### OpenAI Agents SDK Overview
        
        The OpenAI Agents SDK is a production-ready framework for building agentic AI applications. It's an evolution of the Swarm experimental framework with these core primitives:
        
        **Core Primitives:**
        1. **Agents**: LLMs equipped with instructions and tools
        2. **Handoffs**: Agent delegation mechanisms
        3. **Guardrails**: Input validation systems
        4. **Sessions**: Automatic conversation history management
        
        ### Installation and Setup
        ```bash
        pip install openai-agents
        export OPENAI_API_KEY=sk-your-key-here
        ```
        
        ### Hello World Example
        ```python
        from agents import Agent, Runner
        
        agent = Agent(
            name="Assistant", 
            instructions="You are a helpful assistant"
        )
        
        result = Runner.run_sync(
            agent, 
            "Write a haiku about recursion in programming."
        )
        print(result.final_output)
        ```
        """)
    
    # Agent Architecture
    with st.expander("🏗️ Agent Architecture and Configuration"):
        st.markdown("""
        ### Agent Definition and Configuration
        
        **Basic Agent Setup:**
        ```python
        from agents import Agent
        
        agent = Agent(
            name="DataAnalyst",
            instructions=\"\"\"You are a data analyst expert.
            You help users analyze data and create visualizations.
            Always explain your reasoning step by step.\"\"\",
            model="gpt-4",
            temperature=0.1
        )
        ```
        
        **Advanced Agent Configuration:**
        ```python
        agent = Agent(
            name="ResearchAgent",
            instructions="Research specialist",
            model="gpt-4-turbo",
            temperature=0.2,
            max_tokens=4000,
            tools=[search_tool, summarize_tool],
            parallel_tool_calls=True
        )
        ```
        
        ### Agent Capabilities
        
        **1. Tool Integration**
        - Automatic schema generation
        - Pydantic validation
        - Error handling and retries
        
        **2. Model Selection**
        - GPT-4, GPT-4 Turbo support
        - Custom model parameters
        - Cost optimization strategies
        
        **3. Instruction Engineering**
        - System prompts optimization
        - Context-aware instructions
        - Dynamic instruction updates
        """)
    
    # Tools and Functions
    with st.expander("🔧 Tools and Function Implementation"):
        st.markdown("""
        ### Function Tools
        
        **Simple Function Tool:**
        ```python
        def calculate_tip(bill_amount: float, tip_percentage: float = 15.0) -> str:
            \"\"\"Calculate tip amount for a bill.
            
            Args:
                bill_amount: The total bill amount
                tip_percentage: Tip percentage (default 15%)
                
            Returns:
                Formatted tip calculation
            \"\"\"
            tip = bill_amount * (tip_percentage / 100)
            total = bill_amount + tip
            return f"Tip: ${tip:.2f}, Total: ${total:.2f}"
        
        agent = Agent(
            name="TipCalculator",
            instructions="Help calculate tips",
            tools=[calculate_tip]
        )
        ```
        
        **Advanced Tool with External API:**
        ```python
        import requests
        from typing import Optional
        
        def get_weather(city: str, country: Optional[str] = None) -> str:
            \"\"\"Get current weather for a city.
            
            Args:
                city: City name
                country: Country code (optional)
                
            Returns:
                Weather information
            \"\"\"
            api_key = os.getenv("WEATHER_API_KEY")
            location = f"{city},{country}" if country else city
            
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather",
                params={"q": location, "appid": api_key, "units": "metric"}
            )
            
            if response.status_code == 200:
                data = response.json()
                return f"Weather in {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C"
            else:
                return f"Could not get weather for {city}"
        ```
        
        **Database Tool Example:**
        ```python
        import sqlite3
        
        def query_database(query: str) -> str:
            \"\"\"Execute SQL query on database.
            
            Args:
                query: SQL query to execute
                
            Returns:
                Query results as formatted string
            \"\"\"
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            
            try:
                cursor.execute(query)
                results = cursor.fetchall()
                return str(results)
            except Exception as e:
                return f"Error: {str(e)}"
            finally:
                conn.close()
        ```
        """)
    
    # Handoffs and Multi-Agent Systems
    with st.expander("🤝 Handoffs and Multi-Agent Coordination"):
        st.markdown("""
        ### Agent Handoffs
        
        **Basic Handoff Pattern:**
        ```python
        from agents import Agent, Handoff
        
        # Define specialized agents
        research_agent = Agent(
            name="Researcher",
            instructions="You research topics thoroughly",
            tools=[search_tool, web_scraper]
        )
        
        writer_agent = Agent(
            name="Writer",
            instructions="You write engaging articles",
            tools=[grammar_check, style_guide]
        )
        
        # Handoff function
        def transfer_to_writer(research_summary: str) -> Handoff:
            \"\"\"Transfer to writer agent with research summary\"\"\"
            return Handoff(
                agent=writer_agent,
                context=f"Research completed: {research_summary}"
            )
        
        # Main coordinator agent
        coordinator = Agent(
            name="Coordinator",
            instructions="Coordinate research and writing tasks",
            tools=[transfer_to_writer]
        )
        ```
        
        **Advanced Multi-Agent Workflow:**
        ```python
        class ContentCreationWorkflow:
            def __init__(self):
                self.researcher = Agent(
                    name="Researcher",
                    instructions="Research topics and gather information",
                    tools=[self.research_tool, self.fact_check]
                )
                
                self.writer = Agent(
                    name="Writer", 
                    instructions="Create engaging content",
                    tools=[self.write_article, self.optimize_seo]
                )
                
                self.editor = Agent(
                    name="Editor",
                    instructions="Review and edit content",
                    tools=[self.grammar_check, self.style_review]
                )
            
            def create_content(self, topic: str):
                # Research phase
                research = Runner.run_sync(self.researcher, f"Research: {topic}")
                
                # Writing phase
                draft = Runner.run_sync(
                    self.writer, 
                    f"Write article based on: {research.final_output}"
                )
                
                # Editing phase
                final = Runner.run_sync(
                    self.editor,
                    f"Edit this article: {draft.final_output}"
                )
                
                return final.final_output
        ```
        """)
    
    # Sessions and State Management
    with st.expander("💾 Sessions and State Management"):
        st.markdown("""
        ### Session Management
        
        **Basic Session Usage:**
        ```python
        from agents import Agent, Runner, Session
        
        agent = Agent(name="Assistant", instructions="Be helpful")
        session = Session()
        
        # Multiple interactions in same session
        result1 = Runner.run_sync(agent, "My name is Alice", session=session)
        result2 = Runner.run_sync(agent, "What's my name?", session=session)
        # Agent remembers: "Your name is Alice"
        ```
        
        **Advanced Session Configuration:**
        ```python
        session = Session(
            max_turns=50,           # Maximum conversation turns
            context_window=8000,    # Token limit for context
            memory_strategy="sliding_window"  # How to handle context overflow
        )
        ```
        
        **Session Persistence:**
        ```python
        import json
        from agents import Session
        
        # Save session state
        def save_session(session: Session, filename: str):
            session_data = {
                "messages": session.messages,
                "metadata": session.metadata,
                "created_at": session.created_at.isoformat()
            }
            with open(filename, 'w') as f:
                json.dump(session_data, f)
        
        # Load session state
        def load_session(filename: str) -> Session:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            session = Session()
            session.messages = data["messages"]
            session.metadata = data["metadata"]
            return session
        ```
        """)
    
    # Guardrails and Safety
    with st.expander("🛡️ Guardrails and Security Implementation"):
        st.markdown("""
        ### Input Guardrails
        
        **Content Safety Guardrail:**
        ```python
        from agents import Agent, InputGuardrail, GuardrailFunctionOutput
        
        async def content_safety_check(ctx, agent, input_data: str) -> GuardrailFunctionOutput:
            \"\"\"Check for inappropriate content\"\"\"
            banned_words = ["spam", "hack", "exploit"]
            
            if any(word in input_data.lower() for word in banned_words):
                return GuardrailFunctionOutput(
                    tripwire_triggered=True,
                    output_info="Content violates safety policies"
                )
            
            return GuardrailFunctionOutput(tripwire_triggered=False)
        
        safe_agent = Agent(
            name="SafeAgent",
            instructions="Provide helpful responses within safety guidelines",
            input_guardrails=[InputGuardrail(guardrail_function=content_safety_check)]
        )
        ```
        
        **Business Logic Guardrail:**
        ```python
        async def business_hours_check(ctx, agent, input_data: str) -> GuardrailFunctionOutput:
            \"\"\"Only allow certain operations during business hours\"\"\"
            from datetime import datetime
            
            now = datetime.now()
            if now.hour < 9 or now.hour > 17:
                return GuardrailFunctionOutput(
                    tripwire_triggered=True,
                    output_info="This operation is only available during business hours (9 AM - 5 PM)"
                )
            
            return GuardrailFunctionOutput(tripwire_triggered=False)
        ```
        
        ### Output Guardrails
        
        **Response Quality Check:**
        ```python
        from agents import OutputGuardrail
        
        async def quality_check(ctx, agent, output_data: str) -> GuardrailFunctionOutput:
            \"\"\"Ensure response meets quality standards\"\"\"
            
            # Check minimum length
            if len(output_data.strip()) < 10:
                return GuardrailFunctionOutput(
                    tripwire_triggered=True,
                    output_info="Response too short, please provide more detail"
                )
            
            # Check for placeholder text
            placeholders = ["TODO", "PLACEHOLDER", "TBD"]
            if any(placeholder in output_data for placeholder in placeholders):
                return GuardrailFunctionOutput(
                    tripwire_triggered=True,
                    output_info="Response contains placeholder text"
                )
            
            return GuardrailFunctionOutput(tripwire_triggered=False)
        
        quality_agent = Agent(
            name="QualityAgent",
            instructions="Provide high-quality, complete responses",
            output_guardrails=[OutputGuardrail(guardrail_function=quality_check)]
        )
        ```
        """)
    
    # Advanced Production Patterns
    with st.expander("🏭 Production Patterns and Enterprise Deployment"):
        st.markdown("""
        ### Error Handling and Resilience
        
        **Comprehensive Error Handling:**
        ```python
        from agents import Agent, Runner
        from agents.exceptions import AgentException, ToolException
        import logging
        
        logger = logging.getLogger(__name__)
        
        class ProductionAgent:
            def __init__(self):
                self.agent = Agent(
                    name="ProductionAgent",
                    instructions="Handle tasks reliably",
                    tools=[self.reliable_tool],
                    max_retries=3,
                    retry_delay=1.0
                )
            
            def reliable_tool(self, data: str) -> str:
                \"\"\"Tool with built-in error handling\"\"\"
                try:
                    # Simulate external API call
                    result = external_api_call(data)
                    return result
                except APIException as e:
                    logger.error(f"API error: {e}")
                    return f"Service temporarily unavailable: {e}"
                except Exception as e:
                    logger.error(f"Unexpected error: {e}")
                    return "An unexpected error occurred. Please try again."
            
            async def run_with_fallback(self, user_input: str):
                try:
                    result = await Runner.run(self.agent, user_input)
                    return result.final_output
                except AgentException as e:
                    logger.error(f"Agent error: {e}")
                    return "I encountered an issue. Please rephrase your request."
                except Exception as e:
                    logger.error(f"System error: {e}")
                    return "System temporarily unavailable."
        ```
        
        ### Monitoring and Observability
        
        **Custom Metrics and Logging:**
        ```python
        import time
        from dataclasses import dataclass
        from typing import Dict, Any
        
        @dataclass
        class AgentMetrics:
            agent_name: str
            execution_time: float
            tool_calls: int
            tokens_used: int
            success: bool
            error_type: str = None
        
        class MonitoredAgent:
            def __init__(self, agent: Agent):
                self.agent = agent
                self.metrics = []
            
            async def run_with_monitoring(self, input_data: str) -> Any:
                start_time = time.time()
                tool_calls = 0
                success = False
                error_type = None
                
                try:
                    result = await Runner.run(self.agent, input_data)
                    
                    # Extract metrics from result
                    tool_calls = len([item for item in result.new_items if hasattr(item, 'tool_name')])
                    success = True
                    
                    return result
                    
                except Exception as e:
                    error_type = type(e).__name__
                    raise
                    
                finally:
                    execution_time = time.time() - start_time
                    
                    metrics = AgentMetrics(
                        agent_name=self.agent.name,
                        execution_time=execution_time,
                        tool_calls=tool_calls,
                        tokens_used=0,  # Would need actual token counting
                        success=success,
                        error_type=error_type
                    )
                    
                    self.metrics.append(metrics)
                    self._log_metrics(metrics)
            
            def _log_metrics(self, metrics: AgentMetrics):
                logger.info(f"Agent: {metrics.agent_name}, "
                           f"Time: {metrics.execution_time:.2f}s, "
                           f"Tools: {metrics.tool_calls}, "
                           f"Success: {metrics.success}")
        ```
        
        ### Load Balancing and Scaling
        
        **Agent Pool Management:**
        ```python
        import asyncio
        from concurrent.futures import ThreadPoolExecutor
        from typing import List
        
        class AgentPool:
            def __init__(self, agent_template: Agent, pool_size: int = 5):
                self.agent_template = agent_template
                self.pool_size = pool_size
                self.agents = [self._create_agent() for _ in range(pool_size)]
                self.available_agents = asyncio.Queue()
                
                # Initialize queue with all agents
                for agent in self.agents:
                    self.available_agents.put_nowait(agent)
            
            def _create_agent(self) -> Agent:
                return Agent(
                    name=self.agent_template.name,
                    instructions=self.agent_template.instructions,
                    tools=self.agent_template.tools,
                    model=self.agent_template.model
                )
            
            async def execute_with_pool(self, tasks: List[str]) -> List[Any]:
                \"\"\"Execute multiple tasks using agent pool\"\"\"
                results = []
                
                async def process_task(task: str):
                    # Get agent from pool
                    agent = await self.available_agents.get()
                    
                    try:
                        result = await Runner.run(agent, task)
                        return result.final_output
                    finally:
                        # Return agent to pool
                        await self.available_agents.put(agent)
                
                # Process all tasks concurrently
                tasks_coroutines = [process_task(task) for task in tasks]
                results = await asyncio.gather(*tasks_coroutines)
                
                return results
        ```
        
        ### Configuration Management
        
        **Environment-Based Configuration:**
        ```python
        import os
        from dataclasses import dataclass
        from typing import Optional
        
        @dataclass
        class AgentConfig:
            model: str
            temperature: float
            max_tokens: int
            timeout: int
            max_retries: int
            api_key: Optional[str] = None
            
            @classmethod
            def from_environment(cls, env_prefix: str = "AGENT_"):
                return cls(
                    model=os.getenv(f"{env_prefix}MODEL", "gpt-4"),
                    temperature=float(os.getenv(f"{env_prefix}TEMPERATURE", "0.1")),
                    max_tokens=int(os.getenv(f"{env_prefix}MAX_TOKENS", "4000")),
                    timeout=int(os.getenv(f"{env_prefix}TIMEOUT", "30")),
                    max_retries=int(os.getenv(f"{env_prefix}MAX_RETRIES", "3")),
                    api_key=os.getenv("OPENAI_API_KEY")
                )
        
        class ConfigurableAgent:
            def __init__(self, config: AgentConfig):
                self.config = config
                self.agent = Agent(
                    name="ConfigurableAgent",
                    instructions="I adapt to configuration settings",
                    model=config.model,
                    temperature=config.temperature,
                    max_tokens=config.max_tokens
                )
        ```
        """)
    
    # Hosted Tools Deep Dive
    with st.expander("🌐 Hosted Tools and External Integrations"):
        st.markdown("""
        ### OpenAI Hosted Tools
        
        **Web Search Tool:**
        ```python
        from agents.tools import WebSearchTool
        from agents import Agent, Runner
        
        # Basic web search agent
        search_agent = Agent(
            name="SearchAgent",
            instructions="Search the web and provide accurate, up-to-date information",
            tools=[WebSearchTool()]
        )
        
        # Advanced search with result processing
        class AdvancedSearchAgent:
            def __init__(self):
                self.search_tool = WebSearchTool(
                    max_results=10,
                    include_raw_results=True
                )
                
                self.agent = Agent(
                    name="AdvancedSearcher",
                    instructions=\"\"\"Search the web and provide comprehensive analysis.
                    Always cite your sources and provide multiple perspectives.\"\"\",
                    tools=[self.search_tool, self.analyze_results]
                )
            
            def analyze_results(self, search_results: str) -> str:
                \"\"\"Analyze and synthesize search results\"\"\"
                # Custom processing of search results
                lines = search_results.split('\\n')
                sources = [line for line in lines if line.startswith('Source:')]
                
                return f"Analysis based on {len(sources)} sources:\\n{search_results}"
        ```
        
        **Code Interpreter Tool:**
        ```python
        from agents.tools import CodeInterpreterTool
        
        # Data analysis agent with code execution
        data_agent = Agent(
            name="DataAnalyst",
            instructions=\"\"\"You are a data analysis expert.
            Use the code interpreter to analyze data, create visualizations,
            and perform statistical calculations.\"\"\",
            tools=[CodeInterpreterTool()]
        )
        
        # Example usage for data analysis
        async def analyze_csv_data():
            result = await Runner.run(
                data_agent,
                \"\"\"
                Analyze the sales data in the uploaded CSV file:
                1. Calculate total sales by region
                2. Create a bar chart of monthly trends
                3. Identify the top 5 performing products
                4. Provide statistical summary
                \"\"\"
            )
            return result.final_output
        ```
        
        **File Search Tool:**
        ```python
        from agents.tools import FileSearchTool
        
        # Knowledge base agent with file search
        kb_agent = Agent(
            name="KnowledgeBase",
            instructions=\"\"\"Search through company documents and provide
            accurate information from our knowledge base.\"\"\",
            tools=[FileSearchTool(
                vector_store_ids=["vs_knowledge_base_123"],
                max_num_results=5,
                include_metadata=True
            )]
        )
        ```
        
        ### Custom External Tool Integration
        
        **Database Integration Tool:**
        ```python
        import psycopg2
        from typing import List, Dict, Any
        
        class DatabaseTool:
            def __init__(self, connection_string: str):
                self.connection_string = connection_string
            
            def query_database(self, query: str) -> str:
                \"\"\"Execute SQL query and return results\"\"\"
                try:
                    conn = psycopg2.connect(self.connection_string)
                    cursor = conn.cursor()
                    
                    cursor.execute(query)
                    
                    if query.strip().upper().startswith('SELECT'):
                        results = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        
                        # Format results as table
                        formatted_results = []
                        formatted_results.append(' | '.join(columns))
                        formatted_results.append('-' * (len(' | '.join(columns))))
                        
                        for row in results:
                            formatted_results.append(' | '.join(str(cell) for cell in row))
                        
                        return '\\n'.join(formatted_results)
                    else:
                        conn.commit()
                        return f"Query executed successfully. Rows affected: {cursor.rowcount}"
                
                except Exception as e:
                    return f"Database error: {str(e)}"
                finally:
                    if conn:
                        conn.close()
            
            def get_schema(self, table_name: str) -> str:
                \"\"\"Get table schema information\"\"\"
                query = f\"\"\"
                SELECT column_name, data_type, is_nullable, column_default
                FROM information_schema.columns
                WHERE table_name = '{table_name}'
                ORDER BY ordinal_position;
                \"\"\"
                return self.query_database(query)
        
        # Create database-enabled agent
        db_agent = Agent(
            name="DatabaseAnalyst",
            instructions="Analyze data using SQL queries. Always explain your queries.",
            tools=[db_tool.query_database, db_tool.get_schema]
        )
        ```
        
        **API Integration Tool:**
        ```python
        import requests
        import json
        from typing import Optional, Dict, Any
        
        class APIIntegrationTool:
            def __init__(self, base_url: str, api_key: Optional[str] = None):
                self.base_url = base_url.rstrip('/')
                self.headers = {}
                if api_key:
                    self.headers['Authorization'] = f'Bearer {api_key}'
            
            def make_api_call(self, endpoint: str, method: str = 'GET', 
                            params: Optional[Dict] = None, 
                            data: Optional[Dict] = None) -> str:
                \"\"\"Make API call to external service\"\"\"
                url = f"{self.base_url}/{endpoint.lstrip('/')}"
                
                try:
                    response = requests.request(
                        method=method,
                        url=url,
                        headers=self.headers,
                        params=params,
                        json=data,
                        timeout=30
                    )
                    response.raise_for_status()
                    
                    return json.dumps(response.json(), indent=2)
                    
                except requests.RequestException as e:
                    return f"API Error: {str(e)}"
            
            def get_api_documentation(self) -> str:
                \"\"\"Get API documentation or schema\"\"\"
                return self.make_api_call('/docs/openapi.json')
        
        # Create API-enabled agent
        api_agent = Agent(
            name="APIIntegrator",
            instructions="Interact with external APIs to fetch and update data",
            tools=[api_tool.make_api_call, api_tool.get_api_documentation]
        )
        ```
        """)
    
    # Structured Outputs and Pydantic Integration
    with st.expander("📋 Structured Outputs and Data Validation"):
        st.markdown("""
        ### Pydantic Models for Structured Responses
        
        **Complex Data Extraction:**
        ```python
        from pydantic import BaseModel, Field
        from typing import List, Optional
        from datetime import datetime
        
        class Contact(BaseModel):
            name: str
            email: str
            phone: Optional[str] = None
            
        class Event(BaseModel):
            title: str
            date: datetime
            location: str
            attendees: List[Contact]
            description: Optional[str] = None
            
        class EmailAnalysis(BaseModel):
            sender: Contact
            subject: str
            events_mentioned: List[Event]
            action_items: List[str]
            sentiment: str = Field(description="positive, negative, or neutral")
            priority: int = Field(ge=1, le=5, description="Priority from 1-5")
            
        # Agent that extracts structured data from emails
        email_agent = Agent(
            name="EmailAnalyzer",
            instructions="Analyze emails and extract structured information",
            output_type=EmailAnalysis
        )
        
        # Usage
        result = Runner.run_sync(email_agent, "Analyze this email: [email content]")
        analysis = result.final_output_as(EmailAnalysis)
        
        print(f"Priority: {analysis.priority}")
        print(f"Events found: {len(analysis.events_mentioned)}")
        for event in analysis.events_mentioned:
            print(f"- {event.title} on {event.date}")
        ```
        
        **Financial Data Processing:**
        ```python
        from decimal import Decimal
        from enum import Enum
        
        class TransactionType(str, Enum):
            DEBIT = "debit"
            CREDIT = "credit"
            
        class Transaction(BaseModel):
            id: str
            amount: Decimal
            transaction_type: TransactionType
            description: str
            category: str
            date: datetime
            
        class FinancialSummary(BaseModel):
            total_income: Decimal
            total_expenses: Decimal
            net_balance: Decimal
            transactions: List[Transaction]
            top_categories: List[str]
            
        financial_agent = Agent(
            name="FinancialAnalyzer",
            instructions="Analyze financial data and provide structured summaries",
            output_type=FinancialSummary,
            tools=[self.categorize_transaction, self.validate_amount]
        )
        ```
        
        **Dynamic Schema Generation:**
        ```python
        def create_dynamic_model(field_definitions: Dict[str, type]):
            \"\"\"Create Pydantic model dynamically\"\"\"
            return create_model('DynamicModel', **field_definitions)
        
        # Example: Create model based on user requirements
        user_fields = {
            'customer_name': (str, ...),
            'order_total': (float, Field(gt=0)),
            'items': (List[str], [])
        }
        
        DynamicOrderModel = create_dynamic_model(user_fields)
        
        dynamic_agent = Agent(
            name="DynamicProcessor",
            instructions="Process data according to dynamic schema",
            output_type=DynamicOrderModel
        )
        ```
        # Save session to file
        session.save("user_session.json")
        
        # Load session from file
        session = Session.load("user_session.json")
        
        # Continue conversation
        result = Runner.run_sync(agent, "Continue our discussion", session=session)
        ```
        """)
    
    # Guardrails and Validation
    with st.expander("🛡️ Guardrails and Input Validation"):
        st.markdown("""
        ### Input Validation and Guardrails
        
        **Basic Guardrails:**
        ```python
        from agents import Agent, Guardrail
        from pydantic import BaseModel, Field
        
        class UserInput(BaseModel):
            message: str = Field(..., min_length=1, max_length=1000)
            language: str = Field(default="en", pattern="^[a-z]{2}$")
        
        def validate_input(input_data: dict) -> bool:
            \"\"\"Custom validation logic\"\"\"
            try:
                UserInput(**input_data)
                return True
            except Exception:
                return False
        
        guardrail = Guardrail(
            name="input_validator",
            validator=validate_input,
            error_message="Invalid input format"
        )
        
        agent = Agent(
            name="SafeAgent",
            instructions="Process user requests safely",
            guardrails=[guardrail]
        )
        ```
        
        **Content Safety Guardrails:**
        ```python
        def content_safety_check(text: str) -> bool:
            \"\"\"Check for inappropriate content\"\"\"
            prohibited_words = ["spam", "harmful", "inappropriate"]
            return not any(word in text.lower() for word in prohibited_words)
        
        safety_guardrail = Guardrail(
            name="content_safety",
            validator=content_safety_check,
            error_message="Content violates safety guidelines"
        )
        ```
        """)
    
    # Tracing and Debugging
    with st.expander("🔍 Tracing, Debugging, and Monitoring"):
        st.markdown("""
        ### Built-in Tracing
        
        **Enable Tracing:**
        ```python
        from agents import Agent, Runner
        from agents.tracing import enable_tracing
        
        # Enable tracing
        enable_tracing(
            project_name="my-agent-app",
            api_key="your-tracing-key"
        )
        
        agent = Agent(name="TracedAgent", instructions="Be helpful")
        result = Runner.run_sync(agent, "Hello world")
        # Automatically traced and logged
        ```
        
        **Custom Tracing:**
        ```python
        from agents.tracing import trace_function
        
        @trace_function("custom_operation")
        def complex_operation(data):
            # Your complex logic here
            return processed_data
        
        # Function calls are automatically traced
        result = complex_operation(input_data)
        ```
        
        **Performance Monitoring:**
        ```python
        from agents import Agent, Runner
        from agents.monitoring import performance_monitor
        
        @performance_monitor
        def run_agent_workflow():
            agent = Agent(name="MonitoredAgent", instructions="Be efficient")
            return Runner.run_sync(agent, "Process this request")
        
        # Automatically monitors execution time, token usage, etc.
        result = run_agent_workflow()
        ```
        """)

def get_framework_specific_questions(framework, difficulty):
    """Get questions filtered by framework and difficulty"""
    # This would integrate with the existing test generator
    # For now, return a placeholder
    return f"Generating {difficulty} level questions for {framework}..."

def create_framework_test(framework, difficulty, num_questions):
    """Create a test based on framework and difficulty selection"""
    st.info(f"Creating {difficulty} level test for {framework} with {num_questions} questions")
    
    # This would integrate with the existing mock test system
    # Implementation would filter questions based on framework and difficulty
    
    test_questions = []
    
    if framework == "Building Effective Agents":
        # Filter agent-specific questions
        pass
    elif framework == "Model Context Protocol (MCP)":
        # Filter MCP-specific questions  
        pass
    elif framework == "OpenAI Agents SDK":
        # Filter OpenAI SDK-specific questions
        pass
    
    return test_questions