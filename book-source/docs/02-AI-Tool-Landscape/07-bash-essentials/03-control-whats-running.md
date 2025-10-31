---
sidebar_position: 3
title: "Control What's Running — Processes & Backgrounds"
---

# Control What's Running — Processes & Backgrounds

## What You're Trying to Do

Your CLI Coding Agent might start a web server, run tests, or start a background service. You need to know what's running and how to stop it if something goes wrong.

---

## The Bash Commands

### Run Programs
```bash
python script.py         # Run a program (wait for it to finish)
npm start                # Run command in foreground (blocks terminal)
command &                # Run in background (terminal stays free)
```

### See What's Running
```bash
ps aux                   # List all running processes
ps aux | grep python     # Find Python processes
top                      # Interactive view of running processes (q to quit)
```

**Example output from `ps aux | grep python`:**
```
user  12345  0.5  2.1  350000 50000 ?  S  10:15  0:45 python server.py
user  12346  0.1  1.2  300000 30000 ?  S  10:16  0:10 python tests.py
```

### Stop Running Programs
```bash
Ctrl+C                   # Stop current program (press Ctrl and C)
Ctrl+Z                   # Pause current program
kill 12345               # Stop process with ID 12345
killall python           # Stop all Python processes
```

---

## How to Ask Your CLI Coding Agent

| What You Want | What to Ask Your Agent |
|---|---|
| Start a server | "Start the development server" or "Run npm start" |
| Run in background | "Start this in the background so I can keep using the terminal" |
| See what's running | "What Python processes are currently running?" |
| Stop something | "Stop the web server" or "Kill the process running on port 3000" |
| Check if still running | "Is the server still running?" |

**Example conversation:**
```
You: "Start a development server for me"
Agent: "$ npm start"
[Server starts and blocks terminal]

You: "Can you run this in the background instead?"
Agent: "Sure, I'll press Ctrl+C first to stop it, then: $ npm start &"
[Server runs in background, terminal is free]
```

---

## Why This Matters for Your Product

- **Know what's running**: Your agent might start services you need to monitor
- **Stop cleanly**: If something goes wrong, knowing how to stop it prevents chaos
- **Background work**: Tests, servers, and builds should run while you stay productive
- **Debugging**: When something doesn't work, "What's running?" is key info

---

## Common Scenarios

### Your Agent Starts a Web Server
```bash
npm start                # Starts server in foreground
# Terminal is blocked until you stop it

# To stop:
Ctrl+C                   # Kills the server
```

### Your Agent Needs to Run Tests While You Code
```bash
npm test &               # Runs tests in background
# Terminal is free; tests run separately

# To check:
ps aux | grep test       # See if tests are still running

# To stop:
killall npm              # Kills the test process
```

### Your Agent Installs Packages
```bash
pip install -r requirements.txt   # Installation runs in foreground
# Terminal blocked until complete (this is normal)
```

---

## Red Flags to Watch

If something seems stuck:
- ✅ Normal: Installation taking time (can take minutes)
- ✅ Normal: Server starting up (may pause for setup)
- ❌ Problem: Command that should finish but hasn't after 30 seconds
  - Try: `Ctrl+C` to stop it
  - Ask agent: "Why is this taking so long?"

---

## Quick Reference

| Goal | Command |
|---|---|
| Run something and wait | `command` (press Enter, wait) |
| Run something in background | `command &` (type &, press Enter) |
| See what's running | `ps aux` or `top` |
| Stop current program | `Ctrl+C` (hold Ctrl, press C) |
| Stop specific program | `kill <process-ID>` |
| Stop all of a type | `killall program-name` |

---

## Try With AI

Use your AI companion tool set up (e.g., ChatGPT web, Claude Code, Gemini CLI), you may use that instead—the prompts are the same.

### Prompt 1: Understand Processes
```
Explain what these commands do and when I'd use each:
- npm start
- npm start &
- ps aux | grep npm
- killall npm
```

**Expected outcome**: Understand the difference between foreground and background

### Prompt 2: Practical Scenario
```
I want to run my tests in the background while continuing to code.
How would you do this with npm?
What command would I run to check if tests are still running?
```

**Expected outcome**: Learn background process workflow

### Prompt 3: Emergency Stop
```
I started a web server and now the terminal is frozen.
How do I stop it without killing the entire terminal?
```

**Expected outcome**: Know your escape hatch (Ctrl+C)
