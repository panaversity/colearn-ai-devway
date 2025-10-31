---
sidebar_position: 4
title: "Environment Variables and Package Management"
---

# Environment Variables and Package Management

**Duration**: 35-40 minutes

## Introduction

Every development environment requires configuration (API keys, paths, preferences) and software packages (libraries, tools). This lesson teaches you to set environment variables and install packages.

---

## Part 1: Environment Variables

### Temporary Variables

```bash
# Set for current session only
export API_KEY="your-key-here"

# View variable
echo $API_KEY

# See all variables
env
```

### Permanent Variables

Edit `.bashrc` (Linux/Git Bash) or `.zshrc` (macOS):

```bash
# Open file
nano ~/.bashrc

# Add at bottom:
export API_KEY="your-key-here"

# Save (Ctrl+O, Enter, Ctrl+X)

# Reload
source ~/.bashrc
```

### API Key Setup Walkthrough

```bash
# 1. Open config file
nano ~/.bashrc

# 2. Add API key
export OPENAI_API_KEY="sk-proj-..."

# 3. Save and reload
source ~/.bashrc

# 4. Verify
echo $OPENAI_API_KEY
```

---

## Part 2: Python Package Management

### pip Basics

```bash
# Install package
pip install requests

# Install specific version
pip install requests==2.31.0

# List installed
pip list

# Uninstall
pip uninstall requests
```

### Virtual Environments

```bash
# Create venv
python -m venv venv

# Activate (Mac/Linux)
source venv/bin/activate

# Activate (Windows Git Bash)
source venv/Scripts/activate

# Install packages in venv
pip install openai

# Deactivate
deactivate
```

---

## Part 3: Node.js Package Management

```bash
# Initialize project
npm init -y

# Install package
npm install axios

# Install dev dependency
npm install --save-dev eslint

# Install from package.json
npm install
```

---

## Part 4: System Package Managers

### Homebrew (macOS)

```bash
brew install git
brew install python
brew update
brew upgrade
```

### apt (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git
sudo apt install python3
```

---

## Practice Exercises

**Exercise 1**: Set temporary and permanent environment variables  
**Exercise 2**: Create Python virtual environment and install packages  
**Exercise 3**: Set up API key and test with Python script

---

## Summary

- Set temporary variables with `export`
- Make variables permanent in `.bashrc`/`.zshrc`
- Install Python packages with `pip`
- Use virtual environments to isolate dependencies
- Install Node packages with `npm`
- Install system packages with `brew` or `apt`

**Next**: [Lesson 5: Process Management and Troubleshooting →](./05-processes-troubleshooting.md)
