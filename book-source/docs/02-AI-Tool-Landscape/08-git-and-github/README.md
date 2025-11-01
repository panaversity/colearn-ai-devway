# Chapter 8: Git & GitHub for AI-Driven Development

## Overview

This chapter teaches version control using Git and GitHub specifically in the context of AI-driven development workflows. Git provides the **safety net** that makes AI-assisted development viable—every change is tracked, every experiment can be rolled back, and every collaboration is auditable.

When you let Claude Code refactor your project or Gemini CLI generate new features, Git ensures you can always return to a working state. This chapter transforms Git from an intimidating requirement into your most trusted development partner.

---

## Learning Outcomes

By the end of this chapter, you will be able to:

1. **Create safe checkpoints** before letting AI tools modify your code, and successfully rollback if needed
2. **Safely experiment** with AI-generated code using branches, knowing your main codebase remains untouched
3. **Collaborate with teammates** using pull requests to review AI-generated features before merging
4. **Use natural language prompts** with Claude Code or Gemini CLI to execute Git operations without memorizing commands
5. **Track AI contributions** over time using git log and git blame with proper attribution

---

## What You'll Need

- A terminal you can use (macOS Terminal with zsh is perfect)
- A GitHub account (free) for Lesson 4 and the project
- Internet access (for pushing to GitHub)
- Claude Code (Chapter 5) or Gemini CLI (Chapter 6) ready to use
- 3–5 hours focused time for lessons + exercises
- Optional: GitHub CLI (`gh`) for certain workflows; if you don't have it, the GitHub web UI works fine

---

## Key Principles Throughout This Chapter

1. Understand over memorization

- Know what commands do and why you need them; let AI remember exact flags

2. Safety first

- Create checkpoints before AI changes; prefer revert over risky manual edits

3. AI as an equal partner

- Use natural language to drive Git workflows, but keep human judgment in charge

4. Learning through doing

- Every concept comes with realistic practice and AI-assisted troubleshooting

Remember: Git is your safety net. Once you understand it, you'll never fear AI-assisted development again.
