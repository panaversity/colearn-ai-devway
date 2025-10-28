# Skill: Planning — Creating Detailed Chapter Specifications

**Version:** 1.0.0 | **Alignment:** Constitution v2.0.0, Principle 1 (Spec-Kit Methodology)

---

## Overview

Planning is the foundational skill for chapter creation in CoLearning Python. This skill teaches how to transform source material, requirements, and pedagogical goals into detailed, testable specifications that guide all subsequent content creation.

**Core Principle:** Specification-Driven Development (SDD) — clear, testable specifications precede all work.

**When to Use:** Every chapter creation starts with planning. Use this skill when:
- Starting a new chapter
- Refining requirements from source material
- Translating learning objectives into content structure
- Creating AI prompts for chapter writers and lesson writers

---

## The Planning Mindset

### Shift from "Let's Write" to "Let's Specify"

**Traditional Approach:**
> "Write a chapter about Python functions. Include some examples."

**SDD Approach (This Skill):**
> "Specify what readers must know about functions by the end of the chapter. What are the learning objectives? What are minimum and maximum code examples? What mistakes will we address? How does this connect to prior chapters?"

### Why Planning First?

1. **Clarity:** Clear specifications enable AI to generate consistent, targeted content
2. **Quality:** If the spec is clear, the content will be good
3. **Iteration:** Specifications are easier and faster to iterate on than full content
4. **Accountability:** Specifications define what success looks like
5. **Collaboration:** Human and AI align on requirements BEFORE generation starts

---

## The Planning Process (SDD Loop)

```
Source Material / Requirements
    ↓
1. Analyze & Extract
2. Define Learning Objectives
3. Map Prerequisites & Dependencies
4. Structure Content Outline
5. Specify Code Examples
6. Write Acceptance Criteria
    ↓
Specification Document (specs/part-X/chapter-Y-spec.md)
    ↓
Human Review & Iteration
    ↓
Approved Specification
    ↓
(Next phase: Chapter-Writer agent uses this spec)
```

### Stage 1: Analyze & Extract

**Goal:** Deeply understand the source material and learning context.

**Questions to Answer:**
- What is the topic? (Be specific)
- What is the core problem this chapter solves?
- Who are the learners and what do they know already?
- What prior chapters are required?
- What chapters depend on this one?
- What real-world scenarios use these concepts?

**Artifacts:**
- 1-2 paragraph summary of the topic
- List of prerequisite chapters with brief justification
- List of chapters that depend on this one
- Real-world use case or application

**Example (Planning Chapter 20: Type Hints):**
> Topic: Type hints as documentation and verification tools in Python 3.13+
>
> Prerequisites: Ch 19 (functions basics), Ch 17-18 (prompt engineering for understanding)
>
> Depends on: Ch 21-23 (data structures and OOP require type hints)
>
> Real-world: Professional Python code requires type hints for IDE support, error detection, and team collaboration

---

### Stage 2: Define Learning Objectives

**Goal:** Create specific, measurable, learner-centered outcomes.

**Requirements:**
- 3-5 objectives per chapter (not too many)
- Each objective must be testable/verifiable
- Use action verbs (understand, implement, debug, optimize)
- Match Constitution Principle 5 (Progressive Complexity)
- Include cognitive levels (Bloom's taxonomy suggested)

**Format:**
```
By the end of this chapter, learners will be able to:
1. [Verb] [Concept] [Context]
2. [Verb] [Concept] [Context]
3. [Verb] [Concept] [Context]
4. [Verb] [Concept] [Context]
5. [Verb] [Concept] [Context]
```

**Good Examples:**
- ✅ "Write type hints for functions with multiple parameters and return types"
- ✅ "Debug type errors using mypy --strict error messages"
- ✅ "Choose between Generic types and concrete types for different use cases"

**Poor Examples:**
- ❌ "Understand type hints" (too vague, not testable)
- ❌ "Learn about Python" (too broad)
- ❌ "Know what type hints are" (passive, not action-oriented)

---

### Stage 3: Map Prerequisites & Dependencies

**Goal:** Ensure learning progression and identify prerequisite knowledge.

**Explicit Prerequisites:**
- List chapters that MUST be completed before this chapter
- For each prerequisite, note what specific knowledge is required
- Identify knowledge that will be briefly reviewed vs. deeply assumed

**Forward Dependencies:**
- List chapters that depend on concepts taught here
- Note what specific skills/knowledge will be assumed

**Content Bridges:**
- If a prerequisite concept is taught far earlier, plan a brief review
- Example: "Ch 20 (Type Hints) assumes knowledge of functions from Ch 19, which we'll briefly review in the Introduction"

**Example (Chapter 22: Functions, Decorators, and Type Checking):**
```
Explicit Prerequisites:
- Ch 19 (Python functions basic syntax)
- Ch 20 (Type hints fundamentals)
- Ch 3 (Working with AI assistants - for AI Exercise)
- Ch 15-16 (Prompt engineering - for effective AI interaction)

Forward Dependencies:
- Ch 23-26 all assume decorator and type checking competence
- Ch 25 (Testing) depends on understanding function signatures

Knowledge Review Needed:
- Brief review of function parameters vs arguments
- Brief review of basic type hint syntax from Ch 20
```

---

### Stage 4: Structure Content Outline

**Goal:** Create a high-level roadmap of what the chapter teaches.

**Requirements:**
- 2-3 major sections (teaching focus areas)
- Each section should cover ONE primary concept
- Follow Constitution Principle 9 (Show-Then-Explain)
- Include required sections: Common Mistakes, AI Exercise, Summary

**Mandatory Chapter Structure:**
```
1. Introduction (hook + context)
2. [Core Topic 1] → Show-Then-Explain pattern
3. [Core Topic 2] → Show-Then-Explain pattern
4. [Core Topic 3] (optional)
5. Common Mistakes (2-3 misconceptions + fixes)
6. AI Exercise (hands-on practice)
7. Summary (recap + key points)
8. What's Next (preview of next chapter)
9. Additional Resources (links, docs)
```

**Example Outline (Chapter 20: Type Hints):**
```
1. Introduction (why type hints matter in modern Python)
2. Basic Type Hints → Show-Then-Explain
   - Annotating function parameters
   - Annotating return types
   - Using modern syntax (str | None not Optional[str])
3. Generic Types → Show-Then-Explain
   - list[str], dict[str, int] patterns
   - When to use generics vs concrete types
4. Type Checking with mypy → Show-Then-Explain
   - Running mypy --strict
   - Interpreting error messages
5. Common Mistakes
   - Forgetting return type annotations
   - Using old-style type hints
   - Incorrect generic syntax
6. AI Exercise (write type hints with AI assistance)
7. Summary
8. What's Next (OOP with type hints in Ch 21)
9. Resources (mypy docs, PEP 484, etc.)
```

---

### Stage 5: Specify Code Examples

**Goal:** Define exactly what code examples the chapter needs.

**Requirements (per Constitution Principle 3):**
- Minimum: 3 code examples per chapter
- Maximum: 8 code examples per chapter
- ALL code must be tested and working
- ALL code must have type hints
- ALL code must include docstrings (Google style)
- ALL code must pass: python3.13, mypy --strict, black --check
- Each example shows both the AI prompt and the generated code

**For Each Code Example, Specify:**
1. **Purpose** — What concept does this demonstrate?
2. **Complexity** — Simple, moderate, advanced?
3. **Context** — Real-world scenario or learning example?
4. **AI Interaction** — Show the prompt used to generate or refine it
5. **Expected Output** — Document what the code produces
6. **Why This Code** — Pedagogical value and connection to learning objectives

**Example Specification (Chapter 20 Code Examples):**
```
Example 1: Basic Function Type Hints
Purpose: Demonstrate simple type annotations on parameters and return
Complexity: Simple (appropriate for Ch 20)
Context: A calculator function
AI Prompt: "Write a type-hinted add function that takes two numbers and returns their sum"
Expected Output: Function definition with type hints, docstring, and example usage comment
Why: Shows minimum viable type hints for a simple function

Example 2: Generic List Type Hint
Purpose: Show how to annotate functions working with collections
Complexity: Moderate
Context: Filter function working with lists
AI Prompt: "Write a type-hinted filter_positive function that takes a list of integers and returns a filtered list"
Expected Output: Function with list[int] parameter and return type
Why: Bridges from simple types to generic types; common pattern in real code

Example 3: Union Type and Error Handling
Purpose: Show optional/union types in realistic scenarios
Complexity: Moderate-Advanced
Context: User lookup function that might return None
AI Prompt: "Write a type-hinted get_user function that takes a user_id and returns either user data or None"
Expected Output: Function using str | None return type, proper error handling
Why: Real-world pattern; shows mypy can catch missing None checks
```

---

### Stage 6: Write Acceptance Criteria

**Goal:** Define how to verify the chapter meets the specification.

**Acceptance Criteria Format:**
```
The chapter meets this specification when:
- [ ] All learning objectives are explicitly addressed
- [ ] Every major concept has at least one code example
- [ ] Code examples follow code-example.md output style
- [ ] Chapter follows docusaurus-chapter.md structure exactly
- [ ] Common Mistakes section addresses learner misconceptions
- [ ] AI Exercise has clear success criteria and reflects learning objectives
- [ ] Voice and tone match technical-writing.md skill guidelines
- [ ] All cross-references to prior/future chapters are accurate
- [ ] Readability target: Flesch Reading Ease 60-70
- [ ] No forward references without explanation (follow Constitution rule)
- [ ] Human reviewer approves before moving to Chapter-Writer stage
```

**Additional Verification Criteria:**
```
✅ Code Quality Checks (Code-Validator will verify):
- [ ] All code runs without errors (python3.13 <file>)
- [ ] All code passes type checking (mypy --strict)
- [ ] All code passes style check (black --check)
- [ ] Type hints on every function (zero exceptions)

✅ Technical Accuracy Checks (Technical-Reviewer will verify):
- [ ] All Python 3.13+ features are current
- [ ] No deprecated patterns used
- [ ] Best practices demonstrated
- [ ] External links are live
- [ ] Accessibility standards met

✅ Pedagogical Checks (Human Reviewer will verify):
- [ ] Show-Then-Explain pattern is clear (show code first)
- [ ] Complexity progression matches chapter difficulty level
- [ ] No assumptions about learner background (gatekeeping language eliminated)
- [ ] "Common Mistakes" are realistic and address common confusion
- [ ] "AI Exercise" is achievable with provided tools and knowledge
```

---

## Specification Document Template

Use this template when creating specs/part-X/chapter-Y-spec.md:

```markdown
---
chapter: Y
part: X
title: [Chapter Title]
created: YYYY-MM-DD
author: [Name or AI Agent]
status: draft/ready-for-review/approved
---

## 1. Topic Summary

[1-2 paragraph overview of the chapter topic]

## 2. Prerequisites

### Explicit Prerequisites
- [Chapter N]: [What specific knowledge is required]
- [Chapter N]: [What specific knowledge is required]

### Knowledge That Will Be Reviewed
- [Concept]: [Brief review will be included]

### Forward Dependencies
- [Chapter N+X]: [Will assume this knowledge]

## 3. Learning Objectives

By the end of this chapter, learners will be able to:
1. [Verb] [Concept] [Context]
2. [Verb] [Concept] [Context]
3. [Verb] [Concept] [Context]
4. [Verb] [Concept] [Context]
5. [Verb] [Concept] [Context]

## 4. Content Outline

### Introduction
[Hook, context, real-world relevance]

### Section 1: [Core Topic 1]
[High-level what will be taught]

### Section 2: [Core Topic 2]
[High-level what will be taught]

### Section 3: [Core Topic 3] (optional)
[High-level what will be taught]

### Common Mistakes (2-3 misconceptions)
[Patterns learners typically struggle with]

### AI Exercise
[Hands-on practice scenario and success criteria]

### Summary & Next Steps
[What's learned, what's coming next]

## 5. Code Examples

### Example 1: [Title]
- **Purpose:** [What concept demonstrated]
- **Complexity:** [Simple/Moderate/Advanced]
- **Real-world scenario:** [Context]
- **AI Prompt:** [The prompt used to generate this]
- **Expected output:** [What the code produces]
- **Why included:** [Pedagogical value]

### Example 2: [Title]
[Repeat structure above]

### Example 3: [Title]
[Repeat structure above]

## 6. Acceptance Criteria

The chapter meets this specification when:
- [ ] All learning objectives explicitly addressed
- [ ] Code examples follow code-example.md style
- [ ] Chapter structure matches docusaurus-chapter.md exactly
- [ ] Common Mistakes section realistic and useful
- [ ] AI Exercise is achievable and aligned with learning objectives
- [ ] Technical accuracy verified
- [ ] No deprecated patterns used
- [ ] Readability 60-70 Flesch Reading Ease
- [ ] No gatekeeping language
- [ ] Cross-references accurate

## 7. Notes for Chapter Writer

[Any special considerations, common pitfalls, tone preferences, etc.]
```

---

## Tips for Effective Planning

### ✅ Do This

1. **Be Specific:** "Write type hints for every function parameter" not "cover type hints"
2. **Prioritize Clarity:** Would a beginner understand this objective?
3. **Connect to Prior Chapters:** "Building on Ch 19 (functions), we'll now..."
4. **Show the Path:** Make prerequisites explicit so no surprises later
5. **Include Real Scenarios:** Why does this matter in real Python development?
6. **Specify Complexity:** "This is Simple/Moderate/Advanced for chapter 20 students"
7. **Define Done:** What exactly does "complete" look like?
8. **Iterate Collaboratively:** Discuss specs with human reviewers before content generation

### ❌ Don't Do This

1. **Be Vague:** "Teach functions and stuff" (too broad)
2. **Assume Knowledge:** "Obviously, you know what a type is" (gatekeeping)
3. **Forget Context:** "Here are 5 code examples" (without pedagogical purpose)
4. **Plan Too Much Detail:** Specs are high-level; let writers add detail
5. **Ignore Prerequisites:** Leaving readers confused about what they should know
6. **Skip Acceptance Criteria:** No way to know when chapter is "done"
7. **Write in Isolation:** Specifications benefit from collaboration and review

---

## Common Pitfalls & How to Avoid Them

### Pitfall 1: Specifications Too Detailed
**Problem:** "Write 3 paragraphs about functions, then 2 paragraphs about..."
**Better:** "Section 1 introduces function basics using Show-Then-Explain pattern"

### Pitfall 2: Forgetting AI Partnership
**Problem:** Specification assumes human will write entire chapter manually
**Better:** "Planner creates spec → Chapter-Writer uses spec + skills → Lesson-Writer implements → Code-Validator tests"

### Pitfall 3: Unclear Prerequisites
**Problem:** "Ch 20 assumes knowledge from Ch 1-19 somewhere"
**Better:** "Ch 20 explicitly requires: Ch 3 (basic syntax), Ch 19 (functions), Ch 15-16 (prompt engineering)"

### Pitfall 4: No Real-World Context
**Problem:** "Teach exception handling because it's in the curriculum"
**Better:** "Exception handling is essential for reliable code; professional projects require it. Real scenario: API calls can fail, and we must handle gracefully"

### Pitfall 5: Code Examples Without Purpose
**Problem:** "Include code examples" (but unclear why each one exists)
**Better:** "Example 1 (Simple): shows basic syntax. Example 2 (Real): shows professional pattern. Example 3 (Common): shows common mistake"

---

## When Planning is Done (Handoff Criteria)

The specification is ready to hand off to **Chapter-Writer** when:

✅ **Content Quality**
- [ ] 2-3 core topics clearly defined
- [ ] Learning objectives are specific and testable
- [ ] Prerequisites and dependencies are explicit
- [ ] Common mistakes identified
- [ ] AI Exercise scenario is clear and achievable

✅ **Structure**
- [ ] Follows mandatory chapter outline
- [ ] Show-Then-Explain pattern planned for each section
- [ ] Code examples specified (count, purpose, complexity)
- [ ] Acceptance criteria are measurable

✅ **Governance**
- [ ] Aligns with Constitution Principles 1, 5, 9
- [ ] No deprecated patterns mentioned
- [ ] Accessibility and inclusivity considered
- [ ] Real-world relevance established

✅ **Collaboration**
- [ ] Human reviewer has reviewed and approved
- [ ] Any ambiguities clarified
- [ ] Special considerations documented for Chapter-Writer

---

## Related Infrastructure

- **Constitution v2.0.0:** Governance principles that planning embodies
- **output-styles/docusaurus-chapter.md:** The exact structure chapter must follow
- **skills/pedagogy.md:** Teaching methodologies that guide planning
- **sub-agents/planner:** The AI agent that executes this skill
- **sub-agents/chapter-writer:** Uses completed specification
- **specs/part-X/chapter-Y-spec.md:** Output document from planning process

---

**Planning is the foundation. Better specs → better chapters → better learning outcomes.**
