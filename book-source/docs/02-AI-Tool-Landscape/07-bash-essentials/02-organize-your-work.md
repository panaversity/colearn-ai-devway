---
sidebar_position: 2
title: "Organize Your Work — Create & Manage Files"
---

# Organize Your Work — Create & Manage Files

## What You're Trying to Do

Your project needs structure: folders for code, tests, docs, data. Your CLI Coding Agent will suggest commands to create this structure and manage files. You need to understand what happens to your project files.

---

## The Bash Commands

### Create Folders
```bash
mkdir my-folder              # Create a single folder
mkdir -p my-app/{src,tests,docs}  # Create nested folders at once
```

**Example:**
```bash
mkdir -p project/{src,tests,data}
# Creates: project/
#          ├── src/
#          ├── tests/
#          └── data/
```

### Create Files
```bash
touch filename.txt           # Create an empty file
touch file1.py file2.py      # Create multiple files
```

### Copy Files (Safe — Creates Duplicate)
```bash
cp source.txt backup.txt     # Copy file
cp -r src/ src_backup/       # Copy entire folder and contents
```

### Move/Rename Files
```bash
mv old-name.txt new-name.txt # Rename file
mv file.txt folder/          # Move file to folder
mv -r folder/ new_location/  # Move entire folder
```

### Delete Files (⚠️ Permanent — No Trash)
```bash
rm filename.txt              # Delete file
rm -rf folder/               # Delete folder and everything inside (careful!)
```

---

## How to Ask Your CLI Coding Agent

| What You Want | What to Ask Your Agent |
|---|---|
| Organize your project | "Set up a project structure with src/, tests/, and docs folders" |
| Create essential files | "Create a requirements.txt file in the root" |
| Backup something | "Make a backup copy of my main.py before you modify it" |
| Clean up old files | "Remove the old_code folder" |
| Rename something | "Rename test.py to test_suite.py" |

**Example conversation:**
```
You: "Set up my project structure"
Agent: "I'll create folders for you: $ mkdir -p my_project/{src,tests,docs}"
You: "Before you modify anything, can you back it up?"
Agent: "Good idea. $ cp -r my_project my_project_backup"
```

---

## Why This Matters for Your Product

- **Safety first**: When your agent backs up files before modifying, you have insurance
- **Organization**: Proper structure makes your project easier to navigate and deploy
- **Avoid accidents**: Understanding copy vs. move vs. delete prevents losing code
- **Clear projects**: Well-organized code is easier for your AI partner to understand and modify

---

## Safety Pattern: Always Backup Before Deleting

When your agent suggests deleting anything important:

```bash
# First: Backup
cp -r my_project my_project_backup

# Then: Delete
rm -rf my_project
```

Ask your agent: **"Can we back this up first?"** It's faster than recovering deleted files later.

---

## Red Flags to Watch

If your agent suggests:
- ❌ `rm -rf` without mentioning backup → Ask: "Should we back this up first?"
- ❌ Moving files without verifying destination → Ask: "What's already in the destination folder?"
- ❌ Deleting multiple files at once → Ask: "Can we verify which files are being deleted?"

Your job is to supervise. Ask questions before anything is deleted.

---

## Try With AI

Use your AI companion tool set up (e.g., ChatGPT web, Claude Code, Gemini CLI), you may use that instead—the prompts are the same.

### Prompt 1: Create Project Structure
```
I want to create a new project with this structure:
- my_app/
  - src/
  - tests/
  - docs/
  - data/

Show me the command to create this in one go.
What does each part of the command do?
```

**Expected outcome**: Understand how to create nested folders

### Prompt 2: Understand Backup
```
Before modifying my code, how would you back it up?
Show me the command and explain what it does.
```

**Expected outcome**: See the safety pattern in action

### Prompt 3: Safe Deletion
```
I have a folder called "old_code" I want to delete.
What's the safest way to do this?
Walk me through the steps.
```

**Expected outcome**: Learn the backup-first pattern
