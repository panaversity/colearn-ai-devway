---
sidebar_position: 4
title: "Creating and Using Agent Skills"
---

# Creating and Using Agent Skills

## The Competitive Advantage Hiding in Plain Sight

Skills are your team's reusable intelligence. Claude Code can auto‑detect opportunities to apply that intelligence and can also auto‑delegate to the right subagent when focused execution is needed.

Imagine you're working on a Python project. You've created a `docstring-writer` subagent to add documentation to functions. But in the flow of development, you forget to invoke it. You write five new functions, commit them, and move on. A week later during code review, you realize: no docstrings.

**What if Claude Code could automatically suggest adding docstrings when you write a new function—without you asking?**

**What if your company's domain expertise could be encoded once and then autonomously applied across every project, every developer, every day?**

That's the power of **Agent Skills**. Skills are **discovered and suggested autonomously by Claude Code** when relevant, then executed with your approval. Subagents handle focused, isolated execution; skills continuously inject shared standards and domain expertise.

In this lesson, you'll learn how skills work, create your first skill (a Python docstring generator), and understand why building a skill library is a strategic competitive advantage for teams and companies.

---

## What Are Agent Skills?

**Definition**: An Agent Skill is a modular, discoverable capability that Claude Code can autonomously invoke when working on relevant tasks. Skills are defined by a `SKILL.md` file containing instructions and a **description** that helps Claude decide when to use them.

### Skills vs. Subagents vs. Slash Commands

You've now seen three ways to extend Claude Code. Here's how they differ:

| Feature | Subagent | Agent Skill | Slash Command |
|---------|----------|-------------|---------------|
| **Invocation** | Explicit or auto‑delegated | **Autonomous**: Claude discovers and suggests | Explicit: `/command-name` |
| **Discovery** | Manual—you decide when to run | **Automatic**—Claude decides based on context | Manual—you type the command |
| **Use Case** | Repetitive focused tasks | Domain expertise applied automatically | Predefined workflows |
| **Example** | `claude agent run code-reviewer` | Claude detects Python file, suggests docstrings | `/commit` to create git commit |
| **Competitive Advantage** | Medium (consistency) | **High (scales expertise)** | Low (simple automation) |

**Working together**
- Subagents: isolated context, task ownership (Claude may auto‑delegate)
- Skills: ambient capabilities that refine outputs across phases
> Claude discovers skills from `SKILL.md` descriptions and can delegate to subagents when your task clearly matches their description. See Subagents docs for details.

---

## A Day in the Flow: Zero Extra Prompts

Morning:
- You open a PR to add a new endpoint. Claude suggests security and type‑hint skills. You accept; they run with no extra prompting.
- Claude auto‑delegates to your `test-runner` subagent to run tests in isolated context; failures are summarized back in the main thread.

Afternoon:
- While refactoring, skills suggest docstrings and complexity checks; you accept inline.
- For a performance report, Claude delegates to a `profiler` subagent; skills annotate the findings (clarity, pedagogy, compliance) before summarizing.

Outcome: predictable execution in clean contexts (subagents) + continuously applied standards and domain expertise (skills) without added cognitive load.

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
- Clear trigger: when should Claude suggest this skill?
- Outcome: what does the skill produce?
- Scope and boundaries: what it will and will not do

**2. Skill Instructions**:
- Checklist of steps to follow
- Quality bar: what good output looks like
- Edge cases and constraints to respect

**3. Examples** (optional):
- Brief before/after descriptions (no code required)

### Discovery Process

Here's how Claude Code decides to use a skill:

1. Context analysis: current task, open artifacts, recent conversation
2. Skill scanning: available skills’ discoverable descriptions
3. Relevance matching: which skills match the context
4. Suggestion: propose applying relevant skills
5. Approval: accept or skip
6. Execution: follow the skill’s instructions and report back

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

## Quick Start: Add One Skill, See It Work

Goal: add a project skill that explains runtime errors.

Ask Claude:
```
Create a project skill named "error-explainer" that, when a Python error occurs, identifies the error type, explains the cause in simple terms, and proposes a minimal fix. Store it in .claude/skills/.
```

Then trigger an error in your code as usual. Claude will suggest the skill when relevant and summarize the fix—no extra prompting.

---

## ✓ Your Skill Is Working When:

**Quick check**:

1. **Skill is created** - Skill directory exists
2. **Skill is discovered** - When relevant, Claude suggests using it
3. **Explanations are helpful** - You understand what went wrong and how to fix it
4. **It saves you time** - You don't have to google the error—Claude explains it immediately

**If this works**: 🎉 **Your collaborative skill is ready! Claude now automatically helps you understand errors as you encounter them.**

---

## How Skills Work

Skills are **collaborative helpers that Claude discovers automatically**. Unlike subagents (which you explicitly invoke), skills work in the background.

When Claude notices you need help (errors, missing docs, missing types, security checks), it suggests your skill.

**Key point**: Skills should complement your development workflow, not add complexity. Start simple.

---

## What's Next: Lesson 5 - MCP and Workflows

You've learned how to extend Claude Code internally with subagents and skills. But what if you need Claude Code to access **external systems**?

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
