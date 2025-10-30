# Tasks: Chapter 6 - Gemini CLI: Installation and Basics

**Input**: Design documents from `/specs/001-chapter-6/`
**Prerequisites**: plan.md, spec.md (7 user stories with priorities P1-P3)

**Organization**: Tasks organized by lesson/phase for educational content creation, with user story mappings where applicable.

**Note**: This is a book chapter, not software. Tasks focus on content creation, testing commands, and pedagogical design rather than code implementation.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different lessons, no dependencies)
- **[US#]**: Maps to user story from spec.md (US1-US7)
- Include exact file paths in descriptions

## User Story Mapping

| Story | Priority | Focus | Lessons |
|-------|----------|-------|---------|
| US1 | P1 | Installation & Authentication | Lessons 2-3 |
| US2 | P1 | Basic Configuration & First Command | Lessons 3-4 |
| US3 | P2 | Built-In Tools Exploration | Lesson 5 |
| US4 | P2 | Understanding 1M Token Context | Lesson 6 |
| US5 | P3 | Extensions Introduction | Lesson 6 |
| US6 | P2 | Tool Comparison Framework | Lessons 1, 6 |
| US7 | P3 | Qwen Code Alternative | Lessons 1, 6 |

---

## Phase 1: Chapter Foundation & Structure

**Purpose**: Create lesson outlines and chapter framework

- [X] T001 Create chapter README.md in book-source/docs/06-gemini-cli-installation-and-basics/README.md
- [X] T002 [P] Create 01-lesson-1.md outline (Why Gemini CLI Matters) in book-source/docs/06-gemini-cli-installation-and-basics/01-why-gemini-cli-matters.md
- [X] T003 [P] [US1] Create 02-lesson-2.md outline (Installation) in book-source/docs/06-gemini-cli-installation-and-basics/02-installation-platform-specific.md
- [X] T004 [P] [US1] Create 03-lesson-3.md outline (Authentication) in book-source/docs/06-gemini-cli-installation-and-basics/03-authentication-and-configuration.md
- [X] T005 [P] [US2] Create 04-lesson-4.md outline (First Commands) in book-source/docs/06-gemini-cli-installation-and-basics/04-your-first-commands.md
- [X] T006 [P] [US3] Create 05-lesson-5.md outline (Built-In Tools) in book-source/docs/06-gemini-cli-installation-and-basics/05-built-in-tools-deep-dive.md
- [X] T007 [P] [US4] [US5] [US6] Create 06-lesson-6.md outline (Context Window & Comparison) in book-source/docs/06-gemini-cli-installation-and-basics/06-context-window-and-tool-comparison.md

---

## Phase 2: User Story 1 - Installation & Authentication (Priority: P1) 🎯 MVP

**Goal**: Learners can install Gemini CLI and authenticate successfully on their OS
**Independent Test**: `gemini --version` shows version, `gemini status` shows authenticated quota

### Lesson 2: Installation — Platform-Specific (US1)

- [X] T008 [US1] Write pre-installation checklist in 02-installation-platform-specific.md
- [X] T009 [P] [US1] Write Windows installation section with PowerShell and Command Prompt options
- [X] T010 [P] [US1] Write macOS installation section with npm and Homebrew options, M1/M2 guidance
- [X] T011 [P] [US1] Write Linux installation section (Ubuntu/Debian/Fedora coverage)
- [X] T012 [US1] Write verification section common to all platforms (`gemini --version`)
- [X] T013 [US1] Write troubleshooting section covering 8-10 common failure scenarios
- [X] T014 [P] [US1] Create terminal output examples showing successful installation

### Lesson 3: Authentication & Configuration (US1)

- [X] T015 [US1] Write OAuth authentication conceptual explanation in 03-authentication-and-configuration.md
- [X] T016 [US1] Write step-by-step authentication walkthrough (`gemini auth` command)
- [X] T017 [US1] Write verification section explaining `gemini status` output
- [X] T018 [US1] Explain free tier quotas in practical terms (60 req/min, 1,000 req/day)
- [X] T019 [US1] Write configuration section (config file location, customization options)
- [X] T020 [US1] Write authentication troubleshooting (5-6 common failure scenarios)
- [X] T021 [P] [US1] [US7] Mention regional limitations and Qwen Code alternative

---

## Phase 3: User Story 2 - Basic Configuration & First Command (Priority: P1)

**Goal**: Learners can execute first commands and verify tool functionality
**Independent Test**: `gemini "Explain what Gemini CLI is"` returns coherent response

### Lesson 4: Your First Commands (US2)

- [X] T022 [US2] Write command syntax explanation in 04-your-first-commands.md
- [X] T023 [US2] Write first verification command walkthrough
- [X] T024 [US2] Provide five quick verification commands with expected outputs
- [X] T025 [US2] Explain how to interpret AI responses (critical thinking, verification)
- [X] T026 [US2] Write common error scenarios section (5-6 error messages with solutions)
- [X] T027 [P] [US2] Add prompting fundamentals teaser (defer details to Part 3)

---

## Phase 4: User Story 6 - Tool Comparison Framework (Priority: P2)

**Goal**: Learners can compare Gemini CLI and Claude Code objectively
**Independent Test**: Learner creates comparison table with 3+ criteria and justifies tool choices

### Lesson 1: Why Gemini CLI Matters (US6, US7)

- [X] T028 [P] [US6] Write opening hook and context in 01-why-gemini-cli-matters.md
- [X] T029 [P] [US6] Write section on three key differentiators (open source, free tier, context)
- [X] T030 [P] [US6] Create comparison table (Claude Code vs Gemini CLI) with 6-8 dimensions
- [X] T031 [P] [US6] Write when-to-use guidance (3-4 concrete scenarios)
- [X] T032 [P] [US5] Introduce MCP and extensibility conceptually (1-2 paragraphs)
- [X] T033 [P] [US6] Add real-world examples of Gemini CLI benefits

---

## Phase 5: User Story 3 - Built-In Tools Exploration (Priority: P2)

**Goal**: Learners can use file operations, web fetching, search grounding, and shell integration
**Independent Test**: Learner analyzes local file with `gemini --file` command

### Lesson 5: Built-In Tools Deep Dive (US3)

- [X] T034 [US3] Write introduction explaining why built-in tools differentiate Gemini CLI in 05-built-in-tools-deep-dive.md
- [X] T035 [P] [US3] Write File Operations tool section (`--file` flag, examples, use cases, exercise)
- [X] T036 [P] [US3] Write Web Fetching tool section (`--web-fetch`, examples, exercise)
- [X] T037 [P] [US3] Write Search Grounding section (current information, source citation, exercise)
- [X] T038 [P] [US3] Write Shell Integration section (command suggestions, exercise)
- [X] T039 [US3] Write tool combination exercise (realistic scenario using 2-3 tools)
- [X] T040 [P] [US3] Add tool limitations and constraints section

---

## Phase 6: User Stories 4, 5 - Context Window & Extensions (Priority: P2-P3)

**Goal**: Learners understand 1M token context advantage and extensions concept
**Independent Test**: Learner explains context window in practical terms and describes one extension

### Lesson 6: Context Window & Tool Comparison (US4, US5, US6, US7)

- [X] T041 [US4] Write tokens-to-practical translation in 06-context-window-and-tool-comparison.md
- [X] T042 [US4] Write "when context size doesn't matter" section
- [X] T043 [US4] Write "when context becomes critical" section with real scenarios
- [X] T044 [US4] Create scenario table (context requirements vs tool viability)
- [X] T045 [US6] Write decision framework section (when to choose each tool)
- [X] T046 [P] [US5] Introduce Extensions conceptually (2-3 examples)
- [X] T047 [P] [US5] Introduce MCP conceptually (1-2 sentences)
- [X] T048 [P] [US7] Mention Qwen Code as alternative (2,000 req/day free tier)
- [X] T049 [US6] Include decision-making exercise (3-5 scenarios)
- [X] T050 [P] [US6] Create expanded comparison table (8+ dimensions)

---

## Phase 7: Command Verification (Cross-Platform Testing)

**Purpose**: Test all commands on Windows, Mac, Linux to ensure accuracy

- [ ] T051 [P] [US1] Test all installation commands on Windows (fresh Node.js + existing Node.js)
- [ ] T052 [P] [US1] Test all installation commands on macOS (Intel and M1/M2, npm + Homebrew)
- [ ] T053 [P] [US1] Test all installation commands on Linux (Ubuntu, Debian, Fedora)
- [ ] T054 [US2] Test all five verification commands from Lesson 4 (document actual outputs)
- [ ] T055 [P] [US3] Test file operations tool (create sample code, verify analysis)
- [ ] T056 [P] [US3] Test web fetching tool (test 2-3 URLs, verify summaries)
- [ ] T057 [P] [US3] Test search grounding capability (current information questions)
- [ ] T058 [US3] Test tool combination exercise (verify all steps execute successfully)
- [ ] T059 [P] Create terminal output screenshots/transcripts (6-8 interactions)

---

## Phase 8: Exercises & Assessments

**Purpose**: Design hands-on exercises and verification activities

- [ ] T060 [P] [US6] Design reflection exercise for Lesson 1 (tool choice justification)
- [ ] T061 [P] [US1] Design installation verification exercise for Lesson 2 (`gemini --version` proof)
- [ ] T062 [P] [US1] Design authentication verification for Lesson 3 (`gemini status` quota display)
- [ ] T063 [P] [US2] Design command execution verification for Lesson 4 (run 5 commands, document responses)
- [ ] T064 [US3] Design tool combination exercise for Lesson 5 (step-by-step guided exercise)
- [ ] T065 [P] [US6] Design decision-making exercise for Lesson 6 (3-5 scenarios with framework application)
- [ ] T066 [P] Create quick assessment questions (5-10 questions with answers)

---

## Phase 9: Cross-Cutting Concerns

**Purpose**: Ensure quality, accessibility, and constitutional alignment

- [ ] T067 Ensure all content is accessibility-compliant (grade 7 reading level, no gatekeeping language)
- [ ] T068 Verify platform-specific guidance is equal (Windows, Mac, Linux parity)
- [ ] T069 [P] Add security and ethical considerations (API key safety, local execution, ethical AI use)
- [ ] T070 Ensure all troubleshooting guidance is comprehensive (failure scenarios + solutions)
- [ ] T071 [P] Verify all external links are current (Gemini CLI docs, official resources)
- [ ] T072 [P] Add update maintenance notes (version change triggers)

---

## Phase 10: Integration & Cross-Reference

**Purpose**: Ensure smooth integration with adjacent chapters

- [ ] T073 Verify integration with Chapter 5 (references to Claude Code concepts, comparison builds on Ch 5)
- [ ] T074 [P] Verify integration with Chapter 7 (foreshadow Bash integration, create momentum)
- [ ] T075 [P] Verify integration with Chapter 8 (decision framework leads to comprehensive tool selection)
- [ ] T076 Verify prerequisite clarity (assumptions from Chapter 5 made explicit)
- [ ] T077 [P] Add cross-references to Parts 3 and 4 (Prompting, Python progression)

---

## Phase 11: Review & Finalization

**Purpose**: Final quality gates before publication

- [ ] T078 Peer review for pedagogical clarity (2-3 reviewers confirm objectives met)
- [ ] T079 Technical accuracy review (commands tested, outputs verified, facts checked)
- [ ] T080 Accessibility and bias check (no gatekeeping, inclusive examples)
- [ ] T081 Style and consistency check (matches output styles, consistent tone)
- [ ] T082 Final copy editing (zero typos, grammatical errors, placeholders)
- [ ] T083 Docusaurus build validation (builds without errors, links valid, YAML correct)
- [ ] T084 Constitutional alignment final check (all 9 domain skills applied, all principles met)

---

## Acceptance Criteria (Definition of Done)

### For All Lessons:
- [ ] Learning objectives clearly stated and matched to Bloom's taxonomy
- [ ] Content is accessible at grade 7 reading level
- [ ] No gatekeeping language or assumptions about prior knowledge
- [ ] Technical terms defined on first use
- [ ] Tone is professional yet approachable
- [ ] Opening hook engages reader immediately
- [ ] Content flows naturally; transitions between sections smooth
- [ ] Examples are concrete and relatable
- [ ] No placeholder text or incomplete sections
- [ ] Publication-quality writing throughout

### For Technical Lessons (2-5):
- [ ] All code/commands tested and working on relevant platforms
- [ ] Expected outputs provided for all commands
- [ ] Hands-on exercises have clear success criteria
- [ ] Exercises can be completed without external help
- [ ] Error scenarios and solutions provided
- [ ] Links to official documentation included where appropriate

### For Conceptual Lessons (1, 6):
- [ ] Real-world examples are compelling and specific
- [ ] Reflection prompts encourage critical thinking
- [ ] Comparison tables provide visual clarity
- [ ] Forward momentum toward next content established

### Chapter-Level Acceptance:
- [ ] All 7 user stories fully addressed (US1-US7)
- [ ] All 15 functional requirements met (FR-001 through FR-015)
- [ ] All 10 success criteria have clear validation (SC-001 through SC-010)
- [ ] All 6 lessons complete and integrated
- [ ] Chapter README.md follows chapter-readme.md output style
- [ ] Time estimate (2-3 hours) realistic
- [ ] Chapter integrates smoothly with Chapters 5, 7, 8
- [ ] All 9 domain skills applied throughout
- [ ] Constitutional alignment verified (AI-first, accessibility, show-then-explain)
- [ ] Ready for publication

---

## Dependencies & Parallel Work

### Sequential Dependencies:
1. **Phase 1** (outlines) → **Phases 2-6** (lesson writing)
2. **Phases 2-6** (content writing) → **Phase 7** (command verification)
3. **Phase 7** (verification) → **Phase 8** (exercises)
4. **Phases 1-8** complete → **Phase 9** (cross-cutting)
5. **Phase 9** complete → **Phase 10** (integration)
6. **All phases** complete → **Phase 11** (final review)

### Parallel Opportunities:

**Within Phase 1**: All lesson outlines (T002-T007) can be created in parallel

**Within Phases 2-6**: Lessons can be written independently:
- Lesson 1 (T028-T033) ‖ Lesson 2 (T008-T014) ‖ Lesson 3 (T015-T021) ‖ Lesson 4 (T022-T027) ‖ Lesson 5 (T034-T040) ‖ Lesson 6 (T041-T050)

**Within Phase 7**: Platform testing can happen in parallel:
- Windows (T051) ‖ macOS (T052) ‖ Linux (T053)
- Tool testing: T055, T056, T057 can run in parallel

**Within Phase 8**: All exercise design tasks (T060-T066) can run in parallel

**Within Phase 9**: Cross-cutting tasks T069, T071, T072 can run in parallel

**Within Phase 10**: Integration verification T074, T075, T077 can run in parallel

---

## Task Summary

- **Total Tasks**: 84 discrete, testable items
- **Parallelizable Tasks**: 45+ tasks marked with [P]
- **User Story Coverage**: All 7 user stories (US1-US7) mapped to tasks
- **Critical Path**: Outlines → Content Writing → Command Testing → Review
- **Estimated Effort**: 80-100 hours total
- **Bottlenecks**:
  - Phase 7 command testing (requires access to all three platforms)
  - Phase 11 technical accuracy review (requires expert validation)

---

## Implementation Strategy

### MVP Scope (Deliver First)
**User Stories 1-2 (P1 priority)**:
- Lesson 2: Installation (US1)
- Lesson 3: Authentication (US1)
- Lesson 4: First Commands (US2)
- Command verification for US1-US2 only

**Rationale**: Enables learners to install, authenticate, and execute first commands successfully. This is the minimum viable chapter.

### Second Increment
**User Story 6 (P2 priority)**:
- Lesson 1: Why Gemini CLI Matters (US6, US7)
- Lesson 6: Tool Comparison sections (US6)

**Rationale**: Adds strategic context and decision framework for tool selection.

### Third Increment
**User Stories 3-4 (P2 priority)**:
- Lesson 5: Built-In Tools (US3)
- Lesson 6: Context Window (US4)

**Rationale**: Unlocks full Gemini CLI capabilities.

### Final Increment
**User Stories 5, 7 (P3 priority)**:
- Extensions introduction (US5)
- Qwen Code mention (US7)

**Rationale**: Nice-to-have context for advanced learners and ecosystem awareness.

---

## Follow-Ups & Risks

**Risk 1: Gemini CLI Version Changes**
- **Mitigation**: Document current version (Gemini 2.5 Pro) with update trigger note
- **Action**: Flag chapter for review if Gemini releases major version update

**Risk 2: Installation Dependency Complexity**
- **Mitigation**: Comprehensive troubleshooting for Node.js, npm, permissions
- **Action**: Test installations on clean systems with various setups (T051-T053)

**Risk 3: Regional Access Restrictions**
- **Mitigation**: Acknowledge restrictions upfront; mention Qwen Code alternative (T021, T048)
- **Action**: Document regions where Gemini CLI is unavailable

**Risk 4: Learner Overwhelm from Multiple Tools**
- **Mitigation**: Moderate scaffolding; one tool at a time in Lesson 5
- **Action**: Build tool combinations gradually in T039

**Risk 5: Inconsistent Command Output**
- **Mitigation**: Emphasize that Gemini's responses vary; show typical responses
- **Action**: Include multiple example outputs in T024, T054

---

## Next Steps After Task Completion

1. **Technical Review**: Invoke technical-reviewer subagent to validate technical accuracy
2. **Pedagogical Review**: Verify Bloom's progression and learning outcomes met
3. **Integration Verification**: Check flow with Chapters 5, 7, 8
4. **Docusaurus Publication**: Build and publish to book website
5. **Beta Testing**: Gather learner feedback on clarity and exercises
6. **Refinement**: Address feedback and publish final version

---

**Status**: ✅ Ready for implementation
**Created**: 2025-10-31
**Specification**: specs/001-chapter-6/spec.md
**Plan Reference**: specs/001-chapter-6/plan.md
**Branch**: 001-chapter-6
