# Tasks: Chapter 8 - Git & GitHub for AI-Driven Development

**Input**: Design documents from `/specs/001-chapter-8-git-github/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Tests are NOT requested in this feature specification. This is an educational content project, not a software implementation project.

**Organization**: Tasks are grouped by lesson (content unit) to enable independent implementation and delivery of each lesson.

## Format: `- [ ] [ID] [P?] [Lesson] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Lesson]**: Which lesson this task belongs to (e.g., L1, L2, L3, L4, L5)
- Include exact file paths in descriptions

## Path Conventions

- **Book content**: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/`
- **Spec artifacts**: `specs/001-chapter-8-git-github/`

---

## Phase 1: Chapter Foundation

**Purpose**: Create chapter overview and structure that ties all lessons together

- [X] T001 Create chapter README.md in book-source/docs/02-AI-Tool-Landscape/08-git-and-github/README.md
- [X] T002 Review constitution and output styles in .specify/memory/constitution.md and .claude/output-styles/lesson.md

**Checkpoint**: Chapter structure ready - lesson implementation can now begin

---

## Phase 2: User Story 1 - Creating Safe Checkpoints Before AI Changes (Priority: P1) 🎯 MVP

**Goal**: Learners can create safe checkpoints before letting AI tools modify code, and successfully rollback if needed

**Independent Test**: Learner can create a checkpoint commit, make changes (simulated or AI-generated), and successfully roll back to the checkpoint using `git reset --hard HEAD~1`

**Mapped to Lessons**: Lesson 1 (Why), Lesson 2 (Basic commands), Lesson 3 (Checkpoints and rollback)

### L1: Conceptual Foundation (Why Git Matters)

- [X] T003 [L1] Write Lesson 1 content (Why Git Matters) in book-source/docs/02-AI-Tool-Landscape/08-git-and-github/01-why-git-matters.md
- [X] T004 [L1] Create 2-3 reflection prompts for Lesson 1
- [X] T005 [L1] Add 4-5 real-world examples of AI development with Git safety net

### L2: Essential Git Workflow (Installation and Basic Commands)

- [X] T006 [L2] Write Lesson 2 Part I: Installation & Setup in book-source/docs/02-AI-Tool-Landscape/08-git-and-github/02-git-essentials.md
- [X] T007 [L2] Write Lesson 2 Part II: Core Workflow (status → add → commit → push)
- [X] T008 [L2] Write Lesson 2 Part III: Three-Stage Concept (working directory → staging → repository)
- [X] T009 [L2] Write Lesson 2 Part IV: Reading Git Output
- [X] T010 [L2] Write Lesson 2 Part V: Commit Messages with AI Attribution
- [X] T011 [L2] Create 5 hands-on exercises for Lesson 2 (install, configure, init, commit, log)
- [X] T012 [L2] Create 8-10 question self-assessment for Lesson 2

### L3: Safe Experimentation (Checkpoints and Rollback)

- [ ] T013 [L3] Write Lesson 3 Part I: Checkpoint Pattern in book-source/docs/02-AI-Tool-Landscape/08-git-and-github/03-safe-experimentation.md
- [ ] T014 [L3] Write Lesson 3 Part II: Branch-Based Experimentation
- [ ] T015 [L3] Write Lesson 3 Part III: Undoing Changes (reset, revert)
- [ ] T016 [L3] Write Lesson 3 Part IV: Merging Branches
- [ ] T017 [L3] Write Lesson 3 Part V: Stashing
- [ ] T018 [L3] Create 6 hands-on exercises for Lesson 3 (checkpoint, branch, switch, merge, rollback, conflict resolution)
- [ ] T019 [L3] Create 8-10 question self-assessment for Lesson 3

**Checkpoint**: User Story 1 complete - learners can create safe checkpoints and rollback AI changes

---

## Phase 3: User Story 2 - Collaborating on AI-Generated Code via Pull Requests (Priority: P2)

**Goal**: Learners can share AI-generated features with teammates for code review using pull requests

**Independent Test**: Learner can create a feature branch, push to GitHub, create a PR with description, simulate review comments, address feedback, and merge

**Mapped to Lessons**: Lesson 4 (Pull Requests and Team Collaboration)

### L4: Pull Requests and Team Collaboration

- [ ] T020 [L4] Write Lesson 4 Part I: Understanding PRs in book-source/docs/02-AI-Tool-Landscape/08-git-and-github/04-pull-requests.md
- [ ] T021 [L4] Write Lesson 4 Part II: Creating a PR (push, GitHub UI, PR description)
- [ ] T022 [L4] Write Lesson 4 Part III: Reviewing Code
- [ ] T023 [L4] Write Lesson 4 Part IV: Iteration and Feedback
- [ ] T024 [L4] Write Lesson 4 Part V: Merging on GitHub
- [ ] T025 [L4] Write Lesson 4 Part VI: Handling PR Conflicts
- [ ] T026 [L4] Create 7 hands-on exercises for Lesson 4 (create repo, push, branch, create PR, review, iterate, merge)
- [ ] T027 [L4] Create 8-10 question self-assessment for Lesson 4

**Checkpoint**: User Story 2 complete - learners can collaborate via pull requests

---

## Phase 4: User Story 3 - Using Natural Language Prompts for Git Workflows (Priority: P3)

**Goal**: Learners can use Claude Code or Gemini CLI to execute Git operations via natural language instead of memorizing command syntax

**Independent Test**: Learner can provide natural language prompts to AI CLI tools and verify correct Git commands are executed (at least 10 different operations)

**Mapped to Lessons**: Lesson 5 (Natural Language Prompts for Git)

### L5: Natural Language Prompts (Convenience Layer)

- [ ] T028 [L5] Write Lesson 5 Part I: Why Natural Language Prompts in book-source/docs/02-AI-Tool-Landscape/08-git-and-github/05-natural-language-prompts.md
- [ ] T029 [L5] Write Lesson 5 Part II: Command-to-Prompt Translation (10+ examples)
- [ ] T030 [L5] Write Lesson 5 Part III: Complex Workflow Prompts
- [ ] T031 [L5] Write Lesson 5 Part IV: Troubleshooting Prompts
- [ ] T032 [L5] Write Lesson 5 Part V: Best Practices for AI CLI Conversations
- [ ] T033 [L5] Create 6 hands-on exercises for Lesson 5 (concept explanation, branch creation, history, conflict understanding, conflict resolution, complex workflow)
- [ ] T034 [L5] Create 5-8 question self-assessment for Lesson 5

**Checkpoint**: User Story 3 complete - learners can use natural language prompts for Git operations

---

## Phase 5: User Story 4 - Understanding Git History and Blame for AI Changes (Priority: P4)

**Goal**: Learners can track which AI tool or session made specific changes using git log and git blame

**Independent Test**: Learner can create commits with AI attribution, then use `git log` and `git blame` to trace authorship and changes

**Mapped to Lessons**: Integrated into Lesson 2 (commit messages with AI attribution) and Lesson 5 (prompts for git log and git blame)

**Note**: This user story is addressed through content in earlier lessons rather than a dedicated lesson.

### Content Integration Tasks

- [ ] T035 [P] [L2] Ensure Lesson 2 Part V comprehensively covers AI attribution patterns in commit messages
- [ ] T036 [P] [L5] Ensure Lesson 5 Part II includes prompts for `git log` with AI attribution filtering
- [ ] T037 [P] [L5] Ensure Lesson 5 Part II includes prompts for `git blame` to trace AI contributions

**Checkpoint**: User Story 4 complete - learners can track AI contributions over time

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Quality improvements, references, and comprehensive project

- [ ] T038 [P] Create end-of-chapter comprehensive project combining all skills in book-source/docs/02-AI-Tool-Landscape/08-git-and-github/06-comprehensive-project.md
- [ ] T039 [P] Create Quick Reference Card (15-20 essential commands) in book-source/docs/02-AI-Tool-Landscape/08-git-and-github/reference-card.md
- [ ] T040 [P] Create Common Scenarios Reference (5-8 AI development scenarios) in book-source/docs/02-AI-Tool-Landscape/08-git-and-github/common-scenarios.md
- [ ] T041 Platform testing: verify all Git commands on Windows 10+, macOS 10.15+, Linux
- [ ] T042 Platform testing: verify GitHub workflows with free-tier account
- [ ] T043 Platform testing: test natural language prompts with Claude Code and Gemini CLI
- [ ] T044 [P] Accessibility check: verify grade 7 reading level, no gatekeeping language
- [ ] T045 [P] Style guide compliance: verify lesson.md output style followed
- [ ] T046 Constitution alignment validation: verify AI-first, show-then-explain, accessible
- [ ] T047 Cross-chapter coherence: verify integration with Chapters 5-7, bridge to Part 3
- [ ] T048 Final editorial review: grammar, flow, completeness, no placeholders

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Foundation)**: No dependencies - can start immediately
- **Phase 2 (User Story 1)**: Depends on Phase 1 completion
- **Phase 3 (User Story 2)**: Depends on Phase 2 completion (learners need basic Git skills first)
- **Phase 4 (User Story 3)**: Depends on Phases 2-3 completion (prompts assume understanding of core concepts)
- **Phase 5 (User Story 4)**: Can proceed in parallel with Phases 2-4 (content integration tasks)
- **Phase 6 (Polish)**: Depends on all user story phases being complete

### Lesson Dependencies

- **Lesson 1 (Why)**: Can start after Phase 1 - No dependencies on other lessons
- **Lesson 2 (Essentials)**: Depends on Lesson 1 (motivation established)
- **Lesson 3 (Safe Experimentation)**: Depends on Lesson 2 (basic workflow understood)
- **Lesson 4 (Pull Requests)**: Depends on Lesson 3 (branching and merging understood)
- **Lesson 5 (Natural Language)**: Depends on Lessons 2-4 (core concepts understood, prompts are convenience layer)

### Within Each Lesson

- Content sections can be written sequentially (Part I → Part II → Part III...)
- Exercises must follow content completion (can't write exercises before content)
- Assessments must follow exercises (can't assess what hasn't been practiced)

### Parallel Opportunities

- Phase 6 tasks marked [P] can run in parallel (different files, no dependencies)
- User Story 4 content integration tasks (T035-T037) can run in parallel with each other
- Platform testing tasks (T041-T043) can run in parallel
- Accessibility, style, constitution, and coherence checks (T044-T047) can run in parallel

---

## Parallel Example: Phase 6 (Polish)

```bash
# Launch all polish tasks together:
Task: "Create comprehensive project in 06-comprehensive-project.md"
Task: "Create Quick Reference Card in reference-card.md"
Task: "Create Common Scenarios Reference in common-scenarios.md"
Task: "Accessibility check: grade 7 reading level"
Task: "Style guide compliance verification"
```

---

## Implementation Strategy

### MVP First (User Story 1: Safe Checkpoints)

1. Complete Phase 1: Chapter Foundation
2. Complete Phase 2: User Story 1 (Lessons 1-3)
3. **STOP and VALIDATE**: Test Lesson 1-3 independently
4. Learners can now create safe checkpoints and rollback - **Core value delivered**

### Incremental Delivery

1. MVP (Lessons 1-3) → Learners have safety net for AI development
2. Add User Story 2 (Lesson 4) → Learners can collaborate via PRs
3. Add User Story 3 (Lesson 5) → Learners have natural language convenience layer
4. Add User Story 4 (integrated) → Learners can track AI contributions
5. Add Phase 6 (Polish) → Comprehensive project and references
6. Each phase adds value without breaking previous lessons

### Sequential Lesson Strategy

Since this is an educational content project:

1. Write Lesson 1 (foundation) → Review → Approve
2. Write Lesson 2 (essentials) → Review → Approve
3. Write Lesson 3 (experimentation) → Review → Approve
4. Write Lesson 4 (PRs) → Review → Approve
5. Write Lesson 5 (prompts) → Review → Approve
6. Create polish artifacts (project, references) → Review
7. Quality checks (platform testing, accessibility, etc.) → Final review

---

## Notes

- [P] tasks = different files, no dependencies
- [Lesson] label maps task to specific lesson for traceability
- Each lesson should be independently completable and reviewable
- Commit after each lesson or logical section completion
- Stop at any checkpoint to validate lesson independently
- This is **educational content**, not software - no automated tests needed
- Platform testing means **manually testing commands** on different OS platforms
- Natural language prompts must be tested with **actual AI tools** (Claude Code, Gemini CLI)

---

## Success Criteria (from spec.md)

| Success Criteria | Addressed By | Measurement |
|------------------|--------------|-------------|
| SC-001: Create repo and commit in 5 min | Lesson 2, Exercise 3-4 | Timed exercise walkthrough |
| SC-002: Safe checkpoint and rollback | Lesson 3, Exercises 1, 5 | Create checkpoint, rollback, verify |
| SC-003: Branch workflow without data loss | Lesson 3, Exercises 2-4 | Create branch, edit, merge, verify |
| SC-004: Create PR, address feedback, merge | Lesson 4, Exercises 1-7 | Full GitHub PR workflow |
| SC-005: Translate 10+ commands to prompts | Lesson 5, Part II | 10+ command→prompt examples |
| SC-006: Understand when to commit | Lesson 2-3, Reflections | Self-assessment questions |
| SC-007: End-of-chapter project (90% target) | Phase 6, T038 | Comprehensive project combining all skills |
| SC-008: Identify commands for 5 scenarios | Phase 6, T040 | Common scenarios reference |

---

## Estimated Effort

- **Phase 1 (Foundation)**: 1-2 hours
- **Phase 2 (User Story 1)**: 8-10 hours (3 lessons with exercises and assessments)
- **Phase 3 (User Story 2)**: 4-5 hours (1 lesson with exercises and assessment)
- **Phase 4 (User Story 3)**: 3-4 hours (1 lesson with exercises and assessment)
- **Phase 5 (User Story 4)**: 1-2 hours (content integration)
- **Phase 6 (Polish)**: 4-6 hours (project, references, quality checks)

**Total Estimated Effort**: 21-29 hours (assumes sequential lesson-by-lesson implementation)

---

## Follow-Up Sequence

After task generation completes:

1. **Begin MVP Implementation**: Start with Phase 1 and Phase 2 (User Story 1)
2. **Human Review**: After each lesson is drafted, human reviews and provides feedback
3. **Iterative Delivery**: Complete each user story phase and validate before moving to next
4. **Quality Assurance**: Phase 6 ensures publication readiness
5. **Technical Validation**: Use technical-reviewer agent after all content complete
