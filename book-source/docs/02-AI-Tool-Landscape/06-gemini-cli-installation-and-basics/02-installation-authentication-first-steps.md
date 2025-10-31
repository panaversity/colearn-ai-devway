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

## Real-World Use Cases: What You Can Do

Gemini CLI is your AI collaborator for all kinds of tasks—not just coding. Inside the session, you can ask about anything:

### Learning & Understanding

```
Explain machine learning to me in simple terms with a real example
```

**Why this matters:** You're learning something new and want it explained clearly. You can ask follow-ups right there in the session without restarting.

```
What are the key differences between Python and JavaScript?
```

### Writing & Content

```
Write a professional email to my manager about my project status
```

```
Rewrite this paragraph in a more engaging way: [paste your text here]
```

```
Create an outline for a blog post about artificial intelligence for beginners
```

### Problem Solving & Debugging

```
I'm getting an error when I try to install a package. The error message is: [paste error]. What does it mean?
```

```
How do I troubleshoot my WiFi connection if it keeps dropping?
```

### Brainstorming & Planning

```
Give me 5 creative ideas for a small side project I could build this month
```

```
I want to learn programming. What programming language should I start with and why?
```

```
What are the steps I should follow to plan a successful study schedule?
```

### Productivity & Organization

```
Help me organize my weekly schedule. I have: [list tasks]. What's the best order to tackle them?
```

```
I need to research [topic]. What are the key areas I should look into?
```

### Creative Tasks

```
Help me brainstorm names for my new startup
```

```
Give me tips for creating engaging social media content"
```
---

## What's Next?

In the next lesson (**Built-In Tools Deep Dive**), you'll explore the powerful tools Gemini CLI comes with—like file operations, web searching, and more—that make your AI collaborator even more capable.

Until then, **start using Gemini for real tasks**. Launch a session, ask it about something you're learning, get help writing something, brainstorm ideas. The more you use it naturally, the more comfortable you'll become. That's when the real power emerges.
