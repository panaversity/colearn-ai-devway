---
sidebar_position: 3
title: "Lesson 3: Understanding and Using Subagents"
duration: "25-32 min"
---

# Lesson 3: Understanding and Using Subagents

## The Problem: Context Pollution and Specialization

You've installed Claude Code and run your first commands. But as you use it more, you'll encounter a common challenge: **context pollution**.

Imagine this scenario: You're working on a Python project. You ask Claude Code to help debug a function, then to review your code for style issues, then to generate documentation, then to suggest performance optimizations. By the time you're on your fifth request, Claude Code's context includes all your previous conversations—debugging details, style discussions, documentation drafts. The conversation has become cluttered.

**What if you could press "reset" without losing your work?**

**What if you could have specialized AI assistants for different tasks—a code reviewer, a documentation writer, a debugging expert—each with clear focus and isolated context?**

That's what **subagents** enable. They're one of Claude Code's most powerful features, yet often overlooked by beginners who stick to the main conversation for everything.

In this lesson, you'll learn what subagents are, when to use them, and how to create your first custom subagent—a code reviewer that applies your team's specific standards.

---

## What Are Subagents?

**Definition**: A subagent is a specialized instance of Claude within Claude Code, configured with custom instructions (called a "system prompt") and isolated context separate from the main conversation.

Think of subagents as specialized team members:

- **Main Claude Code**: Your general assistant—handles one-off questions, exploratory tasks, varied workflows
- **Subagent 1 (Code Reviewer)**: Focused solely on reviewing code for bugs, style, and best practices
- **Subagent 2 (Test Writer)**: Specialized in generating unit tests for functions
- **Subagent 3 (Documentation Generator)**: Expert at writing clear, comprehensive documentation

Each subagent has:
1. **Custom system prompt**: Instructions that define its role, constraints, and expertise
2. **Isolated context**: Conversations in this subagent don't affect the main conversation or other subagents
3. **Tool access configuration**: You can limit which tools (file read/write, command execution) the subagent can use

### Subagents vs. Main Conversation: When to Use Each

| Aspect | Main Conversation | Subagent |
|--------|-------------------|----------|
| **Use Case** | Exploratory work, varied tasks, one-off questions | Repetitive specialized tasks with clear scope |
| **Context** | Accumulates all conversation history | Isolated—only sees subagent's own history |
| **Customization** | General-purpose Claude behavior | Custom system prompt defines specific role |
| **When to Use** | "Help me understand this error" | "Review this code using our team's style guide" |
| **Examples** | Debugging, learning concepts, exploring codebases | Code reviews, test generation, refactoring, documentation |

**Key Insight**: Use subagents when you have **repeatable tasks with clear instructions**. Use the main conversation when you need flexibility and exploration.

---

## Why Subagents Matter: Three Key Benefits

### Benefit 1: Context Preservation

**Problem Without Subagents**: After 10 interactions in the main conversation, Claude Code's context is filled with unrelated discussions. Asking for a code review now means Claude considers all previous context—even if irrelevant.

**Solution With Subagents**: Launch a fresh subagent for each focused task. The code review happens in a clean context, without clutter from previous debugging or documentation work.

### Benefit 2: Specialization and Consistency

**Problem Without Subagents**: You must repeatedly tell Claude Code your code review standards, testing framework preferences, or documentation style with every new session.

**Solution With Subagents**: Encode these instructions once in a subagent's system prompt. Every time you invoke the "code-reviewer" subagent, it already knows your standards.

**Example System Prompt for Code Reviewer**:
```
You are a code reviewer specializing in Python.
Apply these standards:
- PEP 8 style compliance
- Type hints required for all functions
- Docstrings required (Google style)
- Prefer list comprehensions over loops where readable
- Flag any security concerns (SQL injection, hardcoded secrets)
- Suggest performance improvements for O(n²) or worse complexity
```

Every code review from this subagent applies these standards consistently.

### Benefit 3: Reusability Across Projects

**Problem Without Subagents**: You manually recreate your preferred workflows for each new project.

**Solution With Subagents**: Subagents are stored as files in `.claude/agents/`. You can:
- Share subagents with your team via version control
- Reuse the same subagent across multiple projects
- Build a library of specialized assistants

A well-designed subagent becomes **organizational knowledge**—capturing expertise that benefits your entire team.

---

## Subagent Architecture: How They Work

Let's peek under the hood to understand how subagents function.

### File Structure

When you create a subagent named `code-reviewer`, Claude Code stores it as:

```
.claude/
└── agents/
    └── code-reviewer/
        ├── agent.json          # Configuration (tools, model)
        └── SYSTEM_PROMPT.md    # Custom instructions
```

**agent.json** (configuration):
```json
{
  "name": "code-reviewer",
  "description": "Reviews code for bugs, style, and best practices",
  "tools": ["read", "grep", "glob"],
  "model": "claude-sonnet-4"
}
```

**SYSTEM_PROMPT.md** (custom instructions):
```markdown
You are a code reviewer specializing in Python.

Apply these standards:
- PEP 8 style compliance
- Type hints required for all functions
- Docstrings required (Google style)
- Flag security concerns

Provide:
1. Summary of issues found
2. Specific line numbers and suggestions
3. Positive feedback on good practices
```

### Subagent Lifecycle

1. **Creation**: You define the subagent with `claude agent create <name>`
2. **Invocation**: You run the subagent with `claude agent run <name> "<task>"`
3. **Execution**: The subagent processes the task in isolated context
4. **Completion**: Results return; context is preserved for next invocation
5. **Management**: You can list, edit, or delete subagents with `claude agent` commands

---

## Hands-On Tutorial: Creating Your First Subagent

Let's create a **code-reviewer subagent** that applies Python best practices.

### Step 1: Create the Subagent

In your terminal, run:

```bash
claude agent create code-reviewer
```

**Expected output**:
```
✓ Subagent 'code-reviewer' created
✓ Files created:
  - .claude/agents/code-reviewer/agent.json
  - .claude/agents/code-reviewer/SYSTEM_PROMPT.md

Edit SYSTEM_PROMPT.md to customize instructions.
```

### Step 2: Customize the System Prompt

Open `.claude/agents/code-reviewer/SYSTEM_PROMPT.md` in your text editor:

```bash
# Windows
notepad .claude\agents\code-reviewer\SYSTEM_PROMPT.md

# macOS/Linux
nano .claude/agents/code-reviewer/SYSTEM_PROMPT.md
```

Replace the default content with:

```markdown
# Code Reviewer System Prompt

You are a Python code reviewer with expertise in software engineering best practices.

## Your Role
- Review code for bugs, style issues, and improvements
- Provide constructive, specific feedback
- Balance critique with encouragement

## Standards to Apply

### Style
- PEP 8 compliance (line length, naming conventions)
- Type hints for function parameters and return values
- Google-style docstrings for all functions and classes

### Quality
- No hardcoded values—use constants or configuration
- Error handling for edge cases
- Security concerns (SQL injection, secrets in code)

### Performance
- Flag O(n²) or worse complexity
- Suggest better data structures where applicable

## Output Format

Provide feedback in this structure:

1. **Summary**: One-sentence overall assessment
2. **Critical Issues**: Bugs or security concerns (if any)
3. **Style Issues**: PEP 8 or documentation problems
4. **Suggestions**: Performance or readability improvements
5. **Positive Notes**: What the code does well

Always include line numbers and specific examples.
```

Save and close the file.

### Step 3: Configure Subagent Tools (Optional)

Edit `.claude/agents/code-reviewer/agent.json`:

```json
{
  "name": "code-reviewer",
  "description": "Reviews Python code for bugs, style, and best practices",
  "tools": ["read", "grep", "glob"],
  "model": "claude-sonnet-4"
}
```

**What this configuration does**:
- **tools**: Limits the subagent to reading files, searching code, and finding files—no write or execute permissions (safer for automated reviews)
- **model**: Uses Claude Sonnet (balance of speed and capability)

### Step 4: Test Your Subagent

Create a sample Python file to review:

```bash
cat > sample.py << 'EOF'
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item["price"]
    return total

result = calculate_total([{"price": 10}, {"price": 20}])
print(result)
EOF
```

**This code has intentional issues**:
- No type hints
- No docstring
- No error handling
- O(n) loop could be simplified with `sum()`

Now run the code-reviewer subagent:

```bash
claude agent run code-reviewer "Review sample.py for bugs and style issues"
```

**Expected output** (example):

```
🔍 Code Review: sample.py

1. Summary
Code is functional but lacks documentation, type hints, and error handling.

2. Critical Issues
- No validation for 'items' parameter (line 1)
  What if items is None or contains non-dict elements?

3. Style Issues
- Missing type hints (line 1)
  Should be: def calculate_total(items: list[dict]) -> float:
- Missing docstring (line 1)
  Add description of function purpose and parameters

4. Suggestions
- Use sum() with generator expression (more Pythonic):
  return sum(item["price"] for item in items)
- Add error handling for KeyError if "price" key missing

5. Positive Notes
- Clear variable names ('total', 'items')
- Straightforward logic, easy to understand

Recommended next steps:
1. Add type hints and docstring
2. Validate input parameter
3. Refactor loop to use sum()
```

**If the review appears**: ✅ Your subagent works! It's applying the standards you defined in the system prompt.

---

## When to Use Subagents: Practical Scenarios

Here are five common scenarios where subagents provide value:

### Scenario 1: Code Reviews

**Setup**: Create a `code-reviewer` subagent with your team's style guide
**Invocation**: `claude agent run code-reviewer "Review src/utils.py"`
**Benefit**: Consistent reviews applying team standards every time

### Scenario 2: Test Generation

**Setup**: Create a `test-writer` subagent specialized in your testing framework (pytest, unittest, etc.)
**Invocation**: `claude agent run test-writer "Generate tests for src/auth.py"`
**Benefit**: Tests follow project conventions without explaining them each time

### Scenario 3: Documentation Writing

**Setup**: Create a `doc-writer` subagent that generates API documentation in your preferred format
**Invocation**: `claude agent run doc-writer "Document all functions in api/routes.py"`
**Benefit**: Consistent documentation style across the codebase

### Scenario 4: Refactoring Assistant

**Setup**: Create a `refactor-helper` subagent focused on code simplification and pattern recognition
**Invocation**: `claude agent run refactor-helper "Suggest refactorings for src/legacy.py"`
**Benefit**: Non-destructive suggestions without changing unrelated code

### Scenario 5: Security Auditor

**Setup**: Create a `security-auditor` subagent that scans for common vulnerabilities
**Invocation**: `claude agent run security-auditor "Check src/ for security issues"`
**Benefit**: Systematic security checks using OWASP or CWE standards

---

## Managing Subagents: Essential Commands

Once you've created multiple subagents, you'll need to manage them.

### List All Subagents

```bash
claude agent list
```

**Output**:
```
Available subagents:
  - code-reviewer       (Reviews Python code)
  - test-writer         (Generates unit tests)
  - doc-writer          (Creates API documentation)
```

### View Subagent Details

```bash
claude agent show code-reviewer
```

**Output**: Displays the subagent's configuration and system prompt.

### Edit a Subagent

```bash
claude agent edit code-reviewer
```

**What this does**: Opens the system prompt in your default editor for modifications.

### Delete a Subagent

```bash
claude agent delete test-writer
```

**Warning**: This permanently removes the subagent files. Use with caution.

---

## Exercise: Create Your Own Subagent

Now it's your turn to apply what you've learned.

**Exercise: Build a "Bug Hunter" Subagent**

**Goal**: Create a subagent that specializes in finding common bugs in Python code.

**Requirements**:
1. Name it `bug-hunter`
2. Configure it to only use `read`, `grep`, and `glob` tools (no write access)
3. Write a system prompt that instructs it to look for:
   - Off-by-one errors in loops
   - Unhandled exceptions
   - None checks missing
   - Division by zero risks
   - Mutable default arguments

**Steps**:
1. Create the subagent: `claude agent create bug-hunter`
2. Edit the system prompt with the requirements above
3. Test it on a sample file with intentional bugs

**💡 Learning with AI**: As you build this, if you're unsure how to write an effective system prompt, ask Claude Code:
- "What are common bug patterns to check for in Python?"
- "How should I structure a system prompt for a bug-finding subagent?"
- "Can you review my system prompt and suggest improvements?"

Use AI as a learning mentor to understand system prompt best practices, not just to generate the solution.

<details>
<summary>Show Example Solution</summary>

**System Prompt** (`.claude/agents/bug-hunter/SYSTEM_PROMPT.md`):

```markdown
# Bug Hunter System Prompt

You are a bug detection specialist for Python code.

## Your Mission
Scan code for common bug patterns and potential runtime errors.

## Bug Patterns to Detect

1. **Off-by-one errors**
   - Loop ranges that should be `range(len(x))` but use `range(len(x)-1)` or `range(len(x)+1)`
   - List indexing that may exceed bounds

2. **Unhandled exceptions**
   - File operations without try/except
   - Network calls without error handling
   - Type conversions (int(), float()) without validation

3. **None checks missing**
   - Functions that may return None but callers don't check
   - Optional parameters used without validation

4. **Division by zero risks**
   - Any division operation where denominator could be zero
   - Suggest adding checks: `if denominator != 0:`

5. **Mutable default arguments**
   - Functions with `def func(items=[]):` instead of `def func(items=None):`

## Output Format

List findings with:
- **Severity**: Critical / Warning / Info
- **Line number** and code snippet
- **Explanation** of why it's a bug
- **Suggested fix**

Focus on actionable, specific findings—not theoretical issues.
```

**Test File** (`buggy_code.py`):

```python
def process_items(items=[]):  # Bug: mutable default
    items.append("new")
    return items

def divide_values(a, b):  # Bug: no zero check
    return a / b

def read_config():  # Bug: no error handling
    with open("config.txt") as f:
        return f.read()

result = divide_values(10, 0)  # Runtime error!
```

**Test Command**:
```bash
claude agent run bug-hunter "Scan buggy_code.py for potential bugs"
```

**Expected Output**:
- Identifies mutable default argument
- Flags missing zero check in `divide_values`
- Warns about missing error handling in `read_config`
- Suggests specific fixes for each

</details>

---

## Subagent Best Practices

**1. Keep System Prompts Focused**
- One clear responsibility per subagent
- Avoid combining unrelated tasks (e.g., "review code AND generate docs")

**2. Use Descriptive Names**
- ✅ `python-code-reviewer`, `pytest-test-generator`
- ❌ `helper`, `tool1`, `bob`

**3. Limit Tool Access Appropriately**
- Read-only subagents for analysis tasks
- Full access only when necessary (e.g., refactoring subagents)

**4. Version Control Your Subagents**
- Commit `.claude/agents/` to Git
- Share effective subagents with your team
- Document what each subagent does in a team README

**5. Iterate and Improve**
- After using a subagent, refine its system prompt
- Add examples of good/bad outputs to guide behavior
- Collect feedback from team members

---

## Pause and Reflect: Specialization vs. Flexibility

You've learned how to create specialized AI assistants with subagents. But there's a tradeoff to consider:

**Specialization** provides consistency and focus, but reduces flexibility. A code-reviewer subagent won't help you debug runtime errors or generate documentation—that's by design.

**The main conversation** is flexible and exploratory, but lacks the focused instructions and clean context that subagents provide.

**Reflection Questions**:
- Think about your own development workflow. What repetitive tasks could benefit from a specialized subagent?
- When would you prefer the flexibility of the main conversation over a focused subagent?
- If you work on a team, what subagents could capture and share your team's unique expertise?

---

## What's Next: Lesson 4 - Agent Skills

Subagents are powerful because you explicitly invoke them: `claude agent run code-reviewer`. But what if Claude Code could **discover and invoke specialized capabilities autonomously**?

That's what **Agent Skills** enable—modular capabilities that Claude Code discovers and uses without you explicitly calling them.

In Lesson 4, you'll:
- Learn the difference between subagents (explicit invocation) and skills (autonomous discovery)
- Create your first Agent Skill with a discoverable description
- Understand how to build a skill library that gives you competitive advantage
- See how skills scale expertise across teams and projects

**The key insight**: Skills turn your domain expertise into reusable, discoverable AI capabilities that amplify over time.

Let's explore this powerful feature.

---

## Key Takeaways

- **Subagents are specialized Claude instances** with custom instructions and isolated context
- **Use subagents for repetitive, focused tasks** where you need consistency (code reviews, test generation, documentation)
- **Use main conversation for exploration** and varied tasks where flexibility matters
- **Three key benefits**: Context preservation, specialization, and reusability
- **Subagents are files** stored in `.claude/agents/` that can be versioned and shared
- **System prompts define behavior**: Clear instructions create consistent, valuable assistants
- **Manage subagents** with `claude agent list/create/edit/delete/run` commands
- **Best practice**: One responsibility per subagent, descriptive names, appropriate tool access

---

**Up Next**: [Lesson 4 - Creating and Using Agent Skills](./04-agent-skills.md)
