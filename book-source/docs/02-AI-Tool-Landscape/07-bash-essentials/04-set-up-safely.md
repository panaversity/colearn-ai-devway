---
sidebar_position: 4
title: "Set Up Safely — Environment & Configuration"
---

# Set Up Safely — Environment & Configuration

## What You're Trying to Do

Your project needs secrets: API keys, database passwords, authentication tokens. Your CLI Coding Agent will suggest ways to set these up. You need to understand where these secrets go and how to keep them safe from being committed to git (and exposed on GitHub).

---

## The Bash Commands

### Display Environment Variables (What's Set?)
```bash
echo $HOME              # Show your home directory path
echo $PATH             # Show where the system looks for programs
printenv               # List all environment variables
printenv | grep API    # Find variables containing "API"
env                    # Another way to list all variables
```

**Example output from `printenv`:**
```
HOME=/Users/yourname
PATH=/usr/local/bin:/usr/bin:/bin
PYTHONPATH=/usr/local/lib/python
API_KEY=sk-abc123xyz...
```

### Set Temporary Environment Variables (This Session Only)
```bash
export API_KEY="your-secret-key-here"    # Set variable for this session
export DATABASE_URL="postgres://..."     # Set database connection
export NODE_ENV="production"             # Set environment type
```

**Important:** Variables set with `export` only last while your terminal is open. Once you close the terminal, they're gone.

### Set Permanent Environment Variables (Survive Restart)
```bash
nano ~/.bashrc                     # Edit your bash configuration (macOS/Linux)
nano ~/.zshrc                      # Edit your zsh configuration (newer macOS)
source ~/.bashrc                   # Load the changes immediately
```

**What to add to `~/.bashrc` or `~/.zshrc`:**
```bash
export API_KEY="your-secret-key-here"
export DATABASE_URL="postgres://..."
export NODE_ENV="production"
```

### Load a Configuration File (`.env` Files)
```bash
source .env                        # Load variables from .env file in current folder
cat .env                           # View what's in the .env file
```

---

## How to Ask Your CLI Coding Agent

| What You Want | What to Ask Your Agent |
|---|---|
| Set up API keys | "How should I store my API key for this project?" |
| Hide secrets from git | "I don't want this API key committed to GitHub. How do I set that up?" |
| Understand environment variables | "Explain what this export command does and where it stores the value" |
| Configure a service | "Set up the environment variables for connecting to the database" |
| Check what's configured | "What environment variables are currently set?" or "Show me the contents of the .env file" |

**Example conversation:**
```
You: "I have an API key I need to use. How should I set it up?"
Agent: "I recommend creating a .env file and using it with your project. Don't commit it to git. Should I show you how?"
You: "Yes, please set it up safely"
Agent: "First, I'll create .env with your API key, then add .env to .gitignore to prevent accidents"
```

---

## Why This Matters for Your Product

- **Security first**: Secrets in code = security breach. Secrets in environment = safe
- **No accidents**: If you hardcode API keys in code, they go to GitHub. Then they're public. Then attackers can use them
- **Team collaboration**: Other developers can't see your real keys, but your project still works
- **Easy rotation**: When you need to change a key, update one place (not hunt through code)
- **Professional practice**: Every real project does this

---

## The Safety Pattern: Never Hardcode Secrets

### ❌ WRONG — Secret in Code
```python
api_key = "sk-abc123xyz"  # This goes to GitHub if you commit it
response = requests.get(url, headers={"Authorization": api_key})
```

### ✅ CORRECT — Secret in Environment
```python
import os
api_key = os.getenv("API_KEY")  # Read from environment, not code
response = requests.get(url, headers={"Authorization": api_key})
```

### Setup Process
```bash
# 1. Create a .env file (NOT committed to git)
echo 'API_KEY="sk-abc123xyz"' > .env

# 2. Add .env to .gitignore (prevent accidental commits)
echo ".env" >> .gitignore

# 3. Your code reads from the environment, not from the file
# (Your agent will set this up for you)

# 4. In your code:
api_key = os.getenv("API_KEY")  # Python
const apiKey = process.env.API_KEY  # Node.js
echo $API_KEY  # Bash
```

---

## Common Scenarios

### Scenario 1: Your Agent Says "Set This Environment Variable"
```bash
# Your agent suggests:
export OPENAI_API_KEY="sk-proj-abc123..."

# This means:
1. Temporarily set this variable for your current session
2. Your code can now access it with os.getenv("OPENAI_API_KEY")
3. When you close the terminal, the variable is gone
```

### Scenario 2: You Want This to Persist Across Sessions
```bash
# Option 1: Add to your shell config (~/.bashrc or ~/.zshrc)
nano ~/.bashrc
# Add this line:
export API_KEY="your-key"
# Save and exit, then:
source ~/.bashrc

# Option 2: Use a .env file and load it in your project setup
# (Your agent will usually do this for you)
```

### Scenario 3: Check If a Variable Is Set
```bash
echo $API_KEY              # Shows the value (or nothing if not set)
printenv | grep API_KEY    # Searches for variables with API_KEY in name
```

---

## Red Flags to Watch

If your agent suggests:
- ❌ Putting a secret directly in code → Ask: "Can we use environment variables instead?"
- ❌ Committing a `.env` file → Ask: "Shouldn't we add .env to .gitignore?"
- ❌ Hardcoding database credentials → Ask: "Can we read this from the environment?"
- ✅ Creating a `.env.example` file (without real values) → This is good; it shows other developers what variables they need

---

## Try With AI

**Tool**: Claude Code, Gemini CLI, or ChatGPT Web

### Prompt 1: Understand Environment Variables
```
Explain what happens when I run this:
export API_KEY="sk-12345"

Then:
- Where does this value go?
- How long does it stay set?
- How would my code access it?
- What happens when I close the terminal?
```

**Expected outcome**: Understand that export makes variables available to your program in the current session only.

### Prompt 2: Safe Secret Storage
```
I have an API key I need to use in my project.
Show me the safest way to store it so that:
1. It's not in the code
2. It's not committed to git
3. My code can still access it

What files would you create? What would go in each?
```

**Expected outcome**: See `.env` file pattern and `.gitignore` setup.

### Prompt 3: Practical Setup
```
Help me set up my project with these environment variables:
- OPENAI_API_KEY=sk-proj-abc123...
- DATABASE_URL=postgresql://...
- NODE_ENV=development

Show me:
1. How to set these up temporarily (for this session)
2. How to make them persistent (survive terminal restart)
3. How to verify they're set correctly
```

**Expected outcome**: Learn both temporary and permanent configuration methods.
