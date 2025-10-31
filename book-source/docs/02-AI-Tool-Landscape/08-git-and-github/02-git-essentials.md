---
title: "Lesson 2: Git Essentials - Commands and Setup"
sidebar_position: 2
description: "Install Git, configure it, and execute the basic workflow - your first commits start here."
---

# Lesson 2: Git Essentials - Commands and Setup

## Every Commit Is a Story

In Lesson 1, you learned *why* version control matters: it's how collaborative teams track decisions, recover from mistakes, and build software together. You saw how Git solved real problems in the industry and understood its role in modern development workflows.

Now comes the practical part—the part where your hands touch the keyboard and Git becomes a tool you actually use, not just an idea you understand. This lesson teaches you the mechanics: how to install Git on your computer, set it up with your identity, and execute the workflows that will power your development journey.

By the end of this lesson, you'll have Git running on your machine, configured with your name and email, and ready to create your first commits. This is foundational. Every developer you'll work with uses these same commands. Every open-source project you'll contribute to expects this setup. This is the common language of collaborative development.

---

## Part I: Installation & Setup

Git is **free, open-source software** that runs on Windows, macOS, and Linux. The installation process is straightforward and takes about 5 minutes.

### Windows Installation

**Step 1: Download Git**

1. Visit [https://git-scm.com](https://git-scm.com)
2. Click the blue "Download" button for Windows
3. The installer file (e.g., `Git-2.46.0-64-bit.exe`) will download to your computer

**Step 2: Install Git Bash**

1. Open the downloaded `.exe` file
2. Click through the installer using **default settings**—this is important
   - Accept the license
   - Keep the installation path as `C:\Program Files\Git`
   - Select **"Git Bash Here"** (this option adds Git Bash to your right-click context menu—very useful)
3. Complete the installation

> **What is Git Bash?** Git Bash is a command-line environment that brings Unix-style commands to Windows. It lets you use the same Git commands as macOS and Linux users.

**Step 3: Verify Installation**

Open **Git Bash** (right-click on your desktop or folder and select "Git Bash Here", or search for "Git Bash" in your Start menu):

```bash
git --version
```

**Expected output** (version number may differ):
```
git version 2.46.0.windows.1
```

If you see this, Git is installed correctly. If you get "command not found," see the Troubleshooting section below.

---

### macOS Installation

macOS users have two options: Homebrew (simpler if you already use it) or a direct installer.

#### Option 1: Homebrew (Recommended)

If you have **Homebrew** installed:

```bash
brew install git
```

Then verify:

```bash
git --version
```

**Expected output**:
```
git version 2.46.0
```

> **Don't have Homebrew?** Visit [https://brew.sh](https://brew.sh) and follow the one-line install. Or skip to Option 2.

#### Option 2: Direct Installer

1. Visit [https://git-scm.com](https://git-scm.com)
2. Click the blue "Download" button for macOS
3. Double-click the installer and follow the prompts
4. macOS may prompt you to install Xcode command-line tools—click "Install" if this happens. This is normal and required.

After installation, open **Terminal** and verify:

```bash
git --version
```

**Expected output**:
```
git version 2.46.0
```

---

### Linux Installation

Linux distributions ship with package managers that make installing Git trivial.

#### Debian/Ubuntu (and Mint, Pop!_OS, etc.)

Open a terminal and run:

```bash
sudo apt-get update
sudo apt-get install git
```

When prompted for your password, enter it (no characters will display—this is normal).

#### Fedora/RHEL/CentOS

Open a terminal and run:

```bash
sudo dnf install git
```

#### Verify Installation

All Linux users, run:

```bash
git --version
```

**Expected output**:
```
git version 2.46.0
```

---

### First-Time Configuration (Required)

Before you create your first commit, Git needs to know **who you are**. Every commit stores the author's name and email—this is how teams know who made each change.

**Configure your identity globally** (this applies to all repositories on your computer):

**On Windows (Git Bash), macOS, or Linux:**

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace `"Your Name"` with your actual name (e.g., `"Jane Smith"`) and `"your.email@example.com"` with your real email (e.g., `"jane.smith@example.com"`).

**Example:**
```bash
git config --global user.name "Alice Johnson"
git config --global user.email "alice.johnson@example.com"
```

> **Why globally?** The `--global` flag stores this configuration in your home directory so it applies to every Git repository you work with on this machine. You can override it per-repository later if needed, but global configuration is the standard practice.

**Verify Your Configuration**

Run this command to see all your Git settings:

```bash
git config --list
```

You should see output including:

```
user.name=Alice Johnson
user.email=alice.johnson@example.com
... (other settings)
```

Look for your name and email in the list. If you see them, you're configured correctly.

---

### Troubleshooting Common Issues

**Issue: "git: command not found"**

This means Git is installed but your terminal can't find it. Try:

1. **Windows**: Close Git Bash and reopen it. If that doesn't work, restart your computer.
2. **macOS**: If you used Homebrew, run `brew doctor` to diagnose installation issues. For the direct installer, restart your terminal.
3. **Linux**: Verify the installation ran without errors. Run `which git` to check if Git is in your PATH. If nothing appears, reinstall Git using your package manager.

**Issue: Permission denied on Linux**

If you see a permission error when running `sudo apt-get` or `sudo dnf`, ensure you're using `sudo` (run the full command with `sudo` at the front).

**Issue: macOS prompts for Xcode command-line tools**

This is normal. Click "Install" when prompted. This installs development tools required by Git. It takes a few minutes.

---

## Part II: The Core Workflow - Show Then Explain

Let's see Git in action. You'll create a real Python project, track it with Git, and understand how each command works.

### A Real Example: Building a Calculator

Imagine you're building a simple Python calculator. You want to track your work as you add features. Here's exactly what happens:

```bash
mkdir my-calculator
cd my-calculator
git init
```

Expected output:
```
Initialized empty Git repository in G:/my-calculator/.git/
```

**What just happened**: You created a folder, entered it, and told Git to start watching it. Git created a hidden `.git` folder that stores all your project history.

Now create the calculator file. Open a text editor and save this as `calculator.py`:

```python
"""A simple calculator module with basic operations."""


def add(a, b):
    """Add two numbers together."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers together."""
    return a * b


if __name__ == "__main__":
    print("Calculator ready:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 × 7 = {multiply(6, 7)}")
```

Now check what Git sees:

```bash
git status
```

Expected output:
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        calculator.py

nothing added to commit but untracked files present (tracking enabled)
```

**Translation**: Git sees your calculator file, but it's not being tracked yet. Git is asking: "Do you want me to remember this file?"

Tell Git to track it:

```bash
git add calculator.py
```

No output means success. Now check status again:

```bash
git status
```

Expected output:
```
On branch main

No commits yet

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   calculator.py
```

**Translation**: Your file is now "staged"—ready to be saved into history. It's in the waiting area, like items in a checkout line.

Create your first checkpoint (commit):

```bash
git commit -m "Add basic calculator functions"
```

Expected output:
```
[main (root-commit) a1b2c3d] Add basic calculator functions
 1 file changed, 20 insertions(+)
 create mode 100644 calculator.py
```

**Translation**: Git saved a snapshot with the message you wrote. The code `a1b2c3d` is a unique identifier for this checkpoint.

View your project history:

```bash
git log --oneline
```

Expected output:
```
a1b2c3d Add basic calculator functions
```

**Translation**: You have one commit in your history. The first part (`a1b2c3d`) is the commit ID. The message tells you what changed.

---

### Understanding Each Command

#### `git init` — Start Tracking

What it does: Creates a `.git` folder in your project. This hidden folder stores every change you ever make.

When to use: Once per project, at the very beginning.

#### `git status` — Check What Changed

What it does: Shows you three things:
- Files you've edited but not staged
- Files you've staged but not committed
- Files Git doesn't know about yet

How to read it: Look for section headers. Files listed under "Changes to be committed" are ready. Files under "Changes not staged" need `git add`.

#### `git add` — Prepare Changes

What it does: Moves files from "edited" to "staged." Staging lets you choose exactly which changes to save together.

Example: You edited two files but only want to commit one. Use `git add filename.py` to stage just that file.

#### `git commit` — Create a Checkpoint

What it does: Saves all staged changes as a permanent snapshot with a message explaining what changed.

The message matters: Write clear messages like "Add basic calculator functions" not "stuff" or "fix bugs." Future you will thank present you.

#### `git log` — View History

What it does: Shows all your commits in order, newest first. Each line has:
- A commit ID (unique code like `a1b2c3d`)
- Your commit message

Use `git log --oneline` for a quick view. Use `git log` (without `--oneline`) for more details.

---

## Part III: The Three-Stage Concept

Git doesn't save your changes instantly. Instead, changes move through three stages. Understanding these stages is the key to mastering Git.

### The Three Stages: A Visual Journey

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│  Working Dir    │      │  Staging Area   │      │   Repository    │
├─────────────────┤      ├─────────────────┤      ├─────────────────┤
│                 │      │                 │      │                 │
│  Your files     │ --git add--> Chosen    │ --git commit--> Saved │
│  on disk        │      │  changes ready  │      │  history in     │
│                 │      │  for commit     │      │  .git folder    │
│ (untracked or   │      │                 │      │                 │
│  modified)      │      │ (staged)        │      │ (permanent)     │
└─────────────────┘      └─────────────────┘      └─────────────────┘
```

### Stage 1: Working Directory

This is your project folder. When you edit `calculator.py`, you're working here. These changes exist only on your computer right now. Git sees them but hasn't committed them.

### Stage 2: Staging Area

This is the "waiting room." After you run `git add calculator.py`, the file moves here. You're telling Git: "I'm ready to save this change." You can stage some files and leave others unstaged.

Why does this matter? Imagine you edited three files but only two are ready to commit. Stage just those two, commit them, then commit the third one separately. This keeps your history organized.

### Stage 3: Repository

This is permanent history stored in the `.git` folder. Once you commit, the change is recorded forever with a commit ID and your message. This is what `git log` shows.

### How `git status` Shows All Three Stages

Run `git status` at any time and it tells you exactly where changes are:

```bash
$ git status
On branch main

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   calculator.py    ← In the staging area (ready to commit)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   README.md         ← In working directory (not staged yet)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.py                       ← Git doesn't know about this file
```

**Reading this output**:
- "Changes to be committed": These files are staged and will be saved when you commit.
- "Changes not staged for commit": You edited these files, but they're not staged yet.
- "Untracked files": Git has never seen these files before.

### Why Three Stages?

New developers often ask: "Why not just save changes instantly?"

**Three stages give you control**. You can:
- Edit multiple files but commit them separately
- Review what you're saving before committing
- Decide which changes go together logically
- Avoid committing incomplete or accidental changes

This prevents mistakes. You won't accidentally commit test files or half-finished features because you had to explicitly stage them first.

---

### Key Takeaways

- **`git init`** creates a repository; **`git status`** shows where changes are
- **`git add`** moves changes to the staging area; **`git commit`** saves them permanently
- Changes flow: Working Directory → Staging Area → Repository
- `git status` output shows you exactly which stage each change is in
- Staging lets you choose which changes to commit together

---

## Part IV: Reading Git Output

When you run Git commands, Git talks back to you. Understanding what Git says is crucial—it tells you the state of your work, what's ready to commit, and what's waiting for action.

### Understanding `git status` in Detail

The `git status` command is your window into your repository's current state. Let's break down what a realistic output looks like:

```
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to update the remote branch)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   calculator.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   utils.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test_results.txt
        config.local.json
```

**What each section means:**

- **"On branch main"** — You're working on the `main` branch
- **"Your branch is ahead of 'origin/main' by 2 commits"** — You have 2 commits saved locally that haven't been uploaded to the remote server yet
- **"Changes to be committed"** — Files you've staged with `git add` and are ready to commit. Git will include these when you run `git commit`
- **"Changes not staged for commit"** — Files you've edited, but you haven't told Git to include them in the next commit yet. You need to `git add` them first
- **"Untracked files"** — Files in your folder that Git doesn't know about and isn't tracking. They won't be included in commits unless you add them

**Two important messages you'll see:**

- **"nothing to commit, working tree clean"** — Everything is saved. All your changes are committed, and there's nothing new Git needs to track. Your folder matches what's in the repository
- **"nothing added to commit but untracked files present"** — You have new files Git doesn't know about, but you haven't told Git to track them. You need to `git add` them if you want them in your project

### Understanding `git log` Output

The `git log` command shows you the history of commits in your repository. Here's what it looks like:

**Full output (git log):**

```
commit 3f8a9b2c7e1d4a5f6g9h8i (HEAD -> main)
Author: Alex Chen <alex@example.com>
Date:   Thu Oct 24 14:32:15 2024 -0600

    Add error handling for API timeout

    When the API doesn't respond within 5 seconds,
    the program now logs a warning and retries once.

commit 2e7c8d1b5f4a9g3h6i2j
Author: Jordan Martinez <jordan@example.com>
Date:   Wed Oct 23 10:15:42 2024 -0600

    Refactor calculate function for readability

commit 1d6b7c9a4e3f8g2h5i1j
Author: Casey Wu <casey@example.com>
Date:   Mon Oct 21 09:00:22 2024 -0600

    Initial project setup
```

**Condensed output (git log --oneline):**

```
3f8a9b2 Add error handling for API timeout
2e7c8d1 Refactor calculate function for readability
1d6b7c9 Initial project setup
```

**Breaking down each piece:**

| Part | Example | Meaning |
|------|---------|---------|
| **Commit hash** | `3f8a9b2` | A unique identifier for this commit (like a fingerprint). The full version is longer; the short version is 7 characters |
| **Branch marker** | `(HEAD -> main)` | `HEAD` means "you are here." It shows which commit you're currently on and which branch (`main`) |
| **Author** | `Alex Chen <alex@example.com>` | Who made this commit |
| **Date** | `Thu Oct 24 14:32:15 2024 -0600` | When the commit was made |
| **Message** | `Add error handling for API timeout` | A description of what changed in this commit |

### Common Git Messages Explained

When you work with Git, you'll see these messages frequently:

**"nothing to commit, working tree clean"**
- What it means: Everything is saved and committed. There are no changes Git is tracking
- Your action: Nothing! Your work is safe in the repository

**"Changes not staged for commit"**
- What it means: You edited files, but you haven't used `git add` to prepare them for committing
- Your action: Run `git add <filename>` to stage the file, then `git commit`

**"Your branch is ahead of 'origin/main' by X commits"**
- What it means: You have commits saved locally that haven't been uploaded to the remote server (GitHub, GitLab, etc.) yet
- Your action: Run `git push` to upload your commits to the remote server

**"Untracked files"**
- What it means: Git sees new files in your folder, but you haven't told Git to start tracking them
- Your action: Run `git add <filename>` to start tracking the file, or add it to `.gitignore` if you don't want to track it

---

## Part V: Commit Messages with AI Attribution

A commit message is a note you leave for your teammates—and for yourself in the future. It should explain *what* changed and *why*. When AI tools help you write code, attribution matters for transparency and auditability.

### Best Practices for Commit Messages

Strong commit messages follow a simple pattern:

**1. Use present tense, not past tense:**
- Good: `Add error handling for API timeout`
- Avoid: `Added error handling for API timeout`

**2. Be descriptive and specific:**
- Good: `Fix off-by-one error in loop counter`
- Avoid: `Fix bug`

**3. Start with a verb:**
Common verbs include:
- **Add** — Introduce new functionality or files
- **Fix** — Correct a bug or issue
- **Update** — Modify existing code or documentation
- **Remove** — Delete code or files
- **Refactor** — Restructure code without changing behavior

**4. Keep the first line concise:**
- First line should be 50 characters or less
- It's the subject line, like an email subject
- If you need more detail, add a blank line and then write a longer description

**Example with both subject and description:**

```
Add error handling for API timeout

When the external API doesn't respond within 5 seconds,
the application now logs a warning and retries once
before falling back to cached data.
```

### AI Attribution Pattern

When AI tools (Claude, ChatGPT, Gemini, Copilot, etc.) generate or significantly contribute to code changes, **attribute them in your commit message**. This practice:

- **Tracks AI involvement** — You know which changes came from AI vs. human coding
- **Ensures auditability** — Useful for code review, compliance, and understanding decisions
- **Promotes team transparency** — Everyone knows you used AI assistance
- **Helps learning** — You can review AI-generated code later to understand what it did

**Attribution format:**

```
[AI] <Tool-Name> - <What Changed>
```

**Examples:**

- `[AI] Claude - Add input validation for user email`
- `[AI] Copilot - Refactor database query for performance`
- `[AI] Gemini - Generate unit tests for calculator functions`
- `Add unit tests for calculator functions` (human-written, no AI tag needed)

**When to use AI attribution:**

- AI generated the code (even if you edited it afterward)
- AI wrote a significant portion that you then refined
- AI helped you solve a complex problem

**When you don't need AI attribution:**

- You wrote the code from scratch
- You only asked AI for advice or explanation (no code generation)
- You used AI to review code but wrote it yourself

### Good vs. Poor Commit Messages

Here's a comparison to help you recognize strong patterns:

| Good Message | Poor Message | Why Good Wins |
|--------------|--------------|---------------|
| Add subtract and multiply functions | stuff | Describes exactly what was added |
| [AI] Claude - Fix off-by-one error in loop | fix bug | Attributes AI and specifies the fix |
| Update README with setup instructions | updated stuff | Clear about what file and what changed |
| Refactor authentication module for async/await | changes | Explains both what and why (async/await) |
| Remove unused import statements | cleanup | Specific about what was removed |
| [AI] Copilot - Add input validation for API payload | add validation | Attributes AI and describes the change |

**Poor messages fail because they:**
- Use vague words ("stuff," "changes," "fixes")
- Don't explain what was actually changed
- Don't make it easy for someone reviewing the code to understand the intent

**Good messages succeed because they:**
- Use clear action verbs
- Say specifically what changed
- Help future readers understand the context
- Include AI attribution when appropriate

### Real-World Example Workflow

Here's how it looks in practice:

```bash
# You edit your calculator.py file
# You run git status
$ git status
On branch main
Changes not staged for commit:
  modified:   calculator.py

# You use Claude to help fix a bug and add error handling
# Claude generates code; you review and integrate it
# Now you stage the file
$ git add calculator.py

# You commit with an attributed message
$ git commit -m "[AI] Claude - Add error handling for division by zero"

# Git confirms
[main 7a4c9e2] [AI] Claude - Add error handling for division by zero
 1 file changed, 12 insertions(+)

# You check the log
$ git log --oneline
7a4c9e2 [AI] Claude - Add error handling for division by zero
3f8a9b2 Add subtract and multiply functions
2e7c8d1 Refactor calculate function for readability
```

Every person on your team can now see that Claude helped with the error handling change. This builds trust and transparency in how AI is being used in your project.

---

## Exercises

### Exercise 1: Install Git and Verify
**Objective:** Ensure Git is properly installed on your system.

**Steps:**
1. Download Git from https://git-scm.com/ (Windows/Mac) or use your package manager (Linux)
2. Follow the installation wizard, accepting default settings
3. Open a terminal or command prompt
4. Run: `git --version`

**Success Criteria:**
- A version number displays (e.g., "git version 2.42.0")
- No "command not found" error

**Time:** 10 minutes

---

### Exercise 2: Configure Your Git Identity
**Objective:** Set up your global Git user information.

**Steps:**
1. Open terminal/command prompt
2. Run: `git config --global user.name "Your Full Name"`
3. Run: `git config --global user.email "your.email@example.com"`
4. Verify: `git config --list | grep user` (Mac/Linux) or `git config --list | findstr user` (Windows)

**Success Criteria:**
- Your name and email appear in the output
- No errors during configuration

**Time:** 5 minutes

---

### Exercise 3: Initialize Your First Repository
**Objective:** Create and initialize a Git repository.

**Steps:**
1. Create a folder: `mkdir my-first-repo`
2. Navigate into it: `cd my-first-repo`
3. Initialize: `git init`
4. Check status: `git status`

**Success Criteria:**
- Output shows "On branch main" (or "master")
- A hidden `.git` folder exists in your directory
- No errors

**Time:** 5 minutes

---

### Exercise 4: Make Your First Commit
**Objective:** Create and commit a file to your repository.

**Steps:**
1. Create a Python file called `hello.py`:
   ```python
   # hello.py
   def greet(name):
       """Return a greeting message."""
       return f"Hello, {name}!"

   if __name__ == "__main__":
       print(greet("World"))
   ```

2. Run: `git status` (observe "Untracked files")
3. Run: `git add hello.py`
4. Run: `git status` (observe "Changes to be committed")
5. Run: `git commit -m "Add hello function with greeting logic"`
6. Run: `git log` to view your commit

**Success Criteria:**
- `git log` displays your commit with message
- `git status` shows "nothing to commit, working tree clean"

**Time:** 10 minutes

---

### Exercise 5: Practice Multiple Commits
**Objective:** Build commit muscle memory and practice good commit messages.

**Steps:**
1. Edit `hello.py` to add a second function:
   ```python
   def farewell(name):
       """Return a farewell message."""
       return f"Goodbye, {name}!"
   ```
2. Commit: `git add hello.py && git commit -m "Add farewell function"`
3. Edit again to add error handling to `greet()`:
   ```python
   def greet(name):
       """Return a greeting message."""
       if not name:
           raise ValueError("Name cannot be empty")
       return f"Hello, {name}!"
   ```
4. Commit: `git commit -am "Add validation to greet function"`
5. View history: `git log --oneline`

**Success Criteria:**
- `git log --oneline` shows 3 commits
- Each commit has a clear, descriptive message
- You can explain what changed in each commit

**Time:** 15 minutes

---

## Self-Assessment: 10 Questions

### 1. What are the three stages in Git's workflow?

<details>
<summary>Show Answer</summary>

**Working Directory** → **Staging Area** → **Repository**

The Working Directory is where you edit files. The Staging Area (index) is where you prepare changes with `git add`. The Repository is where commits are permanently stored.

</details>

---

### 2. What command initializes a new Git repository?

<details>
<summary>Show Answer</summary>

`git init`

This creates a hidden `.git` folder in your project directory that stores all version history.

</details>

---

### 3. How do you verify Git is installed on your system?

<details>
<summary>Show Answer</summary>

Run `git --version` in your terminal. A version number (e.g., "git version 2.42.0") confirms installation.

</details>

---

### 4. Interpret this `git status` output. What does it tell you?

```
On branch main
Changes not staged for commit:
  modified:   app.py

Untracked files:
  config.txt
```

<details>
<summary>Show Answer</summary>

- `app.py` has been modified but NOT staged (not yet ready to commit)
- `config.txt` is new and Git hasn't tracked it yet
- You need to run `git add` on both files before committing

</details>

---

### 5. What's the difference between `git add` and `git commit`?

<details>
<summary>Show Answer</summary>

**`git add`** moves files from Working Directory to Staging Area—it prepares changes but doesn't save them permanently.

**`git commit`** takes everything in the Staging Area and permanently saves it to the repository with a message describing the changes.

</details>

---

### 6. Which is a better commit message?

A) "update stuff"
B) "Add user authentication to login form"

<details>
<summary>Show Answer</summary>

**B** is much better.

**A** is vague—you won't know what changed months later.

**B** is specific, uses a clear action verb, and describes the work. Good commit messages help you and your team understand history.

</details>

---

### 7. When should you use AI attribution in a commit message?

<details>
<summary>Show Answer</summary>

When AI tools (Claude, Copilot, Gemini, etc.) generate or significantly contribute to your code. Use this format:

```
[AI] Claude - Add input validation for user email
```

This maintains transparency about how the code was created and helps with auditability.

</details>

---

### 8. What does "nothing to commit, working tree clean" mean?

<details>
<summary>Show Answer</summary>

All changes have been committed. Your Working Directory matches the last commit—there are no new files, modified files, or staged changes waiting to be saved. Your repository is in a clean state.

</details>

---

### 9. What command shows your commit history in a compact format?

<details>
<summary>Show Answer</summary>

`git log --oneline`

This displays each commit as a single line with its hash and message. Use `git log` (without flags) for full details including date and author.

</details>

---

### 10. You've just created a file called `notes.py`. What's the correct sequence of commands to save it to your repository?

<details>
<summary>Show Answer</summary>

1. `git add notes.py` (stage the file)
2. `git commit -m "Add notes module"` (commit with a message)

Verify with `git log` to see your commit. You could also use `git add .` to stage all changes at once.

</details>

---

## Wrapping Up: You've Got This

Congratulations—you've installed Git, configured your identity, and made your first commits. These foundations are **everything** you need to start tracking your code safely. You now understand how Git's three-stage workflow protects your work: changes live in your Working Directory until you deliberately stage and commit them, creating a permanent, reversible history.

Mistakes happen. Good commit messages help you find and understand what changed. AI attribution keeps your workflow transparent. Every commit is a checkpoint you can return to, so experiment confidently—you're now equipped to try new ideas without fear of losing your work.

In **Lesson 3: Safe Experimentation - Branches, Checkpoints, and Rollback**, you'll learn how to create isolated branches where you can test features, fix bugs, and collaborate without touching your main code. Branches turn Git from a history tool into a **safe sandbox** for innovation. You're ready for that next step.

Keep practicing these commands. The repetition will make them second nature, and before long, committing clean, intentional code will feel as natural as saving a document.
