---
sidebar_position: 4
title: "Creating and Using Agent Skills"
---

# Creating and Using Agent Skills

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

## Hands-On Tutorial: Creating a Simple Skill

Let's build a practical skill that helps you understand error messages—your **"error explainer" skill**.

When you get a Python error, Claude automatically explains what went wrong and how to fix it.

### Step 1: Create the Skill

Start Claude Code in your project directory:

```bash
claude
```

Then ask Claude to create the skill:

```
Create a skill called "error-explainer" for my project. https://docs.claude.com/en/docs/claude-code/skills

Description: "When a Python error occurs, identifies the error type and explains what caused it in simple, friendly terms. Provides a corrected code example and shows how to fix the problem."

Instructions:
- Identify what type of error it is (ValueError, KeyError, IndexError, etc.)
- Explain what caused it in simple, non-technical terms
- Show how to fix it with a concrete example
- Provide corrected code that works
- Keep explanations friendly and conversational

Store this in .claude/skills/ so it's available to the whole project.
```

Claude will create the skill files automatically in `.claude/skills/error-explainer/`.

**Expected result**: Claude confirms the skill has been created and saved to your project.

### Step 2: Test Your Skill

Create a Python file with an intentional error:

```python
# error_example.py
my_list = [1, 2, 3]
print(my_list[10])  # IndexError!
```

Now ask Claude to run it and help:

```
Run error_example.py and help me understand what went wrong
```

**What happens**:
Claude Code will:
1. Run the script and see the IndexError
2. Recognize your error-explainer skill applies
3. Automatically explain the error using your skill

**What you might see**:
> "You got an IndexError because you tried to access index 10, but your list only has 3 items (indices 0, 1, 2). Python counts from zero, so the last valid index is 2. To fix this, either check the list length first with `if index < len(my_list)` or use a try/except block."

**Key difference from subagents**: You don't explicitly invoke your skill. Claude **automatically discovers it** based on the error context and applies it. This is the power of skills—they work in the background, applied when relevant.

---

## ✓ Your Skill Is Working When:

**Quick check**:

1. **Skill is created** - Skill directory exists
2. **Skill is discovered** - When you have an error, Claude suggests using it
3. **Explanations are helpful** - You understand what went wrong and how to fix it
4. **It saves you time** - You don't have to google the error—Claude explains it immediately

**If this works**: 🎉 **Your collaborative skill is ready! Claude now automatically helps you understand errors as you encounter them.**

---

## How Skills Work

Skills are **collaborative helpers that Claude discovers automatically**. Unlike subagents (which you explicitly invoke), skills work in the background.

When Claude notices you need help (confused by an error, writing undocumented code, etc.), it suggests your skill.

**Key point**: Skills should complement your development workflow, not add complexity. Start simple.

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
