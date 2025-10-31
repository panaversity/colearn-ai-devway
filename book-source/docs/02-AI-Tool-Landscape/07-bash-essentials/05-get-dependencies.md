---
sidebar_position: 5
title: "Get Dependencies — Install Packages"
---

# Get Dependencies — Install Packages

## What You're Trying to Do

Your project needs code libraries: HTTP clients, database drivers, testing frameworks. Your CLI Coding Agent will suggest commands to install these. You need to understand what's being installed, where it goes, and how to verify installation worked.

---

## The Bash Commands

### Python Package Management (pip)
```bash
pip install requests               # Install a package
pip install requests==2.28.0       # Install specific version
pip install -r requirements.txt    # Install all packages listed in requirements.txt
pip list                           # See what packages are installed
pip show requests                  # Details about a specific package
pip uninstall requests             # Remove a package
pip freeze > requirements.txt      # Save current packages to requirements.txt
```

**Example output from `pip list`:**
```
Package    Version
---------- ---------
requests   2.28.0
flask      2.2.0
pytest     7.1.2
```

### Node.js Package Management (npm)
```bash
npm install express                # Install a package
npm install express@4.18.0         # Install specific version
npm install                        # Install all packages from package.json
npm list                           # See what packages are installed
npm install --save requests        # Install and save to package.json
npm uninstall express              # Remove a package
```

### macOS Package Management (brew)
```bash
brew install postgresql            # Install a package/tool
brew install python@3.10           # Install specific version
brew list                          # See installed packages
brew info postgresql               # Details about a package
brew uninstall postgresql          # Remove a package
```

### Linux Package Management (apt)
```bash
apt-get update                     # Refresh package list
apt-get install python3            # Install a package
apt-get install python3.10         # Install specific version
apt list --installed               # See installed packages
apt-get remove python3             # Remove a package
```

---

## How to Ask Your CLI Coding Agent

| What You Want | What to Ask Your Agent |
|---|---|
| Install required packages | "Install all dependencies for this project" |
| Add a new library | "How do I add the requests library to my project?" |
| See what's installed | "What packages are currently installed?" |
| Check package version | "What version of Flask do we have?" |
| Update packages | "Update all packages to their latest versions" |
| Save installed packages | "Create a requirements.txt with our current packages" |
| Install from requirements | "Install everything in requirements.txt" |

**Example conversation:**
```
You: "This project needs the Flask library. How do I install it?"
Agent: "I'll install it with: $ pip install flask"
[Installation runs]
Agent: "Flask is installed. Would you like me to save it to requirements.txt?"
You: "Yes, do that so other developers know what we need"
Agent: "Done. I added it to requirements.txt"
```

---

## Why This Matters for Your Product

- **Avoid reinventing**: Other developers already solved your problems in libraries. Use them
- **Consistent setup**: requirements.txt or package.json means anyone can set up exactly what you have
- **Team collaboration**: New developers run one command and get everything they need
- **Version control**: Lock specific versions so upgrades don't break your code unexpectedly
- **Deployment**: Production servers install exact same versions you used locally

---

## The Safety Pattern: Always Save Package Lists

### ❌ WRONG — No Record of What's Installed
```bash
pip install requests
pip install flask
pip install pytest
# (Later, new developer joins)
# "What packages do we need?" Nobody knows!
```

### ✅ CORRECT — Package List in Version Control
```bash
# Install packages
pip install requests flask pytest

# Save the list for others
pip freeze > requirements.txt

# Add to git
git add requirements.txt
git commit -m "Add dependencies"

# Another developer can now do:
pip install -r requirements.txt
```

---

## Common Scenarios

### Scenario 1: Your Agent Says "Installing Dependencies"
```bash
pip install -r requirements.txt

# This means:
1. Read the requirements.txt file
2. Download and install each package listed
3. Check that all versions are compatible
4. Place code in your project's library folder
```

### Scenario 2: Your Project Has A Broken Installation
```bash
# First, check what's installed
pip list

# If wrong versions, reinstall:
pip install -r requirements.txt --force-reinstall

# Or uninstall all and start fresh:
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

### Scenario 3: You Want To Use A New Library
```bash
# Tell your agent:
# "I want to add the requests library to my project"

# Agent might do:
pip install requests

# Then save it:
pip freeze > requirements.txt

# Verify it's installed:
pip show requests
```

### Scenario 4: Different Environments Need Different Packages
```bash
# Create separate requirements files:
requirements.txt          # What production needs
requirements-dev.txt      # Extra tools for development (testing, linting)

# Install production packages:
pip install -r requirements.txt

# Install everything (dev + production):
pip install -r requirements-dev.txt
```

---

## Understanding Package Installation

### Where Do Packages Go?
```bash
# Python packages go to your Python library folder:
# macOS/Linux: ~/.local/lib/pythonX.X/site-packages/

# Node.js packages go to:
# node_modules/ folder in your project

# System packages (brew/apt) go to:
# /usr/local/bin or /opt/homebrew/bin
```

### How Do I Know If Installation Worked?
```bash
# Python: Try to import it
python -c "import requests; print(requests.__version__)"

# Node.js: Check package.json
cat package.json | grep requests

# General: List installed packages
pip list | grep requests
npm list | grep requests
```

---

## Red Flags to Watch

If your agent suggests:
- ⚠️ Installing without saving to requirements.txt → Ask: "Should we save this to requirements.txt?"
- ⚠️ `pip install *` → Ask: "What's the *? Can we list the packages specifically?"
- ✅ Creating a requirements-dev.txt for testing tools → This is good practice
- ⚠️ Upgrading packages without checking → Ask: "Will this break our code?"

**Installation Warnings (Usually Safe)**:
- ✅ "warning: pip is configured with locations that require TLS/SSL" → Usually okay
- ✅ "Some packages are not compatible" → Can be fixed, ask agent to resolve
- ⚠️ "ModuleNotFoundError: No module named..." → Package didn't install; ask to retry

---

## Try With AI

**Tool**: Claude Code, Gemini CLI, or ChatGPT Web

### Prompt 1: Understand Package Managers
```
Explain the difference between:
- pip (Python)
- npm (Node.js)
- brew (macOS)
- apt (Linux)

When would I use each one?
Why is having a package manager important for shipping products?
```

**Expected outcome**: Understand that different languages/systems have different package managers.

### Prompt 2: Create a Requirements File
```
I have a Python project with these libraries installed:
- requests
- flask
- pytest
- python-dotenv

Show me:
1. How to create a requirements.txt with these
2. How to add version numbers
3. How another developer would install from this file
```

**Expected outcome**: Learn the requirements.txt pattern that enables team collaboration.

### Prompt 3: Troubleshoot Installation
```
I tried to install a package but got an error.
The error says: "error: invalid syntax"

What could be wrong?
How would you fix it?
What should I check before trying to install again?
```

**Expected outcome**: Learn to read installation errors and understand common causes.
