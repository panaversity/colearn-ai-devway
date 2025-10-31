---
title: "Comprehensive Project: Build an AI-Assisted Feature with Git"
sidebar_position: 6
description: "Put all your Git skills together in a realistic project: create a repository, use AI to build a feature, practice checkpoints and branching, create a pull request, and collaborate safely."
---

# Comprehensive Project: Build an AI-Assisted Feature with Git

## Project Overview

This comprehensive project brings together everything you've learned in Chapter 8. You'll simulate a realistic AI-driven development workflow from start to finish:

✅ Initialize a Git repository
✅ Create checkpoint commits before AI sessions
✅ Use Claude Code or Gemini CLI to generate code
✅ Practice branch-based experimentation
✅ Simulate code review and iterate on feedback
✅ Create and merge a pull request
✅ Use natural language prompts for Git operations

**Time estimate:** 60-90 minutes

**Prerequisites:** Completion of Lessons 1-5

---

## Project Scenario

You're building a **task management CLI tool** in Python. You'll work with AI assistants to build features while using Git to ensure safety and collaboration.

The project will have:
1. **Basic task management** (add, list, complete tasks)
2. **Data persistence** (save tasks to a JSON file)
3. **User-friendly CLI** (colored output, help messages)
4. **Tests** (basic unit tests for core functions)

You'll practice:
- Creating checkpoints before AI code generation
- Using branches to isolate experiments
- Simulating team code review
- Merging with proper Git hygiene
- Using natural language prompts for complex Git operations

---

## Phase 1: Repository Setup

### Step 1: Create Project Directory and Initialize Git

**Task:** Set up your project with Git.

```bash
# Create project directory
mkdir task-manager-ai
cd task-manager-ai

# Initialize Git repository
git init

# Verify
git status
# Should show: "On branch main, no commits yet"
```

### Step 2: Create Initial Project Structure

**Task:** Create basic project files.

**Create `README.md`:**
```markdown
# Task Manager CLI

A simple command-line task manager built with Python and AI assistance.

## Features
- Add tasks
- List tasks
- Mark tasks as complete
- Persistent storage

## Development
This project was built using AI-driven development with Git for safety.
```

**Create `.gitignore`:**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Project-specific
tasks.json
*.log
```

**Create `requirements.txt`:**
```
# No external dependencies yet
# Will add as needed
```

### Step 3: Initial Commit

**Task:** Make your first commit.

```bash
git add README.md .gitignore requirements.txt
git commit -m "Initial project setup

Project structure:
- README with feature overview
- .gitignore for Python projects
- requirements.txt for dependencies

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Verify
git log --oneline
# Should show your initial commit
```

**✅ Checkpoint:** You now have a Git repository with an initial commit.

---

## Phase 2: Build Core Functionality with AI

### Step 4: Create Checkpoint Before AI Session

**Task:** Always create a checkpoint before letting AI generate code.

```bash
# Verify current state
git status
# Should be clean

# Create checkpoint commit
git commit --allow-empty -m "Checkpoint: Starting AI-assisted feature development

About to use Claude Code to generate core task management functions.

Current state: Project initialized, ready for feature implementation.

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Why empty commit?** No files changed yet, but we want a marker in history.

### Step 5: Use AI to Generate Core Module

**Task:** Ask Claude Code or Gemini CLI to create the task manager core.

**Prompt for AI:**
```
"Create a Python module called task_manager.py with these functions:

1. add_task(description) - Add a new task
2. list_tasks() - Display all tasks with status
3. complete_task(task_id) - Mark a task as complete
4. save_tasks() - Save tasks to tasks.json
5. load_tasks() - Load tasks from tasks.json

Use a simple data structure: list of dictionaries with id, description, and completed status.

Include docstrings and type hints."
```

**Expected output:** `task_manager.py` with all functions implemented.

**After AI generates the code:**

1. **Review the code** - Read through it, make sure you understand it
2. **Test it manually** - Run Python interpreter and try the functions
3. **Make any necessary adjustments** - Fix any issues you find

### Step 6: Commit the Core Module

**Task:** Commit the AI-generated code with proper attribution.

```bash
git add task_manager.py
git commit -m "Add core task management functions

Implemented:
- add_task(description): Create new tasks
- list_tasks(): Display all tasks with status
- complete_task(task_id): Mark tasks complete
- save_tasks() / load_tasks(): JSON persistence

Data structure: List of dicts with id, description, completed

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**✅ Checkpoint:** Core functionality is implemented and committed.

---

## Phase 3: Branch-Based Experimentation

### Step 7: Create Feature Branch for CLI Interface

**Task:** Use a branch to isolate CLI development.

```bash
# Create and switch to feature branch
git checkout -b feature/cli-interface

# Verify
git branch
# Should show: * feature/cli-interface
```

### Step 8: Implement CLI with AI

**Task:** Ask AI to create a CLI interface.

**Prompt for AI:**
```
"Create a CLI script called cli.py that uses task_manager.py with these features:

1. Command-line argument parsing (add, list, complete commands)
2. Colored output (use colorama library for green/red status indicators)
3. Help messages explaining usage
4. Error handling for invalid commands

Example usage:
  python cli.py add "Buy groceries"
  python cli.py list
  python cli.py complete 1

Update requirements.txt to include colorama."
```

**After AI generates:**

1. **Review** the CLI implementation
2. **Test** all commands manually
3. **Update requirements.txt** with colorama

### Step 9: Commit CLI Implementation

```bash
git add cli.py requirements.txt
git commit -m "Add CLI interface with colored output

Features:
- Argument parsing for add/list/complete commands
- Colorama for colored task status (green=done, red=pending)
- Help messages and error handling
- User-friendly command-line experience

Usage:
  python cli.py add \"Task description\"
  python cli.py list
  python cli.py complete <id>

Dependencies added: colorama

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**✅ Checkpoint:** CLI interface is working on feature branch.

---

## Phase 4: Testing and Iteration

### Step 10: Add Tests (Still on Feature Branch)

**Task:** Ask AI to generate tests.

**Prompt for AI:**
```
"Create test_task_manager.py with unit tests for:

1. add_task() - Verify task creation
2. complete_task() - Verify status changes
3. save_tasks() and load_tasks() - Verify persistence
4. Edge cases: empty lists, invalid IDs, missing files

Use Python's unittest framework."
```

### Step 11: Run Tests and Fix Issues

```bash
# Run tests
python -m unittest test_task_manager.py

# If tests fail, ask AI:
# "These tests are failing: [paste errors]. Help me fix the implementation."

# Make fixes, then commit
git add test_task_manager.py task_manager.py
git commit -m "Add unit tests and fix edge cases

Tests cover:
- Task creation and listing
- Status changes (complete/incomplete)
- Persistence (save/load JSON)
- Edge cases (empty, invalid IDs, missing files)

Fixed bugs discovered during testing:
- Handle missing tasks.json on first load
- Validate task IDs before completing
- Ensure unique IDs for new tasks

All tests passing.

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**✅ Checkpoint:** Tests are passing on feature branch.

---

## Phase 5: Prepare for Code Review

### Step 12: Update Documentation

**Task:** Update README with usage instructions.

**Edit `README.md`:**
```markdown
# Task Manager CLI

A simple command-line task manager built with Python and AI assistance.

## Features
- ✅ Add tasks
- ✅ List tasks with colored status indicators
- ✅ Mark tasks as complete
- ✅ Persistent storage (JSON)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

**Add a task:**
```bash
python cli.py add "Buy groceries"
```

**List all tasks:**
```bash
python cli.py list
```

**Complete a task:**
```bash
python cli.py complete 1
```

**Get help:**
```bash
python cli.py --help
```

## Development

This project was built using AI-driven development with Git for safety:
- Core logic generated by Claude Code
- Tests ensure reliability
- Git branches used for feature isolation
- Pull requests for code review

## Testing

Run tests:
```bash
python -m unittest test_task_manager.py
```

## License

MIT License
```

### Step 13: Commit Documentation

```bash
git add README.md
git commit -m "Update README with installation and usage instructions

Added:
- Installation steps (pip install requirements)
- Usage examples for all commands
- Testing instructions
- Development methodology note

Documentation is now complete for code review.

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**✅ Checkpoint:** Feature branch is ready for review.

---

## Phase 6: Push to GitHub and Create Pull Request

### Step 14: Create GitHub Repository

**Task:** Create a repository on GitHub.

**Option A: Using GitHub Web UI**
1. Go to GitHub.com
2. Click "+" → "New repository"
3. Name: `task-manager-ai`
4. Description: "CLI task manager built with AI-driven development"
5. **Do NOT** initialize with README (you already have one)
6. Click "Create repository"

**Option B: Using GitHub CLI**
```bash
gh repo create task-manager-ai --public --source=. --remote=origin --description "CLI task manager built with AI-driven development"
```

### Step 15: Push Main Branch

```bash
# Add remote (if not using gh CLI)
git remote add origin https://github.com/YOUR_USERNAME/task-manager-ai.git

# Push main branch
git checkout main
git push -u origin main
```

### Step 16: Push Feature Branch

```bash
# Switch back to feature branch
git checkout feature/cli-interface

# Push feature branch
git push -u origin feature/cli-interface
```

### Step 17: Create Pull Request

**Using GitHub Web UI:**
1. Go to your repository on GitHub
2. You'll see: "feature/cli-interface had recent pushes"
3. Click "Compare & pull request"
4. Fill in the PR description (see template below)
5. Click "Create pull request"

**Using GitHub CLI:**
```bash
gh pr create --title "Add CLI interface with task management features" --body "
## Summary
Implements a complete CLI task manager with colored output and persistent storage.

## What Changed
- Core task management module (add, list, complete, save/load)
- CLI interface with argument parsing and colored output
- Unit tests covering all functionality
- Updated documentation with usage instructions

## Features
✅ Add tasks via command line
✅ List tasks with visual status (green=complete, red=pending)
✅ Mark tasks complete
✅ JSON persistence for data storage
✅ Comprehensive test coverage

## Testing
All unit tests passing:
\`\`\`bash
python -m unittest test_task_manager.py
\`\`\`

Manual testing completed:
- Created 5 tasks
- Listed tasks (verified colored output)
- Completed tasks (status updated correctly)
- Restarted CLI (persistence works)

## AI Collaboration
- Initial module structure generated with Claude Code
- CLI implementation refined through iteration
- Tests generated and edge cases fixed with AI guidance
- Documentation written with AI assistance

All AI-generated code was reviewed and tested before committing.

## Checklist
- [x] All tests passing
- [x] Documentation complete
- [x] No hardcoded secrets or sensitive data
- [x] Code follows Python best practices
- [x] AI attribution included in commits
"
```

**✅ Checkpoint:** Pull request created and ready for review.

---

## Phase 7: Simulate Code Review

### Step 18: Review Your Own Code

**Task:** Pretend you're a teammate reviewing this PR. Look for issues.

**Review checklist:**

1. **Correctness**
   - Do all functions work as expected?
   - Are there bugs or edge cases not handled?

2. **Security**
   - Are there any hardcoded secrets?
   - Is user input validated?

3. **Code quality**
   - Is the code readable?
   - Are there docstrings and type hints?
   - Is error handling present?

4. **Testing**
   - Do tests cover the main functionality?
   - Are edge cases tested?

5. **Documentation**
   - Is the README clear and complete?
   - Are usage examples provided?

**Find at least 2 improvements** you could make. Here are examples:

**Example Issue 1:** "The complete_task function doesn't handle invalid task IDs gracefully."

**Example Issue 2:** "The README doesn't mention that you need Python 3.7+ installed."

### Step 19: Address Review Feedback

**Task:** Make improvements based on your review.

**Example fixes:**

**Fix 1: Improve error handling**
```python
# In task_manager.py
def complete_task(task_id):
    """Mark a task as complete by ID."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            return True
    # Add this:
    raise ValueError(f"Task ID {task_id} not found")
```

**Fix 2: Update README with Python version**
```markdown
## Requirements

- Python 3.7 or higher
- pip for installing dependencies
```

**Commit your fixes:**
```bash
git add task_manager.py README.md
git commit -m "Address code review feedback

Changes:
- Improve error handling in complete_task (raise ValueError for invalid IDs)
- Add Python version requirement to README (3.7+)
- Better user experience when invalid task ID provided

Addresses review comments from self-review.

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Push the update
git push
```

**Result:** Your PR is automatically updated on GitHub.

**✅ Checkpoint:** Review feedback addressed and pushed.

---

## Phase 8: Merge and Cleanup

### Step 20: Merge the Pull Request

**Task:** Merge your PR on GitHub.

**Using GitHub Web UI:**
1. Go to your PR page
2. Scroll to bottom
3. Click "Merge pull request"
4. Click "Confirm merge"
5. Optionally click "Delete branch" (cleanup)

**Using GitHub CLI:**
```bash
# Merge the PR
gh pr merge --merge --delete-branch

# Follow prompts to confirm
```

### Step 21: Update Local Repository

**Task:** Sync your local repository with GitHub.

```bash
# Switch to main
git checkout main

# Pull the merged changes
git pull origin main

# Verify the merge
git log --oneline -n 5
# Should show your feature commits merged into main

# Delete local feature branch
git branch -d feature/cli-interface

# Verify branches
git branch
# Should only show: * main
```

**✅ Checkpoint:** PR merged, branches cleaned up, local repository synchronized.

---

## Phase 9: Practice Natural Language Prompts

### Step 22: View Project History Using Natural Language

**Task:** Use Claude Code to explore your Git history.

**Prompt 1:** View commits
```
"Show me all commits in this repository with a visual graph"
```

**Expected:** Claude Code runs `git log --oneline --graph --all`

---

**Prompt 2:** Find specific changes
```
"Show me which commits modified task_manager.py"
```

**Expected:** Claude Code runs `git log --oneline --follow -- task_manager.py`

---

**Prompt 3:** See authorship
```
"Show me who last modified each line in cli.py"
```

**Expected:** Claude Code runs `git blame cli.py`

---

**Prompt 4:** Understand a commit
```
"Show me exactly what changed in commit [paste commit hash]"
```

**Expected:** Claude Code runs `git show <commit-hash>`

---

### Step 23: Practice "What If" Scenarios

**Task:** Ask AI about Git scenarios without actually executing them.

**Scenario 1: Accidental commit**
```
"What if I accidentally committed sensitive data? How would I remove it from history?"
```

**Expected answer:** AI explains `git filter-branch` or BFG Repo-Cleaner, warns about rewriting history, suggests prevention (.gitignore).

---

**Scenario 2: Merge vs. Rebase**
```
"I'm about to update my feature branch with main. Should I merge or rebase? What's the difference?"
```

**Expected answer:** AI explains merge (preserves history, creates merge commit) vs. rebase (rewrites commits, linear history), suggests merge for shared branches.

---

**Scenario 3: Recovering deleted branch**
```
"What if I accidentally deleted a branch with important work? Can I recover it?"
```

**Expected answer:** AI explains `git reflog` and how to find deleted branch commits, shows recovery steps.

---

**✅ Checkpoint:** You've practiced using natural language prompts for Git exploration.

---

## Phase 10: Reflection and Self-Assessment

### Step 24: Answer Reflection Questions

Take a moment to reflect on what you learned:

**Reflection 1: Safety**
> How did checkpoints and branches make you feel safer when working with AI-generated code?

**Your answer:**
[Write your thoughts. Example: "Knowing I could rollback at any point made me comfortable experimenting with different AI suggestions. I tried multiple approaches without fear."]

---

**Reflection 2: Code Review Value**
> What issues did you find during your self-review that you missed initially?

**Your answer:**
[Write your thoughts. Example: "I found error handling gaps and missing documentation. Code review is valuable even when reviewing your own work."]

---

**Reflection 3: Natural Language Convenience**
> How did natural language prompts change your Git experience compared to memorizing commands?

**Your answer:**
[Write your thoughts. Example: "I focused on *what* I wanted to know instead of *how* to ask Git. This let me explore the history naturally without looking up syntax."]

---

**Reflection 4: AI Collaboration**
> What did you learn about working with AI tools for code generation?

**Your answer:**
[Write your thoughts. Example: "AI is great for boilerplate and structure, but I still need to review and understand the code. The combination of AI speed and human judgment works well."]

---

### Step 25: Verify Project Completion

**Checklist - Mark each item complete:**

- [ ] ✅ Created Git repository with initial commit
- [ ] ✅ Created checkpoint commits before AI sessions
- [ ] ✅ Used AI to generate core functionality
- [ ] ✅ Created feature branch for CLI development
- [ ] ✅ Implemented tests and verified they pass
- [ ] ✅ Pushed code to GitHub
- [ ] ✅ Created pull request with detailed description
- [ ] ✅ Reviewed code and addressed feedback
- [ ] ✅ Merged PR successfully
- [ ] ✅ Cleaned up branches (local and remote)
- [ ] ✅ Used natural language prompts for Git operations
- [ ] ✅ Completed reflection questions

**If all items are checked, congratulations! You've completed the comprehensive project.**

---

## Success Criteria

You've successfully completed this project if you:

✅ **Safety**: Created checkpoints before AI changes, used branches for isolation
✅ **AI Collaboration**: Generated code with AI, reviewed and understood it
✅ **Git Workflow**: Created repository, made meaningful commits, pushed to GitHub
✅ **Team Collaboration**: Created PR, simulated review, addressed feedback, merged
✅ **Natural Language**: Used AI prompts to explore history and understand Git concepts
✅ **Understanding**: Can explain what you did and why at each step

---

## Going Further (Optional Extensions)

Want to continue practicing? Try these extensions:

### Extension 1: Add More Features
- Use AI to add task priorities (high, medium, low)
- Add task due dates with reminders
- Implement task categories or tags

Practice: Create a new feature branch for each addition, create separate PRs.

### Extension 2: Practice Conflict Resolution
- Create two separate branches that modify the same file
- Merge one into main
- Attempt to merge the second (will conflict)
- Resolve the conflict with AI guidance

### Extension 3: Experiment with Rebasing
- Create a feature branch with several commits
- Make commits on main while working
- Use AI to guide you through rebasing your feature branch onto updated main
- Understand when to rebase vs. merge

### Extension 4: Contribute to Open Source
- Find a beginner-friendly open source project on GitHub
- Fork the repository
- Create a small improvement (documentation, bug fix, tests)
- Open a real pull request
- Experience the full collaborative workflow

---

## Conclusion

You've successfully completed a realistic AI-driven development workflow:

🎯 **What you accomplished:**
- Built a functional CLI application with AI assistance
- Used Git as a safety net for experimentation
- Practiced professional collaboration workflows
- Learned to use natural language prompts as a convenience layer
- Gained confidence in AI-assisted development

🚀 **What's next:**
- Apply these Git patterns to all your future projects
- Use checkpoints and branches as standard practice
- Collaborate with real teammates using pull requests
- Continue using AI as a learning tool and productivity multiplier

**Remember:**
- Git is your safety net—experiment fearlessly
- AI is your collaborator—review everything it generates
- Understanding beats memorization—know *what* and *why*, let AI handle *how*
- Code review catches bugs—even your own reviews add value

**You're now equipped for professional AI-driven development. Build amazing things!**
