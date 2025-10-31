---
title: "Quick Reference Card: Essential Git Commands"
sidebar_position: 7
description: "A concise cheat sheet of 15-20 essential Git commands for AI-driven development workflows."
---

# Quick Reference Card: Essential Git Commands

**Quick access to the most important Git commands for AI-driven development.**

Print this page or bookmark it for quick reference while working!

---

## Repository Setup

### Initialize a New Repository

```bash
git init
```
**When to use:** Starting a new project from scratch.

**Example:**
```bash
mkdir my-project
cd my-project
git init
```

---

### Clone an Existing Repository

```bash
git clone <url>
```
**When to use:** Downloading a project from GitHub to work on it locally.

**Example:**
```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

---

### Check Remote Connections

```bash
git remote -v
```
**When to use:** Verify which GitHub repository your local repo is connected to.

**Example output:**
```
origin  https://github.com/username/repo.git (fetch)
origin  https://github.com/username/repo.git (push)
```

---

## Daily Workflow

### Check Repository Status

```bash
git status
```
**When to use:** **Always** before making commits. Shows what changed and what's staged.

**What to look for:**
- Red files = changed but not staged
- Green files = staged and ready to commit
- Untracked files = not in Git yet

---

### View Changes (Diff)

```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --staged

# Show changes in specific file
git diff filename.py
```
**When to use:** Before committing, to review what you're about to save.

---

### Stage Files for Commit

```bash
# Stage specific file
git add filename.py

# Stage all changed files
git add .

# Stage multiple files
git add file1.py file2.py

# Stage all files of a type
git add *.py
```
**When to use:** After making changes and before committing.

**Tip:** Use `git add .` carefully—verify with `git status` first to avoid staging unwanted files.

---

### Create a Commit

```bash
git commit -m "Your commit message here"
```
**When to use:** After staging files, to save a snapshot in history.

**Good commit message format:**
```bash
git commit -m "Add user authentication feature

Implemented:
- Login endpoint with JWT tokens
- Password hashing with bcrypt
- Session management

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### View Commit History

```bash
# Simple one-line format
git log --oneline

# Last 5 commits
git log --oneline -n 5

# Visual graph with branches
git log --oneline --graph --all

# Detailed view with diffs
git log -p
```
**When to use:** To see what's been done recently or find a specific commit.

---

## Branching

### List All Branches

```bash
git branch

# Include remote branches
git branch -a
```
**When to use:** To see which branches exist and which one you're currently on.

**Example output:**
```
* main
  feature/new-ui
  fix/login-bug
```
(* indicates current branch)

---

### Create a New Branch

```bash
# Create and switch to new branch
git checkout -b feature/branch-name

# Or using newer syntax (Git 2.23+)
git switch -c feature/branch-name
```
**When to use:** Before starting work on a new feature or experiment.

**Naming conventions:**
- `feature/` for new features
- `fix/` or `bugfix/` for bug fixes
- `experiment/` for experiments
- `hotfix/` for urgent production fixes

---

### Switch Between Branches

```bash
# Old syntax
git checkout branch-name

# New syntax (Git 2.23+)
git switch branch-name
```
**When to use:** Moving between different lines of work.

**Important:** Commit or stash changes before switching branches!

---

### Merge Branch into Current Branch

```bash
# Switch to destination branch (usually main)
git checkout main

# Merge source branch
git merge feature/branch-name
```
**When to use:** After finishing work on a feature branch, merge it back to main.

**If conflicts occur:** Git will tell you which files have conflicts. Resolve them, then:
```bash
git add resolved-file.py
git commit -m "Merge feature/branch-name, resolved conflicts"
```

---

### Delete a Branch

```bash
# Safe delete (only if merged)
git branch -d branch-name

# Force delete (even if not merged)
git branch -D branch-name
```
**When to use:** After merging a feature branch, clean it up.

**Warning:** `-D` is destructive—only use if you're sure!

---

## Working with GitHub

### Push to GitHub

```bash
# First time pushing a branch
git push -u origin branch-name

# Subsequent pushes (after -u is set)
git push
```
**When to use:** Uploading your local commits to GitHub.

**Common workflow:**
```bash
git add .
git commit -m "Add new feature"
git push origin feature-branch
```

---

### Pull from GitHub

```bash
# Pull changes from remote
git pull origin main

# Or just
git pull
```
**When to use:** Downloading changes others made to the shared repository.

**Before starting new work:** Always pull to ensure you have the latest code.

---

### Fetch Without Merging

```bash
git fetch origin
```
**When to use:** See what's on GitHub without automatically merging into your branch.

**Difference from pull:**
- `fetch` = download info, don't merge
- `pull` = download and merge

---

## Undoing Changes

### Discard Uncommitted Changes

```bash
# Discard changes in specific file
git restore filename.py

# Discard all uncommitted changes
git restore .

# Old syntax (still works)
git checkout -- filename.py
```
**When to use:** You made changes but want to go back to the last commit.

**⚠️ Warning:** Changes are lost permanently!

---

### Unstage Files (Keep Changes)

```bash
# Unstage specific file
git restore --staged filename.py

# Unstage all files
git restore --staged .

# Old syntax
git reset HEAD filename.py
```
**When to use:** You staged files but want to unstage them without losing changes.

---

### Undo Last Commit (Keep Changes)

```bash
git reset --soft HEAD~1
```
**When to use:** You committed but want to modify the commit (add more changes, fix message, etc.).

**What it does:**
- Removes the commit from history
- **Keeps all changes staged**
- You can now edit and re-commit

---

### Undo Last Commit (Discard Changes)

```bash
git reset --hard HEAD~1
```
**When to use:** You made a commit that's completely wrong and want to delete it.

**⚠️ Warning:** This is destructive! Changes are gone permanently.

**Safer alternative:** Create a backup branch first:
```bash
git branch backup-branch
git reset --hard HEAD~1
```

---

### Revert a Commit (Safe for Shared Code)

```bash
git revert <commit-hash>
```
**When to use:** You pushed a commit to GitHub and need to undo it.

**What it does:**
- Creates a **new commit** that undoes the specified commit
- **Doesn't rewrite history** (safe for collaboration)

**Example:**
```bash
git log --oneline
# abc123 Bad commit
# def456 Good commit

git revert abc123
# Creates new commit undoing abc123
```

---

## Stashing (Temporary Saves)

### Save Work Temporarily

```bash
# Stash with auto-generated message
git stash

# Stash with descriptive message
git stash push -m "WIP: refactoring auth module"
```
**When to use:** You need to switch branches but aren't ready to commit current work.

---

### View Stashed Changes

```bash
git stash list
```
**Example output:**
```
stash@{0}: WIP: refactoring auth module
stash@{1}: On feature: experimental UI changes
```

---

### Apply Stashed Changes

```bash
# Apply most recent stash and remove it from list
git stash pop

# Apply specific stash (keeps it in list)
git stash apply stash@{1}
```
**When to use:** After switching back to the branch where you stashed work.

---

### Delete Stashed Changes

```bash
# Delete specific stash
git stash drop stash@{0}

# Delete all stashes
git stash clear
```

---

## Collaboration

### View Who Modified Each Line

```bash
git blame filename.py
```
**When to use:** Finding out who wrote specific code or when a line was last changed.

**Example output:**
```
abc123 (John Doe 2024-01-15) def login(username, password):
def456 (Jane Smith 2024-01-20)     return authenticate(username)
```

---

### View File History

```bash
# Show commits that modified a file
git log --oneline -- filename.py

# Follow file through renames
git log --follow -- filename.py
```
**When to use:** Tracking changes to a specific file over time.

---

### View Specific Commit Details

```bash
git show <commit-hash>
```
**When to use:** See exactly what changed in a particular commit.

**Example:**
```bash
git log --oneline
# abc123 Add user authentication

git show abc123
# Shows full diff of that commit
```

---

## Advanced (Use with Caution)

### Force Push (Dangerous!)

```bash
# Safer force push (fails if remote has changes you don't have)
git push --force-with-lease origin branch-name

# True force push (overwrites remote, very dangerous)
git push --force origin branch-name
```
**When to use:** After rewriting history locally (rebase, amend) and need to update GitHub.

**⚠️ NEVER force push to main or shared branches!**

**Only force push:**
- On your personal feature branches
- When working alone
- After confirming no one else has pulled your branch

---

### Amend Last Commit

```bash
# Change commit message
git commit --amend -m "New commit message"

# Add more changes to last commit
git add forgotten-file.py
git commit --amend --no-edit
```
**When to use:** You just made a commit and realized you forgot something or need to fix the message.

**⚠️ Warning:** Only amend commits that haven't been pushed! Amending rewrites history.

---

## Configuration

### Set Your Identity

```bash
# Set name (required for commits)
git config --global user.name "Your Name"

# Set email (required for commits)
git config --global user.email "your.email@example.com"

# View current config
git config --list
```
**When to use:** First time setting up Git on a new computer.

---

### Create Aliases (Shortcuts)

```bash
# Create shortcuts for common commands
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph --all"

# Now you can use:
git st    # instead of git status
git lg    # instead of git log --oneline --graph --all
```

---

## Troubleshooting

### "Your branch is behind 'origin/main'"

**Solution:**
```bash
git pull origin main
```
This downloads commits from GitHub that you don't have locally.

---

### "CONFLICT: Merge conflict in file.py"

**Solution:**
1. Open `file.py`
2. Look for conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
3. Edit to keep the version you want
4. Delete all conflict markers
5. Save the file
6. Mark as resolved:
```bash
git add file.py
git commit -m "Resolved merge conflict in file.py"
```

---

### "fatal: refusing to merge unrelated histories"

**Solution:**
```bash
git pull origin main --allow-unrelated-histories
```
**Why:** Usually happens when connecting a local repo to an existing GitHub repo. Use with caution.

---

### "error: failed to push some refs"

**Solution:**
```bash
git pull origin main
# Resolve any conflicts
git push origin main
```
**Why:** Someone else pushed to GitHub while you were working. Pull their changes first.

---

## Natural Language Alternative

**Don't want to memorize these commands?**

Ask Claude Code or Gemini CLI:

```
"Show me the status of my repository"
"Create a new branch called feature/authentication"
"Merge my feature branch into main"
"Undo my last commit but keep the changes"
"I have a merge conflict in auth.py, help me resolve it"
```

**AI will:**
- Translate your intent into the correct Git command
- Explain what it's doing
- Handle complex multi-step operations
- Help you understand errors

---

## Quick Workflow Checklist

**Starting a new feature:**
```bash
git checkout main
git pull origin main
git checkout -b feature/new-feature
```

**Regular commit workflow:**
```bash
git status                  # Check what changed
git add .                   # Stage changes
git commit -m "message"     # Commit
git push origin branch-name # Push to GitHub
```

**Finishing a feature:**
```bash
git checkout main
git pull origin main
git merge feature/new-feature
git push origin main
git branch -d feature/new-feature
```

**Creating a pull request:**
```bash
git push -u origin feature/branch-name
# Then create PR on GitHub
```

---

## Most Important Commands (If You Only Remember 5)

1. **`git status`** - Always know what's changed
2. **`git add . && git commit -m "message"`** - Save your work
3. **`git checkout -b feature/name`** - Create feature branches
4. **`git push origin branch-name`** - Upload to GitHub
5. **Ask AI** - When you forget or need help!

---

## Remember

✅ **Commit often** - Especially before AI changes
✅ **Use branches** - Keep main stable
✅ **Pull before pushing** - Avoid conflicts
✅ **Review before committing** - Use `git status` and `git diff`
✅ **Ask AI when stuck** - Natural language is your friend

**Git is your safety net. Use it fearlessly!**
