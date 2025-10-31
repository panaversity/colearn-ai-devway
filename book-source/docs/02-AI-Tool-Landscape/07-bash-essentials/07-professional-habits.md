---
sidebar_position: 7
title: "Professional Bash Habits and Command Patterns"
---

# Professional Bash Habits and Command Patterns

**Duration**: 30-35 minutes

## Introduction

You know the commands. Now learn the efficiency techniques that professionals use: keyboard shortcuts, aliases, history search, and pattern recognition.

---

## Part 1: Keyboard Shortcuts

| Shortcut | Action | Use Case |
|----------|--------|----------|
| **Ctrl+R** | Search command history | Find that long command you ran yesterday |
| **Tab** | Auto-complete | Avoid typos in filenames |
| **Ctrl+A** | Jump to line start | Fix command at beginning |
| **Ctrl+E** | Jump to line end | Append to command |
| **Ctrl+U** | Clear line | Restart typing |
| **Ctrl+L** | Clear screen | Remove clutter |
| **↑/↓** | Navigate history | Repeat recent commands |

---

## Part 2: Command History

### Using history

```bash
# View command history
history

# Run command #123
!123

# Run last command
!!

# Run last command with sudo
sudo !!

# Search history with Ctrl+R
# Press Ctrl+R, type search term
```

---

## Part 3: Aliases

### Creating Shortcuts

```bash
# Add to ~/.bashrc or ~/.zshrc
alias ll='ls -lah'
alias gs='git status'
alias python=python3

# Reload config
source ~/.bashrc

# Now you can use:
ll     # Instead of ls -lah
gs     # Instead of git status
```

---

## Part 4: Common Command Patterns

### Pattern 1: Find and Act

```bash
# Find all .log files and delete them
find . -name "*.log" -delete

# Find Python files and count lines
find . -name "*.py" -exec wc -l {} +
```

### Pattern 2: Search and Filter

```bash
# Find errors, count them
grep "ERROR" log.txt | wc -l

# Find unique errors
grep "ERROR" log.txt | sort | uniq
```

### Pattern 3: Monitor and React

```bash
# Watch log file for errors in real-time
tail -f server.log | grep "ERROR"
```

---

## Part 5: When to Memorize vs. Ask AI

| Criterion | Memorize | Ask AI |
|-----------|----------|--------|
| **Frequency** | Daily (`cd`, `ls`, `git status`) | Rare/one-time |
| **Complexity** | Simple (`pwd`, `mkdir`) | Complex/unfamiliar |
| **Risk** | Low (`cat`, `echo`) | High (`rm -rf`) — verify! |
| **Learning Goal** | Core skills | Exploratory |

**Guideline:**
- Use > 5 times? Memorize it.
- Complex or risky? Ask AI, but verify.
- Exploring? Ask AI to learn patterns.

---

## Part 6: Safety Awareness

### Dangerous Commands (Always Verify)

```bash
# ❌ Permanent deletion
rm -rf directory/

# ❌ Insecure permissions
chmod 777 file.txt

# ❌ Running remote scripts
curl http://site.com/script.sh | bash
```

**Before running ANY destructive command:**
1. Run `pwd` — know where you are
2. Run `ls` — see what's here
3. Test pattern first — `ls temp*` before `rm temp*`
4. Have backups — use Git, copy important files

---

## Practice Exercises

### Exercise 1: Keyboard Shortcuts

1. Type a long command
2. Press Ctrl+A (jump to start)
3. Press Ctrl+E (jump to end)
4. Press Ctrl+R and search for "python"
5. Press Ctrl+U to clear

### Exercise 2: Create Aliases

Add to `.bashrc`:
```bash
alias projects='cd ~/projects'
alias ll='ls -lah'
```

Reload and test:
```bash
source ~/.bashrc
projects
ll
```

### Exercise 3: Command Patterns

1. Find all `.txt` files in your home directory
2. Count how many there are
3. Move them to a `text-files` folder

---

## Summary

- Use keyboard shortcuts to work faster (Ctrl+R, Tab, Ctrl+A/E/U)
- Create aliases for frequently-used commands
- Search command history with Ctrl+R
- Memorize common patterns (find & act, search & filter)
- Decide when to memorize vs. ask AI (frequency, complexity, risk)
- Always verify dangerous commands before execution

**Professional habit**: Spend 5 minutes now to set up aliases and practice shortcuts. It will save hours over the next year.

**Next**: [Lesson 8: Real-World AI-Assisted Workflows →](./08-real-world-workflows.md)
