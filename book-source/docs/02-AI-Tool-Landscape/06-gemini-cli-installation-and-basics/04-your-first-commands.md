---
sidebar_position: 4
title: "Your First Commands"
---

# Your First Commands

## Overview

You've installed Gemini CLI, authenticated your account, and verified everything works with `gemini status`. Now it's time to go beyond verification—it's time to actually use it. This lesson takes you from "the tool is installed" to "I can use Gemini CLI to help me solve real problems."

By the end of this lesson, you'll be able to write and execute Gemini commands at the terminal, interpret AI responses critically, understand how Gemini reads your prompts, and troubleshoot common errors. You'll also get a taste of effective prompting, which Part 3 will explore in depth.

**Learning Objectives:**
By the end of this lesson, you will be able to:
- Construct valid `gemini` commands with proper syntax and quoting
- Execute your first AI-assisted command and interpret the response
- Use at least five common Gemini CLI commands for verification and basic tasks
- Identify and solve common Gemini CLI errors independently
- Think critically about AI responses instead of accepting them at face value
- Write prompts that get meaningful responses from the AI

---

## Understanding Command Syntax

### The Basic Structure

Every Gemini CLI command follows a simple pattern:

```bash
gemini [command] [options] "your prompt text"
```

Let's break this down:

- **`gemini`** — The program you're launching. This is your entry point.
- **`[command]`** — Optional. Specifies what you want to do (e.g., `chat`, `status`, `config`). If you skip this, Gemini sends your text to the AI.
- **`[options]`** — Optional flags that modify behavior (e.g., `--model gemini-2.5-flash`, `--file script.py`).
- **`"your prompt text"`** — Your actual request to the AI. Always wrap multi-word prompts in quotes.

### A Simple Example

The simplest command possible:

```bash
gemini "What is Python?"
```

This tells Gemini: "Take the text 'What is Python?' and send it to the AI. Give me the response."

The AI will respond with an explanation of Python—a few sentences or a paragraph, depending on complexity.

### Quoting Rules: The Gotcha

Your shell (Windows PowerShell, macOS Zsh, Linux Bash) interprets quotes **before** Gemini sees them. This causes confusion.

**Windows PowerShell:**
```powershell
# Double quotes work fine
gemini "What is a list comprehension?"

# Single quotes also work
gemini 'Explain Python decorators'
```

**macOS / Linux (Bash/Zsh):**
```bash
# Double quotes work fine
gemini "What is a list comprehension?"

# Single quotes also work
gemini 'Explain Python decorators'
```

**The Safe Rule:** Always use quotes around your prompt. If your prompt contains quotes, escape them:

```bash
gemini "Explain what a 'for' loop does in Python"
# OR
gemini 'Explain what a "for" loop does in Python'
```

### Complex Commands: Adding Options

Once you're comfortable with basic commands, you can add options:

```bash
# Send a file to Gemini for analysis
gemini --file script.py "Review this code for bugs"

# Use a specific model (if available)
gemini --model gemini-2.5-flash "Explain recursion"

# Start an interactive chat session
gemini chat
```

We'll explore these in more detail throughout the chapter. For now, focus on the basic pattern: `gemini "your prompt"`.

---

## Your First Command: Step by Step

Let's walk through your very first command together. Don't just read this—actually type it.

### Step 1: Open Your Terminal

- **Windows**: PowerShell or Command Prompt
- **macOS**: Terminal app
- **Linux**: Your preferred terminal emulator

### Step 2: Type Your First Command

Type this exactly (or copy-paste it):

```bash
gemini "Explain what Gemini CLI is in one sentence"
```

**What you're doing:** You're asking Gemini a simple, scoped question. The one-sentence constraint forces a concise answer.

### Step 3: Press Enter and Wait

You'll see:
1. A brief pause (Gemini is thinking)
2. A response appears, likely one sentence about Gemini CLI
3. Your terminal prompt returns

### Step 4: Read the Response Carefully

The AI might respond something like:

```
Gemini CLI is a command-line tool that lets you interact with Google's Gemini AI
models directly from your terminal without needing a web browser or extra setup.
```

That's a successful first command. You've just:
- ✅ Constructed a valid command
- ✅ Sent it to Gemini
- ✅ Received a meaningful response
- ✅ Verified end-to-end functionality

**Congratulations.** You're now using Gemini CLI.

---

## Five Quick Verification Commands

These commands verify specific aspects of your Gemini CLI setup. Run each one and note what you see.

### Command 1: Check Your Configuration

```bash
gemini config list
```

**Expected Output:**
```
api_key: ***hidden***
model: gemini-2.0-pro
temperature: 0.7
max_tokens: 1024
timeout: 30
```

**What This Tells You:** Your API key is loaded (shows as hidden for security), your default model is set, and generation parameters are configured. If you see errors here, review Lesson 3 (Authentication & Configuration).

---

### Command 2: Verify Your Quota Status

```bash
gemini status
```

**Expected Output:**
```
Status: Connected
Model: gemini-2.0-pro
Requests Today: 42 / 1000
Requests This Minute: 3 / 60
Quota Reset: 12:00 AM UTC
```

**What This Tells You:** You're authenticated, how many API requests you've used today and this minute, and when your quota resets. If you're approaching 1,000 requests per day, you've hit the free tier limit.

---

### Command 3: Ask a Factual Question

```bash
gemini "What year was Python created?"
```

**Expected Output:**
```
Python was created in 1989 by Guido van Rossum. The first official release,
version 0.9.0, was released in February 1991.
```

**What This Tells You:** The AI can answer factual questions and provides context. It's working normally.

---

### Command 4: Ask for Code

```bash
gemini "Show me a simple Python function that returns the sum of two numbers"
```

**Expected Output:**
```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

**What This Tells You:** Gemini understands code requests and returns executable examples. You can use this for generating code snippets, understanding patterns, or explaining logic.

---

### Command 5: Ask for Explanation

```bash
gemini "What is the difference between a list and a tuple in Python?"
```

**Expected Output:**
```
Lists and tuples are both sequences in Python, but:
- Lists are mutable: you can change, add, or remove elements
- Tuples are immutable: once created, you can't modify them
- Lists use square brackets [1, 2, 3], tuples use parentheses (1, 2, 3)
- Tuples are slightly faster and can be used as dictionary keys
```

**What This Tells You:** Gemini handles conceptual questions and provides structured comparisons. This is useful for learning or reviewing concepts.

---

## Interpreting AI Responses: Think Critically

Here's an uncomfortable truth: **Gemini is very good at sounding confident, even when wrong.**

The AI can confidently explain something incorrect. It can invent facts. It can make mistakes in code. This isn't a bug in Gemini—it's a feature of how large language models work. They're trained to predict the next word based on patterns, not to verify facts against a database.

### How to Evaluate a Response

When Gemini gives you an answer, ask yourself:

**1. Does this match what I already know?**

If Gemini explains a Python concept and you already understand Python, you'll likely spot obvious errors. Trust your knowledge.

**2. Can I verify this independently?**

If you're not sure, test it:
- Try the code example. Does it run? Does it produce the expected output?
- Look up the concept in official documentation.
- Ask Gemini a follow-up question: "Are you sure about that?"

**3. Is this specific or vague?**

Vague answers like "it depends on the situation" are often safer than specific claims. Specific claims are easier to verify (and to disprove).

**4. What's the source?**

Gemini doesn't cite sources by default. If you ask for a citation, it might provide one, but verify it. Don't assume it's accurate just because the AI stated it confidently.

### Example: A Plausible But Wrong Response

You ask: **"What's the best Python framework for web development?"**

Gemini responds: **"Django is always the best choice because it's the oldest and most mature."**

This sounds reasonable, but it's incomplete. Django is good, but so are Flask, FastAPI, and others—each suited to different needs. Gemini stated an opinion as fact.

**Better response from you:** Follow up with:
```bash
gemini "Compare Django, Flask, and FastAPI. When would you use each?"
```

This forces nuance and prevents you from building on a false assumption.

### The Golden Rule

**Always run code before trusting it.** If Gemini gives you a Python script, test it in your environment before using it in production. This catches errors immediately and trains you to validate AI output.

---

## Common Error Scenarios and Solutions

Even experienced users encounter errors. Here are the most common ones and how to fix them.

### Error 1: `command not found: gemini` or `'gemini' is not recognized`

**What This Means:** Your system can't find the `gemini` program. Installation failed or your PATH isn't set correctly.

**How to Fix:**
1. Check that Gemini is installed: `gemini --version`
2. If that fails, reinstall: Follow Lesson 2 (Installation) again.
3. **Windows-specific:** Restart PowerShell after installation. New PATH entries require a fresh terminal.
4. **Mac-specific:** If you installed via Homebrew, run `brew install gemini-cli` again and restart your terminal.

---

### Error 2: `Authentication failed: Invalid API key`

**What This Means:** Your API key is missing, expired, or incorrect.

**How to Fix:**
1. Check your configuration: `gemini config list`
2. Is your API key hidden (shows as `***...`)? If it's blank, you're not authenticated.
3. Re-authenticate: `gemini login` or `gemini auth`
4. If re-authentication fails, your OAuth token may have expired. Log in again at accounts.google.com and refresh Gemini's credentials.

---

### Error 3: `HTTP 429: Too Many Requests`

**What This Means:** You've exceeded your quota. Free tier: 60 requests per minute, 1,000 per day.

**How to Fix:**
1. Check your quota: `gemini status`
2. If you've hit the daily limit, you must wait until midnight UTC.
3. If you've hit the per-minute limit, wait 60 seconds and try again.
4. If you're hitting this frequently, consider upgrading to a paid plan.

---

### Error 4: `Syntax Error: Unexpected token`

**What This Means:** Your shell didn't parse your quotes correctly, or there's a special character Gemini CLI doesn't understand.

**How to Fix:**
1. Check your quoting. Wrap your prompt in single or double quotes: `gemini "your prompt"`
2. Escape special characters (backticks, dollar signs): `gemini "What is a \$variable in Bash?"`
3. For complex prompts with both quote types, use triple quotes or escape: `gemini 'What does "const" mean in JavaScript?'`

---

### Error 5: `Connection Timeout: No response after 30 seconds`

**What This Means:** Your request took too long or your internet connection dropped.

**How to Fix:**
1. Check your internet: Try `ping google.com`
2. Try again: Gemini's servers may have been busy. Retry the command.
3. Shorten your prompt: Extremely long prompts take longer to process.
4. Check for firewall/proxy issues: If you're behind a corporate firewall, it may block API calls. Contact your IT department.

---

### Error 6: `Model Not Found: gemini-2.5-pro`

**What This Means:** You specified a model that's not available to you, or the model name is outdated.

**How to Fix:**
1. Check available models: `gemini --list-models` (if this command exists)
2. Use the default model: `gemini "your prompt"` (no `--model` flag)
3. Update Gemini CLI: `gemini update` or reinstall
4. Check the Gemini CLI documentation for current model names

---

## Prompting Fundamentals: A Quick Taste

You'll spend all of Part 3 mastering effective prompts. For now, here are three quick tips to get better responses from Gemini immediately.

### Tip 1: Be Specific

**Vague prompt:**
```bash
gemini "Tell me about Python"
```
This gives Gemini nowhere to focus. It might ramble about history, features, libraries, or syntax.

**Specific prompt:**
```bash
gemini "What is a list comprehension in Python? Give me one example."
```
This tells Gemini exactly what you want: a definition and one example. The response will be shorter and more useful.

---

### Tip 2: Give Context

**Contextless prompt:**
```bash
gemini "Fix this error"
```
Gemini doesn't know what error you're talking about.

**Contextual prompt:**
```bash
gemini "I'm getting 'TypeError: unsupported operand type(s) for +: 'int' and 'str'' when I run my Python script. What does this mean?"
```
Now Gemini understands the problem and can provide specific help.

---

### Tip 3: Ask for a Specific Format

**Open-ended:**
```bash
gemini "Explain recursion"
```
Gemini might write a paragraph, an essay, or pseudo-code.

**Structured:**
```bash
gemini "Explain recursion in 3 sentences, then give me a Python example of a recursive function that calculates factorial"
```
Gemini knows exactly what you want: three sentences plus working code.

**Part 3 will teach you advanced prompting techniques.** For now, remember: specific beats vague, context beats confusion, and structure beats rambling.

---

## Practice Exercises

It's time to actually use Gemini. These exercises get progressively more complex. Complete at least three of them.

### Exercise 1: Ask a Basic Question

**Task:** Ask Gemini a factual question about programming.

**Suggested prompts:**
- `gemini "What is a variable in programming?"`
- `gemini "What does API stand for?"`
- `gemini "What is version control?"`

**Success Criteria:**
- You receive a clear, coherent answer
- The answer matches your understanding (or teaches you something new)
- You understand the response without looking up terms

**Time:** 2 minutes

---

### Exercise 2: Analyze Python Code

**Task:** Create a simple Python file and ask Gemini to explain it.

**Steps:**
1. Create a file called `sample.py` with this code:
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

2. Run this Gemini command:
```bash
gemini --file sample.py "Explain what this Python script does, line by line"
```

**Success Criteria:**
- Gemini reads the file and explains the function, the function call, and the print statement
- The explanation is accurate (if you're not sure, verify in a Python interpreter)
- You understand each step

**Time:** 5 minutes

**Note:** If `--file` syntax doesn't work, try: `gemini "Here's my Python code. Explain it: [paste code here]"`

---

### Exercise 3: Get Help with a Concept You Don't Understand

**Task:** Pick a programming concept you find confusing and ask Gemini to explain it.

**Suggested concepts:**
- Classes and objects
- Inheritance
- Decorators
- Generators
- Context managers
- Async/await

**Example prompt:**
```bash
gemini "I don't understand how Python decorators work. Explain with a simple example I can run."
```

**Success Criteria:**
- Gemini provides a beginner-friendly explanation
- Gemini gives working code you can test
- You can run the code without errors
- You understand the core concept (even if advanced details are fuzzy)

**Time:** 10 minutes

---

### Exercise 4: Identify an Error and Ask Gemini for Help

**Task:** Create a buggy Python script and ask Gemini to debug it.

**Steps:**
1. Create a file called `buggy.py`:
```python
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

grades = [85, 90, 78]
average = calculate_average(grades)
print(f"Average: {average}")

# This line has a bug
print(f"Length: {len(grades)}"))
```

2. Run this Gemini command:
```bash
gemini "Here's my Python code. There's a syntax error. Find it and explain how to fix it: [paste code]"
```

**Success Criteria:**
- Gemini identifies the syntax error (extra closing parenthesis on the last line)
- Gemini explains why it's wrong
- You fix the code and it runs successfully
- You understand the mistake

**Time:** 5 minutes

---

### Exercise 5: Compare Two Approaches

**Task:** Ask Gemini to compare two ways of doing something in programming.

**Example prompt:**
```bash
gemini "What's the difference between a for loop and a while loop in Python? When would you use each?"
```

**Other comparison ideas:**
- List vs. dictionary
- Function vs. lambda
- Class vs. module
- SQL vs. NoSQL

**Success Criteria:**
- Gemini provides clear differences
- Gemini gives use cases for each approach
- The comparison makes sense (verify against your knowledge)
- You feel more confident using both approaches

**Time:** 5 minutes

---

## Pause and Reflect

Before moving to Lesson 5, take a moment to answer these questions for yourself:

1. **What was surprising about your first Gemini command?** Did the response match your expectation?
2. **Which error scenario resonates most with you?** Have you seen that error before (in other tools)?
3. **How confident are you in AI responses?** What would make you trust them more?
4. **Which Gemini command felt most useful to you?** Why?
5. **What question do you want to ask Gemini next?** (Write it down—you'll use similar prompts in Part 3)

---

## Key Takeaways

- **Command syntax is simple:** `gemini "your prompt"` works for most tasks. Add options only when needed.
- **Always quote your prompt** to avoid shell interpretation issues.
- **AI responses sound confident but need verification.** Test code, check facts, and ask follow-up questions.
- **Common errors have predictable fixes.** API keys, quotas, and syntax issues are solvable.
- **Specific, contextual, structured prompts get better responses.** Vague prompts get vague answers.
- **You're now a Gemini CLI user.** The tool is in your hands.

---

## Forward Bridge: What's Next?

You can now execute Gemini commands and interpret responses. In Lesson 5 (**Built-In Tools Deep Dive**), you'll unlock what makes Gemini CLI truly powerful: tools.

Tools let Gemini do more than chat:
- **Read files:** `gemini --file myfile.py "analyze this"`
- **Fetch web content:** Ask Gemini to search the web and summarize
- **Run Python code:** Gemini can execute code and show you results
- **Generate images:** Create and view AI-generated images

You've been using the foundation. Lesson 5 builds the house.

---

## Additional Resources

- **Gemini CLI Documentation:** Check `gemini --help` for current command options
- **Effective Prompting:** Part 3 covers this in depth
- **Quota and Rate Limits:** Review your status anytime with `gemini status`
- **Getting Help:** Run `gemini help [command]` to see command-specific documentation
