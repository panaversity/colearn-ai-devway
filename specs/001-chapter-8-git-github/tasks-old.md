# Chapter 8: Git & GitHub for AI-Driven Development — Implementation Task Checklist

**Chapter Type**: Hybrid (Technical + Natural Language Prompts)
**Status**: Ready for Implementation
**Feature Branch**: `001-chapter-8-git-github`
**Estimated Total Effort**: 16-23 hours (assumes sequential lesson-by-lesson implementation)
**Story Points**: 21 (13 MUST, 5 SHOULD, 3 NICE-TO-HAVE)

---

## Overview

This task list breaks down the implementation of Chapter 8 (Git & GitHub for AI-Driven Development) into atomic, testable work units. Tasks are organized by phase and must be completed in dependency order. Each task has clear acceptance criteria and expected artifacts.

**Key Principle**: Implement lessons sequentially (Lesson 1 → 2 → 3 → 4 → 5), ensuring each lesson is complete before starting the next.

---

## Phase 1: Chapter Foundation & Lesson 1 (Conceptual Foundation)

### Task 1.1: Create Chapter README.md
**Priority**: MUST | **Effort**: 2h | **Depends On**: None
**Description**: Create the chapter overview document that summarizes learning objectives, structure, and prerequisites.

**Acceptance Criteria**:
- [ ] File: `specs/001-chapter-8-git-github/README.md` exists (canonical output style from `.claude/output-styles/chapter-readme.md`)
- [ ] Includes chapter title, number, and part assignment
- [ ] Learning objectives clearly stated (all 5 from plan.md)
- [ ] Prerequisites listed (Chapters 5-7, GitHub account)
- [ ] Chapter summary: 2-3 sentence overview of why Git matters
- [ ] Section overview: brief description of all 5 lessons
- [ ] Estimated duration: 3-4 hours of content, plus 1+ hour exercises
- [ ] Directory structure outlined: 5 lesson files + README.md
- [ ] No placeholder text or TODOs

**Example Sections**:
- Learning Outcomes (5 bullet points)
- Prerequisites (what learners must know)
- What You'll Build (end-of-chapter project)
- Chapter Structure (lesson titles and durations)
- Success Criteria (how to know you've mastered this chapter)

**Deliverable**: `specs/001-chapter-8-git-github/README.md`

---

### Task 1.2: Write Lesson 1 Content (Why Git Matters)
**Priority**: MUST | **Effort**: 2h | **Depends On**: Task 1.1
**Description**: Write the conceptual narrative lesson establishing why Git matters in AI-driven development.

**Acceptance Criteria**:
- [ ] File: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/01-lesson-1.md`
- [ ] YAML frontmatter: title, sidebar_position: 1, description
- [ ] Opening hook in first 2 paragraphs (engaging, concrete scenario)
- [ ] Three Problems Git Solves section with AI context:
  - [ ] Safety: experiment fearlessly
  - [ ] Collaboration: share code with teammates
  - [ ] Auditability: track AI contributions
- [ ] 4-5 real-world examples (AI refactor with rollback, team PR review, bug hunt with git log, accidental secret, etc.)
- [ ] Analogies section: Git compared to video games, film, sports, other domains
- [ ] Simple diagram or ASCII art showing branches as experiment paths
- [ ] Reflection prompts (2-3 thought-provoking questions)
- [ ] Transition to Lesson 2 bridging from "Why Git?" to "How to use Git?"
- [ ] Word count: 1,500-2,000 words
- [ ] Reading level: grade 7 baseline, no jargon (or jargon defined)
- [ ] No code examples (this is conceptual only)
- [ ] Follows lesson output style from `.claude/output-styles/lesson.md`
- [ ] No placeholder text, TODOs, or missing content

**Tone**: Motivational, narrative-driven, non-technical

**Key Points**:
- Opening hook captures attention immediately
- Real-world examples are concrete and relatable
- Emphasizes safety net metaphor (not scary, not complex)
- Preview of Part II (natural language prompts make Git accessible)
- Transitions naturally to Lesson 2

**Deliverable**: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/01-lesson-1.md`

---

## Phase 2: Lesson 2 (Git Essentials)

### Task 2.1: Write Lesson 2 Content (Installation & Basic Workflow)
**Priority**: MUST | **Effort**: 4h | **Depends On**: Task 1.2
**Description**: Write the technical lesson teaching Git installation and basic workflow (status → add → commit → push).

**Acceptance Criteria**:
- [ ] File: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/02-lesson-2.md`
- [ ] Opening hook: "Every commit is a story. Let's tell good ones."
- [ ] Part I: Installation & Setup (30 min read)
  - [ ] Windows installation (Git Bash, step-by-step)
  - [ ] macOS installation (Homebrew or direct installer)
  - [ ] Linux installation (apt-get/brew commands)
  - [ ] Verification command: `git --version` (with expected output)
  - [ ] Configuration: `git config --global user.name`, `user.email`
  - [ ] Troubleshooting: common installation issues and fixes
  - [ ] Platform-specific callout boxes for Windows/Mac/Linux differences
- [ ] Part II: The Core Workflow - Show Then Explain (15 min)
  - [ ] Complete workflow demonstration (4-5 code blocks with outputs)
  - [ ] Scenario: Initialize new repo → check status → add file → commit → push
  - [ ] Platform-specific notes where commands differ
  - [ ] Expected output for each command
  - [ ] Comments explain what each output means
- [ ] Part III: Three-Stage Concept (10 min)
  - [ ] Diagram or ASCII art: working directory → staging area → repository
  - [ ] Explanation: why three stages exist, when each matters
  - [ ] `git status` output walkthrough (untracked, modified, staged states)
- [ ] Part IV: Reading Git Output (10 min)
  - [ ] Understanding `git status` output (each line explained)
  - [ ] Understanding `git log --oneline` output
  - [ ] Understanding error messages
  - [ ] Example: what does "Your branch is ahead of 'origin/main'" mean?
- [ ] Part V: Commit Messages with AI Attribution (10 min)
  - [ ] Best practices: present tense, descriptive, actionable
  - [ ] AI attribution pattern: `[AI] Claude - Add error handling`
  - [ ] Why this matters: auditability, evolution tracking
  - [ ] Examples: good vs. poor commit messages
- [ ] 3-4 complete, runnable workflow examples (Python project, Node.js project, etc.)
- [ ] All code blocks include expected output
- [ ] No jargon without definition
- [ ] Word count: 2,000-2,500 words
- [ ] Follows lesson output style
- [ ] No placeholder text

**Key Elements**:
- Show-then-explain pattern (show workflow first, explain components after)
- Platform-specific instructions clearly marked
- Commit message examples emphasize AI context
- All output shown (what learner will see)
- Heavy scaffolding (step-by-step, not rushed)

**Deliverable**: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/02-lesson-2.md`

---

### Task 2.2: Design Lesson 2 Exercises
**Priority**: MUST | **Effort**: 2h | **Depends On**: Task 2.1
**Description**: Create 5 hands-on exercises for Lesson 2, each with clear acceptance criteria.

**Acceptance Criteria**:
- [ ] 5 exercises provided (same file as lesson content, in separate section)
- [ ] Exercise 1: Install Git and verify (`git --version`)
  - [ ] Expected: Version number output (e.g., "git version 2.42.0")
  - [ ] Platform-specific troubleshooting notes
- [ ] Exercise 2: Configure user identity
  - [ ] Commands: `git config --global user.name "Your Name"`
  - [ ] Verification: `git config --list` shows new settings
- [ ] Exercise 3: Initialize a new repository
  - [ ] Create test directory, initialize with `git init`
  - [ ] Success: `.git` folder exists
- [ ] Exercise 4: Make your first commit
  - [ ] Create a file, stage it, commit with good message
  - [ ] Expected: commit message includes AI attribution pattern (if done by AI)
  - [ ] Success: `git log --oneline` shows the commit
- [ ] Exercise 5: View commit history
  - [ ] Run `git log --oneline`, interpret output
  - [ ] Understand commit hash, message, author
  - [ ] Success: can identify the 5 most recent commits
- [ ] Each exercise:
  - [ ] Has clear prompt (what to do)
  - [ ] Expected output provided
  - [ ] Success criteria defined (how to verify you did it right)
  - [ ] Time estimate (5-15 min each)
  - [ ] Hints for struggling learners
  - [ ] Cross-platform notes if applicable

**Deliverable**: Integrated into `01-lesson-2.md` (Exercises section at end)

---

### Task 2.3: Create Lesson 2 Assessment
**Priority**: SHOULD | **Effort**: 1h | **Depends On**: Task 2.2
**Description**: Create a 5-10 question self-assessment for Lesson 2.

**Acceptance Criteria**:
- [ ] 8-10 self-check questions provided
- [ ] Mix of question types:
  - [ ] Conceptual: "What is the staging area and why does it exist?"
  - [ ] Procedural: "How do you verify Git is installed?"
  - [ ] Application: "You need to create a checkpoint before AI refactoring. What command do you run?"
- [ ] Answer key provided with explanations
- [ ] Questions test multiple Bloom's levels (understand, apply)
- [ ] No questions require running commands (self-assessed)

**Deliverable**: Integrated into `02-lesson-2.md` (Assessment section)

---

## Phase 3: Lesson 3 (Safe Experimentation)

### Task 3.1: Write Lesson 3 Content (Branches, Checkpoints, Rollback)
**Priority**: MUST | **Effort**: 4h | **Depends On**: Task 2.2
**Description**: Write the technical lesson teaching safe experimentation, branches, and rollback.

**Acceptance Criteria**:
- [ ] File: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/03-lesson-3.md`
- [ ] Opening hook: "Before you let Claude Code refactor your project, save a checkpoint."
- [ ] Part I: The Checkpoint Pattern (10 min)
  - [ ] Commit as checkpoint: `git commit -m "Stable state before AI refactoring"`
  - [ ] Reading commit history: what each checkpoint represents
  - [ ] Best practice: commit before every AI session
  - [ ] Example workflow: stable state → make changes → test → decide to keep/discard
- [ ] Part II: Branch-Based Experimentation (15 min)
  - [ ] Why branches exist: safe isolation, experiment without affecting main
  - [ ] Creating: `git checkout -b feature-branch`
  - [ ] Listing: `git branch`
  - [ ] Switching: `git checkout main`
  - [ ] Use case: let Claude Code experiment on branch, test, merge or discard
  - [ ] Diagram: visual representation of branches diverging and merging
- [ ] Part III: Undoing Changes - The Safety Net (15 min)
  - [ ] Soft reset: `git reset --soft HEAD~1` (undo commit, keep changes)
  - [ ] Hard reset: `git reset --hard HEAD~1` (undo commit and discard)
  - [ ] Revert: `git revert COMMIT_HASH` (safe alternative)
  - [ ] When to use each (with specific scenarios)
  - [ ] WARNING box: be careful with hard reset (irreversible for uncommitted changes)
- [ ] Part IV: Merging Branches (15 min)
  - [ ] Fast-forward merge (linear history)
  - [ ] Three-way merge (creating merge commit)
  - [ ] Merge conflicts: what they are, why they happen
  - [ ] Conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
  - [ ] Simple conflict resolution (choosing one side or manually merging)
  - [ ] Asking AI to help understand conflicts
  - [ ] `git merge --abort` to back out of merge
- [ ] Part V: Stashing (10 min)
  - [ ] `git stash` to save uncommitted work temporarily
  - [ ] `git stash list` to see stashed changes
  - [ ] `git stash pop` to restore
  - [ ] Use case: need to switch branches but not ready to commit
- [ ] 4-5 complete workflow examples:
  - [ ] Checkpoint → experiment → success → merge
  - [ ] Checkpoint → experiment → failure → rollback
  - [ ] Create and resolve simple merge conflict
  - [ ] All with expected output
- [ ] Visual diagrams showing branch creation, merging, conflicts
- [ ] Troubleshooting section: "Accidentally committed on wrong branch?", "Merge conflicts scaring you?"
- [ ] Word count: 2,000-2,500 words
- [ ] All code blocks include expected output
- [ ] Follows lesson output style
- [ ] No placeholder text

**Key Elements**:
- Emphasize safety throughout (checkpoint, rollback, stash are safety tools)
- Show complete workflows (not isolated commands)
- Explain conflict markers clearly with visual examples
- Offer AI assistance for conflict resolution
- Progressive complexity: checkpoint → branches → undoing → merging → stashing

**Deliverable**: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/03-lesson-3.md`

---

### Task 3.2: Design Lesson 3 Exercises
**Priority**: MUST | **Effort**: 2.5h | **Depends On**: Task 3.1
**Description**: Create 6 hands-on exercises for Lesson 3, building from checkpoints to conflict resolution.

**Acceptance Criteria**:
- [ ] 6 exercises provided
- [ ] Exercise 1: Create a checkpoint commit
  - [ ] Make changes, commit with descriptive message
  - [ ] Success: `git log --oneline` shows the checkpoint
- [ ] Exercise 2: Create a feature branch
  - [ ] `git checkout -b feature-new-feature`
  - [ ] Make changes on the branch
  - [ ] Success: branch exists and has new commits
- [ ] Exercise 3: Switch between branches
  - [ ] Verify file contents change when switching branches
  - [ ] Success: main branch unchanged, feature branch has changes
- [ ] Exercise 4: Merge the branch back to main
  - [ ] Switch to main, run `git merge feature-new-feature`
  - [ ] Success: changes are now on main, branch can be deleted
- [ ] Exercise 5: Rollback a commit using `git reset --hard`
  - [ ] Create intentional "bad" commit
  - [ ] Rollback with `git reset --hard HEAD~1`
  - [ ] Success: file state returned to pre-commit state
- [ ] Exercise 6: Create and resolve a merge conflict
  - [ ] Two branches edit same file in conflicting ways
  - [ ] Manually resolve conflict markers
  - [ ] Complete merge
  - [ ] Success: file merged correctly, conflict markers gone
- [ ] Each exercise:
  - [ ] Clear prompt and expected outcome
  - [ ] Expected `git log` or `git status` output
  - [ ] Hints for troubleshooting
  - [ ] Time estimate: 8-15 min each
  - [ ] Success criteria (how to verify completion)

**Deliverable**: Integrated into `03-lesson-3.md` (Exercises section)

---

### Task 3.3: Create Lesson 3 Assessment
**Priority**: SHOULD | **Effort**: 1h | **Depends On**: Task 3.2
**Description**: Create self-assessment for Lesson 3.

**Acceptance Criteria**:
- [ ] 8-10 self-check questions
- [ ] Question types:
  - [ ] Conceptual: "What's the difference between `git reset --soft` and `git reset --hard`?"
  - [ ] Scenario-based: "You accidentally committed on the wrong branch. What do you do?"
  - [ ] Application: "When would you use `git stash` instead of creating a branch?"
- [ ] Answer key with explanations
- [ ] Tests understanding of safety concepts

**Deliverable**: Integrated into `03-lesson-3.md` (Assessment section)

---

## Phase 4: Lesson 4 (Pull Requests)

### Task 4.1: Write Lesson 4 Content (PR Workflow)
**Priority**: MUST | **Effort**: 3.5h | **Depends On**: Task 3.2
**Description**: Write lesson teaching pull requests and team collaboration via GitHub.

**Acceptance Criteria**:
- [ ] File: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/04-lesson-4.md`
- [ ] Opening hook: "Pull requests let teammates review AI code before it ships."
- [ ] Part I: Understanding PRs (10 min)
  - [ ] What is a PR: proposed changes from one branch to another
  - [ ] Why PRs: code review, discussion, auditing
  - [ ] PR workflow: push branch → create PR → review → iterate → merge
  - [ ] GitHub interface: PR page anatomy (description, commits, files changed, comments)
  - [ ] PR vs. commit: PR includes discussion, commits are history
- [ ] Part II: Creating a PR (15 min)
  - [ ] Push branch to GitHub: `git push -u origin feature-branch`
  - [ ] Expected: output shows branch pushed to remote
  - [ ] GitHub UI: click "Compare & Pull Request" button
  - [ ] PR title best practices (clear, descriptive, actionable)
  - [ ] PR description template (what, why, testing notes)
  - [ ] Example: PR description for AI-generated code (what Claude Code did, what to review)
  - [ ] Screenshots/descriptions of GitHub UI (create PR button, form fields)
- [ ] Part III: Reviewing Code (10 min)
  - [ ] What to look for in AI-generated code (security, logic, style)
  - [ ] Leaving comments and suggestions in GitHub
  - [ ] Requesting changes vs. approving
  - [ ] Re-reviewing after changes
  - [ ] Example: code review feedback on AI-generated function
- [ ] Part IV: Iteration and Feedback (10 min)
  - [ ] Making changes based on review feedback
  - [ ] Pushing new commits to PR (automatically updates)
  - [ ] Addressing comments
  - [ ] Optional: squashing commits before merge
  - [ ] Example: responding to feedback, pushing fix, updating PR
- [ ] Part V: Merging on GitHub (10 min)
  - [ ] Merge strategies: merge commit (default), squash, rebase
  - [ ] When to use each strategy
  - [ ] Delete branch after merge (cleanup)
  - [ ] Pulling merged changes locally: `git pull origin main`
  - [ ] Screenshots: merge button, merge strategy options
- [ ] Part VI: Handling PR Conflicts (10 min)
  - [ ] Merge conflicts on GitHub
  - [ ] Resolving conflicts locally:
    - [ ] Pull main: `git fetch origin`
    - [ ] Rebase: `git rebase origin/main`
    - [ ] Resolve markers, push
  - [ ] Or resolve via GitHub web UI (where available)
  - [ ] Asking AI to help understand conflict markers
  - [ ] Example: conflict resolution workflow
- [ ] 2-3 realistic, complete PR workflows (with AI attribution in commit messages)
- [ ] Screenshots/descriptions of GitHub UI (PR creation, review, merge)
- [ ] Troubleshooting: PR can't merge (conflicts), push rejected, authentication issues
- [ ] Word count: 2,000-2,500 words
- [ ] All code examples include expected output
- [ ] Follows lesson output style

**Key Elements**:
- Focus on GitHub web interface (most learners will use this, not CLI)
- Realistic PR scenarios (code review of AI-generated code)
- Show conflict resolution in PR context
- Screenshots make GitHub UI concrete
- Emphasize communication in PR (description, feedback)

**Deliverable**: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/04-lesson-4.md`

---

### Task 4.2: Design Lesson 4 Exercises
**Priority**: MUST | **Effort**: 2.5h | **Depends On**: Task 4.1
**Description**: Create 7 exercises for Lesson 4, culminating in full PR workflow.

**Acceptance Criteria**:
- [ ] 7 exercises provided
- [ ] Exercise 1: Create a repository on GitHub
  - [ ] Web UI: new repository, initialize with README
  - [ ] Success: repo created, accessible at github.com/username/repo-name
- [ ] Exercise 2: Clone and push to GitHub (or init local, add remote)
  - [ ] Local repo connected to GitHub
  - [ ] Push local branch to remote
  - [ ] Success: branch visible on GitHub
- [ ] Exercise 3: Create a feature branch locally
  - [ ] `git checkout -b feature-description`
  - [ ] Make changes, commit with good message
  - [ ] Push: `git push -u origin feature-description`
  - [ ] Success: branch visible on GitHub
- [ ] Exercise 4: Create a pull request via GitHub UI
  - [ ] Navigate to PR tab, click "New PR"
  - [ ] Select feature branch as source, main as target
  - [ ] Write PR title and description
  - [ ] Click "Create Pull Request"
  - [ ] Success: PR appears in PR tab with comments section
- [ ] Exercise 5: Simulate code review (comment on your own PR)
  - [ ] Add comment to PR (GitHub UI)
  - [ ] Ask for improvement in a specific area
  - [ ] Success: comment visible on PR
- [ ] Exercise 6: Make changes based on feedback
  - [ ] Make local changes on feature branch
  - [ ] Commit and push: `git push origin feature-branch`
  - [ ] Success: PR automatically updates with new commit
- [ ] Exercise 7: Merge the PR (optional: conflict resolution)
  - [ ] Click "Merge pull request" on GitHub
  - [ ] Confirm merge
  - [ ] Delete branch (optional)
  - [ ] Pull merged changes: `git pull origin main`
  - [ ] Success: main branch has feature changes, feature branch can be deleted
- [ ] Each exercise:
  - [ ] Clear steps
  - [ ] Expected GitHub UI state
  - [ ] Screenshots or descriptions
  - [ ] Time estimate: 5-20 min each
  - [ ] Success criteria

**Deliverable**: Integrated into `04-lesson-4.md` (Exercises section)

---

### Task 4.3: Create Lesson 4 Assessment
**Priority**: SHOULD | **Effort**: 1h | **Depends On**: Task 4.2
**Description**: Create self-assessment for Lesson 4.

**Acceptance Criteria**:
- [ ] 8-10 self-check questions
- [ ] Question types:
  - [ ] Conceptual: "What is a pull request and why would you use one?"
  - [ ] Procedural: "How do you push a branch to GitHub?"
  - [ ] Application: "You received critical feedback on your PR. How do you address it?"
- [ ] Answer key with explanations
- [ ] Tests PR workflow understanding

**Deliverable**: Integrated into `04-lesson-4.md` (Assessment section)

---

## Phase 5: Lesson 5 (Natural Language Prompts)

### Task 5.1: Write Lesson 5 Content (Natural Language Prompts for Git)
**Priority**: MUST | **Effort**: 2.5h | **Depends On**: Task 4.2
**Description**: Write lesson on using natural language prompts for Git operations via Claude Code/Gemini CLI.

**Acceptance Criteria**:
- [ ] File: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/05-lesson-5.md`
- [ ] Opening hook: "If you find Git commands intimidating, let your AI assistant handle the syntax."
- [ ] Part I: Why Natural Language Prompts (10 min)
  - [ ] Prompts reduce memorization burden
  - [ ] But still understand what commands do
  - [ ] AI as syntax translator, not knowledge replacement
  - [ ] When to use: need exact commands, overwhelmed by syntax
  - [ ] When NOT to use: when learning, when you need understanding
  - [ ] Mindset: convenience layer, not shortcut
- [ ] Part II: Command-to-Prompt Translation (15 min)
  - [ ] Pattern: `command` → natural language request
  - [ ] Examples (10+):
    - [ ] "What changes are in my working directory?" ← `git status`
    - [ ] "Show me the last 5 commits" ← `git log -n 5`
    - [ ] "Create a checkpoint before AI refactoring" ← `git commit -m "..."`
    - [ ] "Create a new branch called feature-auth and switch to it" ← `git checkout -b feature-auth`
    - [ ] "Help me understand these merge conflicts in auth.js" ← conflict explanation
    - [ ] "Stage all changes and commit with a good message" ← `git add .` + `git commit`
    - [ ] "Show me which lines I changed in utils.py" ← `git diff utils.py`
    - [ ] "Revert my last commit but keep the changes" ← `git reset --soft HEAD~1`
    - [ ] "Tell me who wrote this line in models.py" ← `git blame models.py`
    - [ ] "Create a git tag for version 1.0" ← `git tag v1.0`
  - [ ] Comparison table: command | natural language | expected output
  - [ ] Emphasis: same operations, different interface
- [ ] Part III: Complex Workflow Prompts (15 min)
  - [ ] Multi-step scenarios:
    - [ ] "Create a safety checkpoint, let me test this AI change, then I'll decide whether to merge or discard"
    - [ ] "I have merge conflicts. Can you explain what happened and show me how to resolve them?"
    - [ ] "Generate a .gitignore for a Python project and a .gitignore for Node.js"
    - [ ] "Create a PR template that includes a checklist for reviewing AI-generated code"
  - [ ] Combining operations: checkpoint → branch → experiment → merge
  - [ ] All examples show AI response
- [ ] Part IV: Troubleshooting Prompts (10 min)
  - [ ] "I made a mistake. Help me recover."
  - [ ] "Explain this error message: [pasted error]"
  - [ ] "What did I commit? [pasted diff]"
  - [ ] "Help me resolve these merge conflicts"
  - [ ] Real error messages (authentication, conflicts, push rejected)
  - [ ] AI responses helping learners understand
- [ ] Part V: Best Practices for AI CLI Conversations (10 min)
  - [ ] Be specific: "Create a branch for X feature" not "Create a branch"
  - [ ] Ask for explanations: "Do that AND explain what each command does"
  - [ ] Request safety checks: "Before pushing, show me what will be committed"
  - [ ] Use for learning: "Explain this Git concept" (AI as tutor)
  - [ ] Examples of good vs. poor prompts
- [ ] Emphasis throughout: understanding first, convenience second
- [ ] All prompts tested with Claude Code and Gemini CLI (or similar tools)
- [ ] Word count: 1,500-2,000 words
- [ ] Follows lesson output style

**Key Elements**:
- Framed as convenience, not replacement for knowledge
- 10+ realistic, tested prompt examples
- Comparison table for easy reference
- Complex workflows show AI enabling safer, faster development
- Troubleshooting prompts help with real problems
- Best practices emphasize learning + safety

**Deliverable**: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/05-lesson-5.md`

---

### Task 5.2: Design Lesson 5 Exercises
**Priority**: MUST | **Effort**: 1.5h | **Depends On**: Task 5.1
**Description**: Create 6 exercises for Lesson 5, testing prompt translation and usage.

**Acceptance Criteria**:
- [ ] 6 exercises provided
- [ ] Exercise 1: Ask Claude Code/Gemini CLI to explain a Git concept
  - [ ] Prompt: "Explain what a commit is in simple terms"
  - [ ] Success: AI explains concept, learner understands
  - [ ] Learning use case: AI as tutor
- [ ] Exercise 2: Use natural language to create a branch and commit
  - [ ] Prompt: "Create a new branch called feature-settings and make a test commit"
  - [ ] Success: branch exists with new commit
- [ ] Exercise 3: Use natural language to view commit history
  - [ ] Prompt: "Show me the last 3 commits with what changed"
  - [ ] Success: learner understands commit history format
- [ ] Exercise 4: Request help understanding a merge conflict
  - [ ] Create a merge conflict (intentionally)
  - [ ] Prompt: "Help me understand these merge conflicts"
  - [ ] Success: AI explains conflict markers and resolution
- [ ] Exercise 5: Ask AI to help resolve a merge conflict
  - [ ] Prompt: "Here's my merge conflict. How do I resolve it?"
  - [ ] Success: learner understands resolution steps
- [ ] Exercise 6: Complex workflow via prompts
  - [ ] Prompt: "I want to: create a checkpoint, let Claude refactor code on a branch, then decide whether to merge or discard. Walk me through the steps"
  - [ ] Success: learner has step-by-step workflow
- [ ] Each exercise:
  - [ ] Prompt provided
  - [ ] Expected AI response described
  - [ ] Success criteria
  - [ ] Time estimate: 5-10 min each
  - [ ] Teaching goal (learning, convenience, safety)

**Deliverable**: Integrated into `05-lesson-5.md` (Exercises section)

---

### Task 5.3: Create Lesson 5 Assessment
**Priority**: SHOULD | **Effort**: 0.5h | **Depends On**: Task 5.2
**Description**: Create self-assessment for Lesson 5.

**Acceptance Criteria**:
- [ ] 5-8 self-check questions
- [ ] Question types:
  - [ ] Conceptual: "When should you use natural language prompts vs. direct Git commands?"
  - [ ] Translation: "How would you ask Claude Code to show commit history?"
  - [ ] Application: "You're confused about merge conflicts. How would you ask AI for help?"
- [ ] Answer key
- [ ] Tests understanding of prompts as convenience layer

**Deliverable**: Integrated into `05-lesson-5.md` (Assessment section)

---

## Phase 6: Cross-Chapter Integration & Comprehensive Project

### Task 6.1: Design End-of-Chapter Comprehensive Project
**Priority**: MUST | **Effort**: 2h | **Depends On**: Task 5.2
**Description**: Create a realistic, comprehensive project combining all chapter skills (repo creation, commits, branches, PR, natural language).

**Acceptance Criteria**:
- [ ] Project description: 1-2 paragraphs explaining the scenario
- [ ] Scenario context: real-world (e.g., building a Python utility with AI assistance)
- [ ] Project requirements: specific, measurable outcomes
  - [ ] Create a Git repository locally
  - [ ] Make multiple commits (at least 3) with realistic commit messages
  - [ ] Include AI attribution in commit messages (e.g., "[AI] Claude - Add error handling")
  - [ ] Create a feature branch and experiment with changes
  - [ ] Merge feature branch back to main without data loss
  - [ ] Push repository to GitHub
  - [ ] Create a pull request (or simulate with a second branch)
  - [ ] Use natural language prompts (Claude Code/Gemini CLI) to execute at least 2 Git operations
- [ ] Success criteria: learner can verify completion
  - [ ] Repository exists locally and on GitHub
  - [ ] `git log --oneline` shows all commits with proper messages
  - [ ] Branches created and merged successfully
  - [ ] All files intact after merges
  - [ ] Natural language prompts used and documented
- [ ] Estimated time: 60-90 minutes (integrates all lessons)
- [ ] Instructions clear and no ambiguity
- [ ] Optional: rubric for self-grading (excellent/good/needs work)

**Deliverable**: New section in chapter overview or integrated into a lesson as capstone exercise

---

### Task 6.2: Create Quick Reference Card
**Priority**: SHOULD | **Effort**: 1.5h | **Depends On**: All lessons complete
**Description**: Create a one-page reference card of essential Git commands with brief explanations.

**Acceptance Criteria**:
- [ ] File: included in lesson 2 or as downloadable reference
- [ ] Format: table or list (scannable)
- [ ] Essential commands (15-20):
  - [ ] `git init` - Initialize repository
  - [ ] `git status` - Check current state
  - [ ] `git add .` - Stage all changes
  - [ ] `git commit -m "message"` - Create checkpoint
  - [ ] `git push` - Upload to GitHub
  - [ ] `git pull` - Download from GitHub
  - [ ] `git branch -a` - List all branches
  - [ ] `git checkout -b branch-name` - Create and switch branch
  - [ ] `git merge branch-name` - Merge branch
  - [ ] `git reset --hard HEAD~1` - Undo last commit (destructive)
  - [ ] `git reset --soft HEAD~1` - Undo last commit (keep changes)
  - [ ] `git log --oneline` - View commit history
  - [ ] `git diff` - See what changed
  - [ ] `git stash` - Save uncommitted work temporarily
  - [ ] (5 more as space allows)
- [ ] Each command includes: what it does, when to use it
- [ ] Platform-specific notes where needed
- [ ] AI attribution pattern shown
- [ ] Downloadable PDF or printable (optional)

**Deliverable**: Integrated into chapter or as separate reference document

---

### Task 6.3: Create Common Scenarios Reference
**Priority**: SHOULD | **Effort**: 1.5h | **Depends On**: All lessons complete
**Description**: Create reference section with 5-8 common AI development scenarios and their Git solutions.

**Acceptance Criteria**:
- [ ] Scenarios included:
  - [ ] "Before letting Claude Code refactor my project" - Create checkpoint
  - [ ] "I want to test AI changes safely" - Create feature branch, experiment, merge or discard
  - [ ] "I need to share code with teammates" - Create PR, get review, merge
  - [ ] "I accidentally broke something" - Rollback with git reset
  - [ ] "I'm confused about what happened" - Use git log, git diff, git blame
  - [ ] "I need to push a feature for review" - Create PR via GitHub
  - [ ] "I'm scared of losing my work" - Use git stash, commit often
  - [ ] (1-2 more realistic scenarios)
- [ ] Each scenario:
  - [ ] Problem description (2-3 sentences)
  - [ ] Git commands or prompt(s) to use
  - [ ] Expected outcome
  - [ ] Why this works
- [ ] Formatted as quick-lookup reference
- [ ] Indexed by problem type

**Deliverable**: Integrated into chapter or as separate reference document

---

## Phase 7: Quality Assurance & Integration

### Task 7.1: Peer Review for Pedagogical Clarity
**Priority**: SHOULD | **Effort**: 2h | **Depends On**: All content written
**Description**: Review chapter for pedagogical effectiveness, clarity, and learning objective alignment.

**Acceptance Criteria**:
- [ ] Reviewer confirms:
  - [ ] Learning objectives are measurable and achievable
  - [ ] Each lesson has a single, clear focus
  - [ ] Progression is logical (why → essentials → branches → PRs → prompts)
  - [ ] Examples are concrete and relatable
  - [ ] Content is engaging and motivating (not dry)
  - [ ] No unexplained jargon
  - [ ] Exercises align with learning objectives
  - [ ] Assessments test what was taught
  - [ ] Reflection prompts encourage critical thinking
  - [ ] Transitions between lessons are smooth
  - [ ] AI-first teaching philosophy evident throughout
  - [ ] Show-then-explain pattern consistently applied
- [ ] Feedback documented (issues, suggestions)
- [ ] Issues categorized: critical (blocks publication), important (should fix), nice-to-have
- [ ] Author addresses critical/important issues before publication

**Deliverable**: Feedback report + revisions

---

### Task 7.2: Technical Verification (Platform Testing)
**Priority**: MUST | **Effort**: 3h | **Depends On**: All content written
**Description**: Test all Git commands on Windows, macOS, and Linux; verify GitHub workflows; test natural language prompts.

**Acceptance Criteria**:
- [ ] Windows 10+ environment:
  - [ ] All Git commands tested (installation, basic workflow, branches, merging, reset)
  - [ ] Git Bash works correctly
  - [ ] GitHub authentication (HTTPS + PAT) works
  - [ ] All example outputs match documentation
- [ ] macOS 10.15+ environment:
  - [ ] Git installation (Homebrew and direct) both work
  - [ ] All commands produce expected output
  - [ ] GitHub authentication works
- [ ] Linux (modern distribution):
  - [ ] apt-get/brew installation works
  - [ ] All commands produce expected output
  - [ ] GitHub authentication works
- [ ] GitHub workflows (free-tier account):
  - [ ] Create repository, push, create PR, merge
  - [ ] All steps match documented UI
  - [ ] PR conflicts can be resolved
  - [ ] Free-tier limitations documented (if any)
- [ ] Natural language prompts:
  - [ ] Test with Claude Code (if available)
  - [ ] Test with Gemini CLI (if available)
  - [ ] Verify 10+ prompts from Lesson 5 work as described
  - [ ] Document any tool version issues
- [ ] Test results documented:
  - [ ] Which platform tested
  - [ ] Which commands verified
  - [ ] Any issues found and how resolved
  - [ ] Screenshots/output for tricky commands

**Deliverable**: Technical verification report + fixes applied

---

### Task 7.3: Accessibility & Clarity Check
**Priority**: MUST | **Effort**: 2h | **Depends On**: All content written
**Description**: Verify chapter meets accessibility standards (grade 7 reading level, no gatekeeping language, inclusive).

**Acceptance Criteria**:
- [ ] Reading level verified:
  - [ ] No unexplained jargon (all technical terms defined on first use)
  - [ ] Sentences are 1-2 lines average (not complex nested structures)
  - [ ] Paragraph breaks prevent "wall of text"
  - [ ] Grade 7 baseline confirmed (Flesch-Kincaid or similar)
- [ ] No gatekeeping language:
  - [ ] Remove "easy", "simple", "obvious", "just"
  - [ ] Replace with "you can" or "here's how"
  - [ ] Examples: "simply commit" → "make a commit", "obviously branches" → "branches are used for..."
- [ ] Inclusive language:
  - [ ] Gender-neutral pronouns and examples
  - [ ] Diverse example names/contexts
  - [ ] No assumptions about background (everyone starts as beginner)
  - [ ] Free/open-source alternatives provided
- [ ] Platform accessibility:
  - [ ] Instructions work on Windows, Mac, Linux (or clear notes if not)
  - [ ] No single-OS assumptions
  - [ ] Screenshots labeled/described
- [ ] Visual accessibility:
  - [ ] Code blocks have syntax highlighting
  - [ ] Commands clearly distinguished from output
  - [ ] Diagrams have text descriptions
  - [ ] Lists used for scannable content
- [ ] Issues documented and fixed

**Deliverable**: Accessibility report + corrections applied

---

### Task 7.4: Constitution Alignment Validation
**Priority**: MUST | **Effort**: 1.5h | **Depends On**: All content written
**Description**: Verify chapter aligns with project constitution principles.

**Acceptance Criteria**:
- [ ] Principle 1 (AI-First Teaching): Chapter demonstrates AI tools as partners
  - [ ] Natural language prompts shown throughout (not as afterthought)
  - [ ] Lesson 5 (prompts) integrated naturally, not tacked on
  - [ ] AI collaboration for safety emphasized
- [ ] Principle 5 (Progressive Complexity): Content difficulty increases gradually
  - [ ] Lesson 1: motivation only (no commands)
  - [ ] Lesson 2: basic commands (simple workflow)
  - [ ] Lesson 3: branches (more abstract)
  - [ ] Lesson 4: GitHub UI (familiar interface)
  - [ ] Lesson 5: prompts (convenience layer)
- [ ] Principle 8 (Accessibility): No gatekeeping
  - [ ] No assumed prior Git knowledge
  - [ ] No "easy", "simple", "obvious" language
  - [ ] Multiple explanation styles (stories, commands, diagrams, UI)
  - [ ] Platform-specific instructions provided
- [ ] Principle 9 (Show-Then-Explain): Workflows shown before explanations
  - [ ] Complete workflows demonstrated first
  - [ ] Then each piece explained
  - [ ] Why commands exist, not just what they do
- [ ] Book Gaps Checklist items covered:
  - [ ] Factual accuracy: All Git behavior verified (not assumptions)
  - [ ] Field volatility: Notes on which topics need future updates (GitHub UI changes, Git versions)
  - [ ] Inclusive language: Diverse examples, gender-neutral
  - [ ] Accessibility: Defined terminology, multiple explanations
  - [ ] Code security: `.gitignore` coverage, no secrets in examples
  - [ ] Ethical AI: Frame AI limitations in Lesson 5
  - [ ] Testing & quality: Exercises have clear success criteria
  - [ ] Engagement: Opening hooks, realistic examples, visual breaks
- [ ] Issues documented and addressed

**Deliverable**: Constitution alignment report + fixes applied

---

### Task 7.5: Cross-Chapter Coherence Check
**Priority**: SHOULD | **Effort**: 1h | **Depends On**: All content written
**Description**: Verify chapter integrates smoothly with Chapters 5-7 and bridges to Part 3.

**Acceptance Criteria**:
- [ ] Chapter 5 (Claude Code) integration:
  - [ ] Lesson 5 references Claude Code as example AI tool
  - [ ] Shows Claude Code executing Git commands via prompts
  - [ ] Consistent terminology with Chapter 5
- [ ] Chapter 6 (Gemini CLI) integration:
  - [ ] Lesson 5 references Gemini CLI as example tool
  - [ ] Both tools shown as equivalent for Git operations
  - [ ] Consistent with Chapter 6 approach
- [ ] Chapter 7 (Bash) integration:
  - [ ] Chapter 8 builds on terminal skills from Chapter 7
  - [ ] Git commands use same terminal navigation as Chapter 7
  - [ ] No re-teaching of bash basics
- [ ] Bridge to Part 3 (Prompting):
  - [ ] Lesson 5 is preview of prompt engineering (not full methodology)
  - [ ] References forward: "Part 3 will teach formal prompting patterns"
  - [ ] Natural language translation shown as real-world prompting application
- [ ] Part 4 (Python) setup:
  - [ ] Chapter 8 establishes Git as standard workflow (used in all Python projects)
  - [ ] Students will practice "commit early, commit often" in Chapters 14+
  - [ ] Prerequisite explicitly stated
- [ ] No contradictions with prior chapters (verify cross-references)

**Deliverable**: Cross-chapter coherence report

---

## Phase 8: Final Review & Publication Readiness

### Task 8.1: Style Guide Compliance
**Priority**: MUST | **Effort**: 1h | **Depends On**: Tasks 7.1-7.5 complete
**Description**: Verify chapter follows `.claude/output-styles/lesson.md` and `.claude/output-styles/chapter-readme.md`.

**Acceptance Criteria**:
- [ ] Lesson files follow lesson output style:
  - [ ] YAML frontmatter present (title, sidebar_position, description)
  - [ ] H1 title matches frontmatter
  - [ ] Opening hook in first 2-3 paragraphs
  - [ ] Subheadings use H2 (##) and H3 (###)
  - [ ] Code blocks have language syntax highlighting (```python, ```bash, etc.)
  - [ ] AI-native approach evident (how to use with AI, not just standalone)
  - [ ] Exercises section included
  - [ ] Assessment section included
- [ ] Chapter README follows chapter-readme output style:
  - [ ] Title and chapter number
  - [ ] Learning outcomes (bulleted)
  - [ ] Prerequisites listed
  - [ ] Chapter structure overview
  - [ ] Time estimate provided
  - [ ] No placeholder text
- [ ] Formatting consistency:
  - [ ] Consistent capitalization
  - [ ] Consistent date formats
  - [ ] Consistent code formatting (no mixing styles)
  - [ ] Consistent link format
- [ ] Issues documented and fixed

**Deliverable**: Style compliance report + corrections

---

### Task 8.2: Final Content Review (Human Editor)
**Priority**: MUST | **Effort**: 2h | **Depends On**: Task 8.1 complete
**Description**: Human editor performs final review for clarity, flow, engagement, completeness.

**Acceptance Criteria**:
- [ ] Grammar and spelling verified (no errors)
- [ ] Narrative flow smooth and engaging
- [ ] All promised deliverables present:
  - [ ] Chapter README
  - [ ] 5 lesson files
  - [ ] 5+ exercises per lesson
  - [ ] Assessment per lesson
  - [ ] Comprehensive project
  - [ ] Quick reference (optional)
  - [ ] Common scenarios reference (optional)
- [ ] No placeholder text or TODOs
- [ ] All cross-references valid
- [ ] Code examples are complete and correct
- [ ] Screenshots/diagrams appropriately placed and labeled
- [ ] Feedback documented (editorial suggestions, corrections)
- [ ] Author addresses feedback before publication

**Deliverable**: Editorial report + final revisions

---

### Task 8.3: Prepare for Lesson-Writer Agent Handoff
**Priority**: MUST | **Effort**: 1h | **Depends On**: Task 8.2 complete
**Description**: Create summary of plan for lesson-writer agent, confirming all architectural decisions.

**Acceptance Criteria**:
- [ ] Executive summary created:
  - [ ] Chapter type (hybrid)
  - [ ] 5 lessons with durations and objectives
  - [ ] Key architectural decisions explained
  - [ ] Risk mitigations documented
  - [ ] Success criteria summarized
- [ ] All files referenced with absolute paths
- [ ] Expected deliverables listed
- [ ] Acceptance criteria for each lesson provided
- [ ] Links to relevant constitution sections, output styles, prior chapters
- [ ] Outstanding questions or decisions noted
- [ ] Ready for lesson-writer agent to begin implementation

**Deliverable**: Handoff summary document

---

## Acceptance Criteria (Definition of Done)

**ALL tasks must meet these criteria before chapter is publication-ready:**

- [ ] All 5 lessons written (README + 5 lesson files)
- [ ] All exercises have clear prompts and expected outcomes
- [ ] All assessments have answer keys
- [ ] Comprehensive end-of-chapter project included
- [ ] Quick reference card created (SHOULD)
- [ ] Common scenarios reference created (SHOULD)
- [ ] All Git commands tested on Windows, Mac, Linux
- [ ] All GitHub workflows tested with free-tier account
- [ ] All natural language prompts tested with Claude Code/Gemini CLI
- [ ] No placeholder text, TODOs, or unfinished sections
- [ ] No gatekeeping language ("easy", "simple", "obvious", "just")
- [ ] All jargon defined on first use
- [ ] No unexplained assumptions about learner knowledge
- [ ] Reading level verified (grade 7 baseline)
- [ ] All code examples include expected output
- [ ] Platform-specific instructions provided (Windows/Mac/Linux)
- [ ] Learning objectives measurable (can verify success)
- [ ] Exercises align with learning objectives
- [ ] Assessments test what was taught
- [ ] Chapter integrates with Chapters 5-7 (no contradictions)
- [ ] Chapter bridges to Part 3 (prompting)
- [ ] Chapter prepares learners for Part 4 (Python projects using Git)
- [ ] Style guide compliance verified
- [ ] Constitution principles validated (AI-first, show-then-explain, accessible)
- [ ] All risks mitigated (secrets, installation, conflicts, etc.)
- [ ] Success criteria from spec addressed (SC-001 through SC-008)
- [ ] Human editorial review complete
- [ ] Ready for publication

---

## Task Dependencies (Implementation Order)

```
1.1 Chapter README
  ↓
1.2 Lesson 1 Content
  ↓
2.1 Lesson 2 Content
  ↓
2.2 Lesson 2 Exercises
  ├─→ 2.3 Lesson 2 Assessment
  ↓
3.1 Lesson 3 Content
  ↓
3.2 Lesson 3 Exercises
  ├─→ 3.3 Lesson 3 Assessment
  ↓
4.1 Lesson 4 Content
  ↓
4.2 Lesson 4 Exercises
  ├─→ 4.3 Lesson 4 Assessment
  ↓
5.1 Lesson 5 Content
  ↓
5.2 Lesson 5 Exercises
  ├─→ 5.3 Lesson 5 Assessment
  ↓
6.1 Comprehensive Project
6.2 Quick Reference (parallel)
6.3 Common Scenarios (parallel)
  ↓
7.1 Pedagogical Review
7.2 Technical Verification (parallel)
7.3 Accessibility Check (parallel)
7.4 Constitution Alignment (parallel)
7.5 Cross-Chapter Coherence
  ↓
8.1 Style Guide Compliance
  ↓
8.2 Final Content Review
  ↓
8.3 Handoff Summary
```

**Critical Path**: 1.1 → 1.2 → 2.1 → 2.2 → 3.1 → 3.2 → 4.1 → 4.2 → 5.1 → 5.2 → 6.1 → 7.x → 8.1 → 8.2 → 8.3

**Total Estimated Effort**: 16-23 hours
- **MUST tasks**: 13 (6 content + 7 critical reviews)
- **SHOULD tasks**: 5 (references, assessments)
- **NICE-TO-HAVE tasks**: 3 (optional enhancements)

---

## Follow-Up Sequence

After this planning phase completes:

1. **Handoff to Lesson-Writer Agent**: Use `sp.implement` command to begin lesson-by-lesson implementation
2. **Iterative Review**: After each lesson is drafted, human reviews and provides feedback
3. **Integration Testing**: After all lessons written, test cross-chapter coherence and style consistency
4. **Technical Review Agent**: Use technical-reviewer agent to validate pedagogy and technical accuracy
5. **Publication**: After all reviews pass, chapter is ready for Docusaurus build and publication

---

## Notes & Considerations

### For Implementation Team
- Start with Lesson 1 (establishes motivation—foundation for entire chapter)
- Each lesson can be implemented independently once Lesson 1 is complete
- Exercises should be written as you write lessons (not after)
- Test all code examples on actual systems (not assumed to work)
- Screenshot GitHub UI if possible (makes PR workflow concrete)
- Natural language prompts should be tested with actual tools

### For Reviewers
- Verify exercises have clear success criteria (not subjective)
- Confirm assessments test what was taught (alignment check)
- Check that examples are realistic (not contrived or overly simplified)
- Ensure progression is logical (no sudden jumps in complexity)
- Validate cross-chapter references (accuracy, no broken links)

### Known Risks to Mitigate During Implementation
- **Installation issues**: Detailed troubleshooting section essential
- **Merge conflict fear**: Teach rollback and stash early to build confidence
- **Authentication confusion**: Step-by-step PAT/SSH guide with screenshots
- **Secrets in git history**: Early `.gitignore` introduction, warning boxes
- **GitHub UI changes**: Note publication date, include update triggers

### Questions for User (If Needed During Implementation)
- Should we include SSH key setup, or just PAT (simpler for beginners)?
- Do we assume learners have GitHub accounts, or walk through account creation?
- Should `git rebase` be mentioned (decided NO in plan, but confirm)
- Should GitHub Actions be mentioned (decided NO, deferred to later parts, but confirm)

