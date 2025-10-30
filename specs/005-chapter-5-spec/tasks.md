# Chapter 5: How It All Started: The Claude Code Phenomenon — Task Checklist

**Chapter Type**: Hybrid (Narrative Foundation + Technical Tutorials)
**Status**: Ready for Development
**Feature Branch**: `005-chapter-5-spec`
**Approved Plan**: `specs/005-chapter-5-spec/plan.md`
**Estimated Total Effort**: 65-80 hours
**Handoff to**: Lesson-Writer Subagent

---

## Overview

This task checklist breaks down Chapter 5 implementation into specific, testable development tasks organized by lesson. Tasks are sequenced by dependency and prioritized (MUST/SHOULD/NICE-TO-HAVE).

**Chapter Scope**: 5 lessons totaling 75-95 minutes (30-35 reading + 45-60 hands-on)
- Lesson 1: Origin story (narrative)
- Lesson 2: Installation & authentication (technical)
- Lesson 3: Subagents tutorial (technical)
- Lesson 4: Agent Skills tutorial (technical)
- Lesson 5: MCP servers & workflows (technical/practical)

---

## Phase 1: Lesson 1 - Origin Story and Paradigm Shift

### Content Development

- [ ] **MUST**: Create Lesson 1 outline and narrative arc
  - Acceptance: Outline approved, clear narrative flow, hook identified
  - Reference: `plan.md` Lesson 1 section
  - Effort: 3 hours
  - Deliverable: outline.md (private planning doc)

- [ ] **MUST**: Write Lesson 1 - The Claude Code Origin Story (complete content)
  - Acceptance: 800-1200 words, Docusaurus-ready with YAML frontmatter, Grade 7 reading level
  - Reference: `plan.md` Lesson 1; output style from `.claude/output-styles/lesson.md`
  - Effort: 6 hours
  - Includes:
    - [ ] Opening hook: Origin story ("didn't mean to build it")
    - [ ] Clear explanation of what Claude Code is
    - [ ] Comparison: Claude Code vs chat-based AI tools
    - [ ] Paradigm shift narrative (agentic vs passive)
    - [ ] Terminal integration benefits
    - [ ] 5-7 real-world examples or scenarios
    - [ ] 2-3 reflection prompts
    - [ ] Transition to Lesson 2
    - [ ] YAML frontmatter with sidebar_position: 1
  - Deliverable: `01-origin-story.md`

### Review and Polish

- [ ] **SHOULD**: Peer review for pedagogical clarity
  - Acceptance: Reviewer confirms learning objective achieved, content clear, engaging
  - Reference: Existing conceptual chapters for tone/style
  - Effort: 1 hour
  - Stakeholders: Main Claude/human reviewer

- [ ] **MUST**: Technical clarity review (accessibility check)
  - Acceptance: No jargon gatekeeping, concepts explained clearly, inclusive examples
  - Reference: Principle 8 (Accessibility) from constitution
  - Effort: 1.5 hours
  - Deliverable: Clarity review notes

- [ ] **SHOULD**: Cross-chapter coherence check
  - Acceptance: Verified with Chapters 1-4; prerequisites clear, philosophy consistent
  - Reference: Part 1 chapters and book philosophy
  - Effort: 1 hour

**Lesson 1 Subtotal**: 12.5 hours | **Status**: Sequential (dependent on outline completion)

---

## Phase 2: Lesson 2 - Installation and Authentication

### Content Development

- [ ] **MUST**: Create Lesson 2 outline and structure
  - Acceptance: Outline shows clear decision trees (path A: NPM, path B: native; auth flows)
  - Reference: `plan.md` Lesson 2; spec requirements (FR-003, FR-004)
  - Effort: 4 hours
  - Deliverable: outline.md with decision tree visuals

- [ ] **MUST**: Test and verify all installation commands
  - Acceptance: Commands tested on Windows, macOS, Linux; expected output documented
  - Reference: Claude Code official documentation
  - Effort: 5 hours
  - Testing Checklist:
    - [ ] NPM installation method tested and working
    - [ ] Native Windows installer tested
    - [ ] Native macOS (Intel) installer tested
    - [ ] Native macOS (M1/M2) installer tested
    - [ ] Linux installation (apt, snap, or native) tested
    - [ ] Claude.ai subscription authentication flow tested
    - [ ] Claude Console API authentication flow tested
    - [ ] First-run verification command tested
  - Deliverable: verified-commands.md with expected output for each platform

- [ ] **MUST**: Write Lesson 2 - Installation and Authentication (complete content)
  - Acceptance: 2000-2500 words, platform-specific instructions, Docusaurus-ready
  - Reference: verified commands from testing, output style
  - Effort: 8 hours
  - Includes:
    - [ ] Pre-installation checklist (Node.js, accounts, prerequisites)
    - [ ] Decision tree: "Which installation path should I choose?"
    - [ ] Installation Path A: NPM method
      - [ ] Step-by-step commands with copy-paste formatting
      - [ ] Expected output at each step
      - [ ] Common NPM errors and solutions (5+ error cases)
    - [ ] Installation Path B: Native method (Windows, macOS, Linux)
      - [ ] Platform-specific instructions
      - [ ] Download links and what to expect
      - [ ] Verification steps
    - [ ] Authentication flow walkthrough
      - [ ] Claude.ai subscription path
      - [ ] Claude Console API path
      - [ ] "I have both accounts" FAQ
    - [ ] First-run verification test
    - [ ] Comprehensive troubleshooting section (10+ common errors)
      - [ ] Error → Cause → Solution mappings
      - [ ] Links to official GitHub issues
      - [ ] Fallback options ("if this fails, try...")
    - [ ] YAML frontmatter (sidebar_position: 2)
  - Deliverable: `02-installation-and-authentication.md`

### Code Examples and Verification

- [ ] **MUST**: Create terminal output examples for all platform installations
  - Acceptance: 8-12 terminal output screenshots or code blocks showing expected results
  - Effort: 3 hours
  - Deliverable: Terminal output examples file (referenced in lesson)

- [ ] **MUST**: Develop 10+ troubleshooting scenarios with solutions
  - Acceptance: Each scenario has error message, explanation, step-by-step solution, prevention tip
  - Reference: Spec Risk 3 (Platform-Specific Failures), Edge Cases section
  - Effort: 4 hours
  - Scenarios to cover:
    - [ ] Node.js not installed (when choosing NPM method)
    - [ ] npm: command not found
    - [ ] Permission denied during installation
    - [ ] Network timeout during download
    - [ ] Invalid authentication credentials
    - [ ] Claude.ai vs Console account confusion
    - [ ] WSL vs native Windows issue
    - [ ] M1/M2 macOS architecture mismatch
    - [ ] Linux package manager conflicts
    - [ ] Firewall blocking API access
  - Deliverable: troubleshooting-guide.md

### Review and Polish

- [ ] **SHOULD**: Peer review for step clarity
  - Acceptance: Reviewer can follow instructions without external help
  - Effort: 1.5 hours

- [ ] **MUST**: Technical accuracy verification
  - Acceptance: All commands verified current, links live, no deprecated syntax
  - Reference: Claude Code official docs dated 2025+
  - Effort: 2 hours

- [ ] **SHOULD**: Cross-platform testing feedback
  - Acceptance: Tested by someone unfamiliar with Claude Code
  - Effort: 2 hours (coordinated with other teams)

**Lesson 2 Subtotal**: 29.5 hours | **Status**: Parallel (can start after outline, content builds on testing)

---

## Phase 3: Lesson 3 - Subagents

### Content Development

- [ ] **MUST**: Create Lesson 3 outline and subagent architecture diagrams
  - Acceptance: Outline clear, architecture diagram shows isolation, examples listed
  - Reference: `plan.md` Lesson 3; spec requirements (FR-005, FR-006)
  - Effort: 3 hours
  - Deliverable: outline.md with architecture diagram

- [ ] **MUST**: Create code-reviewer subagent working example
  - Acceptance: Complete, tested subagent; SKILL.md and config files included; instructions clear
  - Reference: Claude Code documentation on subagents
  - Effort: 4 hours
  - Deliverable: code-reviewer-subagent/ folder with all files
  - Contents:
    - [ ] Complete system prompt for code-reviewer
    - [ ] Configuration file (if applicable)
    - [ ] Example usage commands
    - [ ] Expected output example

- [ ] **MUST**: Write Lesson 3 - Understanding and Using Subagents (complete content)
  - Acceptance: 1800-2200 words, working tutorial, Docusaurus-ready
  - Reference: working subagent example, output style
  - Effort: 7 hours
  - Includes:
    - [ ] What are subagents? (definition, purpose, benefits)
    - [ ] Why subagents matter (context preservation, specialization, reusability)
    - [ ] Comparison table: Main conversation vs subagents
    - [ ] 3-4 real-world use cases with explanations
    - [ ] Anatomy of a subagent (files, prompts, configuration)
    - [ ] Step-by-step tutorial: Create your first subagent
      - [ ] Choose task type (code-reviewer)
      - [ ] Create subagent structure
      - [ ] Write system prompt
      - [ ] Configure (if needed)
      - [ ] Test on sample code
    - [ ] Subagent management commands (create, list, edit, delete, switch)
    - [ ] Decision tree: "When should I use a subagent?"
    - [ ] Common workflows and patterns
    - [ ] Next steps and exploration ideas
    - [ ] YAML frontmatter (sidebar_position: 3)
  - Deliverable: `03-subagents.md`

### Code Examples and Exercises

- [ ] **MUST**: Create 3 subagent templates for learners
  - Acceptance: Each template has clear purpose, working system prompt, setup instructions
  - Effort: 3 hours
  - Templates:
    - [ ] code-reviewer (primary tutorial example)
    - [ ] documentation-writer
    - [ ] bug-analyst
  - Deliverable: subagent-templates/ folder

- [ ] **MUST**: Design hands-on exercise: Create code-reviewer subagent
  - Acceptance: Clear step-by-step instructions, sample code to review, expected output shown
  - Effort: 2 hours
  - Deliverable: Exercise with solution (private for instructor verification)

- [ ] **SHOULD**: Create alternative subagent template for learners to customize
  - Acceptance: Template with clear placeholders for domain-specific specialization
  - Effort: 1.5 hours
  - Deliverable: customizable-template.md

### Review and Polish

- [ ] **SHOULD**: Peer review for concept clarity
  - Acceptance: Reviewer understands subagent architecture and use cases
  - Effort: 1.5 hours

- [ ] **MUST**: Technical accuracy of subagent files
  - Acceptance: All example subagents tested and working in Claude Code
  - Reference: Claude Code documentation
  - Effort: 2 hours

- [ ] **MUST**: Hands-on exercise testing
  - Acceptance: Exercise can be completed in 15-20 minutes; clear success criteria
  - Effort: 1.5 hours

**Lesson 3 Subtotal**: 25 hours | **Status**: Sequential (depends on Lesson 2 completion)

---

## Phase 4: Lesson 4 - Agent Skills

### Content Development

- [ ] **MUST**: Create Lesson 4 outline and skill discovery research
  - Acceptance: Outline clear, skill structure documented, discovery mechanism explained
  - Reference: `plan.md` Lesson 4; spec requirements (FR-007, FR-008)
  - Effort: 3 hours
  - Deliverable: outline.md with SKILL.md structure breakdown

- [ ] **MUST**: Research and document SKILL.md best practices
  - Acceptance: Skill naming conventions, description guidelines, discovery mechanics documented
  - Reference: Claude Code documentation on Agent Skills
  - Effort: 3 hours
  - Deliverable: skill-best-practices.md

- [ ] **MUST**: Create python-docstring-writer skill working example
  - Acceptance: Complete, tested skill; SKILL.md and supporting files; clear purpose
  - Reference: Claude Code skill documentation
  - Effort: 4 hours
  - Deliverable: python-docstring-writer/ folder with all files
  - Contents:
    - [ ] SKILL.md with clear, discoverable description
    - [ ] Supporting documentation/prompts (if applicable)
    - [ ] Test cases showing skill discovery and invocation
    - [ ] Example output

- [ ] **MUST**: Write Lesson 4 - Creating and Using Agent Skills (complete content)
  - Acceptance: 2000-2300 words, working tutorial, Docusaurus-ready
  - Reference: working skill example, output style
  - Effort: 7 hours
  - Includes:
    - [ ] What are Agent Skills? (definition, lifecycle)
    - [ ] Skills vs slash commands (model-invoked vs user-invoked)
    - [ ] How skill discovery works (Claude Code's automatic invocation)
    - [ ] Anatomy of a skill (SKILL.md structure, metadata, supporting files)
    - [ ] Skill naming and description best practices (for discoverability)
    - [ ] Step-by-step tutorial: Create your first skill
      - [ ] Choose a domain (python-docstring-writer)
      - [ ] Create SKILL.md with purpose statement
      - [ ] Write discoverable description
      - [ ] Set scope (personal/project/shareable)
      - [ ] Add supporting files
      - [ ] Test skill discovery
    - [ ] Skill management (creating, updating, organizing, sharing)
    - [ ] Building a skill library (organizational strategies)
    - [ ] Competitive advantage discussion (domain-specific expertise)
    - [ ] Good vs poor skill descriptions (examples)
    - [ ] Next steps: Extending your library
    - [ ] YAML frontmatter (sidebar_position: 4)
  - Deliverable: `04-agent-skills.md`

### Code Examples and Exercises

- [ ] **MUST**: Create 5 skill templates for different domains
  - Acceptance: Each has clear purpose, good SKILL.md structure, discoverable description
  - Effort: 3 hours
  - Templates:
    - [ ] python-docstring-writer (primary example)
    - [ ] sql-query-optimizer
    - [ ] code-style-converter
    - [ ] error-message-explainer
    - [ ] documentation-generator
  - Deliverable: skill-templates/ folder

- [ ] **MUST**: Design hands-on exercise: Create python-docstring-writer skill
  - Acceptance: Step-by-step instructions, test code samples, success verification
  - Effort: 2.5 hours
  - Deliverable: Exercise with solution

- [ ] **SHOULD**: Create skill naming guidelines and examples
  - Acceptance: Clear rules for naming, bad/good examples, rationale
  - Effort: 1.5 hours
  - Deliverable: skill-naming-guidelines.md

- [ ] **SHOULD**: Create skill description template
  - Acceptance: Template with placeholders for all required elements of discoverable description
  - Effort: 1 hour
  - Deliverable: skill-description-template.md

### Review and Polish

- [ ] **SHOULD**: Peer review for concept clarity
  - Acceptance: Reviewer understands skill discovery and competitive advantage
  - Effort: 1.5 hours

- [ ] **MUST**: Technical accuracy of skill files
  - Acceptance: All example skills tested; Claude Code discovers and invokes them
  - Reference: Claude Code documentation
  - Effort: 2 hours

- [ ] **MUST**: Hands-on exercise testing
  - Acceptance: Exercise completable in 20-25 minutes; learner can verify autonomous discovery
  - Effort: 1.5 hours

- [ ] **SHOULD**: Review against Principle 13 (competitive advantage)
  - Acceptance: Lesson emphasizes domain-specific advantage clearly
  - Effort: 1 hour

**Lesson 4 Subtotal**: 31 hours | **Status**: Sequential (depends on Lesson 3 completion)

---

## Phase 5: Lesson 5 - MCP Servers and Workflows

### Content Development

- [ ] **MUST**: Create Lesson 5 outline and MCP architecture research
  - Acceptance: Outline clear, MCP architecture documented, GitHub MCP walkthrough mapped
  - Reference: `plan.md` Lesson 5; spec requirements (FR-009, FR-010, FR-011)
  - Effort: 4 hours
  - Deliverable: outline.md with MCP architecture diagram, available servers research

- [ ] **MUST**: Verify GitHub MCP integration and create step-by-step guide
  - Acceptance: Github MCP installation tested, configuration verified, working example
  - Reference: GitHub MCP documentation, claude mcp add workflow
  - Effort: 4 hours
  - Deliverable: github-mcp-integration-guide.md with all steps, expected output, troubleshooting

- [ ] **MUST**: Create security guidance document
  - Acceptance: Third-party server risks explained, evaluation checklist, best practices, official guidance
  - Reference: Spec Risk 4 (MCP Server Security Concerns), official Anthropic recommendations
  - Effort: 3 hours
  - Deliverable: mcp-security-guidance.md with permission scoping, trust evaluation, warnings

- [ ] **MUST**: Design 4 end-to-end workflow examples
  - Acceptance: Each workflow shows complete Claude Code + MCP task; expected output; learning points
  - Effort: 5 hours
  - Workflows:
    - [ ] Explore a codebase using file system MCP
    - [ ] Query GitHub issues while debugging
    - [ ] Use database MCP to validate assumptions
    - [ ] Combine multiple MCP servers in one task
  - Deliverable: workflow-examples.md with complete step-by-step instructions for each

- [ ] **MUST**: Write Lesson 5 - Connecting MCP Servers and Common Workflows (complete content)
  - Acceptance: 2200-2500 words, practical workflow examples, Docusaurus-ready
  - Reference: MCP research, GitHub integration guide, workflow examples, output style
  - Effort: 8 hours
  - Includes:
    - [ ] What is MCP? (definition, why it matters)
    - [ ] MCP architecture diagram (client-server-tools relationship)
    - [ ] Why MCP enables paradigm shift (access to external context)
    - [ ] Survey of available MCP servers (GitHub, PostgreSQL, File System, etc.)
    - [ ] Choose your first MCP (decision guidance, GitHub recommended)
    - [ ] Step-by-step GitHub MCP installation
      - [ ] Understanding claude mcp add command
      - [ ] Configuration walkthrough
      - [ ] Verification steps
    - [ ] Using MCP in practice
      - [ ] Querying GitHub data in Claude Code
      - [ ] Incorporating MCP results into tasks
      - [ ] End-to-end workflow example
    - [ ] Security guidance section (PROMINENT)
      - [ ] Third-party server risks
      - [ ] How to evaluate trustworthiness
      - [ ] Permission scoping best practices
      - [ ] Official Anthropic recommendations
    - [ ] Troubleshooting MCP connections (error cases and solutions)
    - [ ] Common Workflows section
      - [ ] Workflow 1: Explore codebase
      - [ ] Workflow 2: Query GitHub issues
      - [ ] Workflow 3: Database validation
      - [ ] Workflow 4: Multi-MCP tasks
    - [ ] Next steps (MCP as you grow)
    - [ ] YAML frontmatter (sidebar_position: 5)
  - Deliverable: `05-mcp-servers-and-workflows.md`

### Code Examples and Exercises

- [ ] **MUST**: Create MCP server reference table
  - Acceptance: Table with name, purpose, use cases, security notes for 8+ servers
  - Effort: 2 hours
  - Deliverable: mcp-servers-reference.md

- [ ] **MUST**: Design hands-on exercise: Connect GitHub MCP
  - Acceptance: Step-by-step instructions, sample task using MCP, success verification
  - Effort: 2.5 hours
  - Deliverable: Exercise with solution

- [ ] **SHOULD**: Create alternative MCP server tutorial (PostgreSQL or similar)
  - Acceptance: Alternative to GitHub for learners with different needs
  - Effort: 2.5 hours
  - Deliverable: alternative-mcp-tutorial.md

- [ ] **MUST**: Create troubleshooting guide for MCP connections
  - Acceptance: 8+ common errors with solutions, prevention tips
  - Effort: 2.5 hours
  - Deliverable: mcp-troubleshooting-guide.md

### Review and Polish

- [ ] **SHOULD**: Peer review for technical depth
  - Acceptance: Reviewer understands MCP architecture and practical application
  - Effort: 2 hours

- [ ] **MUST**: Technical accuracy of GitHub MCP walkthrough
  - Acceptance: Walkthrough tested, commands verified, output current
  - Reference: GitHub MCP documentation, Claude Code docs
  - Effort: 2.5 hours

- [ ] **MUST**: Security review of MCP section
  - Acceptance: Security guidance reviewed by someone with AppSec knowledge
  - Reference: Spec Risk 4 mitigation, official recommendations
  - Effort: 2 hours

- [ ] **MUST**: Hands-on exercise testing
  - Acceptance: Exercise completable in 20-25 minutes; learner successfully uses MCP data
  - Effort: 2 hours

- [ ] **SHOULD**: Cross-reference and integration check
  - Acceptance: Lesson 5 references Lessons 1-4 appropriately; together they tell complete story
  - Effort: 1.5 hours

**Lesson 5 Subtotal**: 40.5 hours | **Status**: Sequential (depends on Lesson 4 completion)

---

## Phase 6: Integration and Finalization

### Cross-Lesson Integration

- [ ] **MUST**: Create chapter-level overview/introduction
  - Acceptance: Overview shows how lessons connect, what readers will learn, time commitment
  - Reference: All 5 lessons, chapter architecture
  - Effort: 2 hours
  - Deliverable: Chapter intro section or README.md for chapter directory

- [ ] **MUST**: Create chapter-level reflection prompt
  - Acceptance: Reflection connects all lessons, helps readers articulate learning, forward-looking
  - Effort: 1 hour
  - Deliverable: Final reflection section for Lesson 5

- [ ] **SHOULD**: Create chapter-level learning objectives summary
  - Acceptance: Consolidated objectives for chapter-level assessment
  - Reference: Learning Objectives skill, all 5 lesson objectives
  - Effort: 1.5 hours
  - Deliverable: Learning objectives summary for chapter README

- [ ] **MUST**: Verify cross-references between lessons
  - Acceptance: All references ("as we saw in Lesson X") are accurate and helpful
  - Effort: 1.5 hours

### Documentation and Metadata

- [ ] **MUST**: Create Docusaurus _category_.json for chapter
  - Acceptance: JSON configures lesson ordering, chapter description for sidebar
  - Reference: Docosaurus documentation
  - Effort: 0.5 hours
  - Deliverable: _category_.json

- [ ] **MUST**: Create chapter README.md (overview for chapter directory)
  - Acceptance: Chapter overview, learning objectives, prerequisites, time estimate
  - Reference: Docosaurus conventions, chapter structure
  - Effort: 1.5 hours
  - Deliverable: README.md with Chapter 5 introduction

- [ ] **SHOULD**: Create supplementary resources list
  - Acceptance: Links to official docs, recommended further reading, video resources
  - Effort: 1 hour
  - Deliverable: supplementary-resources.md

### Quality Assurance and Review

- [ ] **MUST**: Full chapter pedagogical review
  - Acceptance: Reviewer confirms learning objectives met, content clear, scaffolding effective
  - Reference: Plan and all 5 lessons
  - Effort: 3 hours
  - Stakeholders: Main Claude or pedagogical reviewer

- [ ] **MUST**: Full chapter technical accuracy review
  - Acceptance: All commands, configurations, workflows verified current; no deprecated syntax
  - Reference: Claude Code official documentation (v2025+), MCP documentation
  - Effort: 3 hours
  - Stakeholders: Technical expert familiar with Claude Code

- [ ] **MUST**: Accessibility and clarity review
  - Acceptance: No gatekeeping language, clear explanations, examples diverse and inclusive
  - Reference: Principle 8 (Accessibility), constitution guidance
  - Effort: 2 hours

- [ ] **MUST**: Bias and representation check
  - Acceptance: Examples represent diverse perspectives, no stereotypes, inclusive language
  - Reference: Principle 8, Book Gaps Checklist
  - Effort: 1.5 hours

- [ ] **SHOULD**: Cross-chapter coherence check (with Ch 1-4 and Ch 6-8)
  - Acceptance: Chapter integrates seamlessly with prior/subsequent chapters
  - Effort: 2 hours

- [ ] **MUST**: Spell check, grammar review, style consistency
  - Acceptance: No typos, grammatically correct, consistent with style guide
  - Effort: 2 hours
  - Tools: Automated checks + human review

- [ ] **MUST**: Docosaurus build validation
  - Acceptance: All .md files parse correctly, frontmatter valid, no broken links
  - Effort: 1 hour
  - Deliverable: Build log showing zero errors/warnings

### Final Preparation

- [ ] **MUST**: Create instructor/facilitator notes (optional, NICE-TO-HAVE for publication)
  - Acceptance: Teaching tips, common student questions, discussion starters
  - Effort: 3 hours
  - Deliverable: instructor-notes.md (separate from published lesson)

- [ ] **SHOULD**: Create learner checklist/progress tracker
  - Acceptance: Checklist showing lesson objectives and success criteria
  - Effort: 1.5 hours
  - Deliverable: learner-checklist.md

- [ ] **MUST**: Create final author notes (for future updates)
  - Acceptance: Notes on volatile content, maintenance triggers, known issues, update reminders
  - Reference: Update Triggers section in spec
  - Effort: 2 hours
  - Deliverable: author-maintenance-notes.md (private file for future maintenance)

**Integration and Finalization Subtotal**: 31 hours | **Status**: Sequential (after all lessons complete)

---

## Overall Effort Summary

| Phase | Lesson(s) | Hours | Duration |
|-------|-----------|-------|----------|
| Phase 1 | Lesson 1 | 12.5 h | 1-2 weeks |
| Phase 2 | Lesson 2 | 29.5 h | 1-2 weeks |
| Phase 3 | Lesson 3 | 25 h | 1-2 weeks |
| Phase 4 | Lesson 4 | 31 h | 1-2 weeks |
| Phase 5 | Lesson 5 | 40.5 h | 2-3 weeks |
| Phase 6 | Integration | 31 h | 1-2 weeks |
| **TOTAL** | **All** | **169.5 h** | **8-11 weeks** |

**Note**: Phases 1-5 are sequential; Phase 6 can begin as each lesson completes. With parallel work on multiple phases, actual calendar time could be 6-8 weeks.

---

## Acceptance Criteria (Definition of Done)

### All Chapters - Mandatory

- [ ] All 5 lessons written and complete (2000-2500 words each)
- [ ] All lessons have YAML frontmatter with sidebar_position and description
- [ ] All learning objectives are measurable and use appropriate Bloom's taxonomy
- [ ] All lessons follow output style format (from `.claude/output-styles/lesson.md`)
- [ ] Chapter integrates with 8 mandatory domain skills contextually
- [ ] All code examples tested and working
- [ ] All troubleshooting sections address real errors
- [ ] Accessibility requirements met (Grade 7 reading level, no gatekeeping)
- [ ] All 17 functional requirements covered
- [ ] All 10 success criteria addressed
- [ ] No unverified technical claims
- [ ] Docosaurus build succeeds with zero warnings
- [ ] No placeholder text or TODOs remain

### Hybrid Chapter Specific

- [ ] Lesson 1 (narrative) is engaging, well-structured, clear
- [ ] Lessons 2-5 (technical) have working code examples, exercises, assessments
- [ ] Distinction between narrative and technical sections is clear to reader
- [ ] Progressive complexity appropriate (L1 simple → L5 complex)

### Security and Risk Mitigation

- [ ] MCP security guidance is prominent and thorough
- [ ] Authentication complexity addressed with clear decision tree
- [ ] Platform-specific installation failures mitigated with fallbacks
- [ ] Documentation volatility flagged with version dates and maintenance notes
- [ ] Cognitive overload prevented through scaffolding and optional paths

---

## Success Metrics (Validation)

After all tasks complete, the chapter is successful when:

✅ Readers can follow Lesson 2 installation and have working Claude Code within 20 minutes
✅ Readers can create a subagent (Lesson 3) in 15-20 minutes hands-on time
✅ Readers can create an Agent Skill (Lesson 4) in 20-25 minutes hands-on time
✅ Readers can connect MCP server (Lesson 5) in 20-25 minutes hands-on time
✅ Success rates match spec targets: SC-002 (95%), SC-004 (80%), SC-005 (80%), SC-006 (75%)
✅ Troubleshooting sections address 90%+ of common errors learners encounter
✅ No unresolved technical accuracy issues
✅ Chapter is publication-ready with zero warnings in Docosaurus build

---

## Dependencies and Sequencing

**Task Dependencies**:
- Lesson 2 depends on Lesson 1 (motivation established)
- Lesson 3 depends on Lesson 2 (tool must be working)
- Lesson 4 depends on Lesson 3 (subagent context needed)
- Lesson 5 depends on Lesson 2 (tool working) + Lessons 3-4 optional but recommended
- Integration phase depends on all 5 lessons

**Parallel Opportunities**:
- Content outlines (Lesson 1-5) can be created in parallel
- Testing and research (Lesson 2-5) can happen while Lesson 1 is being written
- Code examples (Lesson 2-5) can be developed while content is being drafted

---

## Handoff Criteria

This task checklist is ready for handoff to lesson-writer subagent when:

✅ Approved lesson plan is available (`plan.md`)
✅ All task descriptions are specific and testable
✅ Acceptance criteria are clear and objective
✅ Dependencies and sequencing are explicit
✅ Effort estimates are realistic
✅ Reference materials (output styles, constitution, examples) are accessible

**Current Status**: Ready for Lesson-Writer Subagent

Next step: `/sp.implement` to begin Lesson 1 content creation
