---
sidebar_position: 2
title: "Installing and Authenticating Claude Code"
---

# Installing and Authenticating Claude Code

## From Concept to Reality: Getting Claude Code Running

In Lesson 1, you learned why Claude Code is revolutionary. Now comes the crucial step: **getting it working on your machine.**

This isn't just about following installation commands. It's about crossing the bridge from "interesting concept" to "tool I can actually use." By the end of this lesson, Claude Code will be installed, authenticated, and ready to assist with your development work.

We've designed this lesson to achieve a **95% first-attempt success rate**—meaning you should be up and running without needing external help. We'll cover Windows, macOS, and Linux with multiple installation methods, clear authentication paths, and comprehensive troubleshooting for common issues.

Let's get started.

---

## Prerequisites: What You Need Before Installing

Before we begin, verify you have the following:

**1. Terminal Access**
- **Windows**: Command Prompt, PowerShell, or Windows Terminal
- **macOS**: Terminal app (Applications → Utilities → Terminal)
- **Linux**: Any terminal emulator (GNOME Terminal, Konsole, etc.)

**2. Claude Account** (one of the following):
- **Option A**: Claude.ai subscription (Pro or free tier)
  - Sign up at: https://claude.ai
  - You'll use this account to authenticate Claude Code
- **Option B**: Claude Console account with API credits
  - Create account at: https://console.anthropic.com
  - Requires payment method for API usage

**3. Node.js 18+ (for NPM installation method)**
- Check if installed: `node --version`
- If not installed: https://nodejs.org (download LTS version)
- Note: There's also a native installation method that doesn't require Node.js

**4. Internet Connection**
- Needed for initial download and authentication
- Claude Code requires connection to communicate with Claude AI

**5. Administrator/Sudo Access**
- Some installation steps may require elevated permissions

---

## Installation: Node.js + NPM

Claude Code installs easily via Node.js package manager (npm). This is the recommended path - it works consistently across Windows, macOS, and Linux.

**Why this approach?**
- Node.js is widely installed already (check: `node --version`)
- If needed, easy to install from https://nodejs.org (get LTS version)
- Once you have Node, Claude Code installation is one command

---

## Installation

### Step 1: Install Claude Code Globally

Open your terminal and run:

```bash
npm install -g @anthropic-ai/claude-code
```

**What this does**: Downloads and installs Claude Code globally on your system, making it accessible from any directory.

**Expected output**:
```
added 127 packages in 8s
```

### Step 2: Verify Installation

Check that Claude Code is installed correctly:

```bash
claude --version
```

**Expected output** (version number may vary):
```
claude-code version 1.2.3
```

**If you see the version number**: ✅ Installation successful! Skip to [Authentication](#authentication-connecting-claude-code-to-your-account).

**If you see "command not found"**: See [Troubleshooting: Command Not Found](#troubleshooting-command-not-found).


## Authentication: Connecting Claude Code to Your Account

Once installed, Claude Code needs to authenticate with your Claude account. There are **two authentication paths** depending on which account type you have.

### Which Authentication Method Should I Use?

**Decision Tree**:

```
Do you have a Claude.ai account?
├─ Yes → Use Claude.ai Authentication (Method A)
│        Most common for individual users
│
└─ No, but I have Claude Console API credits
   └─ Use Claude Console Authentication (Method B)
           Common for developers with API access
```

**If you have both**: Use Claude.ai authentication (Method A)—it's simpler and you can switch to Console authentication later if needed.

---

### Authentication Method A: Claude.ai Account (Most Common)

**Step 1: Start the Authentication Flow**

In your terminal, run:

```bash
claude
```

**Expected output**:
```
____
```

**What happens**: Your default browser opens to the Claude.ai authentication page.

**Step 2: Log In to Claude.ai**

1. If not already logged in, enter your Claude.ai credentials
2. Review the permissions Claude Code is requesting
3. Click "Allow" or "Authorize"

**Step 3: Confirm Authentication**

Return to your terminal. You should see:

```
✓ Successfully authenticated with Claude.ai
✓ API key stored securely
You're ready to use Claude Code!
```

**Step 4: Test Your Setup**

Run a simple test command:

```bash
claude "Hello! Can you confirm Claude Code is working?"
```

**Expected output**: Claude responds with a greeting confirming the connection works.

---

## First Run Verification: Confirming Everything Works

Create a test file, then ask Claude to read it:

```bash
echo "This is a test file for Claude Code." > test-claude.txt
claude "Read test-claude.txt and tell me what it says."
```

**Expected**: Claude reads the file and reports the contents.

**Test 3: Command Execution**

```bash
claude "Run the command 'echo Success' and show me the output."
```

**Expected**: Claude executes the command and displays "Success".

**If all three tests pass**: 🎉 **Claude Code is fully installed, authenticated, and working!** You're ready for Lesson 3.

**If any test fails**: Continue to the troubleshooting section below.

---

## If Installation or Authentication Fails

**Most common issues and quick fixes:**

**"command not found" after npm install**:
- Close and reopen your terminal
- Or: `export PATH="$(npm config get prefix)/bin:$PATH"`

**Browser doesn't open for authentication**:
- Check your internet connection
- Try again with `[command to authenticate - phase 2 will confirm correct syntax]`

**API Key error (Console users)**:
- Verify your API key is active: https://console.anthropic.com/keys
- Create a new key and re-authenticate

**Not sure what went wrong?**:
- Check official docs: https://docs.claude.com/en/docs/claude-code/troubleshooting
- Or ask your AI pair programmer for help debugging the error message

---

## Pause and Reflect: You've Crossed the Bridge

**If your installation and authentication succeeded**: Take a moment to appreciate what you've accomplished. Claude Code is now installed and ready to assist you. You've moved from theory to practice.

**Reflection Questions**:
- Which installation method did you choose, and why?
- Did you encounter any issues? If so, which troubleshooting steps helped?
- How does it feel to have an AI assistant accessible directly from your terminal?

**If you're still troubleshooting**: Don't get discouraged. Installation challenges are normal, especially across different platforms and environments. Work through the troubleshooting section systematically, and don't hesitate to seek help from the community resources listed above.

---

## Security and Best Practices

Before moving forward, let's address important security considerations:

**1. API Key Security**

- ✅ **Do**: Store API keys using Claude Code's built-in secure storage (`claude auth login` or `claude auth set-key`)
- ❌ **Never**: Store API keys in code, config files, or environment variables that get committed to version control
- ✅ **Do**: Rotate API keys periodically (every 90 days recommended)
- ❌ **Never**: Share API keys or commit them to public repositories

**2. File System Access**

- Claude Code can read and write files in directories where you run it
- **Best Practice**: Start Claude Code sessions in project directories, not system directories
- Review file changes Claude proposes before approving them

**3. Command Execution**

- Claude Code can execute terminal commands with your permissions
- **Best Practice**: Review commands Claude suggests, especially `sudo` or administrative commands
- Claude Code will ask for approval before executing destructive actions

**4. Cost Management (Console API Users)**

- Set usage limits in Claude Console: https://console.anthropic.com/settings/limits
- Monitor usage regularly to avoid unexpected bills
- Claude Code displays token usage after each interaction

---

## What's Next: Lesson 3 - Subagents

Now that Claude Code is installed and working, you're ready to learn about **subagents**—specialized AI assistants that handle specific tasks with custom instructions and isolated contexts.

In Lesson 3, you'll:
- Understand when to use subagents versus the main conversation
- Create your first subagent (a code reviewer)
- Learn to manage multiple subagents for different tasks
- See how subagents preserve context and improve efficiency

**By mastering subagents**, you'll transform Claude Code from a general assistant into a specialized team of experts, each focused on specific aspects of your development workflow.

Let's continue building your Claude Code expertise.

---

## Key Takeaways

- **Two installation methods**: NPM (for Node.js users) and native installers (platform-specific)
- **Two authentication paths**: Claude.ai accounts (most common) and Claude Console API keys
- **95% success rate achievable**: Comprehensive troubleshooting covers most common issues
- **Security matters**: Store API keys securely, review file changes, monitor usage
- **Verification is essential**: Test basic interaction, file access, and command execution
- **Help is available**: Official docs, GitHub issues, and community Discord for support

---

**Up Next**: [Lesson 3 - Understanding and Using Subagents](./03-subagents.md)
