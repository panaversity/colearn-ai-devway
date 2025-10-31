---
sidebar_position: 5
title: "Get Dependencies — Install Packages"
---

# Lesson 5: Get Dependencies — Install Packages

## What You're Trying to Do

Your project needs code that someone else already wrote. Maybe you need code to talk to an API, read files, or send emails. Instead of writing it from scratch, you **install** it. Your CLI Coding Agent will suggest commands to download and set up these pre-written code packages. You need to understand what's happening and verify it worked.

---

## First: What Are Dependencies?

**Dependency** = A piece of code your project needs to work.

**Real example**: You're building a web app. You don't want to write code to handle user logins from scratch. Someone already solved this problem and shared it. You **depend on** their code. That's a dependency.

```
Your Project
    ↓
    Needs: User login code
    ↓
    Install: auth-library v2.5
    ↓
    auth-library is downloaded and ready to use
```

**Why dependencies matter**:
- You reuse code instead of reinventing it
- You get features built by experts
- You save time
- Your project is smaller and faster

**Your job**: Understand what's being installed and verify it worked.

---

## The Bash Commands

### Package Managers (Let Your Agent Choose The Right One)

Different programming languages use different tools to install dependencies. Your agent knows which one to use.

**Most common**:
```bash
npm install                        # Node.js: Install packages listed in package.json
npm list                           # See what's installed
```

**Alternative** (if you're using Python):
```bash
pip install -r requirements.txt    # Python: Install all packages in requirements.txt
pip list                           # See what's installed
```

**That's it.** Your agent will tell you which command to run. Don't worry about memorizing all the different tools.

---

## How Installation Works (What You'll See)

When you run an install command, your agent will show you output like this:

```bash
$ npm install
npm notice
npm notice New minor version of npm available! 8.19.2 → 9.0.0
npm notice
added 127 packages
```

**What this means:**
1. Downloaded and installed 127 packages your project needs
2. They're ready to use
3. Done!

That's really all that happens. Your agent will tell you if something goes wrong.

---

## How to Ask Your CLI Coding Agent

You don't need to know the exact command. Just describe what you need:

| What You Want | What to Ask Your Agent |
|---|---|
| Install packages | "Install all the packages this project needs" |
| Check what's installed | "What packages are installed?" |
| Add a new package | "I need to add the [package name] library. How do we do that?" |

**Example conversation:**
```
You: "This project needs packages installed. What should I do?"
Agent: "I'll install them now: $ npm install"
[Installation runs]
Agent: "Done! All packages are installed and ready"
You: "How do I know it worked?"
Agent: "Let me verify: $ npm list"
[Shows list of installed packages]
Agent: "Perfect! Everything is installed"
```

**Key point**: You don't need to remember or type these commands. Your agent knows what to do. Your job is just to understand what's happening.

---

## Why This Matters for Your Product

- **Speed**: You get code someone else wrote instead of building it yourself
- **Reliability**: These are proven libraries used by thousands of projects
- **Team setup**: When you share your project, someone else runs `npm install` (or `pip install`) and gets exactly what you have
- **You don't memorize**: Your agent knows which packages to install and how

---

## The Simple Pattern: Ask Your Agent to Verify and Explain

When your agent installs packages, it handles everything:
- Downloads the right packages
- Checks they work together
- Records what it installed
- Reports success or errors

This is why you have an AI companion—to handle the complex stuff while you understand what's happening.

---

## Common Scenarios

### Scenario 1: Your Agent Installs Packages
```bash
$ npm install

# Or if Python:
$ pip install -r requirements.txt

# This downloads and sets up all packages your project needs
# Usually takes 10-60 seconds depending on how many packages
```

**What you see**: Lots of text scrolling, then "added X packages" or similar success message.

**What to do**: Wait. Your agent will tell you when it's done.

### Scenario 2: You Want to Check What's Installed
```bash
# After installation, ask your agent:
# "What packages did we just install?"

# Agent might show:
npm list

# Output shows all installed packages and their versions
```

**What this tells you**: The packages are there and ready to use.

---

## What Actually Happens When You Install

**When you run `npm install` or `pip install`, here's what happens**:

1. **Download**: The package manager downloads the code
2. **Install**: It puts the code in a folder your project can access
3. **Register**: It records "this package is installed"
4. **Done**: Your code can now use that package

You don't need to know WHERE it goes—just that it's ready to use.

**How to know it worked**:
- No error messages = success
- You see "added X packages" or similar = success
- Your agent will tell you if something went wrong

---

## Try With AI

Use your AI companion tool set up (e.g., ChatGPT web, Claude Code, Gemini CLI), you may use that instead—the prompts are the same.

### Prompt 1: Install Packages in a Real Project
```
I'm setting up a new project and it needs packages installed.
I see a requirements.txt (or package.json) file.

What do I need to do to install all the packages?
Walk me through it step-by-step.
What will I see when it's working?
```

**Expected outcome**: See how simple installation is. Your agent handles it.

### Prompt 2: Understand What Was Installed
```
After we install packages, I want to see what we got.
How do I check what's installed?
How do I know installation actually worked?
```

**Expected outcome**: Learn to verify packages are there and working.

### Prompt 3: Handle an Installation Error
```
We tried to install packages but got an error.
What should I do?
Should I try again? Should we fix something first?
```

**Expected outcome**: Feel confident asking for help when something goes wrong.
