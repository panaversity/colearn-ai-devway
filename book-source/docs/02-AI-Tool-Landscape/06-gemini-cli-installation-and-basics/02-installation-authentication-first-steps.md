---
sidebar_position: 2
title: Installation, Authentication & First Steps
---

# Installation, Authentication & First Steps

> **A Word Before We Begin**
> 
> Installing Gemini CLI is like meeting a new colleague—someone who's available 24/7 to help with your work, answer questions, and solve problems. In this lesson, you'll install and launch Gemini CLI, which will then automatically guide you through authentication. You'll be up and running in minutes.


## Prerequisites: What You Need

Make sure you have these before starting:

| Requirement | What It Is | How to Check |
|------------|-----------|-------------|
| **Node.js 20+** | Runtime for JavaScript applications | Open terminal, type: `node --version` |
| **npm** | Package manager (comes with Node.js) | Open terminal, type: `npm --version` |
| **Internet connection** | For installation and Google authentication | You have this already ✓ |
| **Google account** | For secure authentication | Gmail, YouTube, or any Google account |

### Don't Have Node.js 20+?

1. Visit [nodejs.org](https://nodejs.org/en/download)
2. Download the **LTS version** (Long Term Support—the stable version)
3. Follow the installer steps for your operating system
4. When asked about npm, keep the checkbox checked
5. Restart your computer

### Opening Your Terminal

**Windows:** Search "PowerShell" in your Start menu and open it

**macOS:** Press Cmd+Space, type "Terminal", press Enter

**Linux:** Press Ctrl+Alt+T (most distributions)

---

## Installation: One Command

Open your terminal and run this single command:

```bash
npm install -g @google/gemini-cli
```

This command downloads and installs Gemini CLI globally on your computer. You'll see text flowing by—this is normal. Wait for it to complete (usually takes 30-60 seconds).

### Verify Installation

After installation completes, verify it worked:

```bash
gemini -v
```

You should see a version number like `0.4.0` or higher. If you see this, installation is successful! ✓

---

## Authentication & First Launch

Now comes the magic—Gemini CLI handles authentication automatically. Simply type:

```bash
gemini
```

When you run this command for the first time, Gemini CLI launches and **automatically guides you through setup**:

### Step 1: Choose Your Theme

Gemini CLI will ask you to select a visual theme for the terminal interface. Choose whichever you prefer—this is just cosmetic. Use arrow keys to select and press Enter.

### Step 2: Choose Authentication Method

You'll see options for authentication:
- **Google login** (free tier: 60 requests/min, 1,000 requests/day)
- **Gemini API Key** (requires API setup)
- **Vertex AI** (requires Google Cloud Project)

**Select "Google login"** for the free tier. This is the beginner-friendly option.

### Step 3: Browser Opens

Your default web browser will automatically open with Google's login page. Simply:
1. Enter your Google account email
2. Enter your password
3. Click "Allow" when Google asks for permission

### Step 4: You're In!

After you authorize, your terminal displays the Gemini CLI interface, and you're ready to start. You'll see a prompt where you can type your questions and commands.

---

## Understanding the Gemini CLI Interface

When you're inside Gemini CLI, notice these important elements:

**Bottom Status Bar:**
- **Left side**: Your current working directory (folder)
- **Middle**: The model being used (usually `gemini-2.5-pro`)
- **Right side**: Remaining context tokens (how much "memory" is available)

**Useful Commands:**
- Type `/help` to see all available commands
- Type `/tools` to see what tools Gemini can use
- Type `/stats` to see session statistics (tokens used, duration, etc.)
- Type `/quit` or press Ctrl+C twice to exit

**Shell Mode:**
- Type `!` to switch to shell mode (run terminal commands directly)
- Press ESC to exit shell mode

---

## Your First Task with Gemini

Now that you're inside Gemini CLI, you're ready to put your AI collaborator to work. Simply type your question or request and press Enter:

```
Help me understand what artificial intelligence means
```

Gemini will respond with an explanation. That's it—you're using Gemini CLI!

---

## Understanding the Gemini CLI Session

When you run `gemini`, you're entering an interactive session. Inside this session, you have access to powerful commands and can ask Gemini multiple questions without exiting.

### Basic Session Commands

These slash commands work inside Gemini CLI:

- `/help` - See all available commands and shortcuts
- `/tools` - View all available tools Gemini can use
- `/stats` - See session statistics (tokens used, duration, etc.)
- `/quit` - Exit Gemini CLI and return to your terminal

### How to Exit Gemini

To exit Gemini CLI, simply type:

```
/quit
```

Or press **Ctrl+C twice** to force quit.

### Shell Mode (Running Terminal Commands)

You can run terminal commands directly inside Gemini without exiting:

- Type `!` to enter shell mode
- Run any terminal command
- Press **ESC** to exit shell mode and return to Gemini

---

## Real-World Workflow: Inside a Gemini Session

Here's what a typical session looks like:

**Step 1: Launch Gemini**
```bash
gemini
```

**Step 2: Inside the session, ask your first question**
```
Explain machine learning to me in simple terms with a real example
```

**Step 3: Gemini responds**
```
Machine learning is a method where computers learn from data...
[Gemini's detailed response]
```

**Step 4: Ask a follow-up question**
```
What are some real-world applications of machine learning?
```

**Step 5: Continue the conversation** (you can ask as many questions as you want)
```
How do companies use machine learning to recommend products?
```

**Step 6: When you're done, exit**
```
/quit
```

---

## Try With AI

Now that you've installed Gemini CLI, try these prompts to explore what your AI collaborator can do.

### Prompt 1: Learn a New Concept
```
Explain machine learning to me in simple terms with a real example. Then give me 3 real-world applications of machine learning.
```

**Expected outcome**: Clear explanation with concrete examples and practical applications you can understand.

### Prompt 2: Write Professional Content
```
Write a professional email to my manager about my project status. The project is [describe your situation]. Make it concise and positive.
```

**Expected outcome**: Well-structured professional email you can use or adapt.

### Prompt 3: Problem Solving
```
I'm getting an error when I try to install a package. The error message is: [paste error]. What does it mean and how do I fix it?
```

**Expected outcome**: Clear explanation of the error and step-by-step solution.

### Prompt 4: Plan and Organize
```
I want to learn programming. What programming language should I start with and why? Give me a 4-week learning plan with specific goals for each week.
```

**Expected outcome**: Personalized learning recommendation with structured plan you can follow immediately.

