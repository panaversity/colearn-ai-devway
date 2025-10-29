<!--
Sync Impact Report:
Version: 2.1.0 (Decoupled from project specifics, aligned with actual infrastructure)
Created: 2025-10-28
Refactored: 2025-10-29
Rationale: Removed hardcoded project details; now defers to authoritative sources (chapter-index.md). Updated infrastructure to match actual files. Replaced book-architecture with book-scaffolding skill based on proven learnings.

Changes in v2.1.0:
- Replaced book-architecture skill with book-scaffolding (skill 7)
- Fixed chapter count: 26 → 32 throughout
- Removed Part 2 vs Part 5 Spec-Kit contradiction (now refers to chapter-index.md)
- Fixed scaffolding ranges to cover all 32 chapters (1-10 heavy, 11-20 moderate, 21-32 minimal)
- Section III: Book Structure now defers to specs/book/chapter-index.md (authoritative source)
- Section VI: Infrastructure updated to match actual files (.claude/agents, .claude/output-styles, .claude/skills)
- Section V: Workflow updated to reflect actual 3 subagents (chapter-planner, lesson-writer, technical-reviewer)
- Made constitution truly generic and maintainable (follows same pattern as CLAUDE.md refactor)

Templates Aligned:
  - spec-template.md (references these principles)
  - plan-template.md (governance-aware planning)
  - tasks-template.md (task decomposition aligned with principles)
  - output-styles/ (follow principle-based constraints, not this document)
  - skills/ (reference and apply these principles, now includes book-scaffolding)
-->

# CoLearning Python & Agentic AI: The AI-Driven Way — Project Constitution

**Version:** 2.1.0 | **Ratified:** 2025-10-28 | **Last Amended:** 2025-10-29

---

## I. Project Vision & Philosophy

### Vision

"CoLearning Python & Agentic AI: The AI-Driven Way" is a 32-chapter technical book that teaches modern Python programming (3.13+) through systematic collaboration between human learners and AI assistants. It progresses from foundational AI-driven development through advanced topics including agentic AI systems and MCP (Model Context Protocol) frameworks. The book demonstrates how to learn and write code effectively in the AI-driven development era—not as a replacement for thinking, but as an amplifier of capability.

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

Spec-Kit methodology MUST be introduced progressively and applied to all projects and examples.

**Why This Matters:** Specification-Driven Development (SDD) is a scalable, AI-friendly methodology. Progressive exposure builds better software engineering habits and enables collaborative workflows with AI agents.

**What This Means:**
- Spec-Kit concepts introduced early (foundational parts) and formalized in dedicated part (see book structure)
- All significant projects use Spec-Kit structure: spec → plan → tasks → implementation
- Students practice writing specifications and plans WITH AI assistance
- Constitution, ADR, and PHR concepts are explained and practiced as real artifacts, not theory
- Refer to `specs/book/chapter-index.md` for specific chapter assignments and sequencing

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
- Progressive scaffolding: Early chapters (1-10) heavy support, middle chapters (11-20) moderate, later chapters (21-32) minimal
- Concepts introduced once, then referenced by name
- Explicit prerequisite chains documented
- No forward references to unexplained concepts without saying "Chapter X covers this"
- Related concepts taught together, not scattered across chapters
- Refer to `specs/book/chapter-index.md` for specific chapter progression and `book-scaffolding` skill for cognitive load management

---

### Principle 6: Consistent Structure Across All Chapters

All content creators (human authors and AI agents) MUST use the same shared infrastructure (skills, output styles, sub-agents) to ensure consistency across 32 chapters.

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

## II.B Domain Skills (The 8 CoLearning Skills)

All book development MUST leverage these 8 specialized domain skills. These skills codify pedagogical best practices and ensure consistent quality across all 32 chapters and 7 parts:

### 1. **learning-objectives** Skill
Generate measurable learning outcomes aligned with Bloom's taxonomy. Ensures every chapter/lesson has clear, testable objectives that guide content creation and assessment. Critical for parts 6-7 (agentic AI, MCP) where emerging topics require careful scaffolding.

### 2. **concept-scaffolding** Skill
Break down complex topics into manageable, progressive steps. Essential for Parts 1-3 (foundation building) and Parts 6-7 (advanced topics like agents and MCP protocols).

### 3. **code-example-generator** Skill
Create high-quality, runnable code examples with type hints, docstrings, and testing. All Python code in the book must follow this skill's standards (Python 3.13+, type hints, tested).

### 4. **exercise-designer** Skill
Design effective practice exercises aligned with learning objectives. Balances repetition, challenge, and application across all 32 chapters.

### 5. **assessment-builder** Skill
Build meaningful quizzes, review questions, and evaluations. Ensures learners can verify understanding at multiple Bloom's levels.

### 6. **technical-clarity** Skill
Ensure all explanations are clear, accessible, and free of jargon gatekeeping. Critical for our commitment to Principle 8 (Accessibility & Inclusivity).

### 7. **book-scaffolding** Skill
Plan and structure multi-part educational content with cognitive load management, narrative continuity, and just-in-time specification. Essential for planning book structure in collaboration with the user, managing progressive complexity, and ensuring clear prerequisite chains. Use the scaffolding workflow (reference/chapter-flow-patterns.md) for detailed structural planning.

### 8. **ai-augmented-teaching** Skill
Design lessons that effectively integrate AI tools as learning partners (not code generators). Ensures the book itself demonstrates the "learning WITH AI" philosophy it teaches.

**Governance**: All chapter content MUST be validated against these 8 skills before publication. Content creators (human authors and AI agents) should reference and apply these skills throughout development.

---

## III. Book Structure

The book MUST follow a multi-part progressive structure that builds from foundational concepts through advanced topics.

**Authoritative Reference**: `specs/book/chapter-index.md` defines all chapters, their part assignments, titles, key topics, and file names. This is THE definitive source for chapter organization.

**Structural Philosophy**:
1. **Foundation Building (Early Parts)**: Heavy scaffolding, AI-first introduction, tool literacy, and basic skills
2. **Core Skills Development (Middle Parts)**: Python mastery, professional workflows, specification methodology  
3. **Advanced Topics (Final Parts)**: Agentic AI systems, integration frameworks, real-world applications

**Each part MUST**:
- Build on previous parts with clear prerequisite chains
- Follow progressive complexity (gradual difficulty increase)
- Maintain consistent structure using the 8 domain skills and output styles
- Demonstrate AI-augmented learning throughout

**Planning New Parts**:
- Use the `book-scaffolding` skill to plan part structure in collaboration with the user
- Create part specs just-in-time (when prior parts are in implementation)
- Define narrative continuity, cognitive load strategy, and hands-on exercises
- Map connections to subsequent parts

**Key References**:
- **`specs/book/chapter-index.md`** — All 32 chapters with titles, numbers, and topics
- **`specs/book/directory-structure.md`** — File paths, folder organization, and naming conventions (authoritative source)

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

All content development MUST follow this iterative SDD loop:

```
Source Material / Requirements / Vision
    ↓
Human + Main Claude → Create specification
    ↓ (iterate until spec approved)
Chapter-Planner (AI subagent) → Create detailed lesson plans and task checklists
    ↓ (iterate until plans approved)
Lesson-Writer (AI subagent) + Human → Implement lesson content (one lesson at a time)
    ↓ (iterate per lesson with human review)
Technical-Reviewer (AI subagent) → Validate technical accuracy, pedagogy, constitution alignment
    ↓ (iterate if issues found)
Human → Final editorial polish and publication approval
```

**Key Principles:** 
- Every stage can iterate with human oversight
- Handoff criteria define when work moves to the next stage
- Failure at any stage returns to refinement, not manual override
- Use `book-scaffolding` skill for structural planning in collaboration with user

### Quality Gates

Each stage MUST include:
- Clear **input requirements** (what the previous stage must deliver)
- **Acceptance criteria** (how to verify the work meets requirements)
- **Handoff conditions** (when to move forward vs. iterate)

---

## VI. Infrastructure

### Domain Skills (The 8 CoLearning Skills)

All content creators MUST apply the 8 domain skills defined in Section II.B. These skills are located in `.claude/skills/` and provide pedagogical best practices for:

1. **learning-objectives** — Measurable outcomes with Bloom's taxonomy
2. **concept-scaffolding** — Progressive complexity management
3. **code-example-generator** — High-quality, tested code with type hints
4. **exercise-designer** — Effective practice exercises
5. **assessment-builder** — Meaningful quizzes and evaluations
6. **technical-clarity** — Accessibility and clear explanations
7. **book-scaffolding** — Multi-part content structure planning
8. **ai-augmented-teaching** — AI tools as learning partners

### Output Styles (Format Specifications)

All content MUST conform to output styles located in `.claude/output-styles/`:

1. **chapters.md** — Chapter structure and Docusaurus frontmatter format
2. **lesson.md** — Individual lesson section formatting and teaching structure

These are **generic, reusable templates** applicable to any educational content project.

### Sub-Agents (Orchestrators)

Three specialized agents manage the SDD loop phases (located in `.claude/agents/`):

1. **chapter-planner** — Takes approved spec → creates detailed lesson plans and task checklists
2. **lesson-writer** — Takes lesson plan → writes complete lesson content with all 8 domain skills applied
3. **technical-reviewer** — Takes completed chapter → validates technical accuracy, pedagogical effectiveness, and constitutional alignment

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

- [ ] All 32 chapters written and validated
- [ ] All code examples tested and working
- [ ] All chapters follow Constitution principles
- [ ] Pedagogical flow coherent across all 7 parts
- [ ] No contradictions across chapters
- [ ] All cross-references valid
- [ ] Technical accuracy verified by domain experts
- [ ] Beta readers report 80%+ satisfaction
- [ ] Accessibility standards met
- [ ] Docusaurus build succeeds with zero warnings
- [ ] Ready for production publishing

---

**This Constitution is the source of truth for the CoLearning Python project. All decisions about content, structure, quality, and process resolve to these principles first. Implementation details are documented in separate templates and specifications.**
