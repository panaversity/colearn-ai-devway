---
sidebar_position: 7
title: "Connect Commands — Pipes & Complex Operations"
---

# Connect Commands — Pipes & Complex Operations

## What You're Trying to Do

Your CLI Coding Agent will suggest commands that chain together: take output from one command and use it as input to another. Understanding how this works helps you verify the agent's logic and predict what will happen before execution.

---

## The Bash Commands

### The Pipe Symbol (|) — Chain Commands Together
```bash
cat file.txt | grep "error"        # Read file, search for "error"
ls -la | grep ".py"               # List files, find Python files
ps aux | grep python              # List processes, find Python ones
find . -name "*.log" | wc -l       # Find all logs, count them
```

**What happens:**
1. Command on left produces output
2. `|` sends that output to command on right
3. Right command processes it
4. Shows final result

**Example step-by-step:**
```bash
# Without pipe (see all processes):
ps aux
# Shows: user 12345 0.5 2.1 ... python server.py
# Shows: user 12346 0.1 1.2 ... python tests.py
# Shows: [50 other processes]

# With pipe (see only Python):
ps aux | grep python
# Shows: user 12345 0.5 2.1 ... python server.py
# Shows: user 12346 0.1 1.2 ... python tests.py
```

### Save Output To A File (>) — Redirect Output
```bash
ls -la > file_list.txt             # Save directory listing to file
echo "Hello" > message.txt         # Write text to file (overwrites)
ps aux > running_processes.txt     # Save all processes to file
```

### Append To A File (>>) — Add To Existing File
```bash
echo "New line" >> message.txt     # Add line to end of file (keeps existing)
date >> log.txt                    # Add current date to log file
```

### Conditional Execution (&&) — Run Only If Previous Succeeds
```bash
npm install && npm start           # Install packages, THEN start server
python setup.py && python main.py  # Setup, THEN run program
pip install -r requirements.txt && python app.py  # Install, THEN run
```

### Error Handling (||) — Run If Previous Fails
```bash
npm start || echo "Server failed"  # Run server, or print message if it fails
python app.py || exit 1            # Run app, or exit with error code
```

### Combine Multiple Pipes
```bash
cat package.json | grep "version" | head -1  # Get just the version line
ps aux | grep python | grep -v grep          # Find Python processes, exclude search itself
find . -name "*.log" | head -20 | wc -l      # Find logs, show first 20, count them
```

---

## How to Ask Your CLI Coding Agent

| What You Want | What to Ask Your Agent |
|---|---|
| Chain commands | "How would you pipe these commands together?" |
| Understand a complex command | "Break down this command and explain each part" |
| Save output | "Save the results to a file instead of showing them" |
| Verify logic | "Walk me through what this pipe does step-by-step" |
| Test safely | "Show me what this would do without actually running it" |

**Example conversation:**
```
You: "I need to find all errors in our logs"
Agent: "I'll search logs for errors and save to a file: $ cat app.log | grep ERROR > errors.txt"
You: "Walk me through that"
Agent: "1. cat app.log reads the log file
         2. | pipes it to grep
         3. grep ERROR finds lines with ERROR
         4. > saves results to errors.txt"
You: "Got it. How many errors are there?"
Agent: "Let me count: $ grep ERROR app.log | wc -l"
```

---

## Why This Matters for Your Product

- **Data transformation**: Convert one output to exactly what you need
- **Verify safety**: Understand what an agent does before it modifies your system
- **Debugging**: Chain commands to narrow down problems
- **Automation**: Complex tasks are just simple commands piped together
- **Efficiency**: Do in one line what would take many manual steps

---

## Understanding Each Part

### Part 1: Command Chains (Pipes)

**Pattern: `command1 | command2 | command3`**

- **command1** produces output
- **command2** receives that output and processes it
- **command3** receives command2's output
- Final output is shown or redirected

**Real example:**
```bash
ps aux | grep python | head -3

# Step 1: ps aux
# Outputs: [all running processes]

# Step 2: | grep python
# Filters to: [processes with "python" in name]

# Step 3: | head -3
# Shows only: [first 3 Python processes]
```

### Part 2: Output Redirection (> vs >>)

```bash
# > (Overwrite)
echo "Line 1" > file.txt    # file.txt now contains only "Line 1"
echo "Line 2" > file.txt    # file.txt is overwritten; now contains only "Line 2"

# >> (Append)
echo "Line 1" >> file.txt   # file.txt contains "Line 1"
echo "Line 2" >> file.txt   # file.txt now contains "Line 1\nLine 2"
```

### Part 3: Conditional Execution (&& and ||)

```bash
# && (AND — run if previous succeeds)
npm install && npm start
# If npm install succeeds, THEN run npm start
# If npm install fails, npm start does NOT run

# || (OR — run if previous fails)
npm start || echo "Failed"
# If npm start fails, THEN print "Failed"
# If npm start succeeds, echo does NOT run
```

---

## Common Scenarios

### Scenario 1: Agent Shows A Complex Command
```bash
# Agent suggests:
find . -name "*.log" -type f | xargs grep "ERROR" | sort | uniq -c | sort -rn

# Break it down:
find . -name "*.log" -type f          # Find all log files
| xargs grep "ERROR"                 # Search each for "ERROR"
| sort                               # Sort results alphabetically
| uniq -c                            # Count unique lines
| sort -rn                           # Sort by count (highest first)

# Result: Most common errors first
```

### Scenario 2: Search And Count Results
```bash
# How many Python files do we have?
find . -name "*.py" | wc -l

# How many errors in the log?
grep ERROR app.log | wc -l

# How many times is a function used?
grep -r "calculate_total" . | wc -l
```

### Scenario 3: Save Results For Later
```bash
# Find all TODO comments and save to file
grep -r "TODO" . > todos.txt

# View what was saved
cat todos.txt
```

### Scenario 4: Conditional Deploy
```bash
# Only deploy if tests pass
npm test && npm run deploy

# If test fails, deployment doesn't happen
# If test succeeds, deployment runs automatically
```

---

## Reading a Complex Command

**Strategy: Read left to right, understand each part, trace the data flow**

**Example: `ps aux | grep python | grep -v grep | wc -l`**

1. `ps aux` — List all running processes
2. `| grep python` — Filter to lines containing "python"
3. `| grep -v grep` — Remove the grep command itself from results
4. `| wc -l` — Count the remaining lines

**Result**: Number of Python processes running (excluding the grep search itself)

---

## Red Flags to Watch

If your agent suggests:
- ⚠️ Complex piped command you don't understand → Ask: "Explain each part of this"
- ✅ Using `&&` to run multiple commands safely → Good practice
- ⚠️ `> file.txt` when you want to preserve the original → Should be `>> file.txt`
- ⚠️ Piping to `rm` without verification → Ask: "Can we check what would be deleted first?"
- ✅ `| head -5` to preview before running full command → Safe exploration

---

## Try With AI

Use your AI companion tool set up (e.g., ChatGPT web, Claude Code, Gemini CLI), you may use that instead—the prompts are the same.

### Prompt 1: Understand Pipes
```
Explain what these commands do:
1. cat file.txt | grep "error"
2. ls -la | grep ".py" | wc -l
3. ps aux | grep python

For each one:
- What does the first command produce?
- What does the pipe (|) do?
- What does the second command receive?
- What's the final output?
```

**Expected outcome**: Understand pipe as "send output from one to input of another."

### Prompt 2: Chain Commands To Solve A Problem
```
I have a project with many log files.
I need to:
1. Find all .log files
2. Search each one for "ERROR"
3. Count how many errors total
4. Save results to a file called error_report.txt

Show me the piped command to do this.
Explain what each part does.
```

**Expected outcome**: See how complex tasks are built from simple parts.

### Prompt 3: Verify Safety Before Running
```
Before running this command, explain what it does:
npm install && npm test && npm run deploy

What happens if:
- npm install fails?
- npm test fails?
- npm test succeeds?

Should we add error handling?
```

**Expected outcome**: Learn to verify logic before executing, especially for important commands.
