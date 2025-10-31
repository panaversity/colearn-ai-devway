---
sidebar_position: 2
title: Installation, Authentication & First Steps
---

# Installation, Authentication & First Steps

## Learning Objectives

After completing this lesson, you'll be able to:

- **Install** Gemini CLI on Windows, macOS, or Linux using npm
- **Authenticate** with a Google account via OAuth
- **Verify** your installation and authentication status
- **Execute** your first Gemini CLI command successfully
- **Understand** free tier usage quotas and how to monitor them

**Estimated Time**: 25–35 minutes

---

## Pre-Installation Checklist

Before you begin, verify you have the prerequisites:

| Requirement | How to Check |
|-------------|-------------|
| **Node.js 16+** | Open terminal and run: `node --version` |
| **npm 7+** | Open terminal and run: `npm --version` |
| **Internet connection** | Required for installation and OAuth authentication |
| **Google account** | Need one for authentication (free account works) |

**Don't have Node.js?** Visit [nodejs.org](https://nodejs.org) and download the LTS version. The installation includes npm automatically.

**How to open a terminal:**
- **Windows**: Search "PowerShell" in the Start menu, or search "Command Prompt"
- **macOS**: Press Cmd+Space, type "Terminal", press Enter
- **Linux**: Use Ctrl+Alt+T (Ubuntu/Debian) or your distro's application menu

---

## Installation (Platform-Specific)

Choose your platform and follow the steps:

### Windows (PowerShell)

Open PowerShell and run:

```powershell
npm install -g @google/generative-ai-cli
```

**Alternative (Command Prompt):** If PowerShell isn't available, use Command Prompt instead—the command is identical.

### macOS

Open Terminal and run:

```bash
npm install -g @google/generative-ai-cli
```

**Alternative (Homebrew):** If you use Homebrew, you can alternatively install via `brew install gemini-cli` (if available in your Homebrew version).

### Linux (Ubuntu/Debian)

Open Terminal and run:

```bash
sudo npm install -g @google/generative-ai-cli
```

**Other distributions:** The `sudo npm install` command works on most Linux distributions. If you prefer not to use `sudo`, see [npm's global install guide](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally).

### Verify Installation

After installation completes (on any platform), verify it worked:

```bash
gemini --version
```

**Expected output:**
```
@google/generative-ai-cli/1.0.0
```

If you see the version number, installation succeeded. If you see "command not found," try closing and reopening your terminal, or check that npm installed correctly.

---

## Authentication

Gemini CLI uses **OAuth 2.0**, a secure authentication method where you log in through Google without sharing your password with the CLI tool.

### Step-by-Step: Authenticate

1. **Start the authentication process:**

   ```bash
   gemini auth login
   ```

2. **A browser window opens automatically.** Your default browser launches and shows a Google login screen.

3. **Log in with your Google account:**
   - Enter your email (or phone) associated with your Google account
   - Enter your password when prompted
   - Click "Allow" on the permission screen

4. **Return to your terminal.** Once you've authorized, the terminal displays a success message:

   ```
   Authentication successful!
   Credentials saved to: ~/.gemini/auth.json
   ```

### Verify Authentication

Check that your credentials are stored correctly:

```bash
gemini status
```

**Expected output:**
```
Status: Authenticated
User: your-email@gmail.com
Quota: 60 requests/minute, 1,000 requests/day
```

If you see "Authenticated," you're ready to use Gemini CLI.

---

## Understanding Quotas

The free tier of Gemini CLI has these limits:

| Limit | Value |
|-------|-------|
| **Requests per minute** | 60 |
| **Requests per day** | 1,000 |

**What does this mean in practice?**
- You can make 1 request per second continuously (60/min ÷ 60 sec = 1 req/sec)
- Over a full day (24 hours), you can make up to 1,000 requests total
- If you hit these limits, the CLI will pause briefly before allowing more requests

**Check your usage:**

```bash
gemini status
```

This shows your current quota and usage. For detailed quota information, visit the [Google AI Console](https://console.cloud.google.com/).

---

## Your First Command

Let's run your first Gemini CLI command to ensure everything works:

```bash
gemini generate "What is machine learning in one sentence?"
```

**Expected output:**
```
Machine learning is a type of artificial intelligence where computers learn patterns from data without being explicitly programmed for every scenario.
```

If you see a response from Gemini, congratulations—you're authenticated and ready to use Gemini CLI!

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"gemini: command not found"** | Close and reopen your terminal. If it still doesn't work, reinstall: `npm install -g @google/generative-ai-cli` |
| **"Authentication failed" or browser didn't open** | Try again: `gemini auth login`. If the browser still doesn't open, copy the URL from the terminal and paste it into your browser manually. |
| **"No quota available" error** | You've hit your daily limit of 1,000 requests. Wait until tomorrow (UTC midnight) for the quota to reset. |
| **npm: command not found** | Node.js/npm isn't installed or not in your PATH. Download from [nodejs.org](https://nodejs.org) and reinstall. |
| **Permission denied (Linux/macOS)** | Try with `sudo`: `sudo npm install -g @google/generative-ai-cli`. Or see [npm's permission guide](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally). |
| **Credentials expired** | Run `gemini auth login` again to refresh your authentication. |

---

## Practice Exercises

### Exercise 1: Verify Your Setup

Run all three verification commands and record the output:

```bash
gemini --version
gemini status
gemini generate "Hello, Gemini!"
```

**What to look for:** All three commands complete without errors. You should see:
- A version number from `--version`
- "Authenticated" status and your email from `status`
- A response from Gemini for your "Hello" message

### Exercise 2: Test Quota Limits

Make 5 consecutive requests as fast as you can:

```bash
for i in {1..5}; do gemini generate "Test request $i"; done
```

**What to observe:** All 5 requests complete successfully (you're well within the 60 req/min limit).

### Exercise 3: Try a Real Use Case

Ask Gemini CLI to help with a real task:

```bash
gemini generate "Give me 3 tips for learning Python faster"
```

**What to do:** Try different questions related to your learning goals. This exercise validates that the CLI responds to varied inputs and that you can use it for actual work.

---

## Checkpoint: Ready to Move Forward?

Before proceeding to the next lesson, confirm:

- [x] Gemini CLI is installed (`gemini --version` works)
- [x] You're authenticated (`gemini status` shows "Authenticated")
- [x] Free tier quotas understood (60 req/min, 1,000 req/day)
- [x] First command executed successfully (`gemini generate` returns a response)

If all checkboxes are true, you're ready for the next lesson: **Built-In Tools Deep Dive**.

---

## Key Takeaways

- **Installation is straightforward**: One `npm install` command, platform-agnostic
- **OAuth keeps you secure**: Your password never touches the CLI; you authenticate through Google's servers
- **Quotas are generous for learning**: 1,000 requests/day is plenty for tutorials and experimentation
- **Verification commands confirm success**: Use `gemini status` and `gemini generate` to test your setup

---

## What's Next?

In the next lesson, you'll learn:
- How to use Gemini CLI's built-in tools (file operations, web fetching, search grounding)
- Leveraging the 1 million token context window
- When to use Gemini CLI vs. other AI tools

See you there!
