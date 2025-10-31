---
sidebar_position: 8
title: "Lesson 8: Capstone - Real Project Setup and Troubleshooting"
---

# Lesson 8: Capstone — Try With AI, Real Project Setup and Troubleshooting

**Duration**: 50 minutes
**Prerequisites**: All Lessons 1-7 completed

---

## The Capstone Challenge

You've learned:
- ✅ Why bash matters (Lesson 1)
- ✅ The AI Collaboration Pattern (Lesson 2)
- ✅ File navigation and paths (Lesson 3)
- ✅ File operations safely (Lesson 4)
- ✅ Configuration and environment (Lesson 5)
- ✅ Packages and dependencies (Lesson 6)
- ✅ Pipes and complex commands (Lesson 7)

**Now**: Synthesize everything into a real project setup with your AI companion.

---

## What You'll Do in This Lesson

1. **Choose a real project** (Python, Node.js, data analysis—whatever interests you)
2. **Ask your AI companion** (Claude Code or Gemini CLI) to guide you through setup
3. **Apply the 5-step pattern** at each step: Ask → Understand → Verify → Execute → Learn
4. **Handle real errors** when they occur (they will—and that's the learning!)
5. **Complete a working setup** that's ready for real development

**By the end**: You'll have a real project folder that works, and you'll understand every bash command that created it.

---

## The Real Workflow: Start to Finish

### Step 1: Decide on Your Project (2 min)

Choose one of these (or your own idea):

**Option A: Python Data Analysis Project**
```
Goal: Create a Python project for analyzing CSV data
Needs: Python 3.13+, pandas, numpy, jupyter
Tools: Claude Code or Gemini CLI
```

**Option B: Node.js Web Server**
```
Goal: Create a web server with Express
Needs: Node.js, npm, express, cors
Tools: Claude Code or Gemini CLI
```

**Option C: Python Web Scraper**
```
Goal: Create a web scraping project
Needs: Python, requests, beautiful soup, git
Tools: Claude Code or Gemini CLI
```

**Pick one and write it down. This is your capstone project.**

---

### Step 2: Ask Your AI Companion for Help (5 min)

**Open Claude Code** (or Gemini CLI) and ask:

```
I'm setting up a [PROJECT NAME] project with [TECHNOLOGY].

Here's what I want:
- [Goal 1]
- [Goal 2]
- [Goal 3]

Walk me through the setup step-by-step. Before each command,
explain what it does. I'll ask questions if I don't understand something.
```

**Example**:
```
I'm setting up a Python data analysis project.
I want to:
- Create a project folder with src/, data/, and notebooks/
- Set up a Python virtual environment
- Install pandas, numpy, and jupyter
- Configure it to use my ANTHROPIC_API_KEY

Walk me through the setup step-by-step.
```

**What your AI will do**: Provide a plan with step-by-step commands.

---

### Step 3: Apply the 5-Step Pattern at Each Step (25 min)

For each command your AI suggests, follow this pattern:

#### Step 3a: ASK (Understand the Goal)

Your AI says: **"First, let's create the project structure. I'll run: `mkdir -p data_project/{src,data,notebooks}`"**

You ask: **"What does this command do?"**

#### Step 3b: UNDERSTAND (Read the Explanation)

AI responds: **"mkdir -p creates directories. The flag -p creates parent directories too. The braces {src,data,notebooks} create three folders at once inside data_project."**

You understand: *"So after this command, I'll have data_project/ with three subfolders inside."*

#### Step 3c: VERIFY (Check for Safety)

You think: *"Is this safe? Will it affect anything else? Am I in the right location?"*

If unsure, ask: **"Should I run pwd first to verify my location?"**

#### Step 3d: EXECUTE (Run It)

```bash
$ mkdir -p data_project/{src,data,notebooks}
```

Watch it happen. Observe the result.

#### Step 3e: LEARN (Reflect)

```bash
$ ls -la data_project/
# Output shows the three folders were created

You think: "Perfect! The command worked exactly as expected. I can reuse this pattern for other projects."
```

---

### Step 4: Handle Real Errors (When They Occur) (10 min)

You'll likely hit an error. **This is expected and valuable.**

**Common errors**:

#### Error 1: Command Not Found

```bash
$ python3.13 -c "import pandas"
# Error: command not found: python3.13
```

**What to do**:
1. Don't panic—this is learnable
2. Ask your AI: **"I got this error: command not found: python3.13. What does it mean?"**
3. AI explains: **"Python 3.13 isn't installed or isn't in your PATH. Try `which python` to see what's available."**
4. Follow up: **`which python`** → see what you have
5. Adjust: Use the Python version you have, or install the one you need

#### Error 2: Module Not Found

```bash
$ python -c "import pandas"
# Error: ModuleNotFoundError: No module named 'pandas'
```

**What to do**:
1. Ask your AI: **"I installed pandas but it's not found. Why?"**
2. AI explains: **"You might have multiple Python versions. Try: `python -m pip install pandas`"**
3. Then test again: **`python -c "import pandas"`**

#### Error 3: Permission Denied

```bash
$ npm install -g express
# Error: permission denied (trying to write to /usr/local)
```

**What to do**:
1. Ask your AI: **"I got permission denied. What should I do?"**
2. AI suggests: **"Either use sudo, or install locally: `npm install express` (without -g)"**
3. Choose based on your need

---

### Step 5: Verify Your Setup Works (5 min)

After completing all steps, verify everything:

```bash
# Check project structure
$ pwd
/Users/myname/data_project

$ ls -la
(shows src/, data/, notebooks/ folders)

# Check Python/packages
$ python --version
Python 3.13.0

$ pip list | grep pandas
pandas  2.0.0

# Check environment variables
$ echo $ANTHROPIC_API_KEY
sk-ant-v5-... (not shown for security, but it's there)

# Optional: Run a quick test
$ python -c "import pandas; import numpy; print('All imports work!')"
All imports work!
```

**Success**: Your project is ready for real development.

---

## Real Example: Python Data Analysis Project Setup

Here's what a real setup conversation might look like:

### The Conversation

```
You: I'm setting up a Python data analysis project.
     Walk me through the setup.

Claude: Great! Here's what we'll do:
        1. Create project structure
        2. Set up virtual environment
        3. Install packages
        4. Configure environment variables
        5. Run a test to verify

        Ready?

You: Yes, let's start.

Claude: Step 1: Create the structure
        $ mkdir -p analysis_project/{src,data,notebooks}

        This creates:
        analysis_project/
        ├── src/
        ├── data/
        └── notebooks/

You: Clear. What's next?

Claude: Step 2: Navigate and create virtual environment
        $ cd analysis_project
        $ python -m venv venv

        This creates an isolated Python environment.

You: Should I verify this worked?

Claude: Good thinking! Run:
        $ ls -la

        You should see a venv/ folder.

You: [runs ls -la, sees venv folder] Got it!

Claude: Step 3: Activate the virtual environment
        $ source venv/bin/activate

        Your prompt will change to show (venv) at the start.

You: [activates, sees prompt change] Great!

Claude: Step 4: Install packages
        $ pip install pandas numpy scikit-learn jupyter

        This will install multiple packages (many dependencies).

You: [watches installation complete] Done!

Claude: Step 5: Verify
        $ python -c "import pandas; import numpy; print('Success!')"

        You should see: Success!

You: [runs verification, sees "Success!"] Perfect!

Claude: Your project is set up and ready. You can now start analyzing data!
```

---

## Troubleshooting a Real Error

**Scenario**: You activate the virtual environment, but pip install fails.

```bash
$ source venv/bin/activate
(venv) $ pip install pandas
# Error: ERROR: Could not find a version that satisfies the requirement pandas

You: Claude, I'm getting an error. What should I do?

Claude: That's odd. Let's troubleshoot:
        1. First, verify pip is working: pip --version
        2. Try updating pip: pip install --upgrade pip
        3. Then try again: pip install pandas

You: [runs pip --version] pip 23.0
You: [runs pip install --upgrade pip]
You: [runs pip install pandas]
(Success this time!)

Claude: Great! This sometimes happens with older pip versions.
        You've learned a valuable troubleshooting skill.
```

---

## Verification & Reflection (3 min)

**After your project is set up**, answer these questions:

1. **What did you learn?**
   - "I learned how to create a project structure from scratch"
   - "I understand what virtual environments do"
   - "I can troubleshoot package installation errors"

2. **What was surprising?**
   - "More packages were installed than I expected (dependencies!)"
   - "Virtual environment keeps Python isolated per project"
   - "Error messages are actually helpful when you read them"

3. **What would you do differently next time?**
   - "I'd backup before running rm -rf"
   - "I'd ask more questions before executing unfamiliar commands"
   - "I'd check error messages more carefully"

4. **How confident are you now?**
   - "I can set up a new project from scratch"
   - "I can troubleshoot when things go wrong"
   - "I understand what my AI is doing and why"

---

## Try With AI: The Capstone Workflow

**This is the real capstone—you use your AI companion to set up an actual project.**

### Your Task

1. **Open Claude Code or Gemini CLI** (the tool you set up in Chapter 5 or 6)

2. **Describe your project**:
   ```
   I'm ready to set up a real [PROJECT] project.
   I've learned bash basics and I'm ready to apply them.

   Here's what I want to build:
   [Your project description]

   Walk me through the complete setup step-by-step.
   At each step, tell me what you're doing and why.
   I'll ask questions about anything I don't understand.
   ```

3. **Follow the 5-step pattern** for each step

4. **Ask questions freely**:
   - "What does this do?"
   - "Is this safe?"
   - "Should we backup first?"
   - "Why are multiple packages being installed?"

5. **Handle errors**: When they occur (and they will), work with your AI to understand and fix them

6. **Celebrate success**: When your project is set up and working, you've completed the capstone!