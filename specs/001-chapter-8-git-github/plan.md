# Chapter 8: Git & GitHub for AI-Driven Development — Implementation Plan

**Chapter Type**: Hybrid (Technical + Natural Language Prompts)
**Duration**: 3-4 hours (approximately 4-5 hours including exercises)
**Part**: Part 2 (AI Tool Landscape) — Final chapter
**Prerequisites**: Chapters 5-7 completed (Claude Code, Gemini CLI, Bash Essentials)
**Target Audience**: Beginners with no Git/terminal experience
**Key Principle**: Git as the safety net for AI-assisted development (commit early, experiment safely, collaborate professionally)

---

## Chapter Objective

Learners will understand and practice Git version control and GitHub collaboration in the context of AI-driven development, specifically to:
1. Create safe checkpoints before letting AI tools modify their code
2. Safely experiment with AI-generated code using branches
3. Collaborate with teammates using pull requests
4. Use natural language prompts as a convenience layer for Git operations
5. Understand when and why to commit code, and how to track AI contributions

---

## Lesson Architecture (5 Lessons)

### Lesson 1: Why Git Matters in AI-Driven Development (30 min)
**Objective**: Understand the safety net that Git provides when working with AI tools
**Bloom's Level**: Understand (explain the value, not yet do operations)
**Duration**: 30 minutes reading + reflection
**Key Concepts**:
- Safety net concept (every change is reversible)
- Checkpoint analogy (video game save points)
- Collaboration pattern (multiple people, same codebase)
- Auditability (knowing who/what/when changed)

**Content Outline**:
- Opening Hook: "What if Claude Code broke your project? With Git, you're 30 seconds from recovery."
- The Three Problems Git Solves (with AI context)
  - Safety: Experiment fearlessly knowing you can roll back
  - Collaboration: Share code with teammates before merging
  - Auditability: Track which AI tool made which changes
- Real-World Scenarios
  - Solo developer experimenting with AI refactoring
  - Team reviewing AI-generated feature before merging
  - Debugging: "When did this bug appear? Which AI session introduced it?"
- Analogy: Git as versioning in video games, tracks in film production, checkpoints in sports
- Why Part II matters: Natural language prompts make Git more accessible

**Content Elements**:
- 4-5 concrete examples (AI refactor with rollback, team PR review, bug hunt with git log, accidental secret committed, etc.)
- Visual: Simple diagram showing branches as experiment paths
- NO code examples yet (this lesson is conceptual)

**Practice Approach**:
- Reflection prompts: "Can you think of a time you've worked on code with others? What went wrong?"
- Peer insight: "If you were reviewing code from Claude Code, what would concern you?"

**Prerequisites**: None—foundational lesson

**Scaffolding**: Heavy support; establishes motivation before teaching commands

---

### Lesson 2: Git Essentials: Commands and Setup (90 min)
**Objective**: Install Git, configure it, and execute the basic workflow (status → add → commit → push)
**Bloom's Level**: Apply (execute commands independently)
**Duration**: 90 minutes (45 min content + 45 min exercises)
**Key Concepts**:
- Git installation (platform-specific)
- Configuration (user identity for commits)
- Working directory vs. staging area vs. repository
- Basic workflow: status → add → commit → push
- Reading and understanding status output
- Commit messages with intent

**Content Outline**:
- Opening Hook: "Every commit is a story. Let's tell good ones."
- Part I: Installation & Setup
  - Windows-specific instructions (Git Bash)
  - macOS instructions (Homebrew or installer)
  - Linux instructions (apt/brew)
  - Verification: `git --version` and `git config --list`
  - Configuration: `git config --global user.name`, `git config --global user.email`
- Part II: The Core Workflow (Show-Then-Explain)
  - Demonstrate complete workflow: init → status → add → commit → push
  - Each command includes: what it does, why you use it, what it outputs
  - Three-stage concept: working directory → staging area → repository (with diagram)
- Part III: Reading Git Output
  - Understanding `git status` output (untracked, modified, staged)
  - Understanding `git log` output (commit messages, authors, timestamps)
  - Interpreting error messages
- Part IV: Commit Messages with AI Attribution
  - Best practices: present tense, descriptive, linkable
  - AI attribution pattern: `[AI] Claude - Add error handling for API timeout`
  - Why this matters: auditability, understanding evolution

**Content Elements**:
- Code examples: 3-4 complete workflows (Python project, Node.js project, etc.)
- All examples include expected output
- Platform-specific notes (Windows/Mac/Linux) for commands that differ
- Troubleshooting subsection: common installation issues and fixes
- No jargon: define "staging area", "repository", "remote" on first use

**Practice Approach**:
- Exercise 1: Install Git and verify (`git --version`)
- Exercise 2: Configure user identity
- Exercise 3: Initialize a new repository
- Exercise 4: Make a commit with a good commit message
- Exercise 5: View commit history with `git log --oneline`

**Prerequisites**: Bash basics from Chapter 7 (terminal navigation)

**Scaffolding**: Show commands first, explain each component, then independent practice

---

### Lesson 3: Safe Experimentation: Branches, Checkpoints, and Rollback (90 min)
**Objective**: Create checkpoints before AI changes, safely rollback if needed, experiment with branches
**Bloom's Level**: Apply (create branches, make commits, reset safely)
**Duration**: 90 minutes (40 min content + 50 min exercises)
**Key Concepts**:
- Checkpoint as a named commit
- Branching as parallel development paths
- HEAD pointer and state management
- Rolling back with `git reset` (soft vs. hard)
- Reverting with `git revert` (safe alternative)
- Merge strategies (fast-forward vs. three-way)

**Content Outline**:
- Opening Hook: "Before you let Claude Code refactor your project, save a checkpoint."
- Part I: The Checkpoint Pattern
  - Commit as checkpoint: `git commit -m "Stable state before AI refactoring"`
  - Reading commit history: understanding what each checkpoint represents
  - Best practice: commit before every AI session
- Part II: Branch-Based Experimentation
  - Why branches: safe isolation, experiment without affecting main
  - Creating and switching: `git checkout -b feature-branch`
  - List branches: `git branch`
  - Switching between branches: `git checkout main`
  - Use case: let Claude Code experiment on a branch, test results, decide to merge or discard
- Part III: Undoing Changes (The Safety Net)
  - Soft reset: `git reset --soft HEAD~1` (undo commit, keep changes staged)
  - Hard reset: `git reset --hard HEAD~1` (undo commit and discard changes)
  - Revert: `git revert COMMIT_HASH` (safe alternative, creates new commit)
  - When to use each
- Part IV: Merging Branches
  - Fast-forward merge (linear history)
  - Three-way merge (creating merge commit)
  - Handling merge conflicts (conflict markers, manual resolution, asking AI for help)
  - Merge vs. rebase philosophy (choosing safety over perfection)
- Part V: Stashing (Temporary Save)
  - `git stash` to save uncommitted work temporarily
  - Use case: need to switch branches but not ready to commit

**Content Elements**:
- Code examples: 4-5 complete workflows
  - Checkpoint → experiment → success → merge
  - Checkpoint → experiment → failure → rollback to checkpoint
  - Branch creation and merging
  - Merge conflict with resolution
- Visual diagram: branch visualization showing experiment paths and merges
- Troubleshooting: "Accidentally committed on wrong branch?", "Committed something I shouldn't?"

**Practice Approach**:
- Exercise 1: Create a checkpoint commit
- Exercise 2: Create a feature branch and make changes
- Exercise 3: Switch between branches and observe file changes
- Exercise 4: Merge the branch back to main
- Exercise 5: Rollback a commit using `git reset --hard` (in isolated example)
- Exercise 6: Create and resolve a simple merge conflict

**Prerequisites**: Lesson 2 (basic workflow)

**Scaffolding**: Build from checkpoint concept → branches → safe undoing → merging

---

### Lesson 4: Pull Requests and Team Collaboration (75 min)
**Objective**: Create PRs on GitHub, participate in code review, merge safely with team
**Bloom's Level**: Apply (create PR, respond to feedback, merge)
**Duration**: 75 minutes (35 min content + 40 min exercises)
**Key Concepts**:
- Pull request as a code review mechanism
- GitHub PR interface (creating, describing, reviewing)
- Review feedback and iteration
- Merge strategies on GitHub (squash, rebase, merge commit)
- Branch protection and best practices
- Resolving conflicts in PR

**Content Outline**:
- Opening Hook: "Pull requests let teammates review AI code before it ships."
- Part I: Understanding PRs (Conceptually)
  - What is a PR? Proposed changes from one branch to another
  - Why PRs? Code review, discussion, auditing
  - PR vs. merge: PR is proposal, merge is execution
  - GitHub interface: PR page anatomy
- Part II: Creating a PR
  - Push branch to GitHub: `git push -u origin feature-branch`
  - Open PR via GitHub UI (web interface walkthrough)
  - PR title and description best practices
  - Using description to explain AI changes: "Claude Code generated X, we need to review Y"
- Part III: Reviewing Code
  - What to look for in AI-generated code (security, logic, style)
  - Leaving comments and suggestions
  - Requesting changes vs. approving
  - Re-reviewing after changes
- Part IV: Iteration and Feedback
  - Making changes based on review feedback
  - Pushing new commits to PR (automatically updates)
  - Squashing commits before merge (optional, for cleaner history)
  - Addressing all comments
- Part V: Merging on GitHub
  - Merge strategies: merge commit (default), squash, rebase
  - Deleting the branch after merge (cleanup)
  - Pulling merged changes locally: `git pull origin main`
- Part VI: Handling PR Conflicts
  - Merge conflicts on GitHub interface
  - Resolving locally and pushing
  - Asking AI to help understand conflict markers

**Content Elements**:
- Walkthrough: Complete PR workflow from GitHub UI perspective
- Screenshots/descriptions: PR creation, review interface, conflict resolution
- Code examples: 2-3 realistic PRs with AI attribution
- Troubleshooting: PR can't merge (conflicts), push rejected, authentication issues

**Practice Approach**:
- Exercise 1: Create a repository on GitHub
- Exercise 2: Push a local branch to GitHub
- Exercise 3: Create a pull request via web interface
- Exercise 4: Simulate review feedback (make a comment on your own PR)
- Exercise 5: Make additional commits to address "feedback"
- Exercise 6: Merge the PR on GitHub
- Exercise 7 (optional): Create and resolve a merge conflict in a PR

**Prerequisites**: Lesson 3 (branches and merging), GitHub account

**Scaffolding**: Show PR interface first, then explain concepts, then independent practice

---

### Lesson 5: Natural Language Prompts for Git Operations (Part II) (45 min)
**Objective**: Use Claude Code or Gemini CLI to execute Git commands via natural language; understand when to use this convenience layer
**Bloom's Level**: Apply (translate commands to prompts, execute via AI CLI)
**Duration**: 45 minutes (15 min concept + 30 min exercises/examples)
**Key Concepts**:
- Natural language as convenience layer (not replacement for understanding)
- AI CLI tools: Claude Code, Gemini CLI
- Prompt patterns for Git operations
- Complex workflows via prompts (combining multiple operations)
- When to use natural language vs. direct commands
- Troubleshooting prompts (conflict help, error explanation)

**Content Outline**:
- Opening Hook: "If you find Git commands intimidating, let your AI assistant handle the syntax."
- Part I: Why Natural Language Prompts? (Mindset)
  - Prompts reduce memorization burden
  - But still understand what commands do
  - AI as a syntax translator, not a replacement for knowledge
  - When to use: need exact commands, when overwhelmed by syntax
  - When NOT to use: when learning, when you need to understand what's happening
- Part II: Command-to-Prompt Translation
  - Single commands: `git status` → "What changes are in my working directory?"
  - Chained commands: Creating checkpoint → branching → committing → pushing
  - Realistic translations for 10+ common Git scenarios
  - Examples:
    - "Create a safety checkpoint with message 'Stable before AI refactoring'"
    - "Create a new branch called feature-auth and switch to it"
    - "Show me the commit history for the last 5 commits"
    - "Help me understand these merge conflicts in auth.js"
    - "Stage all my changes and commit with a message describing what I did"
- Part III: Complex Workflow Prompts
  - Multi-step scenarios: "Create a feature branch, let me test AI changes, then help me decide to merge or discard"
  - Combining operations: create checkpoint → branch → let Claude refactor → review → merge
  - Example prompts for:
    - Setting up `.gitignore` for Python projects
    - Generating PR templates
    - Understanding blame output
    - Reverting a problematic commit
- Part IV: Troubleshooting Prompts
  - "I made a mistake. Help me recover."
  - "Explain this error message: [pasted error]"
  - "What did I commit? [pasted diff]"
  - "Help me resolve merge conflicts"
- Part V: Best Practices for AI CLI Conversations
  - Be specific: "Create a branch for X feature" not "Create a branch"
  - Ask for explanations: "Do that AND explain what each command does"
  - Request safety checks: "Before pushing, show me what will be committed"
  - Use for learning: "Explain this Git concept" (AI as tutor)

**Content Elements**:
- 10+ realistic prompt examples (all with expected outcomes)
- Comparison table: Git command vs. Natural language prompt vs. Output
- Real prompts that work with Claude Code and Gemini CLI
- Emphasis: prompts are convenience, not shortcuts to understanding
- All examples show AI response alongside the natural language request

**Practice Approach**:
- Exercise 1: Ask Claude Code or Gemini CLI to explain a Git concept (learning use case)
- Exercise 2: Use natural language to create a branch and commit
- Exercise 3: Use natural language to view commit history
- Exercise 4: Request help understanding a merge conflict
- Exercise 5: Ask AI to help resolve a merge conflict
- Exercise 6: Complex workflow: "I want to create a checkpoint, let AI refactor, then decide to merge"

**Prerequisites**: Lessons 1-4 (understand Git concepts), access to Claude Code or Gemini CLI

**Scaffolding**: Heavy emphasis on "this is a convenience layer", reinforce core Git understanding

---

## Lesson Dependencies and Flow

```
Lesson 1 (Why Git?)
    ↓ (establish motivation)
Lesson 2 (Essentials)
    ↓ (learn basic workflow)
Lesson 3 (Safe Experimentation)
    ↓ (create checkpoints, branch, rollback)
Lesson 4 (Pull Requests)
    ↓ (team collaboration)
Lesson 5 (Natural Language)
    ↓ (convenience layer; refer back to all prior lessons)
```

Each lesson builds on prior understanding. Lesson 5 is positioned as a convenience layer that assumes mastery of core Git concepts from Lessons 2-4.

---

## Content Flow & Cognitive Load Management

### Scaffolding Strategy

**Foundation (Lesson 1)**: Establish why Git matters—motivation before commands. No syntax, no overwhelm. Just stories and scenarios.

**Core Skills (Lessons 2-3)**: Teach Git with heavy scaffolding:
- Show complete workflow first
- Explain each part
- Practice individually
- Progress from status/add/commit (simplest) → branches and rollback (more complex) → merging (most complex)

**Professional Workflows (Lesson 4)**: Now that Git basics are solid, introduce team collaboration via pull requests. GitHub UI reduces command-line friction.

**Convenience Layer (Lesson 5)**: Natural language prompts assume full understanding of core concepts. Framed as "if Git commands feel overwhelming, use this", NOT "ignore lessons 2-4 and just use prompts".

### Cognitive Load Management

- **Lesson 1**: ~30 min reading (low load, storytelling)
- **Lesson 2**: ~45 min content + ~45 min practice (medium load, new concepts but practiced step-by-step)
- **Lesson 3**: ~40 min content + ~50 min practice (medium-high load, abstract concept of branches + concrete practice)
- **Lesson 4**: ~35 min content + ~40 min practice (medium load, GitHub UI handles complexity)
- **Lesson 5**: ~15 min concept + ~30 min practice (low load, reviewing known concepts in prompt form)

**Total: ~3.5-4 hours content, +1 hour for optional exercises = 4.5-5 hours**

---

## Integration with Book and Prior Chapters

### Connection to Chapters 5-7
- **Chapter 5 (Claude Code)**: Chapter 8 shows Claude Code can use Git commands via natural language prompts
- **Chapter 6 (Gemini CLI)**: Gemini CLI can execute Git workflows from text prompts
- **Chapter 7 (Bash Essentials)**: Git CLI commands use same terminal skills learned in Chapter 7

### Bridge to Part 3 (Prompt & Context Engineering)
- Chapter 8 demonstrates real-world prompt engineering: translating Git concepts to natural language
- Chapter 9+ will formalize prompt patterns (Part 3: Prompt & Context Engineering)
- Lesson 5 is a "preview" of effective prompting without formal methodology

### Connection to Part 4 (Python & Type Hints)
- Chapter 8 teaches professional version control workflow
- Chapters 14+ will use Git extensively (real projects, repositories, team collaboration)
- Students will practice "commit early, commit often" habit in all Python chapters

---

## Domain Skills Application

### 1. Learning Objectives Skill
- Each lesson has a single, Bloom's-appropriate objective
- Progression: Understand → Apply → Apply (with new context)
- Success validated by exercises with clear pass/fail criteria

### 2. Concept Scaffolding Skill
- Git decomposed into: why → setup → workflow → branches → collaboration → prompts
- Each concept builds on prior (checkpoint → branches → merging → PRs)
- Progressive complexity: simple commands → branching (abstract) → PRs (interface-based)

### 3. Code Example Generator Skill
- All code examples runnable on Windows/Mac/Linux
- Expected output shown for every example
- Platform-specific notes where commands differ

### 4. Exercise Designer Skill
- 20+ exercises across 5 lessons
- Progression from setup (Lesson 2) → safe experimentation (Lesson 3) → team collaboration (Lesson 4) → prompt translation (Lesson 5)
- Each exercise has clear acceptance criteria and expected output

### 5. Assessment Builder Skill
- Self-assessments at end of each lesson
- Reflection prompts: "When should you commit?" "What would you do if you accidentally committed a secret?"
- Comprehensive end-of-chapter project: Create repo, make multiple commits, create branch, simulate PR, push to GitHub

### 6. Technical Clarity Skill
- No assumed prior Git knowledge
- Jargon defined on first use: "A commit is a snapshot of your code at a specific moment"
- Multiple explanation styles: stories (Lesson 1), step-by-step (Lesson 2), diagrams (Lesson 3), UI walkthroughs (Lesson 4), prompts (Lesson 5)
- Accessibility: platform-specific instructions for Windows/Mac/Linux

### 7. Book Scaffolding Skill
- Chapter positioned as final tool in Part 2 (Tool Landscape)
- Explicitly connects to Chapters 5-7 (here's how Claude Code can use Git)
- Bridges to Part 3 (prompting is an AI skill, preview here)
- Sets up Part 4 (students will use Git in all Python projects)

### 8. AI-Augmented Teaching Skill
- Lesson 5 demonstrates using AI tools to reduce friction (natural language prompts)
- Lesson 4 shows using AI to understand merge conflicts ("Ask Claude Code for help understanding this")
- Throughout: emphasizing safe experimentation, which is only possible with version control

### 9. Content Evaluation Framework Skill
- Technical accuracy: All Git commands tested on Windows/Mac/Linux
- Pedagogical effectiveness: Progression from motivation → understanding → practice → professional context
- Accessibility: Grade 7 baseline, jargon defined, multiple explanations
- Constitution alignment: AI-first teaching (natural language prompts), show-then-explain (workflows before explanations), accessibility (no gatekeeping)

---

## Success Criteria Mapping (from Spec)

| Success Criteria | Addressed In | Measurement |
|------------------|--------------|-------------|
| SC-001: Create repo and commit in 5 min | Lesson 2, Exercise 3-4 | Timed exercise |
| SC-002: Safe checkpoint and rollback | Lesson 3, Exercises 1, 5 | Create checkpoint, intentionally break code, rollback, verify |
| SC-003: Branch workflow without data loss | Lesson 3, Exercises 2-4 | Create branch, edit, switch, merge back, verify no loss |
| SC-004: Create PR, address feedback, merge | Lesson 4, Exercises 1-7 | Full GitHub PR workflow |
| SC-005: Translate 10+ commands to prompts | Lesson 5, Exercises 1-6 | List 10 command→prompt translations, practice |
| SC-006: Understand when to commit | Lesson 2, Reflection; Lesson 5, Prompts | Self-assessment, real scenarios |
| SC-007: End-of-chapter project (90% success) | Comprehensive exercise | Create repo, multiple commits with AI attribution, branch, push |
| SC-008: Identify Git commands for 5 scenarios | Lesson 4-5, Scenarios section | Scenario-based exercises |

---

## Validation Strategy

### For Learners
- Self-assessment quizzes at end of each lesson (5-10 questions)
- Practical exercises with clear success criteria (git log output matches expected, file state correct)
- End-of-chapter project combining all skills

### For Authors/Reviewers
- All Git commands tested on Windows 10+, macOS 10.15+, modern Linux
- All GitHub workflows tested with free-tier account
- All natural language prompts tested with Claude Code and Gemini CLI
- Code examples match expected output exactly
- Platform-specific instructions verified for each platform
- Reading level checked (grade 7 baseline, technical terminology defined)
- Constitution alignment verified (AI-first teaching, show-then-explain, accessibility)

---

## File Organization (from directory-structure.md)

**Part**: Part 2 (AI Tool Landscape)
**Chapter**: Chapter 8 (final chapter of Part 2)
**Directory Path**: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/`

**Expected Files**:
- `README.md` — Chapter overview, learning objectives, prerequisites, summary
- `01-lesson-1.md` — Lesson 1: Why Git Matters in AI-Driven Development
- `02-lesson-2.md` — Lesson 2: Git Essentials
- `03-lesson-3.md` — Lesson 3: Safe Experimentation
- `04-lesson-4.md` — Lesson 4: Pull Requests and Collaboration
- `05-lesson-5.md` — Lesson 5: Natural Language Prompts for Git

Each lesson follows the output style from `.claude/output-styles/lesson.md`.

---

## Key Architectural Decisions

### Decision 1: Hybrid Structure (Part I: Commands, Part II: Prompts)
- **Rationale**: Teaches full understanding first (Part I), then shows convenience layer (Part II). Prevents natural language prompts from becoming "magic" without understanding.
- **Alternative Rejected**: Interleaving commands and prompts throughout—too fragmented, learners wouldn't understand why prompts work.

### Decision 2: Five Lessons Instead of Traditional Sections
- **Rationale**: 3-4 hours naturally breaks into 5 focused lessons (30-90 min each). Better pacing, each lesson teaches one Git concept comprehensively.
- **Alternative Rejected**: Fewer, longer lessons—would overload cognitive load. More lessons—unnecessary fragmentation.

### Decision 3: Lesson 5 Positioned as "Convenience Layer"
- **Rationale**: Prevents learners from skipping Lessons 2-4. Emphasizes that understanding comes first, automation second. Aligns with AI-first teaching philosophy (AI as partner, not replacement).
- **Alternative Rejected**: Lesson 5 as "advanced topic"—incorrectly frames natural language prompts as complex.

### Decision 4: GitHub UI Focus (Not Git CLI for Everything)
- **Rationale**: Lesson 4 teaches PR workflow via GitHub web interface, reducing command-line friction. Most learners will create PRs on GitHub web, not CLI.
- **Alternative Rejected**: Teaching `git push`, `git pull request` CLI commands—not standard, GitHub web is preferred.

### Decision 5: Safety and Rollback Emphasized Early (Lesson 3)
- **Rationale**: Addresses Risk 2 from spec ("learners fear breaking everything"). Teaching rollback early builds confidence. Safe experimentation is the core value of Git for AI-driven development.
- **Alternative Rejected**: Advanced rollback techniques late—would leave learners anxious throughout Lessons 2-3.

---

## Risk Mitigations (from Spec)

| Risk | Lesson | Mitigation |
|------|--------|-----------|
| Learners accidentally commit secrets | 2 | Early `.gitignore` introduction, ready-made templates, warning box |
| Fear of "breaking everything" | 1, 3 | Emphasize Git as safety net, teach rollback early and prominently |
| Platform-specific installation issues | 2 | Detailed Win/Mac/Linux instructions, verification step, troubleshooting |
| GitHub authentication confusion | 4 | Step-by-step PAT/SSH guide, error message interpretation |
| Merge conflict paralysis | 3, 5 | Explain markers clearly, show simple resolution, offer AI assistance |

---

## Notes for Implementation Team

### For Lesson Writer Agent
- Follow the lesson output style from `.claude/output-styles/lesson.md`
- Each lesson should be 2,000-2,500 words (8-12 min reading) plus exercises
- Use the Show-Then-Explain pattern: demonstrate complete workflow first, then explain each piece
- Include 4-5 real-world examples per lesson, not toy examples
- All code examples must include expected output
- Platform-specific instructions clearly marked (use callout boxes for Windows/Mac/Linux differences)

### For Technical Reviewer Agent
- Verify all Git commands on Windows 10+, macOS 10.15+, and modern Linux
- Test all GitHub workflows (create repo, PR, merge) with free-tier account
- Check that natural language prompts work with Claude Code and Gemini CLI
- Verify no secrets in examples (no real API keys, tokens, etc.)
- Confirm learning objectives are measurable (can we verify if learner achieved the objective?)
- Check that exercises have clear success criteria and expected output

### For Content Creators
- Do NOT assume readers know what a "repository" or "staging area" means—define on first use
- Do NOT use gatekeeping language ("obviously", "simply", "just")
- DO include screenshots of GitHub UI where helpful
- DO show complete, runnable examples with all output
- DO explain WHY each command exists, not just WHAT it does
- DO emphasize the AI-driven development context throughout (safety net for experiments, tracking AI contributions)

---

## Estimated Effort (for Planning)

- **Lesson 1**: 1-2 hours (research, writing, examples, reflection prompts)
- **Lesson 2**: 3-4 hours (installation docs for 3 platforms, 4 code examples with all output, exercises)
- **Lesson 3**: 4-5 hours (abstract concept of branches, diagrams, 5 complete workflows, complex exercises)
- **Lesson 4**: 3-4 hours (GitHub UI walkthrough, screenshots, PR workflow, conflict resolution)
- **Lesson 5**: 2-3 hours (10+ prompt examples, comparison table, exercises)
- **README.md**: 1-2 hours (chapter overview, learning outcomes, prerequisites, summary)
- **Review and Integration**: 2-3 hours (ensure consistency, cross-chapter checks, style validation)

**Total**: 16-23 hours of implementation effort (assumes one lesson-writer agent working sequentially)

---

## Success Definition

You have succeeded when:

✅ All 5 lessons are written following the lesson output style
✅ Each lesson has clear learning objectives and measurable success criteria
✅ All Git commands are tested on Windows, Mac, and Linux
✅ All GitHub workflows verified with free-tier account
✅ All natural language prompts tested with Claude Code and Gemini CLI
✅ All exercises have clear acceptance criteria and expected output
✅ Chapter integrates seamlessly with Chapters 5-7 and bridges to Part 3
✅ Reading level: grade 7 baseline, technical terms defined, no gatekeeping language
✅ Covers all success criteria from spec (SC-001 through SC-008)
✅ Validates against constitution principles (AI-first, show-then-explain, accessible, progressive scaffolding)

