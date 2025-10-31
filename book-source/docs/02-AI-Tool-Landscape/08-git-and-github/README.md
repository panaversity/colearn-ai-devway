# Chapter 8: Git & GitHub for AI-Driven Development

**Part**: Part 2 - AI Tool Landscape
**Chapter Number**: 8 (Final chapter of Part 2)
**Duration**: 3-4 hours (content) + 1+ hour (exercises)
**Prerequisites**: Chapters 5-7 (Claude Code, Gemini CLI, Bash Essentials)

---

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

## Why This Chapter Matters

**The Three Problems Git Solves for AI Development**:

1. **Safety**: Experiment fearlessly with AI suggestions knowing you can roll back any change
2. **Collaboration**: Share AI-generated code with teammates for review before it ships
3. **Auditability**: Track which AI tool made which changes, when, and why

Without Git, AI-assisted development is risky. With Git, it's a superpower.

---

## Chapter Structure

This chapter is organized into 5 progressive lessons:

### **Lesson 1: Why Git Matters in AI-Driven Development** (30 min)
**Objective**: Understand the safety net that Git provides when working with AI tools

- The three problems Git solves (safety, collaboration, auditability)
- Real-world scenarios: AI refactoring, team code review, bug hunting
- Why Git is essential (not optional) for AI-assisted development
- Preview of natural language prompts (Part II of this chapter)

**No coding** - this lesson establishes motivation before teaching commands.

---

### **Lesson 2: Git Essentials - Commands and Setup** (90 min)
**Objective**: Install Git, configure it, and execute the basic workflow

- **Part I**: Installation (Windows, Mac, Linux) and configuration
- **Part II**: The core workflow: `git status` → `git add` → `git commit` → `git push`
- **Part III**: Understanding the three-stage concept (working directory → staging → repository)
- **Part IV**: Reading Git output and interpreting messages
- **Part V**: Commit messages with AI attribution

**5 hands-on exercises** included (install, configure, init, commit, log)

---

### **Lesson 3: Safe Experimentation - Branches, Checkpoints, and Rollback** (90 min)
**Objective**: Create checkpoints before AI changes, safely rollback if needed, experiment with branches

- **Part I**: The checkpoint pattern (commit before every AI session)
- **Part II**: Branch-based experimentation (isolate AI changes from main codebase)
- **Part III**: Undoing changes (soft reset, hard reset, revert)
- **Part IV**: Merging branches and handling conflicts
- **Part V**: Stashing (temporary saves)

**6 hands-on exercises** included (checkpoint, branch, switch, merge, rollback, conflict resolution)

---

### **Lesson 4: Pull Requests and Team Collaboration** (75 min)
**Objective**: Create PRs on GitHub, participate in code review, merge safely

- **Part I**: Understanding pull requests (code review mechanism)
- **Part II**: Creating a PR (push to GitHub, use GitHub UI)
- **Part III**: Reviewing code (what to look for in AI-generated code)
- **Part IV**: Iteration and feedback (addressing review comments)
- **Part V**: Merging on GitHub (merge strategies)
- **Part VI**: Handling PR conflicts

**7 hands-on exercises** included (create repo, push, branch, create PR, review, iterate, merge)

---

### **Lesson 5: Natural Language Prompts for Git Operations** (45 min)
**Objective**: Use Claude Code or Gemini CLI to execute Git commands via natural language

- **Part I**: Why natural language prompts (convenience, not replacement for understanding)
- **Part II**: Command-to-prompt translation (10+ examples)
- **Part III**: Complex workflow prompts (multi-step scenarios)
- **Part IV**: Troubleshooting prompts (conflict resolution, error explanation)
- **Part V**: Best practices for AI CLI conversations

**6 hands-on exercises** included (concept explanation, branch creation, conflict resolution, complex workflows)

---

## Prerequisites

Before starting this chapter, you should have completed:

- **Chapter 5**: Claude Code Features and Workflows
- **Chapter 6**: Gemini CLI Basics
- **Chapter 7**: Bash Essentials for AI Development

You should also:
- Have a GitHub account (free tier is sufficient) or be willing to create one
- Have internet access for pushing/pulling to GitHub
- Be working on a personal computer where you can install software
- Have created at least one simple Python project (from previous chapters)

---

## What You'll Build

**End-of-Chapter Comprehensive Project**: Create a Git repository for an AI-assisted project, make multiple commits with AI attribution, create feature branches for experimentation, push to GitHub, and create a pull request.

**Success Criteria**:
- Repository exists locally and on GitHub
- Multiple commits with proper AI attribution
- Feature branch created, tested, and merged successfully
- Pull request workflow demonstrated
- Natural language prompts used for at least 2 Git operations

---

## Chapter Goals (Measurable Success Criteria)

- **SC-001**: Create a Git repository and make your first commit within 5 minutes
- **SC-002**: Create a safe checkpoint before AI changes and successfully roll back if needed
- **SC-003**: Create a feature branch, make changes, and merge back to main without data loss
- **SC-004**: Create a pull request on GitHub, simulate review feedback, and merge
- **SC-005**: Translate at least 10 Git commands into equivalent natural language prompts
- **SC-006**: Understand when to commit (before AI changes, after completing work, before switching branches)
- **SC-007**: Successfully complete the end-of-chapter project (90% target completion rate)
- **SC-008**: Identify and use appropriate Git commands for 5 common AI development scenarios

---

## Key Principle: Git as Your Safety Net

Throughout this chapter, remember:

> **Git is not the danger—it's the safety net.**

When working with AI tools like Claude Code and Gemini CLI, Git transforms from an intimidating requirement into your most valuable asset. Every experiment, every AI-generated change, every refactoring attempt is reversible. You can try anything without fear.

---

## Bridge to Part 3

This chapter concludes Part 2 (AI Tool Landscape) and sets you up for Part 3 (Prompt & Context Engineering).

- **Part 2 taught you the tools**: Claude Code, Gemini CLI, Bash, and now Git
- **Part 3 will teach you the skills**: How to craft effective prompts, manage context, and collaborate with AI strategically

Lesson 5 (Natural Language Prompts) is a preview of the prompt engineering skills you'll master in Part 3.

---

## Time Estimate

- **Lesson 1**: 30 minutes (reading + reflection)
- **Lesson 2**: 90 minutes (45 min content + 45 min exercises)
- **Lesson 3**: 90 minutes (40 min content + 50 min exercises)
- **Lesson 4**: 75 minutes (35 min content + 40 min exercises)
- **Lesson 5**: 45 minutes (15 min content + 30 min exercises)
- **Comprehensive Project**: 60-90 minutes

**Total**: 5.5-6.5 hours for full mastery (content + exercises + project)

---

## Quick Reference

After completing this chapter, you'll have access to:

- **Quick Reference Card**: 15-20 essential Git commands with brief explanations
- **Common Scenarios Reference**: 5-8 AI development scenarios with Git solutions
- **Natural Language Prompt Library**: 10+ tested prompts for common Git operations

---

## Ready to Begin?

Start with **Lesson 1: Why Git Matters in AI-Driven Development** to understand the motivation before diving into commands.

Remember: Git is your safety net. Once you understand it, you'll never fear AI-assisted development again.
