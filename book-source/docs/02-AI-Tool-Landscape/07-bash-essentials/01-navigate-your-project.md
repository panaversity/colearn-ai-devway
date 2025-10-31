---
sidebar_position: 1
title: "Move Around — Navigate Your Project"
---

# Move Around — Navigate Your Project

## What You're Trying to Do

Your CLI Coding Agent (Claude Code, Gemini CLI) is about to work on files in your project. You need to understand where it's working and what files it can see. This lesson teaches you to read the agent's environment.

---

## The Bash Commands

### Print Working Directory (Where Are You?)
```bash
pwd                    # Shows the full path where the agent is working
```

**Example output:** `/Users/yourname/my_project`

### List Files (What's Here?)
```bash
ls                     # List files in current folder
ls -la                 # List all files with details (sizes, dates, permissions)
ls -la <folder>        # List files in a specific folder
```

**Example output:**
```
total 32
drwxr-xr-x  5 user staff  160 Oct 31 10:15 .
drwxr-xr-x  8 user staff  256 Oct 31 10:00 ..
-rw-r--r--  1 user staff 1024 Oct 31 10:20 README.md
drwxr-xr-x  3 user staff   96 Oct 31 10:15 src/
drwxr-xr-x  2 user staff   64 Oct 31 10:15 tests/
```

### Change Directory (Move Around)
```bash
cd <folder-name>       # Go into a folder (relative path)
cd /full/path/here     # Go to exact location (absolute path)
cd ~                   # Go to your home directory
cd ..                  # Go up one level
cd -                   # Go back to previous folder
```

**Example:**
```bash
cd my_project          # Go into my_project folder
cd ~/Documents         # Go to Documents in home folder
cd ..                  # Go back up
```

---

## How to Ask Your CLI Coding Agent

Instead of running commands yourself, describe what you want:

| What You Want | What to Ask Your Agent |
|---|---|
| Know where it's working | "What directory are you in?" or "Show me your current path" |
| See project files | "List the files in this project" or "What's in the src folder?" |
| Navigate to a folder | "Go into the src folder" or "Navigate to the tests directory" |
| Check if file exists | "Is there a requirements.txt file?" or "Do I have a config.json?" |

**Example conversation:**
```
You: "What files are in my project right now?"
Agent: "I'll check. $ ls -la"
[Shows output]
Agent: "You have src/, tests/, README.md, and setup.py"
```

---

## Why This Matters for Your Product

- **Verify location**: Before installing packages or creating files, know where the agent is working
- **Understand structure**: See what's already in your project
- **Prevent mistakes**: If the agent needs to work in a specific folder, you'll know if it's in the right place
- **Debug issues**: When something doesn't work, "What folder are you in?" is the first question

---

## Try With AI

**Tool**: Claude Code, Gemini CLI, or ChatGPT Web

### Prompt 1: Check Current Location
```
Show me where you are in the file system and what files are in this directory.
Use pwd and ls commands to show me.
```

**Expected outcome**: You see the agent's current location and can understand the folder structure

### Prompt 2: Navigate and Verify
```
I want you to navigate to my project folder and show me what's there.
What's the full path you're in? What files do you see?
```

**Expected outcome**: You can follow along with the agent's navigation

### Prompt 3: Understand Paths
```
Explain the difference between these two paths:
- /Users/myname/projects/my_app
- ~/projects/my_app

When would I use each one?
```

**Expected outcome**: You understand absolute vs. relative paths
