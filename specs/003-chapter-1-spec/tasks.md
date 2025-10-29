---
description: "Task list for Chapter 1 implementation - Welcome to Agent-Native Education"
---

# Tasks: Chapter 1 - Welcome to Agent-Native Education

**Input**: Design documents from `/specs/003-chapter-1-spec/`
- **spec.md**: 4 user stories (P1, P2) with acceptance criteria
- **plan.md**: 6 lessons with learning objectives, content outlines, pedagogical approach
- **README.md**: Chapter-level integration guide

**Implementation Model**: Lesson-writer agent implements all lessons with **human review checkpoints after each lesson**. Main chapter README finalized by human after all lessons complete. Technical-reviewer subagent validates complete chapter.

**Organization**: Tasks are grouped by lesson to enable independent implementation, review, and refinement of each lesson. Each lesson can be iterated on based on human feedback before proceeding to the next.

---

## Format: `[ID] [P?] [Lesson] Description`

- **[ID]**: Task ID (T001-T048)
- **[P]**: Can run in parallel (content sections, visuals can be created simultaneously)
- **[Lesson]**: Which lesson this task belongs to (e.g., L1, L2, L3, L4, L5, L6)
- **File paths**: Exact output locations for lesson content, visuals, and examples

---

## Phase 1: Setup (Chapter Initialization & Framework)

**Purpose**: Initialize chapter structure, create content framework, and prepare for lesson implementation

- [ ] T001 Create chapter directory structure: `book-source/docs/01-Introducing-AI-Driven-Development/lessons/` with subdirectories L1-L6
- [ ] T002 Create lesson template files with standard header/footer structure
- [ ] T003 Create chapter-level visualization assets directory: `book-source/docs/01-Introducing-AI-Driven-Development/assets/diagrams/`
- [ ] T004 Create chapter-level examples directory: `book-source/docs/01-Introducing-AI-Driven-Development/assets/examples/`
- [ ] T005 Create chapter-level appendix for all term definitions: `book-source/docs/01-Introducing-AI-Driven-Development/appendix-glossary.md`

---

## Phase 2: Foundational (Shared Resources)

**Purpose**: Create cross-lesson assets that multiple lessons depend on

**⚠️ CRITICAL**: These foundational resources must be complete before lesson writing begins

- [ ] T006 [P] Create "Musician vs. Conductor" analogy asset (description + SVG diagram) in `assets/diagrams/musician-vs-conductor.md`
- [ ] T007 [P] Create "Snakes and Ladders" competitive pattern diagram in `assets/diagrams/snakes-ladders.md`
- [ ] T008 [P] Create "Agent-Native Education" three-roles diagram in `assets/diagrams/agent-native-education.md`
- [ ] T009 [P] Create "Agent Orchestrator Dimensions" diagram in `assets/diagrams/agent-orchestrator-roles.md`
- [ ] T010 [P] Create "Book Journey (Parts 1-13)" progression diagram in `assets/diagrams/book-journey.md`
- [ ] T011 [P] Compile solo builder examples with concrete numbers in `assets/examples/solo-builders.md`
- [ ] T012 [P] Compile domain-specific vertical examples (finance, healthcare, education, legal) in `assets/examples/vertical-markets.md`
- [ ] T013 [P] Create prompt-response code pattern examples in `assets/examples/code-patterns.md`

**Checkpoint**: All foundational visuals and examples ready. Lesson writers can now proceed with lesson content.

---

## Phase 3: Lesson 1 - The Paradigm Shift: From Fear to Opportunity

**Goal**: Establish emotional safety and psychological foundation. Readers understand AI amplifies rather than replaces human capability.

**Success Criteria**: Readers articulate that AI is a partner, not competition. Reader feels motivated, not threatened.

**Duration**: 40-50 minutes | **Word Count**: 600-800 words

**Domain Skills Applied**: learning-objectives, technical-clarity, ai-augmented-teaching, book-scaffolding

### Lesson 1 Content Implementation

- [ ] T014 [L1] Write Lesson 1 opening (hook): Acknowledge "Will AI replace me?" fear directly in `lessons/01-paradigm-shift.md` (150-200 words)
- [ ] T015 [L1] Write Lesson 1 reframe section: AI as amplifier, not replacement. Include musician vs. conductor analogy (200-250 words)
- [ ] T016 [P] [L1] Integrate solo builder example 1 with concrete numbers (ARR, team size) in Lesson 1 content
- [ ] T017 [P] [L1] Integrate solo builder example 2 (different domain) in Lesson 1 content
- [ ] T018 [L1] Write Lesson 1 new role introduction: Preview "agent orchestrator" concept (100-150 words)
- [ ] T019 [L1] Write Lesson 1 closing: Establish psychological safety and sense of opportunity (100-150 words)
- [ ] T020 [L1] Add reflection exercise to Lesson 1: "What about your current skills could be amplified by AI?" with clear prompt
- [ ] T021 [L1] Embed musician vs. conductor diagram in Lesson 1 with alt text and caption

### Lesson 1 Assessment

- [ ] T022 [L1] Create formative assessment for Lesson 1 (implicit: If reader continues, they've accepted the reframe)
- [ ] T023 [L1] Add learning outcomes summary at end of lesson (reference learning objectives from plan)

**Checkpoint: Lesson 1 complete and ready for human review**

---

## Phase 4: Lesson 2 - The $3 Trillion Market and Technological Transformation

**Goal**: Ground the paradigm shift in market reality. Readers understand the economic scale and technological forces enabling AI autonomy.

**Success Criteria**: Readers can name and explain 3+ major technological/economic shifts from AI Coding Revolution Paper. Readers grasp distinction between copilots (assistance) and agents (autonomy).

**Duration**: 60-75 minutes | **Word Count**: 1,000-1,200 words

**Domain Skills Applied**: concept-scaffolding, technical-clarity, book-scaffolding, code-example-generator (preview)

### Lesson 2 Content Implementation

- [ ] T024 [L2] Write Lesson 2 opening: The scale ($3 trillion industry, 30 million developers) in `lessons/02-market-transformation.md` (150-200 words)
- [ ] T025 [L2] Write Lesson 2 subsection 1: The Shift (copilot → agent, assistance → autonomy) with real examples (200-250 words)
- [ ] T026 [P] [L2] Write Lesson 2 subsection 2: Context Engineering (how AI maintains understanding of large codebases) (150-200 words)
- [ ] T027 [P] [L2] Write Lesson 2 subsection 3: Autonomous Agents (examples of agents implementing features) (150-200 words)
- [ ] T028 [P] [L2] Write Lesson 2 subsection 4: Sandbox Execution (infrastructure for automated testing/deployment) (150-200 words)
- [ ] T029 [P] [L2] Write Lesson 2 subsection 5: Infrastructure Evolution (version control, cloud-native systems for generated code) (150-200 words)
- [ ] T030 [L2] Write Lesson 2 closing: Why this moment is genuine (not hype), connection to Lesson 1 (100-150 words)
- [ ] T031 [L2] Integrate timeline diagram: "The Evolution of AI Coding" (Copilots 2023 → Agents 2024 → Context Engineering 2025)
- [ ] T032 [L2] Integrate diagram: "4 Enablers of AI Agent Autonomy" with brief explanation of each
- [ ] T033 [L2] Embed code pattern examples (prompt-response showing agent vs. copilot patterns) with explanations
- [ ] T034 [L2] Add reference citations to AI Coding Revolution Paper for all major claims

### Lesson 2 Assessment

- [ ] T035 [L2] Create formative comprehension check: "What are 2 differences between AI copilots and autonomous agents?" (early in lesson)
- [ ] T036 [L2] Add learning outcomes summary at end of lesson

**Checkpoint: Lesson 2 complete and ready for human review**

---

## Phase 5: Lesson 3 - The "Snakes and Ladders" Competitive Pattern and Vertical Opportunities

**Goal**: Help readers recognize the vertical market opportunity and see themselves as potential builders.

**Success Criteria**: Readers can name 1+ vertical market where they could build. Readers understand why Layer 3 (verticals) is the opportunity.

**Duration**: 50-60 minutes | **Word Count**: 800-1,000 words

**Domain Skills Applied**: concept-scaffolding, book-scaffolding, technical-clarity, exercise-designer

### Lesson 3 Content Implementation

- [ ] T037 [L3] Write Lesson 3 opening: Introduce "Snakes and Ladders" pattern in `lessons/03-vertical-opportunities.md` (100-150 words)
- [ ] T038 [L3] Write Lesson 3 section 1: Why Layers 1-2 have limited winners (hyperscaler consolidation, commoditization) (200-250 words)
- [ ] T039 [L3] Write Lesson 3 section 2: Why Layer 3 is unlimited (domain integration, specialized models, system connections) (150-200 words)
- [ ] T040 [P] [L3] Write Lesson 3 vertical example 1: Finance (compliance-aware trading agents) (150-200 words)
- [ ] T041 [P] [L3] Write Lesson 3 vertical example 2: Healthcare (patient-integrated diagnostic agents) (150-200 words)
- [ ] T042 [P] [L3] Write Lesson 3 vertical example 3: Education (adaptive learning agents with pedagogical knowledge) (150-200 words)
- [ ] T043 [P] [L3] Write Lesson 3 vertical example 4: Legal (contract analysis and generation agents) (150-200 words)
- [ ] T044 [L3] Write Lesson 3 section 3: What creates defensible advantage (expertise + AI + integration + fine-tuned models) (150-200 words)
- [ ] T045 [L3] Write Lesson 3 closing: "You have domain expertise; AI gives you the tools" (100-150 words)
- [ ] T046 [L3] Embed "Snakes and Ladders" diagram with visual clarity (3 layers with examples and winner dynamics)
- [ ] T047 [L3] Create visualization: Domain-specific agent capabilities (one example per domain)

### Lesson 3 Assessment

- [ ] T048 [L3] Create reflection exercise: "Identify one domain you know well. What problem could a vertical agentic solution solve?" with clear prompt
- [ ] T049 [L3] Add learning outcomes summary at end of lesson

**Checkpoint: Lesson 3 complete and ready for human review**

---

## Phase 6: Lesson 4 - Agent-Native Education: Learning WITH AI

**Goal**: Set expectations for the pedagogical model and AI's active role throughout the book.

**Success Criteria**: Readers understand "agent-native education" definition. Readers can explain WITH vs. FROM distinction. 85%+ understand what to expect.

**Duration**: 50-65 minutes | **Word Count**: 600-800 words

**Domain Skills Applied**: ai-augmented-teaching, learning-objectives, technical-clarity, book-scaffolding

### Lesson 4 Content Implementation

- [ ] T050 [L4] Write Lesson 4 opening: Define "agent-native" = AI participates actively in `lessons/04-agent-native-education.md` (100-150 words)
- [ ] T051 [L4] Write Lesson 4 subsection 1: Co-learner role (AI explores with you, asks questions, suggests directions) (150-200 words)
- [ ] T052 [L4] Write Lesson 4 subsection 2: Collaborator role (AI shapes ideas, refines specs, suggests architectures) (150-200 words)
- [ ] T053 [L4] Write Lesson 4 subsection 3: Creative partner role (AI amplifies capability, generates code, you evaluate) (150-200 words)
- [ ] T054 [L4] Write Lesson 4 critical section: "Learning WITH AI" vs. "Learning FROM AI" distinction with examples (200-250 words)
- [ ] T055 [L4] Write Lesson 4 section: How this book embodies agent-native education (specs, code gen, evaluation, exercises) (150-200 words)
- [ ] T056 [L4] Write Lesson 4 closing: What to expect (specifications, directing AI partners, understanding reasoning) (100-150 words)
- [ ] T057 [L4] Embed diagram: "Agent-Native Education" showing three roles with examples
- [ ] T058 [L4] Embed infographic: "WITH vs. FROM" comparison (two columns, visual contrast)
- [ ] T059 [L4] Add prompt-response examples for each role (co-learner, collaborator, creative partner)

### Lesson 4 Assessment

- [ ] T060 [L4] Create formative comprehension check: "Explain the difference between learning WITH AI and learning FROM AI."
- [ ] T061 [L4] Add learning outcomes summary at end of lesson

**Checkpoint: Lesson 4 complete and ready for human review**

---

## Phase 7: Lesson 5 - Your Role as Agent Orchestrator

**Goal**: Unify all previous lessons and establish the reader's new professional identity.

**Success Criteria**: Readers can explain "agent orchestrator" and 4 dimensions. Readers understand why these skills transcend syntax knowledge.

**Duration**: 40-55 minutes | **Word Count**: 500-700 words

**Domain Skills Applied**: concept-scaffolding, book-scaffolding, exercise-designer

### Lesson 5 Content Implementation

- [ ] T062 [L5] Write Lesson 5 opening: Unify into orchestrator role in `lessons/05-agent-orchestrator.md` (100-150 words)
- [ ] T063 [L5] Write Lesson 5 dimension 1: Specification writer (clear requirements precede implementation) (100-150 words)
- [ ] T064 [L5] Write Lesson 5 dimension 2: System architect (design intelligent system topology) (100-150 words)
- [ ] T065 [L5] Write Lesson 5 dimension 3: Agent director (guide AI partners toward good solutions) (100-150 words)
- [ ] T066 [L5] Write Lesson 5 dimension 4: Quality arbiter (evaluate and refine AI-generated work) (100-150 words)
- [ ] T067 [L5] Write Lesson 5 section: Why these skills are more valuable than syntax knowledge (100-150 words)
- [ ] T068 [L5] Write Lesson 5 section: How agent orchestrator role applies across domains (100-150 words)
- [ ] T069 [L5] Write Lesson 5 closing: Synthesis and forward look to Part 2 (100-150 words)
- [ ] T070 [L5] Embed diagram: "Agent Orchestrator Dimensions" (4 dimensions with brief descriptions)

### Lesson 5 Assessment

- [ ] T071 [L5] Create application exercise: Role-play as agent orchestrator evaluating AI-generated solution (with prompt and example scenario)
- [ ] T072 [L5] Add learning outcomes summary at end of lesson

**Checkpoint: Lesson 5 complete and ready for human review**

---

## Phase 8: Lesson 6 - Preview of the Journey Ahead

**Goal**: Context-set readers for Parts 2-7 and show the progression of their learning.

**Success Criteria**: Readers understand book structure and progression. Readers feel prepared for Part 2.

**Duration**: 30-40 minutes | **Word Count**: 400-500 words

**Domain Skills Applied**: book-scaffolding, learning-objectives, technical-clarity

### Lesson 6 Content Implementation

- [ ] T073 [L6] Write Lesson 6 opening: Chapter 1 foundation in place, now preview the journey in `lessons/06-preview-journey.md` (100-150 words)
- [ ] T074 [L6] Write Lesson 6 section: Part 1 overview and Chapters 2-5 preview (100-150 words)
- [ ] T075 [L6] Write Lesson 6 section: Part 2 (AI Tool Landscape) preview (75-100 words)
- [ ] T076 [L6] Write Lesson 6 section: Parts 3-7 progression overview (Python, agentic systems, MCP, TypeScript, etc.) (150-200 words)
- [ ] T077 [L6] Write Lesson 6 section: How agent orchestrator role develops through the book (100-150 words)
- [ ] T078 [L6] Write Lesson 6 closing: "You're ready for Part 2" (75-100 words)
- [ ] T079 [L6] Embed diagram: "Book Journey" showing all 13 parts with chapter counts
- [ ] T080 [L6] Create simplified visual: Learning arc from "code writer" to "super orchestrator" across 13 parts

### Lesson 6 Assessment

- [ ] T081 [L6] Create reflection exercise: "Which part are you most excited to explore?" (open-ended, personal)
- [ ] T082 [L6] Add learning outcomes summary at end of lesson

**Checkpoint: Lesson 6 complete and ready for human review**

---

## Phase 9: Chapter Integration & Summative Assessment

**Purpose**: Connect all lessons into cohesive chapter and create summative assessments

**Prerequisite**: All 6 lessons complete and reviewed

- [ ] T083 Update chapter navigation: Add links between lessons in each lesson's intro/conclusion
- [ ] T084 Create chapter-level comprehension check (4 questions covering all major concepts):
  - Question 1: "What does 'agent-native education' mean?"
  - Question 2: "Name 2 reasons why this moment in software development is unique"
  - Question 3: "Explain the 'snakes and ladders' pattern in your own words"
  - Question 4: "What is an 'agent orchestrator' and what do they do?"
- [ ] T085 Finalize chapter README.md with:
  - Main chapter learning outcomes (consolidate from all 6 lessons)
  - Lesson summaries and how each contributes to chapter success
  - Integration with Part 1 and Parts 2-7
  - Domain skills used throughout (all 8 explicitly referenced)
  - Success metrics and how they're measured
  - Constitutional alignment (Principles 1, 5, 8, 9)
- [ ] T086 Add chapter-level reflection exercise at end: "Identify an industry or domain you know well. Describe one problem in that domain that could be solved by a vertical agentic solution. What would you need to learn to build it?"
- [ ] T087 Create chapter glossary (append to appendix): All terms introduced with definitions
- [ ] T088 Add accessibility compliance review: Alt text on all diagrams, clear language, high contrast visuals

**Checkpoint: Chapter fully integrated with all assessments in place**

---

## Phase 10: Technical Review & Polish

**Purpose**: Validate chapter quality and make final refinements

**Prerequisite**: Chapter integration complete

- [ ] T089 Invoke technical-reviewer subagent to validate:
  - Technical correctness (no false claims about AI, technology)
  - Pedagogical effectiveness (clear learning progression, effective scaffolding)
  - Constitution alignment (Principles 1, 5, 8, 9 verified)
  - Code quality (if examples included, all have type hints, follow standards)
  - Content accessibility (no gatekeeping language, multiple entry points)
- [ ] T090 Address any feedback from technical review
- [ ] T091 Final proofreading and copyedit for clarity
- [ ] T092 Verify all cross-references (to other chapters, to Part 1 spec, to Constitution) are active
- [ ] T093 Create final chapter summary statistics:
  - Total word count
  - Reading time estimate
  - Lesson completion times
  - Domain skills coverage
  - Success metrics summary

**Final Checkpoint: Chapter 1 ready for publication**

---

## Dependency Graph

```
Setup (T001-T005)
    ↓
Foundational Assets (T006-T013) — [All must complete before lessons begin]
    ↓
Lesson 1 (T014-T023) ——→ Human Review Checkpoint 1
    ↓
Lesson 2 (T024-T036) ——→ Human Review Checkpoint 2
    ↓
Lesson 3 (T037-T049) ——→ Human Review Checkpoint 3
    ↓
Lesson 4 (T050-T061) ——→ Human Review Checkpoint 4
    ↓
Lesson 5 (T062-T072) ——→ Human Review Checkpoint 5
    ↓
Lesson 6 (T073-T082) ——→ Human Review Checkpoint 6
    ↓
Chapter Integration (T083-T088) ——→ All lessons reviewed and approved
    ↓
Technical Review (T089-T093) ——→ Technical-reviewer subagent validation
    ↓
Publication Ready
```

---

## Parallel Opportunities

**Setup Phase** (T001-T005): All tasks can run in parallel (independent directories)

**Foundational Assets** (T006-T013): All visual and example creation can run in parallel:
- T006, T007, T008, T009, T010 (diagrams) — independent files, can run simultaneously
- T011, T012, T013 (examples) — independent files, can run simultaneously

**Lesson Implementation**: After foundational assets complete, lessons can be partially parallelized:
- Lesson 1 content writing (T014-T023) — some tasks parallelizable (T016, T017 can run simultaneously)
- Lesson 2 content writing (T024-T036) — subsections (T026-T029) can run in parallel
- Lesson 3 examples (T040-T043) — vertical examples can run in parallel
- Lessons 4, 5, 6 — dimensions and sections can run partially in parallel

**Recommended MVP Scope**: Lessons 1-2 + Foundational Assets
- Establishes emotional foundation + market grounding
- Demonstrates pedagogical approach
- Ready for first human review
- Enables feedback before implementing Lessons 3-6

---

## Success Criteria Mapping

| Success Criterion | Addressed in Lessons | Measured By |
|---|---|---|
| SC-001: 90%+ articulate AI amplifies | L1, L5 | Reflection exercise (L1) + Comprehension check (L4) |
| SC-002: 85%+ explain 3+ shifts | L2 | Comprehension check (L2) + Formative check (L2) |
| SC-003: 80%+ identify vertical market | L3 | Reflection exercise (L3) + Chapter-level exercise |
| SC-004: 85%+ understand agent-native ed | L4 | Comprehension check (L4) + Formative check (L4) |
| SC-005: 90%+ feel motivated | L1, L5 | Implicit (L1 tone) + Reflection exercise (L5) |
| SC-006: 80%+ explain orchestrator | L5 | Application exercise (L5) + Chapter comprehension |
| SC-007: Complete without confusion | All | Chapter-level comprehension check (4 questions) |
| SC-008: 75%+ ready for Part 2 | L6 | Reflection exercise (L6) + Chapter closing tone |

---

## Implementation Notes

**For Lesson-Writer Agent**:
- Follow the exact word counts and time budgets in plan.md
- Each lesson begins with learning objectives from plan.md
- Apply domain skills listed for each lesson (all 8 skills distributed across 6 lessons)
- Use Show-Then-Explain pedagogy: examples and stories first, then explanations
- Define every term on first use (no gatekeeping language)
- Heavy scaffolding: use analogies, multiple entry points
- Embed diagrams and examples exactly as specified in foundational assets tasks

**For Human Reviewers**:
- After each lesson completes, review for:
  - **Clarity**: Can a reader with no prior AI knowledge understand the content?
  - **Accuracy**: Are all claims verifiable? Are examples realistic?
  - **Engagement**: Is the tone motivating? Does it address psychological concerns?
  - **Pedagogy**: Does it follow Show-Then-Explain? Are there multiple entry points?
  - **Accessibility**: Are there visuals? Are terms defined? Is language inclusive?
- Provide feedback before proceeding to next lesson

**For Technical Reviewer** (Phase 10):
- Validate technical correctness of claims
- Verify pedagogical effectiveness
- Confirm Constitutional alignment (Principles 1, 5, 8, 9)
- Check accessibility compliance
- Validate that all success criteria are measurable and addressed

---

## File Structure (Output)

```
book-source/docs/01-Introducing-AI-Driven-Development/
├── intro.md (updated)
├── lessons/
│   ├── 01-paradigm-shift.md (T014-T023)
│   ├── 02-market-transformation.md (T024-T036)
│   ├── 03-vertical-opportunities.md (T037-T049)
│   ├── 04-agent-native-education.md (T050-T061)
│   ├── 05-agent-orchestrator.md (T062-T072)
│   └── 06-preview-journey.md (T073-T082)
├── assets/
│   ├── diagrams/
│   │   ├── musician-vs-conductor.md
│   │   ├── snakes-ladders.md
│   │   ├── agent-native-education.md
│   │   ├── agent-orchestrator-roles.md
│   │   └── book-journey.md
│   └── examples/
│       ├── solo-builders.md
│       ├── vertical-markets.md
│       └── code-patterns.md
├── appendix-glossary.md (T005)
├── README.md (updated with chapter outcomes, T085)
└── chapter-summary.md (statistics, T093)
```

---

**Total Task Count**: 93 tasks
- Setup: 5 tasks
- Foundational: 8 tasks
- Lesson 1: 9 tasks
- Lesson 2: 13 tasks
- Lesson 3: 13 tasks
- Lesson 4: 12 tasks
- Lesson 5: 11 tasks
- Lesson 6: 10 tasks
- Chapter Integration: 6 tasks
- Technical Review: 5 tasks

**Parallel Opportunities**: 21 tasks (marked with [P])
**Human Review Checkpoints**: 7 (after each lesson + final technical review)
**Recommended MVP**: Lessons 1-2 (22 tasks) + Foundational assets (8 tasks) = 30 tasks for first MVP delivery
