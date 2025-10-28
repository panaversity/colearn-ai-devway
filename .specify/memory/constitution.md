# CoLearning Python: The AI-Driven Way — Constitution

**Version:** 1.0.0 | **Ratified:** 2025-10-28 | **Last Amended:** 2025-10-28

---

## I. Project Vision & Structure

### Vision
"CoLearning Python: The AI-Driven Way" is a 26-chapter technical book that teaches modern Python programming (3.13+) through systematic collaboration between human learners and AI assistants. The book demonstrates how to learn programming effectively in the AI-driven development era—not as a replacement for thinking, but as an amplifier of capability.

### Core Philosophy
- **AI as Amplifier:** AI accelerates learning and code generation, but human understanding and judgment are always required
- **Specification-First:** Clear requirements (specifications) precede all content and code
- **Learning by Doing:** Every concept is practiced through realistic exercises and AI-assisted workflows
- **Transparency:** We teach readers what we use to create the book and demonstrate our methodology

### Book Structure (5 Parts, 26 Chapters)

**Part 1: Introducing AI-Driven Development (5 chapters)**
- Ch 1: The Paradigm Shift — Why AI changes how we learn programming
- Ch 2: Setting Up Your AI-Assisted Development Environment
- Ch 3: Your First Python Program with AI Assistance
- Ch 4: The Human-AI Partnership Model — When to think, when to ask AI
- Ch 5: When AI Helps and When It Hurts — Critical judgment in AI use

**Part 2: Spec-Kit Methodology (5 chapters)**
- Ch 6: Introduction to Specification-Driven Development
- Ch 7: Writing Effective Constitutions (Project Principles)
- Ch 8: Creating Detailed Specifications (Requirements Documents)
- Ch 9: From Specification to Implementation (Planning)
- Ch 10: Iterative Refinement with Spec-Kit (Feedback Loops)

**Part 3: AI Tool Landscape (4 chapters)**
- Ch 11: Claude Code — Native Abstractions (Skills, Output Styles, Sub-agents)
- Ch 12: Gemini CLI — Conversational AI Development
- Ch 13: OpenAI Codex & AGENTS.md — The Open Standard
- Ch 14: IDE-Integrated AI (Zed, Cursor) — Context-Aware Coding

**Part 4: Prompt & Context Engineering (4 chapters)**
- Ch 15: The Anatomy of Effective Prompts — Structure and Clarity
- Ch 16: Context Window Management — What to Include, What to Omit
- Ch 17: Clarity of Thought → Clarity of Code — From Confusion to Specification
- Ch 18: Debugging AI Outputs — Finding and Fixing Generated Code Problems

**Part 5: Modern Python with Type Hints (8 chapters)**
- Ch 19: Python 3.13 — Modern Features Overview
- Ch 20: Type Hints — Types as Documentation and Verification
- Ch 21: Data Structures with Type Safety — List, Dict, Set with Generics
- Ch 22: Functions, Decorators, and Type Checking — From Simple to Advanced
- Ch 23: Object-Oriented Python with Protocols — Structural Typing
- Ch 24: Pattern Matching and Structural Types — Modern Python Patterns
- Ch 25: Testing and Validation — Pytest, Mypy, Type Safety
- Ch 26: Building Your Portfolio Project — Capstone Application

### Target Audience
- **Primary:** Python beginners (basic computer literacy, no prior programming required)
- **Ages:** 14-65
- **Context:** Self-paced learning or classroom environments
- **Interest:** Using AI tools for productivity and learning

### Prerequisites
- Basic computer literacy (file management, terminal basics)
- Curiosity about AI and programming
- No Python experience required

---

## II. Core Principles

### Principle 1: Specification-Driven Development (SDD)
**Description:** All content, code, and exercises are created from detailed specifications. A specification is a clear, testable definition of what should be created and why.

**Non-Negotiable Rules:**
- Every chapter has a detailed specification (specs/part-X/chapter-Y-spec.md)
- Specifications must precede chapter writing (no "just write and figure it out")
- Specifications are reviewed and approved before content generation begins
- Specifications evolve iteratively based on feedback from generation agents
- Each specification includes: learning objectives, content structure, code examples required, pedagogical approach, success criteria

**Rationale:** Clear specifications enable AI to generate consistent, targeted content. They also serve as a contract between planning and execution—if the spec is clear, the content will be good.

---

### Principle 2: AI as Collaborative Partner (Not Tool Manager)
**Description:** AI agents (Planner, Chapter-Writer, Lesson-Writer) are intelligent collaborators with their own skills and sub-agents, operating within the SDD loop. Humans direct and iterate; AI explores and generates.

**Non-Negotiable Rules:**
- AI agents use shared skills (.claude/skills/), output styles (.claude/output-styles/), and sub-agents
- Humans stay immersed in the creative/iterative process (not delegating completely)
- AI operates within constraints defined by Constitution and Skills
- Every stage of pipeline has defined handoff criteria and can iterate
- AI failure is addressed by refining specifications, not by manual override

**Rationale:** AI models are sophisticated enough to handle complex creative tasks. We trust them as partners within structured constraints, not as black boxes we manage.

---

### Principle 3: Code Quality is Non-Negotiable
**Description:** All Python code must be production-quality, tested, and type-safe.

**Non-Negotiable Rules:**
- **Python Version:** 3.13+ only (use modern syntax, no legacy patterns)
- **Type Hints:** Required on EVERY function parameter and return type (zero exceptions)
- **Type Checking:** All code must pass `mypy --strict` with zero errors
- **Code Style:** All code must pass `black --check` (88-character line length)
- **Testing:** All code examples must run without errors and produce expected output
- **Documentation:** Google-style docstrings on all functions and classes
- **Validation:** Code examples include usage demonstrations with expected output comments

**Code Template (Required Structure):**
```python
"""Module docstring if needed."""

from typing import Optional

def example_function(
    param1: str,
    param2: int = 0
) -> dict[str, int]:
    """One-line summary ending with period.

    Longer explanation if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When/why this error occurs

    Example:
        >>> example_function("test", 5)
        {'result': 5}
    """
    if not param1:
        raise ValueError("param1 cannot be empty")

    # WHY: Explain your reasoning here
    result: dict[str, int] = {"result": len(param1) * param2}
    return result


if __name__ == "__main__":
    output = example_function("hello", 2)
    print(output)  # Output: {'result': 10}
```

**Rationale:** Type-safe, tested code teaches correct programming practices. Readers learn both language syntax and professional standards.

---

### Principle 4: Progressive Pedagogy (Show-Then-Explain)
**Description:** Teaching follows a consistent pattern that builds understanding progressively, without assuming prior knowledge.

**Non-Negotiable Rules:**
- **Show First:** Present working code BEFORE explaining
- **Explain WHAT:** Describe what the code does (high-level overview)
- **Explain HOW:** Walk through step-by-step execution
- **Explain WHY:** Explain design decisions and principles
- **Show Variations:** Demonstrate related patterns
- **Progressive Complexity:** Earlier chapters have heavy scaffolding; later chapters assume more independence
- **Mistake-Driven Learning:** Every chapter includes a "Common Mistakes" section showing what learners often do wrong and why
- **Practical Exercises:** Every chapter includes an "AI Exercise" that applies concepts

**Chapter Progression:**
- **Chapters 1-5:** ONE concept per section, very heavy scaffolding, frequent reinforcement
- **Chapters 6-15:** TWO concepts per chapter, moderate scaffolding, building independence
- **Chapters 16-26:** MULTIPLE concepts, minimal scaffolding, readers mostly self-sufficient

**Rationale:** Research shows learners comprehend better when shown working examples before complex explanations. Progressive complexity prevents overwhelm.

---

### Principle 5: Consistency Through Shared Infrastructure
**Description:** All content creators (human authors and AI agents) use the same skills, output styles, and sub-agents. This ensures consistency across 26 chapters.

**Non-Negotiable Rules:**
- All chapters follow identical structure (docusaurus-chapter.md output style)
- All lessons follow identical teaching structure (lesson.md output style)
- All Python code follows identical formatting (code-example.md output style)
- All exercises follow identical structure (exercise.md output style)
- All content creators reference the same skills (planning, technical-writing, pedagogy, ai-collaboration)
- Cross-chapter consistency is checked by technical-reviewer sub-agent

**Rationale:** Consistency in form allows readers to focus on content. It also makes chapters replaceable and updatable without cascading changes.

---

### Principle 6: Technical Accuracy and Currency
**Description:** All technical claims are verified, tool versions are current, and best practices are followed.

**Non-Negotiable Rules:**
- All Python version features are verified for 3.13+
- All tool instructions are tested (Claude Code, Gemini CLI, OpenAI Codex, etc.)
- All external links are live and current
- Best practices are followed (PEP 8, Python idioms, modern patterns)
- Type hint patterns demonstrate current best practices (use `list[int]` not `List[int]`)
- Security practices are demonstrated (no hardcoded secrets, proper error handling)
- All claims are fact-checked and include rationale

**Rationale:** Teaching outdated or incorrect practices wastes reader time and creates bad habits.

---

### Principle 7: Accessibility and Inclusivity
**Description:** Content is accessible to learners with different backgrounds, abilities, and learning styles.

**Non-Negotiable Rules:**
- No ableist language or gatekeeping ("obviously," "simply," "just," etc.)
- Explain concepts that "everyone" might know—no assumptions about background
- Code examples are screen-reader friendly (semantic markdown)
- Acronyms are defined on first use
- Readability targets: Flesch Reading Ease 60-70, Grade level 8-9
- Inclusive terminology (gender-neutral, culturally aware)
- Assume zero prior programming knowledge
- Diverse examples and use cases

**Rationale:** Inclusivity expands our audience and improves learning for everyone.

---

## III. Mandatory Content Structure

### Every Chapter Must Include (In Order):

1. **YAML Frontmatter** (Docusaurus metadata)
   - chapter_number, part_number, title, description
   - keywords, skills_introduced, skills_practiced, skills_mastered
   - python_version, required_tools, prerequisites, difficulty
   - reading_time, practice_time, sidebar_position

2. **Title (H1)** — Auto-populated from frontmatter

3. **🎯 Learning Objectives (H2)** — 3-5 specific, measurable outcomes

4. **📖 Introduction (H2)** — Hook + context connecting to prior chapters, 150-200 words

5. **[Core Section 1] (H2)** — First major topic using lesson output style

6. **[Core Section 2] (H2)** — Second major topic using lesson output style

7. **[Core Section 3] (H2)** — Optional third topic

8. **⚠️ Common Mistakes (H2)** — 2-3 misconceptions with fixes and explanations

9. **🤖 AI Exercise (H2)** — Specification-based hands-on practice with prompt template

10. **📝 Summary (H2)** — Recap of key points, 100-150 words

11. **🚀 Next Steps (H2)** — Preview of next chapter

12. **📚 Additional Resources (H2)** — Links to docs, tools, further reading

### Content Metrics:

- **Word Count:** 2,000-2,500 words (excluding code examples)
- **Code Examples:** Minimum 3 per chapter, maximum 8
- **Readability:** Flesch Reading Ease 60-70
- **Sentence Length:** 15-20 words average
- **Paragraph Length:** 3-5 sentences maximum
- **Code Line Length:** 88 characters maximum (Black standard)

---

## IV. Writing Style & Voice

### Voice Requirements

**DO (Encouraging Mentor):**
- ✅ "Let's explore type hints together"
- ✅ "You might wonder why..."
- ✅ "Don't worry if this seems tricky at first"
- ✅ Use "we" and "you" frequently
- ✅ Active voice primarily
- ✅ Conversational, encouraging
- ✅ Show enthusiasm for Python and AI

**DON'T (Academic Authority):**
- ❌ Avoid: "Obviously," "simply," "just," "merely"
- ❌ No: "You should already know..."
- ❌ Avoid passive voice (except for technical accuracy)
- ❌ Avoid condescending language or gatekeeping
- ❌ Don't use academic jargon without explanation

### Terminology & Consistency

**Standard Terms (Use Consistently):**
- Always: "AI assistant" (not "AI," "bot," "system")
- Always: "type hint" (not "type annotation" outside technical context)
- Always: "function" (not "method" unless OOP-specific context)
- Always: "parameter" (in function definitions); "argument" (when calling)
- Always: "specification" (not "spec sheet," "brief," "outline")
- Always: "Spec-Kit" (not "spec kit," "SpecKit," "Spec Kit")

---

## V. AI Tool Integration Standards

### How AI Tools Are Taught

**Part 1-2:** Introduce concepts without detailed tool instruction

**Part 3 (AI Tool Landscape):** Deep dive into each platform
- **Chapter 11:** Claude Code (skills, output-styles, sub-agents abstractions)
- **Chapter 12:** Gemini CLI (conversational interface)
- **Chapter 13:** OpenAI Codex (AGENTS.md standard, open ecosystem)
- **Chapter 14:** IDE-integrated AI (Zed, Cursor, VS Code)

**Part 4 (Prompt Engineering):** Tool-agnostic techniques that work across platforms

**Part 5 (Modern Python):** Practical use of AI for coding (in every chapter's AI Exercise)

### When AI Exercises Appear

Every chapter starting from **Chapter 3** includes a "🤖 AI Exercise" section:
- **Chapters 1-5:** Basic AI interaction (simple prompts, reading outputs)
- **Chapters 6-10:** Specification writing (clear requirements, Spec-Kit methodology)
- **Chapters 11-14:** Tool-specific exercises (using each platform)
- **Chapters 15-18:** Advanced prompting (context management, complex specifications)
- **Chapters 19-26:** Practical Python coding with AI (code generation, optimization, testing)

### Responsible AI Use (Always Teach)

Every AI Exercise must reinforce:
1. **Thinking first:** Don't delegate thinking to AI
2. **Clear specifications:** Write requirements before asking AI
3. **Verification:** Always test and understand generated code
4. **Iteration:** Refine prompts based on AI output
5. **Learning:** Study AI-generated code to understand patterns

---

## VI. Docusaurus Format Requirements

### Directory Structure
```
book-site/
├── docs/
│   ├── part-01/
│   │   ├── chapter-01.md
│   │   ├── chapter-02.md
│   │   └── ...
│   ├── part-02/
│   └── ...
├── docusaurus.config.js
├── sidebars.js
└── package.json
```

### Markdown Requirements
- Front matter: YAML between `---` delimiters
- Code blocks: ` ```python title="filename.py" showLineNumbers `
- Admonitions: `:::tip`, `:::note`, `:::caution` (Docusaurus syntax)
- Cross-references: `[text](../part-X/chapter-Y.md)`
- No HTML (use Markdown equivalent)
- Heading hierarchy: Start with H1 (auto from YAML), use H2+ for sections

### Build & Validation
- Build must succeed: `npm run build`
- No broken links: `npm run check-links` (if implemented)
- Markdown linting: MDX/remark standards
- No console warnings or errors

---

## VII. Quality Assurance Workflow

### Pre-Publication Checklist (Every Chapter)

**Content Quality:**
- [ ] All learning objectives addressed in chapter
- [ ] 2,000-2,500 words (excluding code)
- [ ] All required sections present in correct order
- [ ] No typos or grammar errors
- [ ] Flesch Reading Ease 60-70 verified
- [ ] Voice and tone consistent

**Code Quality:**
- [ ] Minimum 3 code examples, maximum 8
- [ ] All code passes `python3.13 code.py` (runs without errors)
- [ ] All code passes `mypy --strict` (zero type errors)
- [ ] All code passes `black --check` (proper formatting)
- [ ] Type hints on every function (zero exceptions)
- [ ] Google-style docstrings present
- [ ] Expected output documented in comments

**Pedagogical Quality:**
- [ ] Show-Then-Explain pattern is clear
- [ ] Complexity progression matches chapter difficulty
- [ ] Prerequisites met before chapter
- [ ] "Common Mistakes" section meaningful and relevant
- [ ] "AI Exercise" has realistic scenario and reflection questions
- [ ] Cross-references to prior/future chapters valid

**Technical Accuracy:**
- [ ] All technical claims fact-checked
- [ ] Tool versions current
- [ ] Links to documentation live
- [ ] Best practices demonstrated
- [ ] No deprecated patterns
- [ ] Security practices correct (no hardcoded secrets)

**Consistency:**
- [ ] Terminology matches glossary
- [ ] Output style (chapter/lesson/code/exercise) followed exactly
- [ ] Voice and tone consistent with prior chapters
- [ ] Skills application evident
- [ ] Cross-chapter dependencies accurate

### Review Pipeline

```
Source Material
    ↓
Planner (AI) + Human → specs/part-X/chapter-Y-spec.md
    ↓ (iterate)
Chapter-Writer (AI) + Human → outline + learning objectives
    ↓ (iterate)
Lesson-Writer (AI) + Human → complete lesson content
    ↓
Code-Validator (AI) → tests all code + report
    ↓
Technical-Reviewer (AI) → accuracy + best practices
    ↓
Human → final editorial polish + publication
```

---

## VIII. Non-Negotiable Rules

### What We ALWAYS Do

✅ **ALWAYS:**
- Include type hints on every function without exception
- Test all code before publication (runs, types check, style compliant)
- Explain WHY not just HOW
- Provide working examples with documented expected output
- Use Python 3.13+ modern syntax (`list[int]`, `str | int`, `match/case`)
- Include a "Common Mistakes" section in every chapter
- Include an "AI Exercise" in every chapter (starting Ch 3)
- Validate against this Constitution before publication
- Document assumptions and limitations
- Give credit to sources and inspiration
- Assume readers know nothing (no gatekeeping)

### What We NEVER Do

❌ **NEVER:**
- Use vague terms without explanation ("easy," "simple," "obvious")
- Include untested or broken code
- Assume reader knowledge or background
- Use deprecated Python syntax
- Skip type hints for "simple" functions
- Condescend to readers or use gatekeeping language
- Hardcode secrets, tokens, API keys, or passwords
- Make technical claims without verification
- Copy content without attribution
- Publish without human review
- Leave placeholder text or TODOs in published chapters
- Contradict information from earlier chapters without explicit explanation

### What Requires Escalation

**Always flag for human decision when:**
- Breaking changes in Python versions
- Significant methodology shifts that affect prior chapters
- Content contradicts earlier chapters
- Uncertain or debatable technical claims
- Accessibility concerns
- Potential copyright or attribution issues
- Major style/voice inconsistencies
- Tool versions change significantly

---

## IX. Glossary (Consistency Reference)

### Key Terms Defined for Book

- **AI Assistant:** An intelligent language model (Claude, Gemini, Codex) used as a coding and learning partner
- **Specification (Spec):** A clear, detailed, testable definition of what to build and why
- **Constitution:** Non-negotiable principles and rules governing a project
- **Spec-Kit:** GitHub's methodology for Specification-Driven Development
- **Type Hint:** A notation in Python indicating what type a variable or function parameter should be
- **Generic Type:** A type that works with any kind of data (e.g., `list[str]`, `dict[str, int]`)
- **Protocol:** A structural type definition in Python (what an object must do, not what it is)
- **Prompt:** A question or instruction given to an AI assistant
- **Context Window:** The amount of text an AI model can read and process in one interaction
- **Docusaurus:** A documentation generator that builds static websites from Markdown

---

## X. Governance & Amendment Process

### This Constitution's Authority

- **Source of Truth:** This Constitution is the supreme governing document for the book project
- **Precedence:** Specifications, Skills, Output Styles, and Sub-Agents must align with this Constitution
- **Enforcement:** All chapters are validated against this Constitution before publication

### Amendment Procedure

1. **Proposal:** Any significant change to principles, structure, or standards requires explicit proposal
2. **Rationale:** Amendments must include clear reasoning and impact analysis
3. **Version Bump:**
   - **MAJOR:** Principle removals/redefinitions (breaking changes)
   - **MINOR:** New principles or significant guidance additions
   - **PATCH:** Clarifications, wording fixes, typo corrections
4. **Effective Date:** Amendments apply to all subsequent chapters immediately unless otherwise specified
5. **Retroactive Application:** Previously published chapters reviewed for major amendments
6. **Documentation:** All amendments logged in "Last Amended" field with date

### Compliance Verification

- **AI Agents:** Verify Constitutional compliance in their outputs before handoff
- **Code Review:** Human reviewer confirms Constitutional adherence
- **Automated Checks:** Code validation (mypy, black) enforces standards where possible

---

## XI. Success Metrics

The book is complete and successful when:

- [ ] All 26 chapters written and validated
- [ ] All code examples tested and working
- [ ] Readability targets met (60-70 Flesch for all chapters)
- [ ] Pedagogical flow coherent across all 5 parts
- [ ] No contradictions across chapters
- [ ] All cross-references valid and working
- [ ] Glossary complete and all terms used consistently
- [ ] Beta readers report 80%+ satisfaction on learning outcomes
- [ ] Technical accuracy verified by subject matter experts
- [ ] Accessibility standards met (inclusive language, no gatekeeping)
- [ ] Docusaurus build succeeds with no warnings or errors
- [ ] Ready for production publishing (copyediting complete)

---

**This Constitution is the source of truth for the CoLearning Python project. All questions about content, structure, quality, and process resolve to this document first.**
