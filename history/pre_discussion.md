# Concrete Implementation Plan: Essential Infrastructure

**Created:** October 28, 2025  
**Approach:** Focused and Practical (Based on Research Paper)

---

## The Loop (Confirmed)

```
constitution.md (governs all)
     ↓
specs/pre-setup.md (book outline, structure, skills taxonomy)
     ↓
specs/part-XX/chapter-YY-spec.md (individual chapter specification)
     ↓
chapter-writer sub-agent (uses output-styles + skills)
     ↓
code-validator sub-agent (tests all code)
     ↓
technical-reviewer sub-agent (verifies accuracy)
     ↓
human (final approval & editorial polish)
     ↓
published chapter in book-site/history/
```

---

## Skills & Sub-Agents: Final Architecture

### Skills Being Pre-Created (4 Total)

These are **shared guidance frameworks** used by both humans and AI agents to ensure consistency.

1. **planning.md** — How to analyze source material and create chapter specs
   - Used by: Planner sub-agent (+ humans iterating)
   - Guides: Systematic specification creation from research/content

2. **technical-writing.md** — Voice, tone, readability standards
   - Used by: Chapter-Writer, Lesson-Writer (+ humans iterating)
   - Guides: Consistent voice and style across all 26 chapters

3. **pedagogy.md** — Teaching methodologies and patterns
   - Used by: Chapter-Writer, Lesson-Writer (+ humans iterating)
   - Guides: Show-then-explain, progressive complexity, mistake-driven learning

4. **ai-collaboration.md** — Responsible AI usage and verification
   - Used by: Lesson-Writer, in AI Exercise sections
   - Guides: When/how to use AI, verification patterns, ethical use

**Key Point:** Skills are **shared guidance frameworks** that inform both humans and AI.

---

### Output Styles Being Pre-Created (4 Total)

These define exact formatting for different content types—used consistently across all chapters.

1. **docusaurus-chapter.md** — Overall chapter structure and frontmatter format
2. **lesson.md** — Individual lesson section formatting (show-then-explain structure)
3. **code-example.md** — Python code formatting (type hints, docstrings, testing)
4. **exercise.md** — AI Exercise formatting (scenario, prompt, reflection questions)

---

### Sub-Agents Being Pre-Created (5 Total)

These are **executable collaborative agents** that work WITH humans (not FOR humans) within the SDD loop.

1. **planner.md** — Creates detailed chapter specifications
   - Input: Source material + pre-setup.md outline
   - Process: Analyzes material → extracts learning objectives → maps dependencies → creates detailed spec
   - Output: specs/part-X/chapter-Y-spec.md
   - Handoff: Humans iterate on spec until ready → chapter-writer

2. **chapter-writer.md** — Creates chapter outline and learning structure
   - Input: Detailed chapter spec + skills
   - Process: Reads spec → creates outline → structures learning objectives → plans sections
   - Output: Chapter outline with structure
   - Handoff: Humans iterate on outline → lesson-writer

3. **lesson-writer.md** — Implements actual lesson content
   - Input: Chapter outline + lesson.md output style + skills
   - Process: Writes lesson sections (show-then-explain) → creates code examples → designs AI exercise
   - Output: Complete chapter content (markdown with all sections)
   - Handoff: Passes to code-validator

4. **code-validator.md** — Tests all Python code
   - Input: Chapter content from lesson-writer
   - Process: Extracts code → runs tests → checks mypy/black → validates style
   - Output: Validation report + fixed code
   - Handoff: If all pass → technical-reviewer; if fail → back to lesson-writer

5. **technical-reviewer.md** — Verifies technical accuracy
   - Input: Code-validated chapter
   - Process: Fact-checks claims → reviews best practices → verifies explanations → checks tool versions
   - Output: Technical review report
   - Handoff: If approved → human; if revisions needed → back to lesson-writer

**Key Point:** Sub-agents are **collaborative orchestrators** in an iterative SDD loop, not one-way generators.

---

## Essential Files Only (Minimum Viable Infrastructure)

Based on the research paper's framework and SDD methodology, we need exactly **14 infrastructure files**:

### Foundation (2 files) ✅ 1/2 Complete
1. ✅ `constitution.md` - DONE (Comprehensive governance document)
2. ⏳ `specs/pre-setup.md` - Book structure, outline, skills taxonomy

### Output Styles (4 files) - "WHAT it looks like"
3. ⏳ `.claude/output-styles/docusaurus-chapter.md` — Chapter structure + frontmatter
4. ⏳ `.claude/output-styles/lesson.md` — Individual lesson section formatting
5. ⏳ `.claude/output-styles/code-example.md` — Python code formatting
6. ⏳ `.claude/output-styles/exercise.md` — AI Exercise formatting

### Skills (4 files) - "HOW to do it well"
7. ⏳ `.claude/skills/planning.md` — How to create specifications
8. ⏳ `.claude/skills/technical-writing.md` — Voice and tone standards
9. ⏳ `.claude/skills/pedagogy.md` — Teaching methodologies
10. ⏳ `.claude/skills/ai-collaboration.md` — Responsible AI usage

### Sub-Agents (5 files) - "WHO does WHAT and HOW"
11. ⏳ `.claude/sub-agents/planner.md` — Creates detailed chapter specifications
12. ⏳ `.claude/sub-agents/chapter-writer.md` — Creates chapter outline and structure
13. ⏳ `.claude/sub-agents/lesson-writer.md` — Implements lesson content
14. ⏳ `.claude/sub-agents/code-validator.md` — Tests all code
15. ⏳ `.claude/sub-agents/technical-reviewer.md` — Verifies accuracy

**Total: 15 files to complete infrastructure**

---

## File-by-File Breakdown

### 1. Pre-Setup Specification ⏳

**File:** `specs/pre-setup.md`

**Purpose:** Master specification before any chapter work

**Contents:**
```markdown
# Pre-Setup Specification

## 1. Book Structure (5 Parts, 26 Chapters)

### Part 1: Introducing AI-Driven Development (5 chapters)
Ch 1: The Paradigm Shift
Ch 2: Setting Up Your Environment  
Ch 3: Your First Python Program with AI
Ch 4: The Human-AI Partnership Model
Ch 5: When AI Helps and When It Hurts

### Part 2: Spec-Kit Methodology (5 chapters)
Ch 6: Introduction to Specification-Driven Development
Ch 7: Writing Effective Constitutions
Ch 8: Creating Detailed Specifications
Ch 9: From Specification to Implementation
Ch 10: Iterative Refinement with Spec-Kit

### Part 3: AI Tool Landscape (4 chapters)
Ch 11: Claude Code - Native Abstractions
Ch 12: Gemini CLI - Conversational AI
Ch 13: OpenAI Codex & AGENTS.md
Ch 14: Zed, Cursor & IDE-Integrated AI

### Part 4: Prompt & Context Engineering (4 chapters)
Ch 15: The Anatomy of Effective Prompts
Ch 16: Context Window Management
Ch 17: Clarity of Thought → Clarity of Code
Ch 18: Debugging AI Outputs

### Part 5: Modern Python with Type Hints (8 chapters)
Ch 19: Python 3.13 - Modern Features Overview
Ch 20: Type Hints - Types as Documentation
Ch 21: Data Structures with Type Safety
Ch 22: Functions, Decorators, and Type Checking
Ch 23: Object-Oriented Python with Protocols
Ch 24: Pattern Matching and Structural Types
Ch 25: Testing and Validation
Ch 26: Building Your Portfolio Project

## 2. Skills Taxonomy

[Complete skills map: which skills taught when]

## 3. Chapter Dependencies

[Prerequisite chain]

## 4. Tool Coverage Plan

[When each tool (Claude Code, Gemini CLI, Codex, etc.) is introduced]
```

**Size:** ~800 lines  
**Time:** 2-3 hours

---

### 2. Docusaurus Chapter Output Style ⏳

**File:** `.claude/output-styles/docusaurus-chapter.md`

**Purpose:** Define exact format for every chapter

**Core Contents:**

```markdown
# Output Style: Docusaurus Chapter

## 1. YAML Frontmatter (Required)

Every chapter MUST start with:

```yaml
---
chapter_number: 1
part_number: 1
title: "Chapter Title"
description: "120-160 char description"
keywords: [python, ai, keyword3, keyword4]

skills_introduced:
  - skill_name: "Skill Name"
    level: "beginner"
    description: "What this skill is"

skills_practiced: [...]
skills_mastered: [...]

python_version: "3.13+"
required_tools: [...]
prerequisites:
  chapters: []
  skills: []

reading_time: "20 minutes"
practice_time: "40 minutes"
difficulty: "beginner"

sidebar_position: 1
---
```

## 2. Required Sections (Exact Order)

1. Title (H1) - auto from frontmatter
2. 🎯 Learning Objectives (H2)
3. 📖 Introduction (H2)
4. [Core Section 1] (H2)
5. [Core Section 2] (H2)
6. [Core Section 3] (H2)
7. ⚠️ Common Mistakes (H2)
8. 🤖 AI Exercise (H2)
9. 📝 Summary (H2)
10. 🚀 Next Steps (H2)
11. 📚 Additional Resources (H2)

## 3. Formatting Rules

### Code Blocks
```python title="filename.py" showLineNumbers
# Code with title and line numbers
```

### Admonitions
:::tip Pro Tip
For best practices
:::

:::note Remember
For key concepts
:::

:::caution Watch Out
For common pitfalls
:::

### Word Count
Target: 2,000-2,500 words
Minimum: 1,800 words
Maximum: 2,800 words

[Complete template with placeholders]
```

**Size:** ~600 lines  
**Time:** 2 hours

---

### 3. Code Example Output Style ⏳

**File:** `.claude/output-styles/code-example.md`

**Purpose:** Format for all Python code

**Core Contents:**

```markdown
# Output Style: Python Code Example

## Required Structure

```python
"""Module docstring if needed."""

from typing import Optional  # Type imports

def function_name(
    param1: str,
    param2: int = 0
) -> dict[str, int]:  # Python 3.13+ generic syntax
    """One-line summary.
    
    Detailed explanation.
    
    Args:
        param1: Description
        param2: Description with default
        
    Returns:
        Return value description
        
    Raises:
        ValueError: When/why
        
    Example:
        >>> function_name("test", 5)
        {'result': 5}
    """
    if not param1:
        raise ValueError("param1 required")
    
    # WHY comment: Explain reasoning
    result: dict[str, int] = {"result": len(param1) * param2}
    return result


if __name__ == "__main__":
    # Usage example
    output = function_name("hello", 2)
    print(output)
    # Output: {'result': 10}
```

## Validation Requirements

Before publication, ALL code must:
- [ ] Run without errors in Python 3.13
- [ ] Pass `mypy --strict`
- [ ] Pass `black --check`
- [ ] Include type hints on ALL functions
- [ ] Have Google-style docstrings
- [ ] Show usage example with output

[Complete style guide]
```

**Size:** ~400 lines  
**Time:** 1.5 hours

---

### 4. Exercise Output Style ⏳

**File:** `.claude/output-styles/exercise.md`

**Purpose:** Format for AI exercises

**Core Contents:**

```markdown
# Output Style: AI Exercise

## Template

```markdown
## 🤖 AI Exercise: [Specific Task Name]

**Scenario:** [Real-world context in 2-3 sentences]

**Challenge:** [What to build - clear and specific]

**Specification:**
Create a [thing] that:
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]

**Prompt Template:**
```
[Exact prompt to use with AI assistant]

Requirements:
- [Specific requirement]
- [Another requirement]
```

**Expected Output:**
[What the AI should generate]

**Success Criteria:**
- [ ] Code runs without errors
- [ ] Includes type hints
- [ ] Handles edge cases
- [ ] Meets all requirements

**Reflection Questions:**
1. How did the AI interpret your specification?
2. What needed clarification or refinement?
3. What did you learn from the generated code?
4. How would you improve the prompt?
```

[Complete patterns for different exercise types]
```

**Size:** ~300 lines  
**Time:** 1 hour

---

### 5. Technical Writing Skill ⏳

**File:** `.claude/skills/technical-writing.md`

**Purpose:** Voice, tone, readability standards

**Core Contents:**

```markdown
# Skill: Technical Writing for Education

## Voice and Tone

### DO (Encouraging Mentor)
- ✅ "Let's explore this together"
- ✅ "You might wonder why..."
- ✅ "Don't worry if this seems tricky"
- ✅ Use "we" and "you"
- ✅ Active voice
- ✅ Conversational

### DON'T (Academic Authority)
- ❌ "Obviously" / "simply" / "just"
- ❌ "You should already know"
- ❌ Passive voice
- ❌ Condescending language

## Readability Standards

**Targets:**
- Flesch Reading Ease: 60-70
- Grade level: 8th-9th
- Sentence length: 15-20 words average
- Paragraph: 3-5 sentences max

## Language Choices

**Use:** discover, explore, learn, practice, experiment, build
**Avoid:** trivial, basic, elementary, simple, obvious

## Quality Criteria

[Specific guidelines with examples]
```

**Size:** ~400 lines  
**Time:** 1.5 hours

---

### 6. Pedagogy Skill ⏳

**File:** `.claude/skills/pedagogy.md`

**Purpose:** Teaching methodologies

**Core Contents:**

```markdown
# Skill: Progressive Pedagogy

## Core Pattern: Show-Then-Explain

### The Pattern
1. Show working code FIRST
2. Explain WHAT it does (high-level)
3. Explain HOW it works (line-by-line)
4. Explain WHY designed this way (principles)
5. Show variations

### Example
```python
# 1. SHOW: Working code first
result = [x * 2 for x in range(5)]
print(result)  # [0, 2, 4, 6, 8]

# 2. WHAT: Creates doubled numbers
# 3. HOW: Iterates 0-4, multiplies each by 2, builds list
# 4. WHY: More readable than for loop
# 5. VARIATION: Can filter while transforming
result = [x * 2 for x in range(10) if x % 2 == 0]
```

## Progressive Complexity

**Chapters 1-5:** ONE concept per section, heavy scaffolding
**Chapters 6-15:** TWO concepts per chapter, moderate scaffolding  
**Chapters 16-26:** MULTIPLE concepts, minimal scaffolding

## Mistake-Driven Learning

Always include Common Mistakes section showing:
1. The mistake (actual code)
2. Why it happens (mental model)
3. The fix (correct code)
4. What was learned

[Complete pedagogical patterns]
```

**Size:** ~500 lines  
**Time:** 2 hours

---

### 7. Python Teaching Skill ⏳

**File:** `.claude/skills/python-teaching.md`

**Purpose:** Python-specific instruction

**Core Contents:**

```markdown
# Skill: Python Teaching Methodology

## Progressive Feature Introduction

### Chapters 1-5: Foundations
- Variables, types (str, int, float, bool)
- Control flow (if/while/for)
- Lists and basic operations
- Simple functions

### Chapters 6-10: Building Blocks
- Functions with basic type hints
- Dictionaries and sets
- File operations
- try/except basics
- List comprehensions

### Chapters 15-18: Prompt Engineering
- Complex type hints
- Optional, Union types
- Generic types

### Chapters 19-26: Modern Python 3.13+
- Advanced type hints (Protocols, TypedDict)
- Pattern matching (match/case)
- Dataclasses
- Full mypy workflow

## Common Misconceptions

### Misconception 1: Indentation is optional
**Truth:** Python uses indentation for structure
**How to teach:**
```python
# Show error with wrong indentation
# Explain Python's philosophy
# Contrast with brace-based languages
```

### Misconception 2: Lists and strings are identical
**Truth:** Strings immutable, lists mutable
**How to teach:**
```python
my_list = [1, 2, 3]
my_list[0] = 99  # Works!

my_str = "hello"
my_str[0] = 'H'  # TypeError!
```

[All common misconceptions with teaching strategies]
```

**Size:** ~450 lines  
**Time:** 2 hours

---

### 8. AI Collaboration Skill ⏳

**File:** `.claude/skills/ai-collaboration.md`

**Purpose:** Teaching AI usage

**Core Contents:**

```markdown
# Skill: AI Collaboration Teaching

## When to Use AI

### USE AI FOR:
✅ Code generation from clear specifications
✅ Error explanation and debugging help
✅ Refactoring and optimization suggestions
✅ Documentation generation
✅ Learning alternative approaches

### THINK FIRST:
⚠️ Problem decomposition
⚠️ Architecture decisions
⚠️ Understanding requirements
⚠️ Algorithm selection

### ALWAYS VERIFY:
🔍 Test generated code
🔍 Understand what it does
🔍 Check edge cases
🔍 Validate logic

## Teaching Progression

**Chapters 1-5:** Basic AI interaction
- Introduce as learning partner
- Simple prompts
- Reading AI outputs

**Chapters 6-10:** Specification writing
- Clear requirements
- Spec-Kit methodology
- Iterative refinement

**Chapters 15-18:** Advanced prompting
- Context management
- Complex specifications
- Multi-step workflows

## Verification Pattern (Teach Every Chapter)

Show students to:
1. Read AI code carefully
2. Understand what it does
3. Test it themselves
4. Modify and experiment
5. Learn from patterns

[Complete teaching strategies]
```

**Size:** ~400 lines  
**Time:** 1.5 hours

---

### 9. Chapter Writer Sub-Agent ⏳

**File:** `.claude/sub-agents/chapter-writer.md`

**Purpose:** Generate complete chapters

**Core Contents:**

```markdown
# Sub-Agent: Chapter Writer

## Role
Generate complete, publication-ready chapter content from specifications.

## Required Inputs
1. **Chapter Spec:** specs/part-XX/chapter-YY-spec.md
2. **Constitution:** constitution.md
3. **Output Styles:**
   - docusaurus-chapter.md
   - code-example.md
   - exercise.md
4. **Skills:**
   - technical-writing.md
   - pedagogy.md
   - python-teaching.md
   - ai-collaboration.md

## Process (6 Steps)

### Step 1: Read and Understand
- Read chapter specification completely
- Understand learning objectives
- Note prerequisites and dependencies
- Review required examples

### Step 2: Apply Structure
- Use docusaurus-chapter.md template
- Fill YAML frontmatter
- Create section outline
- Plan content flow

### Step 3: Write Content
- Apply technical-writing.md voice
- Use pedagogy.md teaching patterns
- Follow show-then-explain
- Maintain conversational tone

### Step 4: Create Code
- Follow code-example.md format
- Python 3.13+ syntax
- Type hints on all functions
- Include usage examples

### Step 5: Design Exercise
- Use exercise.md template
- Create realistic scenario
- Write clear specification
- Add reflection questions

### Step 6: Self-Check
- [ ] Matches spec
- [ ] Follows output styles
- [ ] Applies skills
- [ ] 2,000-2,500 words
- [ ] Has 3+ code examples
- [ ] All sections present

## Output
Complete markdown file: `book-site/history/part-XX/chapter-YY.md`

## Handoff
→ Pass to code-validator sub-agent

## Quality Checks I Perform
- Structure compliance
- Voice consistency
- Pedagogical flow
- Format correctness

## Quality Checks I DON'T Perform
- Code actually runs (code-validator)
- Technical accuracy (technical-reviewer)
- Final editorial polish (human)
```

**Size:** ~400 lines  
**Time:** 2 hours

---

### 10. Code Validator Sub-Agent ⏳

**File:** `.claude/sub-agents/code-validator.md`

**Purpose:** Test all code examples

**Core Contents:**

```markdown
# Sub-Agent: Code Validator

## Role
Extract and test all code examples for correctness, type safety, and style compliance.

## Inputs
- Chapter markdown from chapter-writer
- Python 3.13 environment
- mypy, black tools

## Process

### Step 1: Extract Code
- Find all Python code blocks
- Extract to temporary files
- Preserve line numbers for reporting

### Step 2: Test Execution
```bash
python3.13 extracted_code.py
# Check: Runs without errors
# Check: Output matches expected
```

### Step 3: Type Check
```bash
mypy --strict extracted_code.py
# Check: No type errors
# Check: All functions have hints
```

### Step 4: Style Check
```bash
black --check extracted_code.py
# Check: Properly formatted
# Check: 88 char line length
```

### Step 5: Generate Report

```
Code Validation Report
Chapter: [X]
Date: [timestamp]

Code Block 1 (line 45): ✅ PASS
- Execution: ✅ No errors
- mypy: ✅ Type checks pass
- black: ✅ Formatted correctly
- Output: ✅ Matches expected

Code Block 2 (line 123): ❌ FAIL
- Execution: ❌ NameError: 'x' not defined
- Fix: Define x before use
- Suggested correction: [code]

Summary: 8/10 examples pass
```

## Outputs
- Validation report
- Fixed code (if needed)
- Pass/fail status

## Handoff
- If ALL PASS: → technical-reviewer
- If ANY FAIL: → back to chapter-writer with fixes

## I Check
- Code runs
- Types valid
- Style compliant

## I Don't Check
- Technical accuracy (technical-reviewer)
- Pedagogical quality (human)
```

**Size:** ~350 lines  
**Time:** 1.5 hours

---

### 11. Technical Reviewer Sub-Agent ⏳

**File:** `.claude/sub-agents/technical-reviewer.md`

**Purpose:** Verify technical accuracy

**Core Contents:**

```markdown
# Sub-Agent: Technical Reviewer

## Role
Verify technical accuracy, best practices, and factual correctness.

## Inputs
- Validated chapter (code tested)
- Python documentation
- Best practices references

## Process

### Step 1: Fact Check
- Verify all technical claims
- Check Python version features
- Validate tool capabilities
- Confirm best practices current

### Step 2: Best Practices Review
- Code follows Python conventions
- Uses appropriate patterns
- Demonstrates modern practices
- Avoids anti-patterns

### Step 3: Explanations Check
- Technical explanations accurate
- No misleading statements
- Correct terminology
- Appropriate depth

### Step 4: Tools & Versions
- Tool instructions current
- Version numbers correct
- Installation steps valid
- Links working

### Step 5: Generate Report

```
Technical Review Report
Chapter: [X]
Reviewer: technical-reviewer
Date: [timestamp]

✅ APPROVED Sections:
- Introduction: Accurate and clear
- Section 1: Best practices followed
- Code examples: Modern Python patterns

⚠️ NEEDS REVISION:
- Section 2 (line 234): Claim about Python 3.13 
  feature needs verification
  Suggested fix: [correction]
  
- Exercise (line 456): Tool version outdated
  Current: Python 3.11
  Should be: Python 3.13

Overall: CONDITIONAL APPROVAL
Action: Minor revisions needed
```

## Outputs
- Technical review report
- Required corrections
- Approval status

## Handoff
- If APPROVED: → human for final review
- If REVISIONS NEEDED: → back to chapter-writer

## I Check
- Technical accuracy
- Best practices
- Current information

## I Don't Check
- Code runs (code-validator did this)
- Writing quality (human reviews)
```

**Size:** ~300 lines  
**Time:** 1.5 hours

---

## Implementation Timeline

### Day 1: Foundation & Output Styles
- [ ] Hour 1-3: Create `specs/pre-setup.md`
- [ ] Hour 4-6: Create `docusaurus-chapter.md`
- [ ] Hour 7-8: Create `code-example.md`
- [ ] Hour 9: Create `exercise.md`

**End of Day 1:** Output styles complete

### Day 2: Skills
- [ ] Hour 1-2: Create `technical-writing.md`
- [ ] Hour 3-4: Create `pedagogy.md`
- [ ] Hour 5-6: Create `python-teaching.md`
- [ ] Hour 7-8: Create `ai-collaboration.md`

**End of Day 2:** Skills complete

### Day 3: Sub-Agents & Test
- [ ] Hour 1-2: Create `chapter-writer.md`
- [ ] Hour 3-4: Create `code-validator.md`
- [ ] Hour 5-6: Create `technical-reviewer.md`
- [ ] Hour 7-8: Create Chapter 1 specification
- [ ] Hour 9-10: TEST: Generate Chapter 1

**End of Day 3:** Complete infrastructure + first chapter test

### Day 4: Refinement
- [ ] Review Chapter 1 output
- [ ] Refine infrastructure based on results
- [ ] Regenerate Chapter 1
- [ ] Finalize templates

**End of Day 4:** Production-ready infrastructure

---

## Success Criteria

Infrastructure is complete when:
- [ ] All 12 files created
- [ ] Chapter 1 generates successfully
- [ ] Code validates without errors
- [ ] Technical review approves
- [ ] Human can publish with minimal edits
- [ ] Process is repeatable for remaining 25 chapters

---

## Total Scope

**Files to create:** 12  
**Estimated time:** 3-4 days  
**Lines of content:** ~4,500 lines  
**Result:** Complete working system for 26-chapter book

---

---

## Final Clarity: Sprint Architecture

### ✅ WILL BE PRE-CREATED (15 files):

**Foundation (2 files)**
- ✅ constitution.md (COMPLETE)
- ⏳ specs/pre-setup.md

**Output Styles (4 files)**
- ⏳ .claude/output-styles/docusaurus-chapter.md
- ⏳ .claude/output-styles/lesson.md
- ⏳ .claude/output-styles/code-example.md
- ⏳ .claude/output-styles/exercise.md

**Skills (4 files — shared guidance frameworks)**
- ⏳ .claude/skills/planning.md
- ⏳ .claude/skills/technical-writing.md
- ⏳ .claude/skills/pedagogy.md
- ⏳ .claude/skills/ai-collaboration.md

**Sub-Agents (5 files — collaborative orchestrators)**
- ⏳ .claude/sub-agents/planner.md
- ⏳ .claude/sub-agents/chapter-writer.md
- ⏳ .claude/sub-agents/lesson-writer.md
- ⏳ .claude/sub-agents/code-validator.md
- ⏳ .claude/sub-agents/technical-reviewer.md

**TOTAL: 15 files**

### ❌ NOT IN SCOPE (For Later):

- Additional sub-agents beyond these 5
- Additional skills beyond these 4
- Chapter-specific customizations
- Integration with external APIs or tools
- Advanced features (version control, collaboration, etc.)

### 🎯 Design Principles for This Sprint:

**These 4 skills + 5 sub-agents are sufficient to:**
- Implement the full Spec-Driven Development loop
- Generate a complete, high-quality 26-chapter book
- Maintain consistency through shared infrastructure
- Enable human-AI collaborative writing (not delegation)
- Validate code quality and technical accuracy
- Create a repeatable, scalable process

**Design ensures:**
- AI and humans use the same skills and output styles
- Every stage has iteration points (humans stay immersed)
- Clear handoff criteria between agents
- No one-way delegation (collaborative loop)
- Separation of concerns (plan → structure → write → validate → review)

---

## Ready to Execute?

**Next step:** Create `specs/pre-setup.md`

**Say the word and I'll start building!** 🚀