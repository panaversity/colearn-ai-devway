---
sidebar_position: 2
title: "Lesson 2: Installing and Authenticating Claude Code"
duration: "27-35 min"
---

# Lesson 2: Installing and Authenticating Claude Code

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

## Choosing Your Installation Method

Claude Code offers **two installation methods**. Choose based on your setup:

| Method | Best For | Pros | Cons |
|--------|----------|------|------|
| **NPM** | Developers with Node.js already installed | Easy updates with `npm update -g`, familiar to Node developers | Requires Node.js 18+ |
| **Native Installer** | Users without Node.js or those preferring standalone tools | No Node.js dependency, smaller install size | Platform-specific downloads, manual updates |

**Recommendation**: If you already have Node.js installed (check with `node --version`), use NPM. Otherwise, use the native installer for your platform.

---

## Installation Method 1: NPM Installation (Recommended for Node.js Users)

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

---

## Installation Method 2: Native Installers (No Node.js Required)

### For Windows (10/11)

**Step 1: Download the Windows Installer**

Visit: https://claude.ai/install and download the `.exe` installer for Windows.

**Step 2: Run the Installer**

1. Double-click the downloaded `.exe` file
2. If Windows SmartScreen appears, click "More info" → "Run anyway"
3. Follow the installation wizard (accept defaults)
4. Installation completes in 1-2 minutes

**Step 3: Verify Installation**

Open a **new** Command Prompt or PowerShell window (important: must be new window) and run:

```bash
claude --version
```

**Expected output**:
```
claude-code version 1.2.3
```

**Windows-Specific Note**: If using Windows Subsystem for Linux (WSL), install Claude Code inside WSL using the Linux instructions below—don't use the Windows installer from within WSL.

---

### For macOS (10.15+)

**Step 1: Download the macOS Installer**

Visit: https://claude.ai/install and download the `.dmg` installer for macOS.

**Step 2: Install Claude Code**

1. Open the downloaded `.dmg` file
2. Drag the Claude Code icon to the Applications folder
3. Eject the disk image

**Step 3: Add Claude Code to Your PATH**

Open Terminal and run:

```bash
sudo ln -s /Applications/ClaudeCode.app/Contents/MacOS/claude /usr/local/bin/claude
```

**What this does**: Creates a symbolic link so you can run `claude` from any terminal location.

**Step 4: Verify Installation**

```bash
claude --version
```

**Expected output**:
```
claude-code version 1.2.3
```

**macOS-Specific Note**: On first run, macOS may show a security warning. Go to System Settings → Privacy & Security → Allow "claude" to run.

---

### For Linux (Ubuntu, Debian, Fedora, Arch)

**Step 1: Download the Install Script**

```bash
curl -fsSL https://claude.ai/install.sh -o install-claude.sh
```

**Step 2: Review the Script (Security Best Practice)**

```bash
cat install-claude.sh
```

**What to look for**: Verify the script downloads from official Anthropic sources and doesn't contain suspicious commands.

**Step 3: Run the Installer**

```bash
chmod +x install-claude.sh
sudo ./install-claude.sh
```

**What this does**: Makes the script executable and runs it with administrator permissions to install Claude Code system-wide.

**Step 4: Verify Installation**

```bash
claude --version
```

**Expected output**:
```
claude-code version 1.2.3
```

**Linux-Specific Notes**:
- For **Arch Linux**: Claude Code is also available in the AUR: `yay -S claude-code`
- For **Fedora/RHEL**: Use the install script above or download the `.rpm` package from https://claude.ai/install

---

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
claude auth login
```

**Expected output**:
```
Opening browser for authentication...
Waiting for login to complete...
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

**If authentication fails**: See [Troubleshooting: Authentication Issues](#troubleshooting-authentication-issues).

---

### Authentication Method B: Claude Console (API Credits)

**Step 1: Get Your API Key**

1. Go to: https://console.anthropic.com
2. Navigate to "API Keys" section
3. Click "Create Key"
4. **Copy the key immediately**—you won't see it again

**Security Warning**: Treat API keys like passwords. Never commit them to version control or share them publicly.

**Step 2: Set the API Key in Claude Code**

In your terminal, run:

```bash
claude auth set-key
```

**Expected prompt**:
```
Enter your Anthropic API key:
```

Paste your API key and press Enter.

**Expected output**:
```
✓ API key saved securely
✓ Ready to use Claude Code with Console API
```

**Step 3: Test Your Setup**

```bash
claude "Hello! Verify Claude Code is connected."
```

**Expected output**: Claude responds, confirming the connection.

**Cost Note**: Console API usage is billed based on tokens used. Claude Code will display token usage for each interaction. Monitor usage at: https://console.anthropic.com/usage

---

## First Run Verification: Confirming Everything Works

Let's run a comprehensive test to ensure Claude Code is fully functional.

**Test 1: Basic Interaction**

```bash
claude "What is 2 + 2?"
```

**Expected**: Claude responds with "4" (possibly with additional context).

**Test 2: File System Access**

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

## Troubleshooting: Common Installation and Authentication Issues

This section covers 90% of issues readers encounter. Work through these systematically.

### Troubleshooting: Command Not Found

**Symptom**: Running `claude --version` or `claude` returns "command not found" or "not recognized as an internal or external command."

**Causes and Fixes**:

**1. NPM Global Bin Not in PATH**

**Check**: Run `npm config get prefix` to see where NPM installs global packages.

**Fix (macOS/Linux)**:
```bash
export PATH="$(npm config get prefix)/bin:$PATH"
```

Add this line to your `.bashrc`, `.zshrc`, or `.profile` to make it permanent.

**Fix (Windows)**:
1. Run `npm config get prefix` and note the path
2. Open System Properties → Environment Variables
3. Add the path (with `\` not `/`) to your PATH variable
4. Restart terminal

**2. Installation Failed Silently**

**Fix**: Reinstall with verbose output to see errors:
```bash
npm install -g @anthropic-ai/claude-code --verbose
```

**3. Using Old Terminal Session**

**Fix**: Close and reopen your terminal. Some installations require a new session to update PATH.

---

### Troubleshooting: Authentication Issues

**Symptom**: `claude auth login` fails, or Claude Code can't connect to the API.

**Causes and Fixes**:

**1. Browser Doesn't Open**

**Check**: Does `claude auth login` show "Opening browser..." but nothing happens?

**Fix**: Manually open the authentication URL:
```bash
claude auth login --print-url
```

Copy the URL displayed and paste it into your browser manually.

**2. API Key Not Saved**

**Check**: Run `claude auth status` to see if you're authenticated.

**Fix**: Re-run the authentication process:
```bash
claude auth logout
claude auth login
```

**3. Firewall or Proxy Blocking Connection**

**Check**: Can you access https://api.anthropic.com in your browser?

**Fix**: If behind a corporate firewall, configure proxy settings:
```bash
export HTTPS_PROXY=http://your-proxy:port
claude auth login
```

**4. Invalid or Expired API Key (Console users)**

**Check**: Go to https://console.anthropic.com/keys and verify your key is active.

**Fix**: Create a new API key and re-authenticate:
```bash
claude auth set-key
```

---

### Troubleshooting: Permission Errors

**Symptom**: Installation fails with "EACCES" or "permission denied" errors.

**Causes and Fixes**:

**1. NPM Global Install Without Sudo (Linux/macOS)**

**Don't do this**: `sudo npm install -g` (bad practice—gives NPM root access)

**Better fix**: Configure NPM to use a user-writable directory:
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

Then retry: `npm install -g @anthropic-ai/claude-code`

**2. Windows Requires Administrator**

**Fix**: Right-click Command Prompt or PowerShell → "Run as Administrator" → Retry installation.

---

### Troubleshooting: Node.js Version Mismatch

**Symptom**: NPM installation fails with "requires Node.js >= 18" error.

**Check Current Version**:
```bash
node --version
```

**Fix**: Upgrade Node.js:
- **Using nvm (recommended)**: `nvm install 18 && nvm use 18`
- **Download**: https://nodejs.org (install LTS version)
- **Alternatively**: Use the native installer (doesn't require Node.js)

---

### Troubleshooting: SSL/Certificate Errors

**Symptom**: Authentication fails with SSL certificate errors.

**Causes and Fixes**:

**1. Corporate SSL Inspection**

**Check**: Does your company use SSL inspection or custom certificates?

**Fix**: Configure Node.js to use your company's CA bundle:
```bash
export NODE_EXTRA_CA_CERTS=/path/to/company-ca-bundle.pem
claude auth login
```

**2. System Clock Incorrect**

**Check**: Is your system date/time correct?

**Fix**: Sync your system clock:
- **Windows**: Settings → Time & Language → Sync now
- **macOS**: System Preferences → Date & Time → Set automatically
- **Linux**: `sudo timedatectl set-ntp true`

---

### Troubleshooting: Platform-Specific Issues

**Windows WSL Users**

**Issue**: Installed on Windows but trying to use from WSL (or vice versa).

**Fix**: Install Claude Code inside your WSL environment, not on Windows:
```bash
# From within WSL
curl -fsSL https://claude.ai/install.sh -o install-claude.sh
chmod +x install-claude.sh
./install-claude.sh
```

**macOS Apple Silicon (M1/M2/M3) Users**

**Issue**: "cannot be opened because the developer cannot be verified."

**Fix**:
1. System Settings → Privacy & Security
2. Scroll to "Security" section
3. Click "Open Anyway" next to Claude Code

**Linux Snap/Flatpak Sandboxing**

**Issue**: Claude Code can't access files outside home directory.

**Fix**: Install using the native script method instead of Snap/Flatpak to avoid sandboxing restrictions.

---

### Still Having Issues?

If none of the above resolves your problem:

1. **Check Official Troubleshooting**: https://docs.claude.com/en/docs/claude-code/troubleshooting
2. **Search GitHub Issues**: https://github.com/anthropics/claude-code/issues
   - Someone may have encountered and solved your specific error
3. **Community Discord**: https://discord.gg/anthropic
   - `#claude-code` channel for real-time help
4. **File a Bug Report**: If you've found a new issue, open an issue on GitHub with:
   - Your platform and version (`claude --version`, `node --version`, OS version)
   - Exact error messages
   - Steps to reproduce

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
