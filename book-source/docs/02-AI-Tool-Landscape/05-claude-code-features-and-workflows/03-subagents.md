---
sidebar_position: 3
title: "Understanding and Using Subagents"
---

# Understanding and Using Subagents

## The Problem: Context Pollution and Specialization

You've installed Claude Code and run your first commands. But as you use it more, you'll encounter a common challenge: **context pollution**.

Imagine this scenario: You're working on a Python project. You ask Claude Code to help debug a function, then to review your code for style issues, then to generate documentation, then to suggest performance optimizations. By the time you're on your fifth request, Claude Code's context includes all your previous conversations—debugging details, style discussions, documentation drafts. The conversation has become cluttered.

**What if you could press "reset" without losing your work?**

**What if you could have specialized AI assistants for different tasks—a code reviewer, a documentation writer, a debugging expert—each with clear focus and isolated context?**

That's what **subagents** enable. They're one of Claude Code's most powerful features, yet often overlooked by beginners who stick to the main conversation for everything.

In this lesson, you'll learn what subagents are, when to use them, and how to create your first custom subagent—a code reviewer that applies your team's specific standards.

---

## What Are Subagents?

**Definition**: A subagent is a specialized task-specific agent for improved context management. They are configured with custom instructions (called a "system prompt") and isolated context separate from the main conversation.

Think of subagents as specialized team members:

- **Main Claude Code**: Your general assistant—handles one-off questions, exploratory tasks, varied workflows. It will manage the subagents as well.
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
    └── code-reviewer.md    # Custom instructions
```


**code-reviewer.md** (custom instructions):
```markdown
---
name: chapter-planner
description: You are a code reviewer specializing in Python.
model: haiku
color: blue
---

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

1. **Creation**: You ask Claude Code to create a subagent in conversation. Run /agents command select Create Agent and share your idea about sub agent. (e.g., "Create a subagent called explain-my-code that...")
2. **Storage**: Claude Code ask the location project vs user level. After selection it creates files in `.claude/agents/<your_subagent_name>.md`
3. **Invocation**: You ask Claude Code to use the subagent naturally (e.g., "Use the explain-my-code subagent to explain this code")
4. **Execution**: The subagent processes the task in isolated context
5. **Completion**: Results return; context is preserved for next invocation
6. **Management**: Subagents are stored as files in `.claude/agents/` that you can view, edit, or delete

---

## Hands-On Tutorial: Creating Your First Subagent

Let's create an **"explain-my-code" subagent**—a collaborative partner that helps you understand what your code does.

This is simpler than a code reviewer and directly supports the "learning WITH AI" philosophy.

### Step 1: Create the Subagent

Start Claude Code in your project directory:

```bash
claude
```

Then ask Claude to create the subagent:

1. Use slash command to create a new agent: ```/agents```
2. Select `Create new agent`. 
3. Choose location -> Project
4. Generate with Claude (recommended) 
5. Descibe your idea:

```
Create a subagent called "explain-my-code" with this description:
"A collaborative partner that explains what code does in simple, conversational terms.
Breaks down complex parts, points out confusing sections, and suggests clearer ways
to write code. Perfect for learning and code review."

Keep the explanation helpful and beginner-friendly, not academic.
```

Claude will create the subagent files automatically in `.claude/agents/explain-my-code/`.

**Expected result**: Claude confirms the subagent has been created and saved to your project.

### Step 2: Test Your Subagent

Ask claude 

Create a sample Python file called `example.py` with:
```python
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item["price"]
    return total

result = calculate_total([{"price": 10}, {"price": 20}])
print(result)
```

Now ask Claude to use the subagent:

```
Use the explain-my-code subagent to explain what example.py does
```

Or ask more naturally:

```
Have the explain-my-code subagent break down example.py for me
```

Claude will invoke the subagent, which analyzes the file and explains it in simple terms.

**What you might hear back**:
> "This function adds up prices from a list of items. It starts with `total = 0`, then loops through each item, adds its price to the total, and finally returns the sum. The test code at the bottom calls the function with two items ($10 and $20) and prints the result (30)."

**If your subagent explains the code**: ✅ It works! Now you have a collaborative partner to help you understand your own code.

---

## ✓ Your Subagent Is Working When:

**Quick verification**:

1. **Subagent is created** - You can list it
2. **Subagent can be invoked** - You can ask it to explain code
3. **It returns helpful explanations** - The response makes sense and helps clarify the code
4. **It stays in character** - Multiple invocations maintain the "collaborative explainer" role

**If this works**: 🎉 **Your collaborative helper is ready! You now have a dedicated partner to help you understand code.**

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

**4. Iterate and Improve**
- After using a subagent, refine its system prompt
- Add examples of good/bad outputs to guide behavior
- Collect feedback from team members

---

## Pause and Reflect: Specialization vs. Flexibility

You've learned how to create specialized AI assistants with subagents. But there's a tradeoff to consider:

**Specialization** provides consistency and focus, but reduces flexibility. A code-reviewer subagent won't help you debug runtime errors or generate documentation—that's by design.

**The main conversation** is flexible and exploratory, but lacks the focused instructions and clean context that subagents provide.

**Reflection Questions**:
- Think about your own daily workflow. What repetitive tasks could benefit from a specialized subagent?
- When would you prefer the flexibility of the main conversation over a focused subagent?
- If you work on a team, what subagents could capture and share your team's unique expertise?

---

## What's Next: Lesson 4 - Agent Skills

Subagents are powerful because you run in isolation - what if Claude Code could **discover and invoke specialized capabilities autonomously**?

That's what **Agent Skills** enable—modular capabilities that Claude Code discovers and uses without explicitly invoking subagent in isolated context. 

In Lesson 4, you'll:
- Learn the difference between subagents (isolated context invocation) and skills (autonomous discovery)
- Create your first Agent Skill with a discoverable description
- Understand how to build a skill library that gives you competitive advantage
- See how skills scale expertise across teams and projects

**The key insight**: Skills turn your domain expertise into reusable, discoverable AI capabilities that amplify over time. Let's explore this powerful feature.