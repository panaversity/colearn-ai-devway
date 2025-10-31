---
title: "Lesson 4: Pull Requests and Team Collaboration"
sidebar_position: 4
description: "Learn how to share AI-generated code with your team using pull requests, participate in code reviews, and merge changes safely after approval."
---

# Lesson 4: Pull Requests and Team Collaboration

## The Code Review That Saved Production

It's 3 PM on a Friday. Your teammate Marcus just finished a new user authentication feature. Claude Code helped him write it—500 lines of clean, well-structured code. He's tested it locally. Everything works. He's ready to merge it into the main branch and deploy to production.

But instead of merging immediately, Marcus creates a **pull request** and asks for your review.

You spend 15 minutes reading the code. It looks solid. The logic is clear. Tests are passing. Then you notice something subtle: the password reset tokens never expire. An attacker who intercepts a reset email could use it indefinitely—days, weeks, or months later.

You leave a comment: "Security issue: password reset tokens need expiration. Suggest 1-hour timeout."

Marcus revises the code. Claude Code helps him add token expiration with proper timestamp validation. He pushes the update. You review again. It's perfect now. You approve the pull request. Marcus merges to main.

**What just happened?**

A critical security vulnerability was caught before it reached production. Not because Marcus made a careless mistake—he didn't. The code looked correct. But **two pairs of eyes are better than one**, especially when reviewing AI-generated code that can look perfect but hide subtle issues.

This is the power of pull requests. They create a **mandatory checkpoint** where human judgment reviews AI-generated code before it becomes permanent. They turn collaboration from optional to automatic.

This lesson teaches you how to use GitHub's pull request system to share AI-generated code, review teammates' work, and merge safely after approval.

## Part I: Understanding Pull Requests

### What Is a Pull Request?

A **pull request (PR)** is a proposal to merge changes from one branch into another. It's called a "request" because you're asking: "I've made these changes—please review and approve them before merging."

**The pull request workflow:**

1. **Create a feature branch** and make your changes
2. **Push the branch to GitHub** so others can see it
3. **Open a pull request** describing what changed and why
4. **Team reviews the code**, leaving comments and questions
5. **You address feedback** by making additional commits
6. **Reviewer approves** when satisfied
7. **You merge** the PR into the main branch

### Why Pull Requests Matter for AI Development

AI tools like Claude Code and Gemini CLI can generate large amounts of code quickly. This speed is powerful, but it creates a risk: **fast code without careful review**.

Pull requests solve this by:

1. **Forcing human review** - No AI-generated code reaches production without approval
2. **Creating discussion space** - Team can ask questions, suggest improvements, identify bugs
3. **Building audit trail** - Clear record of who approved what, when, and why
4. **Catching mistakes early** - Issues found in review are 10x cheaper than issues found in production
5. **Knowledge sharing** - Team learns from each other's code and AI usage patterns

### Pull Requests vs. Direct Commits

| Without Pull Requests | With Pull Requests |
|----------------------|-------------------|
| Developer pushes directly to main | Developer creates PR for review |
| Code reaches production immediately | Code waits for approval |
| Mistakes discovered in production | Mistakes caught during review |
| No discussion or feedback loop | Team discusses changes before merge |
| Individual responsibility | Shared responsibility |
| Fast but risky | Slightly slower but much safer |

**Real-world practice:** Most professional teams **require pull requests** for all code changes. No one, not even senior developers, can push directly to main. This isn't about trust—it's about safety.

### The GitHub Pull Request Interface

When you open a pull request on GitHub, you'll see several tabs:

- **Conversation**: Discussion thread, status checks, merge button
- **Commits**: List of all commits in this PR
- **Files changed**: Diff view showing exactly what changed
- **Checks**: Automated tests, linters, security scans (if configured)

You'll also see:
- **PR title and description**: What changed and why
- **Comments**: Inline code comments and general discussion
- **Review status**: Approved, changes requested, or pending
- **Merge button**: Only appears when PR is approved (on protected branches)

## Part II: Creating a Pull Request

### Step 1: Create a Feature Branch

Before you can create a PR, you need a feature branch with your changes.

```bash
# Start on main branch
git checkout main

# Create and switch to feature branch
git checkout -b feature/add-user-dashboard

# Make your changes (with AI assistance or manually)
# Edit files, test locally

# Commit your changes
git add .
git commit -m "Add user dashboard with profile editing

Features implemented:
- User profile view with avatar and bio
- Inline editing with real-time validation
- Save/cancel functionality
- Responsive design for mobile

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Step 2: Push Your Branch to GitHub

GitHub needs to know about your branch before you can create a PR.

```bash
# First time pushing this branch
git push -u origin feature/add-user-dashboard

# Output:
# Enumerating objects: 8, done.
# To https://github.com/username/project.git
#  * [new branch]      feature/add-user-dashboard -> feature/add-user-dashboard
# Branch 'feature/add-user-dashboard' set up to track remote branch
```

**Note:** The `-u` flag (short for `--set-upstream`) tells Git to remember this connection. Future pushes on this branch can just use `git push`.

### Step 3: Open a Pull Request on GitHub

**Option A: Using GitHub Web UI**

1. Go to your repository on GitHub
2. You'll see a banner: "feature/add-user-dashboard had recent pushes"
3. Click **"Compare & pull request"**
4. Fill out the PR form (see next section)
5. Click **"Create pull request"**

**Option B: Using GitHub CLI (`gh`)**

```bash
# Create PR from command line
gh pr create --title "Add user dashboard with profile editing" --body "
## Summary
Adds a user dashboard page with profile editing capabilities.

## What Changed
- New dashboard.html with user profile layout
- JavaScript for inline editing and validation
- CSS for responsive design
- Tests for edit/save functionality

## Testing
- [x] Tested on Chrome, Firefox, Safari
- [x] Mobile responsive design verified
- [x] All validation rules working correctly
- [x] Save/cancel flow tested

## AI Collaboration
Generated initial component structure with Claude Code, then refined through iteration.
"

# Output:
# https://github.com/username/project/pull/123
```

### Step 4: Write a Great PR Description

Your PR description should answer:

1. **What changed?** (bullet points of changes)
2. **Why did you make these changes?** (problem being solved)
3. **How should reviewers test it?** (steps to verify it works)
4. **Any risks or concerns?** (potential issues to watch for)

**Good PR description template:**

```markdown
## Summary
Brief 1-2 sentence overview of what this PR does.

## What Changed
- Bullet point list of changes
- Keep it concise but specific
- Group related changes together

## Why These Changes
Explain the problem you're solving or feature you're adding.
Link to any related issues or discussions.

## How to Test
1. Step-by-step instructions for reviewers
2. Include any setup required
3. What the expected behavior is

## Screenshots (if UI changes)
[Attach images showing before/after]

## Checklist
- [ ] Tests passing locally
- [ ] Code follows project style guide
- [ ] Documentation updated (if needed)
- [ ] No sensitive data (API keys, passwords)

## AI Collaboration Note
Describe how AI tools were used (optional but recommended):
- "Initial implementation generated with Claude Code"
- "Claude Code suggested optimization patterns"
- "Gemini CLI helped with error handling logic"
```

**Example: Real PR Description**

```markdown
## Summary
Add password reset functionality with email-based token verification.

## What Changed
- New `/reset-password` endpoint with token generation
- Email template for password reset links
- Token validation with 1-hour expiration
- Tests for reset flow including expired tokens

## Why These Changes
Users currently have no way to recover accounts if they forget passwords.
This is a common support request (10+ tickets per week).

## How to Test
1. Run the app locally: `python app.py`
2. Navigate to `/forgot-password`
3. Enter email address: test@example.com
4. Check terminal for "email" with reset link
5. Click link, should show password reset form
6. Set new password, verify login works

Test expired token:
1. Generate reset token
2. Wait 2 hours (or modify expiration time in code)
3. Try to use token - should show "expired" error

## Security Considerations
⚠️ **Please review:** Token expiration logic in `auth.py` line 145.
Using SHA-256 for token generation with random salt.

## AI Collaboration Note
Initial implementation by Claude Code with specific prompt:
"Create password reset flow with email tokens, 1-hour expiration, secure random generation."

Iteration after testing revealed edge case with expired tokens - Claude Code helped refactor validation logic.
```

### Step 5: Request Reviewers

After creating the PR, assign reviewers:

**On GitHub web UI:**
1. Look for "Reviewers" section on right sidebar
2. Click gear icon and select teammates
3. They'll receive notification

**Using GitHub CLI:**
```bash
gh pr create --reviewer teammate1,teammate2
```

**Who should review?**
- Someone familiar with the codebase area
- Someone with security expertise (for auth/data handling)
- A senior developer (for architectural changes)
- At least one other person (minimum for most teams)

## Part III: Reviewing Code

### Your Role as a Code Reviewer

When reviewing a pull request, you're not looking for perfection—you're looking for:

1. **Correctness** - Does the code work? Are there bugs?
2. **Security** - Are there vulnerabilities or data leaks?
3. **Maintainability** - Is the code readable and well-structured?
4. **Test coverage** - Are there tests? Do they cover edge cases?
5. **AI-specific concerns** - Does AI-generated code handle errors properly?

### How to Review a Pull Request

**Step 1: Read the PR description**

Before looking at code, understand what the PR is supposed to do.

**Step 2: Check the "Files changed" tab**

GitHub shows a diff (difference) between the old code and new code:
- Green lines = added
- Red lines = removed
- Context lines = unchanged (shown for reference)

**Step 3: Read the code carefully**

Don't skim. Actually read the code. Ask yourself:
- Do I understand what this does?
- Are there edge cases not handled?
- Would I be comfortable maintaining this code?
- Does this match our project's patterns and style?

**Step 4: Leave comments**

Click the line number next to any line of code to leave a comment.

**Types of comments:**

**Blocking issue (must be fixed before merge):**
```
🚨 **Security issue**: Password reset tokens don't expire.

An attacker who intercepts a reset email can use it indefinitely.

Suggestion: Add 1-hour expiration with timestamp validation.
```

**Suggestion (nice to have, not required):**
```
💡 Consider using a constant for this magic number.

Instead of:
  if len(password) < 8:

Consider:
  MIN_PASSWORD_LENGTH = 8
  if len(password) < MIN_PASSWORD_LENGTH:

This makes it easier to change the requirement later.
```

**Question (need clarification):**
```
❓ Why are we using `time.sleep(1)` here?

Is this to prevent rate limiting, or is there another reason?
```

**Praise (good work deserves recognition):**
```
✅ Nice! Using a constant-time comparison for password checking prevents timing attacks.
```

### What to Look For in AI-Generated Code

AI tools like Claude Code produce generally good code, but they have blind spots:

| Common AI Issues | What to Check |
|-----------------|---------------|
| **Security gaps** | Input validation, SQL injection, XSS, token expiration |
| **Error handling** | What happens on network failure, invalid input, edge cases? |
| **Performance** | Unnecessary loops, database queries in loops, memory leaks |
| **Edge cases** | Empty inputs, null values, negative numbers, very large inputs |
| **Hardcoded values** | API keys, passwords, configuration should be in env vars |
| **Over-engineering** | AI sometimes adds complexity where simplicity works better |
| **Deprecated patterns** | AI training data may include outdated libraries or methods |

### Example: Reviewing AI-Generated Authentication Code

**Pull request:** "Add OAuth login with GitHub"

**Code in PR:**

```python
@app.route('/auth/github')
def github_login():
    client_id = "abc123secretclientid"  # 🚨 Issue #1
    redirect_uri = "http://localhost:5000/callback"
    return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}")

@app.route('/auth/callback')
def github_callback():
    code = request.args.get('code')  # 🚨 Issue #2
    # Exchange code for access token
    response = requests.post('https://github.com/login/oauth/access_token', data={
        'client_id': client_id,
        'client_secret': "xyz789secret",  # 🚨 Issue #3
        'code': code
    })
    token = response.json()['access_token']  # 🚨 Issue #4
    return f"Logged in with token: {token}"  # 🚨 Issue #5
```

**Your review comments:**

```
🚨 **Line 3: Security Issue - Hardcoded Secret**
Client ID should be in environment variables, not hardcoded.

Suggestion:
  client_id = os.environ.get('GITHUB_CLIENT_ID')

---

🚨 **Line 9: Missing Error Handling**
What happens if the user declines authorization? `code` will be None.

Add validation:
  if not code:
      return "Authorization failed", 400

---

🚨 **Line 13: Exposed Secret**
Never hardcode client secrets! This is a critical security issue.

Use environment variables:
  client_secret = os.environ.get('GITHUB_CLIENT_SECRET')

---

🚨 **Line 17: Unsafe Access**
If the response is an error, `access_token` key won't exist. This will crash.

Add error checking:
  token_data = response.json()
  if 'access_token' not in token_data:
      return "Failed to get access token", 500
  token = token_data['access_token']

---

🚨 **Line 18: Security Issue - Token Exposure**
Never display access tokens to users! This defeats the purpose of OAuth.

Store token in session, don't display it:
  session['github_token'] = token
  return redirect('/dashboard')
```

**Summary comment:**

```
Overall approach is correct, but there are 5 security issues that must be fixed before merging:

1. Hardcoded client ID → use environment variable
2. Missing validation for authorization failure
3. Hardcoded client secret → use environment variable
4. No error handling for API response
5. Token exposed to user → store in session instead

These are common issues with AI-generated OAuth code. Once fixed, the logic is solid.

**Request:** Please fix these issues and I'll re-review.
```

### The "Approve, Request Changes, Comment" Decision

When you finish reviewing, you choose one of three actions:

**1. Approve** ✅
- Code is good to merge
- No blocking issues
- Minor suggestions can be addressed later

**2. Request Changes** ❌
- Blocking issues must be fixed before merge
- Security vulnerabilities
- Broken functionality
- Major architectural concerns

**3. Comment** 💬
- You have questions or suggestions
- Not ready to approve yet, but no blocking issues
- Waiting for discussion before making decision

**When to approve AI-generated code:**

✅ **Approve when:**
- You understand what the code does
- Tests are passing
- No security issues
- Error handling is present
- Edge cases are handled
- Code is maintainable

❌ **Request changes when:**
- Security vulnerabilities present
- Functionality doesn't work as described
- No error handling for critical paths
- Hardcoded secrets or sensitive data
- Major performance issues
- Code is incomprehensible or unmaintainable

## Part IV: Iteration and Feedback

### Responding to Review Comments

When your PR receives review comments, your job is to:

1. **Read all feedback carefully** - Don't skim
2. **Ask questions if unclear** - "What did you mean by...?"
3. **Fix blocking issues** - Address all security and functionality concerns
4. **Consider suggestions** - Even non-blocking suggestions can improve code
5. **Push updates** - New commits automatically update the PR
6. **Respond to each comment** - Let reviewers know what you did

### Making Changes to a PR

```bash
# Your PR is open and has review comments
# You're still on your feature branch

# Make the requested changes
# Edit files based on feedback

# Commit the changes
git add .
git commit -m "Address review feedback: add token expiration and error handling

Changes based on @reviewer's comments:
- Add 1-hour expiration to password reset tokens
- Add error handling for missing 'code' parameter
- Move secrets to environment variables
- Add tests for expired token edge case

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Push to the same branch
git push

# The PR is automatically updated on GitHub
```

**Important:** Don't create a new PR. Just push to the existing branch. GitHub automatically updates the PR with your new commits.

### Responding to Comments on GitHub

For each review comment, click "Reply" and explain what you did:

**Example responses:**

**For fixed issues:**
```
✅ Fixed in commit abc123.

Added 1-hour expiration with `datetime.now() + timedelta(hours=1)`.
Also added test to verify expired tokens are rejected.
```

**For questions:**
```
Good question! The `time.sleep(1)` is to prevent brute-force attacks.

Without it, an attacker could try thousands of passwords per second.
The 1-second delay limits them to 1 attempt per second per connection.

Alternative: We could use a rate limiter library (e.g., Flask-Limiter).
Would you prefer that approach?
```

**For suggestions you're deferring:**
```
Great suggestion! I agree this would be better as a constant.

For this PR, I'm keeping the current implementation to minimize scope.
I'll create a follow-up issue (#456) to refactor magic numbers across the auth module.

Is that acceptable, or would you prefer I fix it now?
```

### The Iteration Loop

Pull request review is often iterative:

1. **Developer creates PR**
2. **Reviewer finds issues**
3. **Developer fixes issues, pushes updates**
4. **Reviewer checks fixes, finds more issues (or approves)**
5. **Repeat until approved**

This is normal and healthy. Good code often requires 2-3 review rounds.

**Don't take feedback personally.** Reviewers are helping you catch bugs and improve code quality. Every issue found in review is an issue that won't hit production.

## Part V: Merging on GitHub

### When to Merge

A pull request is ready to merge when:

✅ All reviewers have approved
✅ All CI checks are passing (if configured)
✅ No unresolved conversations
✅ Branch is up to date with main (no conflicts)
✅ No blockers or concerns raised

### How to Merge

**On GitHub web UI:**

1. Scroll to bottom of PR conversation tab
2. Click green **"Merge pull request"** button
3. Choose merge strategy (usually "Create a merge commit")
4. Optionally edit merge commit message
5. Click **"Confirm merge"**
6. Optionally click **"Delete branch"** (cleanup)

**Using GitHub CLI:**

```bash
# Merge the PR
gh pr merge 123 --merge

# Or merge and delete branch
gh pr merge 123 --merge --delete-branch
```

### Merge Strategies

GitHub offers three merge strategies:

#### 1. Create a Merge Commit (default)

```
main:     A -- B ------- M
                \       /
feature:         C -- D
```

- Preserves full history with merge commit
- Shows feature branch existed
- Easy to see what was merged together
- **Use when:** Default choice for most teams

#### 2. Squash and Merge

```
main:     A -- B -- S
                    (S contains all changes from C + D)
```

- Combines all PR commits into one commit
- Cleaner history (one commit per feature)
- Loses individual commit details
- **Use when:** PR has many messy commits or work-in-progress commits

#### 3. Rebase and Merge

```
main:     A -- B -- C' -- D'
(C' and D' are rebased versions of C and D)
```

- Rewrites commits to appear sequential
- Linear history (no merge commits)
- Can be confusing if conflicts occur
- **Use when:** Team wants linear history

**Most teams use "Create a merge commit"** as default. It's the safest and most transparent option.

### After Merging

**Good practices:**

1. **Delete the feature branch** (cleanup)
```bash
git branch -d feature/add-user-dashboard
```

2. **Update your local main**
```bash
git checkout main
git pull origin main
```

3. **Verify the merge** (check that changes are in main)

4. **Close related issues** (if PR resolves an issue)

5. **Thank your reviewers** (appreciation builds team culture)

### What If You Need to Undo a Merge?

If you merged something that breaks production:

**Option 1: Revert the merge commit**
```bash
# Identify the merge commit
git log --oneline
# abc123 Merge pull request #456

# Revert it
git revert abc123 -m 1

# Push the revert
git push origin main
```

**Option 2: Create a new PR to fix it**
- Faster than reverting if fix is simple
- Preserves history of what happened

**Option 3: Roll back deployment**
- If using deployment system with rollback
- Buys time to fix properly

## Part VI: Handling PR Conflicts

### What Causes PR Conflicts?

A PR conflict occurs when:

1. You created your feature branch from main
2. You made changes to file X
3. Someone else merged different changes to file X into main
4. Now your PR can't merge automatically

**Example timeline:**

```
Day 1: You create feature branch from main, edit auth.py
Day 2: Teammate merges different auth.py changes to main
Day 3: You try to merge your PR → CONFLICT
```

### Detecting PR Conflicts

GitHub shows a warning on the PR:

```
⚠️ This branch has conflicts that must be resolved
   before merging.
```

You'll also see which files have conflicts.

### Resolving PR Conflicts

**Step 1: Update your local main**

```bash
git checkout main
git pull origin main
```

**Step 2: Switch to your feature branch**

```bash
git checkout feature/add-user-dashboard
```

**Step 3: Merge main into your feature branch**

```bash
git merge main

# Output:
# Auto-merging auth.py
# CONFLICT (content): Merge conflict in auth.py
# Automatic merge failed; fix conflicts and then commit the result.
```

**Step 4: Open conflicted files and resolve**

(Same process as Lesson 3 merge conflicts)

```python
<<<<<<< HEAD (your changes)
def login(username, password):
    return authenticate_with_ldap(username, password)
=======
def login(username, password):  (changes from main)
    return authenticate_with_oauth(username, password)
>>>>>>> main
```

Choose the correct version or combine both.

**Step 5: Mark as resolved and commit**

```bash
git add auth.py
git commit -m "Resolve merge conflict with main

Conflict in auth.py login function:
- Main branch added OAuth support
- My branch added LDAP support
- Resolution: Keep OAuth (main's approach), will add LDAP in follow-up PR

Discussed with team in PR comments."

# Push the resolution
git push
```

**Step 6: PR is now mergeable**

GitHub will update the PR status: "This branch has no conflicts with the base branch."

### Preventing PR Conflicts

1. **Merge main into your branch frequently**
```bash
# While working on feature
git checkout feature/my-work
git merge main  # Stay up to date
```

2. **Keep PRs small and focused**
- Smaller PRs merge faster
- Less time for conflicts to develop

3. **Communicate with team**
- "I'm working on auth.py this week"
- Coordinate to avoid simultaneous edits

4. **Merge approved PRs quickly**
- Don't let approved PRs sit for days
- They create conflicts for other PRs

## Practice Exercises

### Exercise 1: Create Your First Pull Request

**Objective:** Create a repository on GitHub, make changes locally, and open a pull request.

**Steps:**

1. **Create a repository on GitHub:**
   - Go to GitHub.com, click "New repository"
   - Name: `pr-practice`
   - Public or Private
   - Initialize with README
   - Click "Create repository"

2. **Clone it locally:**
```bash
git clone https://github.com/YOUR_USERNAME/pr-practice.git
cd pr-practice
```

3. **Create a feature branch:**
```bash
git checkout -b feature/add-greeting
```

4. **Create a Python file:**
```python
# greeting.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

5. **Commit and push:**
```bash
git add greeting.py
git commit -m "Add greeting function

Simple greeting utility for testing PR workflow.

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

git push -u origin feature/add-greeting
```

6. **Open a PR on GitHub:**
   - Go to your repository on GitHub
   - Click "Compare & pull request"
   - Fill in title: "Add greeting function"
   - Fill in description:
   ```markdown
   ## Summary
   Adds a simple greeting function for PR practice.

   ## What Changed
   - New `greeting.py` with `greet()` function
   - Returns personalized greeting message

   ## Testing
   Run: `python greeting.py`
   Expected: "Hello, World!"
   ```
   - Click "Create pull request"

7. **Verify the PR exists** on GitHub.

💡 **Learning with AI**: Ask Claude Code:
- "What information should I include in a PR description?"
- "How do I know if my PR is ready to merge?"

<details>
<summary>Show Answer</summary>

**Success criteria:**
- ✅ Repository created on GitHub
- ✅ Feature branch created locally
- ✅ Commit made with meaningful message
- ✅ Branch pushed to GitHub
- ✅ Pull request opened with description

**Verification:**
Go to `https://github.com/YOUR_USERNAME/pr-practice/pulls` and see your PR listed.

</details>

---

### Exercise 2: Review a Pull Request (Simulated)

**Objective:** Practice reviewing code by examining a simulated PR scenario.

**Scenario:** Your teammate created a PR with this code:

```python
# File: user_profile.py
import requests

def get_user_profile(user_id):
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)
    data = response.json()
    return data['profile']
```

**Your task:** Write a review comment identifying issues and suggesting improvements.

**Hints:**
- What happens if `user_id` is None?
- What if the API request fails?
- What if `response.json()` fails?
- What if `data['profile']` doesn't exist?

💡 **Learning with AI**: Ask Claude Code:
- "What edge cases should I check for in API calling code?"
- "What's the best way to handle network errors in Python?"

⚠️ **Important**: Try finding issues yourself before asking AI!

<details>
<summary>Show Answer</summary>

**Review comment:**

```
🚨 **Multiple issues need to be addressed:**

**1. Missing input validation (Line 4):**
What if `user_id` is None or empty? This will create an invalid URL.

Suggestion:
  if not user_id:
      raise ValueError("user_id is required")

**2. No error handling for network failures (Line 5):**
If the API is down or network fails, this will crash with an exception.

Suggestion:
  try:
      response = requests.get(url, timeout=5)
      response.raise_for_status()  # Raises exception for 4xx/5xx
  except requests.RequestException as e:
      # Handle error appropriately
      return None  # or raise custom exception

**3. Unsafe JSON parsing (Line 6):**
If response isn't valid JSON, this will crash.

Suggestion:
  try:
      data = response.json()
  except ValueError:
      # Handle invalid JSON
      return None

**4. Missing key check (Line 7):**
If API response doesn't have 'profile' key, this will crash with KeyError.

Suggestion:
  if 'profile' not in data:
      return None
  return data['profile']

**Summary:**
The core logic is correct, but error handling is missing. This code will crash on edge cases. Please add validation and error handling.
```

</details>

---

### Exercise 3: Address Review Feedback

**Objective:** Make changes based on review comments and push updates to your PR.

**Steps:**

1. **Use the PR from Exercise 1** (or create a new one).

2. **Simulate a review comment:** Imagine reviewer said:
   ```
   💡 The greeting is nice, but could you add support for different languages?

   Suggestion:
   greet(name, language="en")

   Where language can be "en", "es", or "fr".
   ```

3. **Make the changes locally:**
```python
# greeting.py
def greet(name, language="en"):
    greetings = {
        "en": f"Hello, {name}!",
        "es": f"¡Hola, {name}!",
        "fr": f"Bonjour, {name}!"
    }
    return greetings.get(language, greetings["en"])

if __name__ == "__main__":
    print(greet("World", "en"))
    print(greet("World", "es"))
    print(greet("World", "fr"))
```

4. **Commit and push:**
```bash
git add greeting.py
git commit -m "Add multilingual support based on review feedback

Added language parameter with en/es/fr support.

Addresses review comment: @reviewer suggestion for i18n.

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

git push
```

5. **Verify on GitHub:** Your PR automatically updates with the new commit.

6. **Reply to the review comment on GitHub:**
   ```
   ✅ Implemented in commit [abc123].

   Added support for English, Spanish, and French greetings.
   Default is English if language not specified or not supported.
   ```

💡 **Learning with AI**: Ask Claude Code:
- "How do I respond professionally to review comments?"
- "Should I create a new PR or update the existing one?"

<details>
<summary>Show Answer</summary>

**Key points:**
- ✅ Don't create a new PR—push to the existing branch
- ✅ Address all review comments, even suggestions
- ✅ Reply to each comment explaining what you did
- ✅ Commit messages should reference the feedback

**Verification:**
Check your PR on GitHub—it should show 2 commits now (original + feedback response).

</details>

---

### Exercise 4: Merge a Pull Request

**Objective:** Complete the PR workflow by merging an approved PR.

**Steps:**

1. **Use your PR from previous exercises.**

2. **If it's not approved yet:** Self-approve it (normally someone else approves, but for practice you can approve your own PR in personal repos).

3. **Merge the PR on GitHub:**
   - Go to your PR page
   - Scroll to bottom
   - Click "Merge pull request"
   - Click "Confirm merge"
   - Click "Delete branch" (cleanup)

4. **Update your local repository:**
```bash
git checkout main
git pull origin main
```

5. **Verify the changes are in main:**
```bash
cat greeting.py  # Should show the multilingual version
```

6. **Delete local feature branch:**
```bash
git branch -d feature/add-greeting
```

💡 **Learning with AI**: Ask Claude Code:
- "What happens to my feature branch after merging?"
- "Why should I delete branches after merging?"

<details>
<summary>Show Answer</summary>

**Complete workflow:**

```bash
# After PR is merged on GitHub

# 1. Switch to main
git checkout main

# 2. Pull latest changes
git pull origin main

# 3. Verify merge
cat greeting.py  # Changes are present

# 4. Clean up local branch
git branch -d feature/add-greeting

# 5. Verify branches
git branch
# Output: * main (only main remains)
```

**Result:**
- ✅ PR merged into main
- ✅ Changes are in main branch
- ✅ Feature branch deleted (both on GitHub and locally)
- ✅ Clean state, ready for next feature

</details>

---

### Exercise 5: Resolve a PR Conflict

**Objective:** Practice resolving conflicts when your PR can't auto-merge.

**Steps:**

1. **Create a new test repository** (or use existing).

2. **Create `config.py` on main:**
```python
# config.py
DEBUG = False
API_URL = "https://api.production.com"
```

3. **Commit and push:**
```bash
git add config.py
git commit -m "Add initial config"
git push origin main
```

4. **Create a feature branch and modify config:**
```bash
git checkout -b feature/staging-config
```

Edit `config.py`:
```python
# config.py
DEBUG = True
API_URL = "https://api.staging.com"
LOG_LEVEL = "DEBUG"  # New line
```

5. **Commit and push feature branch:**
```bash
git add config.py
git commit -m "Add staging configuration"
git push -u origin feature/staging-config
```

6. **Open a PR** on GitHub (don't merge yet).

7. **Switch back to main and make DIFFERENT changes:**
```bash
git checkout main
```

Edit `config.py`:
```python
# config.py
DEBUG = False
API_URL = "https://api.newproduction.com"  # Changed URL
TIMEOUT = 30  # New line
```

8. **Commit and push to main:**
```bash
git add config.py
git commit -m "Update production config"
git push origin main
```

9. **Check your PR on GitHub:** It should now show conflicts.

10. **Resolve the conflict locally:**
```bash
git checkout feature/staging-config
git merge main

# CONFLICT in config.py
```

11. **Open `config.py` and resolve:**
```python
# config.py
DEBUG = True
API_URL = "https://api.staging.com"
LOG_LEVEL = "DEBUG"
TIMEOUT = 30  # Keep from main
```

12. **Complete the merge:**
```bash
git add config.py
git commit -m "Resolve conflict with main: combine staging config and timeout"
git push
```

13. **Check PR on GitHub:** Conflicts should be resolved.

14. **Merge the PR.**

💡 **Learning with AI**: Ask Claude Code:
- "I have a conflict in this file: [paste conflict]. How should I resolve it?"
- "How can I prevent PR conflicts in team projects?"

<details>
<summary>Show Answer</summary>

**Conflict resolution workflow:**

```bash
# When PR shows conflicts

# 1. Update local main
git checkout main
git pull origin main

# 2. Switch to feature branch
git checkout feature/staging-config

# 3. Merge main into feature
git merge main
# CONFLICT appears

# 4. Open conflicted file
# Resolve by combining changes logically

# 5. Mark resolved
git add config.py
git commit -m "Resolve merge conflict with main"

# 6. Push resolution
git push

# PR is now mergeable on GitHub
```

**Key lesson:** Conflicts aren't scary. They just mean two people edited the same code. You decide which changes to keep.

</details>

---

### Exercise 6: Create a Pull Request with Multiple Commits

**Objective:** Practice the realistic scenario of multiple commits in one PR.

**Steps:**

1. **Create a new feature branch:**
```bash
git checkout -b feature/calculator
```

2. **Create initial `calculator.py`:**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

3. **Commit:**
```bash
git add calculator.py
git commit -m "Add basic arithmetic operations (add, subtract)"
```

4. **Add more functions:**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

5. **Commit:**
```bash
git add calculator.py
git commit -m "Add multiply and divide with zero-check"
```

6. **Add tests:**
```python
# test_calculator.py
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        assert True
```

7. **Commit:**
```bash
git add test_calculator.py
git commit -m "Add comprehensive tests for all operations"
```

8. **Push and create PR:**
```bash
git push -u origin feature/calculator
# Open PR on GitHub
```

9. **Verify on GitHub:** PR should show 3 commits in the "Commits" tab.

💡 **Learning with AI**: Ask Claude Code:
- "Should I squash multiple commits before creating a PR?"
- "What makes a good commit history in a PR?"

<details>
<summary>Show Answer</summary>

**PR with multiple commits is fine:**

Each commit represents a logical unit of work:
1. Basic operations (foundation)
2. Advanced operations with error handling (extension)
3. Tests (quality assurance)

This makes the PR easy to review—reviewer can see the progression of work.

**When to squash:**
- If commits are messy ("WIP", "fix typo", "fix again")
- If commits don't represent logical units
- If team prefers one commit per PR

**When to keep multiple commits:**
- Each commit is meaningful and complete
- Commits tell a story of development
- Easier to review in smaller pieces

**Both approaches are valid—follow your team's preference.**

</details>

---

### Exercise 7: Complete Pull Request Workflow

**Objective:** Combine all skills into one complete realistic PR workflow.

**Scenario:** You're adding a user registration feature to a web app.

**Steps:**

1. **Create feature branch:**
```bash
git checkout main
git pull origin main
git checkout -b feature/user-registration
```

2. **Create `registration.py`:**
```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not any(c.isupper() for c in password):
        return False, "Password must contain uppercase letter"
    if not any(c.isdigit() for c in password):
        return False, "Password must contain a digit"
    return True, "Password is valid"

def register_user(email, password):
    if not validate_email(email):
        return {"success": False, "error": "Invalid email format"}

    valid, message = validate_password(password)
    if not valid:
        return {"success": False, "error": message}

    # TODO: Actually save user to database
    return {"success": True, "message": f"User {email} registered"}
```

3. **Commit:**
```bash
git add registration.py
git commit -m "Add user registration with email and password validation

Features:
- Email format validation with regex
- Password strength validation (length, uppercase, digit)
- Registration logic with error handling

TODO: Database integration in follow-up PR

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

4. **Push and create PR:**
```bash
git push -u origin feature/user-registration
gh pr create --title "Add user registration feature" --body "
## Summary
Implements user registration with validation.

## What Changed
- Email format validation
- Password strength requirements (8+ chars, uppercase, digit)
- Registration function with error handling

## Testing
\`\`\`python
from registration import register_user

# Valid registration
print(register_user('user@example.com', 'Password123'))

# Invalid email
print(register_user('invalid-email', 'Password123'))

# Weak password
print(register_user('user@example.com', 'weak'))
\`\`\`

## Next Steps
- Database integration (follow-up PR)
- Email confirmation flow (follow-up PR)

## AI Collaboration
Generated with Claude Code, then refined validation logic through testing.
"
```

5. **Simulate review feedback:** Reviewer comments:
   ```
   💡 Consider adding a check for special characters in password validation.

   More secure passwords include symbols like !@#$%
   ```

6. **Address feedback:**
```python
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not any(c.isupper() for c in password):
        return False, "Password must contain uppercase letter"
    if not any(c.isdigit() for c in password):
        return False, "Password must contain a digit"
    if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password):
        return False, "Password must contain a special character"
    return True, "Password is valid"
```

7. **Commit and push update:**
```bash
git add registration.py
git commit -m "Add special character requirement to password validation

Addresses review feedback from @reviewer.

Passwords now require at least one special character for improved security.

🤖 Generated with Claude Code"
git push
```

8. **Reply to review comment:**
   ```
   ✅ Implemented in commit [abc123].

   Added check for special characters: !@#$%^&*()_+-=[]{}|;:,.<>?
   Updated validation message accordingly.
   ```

9. **Get approval and merge the PR.**

10. **Clean up:**
```bash
git checkout main
git pull origin main
git branch -d feature/user-registration
```

💡 **Learning with AI**: Ask Claude Code after completing:
- "Review this PR workflow—did I follow best practices?"
- "What could I improve in my PR description?"

<details>
<summary>Show Answer</summary>

**Complete PR workflow checklist:**

✅ **Planning:**
- Created feature branch from updated main
- Made logical, focused changes

✅ **Implementation:**
- Clear, well-structured code
- Meaningful commit messages
- AI attribution included

✅ **PR Creation:**
- Descriptive title
- Detailed PR description with testing instructions
- Clear about what's in scope / out of scope

✅ **Review Process:**
- Addressed reviewer feedback
- Made requested improvements
- Replied to comments explaining changes

✅ **Merge & Cleanup:**
- Got approval before merging
- Merged on GitHub
- Updated local main
- Deleted feature branch

**This is the complete professional PR workflow used in real teams.**

</details>

---

## Self-Assessment

Test your understanding with these questions:

1. **What is the main purpose of a pull request?**
   - A) To backup code to GitHub
   - B) To request code review before merging changes
   - C) To create a new branch
   - D) To delete old code

2. **When should you create a pull request?**
   - A) Before writing any code
   - B) After completing and testing your feature on a branch
   - C) Only when code is perfect
   - D) Once a month

3. **What information should a PR description include?**
   - A) Only the title
   - B) A summary of what changed and why, plus testing instructions
   - C) The full code diff
   - D) Personal information about the developer

4. **When reviewing a PR, what should you check for in AI-generated code?**
   - A) Only syntax errors
   - B) Security issues, error handling, edge cases, hardcoded secrets
   - C) Only performance issues
   - D) Nothing—AI code is always perfect

5. **What does "Request Changes" mean in a PR review?**
   - A) The code is perfect
   - B) There are blocking issues that must be fixed before merge
   - C) You don't understand the code
   - D) The PR should be closed

6. **How do you update a PR after receiving review comments?**
   - A) Create a new PR
   - B) Make changes, commit, and push to the same branch
   - C) Email the changes to reviewers
   - D) Delete the PR and start over

7. **What causes a PR merge conflict?**
   - A) The PR is too large
   - B) Both your branch and main modified the same lines of code
   - C) The PR title is wrong
   - D) Too many commits

8. **How do you resolve a PR conflict?**
   - A) Delete your PR
   - B) Merge main into your branch, resolve conflicts, commit, push
   - C) Ask GitHub support
   - D) Wait for the conflict to resolve itself

9. **What should you do after merging a PR?**
   - A) Nothing
   - B) Delete the feature branch and update local main
   - C) Create another PR immediately
   - D) Revert the merge

10. **Which merge strategy preserves full commit history with a merge commit?**
    - A) Squash and merge
    - B) Rebase and merge
    - C) Create a merge commit
    - D) Fast-forward merge

<details>
<summary>Show Answers</summary>

1. **B** - To request code review before merging changes (core purpose of PRs)
2. **B** - After completing and testing your feature on a branch
3. **B** - A summary of what changed and why, plus testing instructions (helps reviewers)
4. **B** - Security issues, error handling, edge cases, hardcoded secrets (common AI issues)
5. **B** - There are blocking issues that must be fixed before merge
6. **B** - Make changes, commit, and push to the same branch (PR auto-updates)
7. **B** - Both your branch and main modified the same lines of code
8. **B** - Merge main into your branch, resolve conflicts, commit, push
9. **B** - Delete the feature branch and update local main (cleanup)
10. **C** - Create a merge commit (default strategy, preserves full history)

**Scoring:**
- 9-10: Excellent! You understand PR workflows
- 7-8: Good! Review conflict resolution and review processes
- 5-6: Needs work—practice the exercises again
- Below 5: Review this lesson thoroughly and practice all exercises

</details>

---

## Reflection and Forward Bridge

### Pause and Reflect

**Reflection 1: How does requiring pull requests change the safety of AI-generated code?**

Without PRs, AI-generated code goes straight to production. One person's judgment (and AI's blind spots) is all that stands between a bug and your users. With PRs, at least two people review every change. Issues are caught before they cause damage.

**Reflection 2: Think about code you've written in the past. What would a reviewer have caught that you missed?**

We all have blind spots. We focus on making code work and miss security issues, edge cases, or maintainability concerns. A reviewer brings fresh eyes and asks questions we didn't think to ask ourselves.

**Reflection 3: How can you be a helpful code reviewer without being discouraging?**

Balance finding issues with recognizing good work. Frame feedback as questions or suggestions, not commands. Explain *why* something is an issue, not just *that* it's wrong. Remember: the goal is better code, not proving you're smarter.

---

## What You've Mastered

You now understand the complete pull request workflow:

✅ **Creating PRs** - Branch, push, open PR with clear description
✅ **Writing PR descriptions** - What changed, why, how to test
✅ **Reviewing code** - Spotting issues, leaving constructive feedback
✅ **Iteration** - Addressing feedback, pushing updates
✅ **Merging** - Completing the workflow safely
✅ **Conflict resolution** - Handling when branches diverge

These skills make you a **collaborative developer**. You can work on a team, share AI-generated code safely, and participate in code review that catches bugs before production.

---

## What's Next

**Next lesson (Lesson 5):** You'll learn how to use **natural language prompts** with Claude Code or Gemini CLI to execute Git operations without memorizing complex commands.

Instead of:
```bash
git rebase -i --autosquash HEAD~5
```

You'll say:
```
"Clean up the last 5 commits into logical groups"
```

This final lesson brings everything together—you'll understand *what* Git does (Lessons 1-4) and use AI to handle *how* to do it (Lesson 5).

You're building a complete Git mastery toolkit that combines human understanding with AI assistance. Let's complete your Git journey.
