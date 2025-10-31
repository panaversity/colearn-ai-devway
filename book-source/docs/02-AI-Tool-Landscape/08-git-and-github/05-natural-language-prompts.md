---
title: "Lesson 5: Natural Language Prompts for Git Operations"
sidebar_position: 5
description: "Learn how to use Claude Code and Gemini CLI to execute Git commands via natural language, turning Git into a conversational interface."
---

# Lesson 5: Natural Language Prompts for Git Operations

## The Conversation That Changed Everything

It's Monday morning. Your teammate Sarah is reviewing her weekend side project. She made 12 commits over two days—some good, some messy, some that say "WIP" or "fix typo." She wants to clean up the commit history before creating a pull request.

The traditional approach requires knowing:
- `git log --oneline -n 12` (view commits)
- `git rebase -i HEAD~12` (interactive rebase)
- Understanding rebase commands: `pick`, `squash`, `fixup`, `reword`
- Resolving any conflicts that arise during rebase
- Force pushing safely: `git push --force-with-lease`

Sarah knows *what* she wants (clean commit history), but she doesn't remember *how* to do interactive rebasing. She hasn't done it in months.

So she asks Claude Code:

> "I have 12 commits on this branch. Many of them are small fixes and typos. Can you help me squash them into 3 logical commits: one for the feature implementation, one for tests, and one for documentation?"

Claude Code responds:

> "I'll help you clean up those commits. Let me check the history first and then guide you through squashing them into the 3 groups you mentioned."

Three minutes later, Sarah has a clean commit history. She created a pull request. Her teammate reviewed it and said, "This is the cleanest PR history I've seen all month."

**What just happened?**

Sarah used **natural language prompts** to execute complex Git operations. She didn't need to memorize `git rebase` syntax. She didn't need to remember the difference between `squash` and `fixup`. She told an AI tool *what* she wanted, and it handled *how* to do it.

This is the future of Git: **understanding concepts, not memorizing commands**. You know *what* Git does and *why* it matters (Lessons 1-4). Now you'll learn to use AI as a convenience layer that translates your intent into Git commands.

## Part I: Why Natural Language Prompts

### Understanding vs. Memorization

Traditional Git learning focuses on memorization:
- "To undo the last commit: `git reset --soft HEAD~1`"
- "To squash commits: `git rebase -i HEAD~n`"
- "To see who modified a line: `git blame <file>`"

**The problem:** Git has hundreds of commands with thousands of flag combinations. Even experienced developers forget syntax and Google commands regularly.

**The solution:** Use AI tools that understand *intent* and translate it into *commands*.

You still need to understand:
- ✅ What a commit is (Lesson 2)
- ✅ Why branches matter (Lesson 3)
- ✅ How pull requests work (Lesson 4)
- ✅ When to merge vs. rebase vs. revert

But you don't need to memorize:
- ❌ The exact syntax of `git rebase -i --autosquash`
- ❌ All 30+ flags for `git log`
- ❌ The difference between `git reset --soft`, `--mixed`, and `--hard`

AI tools handle syntax. You handle strategy.

### AI as a Git Translator

Think of Claude Code and Gemini CLI as translators:

**You speak:** "Show me commits from the last week"

**AI translates:** `git log --since="1 week ago" --oneline`

**You speak:** "Create a branch called 'feature-auth' from main"

**AI translates:**
```bash
git checkout main
git pull origin main
git checkout -b feature-auth
```

**You speak:** "Undo my last commit but keep the changes"

**AI translates:** `git reset --soft HEAD~1`

You provide **intent**. AI provides **implementation**.

### When to Use Natural Language Prompts

✅ **Use prompts when:**
- You know what you want but forget the syntax
- The operation is complex (interactive rebase, cherry-picking)
- You're exploring ("Show me all commits that touched auth.py")
- You want to understand output ("What does this error mean?")
- You need to learn ("How do I...?")

❌ **Don't rely solely on prompts when:**
- You don't understand what you're asking for (learn concepts first)
- The operation is critical and you should understand it (merging, force pushing)
- You're just being lazy about learning basic commands (balance is important)

### The Balance: Understanding + Convenience

**The ideal workflow:**

1. **Understand** Git concepts (Lessons 1-4): commits, branches, merging, pull requests
2. **Use** AI prompts for syntax and complex operations (Lesson 5)
3. **Review** what AI executes (don't blindly run commands)
4. **Learn** from AI's commands (build your Git knowledge over time)

**Example of healthy AI usage:**

```
You: "I want to undo my last commit but keep the changes in my working directory."

Claude Code: "I'll use `git reset --soft HEAD~1` to undo the commit while keeping your changes staged."

[Command runs successfully]

You: "Why --soft instead of --hard?"

Claude Code: "--soft preserves your changes in staging area. --hard would delete them completely. --mixed (default) would preserve changes but unstage them."

You: "Got it. So --soft is safest when I just want to modify the commit."

Claude Code: "Exactly. You can now re-commit with changes or make additional edits."
```

You learned something. You accomplished your goal. You used AI as a teacher, not just a tool.

## Part II: Command-to-Prompt Translation

### Basic Operations

Here are 10+ essential Git commands and their natural language equivalents:

#### 1. Check Repository Status

**Command:**
```bash
git status
```

**Natural language prompt:**
```
"Show me the current status of my repository"
or
"What files have I changed?"
or
"Is my working directory clean?"
```

**What AI does:** Runs `git status` and explains the output in plain English.

---

#### 2. View Commit History

**Command:**
```bash
git log --oneline --graph --all -n 20
```

**Natural language prompt:**
```
"Show me the last 20 commits in a visual tree"
or
"Show commit history for this branch"
or
"What commits were made today?"
```

**What AI does:** Chooses appropriate `git log` flags based on your intent.

---

#### 3. Create and Switch to Branch

**Command:**
```bash
git checkout -b feature/new-feature
```

**Natural language prompt:**
```
"Create a new branch called feature/new-feature and switch to it"
or
"Start a new feature branch for user authentication"
```

**What AI does:** Creates branch with appropriate naming conventions.

---

#### 4. Stage and Commit Changes

**Command:**
```bash
git add .
git commit -m "Add user authentication"
```

**Natural language prompt:**
```
"Commit all my changes with message 'Add user authentication'"
or
"Save my current work with a commit"
```

**What AI does:** Stages files and creates commit with proper message format.

---

#### 5. Push Branch to GitHub

**Command:**
```bash
git push -u origin feature/new-feature
```

**Natural language prompt:**
```
"Push my feature branch to GitHub"
or
"Upload this branch to the remote repository"
```

**What AI does:** Pushes with `-u` flag to set upstream tracking.

---

#### 6. Update Local Main Branch

**Command:**
```bash
git checkout main
git pull origin main
```

**Natural language prompt:**
```
"Update my main branch with the latest changes from GitHub"
or
"Sync my local main with remote"
```

**What AI does:** Switches to main, pulls latest changes.

---

#### 7. Merge Branch into Main

**Command:**
```bash
git checkout main
git merge feature/new-feature
```

**Natural language prompt:**
```
"Merge my feature branch into main"
or
"Combine feature/new-feature with main"
```

**What AI does:** Ensures you're on main, runs merge, handles fast-forward.

---

#### 8. Undo Last Commit (Keep Changes)

**Command:**
```bash
git reset --soft HEAD~1
```

**Natural language prompt:**
```
"Undo my last commit but keep the changes"
or
"I want to modify my last commit"
```

**What AI does:** Uses `--soft` to preserve changes in staging area.

---

#### 9. Discard Uncommitted Changes

**Command:**
```bash
git restore .
```

**Natural language prompt:**
```
"Discard all my uncommitted changes"
or
"Reset my working directory to the last commit"
```

**What AI does:** Uses `git restore` or `git checkout` to discard changes.

---

#### 10. View File History

**Command:**
```bash
git log --follow -- path/to/file.py
```

**Natural language prompt:**
```
"Show me the commit history for auth.py"
or
"Who changed this file and when?"
```

**What AI does:** Shows file-specific history, follows renames.

---

#### 11. See Who Modified Each Line

**Command:**
```bash
git blame auth.py
```

**Natural language prompt:**
```
"Show me who last modified each line in auth.py"
or
"I want to see the authorship history of this file"
```

**What AI does:** Runs `git blame` and explains the output format.

---

#### 12. Stash Uncommitted Work

**Command:**
```bash
git stash push -m "WIP: refactoring authentication"
```

**Natural language prompt:**
```
"Temporarily save my work so I can switch branches"
or
"Stash my changes with a description"
```

**What AI does:** Stashes with descriptive message for easy retrieval.

---

#### 13. Apply Stashed Changes

**Command:**
```bash
git stash pop
```

**Natural language prompt:**
```
"Bring back my stashed changes"
or
"Apply my most recent stash and remove it from the list"
```

**What AI does:** Applies stash and removes from stash list.

---

#### 14. Delete a Branch

**Command:**
```bash
git branch -d feature/old-feature
```

**Natural language prompt:**
```
"Delete the branch feature/old-feature"
or
"Clean up my old feature branch"
```

**What AI does:** Uses `-d` (safe delete) or `-D` (force delete) based on context.

---

#### 15. View Differences

**Command:**
```bash
git diff
git diff --staged
git diff main..feature-branch
```

**Natural language prompt:**
```
"Show me what I've changed since the last commit"
or
"Compare my feature branch with main"
or
"What's different between these two branches?"
```

**What AI does:** Chooses appropriate diff command based on intent.

## Part III: Complex Workflow Prompts

### Scenario 1: Cleaning Up Commit History

**Your situation:** You have 8 commits with messy messages. You want to squash them before creating a PR.

**Traditional approach:** Learn interactive rebase syntax, mark commits for squashing, resolve conflicts.

**Natural language approach:**

```
You: "I have 8 commits on this branch. Can you help me squash them into 2 commits: one for feature implementation, one for tests?"

Claude Code: "I'll help you do an interactive rebase. Let me first show you the 8 commits so we can identify which ones to group together."

[Shows commit list]

Claude Code: "I'll start an interactive rebase. We'll mark commits 1-5 to squash into one commit (feature), and commits 6-8 to squash into another (tests)."

[Guides through interactive rebase]

You: "The editor opened. What do I do?"

Claude Code: "Change 'pick' to 'squash' (or 's') for the commits you want to combine. Keep 'pick' for the first commit in each group. I'll help you edit."

[Completes successfully]

Claude Code: "Done! You now have 2 clean commits. Review them with `git log --oneline -n 2`."
```

**What you learned:** How interactive rebase works, without memorizing syntax.

---

### Scenario 2: Cherry-Picking Specific Commits

**Your situation:** You made commits on the wrong branch. You need to move specific commits to the correct branch.

**Natural language approach:**

```
You: "I accidentally made 3 commits on main instead of my feature branch. How do I move them to the feature branch?"

Claude Code: "We'll use cherry-pick to copy those commits to the feature branch, then remove them from main. First, let me see your commit history."

[Shows commits]

You: "Commits abc123, def456, and ghi789 should be on feature/user-auth instead."

Claude Code:
1. Switch to feature/user-auth
2. Cherry-pick each commit: git cherry-pick abc123 def456 ghi789
3. Switch back to main
4. Reset main to before those commits: git reset --hard HEAD~3
5. Force push if you've already pushed (ONLY if working alone)

Should I proceed?

You: "Yes, but I haven't pushed to GitHub yet."

Claude Code: "Great, that makes it safer. Executing steps..."

[Completes successfully]

Claude Code: "Done! The 3 commits are now on feature/user-auth, and main is back to its previous state."
```

**What you learned:** Cherry-picking strategy, when it's safe to reset.

---

### Scenario 3: Resolving Merge Conflicts

**Your situation:** You're merging a branch and hit conflicts. You're not sure how to proceed.

**Natural language approach:**

```
You: "I'm trying to merge my feature branch into main, but I have conflicts in auth.py. What do I do?"

Claude Code: "Let me help you resolve the conflict. First, let's see what's conflicting."

[Shows git status and conflict markers]

Claude Code: "You have a conflict in auth.py. The main branch changed the login function to use OAuth, while your branch changed it to use LDAP. Both changes happened to the same lines.

Here's what you need to do:
1. Open auth.py
2. Look for markers: <<<<<<< HEAD, =======, >>>>>>>
3. Decide which version to keep, or combine both
4. Delete the conflict markers
5. Save the file
6. Run: git add auth.py
7. Run: git commit to complete the merge

Would you like me to show you the conflicted section?"

You: "Yes, show me the conflict."

[Shows conflict]

You: "I want to keep OAuth from main, not LDAP from my branch."

Claude Code: "Got it. Edit auth.py and keep only the OAuth version (the part after <<<<<<< HEAD and before =======). Delete everything from ======= to >>>>>>> including the markers.

Then:
  git add auth.py
  git commit -m 'Merge feature branch, resolved conflict in auth.py by keeping OAuth'

Let me know when you've done that."

You: [Makes changes] "Done!"

Claude Code: "Perfect! Let me verify the merge completed successfully."

[Checks status]

Claude Code: "Merge successful! Your branch now has OAuth authentication."
```

**What you learned:** How to read conflict markers, when to ask for help, how to complete a merge.

---

### Scenario 4: Finding When a Bug Was Introduced

**Your situation:** A bug exists in production. You need to find which commit introduced it.

**Natural language approach:**

```
You: "There's a bug in the payment processing. It worked last month, but it's broken now. How do I find which commit broke it?"

Claude Code: "We'll use `git bisect` to do a binary search through your commits. Here's how it works:

1. Start bisect: git bisect start
2. Mark current commit as bad: git bisect bad
3. Mark a known good commit (from last month): git bisect good <commit-hash>
4. Git will check out commits in the middle, you test each one
5. Mark each as good or bad until we find the culprit

First, what's the commit hash from last month when it worked?"

You: "I don't remember the exact commit. Can you help me find one from September?"

Claude Code: "Sure. Let me show you commits from September."

[Shows commits]

You: "Try commit abc123 from September 15."

Claude Code: "Starting bisect with abc123 as good and current HEAD as bad..."

[Bisect process begins]

Claude Code: "Git checked out commit def456. Test the payment processing. Does it work or is it broken?"

You: [Tests] "It's broken."

Claude Code: "Marking def456 as bad and continuing..."

[Process continues]

Claude Code: "Found it! Commit ghi789 introduced the bug. The commit message is: 'Refactor payment validation logic.'

Let's look at what changed in that commit."

[Shows diff]

You: "I see the problem. The validation is checking the wrong field."

Claude Code: "Would you like to create a fix branch and revert that specific change?"
```

**What you learned:** How bisect works, how to find bug origins systematically.

## Part IV: Troubleshooting Prompts

### Understanding Git Errors

When Git gives you an error, ask AI to explain it in plain English.

#### Error 1: "Your branch is behind 'origin/main'"

**Git message:**
```
Your branch is behind 'origin/main' by 5 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)
```

**Your prompt:**
```
"Git says my branch is behind origin/main. What does this mean and what should I do?"
```

**AI explanation:**
```
"This means the main branch on GitHub has 5 commits that you don't have locally. Someone else pushed changes.

To fix:
  git pull origin main

This will download the 5 commits and update your local main branch.

It's safe because Git says 'can be fast-forwarded,' meaning there won't be conflicts."
```

---

#### Error 2: "fatal: refusing to merge unrelated histories"

**Git message:**
```
fatal: refusing to merge unrelated histories
```

**Your prompt:**
```
"I'm trying to merge but Git says 'refusing to merge unrelated histories.' What's wrong?"
```

**AI explanation:**
```
"This happens when you're trying to merge two branches that don't share a common ancestor—usually when you initialized separate repositories.

Common causes:
- You created a local repo and a GitHub repo separately
- You're trying to merge completely unrelated projects

To fix (if you're sure you want to merge):
  git merge --allow-unrelated-histories <branch>

But be careful—this is usually a sign something's wrong with your repo setup. Are you trying to connect a local repo to an existing GitHub repo?"
```

---

#### Error 3: "CONFLICT (content): Merge conflict in file.py"

**Git message:**
```
CONFLICT (content): Merge conflict in file.py
Automatic merge failed; fix conflicts and then commit the result.
```

**Your prompt:**
```
"I have a merge conflict in file.py. Walk me through resolving it."
```

**AI guidance:**
```
"A merge conflict means both branches changed the same lines in file.py. Here's how to resolve:

1. Open file.py in your editor
2. Look for conflict markers:
   <<<<<<< HEAD
   Your changes
   =======
   Their changes
   >>>>>>> branch-name

3. Decide which version to keep:
   - Keep yours (delete 'their changes' and markers)
   - Keep theirs (delete 'your changes' and markers)
   - Combine both (edit to merge logically)

4. Delete ALL conflict markers (<<<, ===, >>>)

5. Save the file

6. Mark as resolved:
   git add file.py

7. Complete the merge:
   git commit -m 'Resolved conflict in file.py'

Would you like me to look at the specific conflict?"
```

---

#### Error 4: "error: failed to push some refs"

**Git message:**
```
error: failed to push some refs to 'https://github.com/user/repo.git'
hint: Updates were rejected because the remote contains work that you do not have locally.
```

**Your prompt:**
```
"I can't push to GitHub. It says the remote has work I don't have. What do I do?"
```

**AI explanation:**
```
"Someone else pushed commits to GitHub while you were working. Your local branch is out of sync.

To fix:
1. Pull the remote changes:
   git pull origin main

2. If there are conflicts, resolve them (Git will tell you which files)

3. After resolving (if any), try pushing again:
   git push origin main

Alternative (if you're on a feature branch):
1. Pull with rebase to keep history clean:
   git pull --rebase origin main

2. Resolve any conflicts

3. Push:
   git push origin feature-branch

This ensures your local branch includes all remote changes before pushing yours."
```

### Asking "How Do I...?" Questions

AI is perfect for learning Git workflows:

**Example prompts:**

```
"How do I rename a branch?"

"How do I undo a pushed commit?"

"How do I see what changed in a specific commit?"

"How do I change the commit message of my last commit?"

"How do I delete a remote branch on GitHub?"

"How do I sync my fork with the original repository?"

"How do I move uncommitted changes to a new branch?"

"How do I recover a deleted branch?"
```

For each question, AI explains:
1. The concept (why you'd do this)
2. The command(s) (how to do it)
3. Warnings (when to be careful)
4. Alternatives (other approaches)

## Part V: Best Practices for AI CLI Conversations

### 1. Provide Context

**❌ Bad prompt:**
```
"How do I merge?"
```

**✅ Good prompt:**
```
"I have a feature branch called feature/auth with 5 commits. I want to merge it into main. My feature branch is up to date with main. How do I merge it safely?"
```

**Why good?** AI knows your situation, branch names, and can give specific advice.

---

### 2. Describe Your Goal, Not Just the Command

**❌ Bad prompt:**
```
"Run git rebase"
```

**✅ Good prompt:**
```
"I want to clean up my commit history before creating a PR. I have 7 commits, some are WIP messages. How should I organize them?"
```

**Why good?** AI can suggest the best approach (rebase, squash, etc.) rather than blindly executing a command.

---

### 3. Ask "Why" to Learn

**After AI suggests a command:**

```
AI: "Run git reset --soft HEAD~1"

You: "Why --soft instead of --hard?"

AI: "--soft keeps your changes staged. --hard would delete them permanently. --mixed (default) keeps changes but unstages them."

You: "Got it. So --soft is safest when I want to modify the commit."
```

Build your Git knowledge by asking follow-up questions.

---

### 4. Verify Before Destructive Operations

**AI suggests:**
```
"Run: git reset --hard HEAD~5"
```

**You ask:**
```
"Wait, will this delete my last 5 commits permanently? Is there a safer way?"
```

**AI responds:**
```
"Yes, --hard is destructive. If you want to keep the changes, use:
  git reset --soft HEAD~5

Or if you're not sure, create a backup branch first:
  git branch backup-before-reset
  git reset --hard HEAD~5

That way you can recover if needed."
```

**Always question commands that:**
- Use `--force`, `--hard`, `-D` (force flags)
- Involve `push --force`
- Delete branches or commits

---

### 5. Share Error Messages Completely

**❌ Bad prompt:**
```
"Git gave an error when I tried to push."
```

**✅ Good prompt:**
```
"Git gave this error when I tried to push:

error: failed to push some refs to 'origin'
hint: Updates were rejected because the remote contains work that you do not have locally.

What does this mean and how do I fix it?"
```

**Why good?** Complete error messages help AI diagnose the exact problem.

---

### 6. Confirm Understanding Before Proceeding

**AI gives you 5 commands to run.**

**You respond:**
```
"Before I run these, let me make sure I understand:
1. First command updates my main branch
2. Second creates a new feature branch
3. Third merges main into my feature branch
4. Fourth resolves any conflicts
5. Fifth pushes to GitHub

Is that right?"
```

**AI confirms or corrects your understanding.**

**Then you proceed confidently.**

---

### 7. Learn Patterns, Not Just Commands

**After AI helps you several times:**

```
You: "I notice every time I want to start a new feature, you tell me to:
1. git checkout main
2. git pull origin main
3. git checkout -b feature/name

Is this the standard pattern?"

AI: "Exactly! This pattern ensures:
- You're starting from main (not some random branch)
- You have the latest code (pull)
- You create a fresh branch with a descriptive name

You can memorize this pattern and use it every time."

You: "Great. I'll make that my habit."
```

Look for repeating patterns and internalize them.

---

### 8. Use AI as a Git Tutor

**Don't just ask for commands—ask for explanations:**

```
"Explain the difference between merge and rebase with examples."

"What's the three-stage model in Git? How does staging work?"

"Why do we need branches? Can't we just all work on main?"

"What's the difference between git pull and git fetch?"

"When should I use git revert vs. git reset?"
```

AI can teach concepts in a way that complements hands-on practice.

## Practice Exercises

### Exercise 1: Command Translation

**Objective:** Practice translating Git commands into natural language prompts.

**For each Git command, write a natural language prompt that would achieve the same result:**

1. `git log --oneline --graph -n 10`
2. `git checkout -b feature/new-ui`
3. `git reset --soft HEAD~1`
4. `git stash push -m "WIP on authentication"`
5. `git blame auth.py`

💡 **Learning with AI**: After writing your prompts, ask Claude Code:
- "Here are my natural language versions of these commands. Are they clear enough for you to understand my intent?"

<details>
<summary>Show Answer</summary>

**Possible natural language prompts:**

1. "Show me the last 10 commits in a visual graph format"
   or "Display recent commit history as a tree"

2. "Create a new branch called feature/new-ui and switch to it"
   or "Start a new feature branch for the UI redesign"

3. "Undo my last commit but keep all the changes staged"
   or "I want to modify my last commit"

4. "Temporarily save my authentication work in progress"
   or "Stash my current changes with a description about authentication work"

5. "Show me who last modified each line in auth.py"
   or "I want to see the authorship history of the auth file"

**Key insight:** Multiple phrasings work! AI understands intent, not exact wording.

</details>

---

### Exercise 2: Complex Workflow Prompt

**Objective:** Use natural language to execute a multi-step Git workflow.

**Scenario:** You're working on a feature branch. You need to update it with the latest changes from main, then push it to GitHub.

**Task:** Write a single prompt that asks Claude Code to do all of this.

💡 **Learning with AI**: After writing your prompt, ask Claude Code to execute it and explain each step it takes.

<details>
<summary>Show Answer</summary>

**Example prompt:**

```
"I'm on branch feature/dashboard. I need to update it with the latest changes from main, then push it to GitHub. Can you help me do this safely?"
```

**What Claude Code would do:**

1. Check current branch: `git branch` (verify you're on feature/dashboard)
2. Commit any uncommitted changes or ask you to stash
3. Switch to main: `git checkout main`
4. Pull latest: `git pull origin main`
5. Switch back: `git checkout feature/dashboard`
6. Merge main: `git merge main`
7. Resolve conflicts if any (guides you through)
8. Push: `git push origin feature/dashboard`

**Alternative approach (rebase instead of merge):**

If you prefer rebase:
```
"Update my feature/dashboard branch with main using rebase, then push to GitHub."
```

Claude Code would use `git rebase main` instead of merge.

</details>

---

### Exercise 3: Troubleshooting with AI

**Objective:** Practice asking AI to explain Git errors.

**Scenario:** You tried to push and got this error:

```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/user/repo.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

**Task:** Write a prompt asking AI to explain this error and how to fix it.

💡 **Learning with AI**: Include the full error message in your prompt for best results.

<details>
<summary>Show Answer</summary>

**Example prompt:**

```
"I'm trying to push my changes but got this error:

[paste full error message]

What does this mean and how do I fix it? I don't want to lose any of my local changes."
```

**AI explanation:**

```
"This error means someone else pushed commits to the main branch on GitHub while you were working. Your local main is now 'behind' the remote.

To fix safely:

1. Pull remote changes:
   git pull origin main

2. Git will try to merge automatically:
   - If successful, you'll have both your changes and theirs
   - If there are conflicts, Git will tell you which files

3. If conflicts occur:
   - Open the conflicted files
   - Resolve the conflicts (keep both changes or choose one)
   - git add <resolved-files>
   - git commit -m 'Merge remote changes'

4. Push again:
   git push origin main

Your local changes are safe—this process will preserve them."
```

</details>

---

### Exercise 4: Learning from AI Execution

**Objective:** Understand what AI does when executing commands.

**Task:**

1. Ask Claude Code: "Create a new feature branch called feature/test-ai-prompts"

2. Watch what commands it runs

3. Ask follow-up: "Why did you run those specific commands in that order?"

4. Learn the pattern for future use

💡 **Learning with AI**: After the conversation, summarize what you learned: "So the pattern for starting a new feature is: ensure I'm on main, pull latest, create branch. Got it!"

<details>
<summary>Show Answer</summary>

**AI execution:**

```
1. git checkout main
   (Ensures you're starting from the right branch)

2. git pull origin main
   (Gets the latest code from GitHub)

3. git checkout -b feature/test-ai-prompts
   (Creates new branch and switches to it)
```

**AI explanation of order:**

"This order ensures:
- You create the branch from main (not from some random branch you were on)
- Your branch starts with the absolute latest code
- You're immediately on the new branch ready to work

This is the standard 'new feature' pattern you should use every time."

**What you learned:** Memorize this three-step pattern for starting any new feature.

</details>

---

### Exercise 5: Asking "Why" Questions

**Objective:** Build understanding by asking follow-up questions.

**Task:**

1. Ask Claude Code: "How do I undo my last commit?"

2. When it responds with a command, ask: "Why did you choose that approach?"

3. Ask: "What are the alternatives and when would I use them?"

4. Ask: "What would happen if I used `--hard` instead?"

💡 **Learning with AI**: Don't just execute commands—understand the reasoning behind them.

<details>
<summary>Show Answer</summary>

**Conversation:**

```
You: "How do I undo my last commit?"

AI: "Use: git reset --soft HEAD~1
This will undo the commit but keep all your changes staged."

You: "Why --soft instead of other options?"

AI: "--soft is the safest for undoing commits because:
- It preserves all your changes in the staging area
- You can immediately re-commit or make more changes
- Nothing is lost

Alternatives:
- --mixed (default): Keeps changes but unstages them
- --hard: Deletes changes completely (dangerous!)

Use --soft when you want to modify the commit.
Use --mixed when you want to reorganize what's committed.
Use --hard only when you're sure you want to delete everything."

You: "What happens if I use --hard by accident?"

AI: "Your changes are gone permanently (unless you have uncommitted changes backed up elsewhere). However, Git keeps commits in reflog for ~30 days, so there's a chance to recover:

  git reflog
  git checkout <commit-hash>

But it's complex. Better to avoid --hard unless you're certain."

You: "Got it. I'll use --soft when I want to keep changes."
```

**What you learned:** The three reset modes, when to use each, and how to recover from mistakes.

</details>

---

### Exercise 6: Complex Scenario Resolution

**Objective:** Use AI to guide you through a realistic complex scenario.

**Scenario:**

You're working on `feature/payment-processor`. You made 8 commits over two days. Some commits are good, some say "WIP" or "fix typo". You want to:

1. Clean up the commit history into 3 logical commits
2. Update your branch with the latest from main
3. Push to GitHub
4. Create a pull request

**Task:** Write a single comprehensive prompt that asks AI to guide you through this entire workflow.

💡 **Learning with AI**: Ask AI to explain each step before executing, so you understand the full workflow.

<details>
<summary>Show Answer</summary>

**Example prompt:**

```
"I'm on branch feature/payment-processor with 8 commits. Some are messy (WIP messages, typo fixes). Before creating a PR, I want to:

1. Squash the commits into 3 logical groups:
   - Payment integration (commits 1-4)
   - Tests (commits 5-6)
   - Documentation (commits 7-8)

2. Update my branch with latest from main

3. Push to GitHub

4. Create a pull request

Can you guide me through this step by step, explaining each command before I run it?"
```

**AI response (summarized):**

```
"I'll help you clean up your commits and prepare the PR. Here's the plan:

Step 1: Interactive Rebase
We'll use git rebase -i HEAD~8 to squash commits.

Step 2: Update with Main
Merge or rebase main into your branch.

Step 3: Push
Use git push --force-with-lease since we rewrote history.

Step 4: Create PR
Use gh pr create or GitHub web UI.

Let's start with Step 1. First, let me show you your 8 commits so we can decide which to squash together..."

[Guides through interactive rebase]

"Great! You now have 3 clean commits. Next, let's update with main..."

[Guides through merge]

"Perfect! Now let's push (using --force-with-lease since we rewrote history)..."

[Guides through push]

"Excellent! Now create your PR with a description that summarizes the payment integration feature..."

[Guides through PR creation]

"All done! Your PR is ready for review with a clean, readable commit history."
```

**What you learned:** The complete workflow for preparing a professional pull request with clean history.

</details>

---

## Self-Assessment

Test your understanding with these questions:

1. **What is the main benefit of using natural language prompts for Git?**
   - A) You never need to learn Git
   - B) You understand concepts while AI handles syntax
   - C) AI is faster than typing commands
   - D) Natural language is more powerful than Git commands

2. **When should you NOT rely on AI prompts?**
   - A) When the operation is critical and you should understand it
   - B) When you don't understand what you're asking for
   - C) When learning basic concepts that are foundational
   - D) All of the above

3. **Which prompt is better?**
   - A) "Run git rebase"
   - B) "I want to clean up my commit history. I have 7 commits with messy messages. How should I organize them?"

4. **After AI suggests a command, what should you do?**
   - A) Run it immediately without reading
   - B) Ask "why" to understand the reasoning
   - C) Ignore it and search online
   - D) Copy it but don't run it

5. **What should you include in troubleshooting prompts?**
   - A) Only the error title
   - B) The complete error message
   - C) Your guess at what's wrong
   - D) Just ask "Git broke, help"

6. **How should you verify destructive operations?**
   - A) Trust AI completely
   - B) Ask if there's a safer alternative
   - C) Create a backup branch first
   - D) Both B and C

7. **What's a good follow-up question after AI helps you?**
   - A) "Why did you choose this approach?"
   - B) "What are the alternatives?"
   - C) "What would happen if I did X instead?"
   - D) All of the above

8. **Which is a better learning strategy?**
   - A) Always use AI prompts, never memorize commands
   - B) Never use AI, memorize all Git syntax
   - C) Learn concepts, use AI for syntax, build patterns over time
   - D) Only use Git GUI tools

<details>
<summary>Show Answers</summary>

1. **B** - You understand concepts while AI handles syntax (balance of understanding + convenience)
2. **D** - All of the above (don't rely solely on prompts when you should understand the operation)
3. **B** - The second prompt provides context and intent, allowing AI to suggest the best approach
4. **B** - Ask "why" to understand the reasoning (build your knowledge)
5. **B** - The complete error message (helps AI diagnose accurately)
6. **D** - Both B and C (always question destructive operations and create backups)
7. **D** - All of the above (curiosity builds understanding)
8. **C** - Learn concepts, use AI for syntax, build patterns over time (balanced approach)

**Scoring:**
- 7-8: Excellent! You understand how to use AI as a learning tool
- 5-6: Good! Review best practices for AI conversations
- 3-4: Needs work—focus on asking "why" and providing context
- Below 3: Review this lesson and practice the exercises

</details>

---

## Final Reflection

### Pause and Reflect

**Reflection 1: How has your understanding of Git changed from Lesson 1 to now?**

You started by learning *why* Git matters (safety net for AI development). Then you learned *what* Git does (commits, branches, merging, PRs). Now you can use AI to handle *how* Git works (syntax and commands).

You've built a **complete mental model** of version control that balances understanding with practical efficiency.

**Reflection 2: When will you use Git commands directly vs. asking AI?**

- **Direct commands** for frequent operations you've memorized: `git status`, `git add`, `git commit`
- **AI prompts** for complex operations you use less often: interactive rebase, cherry-picking, bisect
- **AI explanations** when you encounter errors or want to learn a new concept

**Reflection 3: How will you ensure you don't become dependent on AI without understanding?**

- Always ask "why" after AI suggests a command
- Practice fundamental operations manually until they're habitual
- Use AI as a teacher, not just a command generator
- Review what AI executes and learn from its choices

---

## What You've Mastered

Across all 5 lessons, you've built complete Git mastery:

✅ **Lesson 1** - Why Git matters (safety, collaboration, auditability)
✅ **Lesson 2** - Git essentials (commands, workflow, commit messages)
✅ **Lesson 3** - Safe experimentation (checkpoints, branches, rollback)
✅ **Lesson 4** - Team collaboration (pull requests, code review, merging)
✅ **Lesson 5** - Natural language (AI as convenience layer)

You now have:
- **Conceptual understanding** (what Git does and why)
- **Practical skills** (how to use Git for real work)
- **AI collaboration** (using AI to handle complexity)
- **Safety mindset** (experimentation without fear)

---

## What's Next: The End-of-Chapter Project

**Your final challenge:** Complete the comprehensive project that combines all skills:

1. Create a Git repository for an AI-assisted project
2. Make multiple commits with AI attribution
3. Create checkpoint commits before AI sessions
4. Use branches for experimentation
5. Create a pull request on GitHub
6. Simulate code review and address feedback
7. Merge your PR successfully
8. Use natural language prompts for at least 2 Git operations

This project proves you can:
- Work with Git safely in AI-driven development
- Collaborate with teammates using pull requests
- Use AI tools as a convenience layer while maintaining understanding

**Go forth and experiment fearlessly. Git is your safety net.**

---

## Quick Reference: Essential Natural Language Prompts

**Repository Operations:**
- "Show me the status of my repository"
- "Create a new branch called [name] and switch to it"
- "List all branches"

**Committing:**
- "Commit all my changes with message [text]"
- "Show me my commit history"
- "Undo my last commit but keep the changes"

**Branching & Merging:**
- "Merge [branch-name] into main"
- "Update my feature branch with the latest from main"
- "Delete the branch [name]"

**Remote Operations:**
- "Push my branch to GitHub"
- "Pull the latest changes from GitHub"
- "Update my local main with remote changes"

**Troubleshooting:**
- "I have a merge conflict in [file]. Help me resolve it."
- "Git gave me this error: [paste error]. What does it mean?"
- "Show me who last modified [file]"

**Complex Operations:**
- "Help me clean up my commit history before creating a PR"
- "I made commits on the wrong branch. How do I move them?"
- "Show me what changed in the last 5 commits"

**Use these prompts with Claude Code, Gemini CLI, or any AI assistant with Git knowledge.**

---

## Congratulations!

You've completed Chapter 8: Git & GitHub for AI-Driven Development.

You're now equipped to:
- Experiment with AI tools without fear (checkpoints and rollback)
- Collaborate safely using pull requests and code review
- Use natural language to execute Git operations efficiently
- Track AI contributions over time with proper attribution

**Git is no longer intimidating—it's your superpower.**

As you continue your AI-driven development journey, remember:
- Commit often (especially before AI sessions)
- Branch for experiments (keep main safe)
- Review AI code carefully (human judgment still essential)
- Use AI as a learning tool (ask "why" frequently)

**Your next challenge:** Apply these Git skills throughout the rest of this book as you build AI-powered projects. Every project from here forward will use Git as the foundation for safe, collaborative development.

Welcome to fearless AI-driven development.
