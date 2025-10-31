# Feature Specification: Chapter 8 - Git & GitHub for AI-Driven Development

**Feature Branch**: `001-chapter-8-git-github`
**Created**: 2025-10-31
**Status**: Draft
**Input**: User description: "Design chapter 8. Check the part 2 goal provided at book-source\docs\02-AI-Tool-Landscape\README.md and the context here context\09_chap8_specs\"

## Overview

Chapter 8 is the final chapter of Part 2: AI Tool Landscape. It teaches version control using Git and GitHub specifically in the context of AI-driven development workflows. This chapter is critical because Git provides the safety net that makes AI-assisted development viable—every change is tracked, every experiment can be rolled back, and every collaboration is auditable.

The chapter is structured in two parts:
- **Part I: Git Commands** - Essential Git workflows and commands for AI development
- **Part II: Natural Language Prompts for AI CLI Tools** - How to request AI tools execute Git operations via natural language

**Target Audience**: Beginners with no terminal or version control experience (prerequisite: completion of Part 1 and Chapters 5-7 of Part 2)

**Estimated Duration**: 3-4 hours

**Reading Level**: Grade 7 baseline with technical terminology defined on first use

## User Scenarios & Testing

### User Story 1 - Creating Safe Checkpoints Before AI Changes (Priority: P1)

A beginner developer wants to let Claude Code refactor their Python project, but they're worried the AI might break something. They need to create a safe checkpoint they can roll back to if the AI's changes don't work.

**Why this priority**: This is the most fundamental safety practice when working with AI tools. Without this, learners risk losing their work and won't trust AI assistance. This is the core value proposition of using Git with AI development.

**Independent Test**: Can be fully tested by creating a checkpoint before making changes, making modifications (simulated or real), and successfully rolling back to the checkpoint. Delivers immediate safety value.

**Acceptance Scenarios**:

1. **Given** a working Python project with uncommitted changes, **When** the learner commits their work with a descriptive message, **Then** they have a safe checkpoint they can return to
2. **Given** AI has made changes that broke the code, **When** the learner runs `git reset --hard HEAD~1`, **Then** their code returns to the working state before AI changes
3. **Given** a learner wants to experiment with AI-generated code, **When** they create a branch, let AI make changes, test them, and decide to keep or discard, **Then** their main branch remains safe and untouched

---

### User Story 2 - Collaborating on AI-Generated Code via Pull Requests (Priority: P2)

A learner working in a team needs to share their AI-generated feature with teammates for code review before merging it into the main project. They need to create a pull request, address feedback, and merge safely.

**Why this priority**: Pull requests are essential for team collaboration and professional workflows. While not needed for solo learners initially, this is required for career readiness and real-world projects.

**Independent Test**: Can be tested independently by creating a feature branch, pushing to GitHub, creating a PR, simulating review comments, addressing feedback, and merging. Delivers collaboration capability.

**Acceptance Scenarios**:

1. **Given** a completed feature on a branch, **When** the learner pushes to GitHub and creates a pull request with description, **Then** teammates can review and comment on the changes
2. **Given** review feedback on a PR, **When** the learner makes changes, commits, and pushes again, **Then** the PR updates automatically with new commits
3. **Given** an approved pull request, **When** the learner merges it on GitHub, **Then** the feature is integrated into main and the branch can be deleted

---

### User Story 3 - Using Natural Language Prompts for Git Workflows (Priority: P3)

A beginner who finds Git commands intimidating wants to use Claude Code or Gemini CLI to execute Git operations via natural language requests instead of memorizing command syntax.

**Why this priority**: This is an enhancement that makes Git more accessible to beginners, but learners should understand basic Git concepts first. Natural language prompts are a convenience layer, not a replacement for understanding.

**Independent Test**: Can be tested by providing natural language prompts to AI CLI tools and verifying they execute the correct Git commands. Delivers accessibility value for beginners.

**Acceptance Scenarios**:

1. **Given** uncommitted changes in a project, **When** the learner asks Claude Code "Stage all my changes and commit with message 'Add user authentication'", **Then** the AI executes `git add .` and `git commit -m "Add user authentication"`
2. **Given** a need to create a feature branch, **When** the learner requests "Create a new branch called payment-feature and switch to it", **Then** the AI executes `git checkout -b payment-feature`
3. **Given** merge conflicts after pulling, **When** the learner asks "Help me resolve the merge conflicts in auth.js", **Then** the AI explains the conflict markers and guides resolution

---

### User Story 4 - Understanding Git History and Blame for AI Changes (Priority: P4)

A developer needs to understand which AI tool or which session made specific changes to their codebase over time, especially when multiple AI-assisted sessions have modified the same files.

**Why this priority**: This is an advanced workflow for tracking AI contributions over time. Useful for auditing and learning, but not essential for basic safety.

**Independent Test**: Can be tested by creating commits with AI attribution, then using `git log` and `git blame` to trace authorship and changes. Delivers auditability.

**Acceptance Scenarios**:

1. **Given** a file modified by AI in multiple sessions, **When** the learner runs `git blame filename`, **Then** they see line-by-line authorship with commit messages indicating which AI tool made changes
2. **Given** a project with AI-generated commits, **When** the learner reviews `git log --oneline`, **Then** they see commit messages with AI attribution (e.g., "[AI] Claude - Add error handling")
3. **Given** unexpected behavior, **When** the learner uses `git log` to trace when changes were introduced, **Then** they can identify which AI session or commit caused the issue

---

### Edge Cases

- **What happens when AI makes uncommitted changes and the learner switches branches?** Git will prevent the branch switch or carry changes over (depending on conflicts). Learners should commit or stash before switching.
- **What if learners accidentally commit sensitive API keys?** The chapter must teach `.gitignore` practices and explain that removing from history requires `git filter-branch` or BFG Repo-Cleaner (advanced, with warning about exposed keys).
- **How does the system handle merge conflicts from AI-generated code?** The chapter must explain conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and show how to resolve manually or ask AI for help.
- **What if learners delete their local branch before pushing?** Changes are lost unless committed. The chapter emphasizes "commit early, commit often" and push for backup.
- **What happens when multiple AI tools edit the same file?** Standard Git merge conflicts. The chapter shows how to use AI tools to help resolve conflicts.
- **What if GitHub authentication fails?** Chapter must cover Personal Access Tokens (PAT) and SSH keys as modern authentication methods.

## Requirements

### Functional Requirements

#### Part I: Git Commands

- **FR-001**: Chapter MUST explain why Git matters specifically for AI-driven development (safety net, rollback capability, collaboration)
- **FR-002**: Chapter MUST provide platform-specific installation instructions for Git (Windows, Mac, Linux)
- **FR-003**: Chapter MUST teach essential Git configuration (username, email)
- **FR-004**: Chapter MUST demonstrate the basic Git workflow: `git status` → `git add` → `git commit` → `git push`
- **FR-005**: Chapter MUST teach branch creation, switching, and merging for safe AI experimentation
- **FR-006**: Chapter MUST explain undoing changes with `git checkout`, `git reset --soft`, and `git reset --hard`
- **FR-007**: Chapter MUST demonstrate pull request workflows: creating PRs, reviewing, addressing feedback, merging
- **FR-008**: Chapter MUST teach `.gitignore` creation for common AI development files (.env, node_modules, venv, __pycache__)
- **FR-009**: Chapter MUST explain GitHub authentication (Personal Access Tokens and SSH keys)
- **FR-010**: Chapter MUST provide best practices for commit messages with AI attribution (e.g., "[AI] Claude - Implement feature X")
- **FR-011**: Chapter MUST include a "Quick Reference Card" summarizing the most common commands
- **FR-012**: Chapter MUST include "Common AI Development Scenarios" showing realistic workflows (safe checkpoints, testing refactors, sharing code, getting features reviewed)

#### Part II: Natural Language Prompts

- **FR-013**: Chapter MUST provide natural language prompt alternatives for every essential Git command taught in Part I
- **FR-014**: Chapter MUST demonstrate complex workflow prompts combining multiple Git operations (e.g., "Create safety checkpoint, let me test AI changes, then help me decide to merge or discard")
- **FR-015**: Chapter MUST include troubleshooting prompts for common Git problems (merge conflicts, rejected pushes, wrong branch commits)
- **FR-016**: Chapter MUST show best practices for AI CLI conversations: being specific, asking for explanations, requesting safety checks, combining with code generation
- **FR-017**: Chapter MUST include prompt examples for file management (.gitignore creation, PR template generation)

### Key Entities

- **Git Repository**: Local version-controlled project directory initialized with `git init` or cloned from remote
  - Attributes: working directory, staging area, commit history, branches, remote connections
  - Relationships: connected to remote repository (GitHub), contains commits and branches

- **Commit**: Snapshot of project state at a specific point in time
  - Attributes: unique hash, author, timestamp, commit message, parent commit(s), file changes
  - Relationships: part of branch history, linked to previous commit(s)

- **Branch**: Independent line of development diverging from main codebase
  - Attributes: name, pointer to latest commit, tracking remote branch
  - Relationships: can be merged into other branches, tracks remote counterpart

- **Pull Request**: Proposed changes from one branch to another on GitHub
  - Attributes: title, description, source branch, target branch, status (open/merged/closed), reviews, comments
  - Relationships: associated with commits, linked to GitHub issues, has reviewers

- **Remote Repository**: Server-hosted copy of repository (typically GitHub)
  - Attributes: URL, name (usually "origin"), branches, collaborators
  - Relationships: connected to local repository, receives pushes, provides pulls

## Success Criteria

### Measurable Outcomes

- **SC-001**: Learners can create a Git repository and make their first commit within 5 minutes of starting the chapter
- **SC-002**: Learners can create a safe checkpoint before AI changes and successfully roll back if needed (tested via exercise)
- **SC-003**: Learners can create a feature branch, make changes, and merge back to main without data loss (100% success in exercise)
- **SC-004**: Learners can create a pull request on GitHub, simulate review feedback, and merge (tested via guided exercise)
- **SC-005**: Learners can translate at least 10 Git commands into equivalent natural language prompts for AI CLI tools
- **SC-006**: Learners understand when to commit (before AI changes, after completing work, before switching branches) as evidenced by self-assessment
- **SC-007**: 90% of learners successfully complete the end-of-chapter project: "Create a Git repository for your AI-assisted project, make multiple commits with AI attribution, create a feature branch for experimentation, and push to GitHub"
- **SC-008**: Learners can identify and use appropriate Git commands for 5 common AI development scenarios without referencing documentation

## Scope

### In Scope

- Git installation and basic configuration
- Essential Git workflow commands (status, add, commit, push, pull)
- Branch creation, switching, and merging
- Undoing changes and time travel (reset, checkout)
- Pull request workflows on GitHub
- `.gitignore` best practices for AI development projects
- GitHub authentication (PAT and SSH)
- Natural language prompts for all essential Git operations
- AI-specific commit message conventions
- Common AI development scenarios and troubleshooting

### Out of Scope

- Advanced Git topics (rebase, cherry-pick, submodules, hooks)
- Git internals and plumbing commands
- GitHub Actions and CI/CD (covered in later parts)
- GitFlow or other branching strategies (too advanced for beginners)
- Git GUIs (chapter focuses on CLI for consistency with AI CLI tools)
- Team workflow policies and governance
- Git performance optimization
- Monorepo management
- Advanced conflict resolution strategies

### Assumptions

1. Learners have completed Part 1 and Chapters 5-7 (Claude Code, Gemini CLI, Bash essentials)
2. Learners have a GitHub account or are willing to create one (free tier)
3. Learners have internet access for pushing/pulling to GitHub
4. Learners are working on personal computers where they can install software (not locked-down corporate machines)
5. Learners have already created at least one simple Python project to version control (from previous chapters)
6. Learners understand basic terminal navigation from Chapter 7 (Bash Essentials)

### Dependencies

- **Prerequisite Chapters**: Chapters 5 (Claude Code), 6 (Gemini CLI), 7 (Bash Essentials)
- **External Tools**: Git CLI, GitHub account, AI CLI tools (Claude Code or Gemini CLI)
- **Platform Requirements**: Windows 10+, macOS 10.15+, or modern Linux distribution
- **Network Access**: Required for GitHub operations and API calls to AI tools

### Constraints

- **Time Constraint**: Chapter must be completable in 3-4 hours for target audience
- **Complexity Constraint**: Content must remain accessible to beginners with no prior Git experience
- **Platform Constraint**: All instructions must work on Windows, Mac, and Linux with platform-specific notes where necessary
- **Tool Constraint**: Natural language prompts must work with Claude Code and Gemini CLI (the two tools taught in Part 2)
- **GitHub Free Tier**: All features demonstrated must be available on GitHub's free tier
- **Security Constraint**: Must teach `.env` and secrets management from the start to prevent accidental key exposure

## Non-Goals

- Teaching advanced Git workflows beyond basic branching and merging
- Covering Git server administration or self-hosted alternatives
- Deep dive into Git internals or data structures
- Alternative version control systems (Mercurial, SVN, Perforce)
- GitHub enterprise features or organization-level management
- Git performance tuning for large repositories
- Code review best practices beyond basic PR workflow
- GitOps or infrastructure-as-code workflows
- Multi-repo coordination or monorepo strategies

## Risks and Mitigations

### Risk 1: Learners accidentally commit secrets (HIGH IMPACT)

**Impact**: Exposed API keys, passwords, or tokens can lead to security breaches and unexpected costs.

**Mitigation**:
- Introduce `.gitignore` in "Essential Setup" section (very early)
- Provide ready-to-use `.gitignore` templates for Python/Node.js projects
- Include explicit warning: "NEVER commit .env files"
- Show how to check what's staged before committing (`git status`, `git diff`)
- Include troubleshooting section: "What if I already committed a secret?"

### Risk 2: Learners fear "breaking everything" with Git commands (MEDIUM IMPACT)

**Impact**: Intimidation leads to avoiding Git, which defeats the purpose of learning it as a safety net.

**Mitigation**:
- Emphasize that Git is the safety net, not the danger
- Show rollback commands prominently (git reset, git checkout)
- Use reassuring language: "You can always undo this"
- Demonstrate safe experimentation with branches
- Include "Git Recovery" section with common "oops" scenarios

### Risk 3: Platform-specific installation issues (MEDIUM IMPACT)

**Impact**: Learners get stuck at installation and abandon the chapter.

**Mitigation**:
- Provide detailed platform-specific installation instructions
- Include troubleshooting subsection for common installation issues
- Offer alternative installation methods (package manager vs. installer)
- Include verification step: `git --version` to confirm installation
- Suggest asking AI CLI tools for platform-specific help

### Risk 4: GitHub authentication confusion with PAT/SSH (MEDIUM IMPACT)

**Impact**: Learners can't push to GitHub due to authentication failures.

**Mitigation**:
- Explain that passwords no longer work (deprecated by GitHub)
- Provide step-by-step PAT creation guide with screenshots
- Include SSH setup as alternative (with link to GitHub's official guide)
- Show error messages learners might see and how to fix them
- Recommend HTTPS + PAT for beginners (simpler than SSH)

### Risk 5: Merge conflict paralysis (LOW-MEDIUM IMPACT)

**Impact**: Learners encounter merge conflicts and don't know how to resolve them.

**Mitigation**:
- Explain conflict markers clearly with visual examples
- Show simple conflict resolution step-by-step
- Demonstrate asking AI tools to help understand conflicts
- Include "when to ask for help" guidance
- Provide escape hatch: `git merge --abort` to back out

## Validation Criteria

### Content Validation

- [ ] All Git commands are tested on Windows, Mac, and Linux
- [ ] All natural language prompts are tested with Claude Code and Gemini CLI
- [ ] All GitHub workflows are verified with free tier account
- [ ] All examples use realistic filenames and scenarios from AI development
- [ ] `.gitignore` templates are tested with actual Python/Node.js projects
- [ ] Authentication instructions (PAT/SSH) are current as of publication date

### Pedagogical Validation

- [ ] Chapter follows output style for "lesson.md" (defined in `.claude/output-styles/lesson.md`)
- [ ] All 9 domain skills are applied appropriately (learning objectives, scaffolding, examples, exercises, assessments, clarity, book scaffolding, AI-augmented teaching, evaluation)
- [ ] Content meets grade 7 reading level baseline
- [ ] No gatekeeping language ("obviously", "simply", "just")
- [ ] Progressive complexity: Part I builds foundation, Part II adds convenience layer
- [ ] Exercises are testable and have clear success criteria

### Alignment Validation

- [ ] Chapter aligns with Part 2 goals (tool literacy, hands-on practice, professional workflows)
- [ ] Prerequisites clearly stated and enforced (Chapters 5-7 completed)
- [ ] Forward bridge to Part 3 (Prompt & Context Engineering) established
- [ ] AI-first teaching philosophy applied throughout
- [ ] Spec-Kit Plus methodology referenced where appropriate (ADR for decisions, PHR for learning sessions)
- [ ] Modern standards enforced (no legacy Git workflows or deprecated GitHub features)

### Exercise Validation

- [ ] Minimum 5 hands-on exercises included (creating repo, making commits, branching, PR workflow, natural language prompts)
- [ ] Each exercise has clear acceptance criteria
- [ ] Exercises build progressively in complexity
- [ ] At least one comprehensive end-of-chapter project combining multiple skills
- [ ] Exercises are testable independently without manual review

### Accessibility Validation

- [ ] Platform-specific instructions provided for Windows/Mac/Linux where behavior differs
- [ ] Terminal commands include description of what they do
- [ ] Jargon defined on first use (commit, staging area, remote, fork, clone, etc.)
- [ ] Visual aids included for complex concepts (branch diagrams, PR workflow, conflict markers)
- [ ] Multiple explanation styles (text, code examples, scenarios, analogies)
- [ ] Free tier GitHub sufficient for all exercises
