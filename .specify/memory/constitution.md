<!--
Sync Impact Report:
Version: 2.0.0 (Principle-driven governance constitution)
Created: 2025-10-28
Refactored: 2025-10-28
Rationale: Separated principle-level governance from implementation details. Technical specifications and procedural details moved to templates/specs. This document now focuses on WHY and WHAT; templates define HOW.
Templates Aligned:
  - spec-template.md (references these principles)
  - plan-template.md (governance-aware planning)
  - tasks-template.md (task decomposition aligned with principles)
  - output-styles/ (follow principle-based constraints, not this document)
  - skills/ (reference and apply these principles)
Follow-up TODOs:
  - Create technical specification template for chapter implementation
  - Create code standards specification separate from constitution
-->

# CoLearning Python: The AI-Driven Way — Project Constitution

**Version:** 2.0.0 | **Ratified:** 2025-10-28 | **Last Amended:** 2025-10-28

---

## I. Project Vision & Philosophy

### Vision

"CoLearning Python: The AI-Driven Way" is a 26-chapter technical book that teaches modern Python programming (3.13+) through systematic collaboration between human learners and AI assistants. The book demonstrates how to learn and write code effectively in the AI-driven development era—not as a replacement for thinking, but as an amplifier of capability.

### Core Philosophy

- **AI as Collaborative Partner:** AI tools are intelligent co-workers equal to humans, working together within shared constraints
- **Specification-First Methodology:** Clear requirements precede all work; specifications emerge iteratively
- **Learning by Doing:** Every concept is practiced through realistic, AI-assisted hands-on work
- **Transparency:** We teach readers our methodology and demonstrate it throughout the book

### Target Audience

- **Primary:** Programming beginners (no prior coding experience required)
- **Secondary:** Professional developers transitioning to AI-driven development
- **Context:** Self-paced learning, classroom, mentorship, independent study
- **Prerequisite:** Basic computer literacy only (file management, terminal basics, curiosity about AI)

---

## II. Core Principles (Non-Negotiable)

### Principle 1: AI-First Teaching Philosophy

Every concept, example, and exercise MUST demonstrate AI-assisted development as the primary workflow, not an afterthought.

**Why This Matters:** In 2025 and beyond, professional developers work WITH AI, not despite it. Teaching Python without AI is teaching an outdated workflow. Students must develop AI collaboration skills from day one to be job-ready.

**What This Means:**
- AI tools are introduced early (Part 1) and used throughout
- Every code example shows both the prompt/request and the AI-generated result
- Students learn to write effective prompts alongside Python syntax
- Traditional "manual coding first" approach is explicitly rejected as outdated

---

### Principle 2: Spec-Kit Methodology as Foundation

Spec-Kit methodology MUST be introduced early (Part 2) and applied to all subsequent projects and examples.

**Why This Matters:** Specification-Driven Development (SDD) is a scalable, AI-friendly methodology. Early exposure builds better software engineering habits and enables collaborative workflows with AI agents.

**What This Means:**
- Part 2 (5 chapters) exclusively dedicated to Spec-Kit methodology
- All projects from Part 3 onward use Spec-Kit structure: spec → plan → tasks → implementation
- Students practice writing specifications and plans WITH AI assistance
- Constitution, ADR, and PHR concepts are explained and practiced as real artifacts, not theory

---

### Principle 3: Modern Python Standards (3.13+)

All code MUST use Python 3.13+ features with mandatory type hints throughout.

**Why This Matters:** Type hints are now standard in professional Python development. Teaching without them creates technical debt and bad habits. Modern syntax (match/case, structural patterns) makes code more readable. Students must learn current best practices, not legacy patterns.

**What This Means:**
- Python 3.13+ syntax required; no legacy patterns or compatibility code
- Type hints mandatory for all function signatures (zero exceptions)
- Modern syntax features demonstrated and explained
- No pre-3.10 type hint styles (e.g., `Optional` from typing module)
- All code validated for type safety (mypy or pyright)

---

### Principle 4: Test-First Mindset

Testing concepts MUST be integrated early and practiced throughout, not relegated to a single late chapter.

**Why This Matters:** Professional code is tested code. Introducing testing late makes it seem optional. Early integration normalizes testing as part of development. AI tools excel at generating tests from specifications.

**What This Means:**
- Unit testing introduced by Part 2 (no later than Chapter 6)
- Every significant code example includes corresponding tests
- Test-writing prompts shown alongside implementation prompts
- TDD workflow demonstrated: write test → see it fail → implement → see it pass
- Coverage expectations enforced: critical functions 100%, overall >80%

---

### Principle 5: Progressive Complexity with Clear Scaffolding

Content difficulty MUST increase gradually with no sudden jumps. Earlier chapters have heavy support; later chapters assume increasing independence.

**Why This Matters:** Beginners need scaffolding. Jumping complexity levels loses readers. Clear prerequisite chains allow modular learning and reference. Progressive complexity reduces frustration and increases completion rates.

**What This Means:**
- Part 1-5: Chapters 1-5 (heavy scaffolding), 6-15 (moderate), 16-26 (minimal)
- Concepts introduced once, then referenced by name
- Explicit prerequisite chains documented
- No forward references to unexplained concepts without saying "Chapter X covers this"
- Related concepts taught together, not scattered across chapters

---

### Principle 6: Consistent Structure Across All Chapters

All content creators (human authors and AI agents) MUST use the same shared infrastructure (skills, output styles, sub-agents) to ensure consistency across 26 chapters.

**Why This Matters:** Consistency in form allows readers to focus on content. It also makes chapters replaceable and updatable without cascading changes. Shared infrastructure enables AI and humans to collaborate effectively.

**What This Means:**
- All chapters follow identical structure (documented in output-styles)
- All lessons follow identical teaching structure
- All Python code follows identical formatting standards
- All exercises follow identical structure and approach
- All content creators reference the same skills and constraints
- Cross-chapter consistency is verified before publication

---

### Principle 7: Technical Accuracy and Currency (Always Verified)

All technical claims MUST be verified, tool versions current, and best practices demonstrated.

**Why This Matters:** Teaching outdated or incorrect practices wastes reader time and creates bad habits. Accuracy builds trust and sets professional standards.

**What This Means:**
- All Python version features verified for 3.13+
- All tool instructions tested (Claude Code, Gemini CLI, Codex, Cursor, Zed)
- All external links live and current at publication
- Best practices demonstrated (PEP 8, Python idioms, modern patterns)
- All technical claims fact-checked and sourced
- Security practices demonstrated (no hardcoded secrets, proper error handling)

---

### Principle 8: Accessibility and Inclusivity (No Gatekeeping)

Content MUST be welcoming and accessible to diverse learners with varied backgrounds and abilities.

**Why This Matters:** Beginners come from all backgrounds. Assumptions exclude learners. Clarity benefits everyone. Accessibility is quality, not a feature.

**What This Means:**
- No assumed computer science background (explain jargon on first use)
- No ableist language ("obviously", "simply", "just", "easy")
- Code examples include clear comments explaining intent
- Diverse example names/contexts; gender-neutral language
- Multiple explanation styles: text, code, diagrams, analogies
- Platform-specific instructions where setup differs (Windows/Mac/Linux)
- Free/open-source alternatives always provided

---

### Principle 9: Show-Then-Explain Pedagogy

Teaching MUST follow a consistent pattern: show working code FIRST, then explain WHAT/HOW/WHY.

**Why This Matters:** Research shows learners comprehend better when shown working examples before complex explanations. This pattern reduces cognitive load and increases retention.

**What This Means:**
- Present working code before explaining
- Describe WHAT the code does (high-level overview)
- Explain HOW it works (step-by-step execution)
- Explain WHY design decisions were made
- Show variations and related patterns
- Every chapter includes a "Common Mistakes" section
- Every chapter includes an "AI Exercise" (starting Ch 3)

---

### Principle 10: Real-World Project Integration

Projects MUST reflect realistic development scenarios, not contrived academic exercises.

**Why This Matters:** Toy examples don't transfer to real work. Students need portfolio-worthy projects. Real-world friction (APIs, error handling, deployment) is learning opportunity, not obstacle. GitHub presence is essential for job seekers.

**What This Means:**
- Projects use real tools: git, virtual environments, package managers, CI/CD concepts
- File organization matches professional conventions (src/, tests/, history/, .env)
- Projects published to GitHub with README, license, documentation
- Integration with real APIs and data sources (with appropriate error handling)
- Deployment considerations addressed (even if simplified)
- Projects span multiple chapters showing iterative development

---

### Principle 11: Tool Diversity and Honest Comparison

Multiple AI tools MUST be covered with honest comparison, not single-tool lock-in.

**Why This Matters:** AI tool landscape evolves rapidly. Teaching one tool creates fragility. Students benefit from understanding trade-offs and having backup options. Tool diversity builds adaptable problem-solving skills.

**What This Means:**
- Part 3 (AI Tool Landscape) covers: Claude Code, Gemini CLI, GitHub Codex, Cursor, Zed
- Each tool's strengths and ideal use cases explained objectively
- Common workflows demonstrated across multiple tools
- Students encouraged to experiment and find personal preferences
- No vendor lock-in language; all tools presented as options
- Fallback strategies when tools unavailable (rate limits, API changes)

---

## III. Mandatory Five-Part Book Structure

The book MUST consist of exactly five parts with these chapter counts and focus areas:

**Part 1: Introducing AI-Driven Development (5 chapters)**
- Focus: Orientation, setup, first programs with AI
- Outcome: Comfortable using AI tools for basic Python tasks

**Part 2: Spec-Kit Methodology (5 chapters)**
- Focus: Professional workflow, specifications, planning, Spec-Kit practices
- Outcome: Can structure a project using Spec-Kit principles

**Part 3: AI Tool Landscape (4 chapters)**
- Focus: Deep dive into each AI platform and modern editors
- Outcome: Understands tool strengths, can choose appropriate tool for task

**Part 4: Prompt & Context Engineering (4 chapters)**
- Focus: Effective prompting, context management, debugging with AI
- Outcome: Writes high-quality prompts, manages AI interactions effectively

**Part 5: Modern Python with Type Hints (8 chapters)**
- Focus: Deep Python language features with type safety and testing
- Outcome: Writes production-quality Python code with full type annotations

---

## IV. Non-Negotiable Rules

### What We ALWAYS Do

✅ **ALWAYS:**
- Always plan ahead - use learning sciences and Pedagogical principles.
- Use specialized skills and subagents to enhance learning and understanding.
- Include type hints on every function without exception
- Test all code before publication
- Explain WHY, not just HOW (design decisions and reasoning)
- Provide working code examples with documented expected output
- Use Python 3.13+ modern syntax
- Include "Common Mistakes" section in every chapter
- Include "AI Exercise" in every chapter (starting Ch 3)
- Validate against this Constitution before publication
- Assume readers know nothing (no gatekeeping)
- Show both the prompt/request and the AI result
- Encourage verification and iteration with AI tools

### What We NEVER Do

❌ **NEVER:**
- Use vague gatekeeping terms without explanation ("easy", "simple", "obvious")
- Include untested or broken code
- Assume reader knowledge or background
- Use deprecated Python syntax
- Skip type hints for "simple" functions
- Condescend to readers
- Hardcode secrets, tokens, API keys, or passwords
- Make technical claims without verification
- Publish without human review
- Leave placeholder text or TODOs in published chapters
- Contradict earlier chapters without explicit explanation
- Present single AI tool as mandatory

### When to Escalate for Human Decision

**Always flag for human judgment when:**
- Breaking changes in Python versions
- Significant methodology shifts affecting prior chapters
- Content contradicts earlier chapters
- Uncertain or debatable technical claims
- Accessibility concerns
- Copyright or attribution issues
- Major style/voice inconsistencies
- Tool versions change significantly

---

## V. Development Workflow

### Specification-Driven Development Loop

All chapter development MUST follow this iterative SDD loop:

```
Source Material / Requirements
    ↓
Planner (AI) + Human → Create chapter specification
    ↓ (iterate until spec approved)
Chapter-Writer (AI) + Human → Create outline and structure
    ↓ (iterate until structure approved)
Lesson-Writer (AI) + Human → Implement lesson content
    ↓
Code-Validator (AI) → Verify all code works, types check, style compliant
    ↓
Technical-Reviewer (AI) → Verify accuracy and best practices
    ↓
Human → Final editorial polish and publication approval
```

**Key Principle:** Every stage can iterate. Handoff criteria define when work moves to the next stage. Failure at any stage returns to specification refinement, not manual override.

### Quality Gates

Each stage MUST include:
- Clear **input requirements** (what the previous stage must deliver)
- **Acceptance criteria** (how to verify the work meets requirements)
- **Handoff conditions** (when to move forward vs. iterate)

---

## VI. Infrastructure

### Shared Skills (Not Separate Agents)

All content creators MUST reference and apply four shared skills:

1. **planning.md** — How to create detailed specifications from source material
2. **technical-writing.md** — Voice, tone, readability standards for the book
3. **pedagogy.md** — Teaching methodologies (show-then-explain, progressive complexity)
4. **ai-collaboration.md** — Responsible AI usage, verification patterns, iteration strategies

### Output Styles (Format Specifications)

All content MUST conform to four output styles:

1. **docusaurus-chapter.md** — Chapter structure + Docusaurus frontmatter format
2. **lesson.md** — Individual lesson section formatting (teaching structure)
3. **code-example.md** — Python code formatting with type hints, docstrings, testing
4. **exercise.md** — AI Exercise formatting (scenario, prompt, reflection questions)

### Sub-Agents (Orchestrators)

Five specialized agents MUST be created to manage the SDD loop:

1. **planner** — Takes source material → creates detailed chapter specs
2. **chapter-writer** — Takes spec → creates outline and learning objectives
3. **lesson-writer** — Takes outline → writes actual lesson content with examples
4. **code-validator** — Takes chapter → tests code (python, mypy, black, execution)
5. **technical-reviewer** — Takes validated chapter → fact-checks and verifies best practices

---

## VII. Governance

### This Constitution's Authority

- **Source of Truth:** Supreme governing document for all book project decisions
- **Precedence:** All specifications, skills, output styles, and sub-agents must align with this Constitution
- **Enforcement:** All chapters validated against this Constitution before publication

### Amendment Process

**For Small Changes** (clarifications, wording):
- Make changes directly with commit message referencing this Constitution
- Increment PATCH version only

**For Significant Changes** (new principles, removed requirements, major redefinitions):
- Document rationale in commit message or linked ADR
- Update VERSION field
- Increment MAJOR or MINOR per semantic versioning
- Review all dependent templates and chapters for alignment
- Update "Last Amended" date

**For Proposals:**
1. Document the current problem or gap
2. Propose specific change to Constitution text
3. Justify with rationale (pedagogical, technical, practical)
4. Identify affected chapters and templates
5. Seek review and approval before implementing

### Compliance Verification

- **AI Agents** verify Constitutional alignment in outputs before handoff
- **Human Reviewer** confirms adherence before publication
- **Automated Checks** enforce standards where possible (mypy, black, Docusaurus build)

---

## VIII. Success Metrics

The book is complete and successful when:

- [ ] All 26 chapters written and validated
- [ ] All code examples tested and working
- [ ] All chapters follow Constitution principles
- [ ] Pedagogical flow coherent across all 5 parts
- [ ] No contradictions across chapters
- [ ] All cross-references valid
- [ ] Technical accuracy verified by domain experts
- [ ] Beta readers report 80%+ satisfaction
- [ ] Accessibility standards met
- [ ] Docusaurus build succeeds with zero warnings
- [ ] Ready for production publishing

---

**This Constitution is the source of truth for the CoLearning Python project. All decisions about content, structure, quality, and process resolve to these principles first. Implementation details are documented in separate templates and specifications.**
