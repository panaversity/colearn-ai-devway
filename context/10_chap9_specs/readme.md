/sp.specify Write chapter 9 in Part 3 of the book. The title of the chapter will be "Prompt Engineering for AI-Driven Development".

## Introduction: Why Prompt Engineering is Critical in AIDD

In the era of AI-Driven Development (AIDD), your ability to communicate with AI coding agents like Claude Code and Gemini CLI directly determines your productivity and the quality of your code. Unlike traditional programming where you write every line yourself, AIDD transforms you into an "AI director" who guides intelligent agents to build software systems.

**The paradigm shift:**
- **Traditional Development**: You are the code writer
- **AI-Driven Development**: You are the architect and AI orchestrator

According to recent studies, developers using AI coding assistants are 55% more productive, but only when they master effective prompting techniques. Poor prompts lead to buggy code, architectural mistakes, and more time spent fixing AI-generated errors than writing code manually.

This chapter will teach you the complete prompting framework specifically designed for AIDD, combining proven techniques from general AI prompting with developer-specific strategies for Claude Code and Gemini CLI.

## Understanding AI Coding Agents: How They Think

Before diving into prompting techniques, you need to understand how AI coding agents work fundamentally differently from traditional IDEs or autocomplete tools.

### The Context Window: Your AI Agent's Memory

AI coding agents like Claude Code and Gemini CLI operate within a **context window**—a limited memory space where they hold:
- Your current conversation history
- Files you've explicitly shared or they've read
- System prompts and instructions
- Their current understanding of your project

**Key implications:**
- Context is finite (Claude Sonnet 4.5: ~200,000 tokens ≈ 150,000 words)
- Information outside the context doesn't exist to the AI
- You must actively manage what information is available
- Long conversations can "push out" earlier context

### How AI Agents Generate Code

When you prompt an AI coding agent, it:
1. **Analyzes your prompt** using natural language understanding
2. **Retrieves relevant patterns** from training data (billions of lines of code)
3. **Generates responses token-by-token** (word by word, or in code: symbol by symbol)
4. **Self-corrects** based on logical consistency and programming conventions

**This means:**
- Clearer prompts = More accurate code
- Specific technical constraints prevent common mistakes
- Iterative refinement is built into the workflow
- AI learns from corrections within the conversation

## The AIDD Prompting Framework: 8 Essential Elements

Building on the proven 6-part prompting framework and extending it for software development, here's the complete AIDD prompting structure:

### 1. Command: Direct and Developer-Specific

In AIDD, your commands should use precise technical verbs that align with software development tasks.

**Weak Developer Commands:**
```
Help me with this code
Fix my bug
Make this better
```

**Strong Developer Commands:**
```
Refactor the authentication module to use JWT tokens instead of session cookies

Debug the race condition in the async data fetching logic

Implement a responsive navbar component with mobile hamburger menu using TypeScript and Tailwind

Generate comprehensive unit tests for the UserService class with edge cases
```

**Technical Action Verbs for AIDD:**
- **Create/Implement**: Build new features or components
- **Refactor**: Restructure existing code without changing behavior
- **Debug**: Identify and fix specific issues
- **Optimize**: Improve performance, memory usage, or efficiency
- **Generate**: Produce boilerplate, tests, or documentation
- **Analyze**: Review code for issues, patterns, or improvements
- **Migrate**: Convert code between languages, frameworks, or versions
- **Integrate**: Connect different systems or APIs

**Pro Tip**: Start every development session with a clear command that sets the technical direction.

### 2. Context: The Foundation of Good AI Code

Context in AIDD is multi-dimensional. Unlike general AI prompting, you need to provide **technical context** that encompasses your entire development environment.

#### The AIDD Context Stack:

**Layer 1: Project Context**
```
Project: E-commerce platform backend
Tech Stack: Python 3.11, FastAPI, PostgreSQL, Docker
Architecture: Microservices with RESTful APIs
Current Phase: MVP development, focusing on user authentication
```

**Layer 2: Code Context**
```
Working on: /src/auth/services.py
Related files: /src/auth/models.py, /src/auth/schemas.py
Database: Users table with email, hashed_password, created_at fields
Current issue: Token refresh endpoint returning 401 errors
```

**Layer 3: Constraint Context**
```
Requirements:
- Must follow PEP 8 style guidelines
- All functions need type hints
- Security: Implement rate limiting on auth endpoints
- Performance: Response time under 200ms
- Testing: Minimum 80% code coverage
```

**Layer 4: Developer Context**
```
Experience level: Intermediate Python, learning FastAPI
Preferences: Prefer explicit over implicit, comprehensive comments
Time constraint: Need working prototype by Friday
```

#### Context Strategies for Claude Code & Gemini CLI:

**1. Use the File System Effectively**
```bash
# Claude Code can read your entire project structure
claude-code prompt "Analyze the project structure and suggest improvements to the auth module"

# Explicitly reference files
claude-code prompt "Look at src/auth/services.py and src/auth/models.py, then refactor the password hashing logic"
```

**2. Provide Code Snippets in Context**
```
I have this User model:

```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
```

Create a UserService class that handles CRUD operations with proper error handling and type hints.
```

**3. Reference Documentation**
```
Following the FastAPI official documentation for dependency injection, implement a get_current_user dependency that validates JWT tokens and returns the authenticated user object.
```

### 3. Logic: Define the Technical Approach

In AIDD, "logic" means specifying the algorithmic approach, design patterns, and implementation strategy you want the AI to follow.

**Basic Logic Specification:**
```
Implement user registration with the following logic:
1. Validate email format using regex
2. Check if email already exists in database
3. Hash password using bcrypt with salt rounds = 12
4. Create user record in database
5. Return user object without password field
6. Handle all exceptions with appropriate HTTP status codes
```

**Advanced Logic with Design Patterns:**
```
Refactor the payment processing system using the Strategy Pattern:

1. Create a PaymentStrategy abstract base class with process_payment() method
2. Implement concrete strategies: CreditCardPayment, PayPalPayment, CryptoPayment
3. Create a PaymentContext class that accepts any strategy
4. Each strategy should handle its own validation and error handling
5. Return a uniform PaymentResult object regardless of strategy used

Use dependency injection for strategy selection based on configuration.
```

**Algorithmic Logic:**
```
Implement a caching mechanism for API responses:

Algorithm:
- Use LRU (Least Recently Used) cache with max size 1000 items
- Cache key: MD5 hash of request URL + query parameters
- Cache invalidation: 5-minute TTL (time to live)
- On cache miss: Fetch from API, store in cache, return response
- On cache hit: Return cached response immediately
- Handle cache failures gracefully (log but don't break requests)
```

**Testing Logic:**
```
Generate unit tests following this structure:
1. Test happy path with valid inputs
2. Test edge cases (empty strings, null values, boundary conditions)
3. Test error conditions (network failures, invalid data)
4. Mock external dependencies (database, APIs)
5. Use pytest fixtures for test data setup
6. Aim for 90%+ code coverage
```

### 4. Roleplay: Specialized Technical Expertise

In AIDD, roleplay transforms the AI from a generic code generator into a specialized technical expert in your specific domain.

**Generic Developer Role:**
```
You are an experienced software developer.
```

**Specialized AIDD Roles:**

**Backend Developer:**
```
You are a senior backend engineer with 10 years of experience building scalable REST APIs using Python and FastAPI. You specialize in authentication systems, database optimization, and microservices architecture. You prioritize security, performance, and maintainable code. You always include proper error handling, logging, and comprehensive docstrings.
```

**Frontend Developer:**
```
You are an expert frontend developer specializing in React and TypeScript with 8 years of experience building enterprise web applications. You follow modern best practices including component composition, custom hooks, and TypeScript strict mode. You prioritize accessibility (WCAG 2.1 AA), responsive design, and performance optimization.
```

**DevOps Engineer:**
```
You are a DevOps engineer with expertise in Docker, Kubernetes, and CI/CD pipelines. You specialize in infrastructure as code using Terraform, container orchestration, and automated deployment workflows. You prioritize security, reliability, and scalability in all infrastructure decisions.
```

**Data Scientist:**
```
You are a data scientist with expertise in Python, pandas, scikit-learn, and TensorFlow. You specialize in building production-ready machine learning pipelines with proper data validation, feature engineering, and model evaluation. You follow MLOps best practices and always consider model interpretability.
```

**Style and Approach Modifiers:**

```
Be pragmatic and focused on working code over perfect code.
Prioritize readability and maintainability over cleverness.
Follow the principle "Make it work, make it right, make it fast" in that order.
Write defensive code that anticipates edge cases and handles errors gracefully.
Include TODO comments for future improvements but deliver working solutions now.
```

**Anti-Pattern Awareness:**
```
You are aware of common Python anti-patterns and actively avoid them:
- No mutable default arguments
- Proper exception handling (never bare except clauses)
- Avoid global state
- Use context managers for resource cleanup
- Follow SOLID principles but don't over-engineer
```

### 5. Formatting: Structure for Development Workflows

In AIDD, formatting goes beyond visual presentation—it determines how easily you can integrate AI-generated code into your workflow.

#### Code Output Formatting:

**Option 1: Complete Files**
```
Generate the complete implementation of UserService class in a production-ready format:
- Include all necessary imports at the top
- Add comprehensive docstrings (Google style)
- Include type hints for all functions
- Add inline comments for complex logic
- Format according to PEP 8 and Black formatter standards
- Output as a complete .py file ready to copy-paste
```

**Option 2: Code Snippets with Integration Points**
```
Provide the JWT authentication middleware as a snippet that can be inserted into:
- File: src/middleware/auth.py
- Location: After the existing rate limiting middleware
- Include: Import statements needed at top of file
- Format: Properly indented to match existing code style
```

**Option 3: Diff-Style Changes**
```
Show the refactoring changes in diff format:
- Clearly mark lines to remove with "- "
- Clearly mark lines to add with "+ "
- Provide context lines around changes
- Group related changes together
- Include file paths for each change
```

#### Documentation Formatting:

**API Documentation:**
```
Generate FastAPI route documentation in the following format:

For each endpoint include:
1. HTTP method and path
2. Description (one sentence)
3. Request body schema (JSON example)
4. Response schema (JSON example with status codes)
5. Error responses (all possible error codes)
6. Example curl command

Format as Markdown that can be added to README.md
```

**Code Comments:**
```
Add comments following this structure:
- Module-level docstring: Purpose and high-level architecture
- Class docstring: Responsibilities and usage examples
- Function docstring: Google style with Args, Returns, Raises sections
- Inline comments: Only for complex logic that isn't self-evident
- TODO comments: For known limitations or future enhancements
```

#### Test Output Formatting:

```
Generate pytest test cases formatted as:
- One test class per function/method being tested
- Test function names: test_<function>_<scenario>_<expected_result>
- Use descriptive assertion messages
- Group related tests with markers (@pytest.mark.unit, @pytest.mark.integration)
- Include fixtures in conftest.py separately
- Output as complete test file with all necessary imports
```

### 6. Technical Constraints: The AIDD-Specific Element

This is unique to AIDD prompting. Technical constraints ensure the AI generates code that fits your exact requirements, dependencies, and environment.

#### Dependency Constraints:

```
Technical Constraints:
- Python version: 3.11 (use match-case statements, not Python 3.9 compatible)
- FastAPI version: 0.104.0 (use latest Annotated syntax)
- Database: PostgreSQL 15 with SQLAlchemy 2.0 (use new ORM syntax)
- No additional dependencies beyond requirements.txt
- Must work in Docker container (Alpine Linux base)
```

#### Performance Constraints:

```
Performance Requirements:
- API response time: < 200ms for 95th percentile
- Database queries: Use proper indexing, limit N+1 queries
- Memory usage: Keep under 512MB per container instance
- Concurrent connections: Handle at least 1000 simultaneous users
```

#### Security Constraints:

```
Security Requirements:
- All user inputs must be validated and sanitized
- Use parameterized queries (no raw SQL)
- Implement rate limiting: 100 requests per minute per IP
- All passwords must be hashed with bcrypt (cost factor 12)
- JWT tokens expire after 1 hour with refresh token mechanism
- CORS configured for frontend domain only
- No sensitive data in logs
```

#### Code Quality Constraints:

```
Code Quality Standards:
- Type hints required for all functions (use mypy for validation)
- Minimum test coverage: 80% (measured by pytest-cov)
- No pylint errors, minimal warnings
- All functions under 50 lines (complex functions should be split)
- Cyclomatic complexity under 10 per function
- Follow Google Python Style Guide
```

#### Integration Constraints:

```
Integration Requirements:
- Must integrate with existing Redis cache layer (redis-py client)
- Authentication must work with existing frontend React app (expecting specific JWT payload structure)
- Logging must use existing structlog configuration
- Database migrations via Alembic (generate migrations, don't modify existing)
- Must work with current CI/CD pipeline (GitHub Actions, no breaking changes)
```

### 7. Examples: Show, Don't Just Tell

In AIDD, providing examples of existing code, desired patterns, or similar implementations dramatically improves AI output quality.

#### Code Pattern Examples:

```
Here's how we handle other service classes in our codebase:

```python
class ProductService:
    def __init__(self, db: Session):
        self.db = db
    
    async def get_product(self, product_id: int) -> ProductSchema:
        product = await self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return ProductSchema.from_orm(product)
```

Create a similar UserService class following this exact pattern.
```

#### Style Examples:

```
Match the existing error handling pattern used in the codebase:

```python
try:
    result = await some_operation()
except DatabaseError as e:
    logger.error(f"Database error in operation: {str(e)}")
    raise HTTPException(status_code=500, detail="Database error occurred")
except ValidationError as e:
    logger.warning(f"Validation error: {str(e)}")
    raise HTTPException(status_code=400, detail=str(e))
```

Apply this same error handling pattern to the new authentication endpoints.
```

#### Test Examples:

```
Follow this testing pattern from existing tests:

```python
@pytest.mark.asyncio
async def test_create_product_success(db_session, sample_product_data):
    """Test successful product creation with valid data."""
    service = ProductService(db_session)
    result = await service.create_product(sample_product_data)
    
    assert result.id is not None
    assert result.name == sample_product_data.name
    assert result.price == sample_product_data.price
```

Create similar tests for UserService following this exact structure and naming convention.
```

#### API Response Examples:

```
Our API responses follow this structure:

Success Response:
```json
{
  "status": "success",
  "data": {
    "user": {
      "id": 123,
      "email": "user@example.com",
      "created_at": "2025-01-15T10:30:00Z"
    }
  },
  "message": "User created successfully"
}
```

Error Response:
```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": {
      "field": "email",
      "provided": "invalid-email"
    }
  }
}
```

Ensure all new endpoints follow this exact response structure.
```

### 8. Iterative Questions: The AI as Technical Consultant

The most powerful technique in AIDD is using the AI as a technical consultant that asks clarifying questions before generating code.

#### The Question-Driven Development Process:

**Step 1: Initial Prompt with Question Request**
```
I need to implement a user authentication system for a FastAPI application.

Before you provide an implementation, ask me 10 detailed technical questions that will help you create the most appropriate solution for my specific needs.
```

**Step 2: AI Asks Clarifying Questions**
The AI might ask:
1. What authentication method do you prefer: JWT, OAuth2, session-based, or a combination?
2. Do you need social login (Google, GitHub, etc.) or just email/password?
3. What's your database: PostgreSQL, MySQL, MongoDB? Which ORM: SQLAlchemy, Tortoise, raw queries?
4. Do you need role-based access control (RBAC) or just basic authentication?
5. What's your token expiration strategy: short-lived access tokens with refresh tokens, or long-lived tokens?
6. Do you need email verification for new users?
7. What's your password policy: minimum length, complexity requirements, password reset flow?
8. Do you need rate limiting on authentication endpoints?
9. Are there any existing authentication systems this needs to integrate with?
10. What's your testing strategy: unit tests, integration tests, or both?

**Step 3: Provide Detailed Answers**
```
1. JWT with refresh token mechanism
2. Just email/password for now, social login in future phase
3. PostgreSQL 15 with SQLAlchemy 2.0
4. RBAC with roles: admin, user, guest
5. Access token: 15 min expiration, Refresh token: 7 days, rotating refresh tokens
6. Yes, email verification required before login
7. Password policy: min 8 chars, must include uppercase, lowercase, number, special char. Password reset via email link.
8. Yes, rate limiting: 5 login attempts per minute per IP
9. No existing systems, this is greenfield
10. Both unit and integration tests, aiming for 85% coverage
```

**Step 4: AI Generates Tailored Solution**

After your answers, the AI can generate precisely what you need instead of a generic solution.

#### Advanced Question Techniques for AIDD:

**Architecture Review Questions:**
```
I've implemented the basic authentication system. Now review my architecture and ask me 10 questions about:
- Scalability concerns
- Security vulnerabilities  
- Performance bottlenecks
- Code maintainability issues
- Missing features or edge cases

Be specific about which files or functions you're questioning.
```

**Debugging Question Process:**
```
I'm getting a "Connection pool exhausted" error in production but not in development.

Before suggesting solutions, ask me debugging questions about:
- Environment configurations
- Traffic patterns and load
- Database connection settings
- Resource monitoring data
- Recent changes or deployments

Ask questions in priority order (most likely causes first).
```

**Optimization Questions:**
```
My API endpoint is slow (response time: 2 seconds average).

Before optimizing, ask me questions about:
- What the endpoint does (database queries, external APIs, computations)
- Current performance metrics (database query times, external API latency)
- Caching strategy currently in use
- Expected load and usage patterns
- Acceptable trade-offs (memory vs speed, accuracy vs performance)
```

## Complete AIDD Prompt Examples

### Example 1: Feature Implementation

```
**COMMAND:**
Implement a complete user registration system with email verification

**CONTEXT:**
Project: SaaS analytics platform backend
Tech Stack: Python 3.11, FastAPI 0.104, PostgreSQL 15, SQLAlchemy 2.0, Redis for cache
Architecture: Monolithic REST API (transitioning to microservices later)
Current State: Basic FastAPI app structure exists, database models for User table defined
Team: 2 backend developers, 1 frontend developer

**LOGIC:**
Implementation flow:
1. User submits registration form (email, password, name)
2. Validate email format and check uniqueness
3. Hash password using bcrypt (cost factor 12)
4. Generate verification token (UUID4) with 24-hour expiration
5. Store user in database with is_verified=False status
6. Send verification email via SendGrid API (existing email service)
7. User clicks verification link in email
8. API verifies token and updates is_verified=True
9. Return JWT access token upon successful verification

**ROLEPLAY:**
You are a senior backend engineer specializing in authentication systems and secure API design. You have deep expertise in FastAPI, SQLAlchemy, and modern Python async patterns. You prioritize security best practices (OWASP guidelines), proper error handling, and code that's easy to test and maintain.

**TECHNICAL CONSTRAINTS:**
- Use FastAPI dependency injection for database sessions
- All endpoints must have proper type hints (validate with mypy)
- Password hashing: bcrypt with cost factor 12 (no argon2 or other libraries)
- Email service: Use existing EmailService class in src/services/email.py
- Database: Use existing session management (src/database/session.py)
- Token storage: Store verification tokens in Redis (TTL: 24 hours)
- Rate limiting: 3 registration attempts per hour per IP
- Validation: Use Pydantic models for request/response schemas
- Logging: Use existing structlog configuration

**FORMATTING:**
Provide the implementation as:
1. File: src/auth/registration.py (complete file with all imports)
2. Pydantic schemas in: src/auth/schemas.py (just the new schemas)
3. Database model changes in: src/auth/models.py (additions only)
4. New API routes in: src/api/routes/auth.py (route definitions)
5. Include example curl commands for testing each endpoint

Format code with Black formatter standards, include comprehensive docstrings.

**EXAMPLES:**
Here's how we structure other service classes:

```python
class ProductService:
    def __init__(self, db: Session, cache: Redis):
        self.db = db
        self.cache = cache
    
    async def create_product(self, product_data: ProductCreate) -> ProductResponse:
        """Create new product with caching."""
        # Implementation
```

Follow this same structure for the RegistrationService.

**QUESTIONS:**
Before implementing, ask me 8 questions about:
- Email template content and verification link URL structure
- Error handling preferences (return errors vs raise exceptions)
- Logging detail level (what should be logged)
- Testing approach (what tests do you want generated)
```

### Example 2: Debugging Session

```
**COMMAND:**
Debug the intermittent "Database connection timeout" errors occurring in production

**CONTEXT:**
Project: E-commerce order processing system
Tech Stack: Python 3.13, FastAPI, PostgreSQL 14, SQLAlchemy 1.4, deployed on AWS ECS
Issue: Started 3 days ago after deploying new batch processing feature
Frequency: 5-10 errors per hour, mostly during peak traffic (2-4 PM EST)
Impact: Orders failing to process, customer complaints increasing

Current observations:
- Error occurs in multiple endpoints, not isolated to one
- Database CPU usage spikes to 80% during errors
- Connection pool shows 20/20 connections in use (pool size: 20)
- No recent changes to database configuration
- New batch job processes 10,000 records every hour

**LOGIC:**
Debugging approach:
1. Analyze connection pool usage patterns
2. Identify long-running queries or connections
3. Check for connection leaks (connections not being released)
4. Review batch job database interaction
5. Examine transaction management and rollback handling
6. Propose configuration changes and code fixes

**ROLEPLAY:**
You are a database performance expert with 12 years experience optimizing PostgreSQL and fixing connection pool issues in Python applications. You excel at systematic debugging, reading query execution plans, and identifying resource bottlenecks. You provide practical, actionable solutions backed by performance data.

**TECHNICAL CONSTRAINTS:**
- Cannot increase database instance size (budget constraint)
- Must maintain backward compatibility with existing code
- Maximum acceptable connection pool size: 30 (ECS task limit)
- Cannot add new infrastructure components without approval
- Changes must be deployable via existing CI/CD pipeline
- Must implement monitoring to track fix effectiveness

**FORMATTING:**
Structure your response as:
1. Root Cause Analysis (specific findings with evidence)
2. Immediate Mitigation Steps (what to do right now)
3. Code Changes Required (exact file locations and code modifications)
4. Configuration Changes (database.ini, connection pool settings)
5. Monitoring Implementation (what metrics to track)
6. Long-term Recommendations (architectural improvements)

Use code blocks for all code examples, include comments explaining changes.

**QUESTIONS:**
Ask me 10 debugging questions to help diagnose the issue:
- Connection pool configuration details
- SQLAlchemy session management patterns
- Batch job implementation specifics
- Query patterns and ORM usage
- Recent code changes or deployments
- Database query logs or slow query logs available
- Current monitoring and alerting setup
```

### Example 3: Code Review and Refactoring

```
**COMMAND:**
Review and refactor the payment processing module for better maintainability, testability, and error handling

**CONTEXT:**
Project: Multi-tenant SaaS billing system
Current State: Payment module works but is difficult to test and extend
Tech Stack: Python 3.13, FastAPI, Stripe API, PostgreSQL
Problems:
- 300-line function handling multiple payment providers
- Tight coupling to Stripe API (hard to add new providers)
- Insufficient error handling (generic exceptions)
- No unit tests (only manual testing)
- Difficult to mock for testing
- Business logic mixed with API integration code

Code location: src/billing/payment_processor.py

**LOGIC:**
Refactoring strategy:
1. Analyze current code structure and identify code smells
2. Apply Strategy Pattern to separate payment providers
3. Introduce dependency injection for testability
4. Separate business logic from API integration
5. Implement comprehensive error handling with custom exceptions
6. Add type hints throughout
7. Create unit tests covering key scenarios

**ROLEPLAY:**
You are a software architect specializing in clean code, design patterns, and building maintainable systems. You have deep expertise in Python, API integration patterns, and test-driven development. You balance pragmatism with best practices, avoiding over-engineering while ensuring code quality.

**TECHNICAL CONSTRAINTS:**
- Must maintain existing API contracts (external clients depend on current response format)
- Cannot change database schema (migrations are frozen until next sprint)
- Must support existing payment providers: Stripe, PayPal (adding Square in future)
- Transaction processing must remain atomic (no partial payments)
- Response time must stay under 500ms
- Must be backward compatible with existing calling code

**FORMATTING:**
Provide the refactoring as:
1. Architecture Overview (diagram in Mermaid format showing new structure)
2. New file structure (list of new files to create)
3. Complete implementation of each new file
4. Migration guide (how to transition from old to new code)
5. Unit test examples (key test cases demonstrating testability)
6. Documentation updates (docstrings and README additions)

**EXAMPLES:**
We recently refactored the notification system using Strategy Pattern:

```python
class NotificationStrategy(ABC):
    @abstractmethod
    async def send(self, recipient: str, message: str) -> bool:
        pass

class EmailNotification(NotificationStrategy):
    async def send(self, recipient: str, message: str) -> bool:
        # Implementation
        
class NotificationService:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy
```

Apply a similar pattern to the payment processing system.

**QUESTIONS:**
Before refactoring, ask me 10 questions about:
- Business rules that must be preserved
- Error scenarios that must be handled
- Expected behavior for edge cases
- Testing requirements and coverage expectations
- Performance requirements for different operations
- Which payment provider to prioritize for initial refactoring
```

## Claude Code Specific Prompting Techniques

Claude Code has unique capabilities that require specific prompting strategies.

### 1. Project Context Loading

```bash
# Let Claude Code explore your project first
claude-code prompt "Analyze this project structure and give me a high-level overview of the architecture, main modules, and key patterns used."

# Then ask for specific work
claude-code prompt "Now that you understand the project, implement a new auth middleware following the existing patterns you identified."
```

### 2. Multi-File Operations

```bash
# Claude Code can work across multiple files
claude-code prompt "Refactor the user authentication across these files:
- src/auth/service.py
- src/auth/models.py  
- src/api/routes/auth.py
- tests/test_auth.py

Ensure consistency across all files and update tests accordingly."
```

### 3. Iterative Development Sessions

```bash
# Start broad
claude-code prompt "I need to add a REST API for managing products. Ask me questions about requirements."

# After answering questions
claude-code prompt "Good questions. Here are my answers: [detailed answers]
Now create the implementation."

# Review and iterate
claude-code prompt "The implementation looks good, but the error handling needs improvement. Make it more robust."

# Add tests
claude-code prompt "Now generate comprehensive pytest tests for the product API you just created."
```

### 4. Using MCP Tools

```bash
# Claude Code can use Model Context Protocol tools
claude-code prompt "Search my project for all database queries that might have N+1 problems. Use the codebase search tool to find patterns like 'for item in items: db.query(...)'"

# File operations
claude-code prompt "Read all files in src/models/ and create a comprehensive data model diagram in Mermaid format."
```

## Gemini CLI Specific Prompting Techniques

Gemini CLI works differently than Claude Code and requires adapted prompting strategies.

### 1. Session-Based Context

```bash
# Start a session for persistent context
gemini chat --session project-refactor

# Session maintains context across multiple prompts
gemini chat "I'm refactoring a Python Flask app. Current structure: [describe]"
gemini chat "Good context. Now help me convert the routes to use blueprints."
gemini chat "Perfect. Now update the test suite to match the new structure."
```

### 2. Code Generation with Gemini

```bash
# Gemini excels at code generation from specifications
gemini chat "Generate a Python FastAPI CRUD API with these specs:
- Resource: Products
- Fields: id (int), name (str), price (float), stock (int)
- Endpoints: GET /products, GET /products/{id}, POST /products, PUT /products/{id}, DELETE /products/{id}
- Use SQLAlchemy for database
- Include Pydantic schemas
- Add proper error handling
Output as complete, production-ready code."
```

### 3. Explanation and Documentation

```bash
# Gemini is excellent at explaining code
gemini chat "Explain this Python code in detail, including potential issues:
[paste code]

Focus on:
- What it does
- How it works
- Potential bugs or performance issues
- Suggestions for improvement"

# Generate documentation
gemini chat "Generate comprehensive documentation for this module:
[paste code]

Include:
- Module overview
- Function/class documentation with examples
- Usage instructions
- Error handling notes
Format as Markdown for README.md"
```

### 4. Multi-Language Support

```bash
# Gemini handles multiple languages well
gemini chat "Convert this Python code to TypeScript, maintaining the same functionality and adding proper TypeScript types:
[paste Python code]"

gemini chat "I have a Python backend using FastAPI and need a TypeScript frontend using React. Generate the API client code that matches these backend endpoints:
[paste FastAPI routes]"
```

## Advanced AIDD Prompting Strategies

### 1. Prompt Chaining for Complex Tasks

Break complex development tasks into a chain of prompts:

```bash
# Step 1: Architecture
claude-code prompt "Design a caching strategy for our API. Ask me questions about usage patterns and requirements."

# Step 2: Implementation Plan
claude-code prompt "Based on the caching strategy, create a detailed implementation plan with file structure and key classes."

# Step 3: Core Implementation
claude-code prompt "Implement the cache manager class according to the plan."

# Step 4: Integration
claude-code prompt "Integrate the cache manager into the existing API routes."

# Step 5: Testing
claude-code prompt "Generate comprehensive tests for the caching system."

# Step 6: Documentation
claude-code prompt "Create documentation for the caching system including architecture diagrams and usage examples."
```

### 2. Test-Driven Prompting

Let AI help you follow TDD:

```bash
# Step 1: Write test cases first
claude-code prompt "I need to implement a user authentication service. First, generate comprehensive pytest test cases that define the expected behavior, including:
- Registration tests
- Login tests  
- Token validation tests
- Error condition tests
Don't implement the service yet, just the tests."

# Step 2: Implement to pass tests
claude-code prompt "Now implement the UserAuthService class that will make all these tests pass."

# Step 3: Refine
claude-code prompt "All tests pass. Now refactor the implementation for better maintainability while keeping tests green."
```

### 3. Progressive Enhancement Prompting

Start simple, add complexity incrementally:

```bash
# Version 1: Basic functionality
gemini chat "Create a simple TODO API with just create and list operations."

# Version 2: Add features
gemini chat "Enhance the TODO API to add update and delete operations."

# Version 3: Add complexity
gemini chat "Add user authentication so each user has their own TODO list."

# Version 4: Add advanced features
gemini chat "Add due dates, priorities, and categories to TODOs."

# Version 5: Optimize
gemini chat "Optimize the TODO API for performance with database indexing and caching."
```

### 4. Error Recovery Prompting

When AI generates incorrect code:

```bash
# Initial attempt
claude-code prompt "Implement JWT token validation middleware for FastAPI."

# If the generated code has issues
claude-code prompt "The middleware you generated has a bug: it's not properly handling expired tokens. Here's the error I'm getting: [paste error]

Fix the token validation logic to properly catch and handle JWT expired exceptions."

# Provide more context if still problematic
claude-code prompt "Still having issues. Here's my complete error traceback: [paste traceback]

And here's how I'm calling the middleware: [paste usage code]

Debug and fix the middleware implementation."
```

### 5. Code Review Prompting

Use AI as a code reviewer:

```bash
claude-code prompt "Review this code I wrote and provide a detailed critique:

[paste code]

Focus on:
1. Code quality and maintainability
2. Performance issues
3. Security vulnerabilities
4. Python best practices violations
5. Missing error handling
6. Insufficient testing

Be harsh and thorough. Rate each aspect from 1-10 and provide specific improvement recommendations."
```

## Common AIDD Prompting Pitfalls and Solutions

### Pitfall 1: Vague Requirements
**Bad:**
```
Make an API for my app
```

**Good:**
```
Create a RESTful API for a task management application with the following requirements:
- User authentication (JWT)
- CRUD operations for tasks
- Task filtering by status and priority
- PostgreSQL database
- FastAPI framework
Include complete implementation with tests.
```

### Pitfall 2: Missing Technical Context
**Bad:**
```
Debug this code [paste code]
```

**Good:**
```
Debug this code:
[paste code]

Context:
- This is part of a FastAPI application
- The error occurs intermittently (20% of requests)
- Error message: "Connection pool exhausted"
- Using SQLAlchemy 2.0 with PostgreSQL
- Deployed on Docker with 4 workers

Current configuration:
- Connection pool size: 10
- Pool timeout: 30 seconds
- Max overflow: 5
```

### Pitfall 3: Ignoring Existing Code Patterns
**Bad:**
```
Add a new API endpoint for user profile
```

**Good:**
```
Add a new API endpoint for user profile following our existing patterns.

Existing route example:
[paste example route showing your patterns]

Existing service example:
[paste example service]

Follow the same structure, naming conventions, and error handling approach.
```

### Pitfall 4: No Validation Criteria
**Bad:**
```
Optimize this function
```

**Good:**
```
Optimize this function:
[paste code]

Current performance: 2.5 seconds average
Target performance: Under 500ms
Constraints:
- Cannot change the function signature (used by 10 other modules)
- Must maintain exact same return value format
- Can use caching if beneficial
- Maximum memory usage: 100MB

Provide optimized code with explanation of improvements and estimated performance gain.
```

### Pitfall 5: Accepting First Output Without Iteration
**Bad Practice:**
```
[Accept whatever AI generates first]
```

**Good Practice:**
```
# First generation
claude-code prompt "Implement user authentication service"

# Review and refine
claude-code prompt "The implementation looks good but needs improvements:
1. Add rate limiting to prevent brute force attacks
2. Implement account lockout after 5 failed attempts  
3. Add logging for security events
4. Improve error messages to be more user-friendly
Update the implementation."

# Validate and test
claude-code prompt "Generate integration tests that verify:
1. Rate limiting works correctly
2. Account lockout triggers appropriately
3. Security events are logged
4. Error messages don't leak sensitive information"
```

## Measuring Prompt Effectiveness in AIDD

How do you know if your prompts are good? Use these metrics:

### 1. First-Time Success Rate
- **Goal**: 70%+ of AI-generated code works on first try
- **Measure**: Track how often you can use AI code without modifications
- **Improve**: Add more context, examples, and constraints to prompts

### 2. Iteration Count
- **Goal**: Average 2-3 iterations to reach production-ready code
- **Measure**: Count prompt-response cycles per feature
- **Improve**: Use question-driven approach earlier in process

### 3. Code Quality Metrics
- **Goal**: AI code passes same quality checks as human code
- **Measure**: Test coverage, linting scores, code review feedback
- **Improve**: Add quality requirements explicitly in prompts

### 4. Time to Completion
- **Goal**: 3-5x faster than manual coding for suitable tasks
- **Measure**: Track time from first prompt to completed, tested feature
- **Improve**: Optimize prompt templates for common tasks

### 5. Maintenance Overhead
- **Goal**: AI-generated code requires minimal future fixes
- **Measure**: Track bugs, refactoring needs in AI code vs manual code
- **Improve**: Emphasize maintainability, documentation, and testing in prompts

## Building Your AIDD Prompt Library

Create reusable prompt templates for common development tasks:

### Template: New API Endpoint
```
Implement a new API endpoint with the following specifications:

**Endpoint Details:**
- HTTP Method: [GET/POST/PUT/DELETE]
- Path: [/api/path]
- Purpose: [what it does]

**Request Schema:**
[Pydantic model or JSON schema]

**Response Schema:**
[Pydantic model or JSON schema]

**Business Logic:**
[step-by-step processing]

**Technical Requirements:**
- Framework: [FastAPI/Flask/Django]
- Database: [PostgreSQL/MySQL/MongoDB]
- Authentication: [required/optional]
- Rate Limiting: [X requests per minute]
- Caching: [yes/no, if yes what strategy]

**Error Handling:**
[list expected errors and how to handle them]

**Testing:**
Generate unit tests covering:
- Happy path with valid inputs
- Edge cases
- Error conditions
- Authentication/authorization checks

Follow existing patterns in [file location].
```

### Template: Bug Fix
```
Debug and fix the following issue:

**Bug Description:**
[what's wrong]

**Error Message/Behavior:**
[exact error or unexpected behavior]

**Code Location:**
[file and function name]

**Reproduction Steps:**
1. [step 1]
2. [step 2]
3. [step 3]

**Current Code:**
[paste relevant code]

**Context:**
- Related files: [list files]
- Recent changes: [what changed recently]
- Environment: [dev/staging/production]
- Frequency: [always/intermittent]

**Expected Behavior:**
[what should happen]

**Constraints:**
- [any constraints on the fix]

Provide:
1. Root cause analysis
2. Fixed code with explanation
3. Test case to prevent regression
```

### Template: Refactoring
```
Refactor the following code for [better performance/maintainability/testability]:

**Current Code:**
[paste code]

**Problems with Current Implementation:**
1. [problem 1]
2. [problem 2]
3. [problem 3]

**Refactoring Goals:**
- [goal 1]
- [goal 2]
- [goal 3]

**Constraints:**
- Must maintain backward compatibility: [yes/no]
- Cannot change: [what can't change]
- Must preserve: [what must stay the same]

**Desired Patterns/Approaches:**
[any specific patterns to use]

Provide:
1. Refactored code
2. Explanation of improvements
3. Migration guide if breaking changes
4. Updated tests
```

## Conclusion: The Future of Development is AI-Augmented

Prompt engineering for AIDD is not about replacing developers—it's about amplifying their capabilities. The best developers in the AI era will be those who:

1. **Master human-AI collaboration** - Know when and how to delegate to AI
2. **Maintain technical fundamentals** - Understand what AI generates and why
3. **Think architecturally** - Guide AI with high-level design, let it handle implementation
4. **Iterate intelligently** - Refine AI output rather than accepting first attempts
5. **Build systematically** - Create prompt templates and workflows for efficiency

As you progress through this book, you'll apply these prompting techniques to learn Python, TypeScript, and build agentic AI applications. The prompting skills you develop now will be your competitive advantage in the AI-driven development era.

**Key Takeaways:**

- **Context is king**: More technical context = better code
- **Be specific**: Precise requirements prevent generic solutions
- **Iterate deliberately**: Use questions to refine before generating
- **Validate everything**: AI generates code fast, but you ensure it's correct
- **Build templates**: Reusable prompts accelerate recurring tasks

In the next chapter, we'll apply these prompting techniques to our first real project: building a complete REST API using Claude Code and Python. You'll see how effective prompting transforms AI from a simple code completion tool into a powerful development partner.

## Practice Exercises

1. **Prompt Refinement Exercise**: Take a vague prompt ("make a login system") and transform it into a complete AIDD prompt using all 8 elements.

2. **Context Building Exercise**: For a feature you need to build, create a comprehensive context document including tech stack, constraints, existing patterns, and requirements.

3. **Question-Driven Development**: Practice the question-driven approach by prompting AI to ask 10 questions about a project before implementation, then refining based on your answers.

4. **Debugging Practice**: Take a real bug you're facing and craft a comprehensive debugging prompt following the template.

5. **Template Creation**: Build 5 prompt templates for your most common development tasks (new feature, bug fix, refactoring, optimization, testing).

## Additional Resources

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Google Gemini Best Practices](https://ai.google.dev/docs/prompt_best_practices)
- [pytest Documentation](https://docs.pytest.org/)

---

