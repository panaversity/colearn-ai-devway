---
title: "Common Scenarios Reference: Git for AI Development"
sidebar_position: 8
description: "Real-world scenarios you'll encounter when doing AI-driven development with Git, with step-by-step solutions."
---

# Common Scenarios Reference: Git for AI Development

**Practical solutions to common Git situations in AI-assisted development workflows.**

These scenarios reflect real challenges developers face when working with AI tools like Claude Code and Gemini CLI. Each includes context, problem, solution, and explanation.

---

## Scenario 1: "AI Broke My Code—How Do I Undo?"

### Context

You asked Claude Code to refactor your authentication module. The AI made extensive changes across 3 files. You tested the code, and it's completely broken. The original code worked fine.

### Problem

You need to revert to the working version immediately, but you're not sure how to undo AI changes without losing other work.

### Solution

**If you created a checkpoint commit before the AI session (recommended):**

```bash
# Check your recent commits
git log --oneline -n 5

# Output:
# abc123 (HEAD) Refactor authentication with Claude Code
# def456 Checkpoint: working auth before refactoring
# 789abc Previous work

# Reset to the checkpoint
git reset --hard def456

# Verify you're back to working code
# Test your application
```

**If you didn't create a checkpoint but the changes are uncommitted:**

```bash
# Discard all uncommitted changes
git restore .

# Verify
git status
# Should show: "nothing to commit, working tree clean"
```

**If you committed the broken code but haven't pushed:**

```bash
# Undo the last commit, discard changes
git reset --hard HEAD~1

# Your code is now back to before the AI changes
```

**If you already pushed to GitHub:**

```bash
# Create a revert commit (safe for shared code)
git revert abc123

# This creates a new commit that undoes the AI changes
# Push the revert
git push origin main
```

### Why This Works

- **Checkpoint commits** create safe restore points before risky changes
- **`git reset --hard`** is fast but destructive (use only if not pushed)
- **`git revert`** is safe for shared code (doesn't rewrite history)

### Prevention

**Always before AI sessions:**
```bash
git add .
git commit -m "Checkpoint: working state before Claude Code refactoring"
```

---

## Scenario 2: "I Want to Try Multiple AI Approaches"

### Context

You're building a data processing feature. You want Claude Code to try two different approaches:
1. Using pandas for data manipulation
2. Using NumPy for performance

You want to compare both before deciding which to keep.

### Problem

How do you test multiple AI solutions without mixing code or losing work?

### Solution

**Use branches to isolate experiments:**

```bash
# Ensure you're starting from a clean state
git checkout main
git pull origin main

# Create first experiment branch
git checkout -b experiment/pandas-approach

# Ask Claude Code: "Implement data processing using pandas"
# [AI generates code]
# Test it, measure performance

# Commit the pandas approach
git add .
git commit -m "Experiment: data processing with pandas

Performance: 2.3 seconds for 10K rows

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Switch back to main (unchanged)
git checkout main

# Create second experiment branch
git checkout -b experiment/numpy-approach

# Ask Claude Code: "Implement data processing using NumPy"
# [AI generates code]
# Test it, measure performance

# Commit the numpy approach
git add .
git commit -m "Experiment: data processing with NumPy

Performance: 0.8 seconds for 10K rows (3x faster!)

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Now compare the two approaches
git checkout experiment/pandas-approach
# Test pandas version, note results

git checkout experiment/numpy-approach
# Test numpy version, note results

# Decision: NumPy is faster, keep that one
git checkout main
git merge experiment/numpy-approach

# Clean up
git branch -d experiment/pandas-approach
git branch -d experiment/numpy-approach
```

### Why This Works

- Each branch is an **isolated experiment**
- You can switch between them to compare
- Main branch stays unchanged during experimentation
- You only merge the winner

### Variation: Keep Both

If you want to keep both approaches:

```bash
# Keep pandas in a feature branch for smaller datasets
git checkout experiment/pandas-approach
git checkout -b feature/pandas-processor

# Keep numpy in main for large datasets
git checkout main
git merge experiment/numpy-approach

# Now you have both options available
```

---

## Scenario 3: "My Teammate Changed the Same File"

### Context

You and your teammate are both working on `user_profile.py`. They finished their feature and merged it to main. Now you're trying to push your feature branch, but Git says there's a conflict.

### Problem

Both branches modified the same lines in `user_profile.py`. Git can't automatically merge them.

### Solution

**Step 1: Update your branch with main**

```bash
# Make sure your changes are committed
git status
# If uncommitted changes, commit them first

# Switch to main and pull latest
git checkout main
git pull origin main

# Switch back to your feature branch
git checkout feature/profile-editing

# Merge main into your branch
git merge main

# Output:
# Auto-merging user_profile.py
# CONFLICT (content): Merge conflict in user_profile.py
# Automatic merge failed; fix conflicts and then commit the result.
```

**Step 2: Open the conflicted file**

```python
# user_profile.py
class UserProfile:
    def save(self):
<<<<<<< HEAD (your changes)
        # Your feature: add validation
        if not self.validate():
            raise ValueError("Invalid profile data")
        self.db.save(self)
=======
        # Teammate's feature: add logging
        print(f"Saving profile: {self.username}")
        self.db.save(self)
>>>>>>> main
```

**Step 3: Resolve the conflict**

Choose one approach or **combine both** (often the best solution):

```python
# user_profile.py
class UserProfile:
    def save(self):
        # Combined: validation AND logging
        print(f"Saving profile: {self.username}")  # Teammate's feature
        if not self.validate():  # Your feature
            raise ValueError("Invalid profile data")
        self.db.save(self)
```

**Delete all conflict markers** (`<<<<<<<`, `=======`, `>>>>>>>`).

**Step 4: Mark as resolved**

```bash
# Stage the resolved file
git add user_profile.py

# Check status
git status
# Should show: "All conflicts fixed but you are still merging"

# Complete the merge
git commit -m "Merge main into feature/profile-editing

Resolved conflict in user_profile.py:
- Combined teammate's logging feature with my validation
- Both features now work together

Tested: validation still works, logging confirmed"

# Push your updated branch
git push origin feature/profile-editing
```

**Step 5: Create or update your pull request**

Your PR now includes your feature **plus** your teammate's feature, with conflicts resolved.

### Why This Works

- Merging main into your feature branch **updates your branch** with teammate's work
- You resolve conflicts on your branch (main stays clean)
- After resolving, your branch is ready to merge into main without conflicts

### Prevention

**Reduce conflicts by:**
1. **Coordinating with teammates** - "I'm working on user_profile.py this week"
2. **Merging main frequently** - Don't let your branch get stale
3. **Keeping PRs small** - Smaller changes = fewer conflicts

---

## Scenario 4: "I Committed Secrets to GitHub"

### Context

You were developing a feature that uses an API key. In a rush, you hardcoded the API key in `config.py` and committed it. You pushed to GitHub. An hour later, you realized: **my API key is now in the public repository history!**

### Problem

Even if you remove the key and commit again, it's still in Git history. Anyone can see it. Attackers scan GitHub for exposed secrets.

### Solution

**Step 1: Rotate the secret immediately**

```bash
# Before fixing Git, rotate the compromised secret
# Go to your API provider's website
# Generate a new API key
# Invalidate the old key
```

**This is critical:** The exposed key is compromised forever. Fixing Git doesn't make the old key safe.

**Step 2: Remove the secret from your code**

```python
# config.py - BEFORE (bad)
API_KEY = "sk-1234567890abcdef"  # ❌ Hardcoded

# config.py - AFTER (good)
import os
API_KEY = os.environ.get("API_KEY")  # ✅ From environment variable
```

**Step 3: Add to .gitignore**

```bash
# .gitignore
.env
*.secret
config.local.py
```

**Step 4: Commit the fix**

```bash
git add config.py .gitignore
git commit -m "Remove hardcoded API key, use environment variable

Security fix:
- Remove exposed API key from code
- Load from environment variable
- Add .env to .gitignore

Note: API key has been rotated (old key invalidated)"
```

**Step 5: Remove from Git history (advanced)**

The secret is still in history. To remove it completely:

**Option A: Using BFG Repo-Cleaner (recommended)**

```bash
# Install BFG: https://rtyley.github.io/bfg-repo-cleaner/

# Clone a fresh copy
git clone --mirror https://github.com/username/repo.git

# Remove the secret
bfg --replace-text passwords.txt repo.git

# Push the cleaned history
cd repo.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

**Option B: Using git-filter-repo**

```bash
# Install git-filter-repo
pip install git-filter-repo

# Create a fresh clone
git clone https://github.com/username/repo.git
cd repo

# Remove the file from all history
git filter-repo --path config.py --invert-paths

# Force push
git push --force origin main
```

**⚠️ Warning:** Force pushing rewrites history. Coordinate with your team first!

### Why This Happened

Common causes:
- Rushing and forgetting to use environment variables
- Not reviewing `git diff` before committing
- No pre-commit hooks to scan for secrets

### Prevention

**1. Use environment variables:**
```python
import os
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")
```

**2. Use a .env file:**
```bash
# .env (add to .gitignore)
API_KEY=sk-1234567890abcdef
DATABASE_URL=postgresql://localhost/mydb
```

**3. Install a pre-commit hook:**
```bash
# Install detect-secrets
pip install detect-secrets

# Scan your repo
detect-secrets scan

# Add as pre-commit hook
```

**4. Review before committing:**
```bash
git diff  # Check what you're about to commit
git add config.py
git diff --staged  # Review staged changes
git commit -m "message"
```

---

## Scenario 5: "I Need to Move Commits to a Different Branch"

### Context

You started working on a feature and made 3 commits. But you accidentally made them on `main` instead of creating a feature branch first. Now `main` has unreleased code.

### Problem

You need to move the 3 commits to a feature branch and reset `main` back to its clean state.

### Solution

**Step 1: Create a feature branch (preserve the commits)**

```bash
# You're on main with 3 unwanted commits
git log --oneline -n 5

# Output:
# abc123 (HEAD -> main) Commit 3
# def456 Commit 2
# ghi789 Commit 1
# jkl012 Last good commit on main

# Create a feature branch from current position
git checkout -b feature/accidentally-on-main

# Now feature/accidentally-on-main has all 3 commits
```

**Step 2: Reset main to before the commits**

```bash
# Switch back to main
git checkout main

# Reset to before the 3 commits
git reset --hard jkl012

# Verify
git log --oneline -n 3
# Should NOT show the 3 commits anymore
```

**Step 3: Verify both branches**

```bash
# Check main (should be clean)
git checkout main
git log --oneline -n 3

# Check feature branch (should have the 3 commits)
git checkout feature/accidentally-on-main
git log --oneline -n 5
```

**Step 4: Push the feature branch**

```bash
git push -u origin feature/accidentally-on-main
```

**Step 5: If you already pushed main**

If you already pushed the wrong commits to GitHub:

```bash
# Option 1: Force push (if working alone)
git checkout main
git reset --hard jkl012
git push --force-with-lease origin main

# Option 2: Revert the commits (if others pulled them)
git revert abc123 def456 ghi789
git push origin main
```

### Why This Works

- Creating a new branch **preserves** commits
- Resetting main **removes** commits from that branch
- Both branches now have the correct commits

### Prevention

**Always create a feature branch before starting new work:**

```bash
# Good workflow
git checkout main
git pull origin main
git checkout -b feature/new-work
# Now you're safe to commit
```

---

## Scenario 6: "Claude Code Suggested Changes, But I Want to Review First"

### Context

You asked Claude Code to optimize a complex function. It generated 150 lines of refactored code. Before committing, you want to review what actually changed.

### Problem

The code is long and complex. How do you efficiently review AI changes before committing?

### Solution

**Step 1: Stage the AI-generated changes**

```bash
git add optimized_function.py
```

**Step 2: View the diff**

```bash
# See what changed
git diff --staged

# Output shows:
# - Red lines (deleted/old code)
# - Green lines (added/new code)
```

**Step 3: Review section by section**

Ask Claude Code to explain changes:

```
You: "Show me what changed in the optimize_query() function"

Claude Code: [Shows specific diff]

You: "Why did you change the for loop to a list comprehension?"

Claude Code: "List comprehensions are more efficient in Python..."

You: "What about the caching logic? Why add @lru_cache?"

Claude Code: "This prevents redundant calculations..."
```

**Step 4: Test the changes**

```bash
# Run your tests
pytest tests/test_optimized_function.py

# Or test manually
python -c "from optimized_function import optimize_query; print(optimize_query(data))"
```

**Step 5: Commit only if satisfied**

```bash
# If everything looks good
git commit -m "Optimize query processing function

Changes by Claude Code:
- Convert loops to list comprehensions (20% faster)
- Add LRU caching for repeated queries (50% faster on cache hits)
- Simplified nested conditionals for readability
- Updated docstrings

Performance test results:
- Before: 250ms average
- After: 125ms average (50% improvement)

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# If not satisfied, discard changes
git restore --staged optimized_function.py
git restore optimized_function.py
```

### Why This Works

- **`git diff --staged`** shows exactly what you're about to commit
- You can ask AI to explain specific changes
- Testing before committing prevents broken code
- You can discard changes without consequences

### Best Practice

**Always review AI changes before committing:**

1. **Read the diff** - Don't blindly commit
2. **Ask "why"** - Understand the reasoning
3. **Test thoroughly** - Verify functionality
4. **Commit with context** - Explain what changed and why

---

## Scenario 7: "I Started Multiple Features and Lost Track"

### Context

You've been working for a few days and created multiple branches:
- `feature/user-auth`
- `experiment/new-ui`
- `fix/login-bug`
- `feature/dashboard`

Some have uncommitted changes. Some are finished. You're not sure which is which.

### Problem

You're overwhelmed and need to organize your work.

### Solution

**Step 1: Survey all branches**

```bash
# List all local branches
git branch

# See which branch has uncommitted changes
git status

# Check each branch
for branch in $(git branch | grep -v "main"); do
  echo "=== Branch: $branch ==="
  git checkout $branch
  git status
  echo ""
done
```

**Or use AI:**

```
You: "Help me check the status of all my feature branches and tell me which ones have uncommitted changes"

Claude Code: [Runs checks and summarizes]
```

**Step 2: Categorize branches**

| Branch | Status | Action |
|--------|--------|--------|
| `feature/user-auth` | Complete, pushed, PR merged | **Delete** |
| `experiment/new-ui` | Has uncommitted changes, not ready | **Commit or stash** |
| `fix/login-bug` | Complete, pushed, PR open | **Wait for review** |
| `feature/dashboard` | In progress, committed | **Continue work** |

**Step 3: Clean up finished branches**

```bash
# Delete merged branches
git checkout main
git branch -d feature/user-auth

# Delete experiment you don't want
git branch -D experiment/new-ui
```

**Step 4: Commit or stash unfinished work**

```bash
git checkout experiment/new-ui

# Option A: Commit the work in progress
git add .
git commit -m "WIP: experimental UI changes (not ready for review)"

# Option B: Stash for later
git stash push -m "Experimental UI work, not yet ready"
```

**Step 5: Create a tracking system**

```bash
# Create a simple status file
cat > BRANCH_STATUS.md << EOF
# Branch Status

## Active Work
- feature/dashboard (in progress, 60% done)
- fix/login-bug (PR #45 open, waiting for review)

## Paused
- experiment/new-ui (stashed, will resume after dashboard)

## Completed
- feature/user-auth (merged in PR #42)

Last updated: 2025-01-15
EOF

git add BRANCH_STATUS.md
git commit -m "Add branch status tracking"
```

### Why This Happens

- Working on too many things at once
- Not cleaning up merged branches
- Not committing or stashing work before switching branches

### Prevention

**1. Work on fewer branches simultaneously**
- Finish and merge one feature before starting another

**2. Clean up regularly**
```bash
# Weekly cleanup
git checkout main
git pull origin main
git branch --merged | grep -v "main" | xargs git branch -d
```

**3. Use descriptive branch names with dates**
```bash
git checkout -b feature/user-auth-2025-01-15
```

**4. Commit or stash before switching**
```bash
# Never switch branches with uncommitted changes
git status  # Check first
git stash   # If not ready to commit
git checkout other-branch
```

---

## Scenario 8: "I Want to See What AI Changed Over Time"

### Context

Over the past month, you've built a project with heavy AI assistance. Claude Code helped with:
- Initial structure (Week 1)
- Database integration (Week 2)
- API endpoints (Week 3)
- Frontend components (Week 4)

You want to review AI contributions and see how the project evolved.

### Problem

How do you trace AI contributions across many commits?

### Solution

**Step 1: Search commit messages for AI attribution**

```bash
# Find all commits with Claude Code attribution
git log --oneline --grep="Claude Code"

# Output:
# abc123 Add user authentication (Claude Code)
# def456 Refactor database queries (Claude Code)
# ghi789 Add API endpoints (Claude Code)
```

**Step 2: View AI contributions by week**

```bash
# Week 1 (Jan 1-7)
git log --oneline --since="2025-01-01" --until="2025-01-07" --grep="Claude Code"

# Week 2 (Jan 8-14)
git log --oneline --since="2025-01-08" --until="2025-01-14" --grep="Claude Code"
```

**Step 3: See what AI changed in specific files**

```bash
# Find commits that modified auth.py with AI help
git log --oneline --grep="Claude Code" -- auth.py

# View the actual changes
git show <commit-hash>
```

**Step 4: Use git blame to see AI contributions by line**

```bash
# See who (human or AI) wrote each line
git blame auth.py

# Look for commits with "Claude Code" in the message
# Those lines were AI-generated
```

**Step 5: Generate an AI contribution report**

```bash
# Count AI commits
git log --oneline --grep="Claude Code" | wc -l

# List AI-touched files
git log --name-only --grep="Claude Code" | grep -v "^$" | sort | uniq

# Generate summary report
echo "=== AI Contribution Report ===" > ai_report.txt
echo "Total commits: $(git log --oneline | wc -l)" >> ai_report.txt
echo "AI-assisted commits: $(git log --oneline --grep='Claude Code' | wc -l)" >> ai_report.txt
echo "" >> ai_report.txt
echo "Files modified by AI:" >> ai_report.txt
git log --name-only --grep="Claude Code" | grep -v "^$" | sort | uniq >> ai_report.txt
```

**Or use AI for analysis:**

```
You: "Analyze my Git history and tell me which features were built with Claude Code assistance"

Claude Code: [Scans commit messages and provides summary]
```

### Why This Works

- **AI attribution** in commit messages makes contributions traceable
- Git's search tools (`--grep`, `blame`, `log`) work with any text in commits
- You can generate reports showing AI impact

### Best Practice

**Always attribute AI contributions in commits:**

```bash
git commit -m "Add user authentication

Implemented JWT token generation and validation.

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

This makes it easy to:
- Track AI contributions over time
- Understand which code was AI-generated vs. human-written
- Generate reports for audits or stakeholders
- Learn from AI suggestions by reviewing them later

---

## Quick Scenario Lookup

| Scenario | Quick Solution |
|----------|----------------|
| **AI broke code** | `git reset --hard HEAD~1` (if not pushed) |
| **Try multiple AI approaches** | Use branches for each experiment |
| **Merge conflict** | Merge main into feature branch, resolve, commit |
| **Committed secret** | Rotate key, use env var, use BFG to clean history |
| **Wrong branch** | Create new branch, reset old branch |
| **Review AI changes** | `git diff --staged`, test, then commit |
| **Too many branches** | Survey, categorize, clean up merged branches |
| **Track AI contributions** | `git log --grep="Claude Code"` |

---

## Remember

✅ **Checkpoint before AI sessions** - Always create a restore point
✅ **Use branches for experiments** - Keep main stable
✅ **Review before committing** - Don't trust AI blindly
✅ **Attribute AI contributions** - Make them traceable
✅ **Clean up regularly** - Delete merged branches
✅ **Communicate with team** - Coordinate on shared files
✅ **Ask AI for help** - Use natural language to solve Git problems

**Git + AI = Safe, fast, fearless development. You've got this!**
