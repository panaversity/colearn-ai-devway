---
title: "Lesson 3: Safe Experimentation - Branches, Checkpoints, and Rollback"
sidebar_position: 3
description: "Master the art of fearless experimentation with AI tools using Git's checkpoint pattern, branches, and rollback capabilities."
---

# Lesson 3: Safe Experimentation - Branches, Checkpoints, and Rollback

## The Power of Fearless Experimentation

Picture this: Claude Code offers to refactor your entire authentication system. It promises better security, cleaner code, and improved performance. Do you accept?

Without Git branching and checkpoints, this is a terrifying question. If you accept and something breaks, you're stuck manually undoing hundreds of lines of changes. You might miss something. You might introduce new bugs while trying to fix the AI's mistakes.

With Git's safety mechanisms, this same question becomes exciting. You create a checkpoint, let Claude Code refactor everything, test the results, and if anything goes wrong—you're back to working code in 30 seconds. No risk. No fear. Just experimentation.

This lesson teaches you the patterns that make AI-assisted development safe: **checkpoints before changes**, **branches for isolation**, and **rollback when needed**. These aren't just Git commands—they're a mindset that transforms how you work with AI tools.

By the end of this lesson, you'll experiment boldly, knowing you can always go back.

## Part I: The Checkpoint Pattern

### The Golden Rule: Commit Before Every AI Session

Here's the most important Git habit you'll develop:

> **Before you ask an AI tool to modify your code, create a checkpoint commit.**

This single habit makes everything else possible. It gives you a known-good state to return to. It makes rollback trivial. It removes fear from experimentation.

### What Is a Checkpoint Commit?

A checkpoint commit is a regular Git commit that marks a stable, working state before you make risky changes. It's not about completing a feature—it's about creating a safety net.

**Example checkpoint workflow:**

```bash
# Your code is working right now
git status  # Check what's uncommitted

# Create a checkpoint
git add .
git commit -m "Checkpoint: working authentication before Claude Code refactoring

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Now safely let AI modify your code
```

### When to Create Checkpoints

Create checkpoint commits:

1. **Before AI refactoring** - "Claude Code, optimize this function"
2. **Before AI feature generation** - "Gemini CLI, add user profile editing"
3. **Before experimental changes** - "Let me try a completely different approach"
4. **Before switching contexts** - "I need to work on something else, save current state"
5. **After completing working increments** - "This piece works, lock it in"

### Checkpoint Commit Message Pattern

Good checkpoint messages are specific and actionable:

✅ **Good checkpoints:**
- "Checkpoint: working login before async/await refactoring"
- "Checkpoint: stable payment processing before adding webhooks"
- "Checkpoint: tests passing before Claude Code optimization"

❌ **Poor checkpoints:**
- "WIP" (what work? what's in progress?)
- "Checkpoint" (checkpoint of what?)
- "Saving changes" (why? what state?)

### The Psychology of Checkpoints

Checkpoints change how you think:

**Without checkpoints:**
- "Should I try this? What if it breaks?"
- "Maybe I should manually back up these files first..."
- "I'll just make small, timid changes to be safe"

**With checkpoints:**
- "Let's try it—worst case, I revert"
- "I can experiment boldly because I have a safety net"
- "If this approach fails, I'll learn something and try another"

This psychological shift is the real power of Git. You stop being defensive and start being exploratory.

### Checkpoint Demonstration

Let's see the checkpoint pattern in action:

```bash
# You're working on a Python calculator
# Currently: basic arithmetic works

# 1. Verify current state
python calculator.py
# Output: All tests pass

# 2. Create checkpoint
git status
git add .
git commit -m "Checkpoint: basic arithmetic working before AI refactoring

Current state:
- Addition, subtraction, multiplication, division all work
- Input validation handles edge cases
- Tests: 12/12 passing

About to: Ask Claude Code to add scientific functions (sin, cos, log, exp)

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# 3. Now safely experiment
# Ask Claude Code: "Add scientific calculator functions (sin, cos, log, exp)"
```

If Claude Code's changes break something, you have a clear revert point. If they work perfectly, you've made progress. Either way, you're safe.

## Part II: Branch-Based Experimentation

### What Is a Branch?

A branch is a parallel timeline for your code. Imagine your project is a tree:

- **Main branch** (trunk): Your stable, production-ready code
- **Feature branches** (branches): Experimental workspaces that don't affect the trunk

When you create a branch, you're saying: "I want to try something without risking the main codebase." You can make any changes you want on a branch. If they work, you merge them back to main. If they don't, you delete the branch. Main remains untouched.

### Why Branches Matter for AI Development

AI tools can generate large amounts of code quickly. Sometimes it's brilliant. Sometimes it needs iteration. Sometimes it's completely wrong.

Branches let you:
- **Isolate AI experiments** - Try radical refactorings without touching working code
- **Compare approaches** - "Let's see Claude Code's approach vs. Gemini CLI's approach"
- **Collaborate safely** - Share AI-generated code for review before merging
- **Abandon failures** - Delete failed experiments without a trace

### Basic Branch Operations

**Check current branch:**
```bash
git branch
# Output: * main (asterisk shows current branch)
```

**Create and switch to a new branch:**
```bash
git checkout -b feature/ai-refactoring
# Creates branch "feature/ai-refactoring" and switches to it

# Alternative (Git 2.23+):
git switch -c feature/ai-refactoring
```

**List all branches:**
```bash
git branch
# Output:
#   main
# * feature/ai-refactoring (current branch)
```

**Switch back to main:**
```bash
git checkout main
# or
git switch main
```

**Delete a branch:**
```bash
git branch -d feature/ai-refactoring
# Safe delete: only works if branch is merged

git branch -D feature/ai-refactoring
# Force delete: deletes even if not merged (use carefully!)
```

### Branch-Based Experimentation Workflow

Here's the pattern you'll use constantly:

```bash
# 1. Start on main branch with working code
git checkout main

# 2. Create a checkpoint on main (optional but recommended)
git add .
git commit -m "Checkpoint: stable state before AI experiment"

# 3. Create an experiment branch
git checkout -b experiment/claude-refactoring

# 4. Let AI modify code (Claude Code, Gemini CLI, etc.)
# Make changes, test, iterate

# 5. Commit the AI changes
git add .
git commit -m "Refactor authentication using Claude Code suggestions

Changes:
- Converted sync functions to async/await
- Added connection pooling
- Improved error handling

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# 6. Test thoroughly
# Run tests, check functionality, look for bugs

# 7a. If successful: merge back to main
git checkout main
git merge experiment/claude-refactoring
git branch -d experiment/claude-refactoring

# 7b. If failed: abandon the experiment
git checkout main
git branch -D experiment/claude-refactoring
# Your main branch is unchanged - no harm done
```

### Real-World Branching Scenario

**Scenario**: You want Claude Code to optimize a slow data processing function.

```bash
# Your data processor works but takes 10 seconds per file

# 1. Checkpoint on main
git checkout main
git add .
git commit -m "Checkpoint: data processor functional before optimization"

# 2. Create optimization branch
git checkout -b optimize/data-processor

# 3. Ask Claude Code: "Optimize process_data() for speed"
# AI suggests using multiprocessing and batch operations

# 4. Test the changes
python test_processor.py
# Success: Now processes in 2 seconds per file!

# 5. Commit the optimization
git add .
git commit -m "Optimize data processor using multiprocessing

Performance improvements:
- Process time: 10s → 2s per file (80% faster)
- Memory usage: stable
- All tests passing

Implementation:
- Added multiprocessing.Pool for parallel processing
- Batch operations for file I/O
- Progress tracking with tqdm

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# 6. Merge to main
git checkout main
git merge optimize/data-processor
git branch -d optimize/data-processor

# Now main has the optimized code
```

**What if it failed?**

```bash
# After step 3, you test and find:
python test_processor.py
# Error: Multiprocessing breaks on Windows, tests fail

# No problem - abandon the branch
git checkout main
git branch -D optimize/data-processor

# Try a different approach
git checkout -b optimize/data-processor-v2
# Ask Claude Code: "Optimize without multiprocessing - use generators and streaming"
```

### Branch Naming Conventions

Use descriptive branch names that show intent:

✅ **Good branch names:**
- `feature/user-authentication`
- `experiment/claude-refactoring`
- `fix/login-bug`
- `optimize/database-queries`

❌ **Poor branch names:**
- `test`
- `new-branch`
- `my-branch`
- `temp`

## Part III: Undoing Changes

### The Three Ways to Undo

Git provides three main ways to undo changes, each for different situations:

1. **git restore** - Discard uncommitted changes (most common)
2. **git reset** - Move back in commit history (powerful, use carefully)
3. **git revert** - Create a new commit that undoes a previous commit (safest for shared code)

Let's understand each one.

### git restore: Discard Uncommitted Changes

**When to use:** You've made changes but haven't committed yet, and you want to throw them away.

**Scenario**: Claude Code modified a file, but you don't like the changes.

```bash
# Claude Code edited config.py
# You test it and don't like the results

# Discard changes to specific file
git restore config.py
# File is now back to the last committed version

# Or discard ALL uncommitted changes
git restore .
# Everything reverts to last commit
```

**Important:** `git restore` is destructive—changes are gone forever. Make sure you want to discard them.

### git reset: Move Back in Commit History

**When to use:** You've committed changes but want to undo those commits.

There are three types of reset:

#### Soft Reset: Undo Commit, Keep Changes

```bash
# You committed but realize you forgot something
git reset --soft HEAD~1

# Effect:
# - Last commit is gone from history
# - Changes are still in your files
# - Changes are staged (ready to commit again)

# Use case: "I want to modify this commit"
```

#### Mixed Reset: Undo Commit, Unstage Changes

```bash
# You committed but want to recommit differently
git reset HEAD~1
# Same as: git reset --mixed HEAD~1

# Effect:
# - Last commit is gone from history
# - Changes are still in your files
# - Changes are NOT staged (you can stage selectively)

# Use case: "I want to reorganize these changes into different commits"
```

#### Hard Reset: Undo Commit, Delete Changes

```bash
# You committed AI-generated code that's completely wrong
git reset --hard HEAD~1

# Effect:
# - Last commit is gone from history
# - Changes are DELETED from your files
# - You're back to the previous commit state

# Use case: "This commit was a mistake - delete everything"
```

**HEAD~1 explained:**
- `HEAD` = current commit
- `HEAD~1` = one commit before current
- `HEAD~2` = two commits before current
- You can also use commit hashes: `git reset --hard abc123`

### git revert: Safe Undo for Shared Code

**When to use:** You've pushed commits to GitHub and others might have pulled them.

`git revert` doesn't delete history—it creates a new commit that undoes a previous commit. This is safe because it doesn't rewrite history that others might have.

```bash
# You pushed a commit with a bug
git log
# commit abc123 "Add user profile feature" (buggy)
# commit def456 "Previous working state"

# Create a revert commit
git revert abc123

# Git opens an editor with message:
# "Revert 'Add user profile feature'"
# You can edit or keep default

# Effect:
# - New commit is created that undoes abc123
# - History is preserved (abc123 still visible)
# - Code state is back to before abc123
# - Safe to push to GitHub
```

### Which Undo Method Should You Use?

| Situation | Command | Safe to Use? |
|-----------|---------|--------------|
| Uncommitted changes you don't want | `git restore <file>` | ✅ Yes (but changes lost) |
| Last commit was wrong, haven't pushed | `git reset --hard HEAD~1` | ✅ Yes (local only) |
| Need to modify last commit | `git reset --soft HEAD~1` | ✅ Yes (local only) |
| Already pushed to GitHub | `git revert <commit>` | ✅ Yes (safe for shared) |
| Multiple people working on branch | `git revert <commit>` | ✅ Yes (safe for shared) |

**Golden rule:** If you've pushed to GitHub and others might have pulled, use `git revert`. If it's only local, `git reset` is fine.

### Undoing AI Changes: Complete Example

**Scenario**: Claude Code refactored your authentication module, but after testing, you realize it broke session handling.

```bash
# Current situation:
git log --oneline
# abc123 (HEAD) Refactor auth module with Claude Code
# def456 Checkpoint: working auth before refactoring
# 789abc Previous work

# Check what changed
git show abc123
# Shows all changes Claude Code made

# Option 1: Hard reset (if you haven't pushed)
git reset --hard def456
# You're now back to the checkpoint before AI refactoring

# Option 2: Revert (if you've pushed to GitHub)
git revert abc123
# Creates new commit that undoes the refactoring
# History preserved, safe for teammates
```

## Part IV: Merging Branches

### What Is Merging?

Merging combines changes from two branches. Usually, you merge a feature branch back into main after testing.

**The merge process:**

1. You're on `main` branch (destination)
2. You run `git merge feature-branch` (source)
3. Git combines changes from both branches
4. If successful, you have one unified history

### Basic Merge Workflow

```bash
# You've been working on a feature branch
git checkout feature/ai-generated-ui

# Make changes, test, commit
git add .
git commit -m "Add user dashboard UI

🤖 Generated with Claude Code"

# Ready to merge into main
git checkout main
git merge feature/ai-generated-ui

# Output (if successful):
# Updating def456..abc123
# Fast-forward
#  dashboard.py | 45 +++++++++++++++++++++++
#  1 file changed, 45 insertions(+)

# Clean up the feature branch
git branch -d feature/ai-generated-ui
```

### Fast-Forward vs. Three-Way Merge

Git uses two merge strategies:

#### Fast-Forward Merge

Happens when main hasn't changed since you created the branch.

```bash
# Timeline:
# main: A -- B
#             \
# feature:     C -- D

# After merge:
# main: A -- B -- C -- D

# Git just moves main forward - no merge commit needed
```

#### Three-Way Merge

Happens when both branches have new commits.

```bash
# Timeline:
# main:    A -- B -- E
#               \
# feature:       C -- D

# After merge:
# main: A -- B -- E -- M (merge commit)
#             \       /
# feature:     C -- D

# Git creates a merge commit (M) that combines both histories
```

### Merge Conflicts: What and Why

A **merge conflict** happens when Git can't automatically combine changes because both branches modified the same lines of code differently.

**Example scenario:**

```python
# On main branch, you changed:
def login(username, password):
    return authenticate(username, password)

# On feature branch, Claude Code changed:
def login(username, password):
    return async_authenticate(username, password)
```

When you try to merge, Git doesn't know which version to keep. You have to decide.

### Resolving Merge Conflicts

**Step 1: Attempt the merge**

```bash
git checkout main
git merge feature/async-login

# Output:
# Auto-merging auth.py
# CONFLICT (content): Merge conflict in auth.py
# Automatic merge failed; fix conflicts and then commit the result.
```

**Step 2: Check conflict status**

```bash
git status

# Output:
# On branch main
# You have unmerged paths.
#   (fix conflicts and run "git commit")
#
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
#         both modified:   auth.py
```

**Step 3: Open the conflicted file**

Git marks conflicts with special markers:

```python
def login(username, password):
<<<<<<< HEAD
    return authenticate(username, password)
=======
    return async_authenticate(username, password)
>>>>>>> feature/async-login
```

**Markers explained:**
- `<<<<<<< HEAD` - Start of your current branch version (main)
- `=======` - Separator between versions
- `>>>>>>> feature/async-login` - End of branch you're merging

**Step 4: Resolve the conflict**

Edit the file to keep what you want:

```python
# Option 1: Keep main version
def login(username, password):
    return authenticate(username, password)

# Option 2: Keep feature version
def login(username, password):
    return async_authenticate(username, password)

# Option 3: Combine both (if that makes sense)
def login(username, password):
    # TODO: Migrate fully to async in next sprint
    return authenticate(username, password)  # Keep sync for now
```

Delete the conflict markers completely.

**Step 5: Mark as resolved**

```bash
# After editing and saving
git add auth.py

# Check status
git status
# Output: All conflicts fixed but you are still merging.

# Complete the merge
git commit -m "Merge feature/async-login

Resolved conflicts in auth.py:
- Kept synchronous authenticate() for now
- Will migrate to async in separate sprint
- All tests passing

🤖 Generated with Claude Code"
```

### Conflict Prevention Strategies

Reduce conflicts by:

1. **Merge main into your branch frequently**
```bash
# While working on feature branch
git checkout feature/my-work
git merge main  # Pull in latest changes from main
# Resolve any conflicts early and often
```

2. **Keep branches short-lived**
- Create branch → Make changes → Merge → Delete branch
- Don't let branches live for weeks

3. **Coordinate with teammates**
- "I'm working on auth.py this week"
- Avoid editing the same files simultaneously

4. **Use small, focused commits**
- Easier to understand what changed
- Easier to resolve conflicts when they occur

### Asking AI to Help with Conflicts

When you encounter a merge conflict, you can ask Claude Code or Gemini CLI for help:

**Example prompt:**

```
I have a merge conflict in auth.py:

<<<<<<< HEAD
def login(username, password):
    return authenticate(username, password)
=======
def login(username, password):
    return async_authenticate(username, password)
>>>>>>> feature/async-login

The main branch uses synchronous authentication.
The feature branch uses async authentication.

What's the best way to resolve this?
Should I keep sync or migrate to async?
What are the implications?
```

Claude Code can explain the tradeoffs and suggest a resolution strategy. You make the final decision.

## Part V: Stashing - Temporary Saves

### What Is Git Stash?

**Stash** is a temporary storage area for uncommitted changes. Think of it as a clipboard for your code.

**When to use stash:**

1. **Context switching** - You're working on feature A, but need to quickly fix a bug on main
2. **Branch switching** - You want to switch branches but aren't ready to commit yet
3. **Experiment preservation** - You want to try something radical but save current work first

### Basic Stash Operations

**Save current work:**

```bash
# You have uncommitted changes
git status
# Modified: config.py, utils.py

# Stash them
git stash
# or with a descriptive message:
git stash push -m "WIP: refactoring config loader"

# Output: Saved working directory and index state

# Your working directory is now clean
git status
# Output: nothing to commit, working tree clean
```

**View stashed changes:**

```bash
git stash list

# Output:
# stash@{0}: On main: WIP: refactoring config loader
# stash@{1}: On feature: experimental UI changes
```

**Apply stashed changes:**

```bash
# Apply most recent stash
git stash pop
# Applies stash@{0} and removes it from stash list

# Or apply specific stash without removing
git stash apply stash@{1}
# Applies stash@{1} but keeps it in the list
```

**Delete stashed changes:**

```bash
# Delete specific stash
git stash drop stash@{0}

# Delete all stashes
git stash clear
```

### Real-World Stash Scenario

**Scenario**: You're refactoring a module with Claude Code, but a critical bug is reported that you need to fix immediately.

```bash
# Current situation: uncommitted refactoring work
git status
# Modified: payment_processor.py (half-refactored)

# Bug reported: production issue in login.py
# You need to fix it NOW on main branch

# 1. Stash your refactoring work
git stash push -m "WIP: payment processor refactoring with Claude Code"

# 2. Switch to main and create a bugfix branch
git checkout main
git checkout -b hotfix/login-bug

# 3. Fix the bug in login.py
git add login.py
git commit -m "Fix: session timeout bug in login

Critical fix for production issue.
Session timeout was not being reset on activity.

🤖 Generated with Claude Code"

# 4. Merge the fix
git checkout main
git merge hotfix/login-bug
git push origin main

# 5. Return to your refactoring work
git checkout feature/payment-refactor
git stash pop
# Your refactoring work is back, exactly as you left it
```

### Stash vs. Commit vs. Branch

| Situation | Use This | Why |
|-----------|----------|-----|
| Temporary save, will continue soon | `git stash` | Quick save for context switching |
| Work is incomplete but worth saving | `git commit` on branch | Creates permanent history |
| Experimenting with different approaches | Create new branch | Isolates experiments safely |

**General guideline:**
- Stash for temporary saves (hours)
- Commit for meaningful progress (even if incomplete)
- Branch for parallel explorations

## Practice Exercises

### Exercise 1: Checkpoint and Rollback

**Objective:** Practice creating checkpoints before AI changes and rolling back if needed.

**Steps:**

1. Create a simple Python file `calculator.py`:
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(add(5, 3))  # Should print 8
```

2. Initialize Git and create a checkpoint:
```bash
git init
git add calculator.py
git commit -m "Checkpoint: basic calculator working"
```

3. Ask Claude Code or manually modify the file to add multiplication and division (simulate AI changes):
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # Bug: doesn't handle division by zero

print(divide(10, 0))  # This will crash!
```

4. Test it and notice the bug.

5. Roll back to your checkpoint:
```bash
git reset --hard HEAD~1
```

6. Verify that calculator.py is back to the original version.

💡 **Learning with AI**: After completing this exercise, ask Claude Code:
- "Why is `git reset --hard` powerful but dangerous?"
- "What's the difference between `git reset --soft`, `git reset --mixed`, and `git reset --hard`?"

<details>
<summary>Show Answer</summary>

**Complete solution:**

```bash
# Step 1-2: Create file and checkpoint
echo 'def add(a, b): return a + b
def subtract(a, b): return a - b
print(add(5, 3))' > calculator.py

git init
git add calculator.py
git commit -m "Checkpoint: basic calculator working"

# Step 3: Make changes (simulate AI modification)
echo 'def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
print(divide(10, 0))' > calculator.py

# Step 4: Test (this will error)
python calculator.py  # ZeroDivisionError

# Step 5: Rollback
git reset --hard HEAD~1

# Step 6: Verify
cat calculator.py  # Back to original version
python calculator.py  # Works: prints 8
```

**Key lesson:** Checkpoints let you experiment fearlessly. If AI changes break things, rollback is instant.

</details>

---

### Exercise 2: Branch-Based Experimentation

**Objective:** Use branches to safely test AI-generated code without affecting your main codebase.

**Steps:**

1. Create a working Python script `greeter.py` on main:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```

2. Commit it:
```bash
git init
git add greeter.py
git commit -m "Initial greeter working"
```

3. Create an experiment branch:
```bash
git checkout -b experiment/multilingual
```

4. Modify greeter.py (simulate AI adding multilingual support):
```python
def greet(name, language="en"):
    greetings = {
        "en": f"Hello, {name}!",
        "es": f"¡Hola, {name}!",
        "fr": f"Bonjour, {name}!",
    }
    return greetings.get(language, greetings["en"])

print(greet("World", "es"))
```

5. Test it and commit:
```bash
python greeter.py  # Should print: ¡Hola, World!
git add greeter.py
git commit -m "Add multilingual support"
```

6. Switch back to main and verify it's unchanged:
```bash
git checkout main
cat greeter.py  # Should be original version
```

7. Merge the experiment:
```bash
git merge experiment/multilingual
```

8. Delete the experiment branch:
```bash
git branch -d experiment/multilingual
```

💡 **Learning with AI**: Ask Claude Code:
- "When should I use branches vs. just committing on main?"
- "What happens if I switch branches with uncommitted changes?"

⚠️ **Important**: Always test AI-generated code before merging to main!

<details>
<summary>Show Answer</summary>

**Key commands:**

```bash
# Create and switch to branch
git checkout -b experiment/multilingual

# Make changes, then commit
git add greeter.py
git commit -m "Add multilingual support"

# Switch back to main (unchanged)
git checkout main

# Merge experiment into main
git merge experiment/multilingual

# Clean up
git branch -d experiment/multilingual
```

**Result:** Main now has multilingual support, but you tested it safely on a branch first.

</details>

---

### Exercise 3: Resolving a Merge Conflict

**Objective:** Practice resolving merge conflicts that occur when both branches modify the same code.

**Steps:**

1. Create `config.py` on main:
```python
DEBUG = False
API_URL = "https://api.production.com"
```

2. Commit it:
```bash
git init
git add config.py
git commit -m "Initial config"
```

3. Create a feature branch and change API_URL:
```bash
git checkout -b feature/staging-config
```

4. Edit `config.py` on the feature branch:
```python
DEBUG = True
API_URL = "https://api.staging.com"
```

5. Commit:
```bash
git add config.py
git commit -m "Add staging config"
```

6. Switch back to main and make a DIFFERENT change to API_URL:
```bash
git checkout main
```

Edit `config.py`:
```python
DEBUG = False
API_URL = "https://api.newproduction.com"
```

7. Commit on main:
```bash
git add config.py
git commit -m "Update production API URL"
```

8. Try to merge the feature branch (this will conflict):
```bash
git merge feature/staging-config
# Output: CONFLICT (content): Merge conflict in config.py
```

9. Open `config.py` and you'll see:
```python
DEBUG = True
<<<<<<< HEAD
API_URL = "https://api.newproduction.com"
=======
API_URL = "https://api.staging.com"
>>>>>>> feature/staging-config
```

10. Resolve by choosing or combining:
```python
DEBUG = True
API_URL = "https://api.staging.com"  # Keep staging for this branch
```

11. Mark as resolved:
```bash
git add config.py
git commit -m "Merge feature/staging-config, resolved API_URL conflict"
```

💡 **Learning with AI**: Ask Claude Code:
- "I have a merge conflict in this file: [paste conflict]. What's the best way to resolve it?"
- "How can I avoid merge conflicts when working with a team?"

<details>
<summary>Show Answer</summary>

**Conflict resolution steps:**

1. When merge conflict occurs, Git marks the file with conflict markers
2. Open the file and find markers: `<<<<<<< HEAD`, `=======`, `>>>>>>>`
3. Decide which version to keep (or combine both)
4. Delete ALL conflict markers
5. Save the file
6. `git add <file>` to mark as resolved
7. `git commit` to complete the merge

**In this exercise:**
- Both branches changed `API_URL` differently
- You chose to keep the staging URL
- Conflict resolved, merge completed

</details>

---

### Exercise 4: Using Git Stash

**Objective:** Use stash to temporarily save work when switching contexts.

**Steps:**

1. Create `app.py` on main:
```python
def main():
    print("App version 1.0")

if __name__ == "__main__":
    main()
```

2. Commit it:
```bash
git init
git add app.py
git commit -m "Initial app"
```

3. Start refactoring (don't commit yet):
```python
def main():
    version = "2.0"
    print(f"App version {version}")
    # TODO: Add more features here

if __name__ == "__main__":
    main()
```

4. Urgent bug reported! You need to fix something else immediately.

5. Stash your refactoring work:
```bash
git stash push -m "WIP: refactoring version display"
```

6. Verify working directory is clean:
```bash
git status  # Should show: nothing to commit
cat app.py  # Should be back to version 1.0
```

7. Create a bugfix branch and fix the bug:
```bash
git checkout -b hotfix/typo
```

Edit app.py:
```python
def main():
    print("Application version 1.0")  # Fixed typo

if __name__ == "__main__":
    main()
```

8. Commit and merge:
```bash
git add app.py
git commit -m "Fix: correct typo in main message"
git checkout main
git merge hotfix/typo
```

9. Return to your refactoring work:
```bash
git stash pop
```

10. Continue working on your refactoring.

💡 **Learning with AI**: Ask Claude Code:
- "When should I use `git stash` vs. creating a commit?"
- "What happens if I stash changes and then modify the same file?"

<details>
<summary>Show Answer</summary>

**Key stash commands:**

```bash
# Save work temporarily
git stash push -m "descriptive message"

# List stashes
git stash list

# Apply most recent stash and remove it
git stash pop

# Apply specific stash without removing
git stash apply stash@{0}

# Delete stash
git stash drop stash@{0}
```

**Use cases:**
- Context switching (work on different task urgently)
- Branch switching (not ready to commit)
- Trying something radical (save current state first)

</details>

---

### Exercise 5: Complete Safe Experimentation Workflow

**Objective:** Combine checkpoints, branches, and rollback in a realistic AI development scenario.

**Scenario:** You have a working data processor. Claude Code offers to optimize it. You want to try it safely.

**Steps:**

1. Create `processor.py`:
```python
def process_data(data):
    result = []
    for item in data:
        result.append(item * 2)
    return result

data = [1, 2, 3, 4, 5]
print(process_data(data))  # [2, 4, 6, 8, 10]
```

2. Initialize and create checkpoint:
```bash
git init
git add processor.py
git commit -m "Checkpoint: data processor working"
```

3. Create an experiment branch:
```bash
git checkout -b experiment/optimize-processor
```

4. Simulate Claude Code optimization (use list comprehension):
```python
def process_data(data):
    return [item * 2 for item in data]

data = [1, 2, 3, 4, 5]
print(process_data(data))  # [2, 4, 6, 8, 10]
```

5. Test the optimized version:
```bash
python processor.py  # Should work correctly
```

6. Commit the optimization:
```bash
git add processor.py
git commit -m "Optimize process_data with list comprehension

Performance: More Pythonic and faster for large datasets

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

7. Switch back to main (unchanged):
```bash
git checkout main
python processor.py  # Still original version
```

8. Merge the optimization:
```bash
git merge experiment/optimize-processor
```

9. If you later realize the optimization broke something (simulate this):
```bash
# Rollback the merge
git reset --hard HEAD~1
```

10. Main is back to the checkpoint—safe and working.

💡 **Learning with AI**: Ask Claude Code:
- "Walk me through this workflow step by step and explain why each step matters."
- "What would happen if I skipped creating a branch and just edited on main?"

⚠️ **Important**: Try solving this yourself first! Use AI to understand, not to generate the answer.

<details>
<summary>Show Answer</summary>

**Complete workflow:**

```bash
# 1. Create file and checkpoint
git init
git add processor.py
git commit -m "Checkpoint: data processor working"

# 2. Create experiment branch
git checkout -b experiment/optimize-processor

# 3-5. Make changes, test, commit
# (edit processor.py with list comprehension)
python processor.py  # Test
git add processor.py
git commit -m "Optimize with list comprehension"

# 6. Switch back to main
git checkout main
# Main is unchanged

# 7. Merge if satisfied
git merge experiment/optimize-processor

# 8. If later you need to rollback
git reset --hard HEAD~1
# Back to checkpoint
```

**Why this workflow is powerful:**
- Main branch always stays working
- You can test AI changes in isolation
- Rollback is instant if something breaks
- You learn whether AI suggestions work without risk

</details>

---

### Exercise 6: Practicing Conflict Resolution with AI Help

**Objective:** Use AI to help understand and resolve a complex merge conflict.

**Steps:**

1. Create `auth.py` on main:
```python
def login(username, password):
    if username and password:
        return {"status": "success", "user": username}
    return {"status": "error", "message": "Invalid credentials"}
```

2. Commit:
```bash
git init
git add auth.py
git commit -m "Initial authentication"
```

3. Create branch and modify (simulate AI adding logging):
```bash
git checkout -b feature/add-logging
```

Edit `auth.py`:
```python
def login(username, password):
    print(f"Login attempt: {username}")  # Added logging
    if username and password:
        return {"status": "success", "user": username}
    return {"status": "error", "message": "Invalid credentials"}
```

4. Commit:
```bash
git add auth.py
git commit -m "Add login logging"
```

5. Switch to main and make DIFFERENT change (simulate teammate adding validation):
```bash
git checkout main
```

Edit `auth.py`:
```python
def login(username, password):
    if not username or not password:  # Added validation
        return {"status": "error", "message": "Username and password required"}
    if username and password:
        return {"status": "success", "user": username}
    return {"status": "error", "message": "Invalid credentials"}
```

6. Commit:
```bash
git add auth.py
git commit -m "Add input validation"
```

7. Try to merge (conflict will occur):
```bash
git merge feature/add-logging
# CONFLICT in auth.py
```

8. Open `auth.py` and examine the conflict:
```python
def login(username, password):
<<<<<<< HEAD
    if not username or not password:
        return {"status": "error", "message": "Username and password required"}
=======
    print(f"Login attempt: {username}")
>>>>>>> feature/add-logging
    if username and password:
        return {"status": "success", "user": username}
    return {"status": "error", "message": "Invalid credentials"}
```

9. Ask Claude Code for help:
```
I have a merge conflict. The main branch added input validation at the start of the function. The feature branch added logging. How should I combine both changes?
```

10. Resolve by combining both:
```python
def login(username, password):
    print(f"Login attempt: {username}")  # Logging from feature branch
    if not username or not password:  # Validation from main
        return {"status": "error", "message": "Username and password required"}
    if username and password:
        return {"status": "success", "user": username}
    return {"status": "error", "message": "Invalid credentials"}
```

11. Complete the merge:
```bash
git add auth.py
git commit -m "Merge feature/add-logging

Combined changes:
- Logging from feature branch
- Validation from main branch
Both features work together"
```

💡 **Learning with AI**: After resolving, ask:
- "Is there a better way to structure this function now that it has both logging and validation?"
- "Could this conflict have been avoided with better coordination?"

<details>
<summary>Show Answer</summary>

**Conflict resolution strategy:**

When both branches modify the same function:

1. **Understand both changes:**
   - Main added validation (checking for empty inputs)
   - Feature added logging (printing login attempts)

2. **Combine both logically:**
   - Keep logging first (good to log all attempts)
   - Then do validation (reject invalid inputs)
   - Then proceed with authentication

3. **Test the combined result:**
   ```python
   print(login("", ""))  # Should log and return validation error
   print(login("user", "pass"))  # Should log and return success
   ```

**AI can help by:**
- Explaining what each change does
- Suggesting the logical order
- Identifying potential bugs in your resolution
- Recommending improvements to the combined code

</details>

---

## Self-Assessment

Test your understanding with these questions:

1. **When should you create a checkpoint commit?**
   - A) Only when you finish a complete feature
   - B) Before asking AI to modify your code
   - C) Once a week
   - D) Only when pushing to GitHub

2. **What does `git reset --hard HEAD~1` do?**
   - A) Undoes the last commit and keeps the changes in your files
   - B) Undoes the last commit and deletes the changes completely
   - C) Creates a new branch
   - D) Pushes changes to GitHub

3. **What is the main benefit of using branches for AI-generated code?**
   - A) It makes your code run faster
   - B) It isolates experiments so main branch stays working
   - C) It automatically fixes bugs
   - D) It creates backups of your code

4. **When you have a merge conflict, Git marks it with:**
   - A) `### CONFLICT ###`
   - B) `<<<<<<< HEAD` and `>>>>>>>`
   - C) `[CONFLICT]` and `[END]`
   - D) Git automatically resolves conflicts

5. **What's the difference between `git reset` and `git revert`?**
   - A) There is no difference
   - B) `reset` rewrites history (dangerous if pushed), `revert` creates new commit (safe)
   - C) `reset` is faster
   - D) `revert` only works on branches

6. **When should you use `git stash`?**
   - A) To permanently delete changes
   - B) To temporarily save uncommitted work while switching contexts
   - C) To create a new branch
   - D) To merge branches

7. **What happens to your working directory after `git stash`?**
   - A) All files are deleted
   - B) Changes are committed automatically
   - C) Working directory becomes clean (changes hidden in stash)
   - D) Nothing changes

8. **Which undo command is safest for code already pushed to GitHub?**
   - A) `git reset --hard`
   - B) `git revert`
   - C) `git restore`
   - D) Delete the file and recommit

9. **What does the asterisk (*) mean in `git branch` output?**
   - A) The branch has conflicts
   - B) The branch is behind main
   - C) The current branch you're on
   - D) The branch is ready to delete

10. **After resolving a merge conflict, what must you do?**
    - A) Delete one of the branches
    - B) Run `git reset`
    - C) `git add` the resolved file and `git commit`
    - D) Push immediately to GitHub

<details>
<summary>Show Answers</summary>

1. **B** - Before asking AI to modify your code (checkpoint pattern creates safety net)
2. **B** - Undoes last commit and deletes changes completely (use with caution!)
3. **B** - Isolates experiments so main branch stays working (key safety principle)
4. **B** - `<<<<<<< HEAD` and `>>>>>>>` (standard Git conflict markers)
5. **B** - `reset` rewrites history (dangerous if pushed), `revert` creates new commit (safe)
6. **B** - Temporarily save uncommitted work while switching contexts
7. **C** - Working directory becomes clean (changes hidden in stash, can be restored later)
8. **B** - `git revert` (creates new commit, doesn't rewrite shared history)
9. **C** - The current branch you're on
10. **C** - `git add` the resolved file and `git commit` (completes the merge)

**Scoring:**
- 9-10: Excellent! You understand Git safety patterns
- 7-8: Good! Review merge conflicts and reset vs. revert
- 5-6: Needs work - practice the exercises again
- Below 5: Review this lesson thoroughly before continuing

</details>

---

## Reflection and Forward Bridge

### Pause and Reflect

Before moving forward, consider these questions:

**Reflection 1: How does the checkpoint pattern change your mindset about AI-generated code?**

Without checkpoints, AI suggestions feel risky—what if they break something? With checkpoints, AI becomes a collaborative partner. You can try anything, knowing you can always return to a working state.

**Reflection 2: Think about a time you've been afraid to change code because you might break something. How would branches have helped?**

Branches create parallel realities. You can experiment wildly on a branch while main stays safe. If your experiment works, you merge it. If it fails, you delete the branch. Main never knew it happened.

**Reflection 3: When would you choose `git revert` over `git reset`?**

If you've pushed changes to GitHub and others might have pulled them, always use `git revert`. It preserves history and creates a new commit that undoes the problematic change. `git reset` rewrites history, which breaks things for collaborators.

---

## What You've Mastered

You now have the essential Git safety skills for AI-driven development:

✅ **Checkpoint pattern** - Always create safe restore points before AI changes
✅ **Branch-based experimentation** - Isolate AI work from stable code
✅ **Rollback strategies** - Undo mistakes quickly and safely
✅ **Merge conflicts** - Resolve when two branches change the same code
✅ **Stashing** - Temporarily save work when context switching

These aren't just Git commands—they're a **safety mindset**. With these tools, you can:
- Let AI modify your code without fear
- Experiment boldly, knowing rollback is instant
- Keep your main codebase stable while testing radical ideas

---

## What's Next

**Next lesson (Lesson 4):** You'll learn how to **collaborate with teammates** using GitHub pull requests. You'll share AI-generated code for review, provide feedback on others' code, and merge safely after approval.

The skills from this lesson (branches, merging, conflict resolution) are the foundation for team collaboration. Everything you learned here applies directly to pull request workflows.

You're building a **complete safety system** for AI-assisted development:
- Lesson 3 (this lesson) = Personal safety (checkpoints, branches, rollback)
- Lesson 4 (next) = Team safety (pull requests, code review)
- Lesson 5 (final) = Convenience (natural language prompts)

Let's continue building your Git mastery.
