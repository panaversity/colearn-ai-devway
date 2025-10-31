---
sidebar_position: 6
title: "Lesson 6: Find & Fix — Search & Permissions"
---

# Lesson 6: Find & Fix — Search & Permissions

## What You're Trying to Do

Your project has hundreds or thousands of files. You need to find specific code, understand why something isn't working (permissions), or locate config files. Your CLI Coding Agent will suggest commands to search, find, and fix these issues.

---

## The Bash Commands

### Search for Files (Where Is This File?)
```bash
find . -name "config.json"         # Find a file by exact name
find . -name "*.py"                # Find all Python files
find . -type f -name "*.js"        # Find files (not folders) ending in .js
find . -type d -name "node_modules" # Find folders named node_modules
find . -name "test*.py"            # Find files starting with test
```

**Example output from `find . -name "*.py"`:**
```
./src/main.py
./src/utils.py
./tests/test_main.py
./tests/test_utils.py
```

### Search Inside Files (Find Code/Text)
```bash
grep "API_KEY" .env                # Find lines containing API_KEY in .env
grep -r "import requests" src/    # Search for "import requests" in all files in src/
grep -i "error" log.txt           # Case-insensitive search (ERROR, Error, error all match)
grep -n "TODO" main.py            # Show line numbers where TODO appears
grep -c "def " main.py            # Count how many function definitions exist
```

**Example output from `grep -r "API_KEY" .`:**
```
.env:API_KEY=sk-proj-abc123
.env.example:API_KEY=your-key-here
config.py:api_key = os.getenv("API_KEY")
```

### Understand File Permissions (Who Can Do What?)
```bash
ls -la                             # Show files with permissions
ls -la src/                        # Show permissions for files in src/
```

**Understanding the permission output:**
```
-rw-r--r--  1 user staff  1024 Oct 31 10:20 README.md
^ owner can read/write (rw-)
        ^ group can read (r--)
              ^ others can read (r--)
```

### Fix Permissions (Make Files Readable/Executable)
```bash
chmod +x script.sh                # Make script executable
chmod 644 config.json             # Make readable by all (but only owner can write)
chmod 755 src/                    # Standard folder permissions
chmod -R 755 src/                # Change permissions for src/ and everything inside
```

---

## How to Ask Your CLI Coding Agent

| What You Want | What to Ask Your Agent |
|---|---|
| Find a file | "Where is the config.json file?" or "Find all .env files" |
| Find specific code | "Search for all places where we use the API_KEY" |
| Find by pattern | "Find all Python test files" or "What JavaScript files do we have?" |
| Check permissions | "Why can't I run this script?" |
| Fix permissions | "Make this script executable" or "Fix permissions on the src/ folder" |
| Search multiple files | "Search all code files for references to 'database'" |

**Example conversation:**
```
You: "I need to find where we use the API key. Can you search for it?"
Agent: "I'll search for API_KEY in all files: $ grep -r API_KEY ."
[Shows results]
Agent: "Found it in 3 places: .env, config.py, and main.py"
You: "Good, now check if it's hardcoded anywhere"
Agent: "Searching for hardcoded keys... Found one in config.py. Should we fix it?"
```

---

## Why This Matters for Your Product

- **Find bugs fast**: Instead of reading 100 files, search for the problem
- **Understand structure**: What files do you actually have? Where's the test code?
- **Security checks**: Search for hardcoded secrets or insecure patterns
- **Refactoring**: When changing code, find all places that use it
- **Troubleshooting**: Find error messages in logs to debug issues

---

## Common Scenarios

### Scenario 1: Agent Suggests Running A Script But It Fails
```bash
# Error: "Permission denied"
./deploy.sh
# Permission denied: ./deploy.sh

# Agent says: "Let me make it executable"
chmod +x deploy.sh

# Now it works:
./deploy.sh
```

### Scenario 2: Finding Where Something Is Used
```bash
# Agent needs to refactor function name
# But first, find all uses of old name:
grep -r "old_function_name" .

# Output shows:
# src/main.py: result = old_function_name()
# src/utils.py: return old_function_name(data)
# tests/test_main.py: assert old_function_name() == expected

# Now agent knows everywhere to update
```

### Scenario 3: Checking If A File Exists
```bash
# Agent might do:
find . -name "requirements.txt"

# If nothing appears, file doesn't exist
# Then agent says: "requirements.txt not found. Should I create it?"
```

### Scenario 4: Searching Logs For Errors
```bash
# Find error messages in application log:
grep "ERROR" app.log

# Count how many errors:
grep -c "ERROR" app.log

# Show lines with context (before and after):
grep -B2 -A2 "ERROR" app.log
```

---

## Understanding Find and Grep

### `find` — Locate Files by Name
```bash
find . -name "pattern"

# What this means:
# . = search current folder (. = here)
# -name = search by filename
# "pattern" = exact name or wildcard pattern (*.py = all Python files)
```

### `grep` — Search Inside Files
```bash
grep "search_term" filename.txt

# What this means:
# Search for lines containing "search_term"
# In the file named "filename.txt"
# Show the matching lines
```

### `grep -r` — Search Recursively (All Folders)
```bash
grep -r "API_KEY" .

# What this means:
# -r = recursive (include subfolders)
# Search for "API_KEY"
# In all files starting from . (current location)
```

---

## Red Flags to Watch

If your agent suggests:
- ⚠️ `chmod 777` on files → Ask: "Is that secure? Why do we need full permissions?"
- ⚠️ Changing permissions on system folders → Ask: "Could this break something?"
- ✅ `chmod +x script.sh` to make scripts executable → Standard practice
- ✅ `grep -r` to search your code → Good for finding issues
- ⚠️ `rm` based on search results → Ask: "Should we verify what we're deleting first?"

---

## Try With AI

**Tool**: Claude Code, Gemini CLI, or ChatGPT Web

### Prompt 1: Find Files in Your Project
```
I have a project with many files and folders.
Show me:
1. How to find all Python files (.py)
2. How to find all test files
3. How to find files with "config" in the name
4. How to count how many JavaScript files we have

Use the find command to demonstrate each.
```

**Expected outcome**: Learn how to locate files instead of browsing manually.

### Prompt 2: Search Your Code
```
I'm looking for everywhere we use a specific function called "calculate_total".
Show me:
1. How to search all code files for this function
2. How to count how many places use it
3. How to see the context around each use (lines before and after)

Use the grep command.
```

**Expected outcome**: Learn to search code patterns across your project.

### Prompt 3: Understand Permissions
```
I have a script that I can't run. The error is "Permission denied".
Explain:
1. What "Permission denied" means
2. How to check the file's current permissions
3. How to fix it so I can run the script
4. When would I use chmod vs. when is it dangerous?
```

**Expected outcome**: Understand file permissions and when to change them.
