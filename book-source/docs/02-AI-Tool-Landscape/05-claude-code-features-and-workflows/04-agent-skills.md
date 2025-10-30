---
sidebar_position: 4
title: "Lesson 4: Creating and Using Agent Skills"
duration: "32-39 min"
---

# Lesson 4: Creating and Using Agent Skills

## The Competitive Advantage Hiding in Plain Sight

You've learned about subagents—specialized assistants you explicitly invoke for focused tasks. But here's a challenge: **you have to remember to use them.**

Imagine you're working on a Python project. You've created a `docstring-writer` subagent to add documentation to functions. But in the flow of development, you forget to invoke it. You write five new functions, commit them, and move on. A week later during code review, you realize: no docstrings.

**What if Claude Code could automatically suggest adding docstrings when you write a new function—without you asking?**

**What if your company's domain expertise could be encoded once and then autonomously applied across every project, every developer, every day?**

That's the power of **Agent Skills**. Unlike subagents (which require explicit invocation), skills are **discovered and invoked autonomously by Claude Code** when relevant to your task.

In this lesson, you'll learn how skills work, create your first skill (a Python docstring generator), and understand why building a skill library is a strategic competitive advantage for teams and companies.

---

## What Are Agent Skills?

**Definition**: An Agent Skill is a modular, discoverable capability that Claude Code can autonomously invoke when working on relevant tasks. Skills are defined by a `SKILL.md` file containing instructions and a **description** that helps Claude decide when to use them.

### Skills vs. Subagents vs. Slash Commands

You've now seen three ways to extend Claude Code. Here's how they differ:

| Feature | Subagent | Agent Skill | Slash Command |
|---------|----------|-------------|---------------|
| **Invocation** | Explicit: `claude agent run <name>` | **Autonomous**: Claude discovers and uses | Explicit: `/command-name` |
| **Discovery** | Manual—you decide when to run | **Automatic**—Claude decides based on context | Manual—you type the command |
| **Use Case** | Repetitive focused tasks | Domain expertise applied automatically | Predefined workflows |
| **Example** | `claude agent run code-reviewer` | Claude detects Python file, suggests docstrings | `/commit` to create git commit |
| **Competitive Advantage** | Medium (consistency) | **High (scales expertise)** | Low (simple automation) |

**Key Distinction**: With subagents and commands, **you** decide when to use them. With skills, **Claude** decides when they're relevant and suggests using them.

---

## Why Agent Skills Matter: The Strategic Value

Agent Skills aren't just a technical feature—they're a **strategic business advantage**. Here's why:

### 1. Expertise That Scales Automatically

**Without Skills**:
- Senior developer explains best practices to junior developer
- Junior developer forgets 60% within a week
- Process repeats for every new hire
- Knowledge stays locked in people's heads

**With Skills**:
- Senior developer encodes expertise once as a skill
- Claude Code applies it automatically across all projects
- Every developer benefits immediately
- Knowledge captured permanently in version control

**Example**: A security expert creates an `sql-injection-checker` skill. Now every developer—regardless of security expertise—gets automatic alerts when writing database queries that might be vulnerable.

### 2. Consistent Standards Without Enforcement Overhead

**Without Skills**:
- Team agrees on coding standards (docstrings, type hints, naming conventions)
- Code reviews catch violations manually
- Inconsistency creeps in over time
- Engineers spend hours enforcing standards

**With Skills**:
- Standards encoded as skills (e.g., `enforce-type-hints`, `docstring-generator`)
- Claude Code automatically applies them
- Standards maintained consistently without manual enforcement
- Engineers focus on logic, not style policing

### 3. Competitive Differentiation Through Domain Expertise

This is where skills become truly powerful: **Your unique domain knowledge becomes an automated advantage.**

**Example 1**: A fintech company builds a `compliance-checker` skill that validates financial calculations against regulatory requirements. Their developers ship compliant code faster than competitors who review regulations manually.

**Example 2**: A healthcare startup creates a `hipaa-privacy-auditor` skill that scans code for potential PHI (Protected Health Information) leaks. Their code is secure by default; competitors discover privacy issues in production.

**Example 3**: A machine learning team builds a `model-reproducibility-checker` skill that ensures experiments log hyperparameters and random seeds. Their models are reproducible; competitors waste weeks debugging non-deterministic results.

**The pattern**: Domain expertise encoded as skills compounds over time, creating organizational capabilities that competitors can't easily replicate.

---

## How Agent Skills Work: The Discovery Mechanism

Let's understand the magic behind autonomous discovery.

### Skill Anatomy: The SKILL.md File

Every skill is defined by a `SKILL.md` file with three critical sections:

**1. Discoverable Description** (most important):
```markdown
---
name: python-docstring-writer
description: |
  Use this skill when working with Python functions that lack docstrings.
  Automatically generates Google-style docstrings with parameter descriptions,
  return types, and usage examples. Invoke when creating or editing Python
  functions without documentation.
allowed-tools: [read, write, edit]
---
```

**2. Skill Instructions**:
```markdown
# Python Docstring Writer Skill

When invoked, analyze the target Python function and generate a comprehensive
Google-style docstring that includes:

- Brief one-line summary
- Detailed description (if function is complex)
- Args section with type hints and descriptions
- Returns section with type and description
- Raises section (if function throws exceptions)
- Example usage (if helpful)

Format:
(Provide docstring format example)

Apply PEP 257 conventions for docstring placement and style.
```

**3. Examples** (optional but recommended):
```markdown
## Example

Input function:
(code example without docstring)

Output:
(same function with generated docstring)
```

### Discovery Process

Here's how Claude Code decides to use a skill:

1. **Context Analysis**: Claude reads your current task, open files, and conversation history
2. **Skill Scanning**: Claude scans available skills' descriptions
3. **Relevance Matching**: Claude evaluates which skills match the current context
4. **Autonomous Invocation**: If a skill is highly relevant, Claude suggests using it: *"I notice you're writing Python functions. Should I use the python-docstring-writer skill to add documentation?"*
5. **User Approval**: You approve (or skip) the suggestion
6. **Skill Execution**: Claude follows the skill's instructions

**Key Insight**: The **description** is what makes skills discoverable. A vague description means Claude won't know when to use the skill. A specific, context-rich description enables autonomous discovery.

---

## Skill Scopes: Where Skills Live

Skills can exist at three levels:

**1. Personal Skills** (`~/.claude/skills/`)
- Your personal toolkit
- Not shared with projects or team
- Use for personal workflow preferences

**2. Project Skills** (`.claude/skills/` in project directory)
- Specific to one project
- Committed to version control
- Team members inherit when they clone the repo
- **Most common for team collaboration**

**3. Plugin Skills** (installed from skill registry)
- Publicly available skills
- Installed with `claude skill install <name>`
- Maintained by community or vendors

**Best Practice**: Use **project skills** for team standards and domain expertise. This ensures everyone on the team benefits from shared knowledge.

---

## Hands-On Tutorial: Creating a Python Docstring Writer Skill

Let's build a practical skill that adds Google-style docstrings to Python functions.

### Step 1: Create the Skill Directory

In your project directory, run:

```bash
mkdir -p .claude/skills/python-docstring-writer
```

### Step 2: Create the SKILL.md File

Create `.claude/skills/python-docstring-writer/SKILL.md`:

```bash
# macOS/Linux
nano .claude/skills/python-docstring-writer/SKILL.md

# Windows
notepad .claude\skills\python-docstring-writer\SKILL.md
```

### Step 3: Define the Skill

Paste the following content:

```markdown
---
name: python-docstring-writer
description: |
  Use this skill when working with Python functions or methods that lack docstrings.
  The skill generates comprehensive Google-style docstrings with parameter descriptions,
  return types, exception documentation, and usage examples. Invoke automatically when:
  - Creating new Python functions without docstrings
  - Editing existing functions that lack documentation
  - User mentions "add docs" or "document this function"
  - Reviewing code that fails documentation linting
allowed-tools: [read, edit, grep]
---

# Python Docstring Writer

## Purpose
Generate high-quality, comprehensive docstrings for Python functions and methods following Google style guide conventions.

## When to Use
- Python function/method lacks a docstring
- Existing docstring is incomplete or outdated
- User explicitly requests documentation
- Code review identifies missing documentation

## Instructions

### 1. Analyze the Function
Read the function signature and body to understand:
- Purpose and behavior
- Parameters (types, descriptions)
- Return value (type, meaning)
- Exceptions raised
- Side effects or state changes

### 2. Generate Docstring
Create a Google-style docstring with these sections:

**Required**:
- Brief one-line summary
- Args section (for functions with parameters)
- Returns section (if function returns a value)

**Optional** (include if applicable):
- Detailed description paragraph (for complex functions)
- Raises section (if function throws exceptions)
- Example section (for non-obvious usage)
- Note/Warning (for important caveats)

### 3. Format Standards

```python
def function_name(param1: type1, param2: type2) -> return_type:
    """Brief one-line summary ending with period.

    Optional detailed description providing context, explaining
    non-obvious behavior, or clarifying usage patterns.

    Args:
        param1: Description of param1, including valid values
            and constraints. Use indentation for multi-line descriptions.
        param2: Description of param2.

    Returns:
        Description of return value, including type information
        and meaning.

    Raises:
        ValueError: When param1 is negative.
        TypeError: When param2 is not a string.

    Example:
        >>> result = function_name(10, "test")
        >>> print(result)
        Expected output

    Note:
        Important implementation detail or usage caveat.
    """
```

### 4. Best Practices
- Start with a verb ("Calculate", "Return", "Generate", etc.)
- Keep summary under 80 characters
- Be specific: "Calculate the average of positive integers" not "Do math"
- Include type information even if type hints exist
- Provide examples for non-obvious usage
- Document side effects explicitly

## Example

### Input (function without docstring):

```python
def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
```

### Output (with generated docstring):

```python
def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a percentage discount.

    Takes an original price and discount percentage, validates the discount
    is within acceptable range (0-100), and returns the discounted price.

    Args:
        price: Original price in dollars before discount. Must be positive.
        discount_percent: Discount percentage to apply. Must be between 0
            and 100 inclusive.

    Returns:
        Final price in dollars after discount is applied. Will be equal to
        or less than the original price.

    Raises:
        ValueError: If discount_percent is negative or greater than 100.

    Example:
        >>> calculate_discount(100, 20)
        80.0
        >>> calculate_discount(50, 10)
        45.0
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
```

## Output Format
Provide the complete updated function with the docstring inserted immediately after the function signature, maintaining proper indentation.
```

Save and close the file.

### Step 4: Test the Skill

Create a test Python file with an undocumented function:

```bash
cat > test_function.py << 'EOF'
def validate_email(email):
    if '@' not in email:
        raise ValueError("Invalid email format")
    local, domain = email.split('@')
    if not local or not domain:
        raise ValueError("Email missing local or domain part")
    return True
EOF
```

Now ask Claude Code to work with this file:

```bash
claude "Review test_function.py and improve it"
```

**Expected Behavior**: Claude Code should:
1. Read the file and notice the function lacks a docstring
2. Discover the `python-docstring-writer` skill is relevant
3. Suggest: *"I notice this function lacks documentation. Should I use the python-docstring-writer skill to add a comprehensive docstring?"*
4. Upon your approval, generate and add a Google-style docstring

**If Claude discovers and suggests the skill**: ✅ Your skill is working! The description enabled autonomous discovery.

**If Claude doesn't suggest the skill**: Check:
- Is the `SKILL.md` file in the correct location? (`.claude/skills/python-docstring-writer/SKILL.md`)
- Is the YAML frontmatter properly formatted?
- Try being more explicit: `claude "Add docstrings using the python-docstring-writer skill"`

---

## Writing Effective Skill Descriptions: Best Practices

The **description** field determines whether Claude discovers your skill. Here's how to write effective descriptions:

### ❌ Bad Description (Vague, Won't Be Discovered)

```yaml
description: "Helps with Python docs"
```

**Why it fails**: Too vague. Claude can't determine when this is relevant.

### ✅ Good Description (Specific, Discoverable)

```yaml
description: |
  Use this skill when working with Python functions that lack docstrings.
  Automatically generates Google-style docstrings with parameter descriptions,
  return types, and usage examples. Invoke when creating or editing Python
  functions without documentation.
```

**Why it works**:
- Specific trigger: "Python functions that lack docstrings"
- Clear outcome: "generates Google-style docstrings"
- Action words: "creating or editing"

### Description Formula

Use this template for effective skill descriptions:

```
Use this skill when [SPECIFIC CONTEXT/TRIGGER].
[WHAT THE SKILL DOES] with [KEY FEATURES/BENEFITS].
Invoke when [LIST OF SCENARIOS WHERE IT APPLIES].
```

**Examples**:

**Security Auditor Skill**:
```yaml
description: |
  Use this skill when reviewing code that handles user input, database queries,
  or authentication. Scans for common security vulnerabilities (SQL injection,
  XSS, hardcoded secrets, weak crypto) and suggests fixes. Invoke when reviewing
  pull requests, writing new API endpoints, or handling sensitive data.
```

**Test Generator Skill**:
```yaml
description: |
  Use this skill when functions or classes lack unit tests. Generates pytest
  test cases covering happy path, edge cases, and error conditions. Invoke when
  completing feature implementation, before code review, or when test coverage
  drops below threshold.
```

**API Documentation Skill**:
```yaml
description: |
  Use this skill when REST API endpoints lack OpenAPI/Swagger documentation.
  Generates complete API docs with request/response examples, parameter
  descriptions, and status codes. Invoke when adding new endpoints or updating
  existing API routes.
```

---

## Building a Skill Library: Strategic Recommendations

For teams serious about leveraging skills for competitive advantage:

### 1. Start with High-Frequency Pain Points

**Identify**: What tasks does your team repeatedly spend time on?
- Code reviews finding the same issues
- Boilerplate that's tedious to write
- Standards that are inconsistently applied

**Encode**: Create skills that automate these tasks.

**Examples**:
- `enforce-type-hints` → Ensures all functions have type annotations
- `database-migration-generator` → Creates migration files from model changes
- `error-handling-wrapper` → Adds try/except blocks with logging

### 2. Capture Expert Knowledge

**Identify**: What domain expertise do your senior engineers have?
- Security best practices
- Performance optimization patterns
- Domain-specific business rules

**Encode**: Turn their expertise into skills that apply automatically.

**Examples**:
- `fintech-compliance-checker` → Validates calculations meet financial regulations
- `ml-reproducibility-enforcer` → Ensures experiments log hyperparameters
- `accessibility-auditor` → Checks UI code for WCAG compliance

### 3. Make Skills Discoverable and Maintainable

**Naming Convention**: Use descriptive, domain-specific names
- ✅ `python-pytest-test-generator`
- ❌ `test-helper`

**Documentation**: Include README.md in skill directory explaining:
- What the skill does
- When to use it
- Who maintains it
- How to contribute improvements

**Version Control**: Commit skills to your repo
```bash
git add .claude/skills/
git commit -m "Add python-docstring-writer skill"
```

**Team Onboarding**: Add a section to your team handbook:
*"We use Claude Code skills to automate expertise. Here's our skill library and what each does..."*

### 4. Iterate Based on Usage

**Track**: Which skills are invoked most frequently?
**Refine**: Improve descriptions and instructions based on how well they work
**Expand**: Build new skills based on team feedback and emerging needs

---

## Exercise: Create a Domain-Specific Skill

Now it's your turn to apply what you've learned.

**Exercise: Build a Skill for Your Domain**

**Goal**: Create a skill that captures expertise from your field (or learning area).

**Options** (choose one):

1. **Data Science**: `data-validation-checker` — Validates datasets for missing values, outliers, type consistency
2. **Web Development**: `responsive-design-auditor` — Checks if UI components have mobile-friendly breakpoints
3. **Backend**: `api-error-handler` — Ensures API endpoints return consistent error response formats
4. **DevOps**: `dockerfile-optimizer` — Suggests improvements for Docker images (layer caching, security, size)

**Requirements**:
1. Create the skill in `.claude/skills/[skill-name]/SKILL.md`
2. Write a specific, discoverable description (use the formula above)
3. Define clear instructions for what the skill should check or generate
4. Include at least one example showing input and expected output
5. Test the skill by creating a relevant file and asking Claude to review it

**💡 Learning with AI**:
- Ask Claude Code: *"What are common issues in [your domain] that could be automated with a skill?"*
- Request feedback: *"Review my skill description—will Claude be able to discover it effectively?"*
- Iterate: *"Based on this test case, how should I improve my skill's instructions?"*

Use Claude Code as a mentor to learn effective skill design, not just to complete the exercise.

---

## Skill Management Commands

As your skill library grows, you'll need to manage skills effectively.

### List Available Skills

```bash
claude skill list
```

**Output**:
```
Available skills:
Personal (.config/claude/skills/):
  - personal-notes-formatter

Project (.claude/skills/):
  - python-docstring-writer
  - sql-injection-checker
  - pytest-test-generator

Plugins:
  (none installed)
```

### Show Skill Details

```bash
claude skill show python-docstring-writer
```

**Output**: Displays the full SKILL.md content and metadata.

### Test Skill Discovery

```bash
claude skill test python-docstring-writer --context "Python function without docstring"
```

**Output**: Shows whether Claude would discover this skill in the given context (useful for debugging descriptions).

### Disable a Skill Temporarily

```bash
claude skill disable sql-injection-checker
```

**Use case**: Temporarily disable a skill that's being invoked too aggressively while you refine it.

---

## Pause and Reflect: Your Competitive Edge

You've learned a powerful concept: **domain expertise encoded as skills compounds over time.**

A single senior developer can encode their knowledge once, and that expertise automatically applies across:
- Every developer on the team
- Every project in the organization
- Every line of code written going forward

This is fundamentally different from traditional knowledge transfer (documentation, training, mentorship), which:
- Requires active learning effort
- Fades over time
- Doesn't scale to entire codebases automatically

**Reflection Questions**:
- What unique expertise does your team or company have that could be encoded as skills?
- If you're learning programming, what skills could accelerate your learning? (e.g., `explain-error-messages`, `suggest-better-variable-names`)
- How would your development workflow change if common mistakes were caught automatically?

---

## What's Next: Lesson 5 - MCP and Workflows

You've learned how to extend Claude Code internally with subagents and skills. But what if you need Claude Code to access **external systems**—databases, APIs, monitoring tools, or third-party services?

That's where **Model Context Protocol (MCP)** comes in. MCP allows Claude Code to connect to external data sources and tools, dramatically expanding its capabilities.

In Lesson 5, you'll:
- Learn what MCP is and how it works
- Connect Claude Code to a GitHub MCP server
- See complete workflows combining files, commands, and external integrations
- **Understand security considerations** for evaluating third-party MCP servers
- Explore four common real-world workflows

**The final piece**: Combining everything you've learned—installation, subagents, skills, and MCP—into powerful, integrated development workflows.

Let's complete your Claude Code mastery.

---

## Key Takeaways

- **Agent Skills are autonomously discovered** by Claude Code based on context and descriptions
- **Skills vs. Subagents**: Skills are auto-invoked; subagents require explicit commands
- **Strategic value**: Skills scale expertise, enforce standards consistently, and create competitive advantages
- **Discovery mechanism**: Well-written descriptions determine whether Claude finds and suggests skills
- **Description formula**: "Use when [context]. Does [action] with [features]. Invoke when [scenarios]."
- **Skill scopes**: Personal (~/.claude), Project (.claude), or Plugin (installed)
- **Competitive advantage**: Domain expertise encoded as skills compounds over time
- **Best practices**: Start with frequent pain points, capture expert knowledge, version control skills
- **Management**: List, show, test, and disable skills with `claude skill` commands

---

**Up Next**: [Lesson 5 - Connecting MCP Servers and Common Workflows](./05-mcp-servers-and-workflows.md)
