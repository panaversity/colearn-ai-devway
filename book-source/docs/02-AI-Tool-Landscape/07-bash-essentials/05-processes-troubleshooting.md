---
sidebar_position: 5
title: "Process Management and Troubleshooting"
---

# Process Management and Troubleshooting

**Duration**: 30-35 minutes

## Introduction

When processes freeze, consume excessive resources, or throw errors—you need diagnostic tools. This lesson teaches you to monitor, stop, and troubleshoot processes.

---

## Part 1: Viewing Processes

### ps — Process Status

```bash
# Show processes in current terminal
ps

# Show all processes
ps aux

# Find specific process
ps aux | grep python
```

### top — Real-Time Monitoring

```bash
# Start interactive monitor
top

# Press 'q' to quit
# Press 'M' to sort by memory
# Press 'P' to sort by CPU
```

---

## Part 2: Stopping Processes

### kill Commands

```bash
# Graceful termination
kill <PID>

# Force kill
kill -9 <PID>

# Kill all processes by name
killall python
```

### Keyboard Shortcuts

- **Ctrl+C**: Interrupt current process
- **Ctrl+Z**: Suspend process
- `fg`: Resume in foreground
- `bg`: Resume in background

---

## Part 3: Common Errors

### Error 1: "command not found"

**Diagnosis:**
```bash
which python
echo $PATH
```

**Solutions:**
- Use correct command name (`python3` not `python`)
- Install the tool (`brew install python`)
- Add to PATH in `.bashrc`

### Error 2: "permission denied"

**Diagnosis:**
```bash
ls -l script.sh
```

**Solutions:**
```bash
# Add execute permission
chmod +x script.sh

# Or use interpreter directly
bash script.sh

# Or use sudo (if appropriate)
sudo ./script.sh
```

### Error 3: Environment Variable Not Persisting

**Diagnosis:**
```bash
echo $API_KEY
grep API_KEY ~/.bashrc
```

**Solution:**
```bash
nano ~/.bashrc
# Add: export API_KEY="..."
source ~/.bashrc
```

---

## Troubleshooting Decision Tree

```
ERROR?
├─ "command not found" → check 'which', check PATH, install
├─ "permission denied" → check permissions, use chmod +x
├─ Variable missing → check .bashrc, reload with 'source'
└─ Process stuck → find PID with 'ps', kill with 'kill -9'
```

---

## Practice Exercises

**Exercise 1**: Monitor and kill a long-running process  
**Exercise 2**: Diagnose and fix "command not found"  
**Exercise 3**: Fix environment variable persistence

---

## Summary

- Monitor processes with `ps` and `top`
- Terminate processes with `kill` and `kill -9`
- Diagnose "command not found" (PATH, installation)
- Fix "permission denied" (chmod, sudo)
- Make environment variables persistent (.bashrc)

**Next**: [Lesson 6: Natural Language Prompts for Bash →](./06-natural-language-prompts.md)
