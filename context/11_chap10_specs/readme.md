/sp.specify Write chapter 10 in Part 3 of the book. The title of the chapter will be "Context Engineering for AI-Driven Development".

## Introduction: Why Context Engineering is Critical in AIDD

In Chapter 9, you learned how to craft effective prompts for AI coding agents. But prompts are just one piece of the puzzle. **Context engineering** is about managing the entire information environment that AI coding agents operate within—from your codebase structure to your development preferences to the technical constraints of your project.

Think of it this way:
- **Prompt Engineering** = What you say to the AI
- **Context Engineering** = Everything the AI knows when processing what you said

In AI-Driven Development (AIDD), context engineering can mean the difference between an AI that generates perfect, production-ready code and one that produces buggy, inconsistent implementations that don't fit your project.

### The Karpathy Principle for AIDD

As Andrej Karpathy famously explained: **"The LLM is the CPU, and the context window is the RAM."**

In AIDD, this means:
- Your **AI coding agent** is the processor
- Your **project context** (files, standards, dependencies) is the memory
- Your **prompts** are the instructions
- **Context engineering** is optimizing memory management for maximum performance

### The Real-World Impact

Consider two developers working on the same task:

**Developer A** (Poor Context Management):
```bash
claude-code prompt "Create a user authentication system"
```
Result: Generic implementation that doesn't match their tech stack, ignores their existing patterns, and requires hours of refactoring.

**Developer B** (Good Context Engineering):
```bash
# First, loads project context
claude-code prompt "Analyze our project structure in src/, understand our existing auth patterns in src/auth/oauth.py, and note our dependencies in requirements.txt"

# Then requests implementation
claude-code prompt "Create a user authentication system that:
- Follows our existing OAuth pattern in src/auth/oauth.py
- Uses our database models from src/models/user.py
- Matches our FastAPI route structure in src/api/
- Adheres to our testing patterns in tests/
- Uses only dependencies already in requirements.txt"
```
Result: Perfect fit implementation that requires minimal modifications.

The difference? **Context engineering.**

## Context Engineering vs Prompt Engineering

While Chapter 9 focused on prompt engineering, let's clarify how context engineering differs and why both are essential:

### Prompt Engineering (Chapter 9 Focus)
- **Scope**: Single interaction or conversation
- **Focus**: How you phrase requests and commands
- **Nature**: Tactical - optimizing individual prompts
- **Goal**: Get the best response to a specific request
- **Example**: "Implement JWT authentication with refresh tokens using bcrypt for password hashing"

### Context Engineering (This Chapter)
- **Scope**: Entire development environment and session
- **Focus**: What information is available to the AI
- **Nature**: Strategic - architecting information flow
- **Goal**: Enable the AI to make informed decisions across multiple interactions
- **Example**: Loading project structure, coding standards, existing patterns, dependencies, and constraints so the AI automatically produces consistent code

### Why You Need Both

**Prompt engineering without context engineering:**
- Every prompt requires extensive detail
- AI can't maintain consistency across features
- You repeat project information constantly
- AI lacks awareness of your existing codebase

**Context engineering without prompt engineering:**
- Even with perfect context, vague prompts produce poor results
- AI may not know which context is relevant for current task
- Lack of clear direction despite abundant information

**Together:**
- Context provides the knowledge base
- Prompts provide the specific instructions
- AI produces contextually appropriate, well-directed code

## Understanding the AIDD Context Window

Before diving into context engineering techniques, you need to understand how AI coding agents manage context.

### Context Window Basics

The context window is the "working memory" of your AI coding agent. It has:

**Finite Size:**
- Claude Sonnet 4.5: ~200,000 tokens (≈150,000 words or ≈500 pages)
- Gemini 1.5 Pro: 1,000,000 tokens (≈750,000 words)

**Contents Include:**
- System prompts and instructions
- Conversation history
- Files you've explicitly loaded or AI has read
- Tool outputs (bash commands, search results)
- Your prompts and AI's responses

**Key Characteristics:**
1. **Everything in context is "visible" to the AI**
2. **Anything outside context doesn't exist to the AI**
3. **Context degrades as it fills up** ("context rot")
4. **You must actively manage what's in context**

### Context Rot: The Performance Degradation Problem

As the context window fills up, AI performance degrades:

**Early in Session (20% context filled):**
- AI recalls details accurately
- Quick, precise responses
- Strong awareness of all available information

**Mid Session (60% context filled):**
- Some details may be missed
- Slower processing
- May need reminders about earlier decisions

**Late Session (90% context filled):**
- Significant detail loss
- Inconsistent with earlier responses
- May contradict previous decisions

**Why This Happens:**
- Transformer attention mechanism must process every token against every other token
- More tokens = exponentially more processing
- AI models are trained on shorter sequences, so performance drops with length

### Context Management Strategies for AIDD

Given these constraints, effective AIDD requires strategic context management:

**1. Load Essential Context Early**
```bash
# Session start
claude-code prompt "Read and understand:
- Project structure: src/, tests/, docs/
- Tech stack: requirements.txt, package.json
- Coding standards: CONTRIBUTING.md
- Key patterns: src/core/base_service.py"
```

**2. Use Just-In-Time Context Loading**
```bash
# Don't load all files upfront
# Instead, load as needed
claude-code prompt "Implement user service. First, read src/services/product_service.py to understand our service pattern, then implement user service following the same structure."
```

**3. Periodic Context Compression**
```bash
# After several interactions
claude-code prompt "Summarize our progress so far: what have we built, what decisions have we made, and what's next? Keep it under 200 words."

# Then start fresh with the summary
# This "compacts" your conversation history
```

**4. Context Isolation for Complex Tasks**
```bash
# Use separate sessions for different concerns
# Session 1: Backend API development
# Session 2: Frontend component development
# Session 3: Testing and debugging
```

## The Six Components of AIDD Context

Building on the six components of AI agents from general context engineering, here's how they apply specifically to AIDD:

### 1. Model Selection for Development Tasks

Different AI models excel at different development tasks:

**Claude Sonnet 4.5 (Best for AIDD Overall)**
- **Strengths**: Complex reasoning, architecture design, refactoring
- **Best for**: Backend development, system design, debugging
- **Context window**: 200K tokens
- **Use when**: Building production systems, need strong reasoning

**Gemini 1.5 Pro (Best for Large Codebases)**
- **Strengths**: Massive context window, fast processing
- **Best for**: Working with large codebases, documentation
- **Context window**: 1M tokens
- **Use when**: Need to load entire project context at once

**Model Selection Strategy:**
```bash
# For new feature with complex logic → Claude
claude-code prompt "Design and implement a payment processing system with retry logic, idempotency, and comprehensive error handling"

# For understanding large codebase → Gemini
gemini chat --session analysis "Read all files in src/ (50+ files) and create an architectural diagram showing how components interact"
```

### 2. Development Tools as Context Sources

In AIDD, "tools" are not just external APIs—they're sources of critical development context:

**File System Tools:**
```bash
# Claude Code can read your file system
claude-code prompt "Analyze the directory structure of src/ and tests/ and suggest improvements to organization"

# Gemini CLI with file access
gemini chat "Read src/database/models.py and generate SQLAlchemy migration scripts"
```

**Bash/Terminal Tools:**
```bash
# AI can execute commands to gather context
claude-code prompt "Run 'pytest --collect-only' to see all existing tests, then generate tests for the new user service following existing patterns"

# Check dependencies
claude-code prompt "Run 'pip list' to see installed packages, then implement the feature using only available dependencies"
```

**Git Tools:**
```bash
# Git history as context
claude-code prompt "Run 'git log --oneline -20' to see recent changes, then analyze if my new feature conflicts with recent work"

# Diff context
claude-code prompt "Run 'git diff main' to see my changes, then review for potential issues"
```

**Search Tools:**
```bash
# Code search for context
claude-code prompt "Search the codebase for all uses of 'authenticate' function to understand current authentication patterns before implementing new auth"
```

### 3. Knowledge and Memory in AIDD

Knowledge and memory in AIDD context consists of multiple layers:

#### Static Knowledge Layer: Project Documentation

**Essential Documents to Load:**
```
/
├── README.md           # Project overview, setup instructions
├── CONTRIBUTING.md     # Code standards, commit conventions
├── ARCHITECTURE.md     # System design, component relationships
├── API_DOCS.md        # API specifications, endpoint contracts
├── SETUP.md           # Development environment setup
└── docs/
    ├── database_schema.md
    ├── authentication.md
    └── deployment.md
```

**Loading Strategy:**
```bash
# At session start
claude-code prompt "Read README.md, CONTRIBUTING.md, and ARCHITECTURE.md to understand the project"

# For specific tasks
claude-code prompt "Before implementing the API endpoint, read API_DOCS.md to understand our API conventions"
```

#### Dynamic Memory Layer: Conversation History

**What Gets Stored in Conversation Memory:**
- Previous prompts and responses
- Code generated by AI
- Decisions and trade-offs discussed
- Bugs found and fixed
- Architecture choices made

**Memory Management Techniques:**

**1. Explicit Memory Creation:**
```bash
claude-code prompt "Important decision: We're using JWT with 15-minute access tokens and 7-day refresh tokens. Remember this for all future authentication implementations."
```

**2. Memory Checkpoints:**
```bash
# After major milestone
claude-code prompt "Create a summary of what we've built so far:
- Features implemented
- Architecture decisions
- Known issues or TODOs
- Next steps

Format as a PROGRESS.md file."
```

**3. Architectural Decision Records (ADRs):**
```bash
claude-code prompt "Create an ADR documenting our decision to use Redis for session storage instead of database sessions. Include context, decision, consequences, and alternatives considered."
```

#### Code Pattern Memory: Learning from Existing Code

**Teaching AI Your Patterns:**
```bash
# Show examples of your patterns
claude-code prompt "Here are three examples of our service classes:

src/services/user_service.py
src/services/product_service.py  
src/services/order_service.py

Study these patterns and implement payment_service.py following the exact same structure:
- Constructor with dependency injection
- Async methods throughout
- Custom exceptions for business logic errors
- Comprehensive docstrings
- Type hints on all methods"
```

### 4. Audio and Speech (Less Relevant for AIDD)

While voice interfaces exist for coding, they're less common in AIDD. However, they can be useful for:

**Voice-Based Code Review:**
```bash
# Dictate changes while reviewing code
"Add error handling to the authentication function, specifically catch JWT expiration and return a 401 status"
```

**Verbal Debugging:**
```bash
# Describe the problem verbally
"The user registration endpoint is returning 500 errors when the email already exists. Check the validation logic and fix it to return a proper 400 error with a clear message."
```

**Most AIDD remains text-based** because:
- Code requires precise syntax
- File paths and technical terms are easier to type
- Copy-paste workflows are essential
- Code review requires visual inspection

### 5. Guardrails for Code Quality

In AIDD, guardrails ensure AI-generated code meets quality and security standards:

#### Code Quality Guardrails

**Style and Convention Enforcement:**
```bash
# Explicit guardrails in prompt
claude-code prompt "Implement user authentication with these guardrails:
- MUST follow PEP 8 style (enforce with Black formatter)
- MUST include type hints on all functions
- MUST have docstrings (Google style)
- MUST have 80%+ test coverage
- MUST handle all errors explicitly (no bare except clauses)"
```

**Architectural Guardrails:**
```bash
claude-code prompt "Add new feature with these constraints:
- MUST NOT introduce new dependencies
- MUST follow existing layered architecture (API -> Service -> Repository)
- MUST NOT bypass existing authentication middleware
- MUST maintain backward compatibility with existing API contracts"
```

#### Security Guardrails

**Preventing Vulnerable Code:**
```bash
claude-code prompt "Implement password reset functionality with security guardrails:
- MUST use cryptographically secure random tokens (secrets.token_urlsafe)
- MUST implement rate limiting (5 requests per hour per email)
- MUST use parameterized queries (never raw SQL)
- MUST validate and sanitize all user inputs
- MUST NOT log sensitive information (passwords, tokens)
- MUST expire reset tokens after 1 hour"
```

**Compliance Guardrails:**
```bash
claude-code prompt "Implement user data export for GDPR compliance:
- MUST include ALL user data across all tables
- MUST properly anonymize related data if user deleted
- MUST log data export requests with timestamp and IP
- MUST enforce authentication before export
- MUST return data in machine-readable format (JSON)"
```

#### Testing Guardrails

**Enforcing Test Quality:**
```bash
claude-code prompt "Generate tests with these guardrails:
- MUST test happy path AND edge cases
- MUST mock external dependencies (databases, APIs)
- MUST follow AAA pattern (Arrange, Act, Assert)
- MUST have descriptive test names (test_<function>_<scenario>_<expected>)
- MUST achieve minimum 85% code coverage"
```

### 6. Orchestration and Workflow Management

Orchestration in AIDD means coordinating multiple AI interactions across a development workflow:

#### Session Orchestration

**Single-Feature Development Flow:**
```bash
# Session 1: Research and design
claude-code prompt "Analyze existing authentication systems in our codebase and propose an architecture for adding OAuth social login"

# Session 2: Implementation  
claude-code prompt "Implement the OAuth social login architecture we designed"

# Session 3: Testing
claude-code prompt "Generate comprehensive tests for the OAuth implementation"

# Session 4: Documentation
claude-code prompt "Create API documentation and usage examples for the new OAuth endpoints"
```

**Multi-Day Project Orchestration:**
```bash
# Day 1: Foundation
claude-code prompt "Set up project structure and base models for inventory management system"

# Day 2: Core features (load previous context)
claude-code prompt "Continuing from yesterday's work, implement CRUD operations for inventory items"

# Day 3: Advanced features (reference earlier decisions)
claude-code prompt "Add barcode scanning and low-stock alerts to the inventory system we built"
```

#### Task Decomposition and Sub-Agents

For complex features, break into sub-tasks:

**Example: E-commerce Checkout System**

```bash
# Master prompt (architecture)
claude-code prompt "Design a complete checkout system with cart, payment, and order processing. Break this into 5 implementable components with clear interfaces."

# Sub-task 1: Shopping cart
claude-code prompt "Implement the shopping cart service as designed. Focus only on cart operations (add, remove, update, get cart)."

# Sub-task 2: Payment processing
claude-code prompt "Implement payment processing integration with Stripe API as designed."

# Sub-task 3: Order creation
claude-code prompt "Implement order creation service that uses cart and payment services."

# Sub-task 4: Inventory updates
claude-code prompt "Implement inventory update service that reduces stock after successful orders."

# Sub-task 5: Integration
claude-code prompt "Create the checkout orchestrator that coordinates all services into a complete checkout flow."
```

## Advanced Context Engineering Strategies for AIDD

Now let's dive into sophisticated techniques for managing context in real-world development scenarios.

### Strategy 1: Progressive Context Loading

**Problem**: Loading entire codebase upfront fills context window quickly and causes context rot.

**Solution**: Load context progressively as needed.

**Implementation:**

**Phase 1: High-Level Overview**
```bash
claude-code prompt "Give me a high-level overview of the project structure:
- What are the main directories?
- What's the general architecture?
- What are the key technologies?

Don't read files yet, just analyze directory structure."
```

**Phase 2: Relevant Module Context**
```bash
claude-code prompt "Now read only the authentication module files:
- src/auth/__init__.py
- src/auth/service.py
- src/auth/models.py

Understand the existing authentication patterns."
```

**Phase 3: Task-Specific Deep Dive**
```bash
claude-code prompt "Now implement the OAuth login feature following the patterns you learned from existing auth code."
```

**Benefits:**
- Keeps context focused and relevant
- Reduces context rot
- Faster AI processing
- More accurate results

### Strategy 2: Context Compression for Long Sessions

**Problem**: Development sessions can span hours, filling context window with increasingly irrelevant details.

**Solution**: Periodically compress context by summarizing and restarting with essentials.

**Implementation:**

**Step 1: Trigger Compression (every 10-15 interactions or when feeling context degradation)**
```bash
claude-code prompt "Compress our conversation history. Create a summary document including:

# PROJECT_STATE.md

## What We've Built
[List completed features]

## Architecture Decisions Made
[Key technical decisions]

## Code Patterns Established
[Patterns to follow in future code]

## Current Status
[What works, what's in progress, what's next]

## Known Issues/TODOs
[Outstanding tasks]

Keep it concise - under 500 words."
```

**Step 2: Start Fresh Session**
```bash
# New session, load compressed context
claude-code prompt "Read PROJECT_STATE.md to understand current project status, then continue with [next task]."
```

**Benefits:**
- Maintains important context across long sessions
- Removes noise and irrelevant details
- Keeps context window fresh
- Enables multi-day development continuity

### Strategy 3: Context Isolation for Parallel Development

**Problem**: Working on multiple features simultaneously causes context confusion.

**Solution**: Use isolated context environments for different tasks.

**Implementation:**

**Option A: Separate Terminal Sessions**
```bash
# Terminal 1: Feature A
claude-code prompt "Working on user authentication module"

# Terminal 2: Feature B  
claude-code prompt "Working on payment processing module"

# Terminal 3: Bug fixes
claude-code prompt "Debugging production issues"
```

**Option B: Context Switching with Markers**
```bash
# Switch context explicitly
claude-code prompt "=== CONTEXT SWITCH ===
Forget about the authentication work.
Now focusing on: Payment processing module
Relevant files: src/payments/
Goal: Implement Stripe integration"
```

**Option C: Named Sessions (Gemini CLI)**
```bash
# Create isolated sessions
gemini chat --session auth "Working on authentication"
gemini chat --session payments "Working on payments"
gemini chat --session testing "Working on test suite"
```

**Benefits:**
- Prevents cross-contamination between features
- Maintains focused context per task
- Easier to switch between tasks
- Clearer conversation history

### Strategy 4: Context Curation Through File Selection

**Problem**: AI reads unnecessary files, wasting context space.

**Solution**: Explicitly control which files AI accesses.

**Implementation:**

**Explicit File Loading:**
```bash
# Instead of vague request
claude-code prompt "Fix the bug in the authentication system"  # AI might read all files

# Explicit file targeting
claude-code prompt "Fix the JWT token expiration bug. Only read these files:
- src/auth/jwt_handler.py
- src/auth/middleware.py
- tests/test_jwt.py

Don't read other files unless specifically needed."
```

**Context Budget Management:**
```bash
claude-code prompt "I have a complex task requiring multiple files. Let's manage context budget:

1. First, tell me which files you need to read for this task
2. I'll confirm which are most critical
3. You'll read only approved files
4. If you need more, ask before reading

Task: Refactor authentication to support multiple identity providers"
```

**Layered File Access:**
```bash
# Layer 1: Interfaces only
claude-code prompt "Read only the interface/abstract class files to understand the architecture"

# Layer 2: Specific implementation
claude-code prompt "Now read the JWT implementation specifically"

# Layer 3: Related code
claude-code prompt "If needed, read related utility functions"
```

### Strategy 5: Structured Note-Taking (Agentic Memory)

**Problem**: Important decisions and context get lost in long conversations.

**Solution**: Maintain structured notes that persist outside conversation context.

**Implementation:**

**Create Memory Files:**

```bash
claude-code prompt "Create these memory files:

## DECISIONS.md
- Record architectural decisions
- Format: Decision, Context, Consequences

## PATTERNS.md
- Document code patterns we've established
- Include examples

## TODO.md  
- Track outstanding tasks
- Prioritized and categorized

## GOTCHAS.md
- Note tricky bugs or edge cases discovered
- Include solutions

Update these files as we work, so we can reference them in future sessions."
```

**Using Memory Files:**
```bash
# Start new session
claude-code prompt "Read DECISIONS.md and PATTERNS.md, then implement the next feature following established patterns and previous decisions."

# Update during work
claude-code prompt "Update TODO.md: Mark 'OAuth implementation' as complete, add 'Write OAuth tests' as next task."
```

**Memory File Template:**

```markdown
# DECISIONS.md

## [Decision ID]: Use Redis for Session Storage
**Date**: 2025-01-15
**Context**: Need fast session lookup for API authentication
**Decision**: Use Redis instead of database sessions
**Alternatives Considered**: 
- Database sessions (too slow)
- JWT-only (no server-side revocation)
**Consequences**: 
- Positive: Fast, scalable, easy revocation
- Negative: Additional infrastructure, memory usage
**Implementation Notes**: 
- TTL: 24 hours
- Key format: `session:{user_id}:{token_id}`
```

### Strategy 6: Example-Driven Context Engineering

**Problem**: Explaining desired code style is difficult with words alone.

**Solution**: Provide concrete examples as context.

**Implementation:**

**Pattern Examples:**
```bash
claude-code prompt "Here's an example of our service layer pattern:

\`\`\`python
class UserService:
    \"\"\"Service for user-related operations.\"\"\"
    
    def __init__(self, db: Database, cache: Cache):
        self.db = db
        self.cache = cache
    
    async def get_user(self, user_id: int) -> UserSchema:
        \"\"\"Get user by ID with caching.\"\"\"
        # Try cache first
        cached = await self.cache.get(f\"user:{user_id}\")
        if cached:
            return UserSchema.parse_raw(cached)
        
        # Fetch from database
        user = await self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail=\"User not found\")
        
        # Cache result
        schema = UserSchema.from_orm(user)
        await self.cache.set(f\"user:{user_id}\", schema.json(), ttl=3600)
        return schema
\`\`\`

Create ProductService following this EXACT pattern:
- Same constructor signature style
- Same caching approach
- Same error handling
- Same docstring format"
```

**Error Handling Examples:**
```bash
claude-code prompt "Here's how we handle errors in API routes:

\`\`\`python
@router.post(\"/users\")
async def create_user(user_data: UserCreate, db: Database = Depends(get_db)):
    try:
        user = await user_service.create_user(db, user_data)
        return {\"status\": \"success\", \"data\": user}
    except EmailAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error(f\"Unexpected error creating user: {e}\")
        raise HTTPException(status_code=500, detail=\"Internal server error\")
\`\`\`

Apply this exact error handling pattern to the new payment endpoint."
```

**Test Pattern Examples:**
```bash
claude-code prompt "Here's our test structure:

\`\`\`python
class TestUserService:
    @pytest.fixture
    async def user_service(self, db_session):
        return UserService(db_session, mock_cache)
    
    @pytest.mark.asyncio
    async def test_get_user_success(self, user_service, sample_user):
        \"\"\"Test successful user retrieval with valid ID.\"\"\"
        result = await user_service.get_user(sample_user.id)
        
        assert result.id == sample_user.id
        assert result.email == sample_user.email
    
    @pytest.mark.asyncio
    async def test_get_user_not_found(self, user_service):
        \"\"\"Test user retrieval with non-existent ID.\"\"\"
        with pytest.raises(HTTPException) as exc_info:
            await user_service.get_user(999999)
        
        assert exc_info.value.status_code == 404
\`\`\`

Create tests for ProductService following this exact structure."
```

### Strategy 7: Multi-Agent Context Architecture

**Problem**: Complex features require different types of expertise (backend, frontend, testing, deployment).

**Solution**: Use multiple AI "agents" with specialized contexts.

**Implementation:**

**Architecture Agent:**
```bash
claude-code prompt "You are a software architect. Based on these requirements:
[requirements]

Design:
1. System architecture diagram (Mermaid)
2. Component breakdown with responsibilities
3. Data flow between components
4. API contracts between services
5. Database schema

Don't implement yet - just design."
```

**Implementation Agent:**
```bash
claude-code prompt "You are a backend developer. Here's the architecture:
[paste architecture from above]

Implement Component 1: User Authentication Service
Follow the design exactly. Ask questions if anything is unclear."
```

**Testing Agent:**
```bash
claude-code prompt "You are a QA engineer. Here's the implemented authentication service:
[paste implementation]

Create comprehensive test suite:
1. Unit tests for each method
2. Integration tests for full flows
3. Edge case tests
4. Security tests
5. Performance tests"
```

**Documentation Agent:**
```bash
claude-code prompt "You are a technical writer. Here's the completed feature:
[paste implementation]

Create:
1. API documentation
2. Usage examples
3. Integration guide
4. Troubleshooting section"
```

**Benefits:**
- Specialized expertise for each concern
- Isolated contexts prevent confusion
- Better separation of concerns
- Higher quality specialized outputs

### Strategy 8: Just-In-Time Context Fetching

**Problem**: Pre-loading too much context wastes space; having too little requires multiple rounds of back-and-forth.

**Solution**: Let AI request context as needed.

**Implementation:**

**Lazy Context Loading:**
```bash
claude-code prompt "I need to add social login (Google, GitHub) to our authentication system.

First, tell me which files you need to understand:
1. To understand current authentication
2. To implement OAuth flow
3. To test the implementation

I'll tell you which to read, then you'll read only those."
```

**AI might respond:**
```
I need to see:
1. Current auth: src/auth/service.py, src/auth/routes.py
2. OAuth: Any existing OAuth configs, third-party API integrations
3. Testing: tests/test_auth.py pattern

Should I proceed with reading these?
```

**Progressive Disclosure:**
```bash
# Start minimal
claude-code prompt "Implement OAuth login. Start by asking what you need to know."

# AI asks questions
# AI: "Which OAuth providers? What's your existing auth method? Where should I integrate?"

# You answer
claude-code prompt "Google and GitHub. JWT-based auth in src/auth/. Integrate as alternative to password login."

# AI asks for specific files
# AI: "Can I read src/auth/jwt_handler.py to understand token generation?"

# You approve
claude-code prompt "Yes, read that file."

# AI implements with perfect context
```

## Real-World AIDD Context Engineering Example

Let's walk through a complete example: Building a blog API with proper context engineering.

### Scenario
You're building a blog API with posts, comments, and user management using FastAPI, PostgreSQL, and SQLAlchemy.

### Session 1: Project Initialization and Context Setup

```bash
# Step 1: Initialize project context
claude-code prompt "I'm starting a new project: Blog API

Tech Stack:
- Python 3.11
- FastAPI 0.104
- PostgreSQL 15
- SQLAlchemy 2.0
- Pydantic v2
- pytest for testing

Create initial project structure following Python best practices:
- Separate concerns (api, services, models, schemas)
- Configuration management
- Testing structure
- Development tools setup (Black, mypy, pytest)

Generate:
1. Directory structure
2. requirements.txt
3. pyproject.toml
4. README.md with setup instructions
5. .gitignore
6. Basic main.py with FastAPI app"
```

```bash
# Step 2: Establish code patterns
claude-code prompt "Before we implement features, let's establish our coding patterns.

Create PATTERNS.md documenting:
1. Service Layer Pattern (how services should be structured)
2. Repository Pattern (database access)
3. Error Handling Pattern
4. API Response Format
5. Testing Pattern

Use actual code examples for each pattern."
```

```bash
# Step 3: Create memory infrastructure
claude-code prompt "Create these tracking files:

1. DECISIONS.md - Architectural decisions
2. TODO.md - Feature backlog
3. GOTCHAS.md - Known issues and workarounds

Initialize them with our first decision: 'Using layered architecture (API -> Service -> Repository)'"
```

### Session 2: Implementing Core Features

```bash
# Load project context at session start
claude-code prompt "Read:
- PATTERNS.md (understand our patterns)
- DECISIONS.md (understand our architecture)
- TODO.md (see what's next)

Then confirm you understand the project structure and patterns before we proceed."
```

```bash
# Implement first feature with full context
claude-code prompt "Implement User Management following our patterns in PATTERNS.md:

Requirements:
1. User model with fields: id, email, username, hashed_password, created_at
2. UserService with methods: create_user, get_user, update_user, delete_user, list_users
3. UserRepository for database operations
4. API routes: POST /users, GET /users/{id}, PUT /users/{id}, DELETE /users/{id}, GET /users
5. Pydantic schemas: UserCreate, UserUpdate, UserResponse
6. Password hashing with bcrypt
7. Comprehensive input validation

Generate:
- models/user.py
- repositories/user_repository.py
- services/user_service.py
- schemas/user_schema.py
- api/routes/users.py
- tests/test_user_service.py

Follow exact patterns from PATTERNS.md"
```

```bash
# Update memory after implementation
claude-code prompt "Update TODO.md:
- Mark 'User Management' as complete
- Add 'Post Management' as next task
- Add 'Authentication' as future task

Update DECISIONS.md with decision:
'Using bcrypt for password hashing with cost factor 12 for security/performance balance'"
```

### Session 3: Adding Related Features

```bash
# Start with context refresh
claude-code prompt "Read TODO.md and PATTERNS.md to refresh context.

Next task from TODO: Implement Post Management

First, analyze the User implementation we created:
- src/models/user.py
- src/services/user_service.py  
- src/repositories/user_repository.py

Then tell me if you understand the pattern and are ready to implement Post Management following the same structure."
```

```bash
# Implement with reference to existing code
claude-code prompt "Implement Post Management following the EXACT same pattern as User Management:

Requirements:
1. Post model: id, title, content, author_id (FK to User), created_at, updated_at
2. PostService with CRUD operations
3. PostRepository
4. API routes with proper relationships to users
5. Pydantic schemas
6. Tests

Key differences from User:
- Posts have author relationship (Many-to-One with User)
- Only authenticated users can create/update/delete posts
- Anyone can read posts (public)

Generate all necessary files following established patterns."
```

```bash
# Context compression checkpoint
claude-code prompt "We've now implemented User and Post management. Create a checkpoint summary:

## CHECKPOINT_001.md

### Completed Features
- User Management (full CRUD)
- Post Management (full CRUD with user relationship)

### Architecture Established
- [Summary of layers and patterns]

### Next Steps
- [What's remaining]

### Code Quality
- Test coverage: [percentage]
- Key patterns working well
- Potential improvements

Keep it concise - 300 words max."
```

### Session 4: Complex Feature with Multiple Contexts

```bash
# Load checkpoint and relevant context
claude-code prompt "Read CHECKPOINT_001.md to understand project status.

Next feature: Comment System
This touches multiple existing features (Users, Posts).

Before implementing:
1. Read src/models/user.py and src/models/post.py to understand existing relationships
2. Analyze how we handle relationships in existing code
3. Propose the Comment model design with relationships

Don't implement yet - just design and explain."
```

```bash
# Implement with complex context
claude-code prompt "Approved. Implement Comment System:

Requirements:
1. Comment model: id, content, author_id (FK User), post_id (FK Post), parent_id (self-referential for nested comments), created_at
2. Support nested comments (replies to comments)
3. CommentService with methods: create_comment, get_comment, update_comment, delete_comment, get_post_comments (with threading)
4. API routes with proper nesting: POST /posts/{post_id}/comments, GET /comments/{id}, etc.
5. Only comment authors can edit/delete
6. Deleting a comment soft-deletes it (preserves thread structure)

This is complex - ask questions before implementing if anything is unclear about:
- Nested comment structure
- Deletion behavior
- Permission logic"
```

### Session 5: Testing and Refinement

```bash
# Context for testing session
claude-code prompt "Read all implemented services:
- src/services/user_service.py
- src/services/post_service.py
- src/services/comment_service.py

Then analyze our existing test patterns in:
- tests/test_user_service.py

Generate comprehensive integration tests that test:
1. Complete user flows (register -> create post -> comment)
2. Permission edge cases (users can't edit others' content)
3. Relationship integrity (deleting user affects posts, deleting post affects comments)
4. Nested comment threading

Aim for 85%+ coverage."
```

### Session 6: Documentation and Deployment Prep

```bash
# Documentation context
claude-code prompt "We're ready to document the API. Read:
- All API route files in src/api/routes/
- All schema files in src/schemas/

Generate comprehensive API documentation:
1. OpenAPI spec (FastAPI auto-generates, but enhance with examples)
2. README.md with:
   - Setup instructions
   - API endpoint reference
   - Authentication guide
   - Example requests/responses
3. DEPLOYMENT.md with production considerations"
```

## Claude Code vs Gemini CLI: Context Management Differences

Both tools handle context differently. Understanding these differences helps you choose the right tool and strategy.

### Claude Code Context Management

**Strengths:**
- **MCP (Model Context Protocol) Integration**: Can use MCP servers for extended context sources
- **Strong Reasoning**: Better at maintaining context coherence across complex refactoring
- **File Operation Intelligence**: Smart about which files to read based on task

**Context Loading:**
```bash
# Claude Code automatically explores relevant files
claude-code prompt "Refactor authentication to support multiple identity providers"
# Claude will identify and read relevant auth files intelligently
```

**Best Practices:**
- Let Claude explore project structure first
- Provide high-level goals, Claude determines needed context
- Use for complex architecture and refactoring tasks
- Ideal for tasks requiring deep code understanding

**Example Session:**
```bash
# Start broad
claude-code prompt "Analyze this FastAPI project structure and identify areas for improvement"

# Claude explores and reports findings

# Implement improvements
claude-code prompt "Refactor the authentication module based on your analysis"

# Claude reads necessary files and implements coherent changes
```

### Gemini CLI Context Management

**Strengths:**
- **Massive Context Window**: 1M tokens allows loading entire large codebases
- **Fast Processing**: Handles large context efficiently
- **Session Persistence**: Named sessions maintain context across invocations

**Context Loading:**
```bash
# Gemini can handle entire codebase
gemini chat --session analysis "Read all Python files in src/ and create an architectural diagram"

# Continue in same session with full context
gemini chat --session analysis "Now find all database queries and list potential N+1 problems"
```

**Best Practices:**
- Use for large codebase analysis
- Good for documentation generation (needs access to many files)
- Ideal for pattern detection across large projects
- Use sessions for multi-step analysis

**Example Session:**
```bash
# Start session with massive context load
gemini chat --session refactor "Read entire src/ directory (100+ files) and identify duplicate code patterns"

# Continue in session
gemini chat --session refactor "Create a refactoring plan to eliminate the duplicates you found"

# Implement in same session
gemini chat --session refactor "Implement the refactoring plan for the authentication duplicates"
```

### Context Management Comparison Table

| Feature | Claude Code | Gemini CLI |
|---------|-------------|------------|
| Context Window | 200K tokens (~150K words) | 1M tokens (~750K words) |
| Smart File Selection | Excellent | Good |
| Session Persistence | Via conversation | Named sessions |
| Best For | Complex reasoning, refactoring | Large codebase analysis |
| Context Loading | Just-in-time (smart) | Bulk loading possible |
| Multi-Turn Context | Strong coherence | Strong with sessions |
| MCP Integration | Yes | No (as of now) |
| Speed | Fast | Very fast with large context |

### Hybrid Approach

For complex projects, use both tools strategically:

```bash
# Use Gemini for initial analysis (leverage large context window)
gemini chat --session analysis "Read all 200 files in src/ and docs/ and create a comprehensive project report including architecture, patterns, and potential issues"

# Use Claude Code for implementation (better reasoning)
claude-code prompt "Based on the analysis from Gemini [paste relevant parts], refactor the authentication module to follow microservices pattern"

# Use Gemini for documentation (needs access to many files)
gemini chat --session docs "Read all implemented files and generate API documentation with examples"

# Use Claude Code for complex debugging (better reasoning)
claude-code prompt "Debug the intermittent race condition in the payment processing that occurs under high load"
```

## Common Context Engineering Pitfalls in AIDD

### Pitfall 1: Context Overload at Session Start

**Bad Practice:**
```bash
claude-code prompt "Read the entire src/ directory (100 files) and implement a new authentication system"
```

**Why It's Bad:**
- Fills context window immediately
- AI must process irrelevant files
- Slower responses
- Context rot happens faster

**Good Practice:**
```bash
# Step 1: Understand high-level structure
claude-code prompt "Analyze the directory structure of src/ without reading files. Tell me where authentication-related code likely lives."

# Step 2: Load only relevant context
claude-code prompt "Now read only the authentication-related files you identified"

# Step 3: Implement
claude-code prompt "Implement the new authentication feature following existing patterns"
```

### Pitfall 2: Losing Context Between Sessions

**Bad Practice:**
```bash
# Day 1
claude-code prompt "Implement user management"

# Day 2 (new session, no context loading)
claude-code prompt "Add post management"
# AI has no idea about the user management implementation!
```

**Good Practice:**
```bash
# Day 1
claude-code prompt "Implement user management"
# ... implementation ...
claude-code prompt "Create PROGRESS.md documenting what we built and the patterns we established"

# Day 2 (new session, load context)
claude-code prompt "Read PROGRESS.md to understand what we built yesterday. Then implement post management following the same patterns."
```

### Pitfall 3: Mixing Contexts Without Boundaries

**Bad Practice:**
```bash
claude-code prompt "I'm working on authentication but also need to fix this bug in the payment system and also redesign the database schema"
```

**Why It's Bad:**
- Confuses AI about current focus
- Mixes unrelated context
- Lower quality results for all tasks

**Good Practice:**
```bash
# Complete one task first
claude-code prompt "Focus only on authentication: implement JWT token validation middleware"

# Then explicitly switch context
claude-code prompt "Authentication is complete. Now switching context to payment system bug. Forget about auth for now. Here's the payment bug: [details]"
```

### Pitfall 4: Not Maintaining Architectural Memory

**Bad Practice:**
```bash
# No record of decisions
claude-code prompt "Implement feature X"
# AI makes architectural choice

# Later...
claude-code prompt "Implement feature Y"
# AI makes contradictory architectural choice!
```

**Good Practice:**
```bash
# Document decisions
claude-code prompt "Implement feature X. After implementation, update DECISIONS.md with any architectural decisions made."

# Later, load decisions
claude-code prompt "Read DECISIONS.md. Implement feature Y following the same architectural approach we used for feature X."
```

### Pitfall 5: Ignoring Context Budget

**Bad Practice:**
```bash
# Never checking context usage
claude-code prompt "Let's add another feature"
claude-code prompt "And another feature"  
claude-code prompt "And fix this bug"
# ... conversation continues indefinitely until context degradation is severe
```

**Good Practice:**
```bash
# Every 10-15 interactions or major feature
claude-code prompt "We've been working for a while. Create a context checkpoint:
1. Summarize what we've built
2. Document key patterns and decisions
3. List what's next

Save to CHECKPOINT_[date].md"

# Start fresh session
# Load checkpoint in new session
claude-code prompt "Read CHECKPOINT_2025_01_15.md and continue from there"
```

## Measuring Context Engineering Effectiveness

How do you know if your context engineering is effective? Use these metrics:

### 1. First-Attempt Accuracy
**Metric**: Percentage of times AI generates correct code on first attempt
**Target**: 70%+ for routine tasks, 50%+ for complex tasks
**Improve**: Add more pattern examples, better constraints

### 2. Context Relevance Score
**Metric**: Ratio of (context used by AI) / (total context provided)
**Target**: 70%+ (indicates efficient context loading)
**Improve**: Use just-in-time loading, better file targeting

### 3. Session Productivity
**Metric**: Features implemented per session before context degradation
**Target**: 3-5 complete features per session
**Improve**: Better compression, earlier checkpoint creation

### 4. Consistency Across Sessions
**Metric**: Code style and pattern consistency between sessions
**Target**: 90%+ pattern adherence
**Improve**: Better memory files, pattern documentation

### 5. Debug Efficiency
**Metric**: Percentage of bugs AI can debug without additional context
**Target**: 80%+ when context is properly loaded
**Improve**: Include error logs, stack traces, related code in context

## Context Engineering Checklist for AIDD

Use this checklist at the start of every development session:

### Pre-Session Setup
- [ ] Understand the task scope and complexity
- [ ] Identify relevant context sources (files, docs, memory files)
- [ ] Choose appropriate tool (Claude Code vs Gemini CLI)
- [ ] Decide on session strategy (single session vs multiple isolated sessions)

### Session Initialization
- [ ] Load project overview (README, ARCHITECTURE docs)
- [ ] Load relevant memory files (DECISIONS, PATTERNS, TODO)
- [ ] Load recent checkpoint if continuing from previous session
- [ ] Verify AI understands project context before proceeding

### During Development
- [ ] Load context just-in-time (don't preload everything)
- [ ] Request specific files when needed
- [ ] Update memory files as decisions are made
- [ ] Monitor context usage (compress if feeling degradation)

### Session Checkpointing
- [ ] Every 10-15 interactions: Consider context compression
- [ ] After major features: Create checkpoint summary
- [ ] Before ending session: Update memory files
- [ ] Document any new patterns or decisions

### Post-Session Cleanup
- [ ] Update TODO with completed tasks and next steps
- [ ] Create session summary if major work completed
- [ ] Note any issues or context management improvements needed

## Conclusion: The Art and Science of AIDD Context Engineering

Context engineering is where AIDD transforms from "AI writes some code" to "AI acts as your development partner." Mastering context engineering means:

**Understanding Context Limitations:**
- Context windows are finite
- Context degrades as it fills
- Not all context is equally valuable

**Strategic Context Management:**
- Load progressively, not all at once
- Compress periodically to maintain quality
- Isolate contexts for different tasks

**Systematic Approach:**
- Use memory files to persist key information
- Create checkpoints for continuity
- Document patterns and decisions

**Tool-Specific Optimization:**
- Leverage Claude Code's smart file selection
- Use Gemini's massive context for large codebases
- Hybrid approaches for complex projects

In Chapter 9, you learned what to say to AI. In this chapter, you learned what AI needs to know to understand what you're saying. Together, these two skills form the foundation of effective AI-Driven Development.

**Key Takeaways:**

1. **Context > Prompts**: Rich context enables simple prompts to produce great results
2. **Progressive Loading**: Load context as needed, not all upfront
3. **Memory Files**: Persist important context outside conversation
4. **Compress Regularly**: Prevent context rot with periodic compression
5. **Isolate Contexts**: Separate contexts for separate concerns
6. **Examples Rule**: Show AI your patterns through concrete examples
7. **Budget Awareness**: Monitor and manage context usage actively

In the next chapter, we'll put both prompt engineering and context engineering into practice as we build a complete production-grade REST API from scratch using Python, FastAPI, and Claude Code.

## Practice Exercises

### Exercise 1: Context Budget Analysis
Take a real coding session and analyze:
- What context was loaded?
- How much was actually used by AI?
- What could have been loaded just-in-time instead?
- When did context degradation start (if at all)?

### Exercise 2: Memory File Creation
For your current project, create:
- PATTERNS.md documenting 3 code patterns
- DECISIONS.md documenting 3 architectural decisions
- TODO.md with prioritized task list
- GOTCHAS.md with 3 known issues/solutions

### Exercise 3: Multi-Session Continuity
Test session continuity:
1. Start a feature implementation
2. Stop mid-way and create a checkpoint
3. New session next day: Load checkpoint and continue
4. Measure: How well did AI maintain consistency?

### Exercise 4: Context Compression Practice
Take a long conversation with AI (15+ interactions):
1. Practice compressing it into a 300-word summary
2. Start fresh session with summary
3. Compare AI performance with summary vs full history

### Exercise 5: Tool Comparison
Same task with both tools:
1. Implement a feature with Claude Code
2. Implement same feature with Gemini CLI
3. Compare: context management approach, results, efficiency


