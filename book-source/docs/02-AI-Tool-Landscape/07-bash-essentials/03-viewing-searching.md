---
sidebar_position: 3
title: "Viewing and Searching File Content"
---

# Viewing and Searching File Content

**Duration**: 30-35 minutes

## Opening: From File Management to File Analysis

You can navigate directories and create files—but what if you need to inspect a 10,000-line log file? Search for a specific error message across dozens of files? Extract data from text files without opening an editor?

This lesson teaches you to work with file **content**, not just file **names**. You'll learn to read, search, and filter text using commands that are faster and more powerful than any text editor.

**Real-world scenario:** Your AI application crashes. The error logs are 50,000 lines. You need to find all instances of "ERROR" in the last hour. Opening this file in a text editor would freeze your computer. Using Bash commands, you'll find the errors in seconds.

---

## Part 1: Reading File Contents

### Command 1: `cat` — Display Entire File

**What it does:** Prints all content of a file to the terminal.

**Syntax:**
```bash
cat <filename>
```

**Example:**
```bash
cat README.md
# Output: (entire file displayed)
```

**When to use:** Small files you want to view quickly.

**When NOT to use:** Large files (use `less` or `head`/`tail` instead).

---

### Command 2: `head` — Show First Lines

**What it does:** Displays the first 10 lines (or specified number).

**Syntax:**
```bash
head <filename>       # First 10 lines
head -n 20 <filename> # First 20 lines
```

**Example:**
```bash
head server.log
# Output: First 10 lines of server.log

head -n 5 README.md
# Output: First 5 lines of README
```

**When to use:** Preview the beginning of a large file.

---

### Command 3: `tail` — Show Last Lines

**What it does:** Displays the last 10 lines (or specified number).

**Syntax:**
```bash
tail <filename>       # Last 10 lines
tail -n 20 <filename> # Last 20 lines
tail -f <filename>    # Follow file (show new lines as they're added)
```

**Example:**
```bash
tail error.log
# Output: Last 10 lines of error.log

# Monitor log file in real-time
tail -f server.log
# Press Ctrl+C to stop
```

**When to use:**
- Check end of log files (most recent entries)
- Monitor live logs with `-f` (follow mode)

---

### Command 4: `less` — Browse File Interactively

**What it does:** Opens file in a scrollable viewer.

**Syntax:**
```bash
less <filename>
```

**Navigation inside `less`:**
- **Scroll down**: Space bar or `d`
- **Scroll up**: `b`
- **Search**: `/` then type search term, press Enter
- **Next match**: `n`
- **Previous match**: `N`
- **Quit**: `q`

**Example:**
```bash
less documentation.md
# Opens documentation.md in viewer
# Press '/' to search, 'q' to quit
```

**When to use:** Large files you want to navigate and search interactively.

---

## Part 2: Searching File Content

### Command 5: `grep` — Search for Patterns

**What it does:** Finds lines containing a specific pattern.

**Syntax:**
```bash
grep "pattern" <filename>        # Search in one file
grep "pattern" file1 file2       # Search in multiple files
grep -r "pattern" directory/     # Search recursively in directory
grep -i "pattern" <filename>     # Case-insensitive search
```

**Examples:**

```bash
# Find all lines containing "error" in log file
grep "error" app.log

# Case-insensitive search (matches ERROR, Error, error)
grep -i "error" app.log

# Search for "TODO" in all Python files in current directory
grep "TODO" *.py

# Search recursively in all files in src/ directory
grep -r "function_name" src/
```

**Common flags:**
- `-i`: Case-insensitive
- `-r`: Recursive (search subdirectories)
- `-n`: Show line numbers
- `-v`: Invert match (show lines that DON'T match)
- `-c`: Count matches

**Real-world example:**

```bash
# Count how many times "ERROR" appears in logs
grep -c "ERROR" server.log
# Output: 142

# Find errors with line numbers
grep -n "ERROR" server.log
# Output:
# 45:ERROR: Database connection failed
# 98:ERROR: API timeout
```

---

## Part 3: Pipes and Redirection

### Concept: Chaining Commands with Pipes (`|`)

**Pipes** let you connect commands: output of command 1 becomes input of command 2.

**Syntax:**
```bash
command1 | command2
```

**Examples:**

```bash
# Count how many files are in directory
ls | wc -l
# Output: 15

# Find all Python files, then count them
ls | grep ".py" | wc -l
# Output: 8

# Show errors in log file, then display first 5
grep "ERROR" server.log | head -5
```

**Analogy:** Think of pipes like an assembly line. Each command does one task and passes the result to the next.

---

### Redirection: Saving Output to Files

**Redirect output** using `>` (overwrite) or `>>` (append).

**Syntax:**
```bash
command > file.txt   # Save output to file (overwrite)
command >> file.txt  # Append output to file
command 2> errors.txt # Save errors to file
```

**Examples:**

```bash
# Save directory listing to file
ls -la > directory-contents.txt

# Append current date to log
date >> activity.log

# Save only error messages
python script.py 2> errors.txt
```

**Common mistake:**
```bash
# ❌ This deletes file contents then tries to process it
cat file.txt > file.txt
# File becomes empty!

# ✅ Use a different output filename
cat file.txt > file-copy.txt
```

---

## Part 4: Finding Files

### Command 6: `find` — Search for Files by Name/Properties

**What it does:** Searches for files matching criteria.

**Syntax:**
```bash
find <directory> -name "<pattern>"
find <directory> -type f    # Find files
find <directory> -type d    # Find directories
```

**Examples:**

```bash
# Find all Python files in current directory and subdirectories
find . -name "*.py"

# Find all files modified in last 24 hours
find . -type f -mtime -1

# Find files larger than 100MB
find . -type f -size +100M

# Find and delete all .tmp files (use with caution!)
find . -name "*.tmp" -delete
```

**Real-world example:**

```bash
# Find all JSON config files in project
find . -name "*.json" -type f
# Output:
# ./config/settings.json
# ./data/sample.json
# ./tests/test-config.json
```

---

## Part 5: Combining Everything — Real-World Example

**Scenario:** You have a log file (`server.log`) and need to:
1. Find all ERROR messages
2. Count how many there are
3. Save them to a separate file
4. Show the first 10 errors

**Solution:**

```bash
# Step 1: Find all ERROR lines
grep "ERROR" server.log

# Step 2: Count errors
grep "ERROR" server.log | wc -l
# Output: 87

# Step 3: Save errors to file
grep "ERROR" server.log > errors.txt

# Step 4: Show first 10 errors
grep "ERROR" server.log | head -10

# Or chain everything: count and save simultaneously
grep "ERROR" server.log | tee errors.txt | wc -l
# 'tee' writes to file AND passes output to next command
```

---

## Practice Exercises

### Exercise 1: Reading Files (Beginner)

**Setup:**
```bash
echo "Line 1\nLine 2\nLine 3\nLine 4\nLine 5" > test.txt
```

**Tasks:**
1. Display the entire file with `cat`
2. Show first 2 lines with `head`
3. Show last 2 lines with `tail`
4. Browse the file with `less`

---

### Exercise 2: Searching for Patterns (Intermediate)

**Setup:**
```bash
echo "ERROR: Connection failed\nINFO: Server started\nERROR: Timeout\nWARNING: Low memory\nERROR: Invalid input" > app.log
```

**Tasks:**
1. Find all lines containing "ERROR"
2. Count how many ERROR lines there are
3. Find all lines that DON'T contain "ERROR" (hint: `-v` flag)
4. Save all ERROR lines to a new file `errors-only.log`

**Expected commands:**
```bash
grep "ERROR" app.log
grep -c "ERROR" app.log
grep -v "ERROR" app.log
grep "ERROR" app.log > errors-only.log
```

---

### Exercise 3: Pipes and Chaining (Intermediate)

**Tasks:**
1. List all files in current directory
2. Pipe the output to `grep` to find only `.txt` files
3. Count how many `.txt` files there are

**Expected commands:**
```bash
ls
ls | grep ".txt"
ls | grep ".txt" | wc -l
```

---

### Exercise 4: Finding Files (Advanced)

**Tasks:**
1. Find all Python files (`.py`) in your home directory
2. Find all files modified in the last day
3. Find all files larger than 1MB in your Downloads folder

**Expected commands:**
```bash
find ~ -name "*.py"
find ~ -type f -mtime -1
find ~/Downloads -type f -size +1M
```

---

## Reflection and Key Takeaways

### Pause and Reflect

1. **When would you use `grep` instead of opening a file in a text editor?** (When searching large files or multiple files simultaneously)
2. **What's the difference between `>` and `>>`?** (`>` overwrites, `>>` appends)
3. **Why are pipes powerful?** (They let you chain simple commands into complex workflows)

### What You've Accomplished

You can now:
- ✅ Read file contents with `cat`, `head`, `tail`, `less`
- ✅ Search for patterns in files with `grep`
- ✅ Chain commands together with pipes (`|`)
- ✅ Redirect output to files (`>`, `>>`)
- ✅ Find files by name or properties with `find`
- ✅ Build complex workflows by combining commands

---

## Next Steps: Forward Bridge to Lesson 4

You can navigate, manage files, and search content. But every time you restart your terminal, your environment resets. API keys vanish. Custom settings disappear.

**In Lesson 4: Environment Variables and Package Management**, you'll learn to:
- Store configuration that persists across sessions
- Set up API keys for AI tools
- Install Python packages and manage dependencies
- Install system-level tools with package managers

**Preview question:** How would you store an API key so it's available every time you open a terminal? Lesson 4 shows you how to configure your shell permanently.

---

## Summary

In this lesson, you learned:

- **Reading files**: `cat`, `head`, `tail`, `less`
- **Searching content**: `grep` with flags (`-i`, `-r`, `-n`, `-c`)
- **Pipes**: Chaining commands with `|`
- **Redirection**: Saving output with `>` and `>>`
- **Finding files**: `find` by name, type, size, modification time
- **Real-world workflows**: Combining commands to analyze logs and search projects

**Key insight:** The power of Bash isn't in individual commands—it's in **combining them** to build workflows that would be impossible in a GUI.

---

**Next lesson**: [Lesson 4: Environment Variables and Package Management →](./04-environment-packages.md)
