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

**4. Internet Connection**
- Needed for initial download and authentication
- Claude Code requires connection to communicate with Claude AI

---

## Installation: Node.js + NPM

Claude Code installs easily via Node.js package manager (npm). This is the recommended path - it works consistently across Windows, macOS, and Linux.

---

## Installation

### Step 1: Install Claude Code Globally

Open your terminal and run:

```bash
npm install -g @anthropic-ai/claude-code
```

**What this does**: Downloads and installs Claude Code globally on your system, making it accessible from any directory.

For macOs/Linux you can use:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Step 2: Verify Installation

Check that Claude Code is installed correctly:

```bash
claude --version
```

**Expected output** (version number may vary):
```
2.0.30 (Claude Code)
```

**If you see the version number**: ✅ Installation successful! Skip to [Authentication](#authentication-connecting-claude-code-to-your-account).

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

## If Installation or Authentication Fails

**Most common issues and quick fixes:**

**"command not found" after npm install**:
- Close and reopen your terminal
- Or: `export PATH="$(npm config get prefix)/bin:$PATH"`

**Browser doesn't open for authentication**:
- Check your internet connection
- Try again with `[command to authenticate - phase 2 will confirm correct syntax]`

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

**1. File System Access**

- Claude Code can read and write files in directories where you run it
- **Best Practice**: Start Claude Code sessions in project directories, not system directories
- Review file changes Claude proposes before approving them

**2. Command Execution**

- Claude Code can execute terminal commands with your permissions
- **Best Practice**: Review commands Claude suggests, especially `sudo` or administrative commands
- Claude Code will ask for approval before executing destructive actions

**3. Cost Management (Console API Users)**

- Set usage limits in Claude Console: https://console.anthropic.com/settings/limits
- Monitor usage regularly to avoid unexpected bills
- Claude Code displays token usage after each interaction

---

## Try With AI

Use Claude Code for this activity (preferred, since you just installed it). If you already have another AI companion tool set up (e.g., ChatGPT web, Gemini CLI), you may use that instead—the prompts are the same.

### Prompt 1: Installation Troubleshooting

```
I'm trying to install Claude Code on [Windows / macOS / Linux] and I'm stuck at [describe where you're stuck]. Walk me through troubleshooting step-by-step. What should I check FIRST? What's the most common cause of this issue? Give me 3-5 diagnostic commands I can run to figure out what's wrong.
```

**Expected outcome:** Step-by-step troubleshooting guidance for installation issues

### Prompt 2: Authentication Setup

```
I successfully installed Claude Code but I'm confused about authentication. I have [Claude.ai account / Claude Console account / both / neither]. Which authentication method should I use? Walk me through the exact steps, including where to find my credentials and what to paste where. Be very specific.
```

**Expected outcome:** Crystal-clear authentication instructions for your specific situation

### Prompt 3: Security Boundaries

```
The lesson mentions 'security considerations' like file access and command execution. I'm nervous about this. Help me set up safe boundaries: What directories should I AVOID running Claude Code in? What commands should I NEVER approve? Create a 'safety checklist' I can follow until I'm more comfortable.
```

**Expected outcome:** Practical safety boundaries and approval criteria

### Prompt 4: First Test Commands

```
I completed installation successfully! Now I want to test it with a simple, safe first command. Give me 3-5 'Hello World' style prompts I can try RIGHT NOW that will: (a) show me Claude Code works, (b) won't break anything, (c) help me understand what it can do. Include expected outputs so I know if it's working correctly.
```

**Expected outcome:** Confidence-building first commands with expected results
