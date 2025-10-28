# Tasks: Colearning Skills for Python Book Agent

**Input**: Design documents from `/specs/001-colearning-skills/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md, contracts/

**Tests**: Integration tests included to validate skill activation and output correctness

**Organization**: Tasks are grouped by user story (6 skills = 6 user stories) to enable independent implementation and testing of each skill.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story (skill) this task belongs to (US1-US6)
- Include exact file paths in descriptions

## Path Conventions

Skills live in `.claude/skills/<skill-name>/` per Claude Code conventions:
- `SKILL.md` - Core instructions
- `reference/` - Documentation (markdown)
- `templates/` - Output structures (YAML/markdown)
- `scripts/` - Validation utilities (Python 3.13+)

Tests live in `tests/` at repository root.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and directory structure for all 6 skills

- [ ] T001 Create base `.claude/skills/` directory structure
- [ ] T002 [P] Create `tests/unit/` directory for script unit tests
- [ ] T003 [P] Create `tests/integration/` directory for skill activation tests
- [ ] T004 [P] Create `tests/fixtures/` directory for test data
- [ ] T005 [P] Configure Python 3.13+ environment with type checking (mypy/pyright)
- [ ] T006 [P] Configure code formatting (black, isort) and linting (ruff/pylint)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared utilities and validation scripts that ALL skills depend on

**⚠️ CRITICAL**: No skill implementation can begin until this phase is complete

- [ ] T007 Create `.claude/skills/_shared/` directory for common utilities
- [ ] T008 [P] Implement `_shared/yaml_loader.py` for YAML file loading with type hints
- [ ] T009 [P] Implement `_shared/markdown_parser.py` for parsing markdown content
- [ ] T010 Implement `_shared/sandbox_executor.py` for isolated Python code execution with security constraints (timeout=5s, temp directory, no network)
- [ ] T011 [P] Write unit tests for sandbox_executor.py in `tests/unit/test_sandbox.py`
- [ ] T012 [P] Implement `_shared/validation_helpers.py` for common validation functions
- [ ] T013 [P] Create base YAML schema validator utility in `_shared/schema_validator.py`

**Checkpoint**: Foundation ready - skill implementation can now begin in parallel

---

## Phase 3: User Story 1 - learning-objectives Skill (Priority: P1) 🎯 MVP

**Goal**: Enable educators to generate measurable learning outcomes aligned with Bloom's taxonomy

**Independent Test**: Educator inputs "Define objectives for Python decorators" → skill activates → produces 3-5 objectives with Bloom's levels, prerequisites, assessment methods

### Implementation for learning-objectives

- [ ] T014 Create `.claude/skills/learning-objectives/` directory structure (reference/, templates/, scripts/)
- [ ] T015 [US1] Create `learning-objectives/SKILL.md` with frontmatter (name: learning-objectives, description with triggers: "define objectives", "learning goals", "prerequisites")
- [ ] T016 [P] [US1] Create `learning-objectives/reference/blooms-taxonomy-programming.md` with Bloom's 6 levels applied to programming
- [ ] T017 [P] [US1] Create `learning-objectives/reference/prerequisite-analysis.md` with prerequisite identification strategies
- [ ] T018 [P] [US1] Create `learning-objectives/reference/assessment-methods.md` with formative/summative/performance assessment types
- [ ] T019 [P] [US1] Create `learning-objectives/templates/learning-objective-template.yml` matching data-model.md schema
- [ ] T020 [US1] Implement `learning-objectives/scripts/validate-objectives.py` to validate objective statements use action verbs and are measurable
- [ ] T021 [US1] Write unit test for validate-objectives.py in `tests/unit/test_validate_objectives.py`
- [ ] T022 [US1] Update SKILL.md with complete instructions (Purpose, When to Activate, Inputs, Process, Output Format, Examples, References)
- [ ] T023 [US1] Add 2-3 example interactions to SKILL.md showing input → output
- [ ] T024 [US1] Write integration test in `tests/integration/test_learning_objectives_activation.py` with varied prompts to validate activation

**Checkpoint**: learning-objectives skill should be fully functional - test by requesting objective generation for a Python topic

---

## Phase 4: User Story 2 - concept-scaffolding Skill (Priority: P1)

**Goal**: Enable educators to break down complex concepts into progressive learning steps with cognitive load management

**Independent Test**: Educator inputs "Scaffold async/await" → skill activates → produces 3-7 steps with cognitive load warnings, prerequisite chains

### Implementation for concept-scaffolding

- [ ] T025 Create `.claude/skills/concept-scaffolding/` directory structure
- [ ] T026 [US2] Create `concept-scaffolding/SKILL.md` with frontmatter (name: concept-scaffolding, description with triggers: "break down", "scaffold", "progressive steps")
- [ ] T027 [P] [US2] Create `concept-scaffolding/reference/cognitive-load-theory.md` with CLT principles (intrinsic/extraneous/germane load, 7±2 chunk limit)
- [ ] T028 [P] [US2] Create `concept-scaffolding/reference/scaffolding-strategies.md` with worked examples, faded guidance, chunking patterns
- [ ] T029 [P] [US2] Create `concept-scaffolding/reference/worked-examples.md` with effective worked example patterns
- [ ] T030 [P] [US2] Create `concept-scaffolding/templates/scaffolding-plan-template.yml` matching data-model.md schema (max 7 steps, max 3 new concepts per step)
- [ ] T031 [US2] Implement `concept-scaffolding/scripts/assess-cognitive-load.py` to calculate load based on new concepts + prerequisites
- [ ] T032 [US2] Write unit test for assess-cognitive-load.py in `tests/unit/test_cognitive_load.py`
- [ ] T033 [US2] Update SKILL.md with complete instructions and examples
- [ ] T034 [US2] Write integration test in `tests/integration/test_concept_scaffolding_activation.py`

**Checkpoint**: concept-scaffolding skill should produce progressive breakdowns with cognitive load analysis

---

## Phase 5: User Story 3 - code-example-generator Skill (Priority: P1)

**Goal**: Enable authors to generate runnable, pedagogically sound code examples validated via sandbox execution

**Independent Test**: Author requests "Generate beginner example for list comprehensions" → skill activates → produces runnable code + explanation (what/how/why) + validation results

### Implementation for code-example-generator

- [ ] T035 Create `.claude/skills/code-example-generator/` directory structure
- [ ] T036 [US3] Create `code-example-generator/SKILL.md` with frontmatter (name: code-example-generator, description with triggers: "generate example", "show code for", "demonstrate")
- [ ] T037 [P] [US3] Create `code-example-generator/reference/python-best-practices.md` with PEP 8 summary, type hints, docstrings
- [ ] T038 [P] [US3] Create `code-example-generator/reference/example-patterns.md` with effective teaching example patterns (simple→complex progression)
- [ ] T039 [P] [US3] Create `code-example-generator/reference/pep8-summary.md` with key PEP 8 style rules
- [ ] T040 [P] [US3] Create `code-example-generator/templates/code-example-template.md` with fenced code block + explanation structure
- [ ] T041 [US3] Implement `code-example-generator/scripts/validate-syntax.py` using AST parsing to check Python syntax
- [ ] T042 [US3] Implement `code-example-generator/scripts/execute-sandbox.py` using subprocess with security constraints (calls _shared/sandbox_executor.py)
- [ ] T043 [US3] Write unit tests for validate-syntax.py in `tests/unit/test_syntax_validator.py`
- [ ] T044 [US3] Write integration tests for execute-sandbox.py in `tests/unit/test_execute_sandbox.py` (test timeout, isolation, success/failure)
- [ ] T045 [US3] Update SKILL.md with complete instructions including validation flow
- [ ] T046 [US3] Add examples showing generated code + validation results
- [ ] T047 [US3] Write integration test in `tests/integration/test_code_example_generator_activation.py`

**Checkpoint**: code-example-generator should produce validated, runnable examples with >95% success rate (SC-007)

---

## Phase 6: User Story 4 - exercise-designer Skill (Priority: P1)

**Goal**: Enable educators to design deliberate practice exercises applying evidence-based learning strategies

**Independent Test**: Educator provides learning objectives → skill activates → produces 3-5 varied exercises with difficulty progression, identified learning strategies, test cases

### Implementation for exercise-designer

- [ ] T048 Create `.claude/skills/exercise-designer/` directory structure
- [ ] T049 [US4] Create `exercise-designer/SKILL.md` with frontmatter (name: exercise-designer, description with triggers: "create exercises", "practice problems", "design activities")
- [ ] T050 [P] [US4] Create `exercise-designer/reference/exercise-types.md` with fill-in-blank, debug-this, build-from-scratch, extend-code patterns
- [ ] T051 [P] [US4] Create `exercise-designer/reference/evidence-based-strategies.md` with retrieval practice, spaced repetition, interleaving, desirable difficulty
- [ ] T052 [P] [US4] Create `exercise-designer/reference/difficulty-progression.md` with guidelines for gradual difficulty increase
- [ ] T053 [P] [US4] Create `exercise-designer/reference/spaced-repetition.md` with spacing intervals and repetition patterns
- [ ] T054 [P] [US4] Create `exercise-designer/templates/exercise-template.yml` matching data-model.md schema (includes test cases, rubric)
- [ ] T055 [P] [US4] Create `exercise-designer/templates/rubric-template.yml` with criterion/points/descriptors
- [ ] T056 [US4] Implement `exercise-designer/scripts/generate-test-cases.py` to create input/output test cases for exercises
- [ ] T057 [US4] Write unit test for generate-test-cases.py in `tests/unit/test_generate_test_cases.py`
- [ ] T058 [US4] Update SKILL.md with complete instructions and varied exercise examples
- [ ] T059 [US4] Write integration test in `tests/integration/test_exercise_designer_activation.py`

**Checkpoint**: exercise-designer should produce varied exercises with evidence-based strategies identified

---

## Phase 7: User Story 5 - technical-clarity Skill (Priority: P1)

**Goal**: Enable authors to review technical explanations for jargon, clarity, completeness, and readability

**Independent Test**: Author submits draft explanation → skill activates → produces clarity report with jargon identified, readability metrics, suggestions for improvement

### Implementation for technical-clarity

- [ ] T060 Create `.claude/skills/technical-clarity/` directory structure
- [ ] T061 [US5] Create `technical-clarity/SKILL.md` with frontmatter (name: technical-clarity, description with triggers: "review for clarity", "check readability", "improve explanation")
- [ ] T062 [P] [US5] Create `technical-clarity/reference/readability-metrics.md` with Flesch-Kincaid, sentence length, vocabulary complexity
- [ ] T063 [P] [US5] Create `technical-clarity/reference/analogy-patterns.md` with effective analogy structures for technical concepts
- [ ] T064 [P] [US5] Create `technical-clarity/reference/clarity-checklist.md` with systematic clarity review criteria
- [ ] T065 [P] [US5] Create `technical-clarity/reference/gatekeeping-language.md` with examples of ableist terms ("obviously", "simply", "just", "easy")
- [ ] T066 [P] [US5] Create `technical-clarity/templates/clarity-report-template.yml` matching data-model.md schema
- [ ] T067 [US5] Implement `technical-clarity/scripts/analyze-readability.py` to calculate Flesch-Kincaid grade level, sentence length, complexity
- [ ] T068 [US5] Implement `technical-clarity/scripts/check-completeness.py` to identify missing critical information
- [ ] T069 [US5] Write unit tests for analyze-readability.py in `tests/unit/test_readability_analyzer.py`
- [ ] T070 [US5] Write unit tests for check-completeness.py in `tests/unit/test_completeness_checker.py`
- [ ] T071 [US5] Update SKILL.md with complete instructions and example clarity reports
- [ ] T072 [US5] Write integration test in `tests/integration/test_technical_clarity_activation.py`

**Checkpoint**: technical-clarity should identify >80% of clarity issues when validated against expert review (SC-009)

---

## Phase 8: User Story 6 - assessment-builder Skill (Priority: P1)

**Goal**: Enable educators to create assessments measuring deep understanding with meaningful distractors and rubrics

**Independent Test**: Educator provides learning objectives → skill activates → produces varied questions (MCQ, code-completion, debugging, projects) with distractors based on misconceptions

### Implementation for assessment-builder

- [ ] T073 Create `.claude/skills/assessment-builder/` directory structure
- [ ] T074 [US6] Create `assessment-builder/SKILL.md` with frontmatter (name: assessment-builder, description with triggers: "create quiz", "build assessment", "generate questions")
- [ ] T075 [P] [US6] Create `assessment-builder/reference/question-types.md` with MCQ, code-completion, debugging, short-answer, project-based patterns
- [ ] T076 [P] [US6] Create `assessment-builder/reference/distractor-design.md` with misconception-based distractor creation strategies
- [ ] T077 [P] [US6] Create `assessment-builder/reference/rubric-guidelines.md` with criterion design for open-ended questions
- [ ] T078 [P] [US6] Create `assessment-builder/reference/blooms-assessment-alignment.md` mapping Bloom's levels to question types
- [ ] T079 [P] [US6] Create `assessment-builder/templates/assessment-template.yml` matching data-model.md schema
- [ ] T080 [P] [US6] Create `assessment-builder/templates/rubric-template.yml` with excellent/adequate/insufficient descriptors
- [ ] T081 [US6] Implement `assessment-builder/scripts/validate-assessment.py` to check objective coverage, cognitive distribution, distractor quality
- [ ] T082 [US6] Write unit test for validate-assessment.py in `tests/unit/test_validate_assessment.py`
- [ ] T083 [US6] Update SKILL.md with complete instructions and example assessment packages
- [ ] T084 [US6] Write integration test in `tests/integration/test_assessment_builder_activation.py`

**Checkpoint**: assessment-builder should produce assessments with meaningful distractors and balanced cognitive distribution (60%+ non-recall per SC-010)

---

## Phase 9: Integration & Sequential Activation Testing

**Purpose**: Validate multi-skill workflows and sequential activation patterns

- [ ] T085 Write integration test in `tests/integration/test_sequential_skills.py` for "generate example and review for clarity" (code-example-generator → technical-clarity)
- [ ] T086 [P] Write integration test for "create objectives and design exercises" (learning-objectives → exercise-designer)
- [ ] T087 [P] Write integration test for "scaffold concept and generate examples" (concept-scaffolding → code-example-generator)
- [ ] T088 Verify mutually exclusive skill descriptions prevent activation conflicts
- [ ] T089 Test skill activation accuracy with varied prompt phrasings (target >80% activation success per SC-003)

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements affecting multiple skills and final validation

- [ ] T090 [P] Validate all SKILL.md files against `contracts/skill-metadata.schema.yml`
- [ ] T091 [P] Validate all YAML templates against their respective schemas in `contracts/`
- [ ] T092 [P] Run code formatter (black, isort) on all Python scripts
- [ ] T093 [P] Run type checker (mypy/pyright) on all Python scripts - must pass with no errors
- [ ] T094 [P] Run linter (ruff/pylint) on all Python scripts
- [ ] T095 Create `README.md` in `.claude/skills/` directory explaining skill organization
- [ ] T096 Update `quickstart.md` with any implementation-specific details discovered during development
- [ ] T097 Add troubleshooting section to quickstart.md based on integration test findings
- [ ] T098 Verify all file paths in quickstart.md match actual implementation
- [ ] T099 Run all unit tests (`pytest tests/unit/`) - must pass 100%
- [ ] T100 Run all integration tests (`pytest tests/integration/`) - must pass with >80% skill activation accuracy
- [ ] T101 Performance validation: Measure response times for each skill against targets (SC-005 to SC-010)
- [ ] T102 Create skill activation reference chart (trigger phrases → skills) for documentation
- [ ] T103 Final validation: Test each skill independently per user story acceptance scenarios

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all skills
- **Skills US1-US6 (Phases 3-8)**: All depend on Foundational phase completion
  - Skills can then proceed in parallel (6 developers, 6 skills simultaneously)
  - Or sequentially in priority order (all P1, but can pick any order within P1)
- **Integration (Phase 9)**: Depends on at least 2 skills complete (recommend all 6)
- **Polish (Phase 10)**: Depends on all skills complete

### Skill (User Story) Dependencies

- **US1 (learning-objectives)**: Can start after Foundational ✅ MVP candidate
- **US2 (concept-scaffolding)**: Can start after Foundational - Independent
- **US3 (code-example-generator)**: Can start after Foundational - Independent (uses sandbox from Foundational)
- **US4 (exercise-designer)**: Can start after Foundational - Independent
- **US5 (technical-clarity)**: Can start after Foundational - Independent
- **US6 (assessment-builder)**: Can start after Foundational - Independent

**KEY INSIGHT**: All 6 skills are completely independent after Foundational phase completes!

### Within Each Skill

1. Create directory structure
2. Create SKILL.md with frontmatter
3. Create reference files (can be parallel)
4. Create templates (can be parallel)
5. Implement scripts
6. Write unit tests for scripts
7. Update SKILL.md with complete instructions
8. Write integration test for skill activation

### Parallel Opportunities

**Phase 1 (Setup)**: T002, T003, T004, T005, T006 can all run in parallel

**Phase 2 (Foundational)**: T008, T009, T011, T012, T013 can run in parallel (T010 blocks T011)

**Phase 3-8 (Skills)**:
- All 6 skill phases can run in parallel with 6 developers
- Within each skill: reference files, templates, and some tests can run in parallel
- Example for learning-objectives: T016, T017, T018, T019 can all run in parallel

**Phase 10 (Polish)**: T090, T091, T092, T093, T094 can all run in parallel

---

## Parallel Example: learning-objectives Skill (Phase 3)

```bash
# After T014 (directory structure) and T015 (base SKILL.md):

# Launch all reference docs in parallel:
Task: "Create blooms-taxonomy-programming.md"
Task: "Create prerequisite-analysis.md"
Task: "Create assessment-methods.md"
Task: "Create learning-objective-template.yml"

# Then implement script + test (sequential):
Task: "Implement validate-objectives.py"
Task: "Write unit test for validate-objectives.py"

# Then complete SKILL.md and integration test (sequential):
Task: "Update SKILL.md with complete instructions"
Task: "Add example interactions to SKILL.md"
Task: "Write integration test for skill activation"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only - learning-objectives)

1. Complete Phase 1: Setup (T001-T006)
2. Complete Phase 2: Foundational (T007-T013) **← CRITICAL BLOCKER**
3. Complete Phase 3: learning-objectives skill (T014-T024)
4. **STOP and VALIDATE**: Test learning-objectives independently
   - Try: "Define objectives for Python decorators"
   - Verify: 3-5 objectives produced, Bloom's levels applied, prerequisites identified
5. Deploy/demo if ready - **This is a viable MVP!**

### Incremental Delivery (Add Skills One at a Time)

1. Setup + Foundational → Foundation ready
2. Add learning-objectives → Test independently → Deploy/Demo (MVP!)
3. Add concept-scaffolding → Test independently → Deploy/Demo
4. Add code-example-generator → Test independently → Deploy/Demo
5. Add exercise-designer → Test independently → Deploy/Demo
6. Add technical-clarity → Test independently → Deploy/Demo
7. Add assessment-builder → Test independently → Deploy/Demo
8. Each skill adds value without breaking previous skills

### Parallel Team Strategy (6 Developers)

With 6 developers:

1. Team completes Setup (Phase 1) together (T001-T006)
2. Team completes Foundational (Phase 2) together (T007-T013) **← CRITICAL**
3. Once Foundational is done, **split into 6 parallel tracks**:
   - Developer A: learning-objectives (T014-T024)
   - Developer B: concept-scaffolding (T025-T034)
   - Developer C: code-example-generator (T035-T047)
   - Developer D: exercise-designer (T048-T059)
   - Developer E: technical-clarity (T060-T072)
   - Developer F: assessment-builder (T073-T084)
4. All skills complete independently and simultaneously
5. Reconvene for Integration testing (Phase 9) and Polish (Phase 10)

**Timeline with 6 developers**: ~3-4 days
- Day 1: Setup + Foundational (everyone)
- Days 2-3: Parallel skill implementation (6 tracks)
- Day 4: Integration + Polish

**Timeline with 1 developer**: ~10-12 days (sequential implementation)

---

## Task Count Summary

- **Phase 1 (Setup)**: 6 tasks
- **Phase 2 (Foundational)**: 7 tasks (CRITICAL - blocks all skills)
- **Phase 3 (US1 - learning-objectives)**: 11 tasks
- **Phase 4 (US2 - concept-scaffolding)**: 10 tasks
- **Phase 5 (US3 - code-example-generator)**: 13 tasks
- **Phase 6 (US4 - exercise-designer)**: 12 tasks
- **Phase 7 (US5 - technical-clarity)**: 13 tasks
- **Phase 8 (US6 - assessment-builder)**: 12 tasks
- **Phase 9 (Integration)**: 5 tasks
- **Phase 10 (Polish)**: 14 tasks

**Total**: 103 tasks

**Parallel opportunities**: 40+ tasks marked [P] can run in parallel when conditions are met

---

## Success Criteria Validation

Each skill phase maps to success criteria from spec.md:

| Skill | Success Criteria | Validation Task |
|-------|------------------|-----------------|
| learning-objectives | SC-001, SC-005, SC-011 | T024 (integration test) |
| concept-scaffolding | SC-001, SC-006 | T034 (integration test) |
| code-example-generator | SC-001, SC-007, SC-012 | T047 (integration test) |
| exercise-designer | SC-001, SC-008, SC-013 | T059 (integration test) |
| technical-clarity | SC-001, SC-009, SC-014 | T072 (integration test) |
| assessment-builder | SC-001, SC-010 | T084 (integration test) |
| All skills | SC-002, SC-003, SC-004 | T088, T089 (activation tests) |
| All skills | SC-015 | T103 (final validation) |

Performance validation (SC-005 to SC-010) in T101.

---

## Notes

- [P] tasks = different files, no dependencies on incomplete work
- [Story] label (US1-US6) maps task to specific skill for traceability
- Each skill is independently completable and testable
- Tests validate skill activation accuracy and output correctness
- Foundational phase (T007-T013) is CRITICAL - nothing else can start until complete
- All 6 skills can be built in parallel after Foundational phase
- Commit after each task or logical group
- Stop at any checkpoint to validate skill independently
- Hard failure mode (per clarification #1) means validation errors must be clear and actionable
