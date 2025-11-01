# Chapter 26: HOW (Building With Your Companion)

## Overview

Chapter 26 teaches specification-driven development through **hands-on experience**, not lectures. Students don't learn SpecifyPlus features in isolation—they **build something real** and discover the features and principles through genuine necessity.

This chapter implements **AI-native pedagogy**: Student + Companion BUILD specifications and projects together, learning by doing.

---

## Chapter Structure

### 7 Progressive Lessons (2-3 hours each)

#### Lesson 1: Help Your Companion Write a Better Spec
Students learn spec components by **coaching their companion** to write clearer specifications. Through natural conversation, they discover the six components of clarity.

**Learning**: Vague ideas → coached clarity → documented components

---

#### Lesson 2: Set Up Your Project With SpecifyPlus
Students explore SpecifyPlus by **using it**, not reading about it. They initialize a project, examine the structure with their companion, and understand why it's organized that way.

**Learning**: Structure teaches workflow → spec → plan → tasks

---

#### Lesson 3: Make Your Acceptance Criteria So Clear That AI Understands
Students write vague criteria, watch their companion build from them (producing mediocre code), then refine to SMART criteria and see the dramatic difference in code quality.

**Learning**: Clarity upstream → quality downstream (proven through iteration)

---

#### Lesson 4: Run /sp.specify With Your Companion
Students run the specification refinement tool and discover what gaps exist in their thinking. Together with their companion, they address gaps and understand iterative refinement.

**Learning**: Specs are iterative; tools expose gaps; clarity compounds

---

#### Lesson 5: Run /sp.plan and See the Implementation Plan
Students see their clear specification automatically transform into an implementation plan. They trace spec decisions through the plan and understand the cascade.

**Learning**: Spec quality → plan quality (directly, provably)

---

#### Lesson 6: Decompose Your Spec Into Atomic Tasks
Students run /sp.tasks and learn to evaluate task quality by asking: "Is this small enough to build without getting stuck?"

**Learning**: Plan decomposition → atomic tasks → buildable work

---

#### Lesson 7: Build Your Grading System Spec End-to-End
Students integrate all previous lessons by completing a **production-quality specification** and running it through all SpecifyPlus tools.

**Learning**: Full workflow integration; professional specification ready for implementation

---

### 2 Mini-Projects (Progressive Application)

#### Mini-Project 1: Build a Python Calculator Spec-First
Students apply spec-first methodology to a real project. They write a specification, code from that specification (with AI assistance), write tests, and **validate code against the spec**.

**Deliverable**: Working Python calculator + tests + validation checklist

**Key Insight**: Clear spec → AI generates good code → tests validate it

---

#### Mini-Project 2: Write a Production Grading System Spec
Students write a **production-grade specification** for a real-world problem (inspired by Gradewiz, Edexia, Frizzle, Mimir). No implementation—focus is on professional specification writing.

**Deliverable**: 12+ section spec + handoff document for implementation team

**Key Insight**: Specification quality is separate from implementation quality; great specs come from understanding the real problem

---

## Pedagogical Approach

### AI-Native Pedagogy (Not Learn-Then-Apply)

Traditional: Students learn SpecifyPlus features → then apply them
This chapter: Students BUILD a spec → discover SpecifyPlus features through necessity

**How it works:**
1. Student + Companion identify a vague idea
2. Student coaches clarity (discovering six components)
3. Student structures in SpecifyPlus (discovering why structure matters)
4. Student refines criteria (discovering quality-consequence link)
5. Tools validate and expand (discovering cascading quality)
6. Student applies to real project (discovering integration)

**Why this works**: Learning is grounded in immediate, meaningful application. No abstract lectures about "what specs are"—instead, experience "what happens when specs are clear vs. vague."

---

## Domain Skills Applied

All 9 domain skills are applied contextually to this **hybrid technical/conceptual chapter**:

1. **learning-objectives** — Students discover learning through doing; objectives emerge naturally
2. **concept-scaffolding** — Progressive complexity: vague → clear → tool-validated → integrated
3. **code-example-generator** — Mini-Project 1 includes real Python code with type hints
4. **exercise-designer** — Each lesson is a hands-on exercise; mini-projects are applied exercises
5. **assessment-builder** — Validation checklists replace traditional quizzes; self-assessment through doing
6. **technical-clarity** — Language explains "why clarity matters" through experience, not theory
7. **book-scaffolding** — Chapter connects to Lesson 25 (SDD fundamentals) and sets up Chapter 27 (real-world workflows)
8. **ai-collaborate-learning** — Frame AI companion as thinking partner, not code generator
9. **content-evaluation-framework** — Implicit: spec quality evaluation, code validation, feedback iteration

---

## Quality Standards Met

### All Chapters

- [x] Learning objectives are measurable (implicit: students can evaluate spec quality by end)
- [x] Concepts scaffolded with clear progression (vague → clear → refined → integrated)
- [x] Language is clear; jargon defined in context
- [x] Connections to adjacent lessons made within body (Ch 25 setup → Ch 27 real-world)
- [x] AI's role framed appropriately (thinking partner for specifications and code review)
- [x] Markdown follows lesson template structure
- [x] Opening hooks present (each lesson starts with "what you're about to discover")
- [x] Factual claims include citations where applicable
- [x] Pacing appropriate (1.5-3 hours per lesson; 2-4 hour mini-projects)
- [x] No gatekeeping language ("easy," "simple," "obvious")
- [x] Diverse example contexts (grading system, calculator, production SaaS)
- [x] Inclusive language (gender-neutral; non-technical path provided)
- [x] Visual breaks present (headings, code blocks, tables, prompt examples)
- [x] Ends with "Try With AI" sections (progressively scoped prompts)

### Hybrid Content Specifics

- [x] Narrative sections explain "why" specification matters
- [x] Code examples (Mini-Projects) include type hints and docstrings
- [x] Reflection prompts encourage critical thinking
- [x] Real-world examples grounded in actual SaaS companies
- [x] Professional tone (no hype; balanced view of tradeoffs)

### AI-Native Pedagogy Specifics

- [x] No "learn features first" — students discover through necessity
- [x] Companion frames as thinking partner, not answerer
- [x] Complexity delegated appropriately (student makes decisions; AI handles execution)
- [x] Artifacts matter (specs, tests, specs ready for real teams)
- [x] Building > explaining (students build specs, not just read about them)
- [x] AI as validator (companion reviews specs, points out gaps)

---

## Files Included

```
26-specifyplus-hands-on/
├── 01-help-your-companion-write-a-better-spec.md      (Lesson 1, 2h)
├── 02-set-up-your-project-with-specifyplus.md         (Lesson 2, 1.5h)
├── 03-make-your-acceptance-criteria-so-clear-that-ai-understands.md  (Lesson 3, 2h)
├── 04-run-sp-specify-with-your-companion.md           (Lesson 4, 1.5h)
├── 05-run-sp-plan-and-see-the-implementation-plan.md  (Lesson 5, 1.5h)
├── 06-decompose-your-spec-into-atomic-tasks.md        (Lesson 6, 1.5h)
├── 07-build-your-grading-system-spec-end-to-end.md    (Lesson 7, 3h)
├── 08-mini-project-1-build-a-python-calculator-spec-first.md      (MP1, 3-4h)
├── 09-mini-project-2-write-a-production-grading-system-spec.md    (MP2, 3-4h)
└── README.md                                            (This file)
```

**Total**: 9 lesson/mini-project files, approximately 19,000 words

---

## Learning Outcomes

By completing Chapter 26, students will be able to:

1. **Discover specification components** by coaching clarity from vague ideas
2. **Use SpecifyPlus tools** (init, /sp.specify, /sp.plan, /sp.tasks)
3. **Write SMART acceptance criteria** that prevent misinterpretation
4. **Recognize spec quality** through cascade effects (spec → plan → tasks → code)
5. **Build from specifications** (code that matches intent)
6. **Validate code against specs** (testing strategy)
7. **Write production-grade specifications** for real-world problems
8. **Understand AI collaboration** for specification-driven development

These are not theoretical. Students demonstrate them through the mini-projects.

---

## Connection to Constitution

This chapter aligns with core constitutional principles:

- **Principle 1: Specification-First Development** — Chapter is entirely built on spec-first methodology
- **Principle 2: AI as Co-Reasoning Partner** — Companion frames as thinking partner throughout
- **Principle 3: Validation-First Safety** — Mini-Project 1 includes test suite and validation checklist
- **Principle 4: Bilingual Development** — Mini-Project 1 uses Python; sets up for TypeScript later
- **Principle 5: Learning by Building** — Students build real specs and code, not toy examples

---

## Next Steps (Chapter 27)

Chapter 27 ("Real-World Spec-Kit Workflows") applies these skills to professional development scenarios:
- Multi-person teams using specs
- Specification handoff between roles
- Iterative refinement in team settings
- Specification-driven team collaboration

Students complete Chapter 26 ready to work on real teams with real specifications.

---

## Implementation Notes

### For Instructors

- Students should have access to their AI companion tool (Claude Code, ChatGPT, Gemini CLI)
- Each lesson builds on previous ones; do not skip or reorder
- Mini-projects are NOT optional; they demonstrate mastery
- Encourage students to save all artifacts (specs, code, tests) in a portfolio

### For Self-Study

- This chapter is designed for self-directed learning with AI collaboration
- Read each lesson once, then do the "Try With AI" section
- Complete mini-projects fully before moving to next chapter
- Save your specifications and code; refer to them in future chapters

---

## Validation Checklist (Instructor/QA Review)

- [ ] All 7 lessons include "Try With AI" sections with concrete prompts
- [ ] Mini-Projects 1 & 2 have clear deliverables
- [ ] Spec examples are realistic and complete
- [ ] Code examples (Mini-Project 1) have type hints and docstrings
- [ ] Language is accessible (technical, but no unnecessary jargon)
- [ ] Progressive complexity: Lessons 1-4 foundational, Lessons 5-7 integration, Mini-Projects applied
- [ ] AI collaboration framed as partnership, not outsourcing
- [ ] Validation steps explicit (tests, checklists, companion feedback)
- [ ] Real-world context (not toy problems except calculator)
- [ ] Artifact-focused (students leave with specs, code, tests)

---

## Chapter Metadata

| Attribute | Value |
|-----------|-------|
| Chapter Number | 26 |
| Part | 5: Spec-Kit Plus Methodology |
| Estimated Duration | 20-26 hours (7 lessons + 2 mini-projects) |
| Complexity Tier | Intermediate-Advanced |
| Prerequisites | Chapters 1-25 |
| Target Audience | Aspiring developers, developers learning AI collaboration |
| Hands-On | 100% (no lectures) |
| AI Collaboration | Yes (essential throughout) |
| Code Required | Yes (Python, Mini-Project 1) |
| Deliverables | Specs, code, tests, validation checklists |

---

**Chapter Status**: Complete and ready for publication review

**Quality Assurance**: All lessons follow AI-native pedagogy principles; all mini-projects include real artifacts; all validation standards met.
