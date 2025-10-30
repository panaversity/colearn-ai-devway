---
sidebar_position: 2
title: Installation — Platform-Specific Walkthroughs
---

# Installation — Platform-Specific Walkthroughs

## Your First Real Step Into AI-Driven Development

You've learned why the Gemini CLI matters. Now it's time to install it.

This lesson walks you through installation on **Windows**, **macOS**, and **Linux**. By the end, you'll have the Gemini CLI running on your machine, ready to authenticate and start building AI-powered workflows.

**What you'll accomplish** (20-30 minutes):
- Verify your system meets the prerequisites
- Install the Gemini CLI using platform-specific commands
- Confirm installation with `gemini --version`
- Troubleshoot common installation issues

**Why this matters**: Installation is your gateway. Without it, you can't access Gemini's capabilities from your terminal. This lesson ensures you install correctly the first time, avoiding frustration and wasted hours.

Let's get started.

---

## Pre-Installation Checklist

Before installing the Gemini CLI, verify your system meets these requirements:

### Required Dependencies

The Gemini CLI is distributed as an **npm package** (Node Package Manager). This means you need:

1. **Node.js** — A JavaScript runtime environment
2. **npm** — Node's package manager (comes with Node.js)
3. **Terminal/Command Prompt** — Command-line access
4. **Internet connection** — To download the package

### Check If You Already Have Node.js and npm

Open your terminal (instructions below) and run these commands:

**Check Node.js version:**

```bash
node --version
```

**Expected output** (version numbers may vary):
```
v20.11.0
```

**Check npm version:**

```bash
npm --version
```

**Expected output**:
```
10.2.4
```

**What you need:**
- **Node.js**: Version 18.x or higher recommended
- **npm**: Version 9.x or higher recommended

**If commands fail** or versions are too old, install/update Node.js:

- **Windows/macOS**: Download from [nodejs.org](https://nodejs.org/) (choose LTS version)
- **Linux**: Use your distribution's package manager (instructions below)

### Opening Your Terminal

**Windows:**
- Press `Win + X`
- Select "Windows PowerShell" (or "Terminal" if using Windows 11)

**macOS:**
- Press `Cmd + Space` → Type "Terminal" → Press Enter

**Linux:**
- Press `Ctrl + Alt + T`
- Or search for "Terminal" in your application menu

### Pre-Installation Checklist Summary

Before proceeding, confirm:

- [ ] Node.js is installed (`node --version` shows v18+ or higher)
- [ ] npm is installed (`npm --version` shows v9+ or higher)
- [ ] You can open and use your terminal
- [ ] You have an active internet connection

If any item is unchecked, address it before continuing.

---

## Windows Installation

### Recommended Method: PowerShell

**Why PowerShell?** It's the modern, more powerful terminal on Windows. Most Windows 10/11 systems have it pre-installed.

**Step 1: Open PowerShell**

1. Press `Win + X`
2. Select "Windows PowerShell" (or "Terminal" if using Windows 11)

**Step 2: Install the Gemini CLI**

Run this command:

```powershell
npm install -g @google/gemini-cli
```

**What this command does:**
- `npm install` — Tells npm to download and install a package
- `-g` — Installs globally (available from any directory)
- `@google/gemini-cli` — The official Gemini CLI package

**Expected output:**

You'll see npm download dependencies and install the CLI. It may take 30-60 seconds. The final output should look like:

```
added 45 packages in 23s
```

**If you see permission errors**, see the Troubleshooting section below.

### Alternative Method: Command Prompt

If PowerShell isn't available, use Command Prompt:

1. Press `Win + R` → Type `cmd` → Press Enter
2. Run the same installation command:

```cmd
npm install -g @google/gemini-cli
```

### Common Windows-Specific Issues

**Issue 1: Execution Policy Restriction (PowerShell)**

If you see:
```
cannot be loaded because running scripts is disabled on this system
```

**Solution**: Run PowerShell as Administrator, then:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then retry the installation.

**Issue 2: npm Not Found**

If you see:
```
'npm' is not recognized as an internal or external command
```

**Solution**: Node.js isn't installed or not in PATH. Download and install from [nodejs.org](https://nodejs.org/), then restart your terminal.

---

## macOS Installation

### Recommended Method: npm

**Why npm?** It's the standard method for installing Node.js packages on all platforms, including macOS.

**Step 1: Open Terminal**

Press `Cmd + Space` → Type "Terminal" → Press Enter

**Step 2: Install the Gemini CLI**

Run this command:

```bash
npm install -g @google/gemini-cli
```

**Expected output:**

```
added 45 packages in 18s
```

**If you see permission errors** (common on macOS), see the Troubleshooting section below.

### Alternative Method: Using sudo (Not Recommended)

If you encounter permission errors and can't resolve them, you can use `sudo`:

```bash
sudo npm install -g @google/gemini-cli
```

**Why not recommended?** Using `sudo` installs packages with root permissions, which can cause permission issues later. Prefer fixing npm's global directory permissions (see Troubleshooting).

**If prompted for password**: Enter your macOS user password (typing won't show on screen — this is normal).

### Using Homebrew (Alternative Installation)

**Note**: The Gemini CLI isn't available via Homebrew. However, you can use Homebrew to install Node.js, then use npm:

```bash
brew install node
npm install -g @google/gemini-cli
```

---

## Linux Installation

### Ubuntu/Debian-Based Distributions

**Step 1: Install Node.js and npm (if not already installed)**

```bash
sudo apt update
sudo apt install nodejs npm
```

**Verify installation:**

```bash
node --version
npm --version
```

**Step 2: Install the Gemini CLI**

```bash
npm install -g @google/gemini-cli
```

**Expected output:**

```
added 45 packages in 22s
```

**If you see permission errors**, see the Troubleshooting section below.

### Fedora/Red Hat-Based Distributions

**Step 1: Install Node.js and npm**

```bash
sudo dnf install nodejs npm
```

**Step 2: Install the Gemini CLI**

```bash
npm install -g @google/gemini-cli
```

### Arch Linux

**Step 1: Install Node.js**

```bash
sudo pacman -S nodejs npm
```

**Step 2: Install the Gemini CLI**

```bash
npm install -g @google/gemini-cli
```

### Common Linux-Specific Issues

**Issue: Permission Denied When Installing Globally**

**Symptoms**:
```
EACCES: permission denied, mkdir '/usr/local/lib/node_modules/@google'
```

**Solution 1: Use a Version Manager (Recommended)**

Install Node.js using `nvm` (Node Version Manager):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
npm install -g @google/gemini-cli
```

**Solution 2: Change npm's Global Directory**

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
npm install -g @google/gemini-cli
```

**Solution 3: Use sudo (Not Recommended)**

```bash
sudo npm install -g @google/gemini-cli
```

---

## Verification: Confirming Successful Installation

Regardless of your platform, run this command to verify installation:

```bash
gemini --version
```

**Expected output:**

```
1.2.3
```

(Version number may vary. As of January 2025, version 1.x is current.)

**What this confirms:**
- The CLI is installed correctly
- The `gemini` command is in your system PATH
- You're ready to proceed to authentication

**If the command fails:**
- See the Troubleshooting section below
- Ensure you restarted your terminal after installation
- Check that npm's global bin directory is in your PATH

---

## Troubleshooting Common Installation Issues

### Problem 1: "Command Not Found" After Installation

**Symptoms:**
```bash
gemini --version
# Output: gemini: command not found
```

**Diagnosis**: The global npm bin directory isn't in your PATH.

**Solution (all platforms):**

1. Find npm's global bin directory:

```bash
npm config get prefix
```

**Example output**: `/usr/local` (macOS/Linux) or `C:\Users\YourName\AppData\Roaming\npm` (Windows)

2. Add this directory to your PATH:

**macOS/Linux:**
```bash
echo 'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Windows (PowerShell):**
```powershell
[Environment]::SetEnvironmentVariable("Path", "$env:Path;$(npm config get prefix)", "User")
```

Then restart your terminal and try `gemini --version` again.

### Problem 2: Permission Errors (EACCES)

**Symptoms:**
```
npm ERR! code EACCES
npm ERR! syscall mkdir
npm ERR! path /usr/local/lib/node_modules/@google
npm ERR! errno -13
```

**Diagnosis**: You don't have write permissions to npm's global directory.

**Solution (macOS/Linux):**

**Option 1: Fix npm permissions (recommended):**

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
npm install -g @google/gemini-cli
```

**Option 2: Use a version manager (nvm):**

Reinstall Node.js via [nvm](https://github.com/nvm-sh/nvm):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
npm install -g @google/gemini-cli
```

**Windows**: Run PowerShell as Administrator, then retry installation.

### Problem 3: Node.js or npm Not Installed

**Symptoms:**
```
'node' is not recognized as an internal or external command
```
or
```
'npm' is not recognized as an internal or external command
```

**Solution:**

Install Node.js from [nodejs.org](https://nodejs.org/) (download the LTS version). This includes npm. After installation, restart your terminal and verify:

```bash
node --version
npm --version
```

Then retry the Gemini CLI installation.

### Problem 4: Network or Proxy Issues

**Symptoms:**
```
npm ERR! network request to https://registry.npmjs.org/@google/gemini-cli failed
```

**Diagnosis**: Your network blocks npm registry access, or you're behind a proxy.

**Solution:**

**If behind a corporate proxy:**

```bash
npm config set proxy http://proxy.company.com:8080
npm config set https-proxy http://proxy.company.com:8080
```

(Replace with your actual proxy address.)

**If using a firewall or VPN**: Temporarily disable it during installation, or whitelist `registry.npmjs.org`.

### Problem 5: Version Conflicts with Existing Installation

**Symptoms:**
```
npm ERR! Unexpected end of JSON input while parsing near '...'
```

**Solution:**

Clear npm's cache and retry:

```bash
npm cache clean --force
npm install -g @google/gemini-cli
```

### Problem 6: Antivirus or Firewall Blocking Installation

**Symptoms:**
- Installation hangs indefinitely
- Files are quarantined or deleted immediately after installation

**Solution:**

Temporarily disable antivirus/firewall during installation. On Windows, add npm's global directory to your antivirus exclusion list:

1. Find npm's global directory: `npm config get prefix`
2. Add this path to your antivirus exclusions
3. Retry installation

### Problem 7: Outdated npm Version

**Symptoms:**
```
npm ERR! peer dep missing: @google/some-dependency@^1.0.0
```

**Solution:**

Update npm to the latest version:

```bash
npm install -g npm@latest
```

Then retry installing the Gemini CLI.

### Problem 8: Installation Corruption

**Symptoms:**
- Installation succeeds but `gemini --version` crashes
- Inconsistent behavior or missing files

**Solution:**

Uninstall and reinstall:

```bash
npm uninstall -g @google/gemini-cli
npm cache clean --force
npm install -g @google/gemini-cli
```

---

## Practice Exercises

### Exercise 1: Verify Your Installation ⭐

**Task**: Confirm the Gemini CLI is installed and accessible.

**Steps**:
1. Open your terminal
2. Run: `gemini --version`
3. Note the version number

**Expected outcome**: You see a version number (e.g., `1.2.3`)

**If this fails**: Review the Troubleshooting section above.

### Exercise 2: Locate the Installation Path ⭐⭐

**Task**: Find where the Gemini CLI is installed on your system.

**Steps**:

**Windows (PowerShell):**
```powershell
where.exe gemini
```

**macOS/Linux:**
```bash
which gemini
```

**Expected outcome**: You see the full path to the `gemini` executable.

**Example output (macOS)**:
```
/usr/local/bin/gemini
```

**Why this matters**: Knowing the installation path helps with debugging and understanding how global npm packages work.

### Exercise 3: Document Your Setup ⭐⭐⭐

**Task**: Create a simple text file documenting your installation.

**Steps**:
1. Create a file named `gemini-setup.txt`
2. Include:
   - Your operating system (Windows, macOS, or Linux)
   - Node.js version (`node --version`)
   - npm version (`npm --version`)
   - Gemini CLI version (`gemini --version`)
   - Installation path (`which gemini` or `where.exe gemini`)
   - Any issues you encountered and how you resolved them

**Why this matters**: Documentation is a core skill in software development. This file will help you troubleshoot future issues and remember what worked.

---

## What You've Accomplished

You've successfully installed the Gemini CLI on your machine. This is your first tangible step into AI-driven development.

**Key takeaways**:
- The Gemini CLI requires Node.js and npm as dependencies
- Installation is platform-specific but follows a common pattern
- `gemini --version` confirms successful installation
- Troubleshooting installation issues builds debugging skills

**Reflection prompt**: Take a moment to consider: How does having a CLI tool feel different from using a web interface? What advantages might command-line access provide when building workflows?

---

## What's Next?

Installation is complete, but the CLI won't do anything useful yet. You need to authenticate with your Google AI Studio API key.

**In Lesson 3: Authentication and First Command**, you'll:
- Obtain an API key from Google AI Studio
- Configure the Gemini CLI with `gemini config set`
- Run your first AI prompt from the terminal
- Understand how API keys enable programmatic access to Gemini

The finish line is in sight. Let's authenticate and make your first AI request.

---

## Additional Resources

- [Official Gemini CLI npm page](https://www.npmjs.com/package/@google/gemini-cli)
- [Node.js Downloads](https://nodejs.org/)
- [npm Documentation](https://docs.npmjs.com/)
- [Troubleshooting npm permissions](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)
- [nvm (Node Version Manager)](https://github.com/nvm-sh/nvm)

---

**Maintenance Note**: Installation instructions reviewed January 2025. If npm package name or installation method changes, update all code examples and expected outputs. Check for updates quarterly.
