---
sidebar_position: 2
title: "Two Development Patterns"
chapter: 2
lesson: 2
duration: "8-10 minutes"
learning_objectives:
  - "Define vibe coding and Spec-Driven Development and identify their key characteristics"
  - "Explain how vibe coding fails in production contexts (ambiguous requirements, missing tests, architecture drift)"
  - "Recognize when each approach is appropriate based on context (learning vs. production, solo vs. team, exploration vs. delivery)"
  - "Understand that AI amplifies both good practices and bad practices—discipline becomes MORE critical, not less"
---

# Two Development Patterns

## Learning Objectives

By the end of this lesson, you will be able to:

- **LO-2.1**: Define vibe coding and Spec-Driven Development and identify their key characteristics
- **LO-2.2**: Explain how vibe coding fails in production contexts (ambiguous requirements, missing tests, architecture drift)
- **LO-2.3**: Recognize when each approach is appropriate based on context (learning vs. production, solo vs. team, exploration vs. delivery)
- **LO-2.4**: Understand that AI amplifies both good practices and bad practices—discipline becomes MORE critical, not less

---

## The Speed Paradox

You've probably experienced this: you start a project and move *fast*. No specs, no planning, just coding. The first feature ships in hours. It works. You ship it.

Then week two arrives. You need to add a related feature, but the code resists. The structure doesn't accommodate it. You discover edge cases weren't tested. A teammate looks at the code and asks, "Why did you do it this way?" You don't have a good answer—it just felt right at the time.

By week three, you're slower than if you'd spent the first two days planning. The fast start masked a slow finish.

This paradox reveals something important: **there are fundamentally different ways of building software, and they have different tradeoffs.** Neither is universally "right" or "wrong." But understanding when each one works—and why—is critical for using AI effectively as a development partner.

---

## Vibe Coding: Intuition-Led Development

**Vibe coding** is development driven by intuition, exploration, and immediate feedback. You write code, you run it, you see what happens, and you adjust. There's no formal specification. Requirements emerge as you explore.

### Why Vibe Coding Works

Vibe coding is **genuinely excellent** for certain contexts:

- **Learning**: When you're new to a language or framework, vibe coding gives you immediate feedback. You try something, it fails, you learn why. This tight feedback loop is one of the best ways to internalize how something works.

- **Exploration and Discovery**: When you're prototyping a new idea or investigating a technical question, rigid planning can slow you down. "What if I try this?" is often faster than "What if I document this first?"

- **Low Stakes Solo Work**: If you're building a personal tool or learning project, the cost of rework is low. You can afford to refactor.

- **Creative Flow**: Some of the best code comes from a state of creative focus where you're responding to the problem intuitively. Stopping to write a spec can interrupt that flow.

Many experienced developers will tell you their best work came from vibe coding sessions. There's real value there.

### Where Vibe Coding Breaks Down

Vibe coding has **predictable failure modes** that show up when stakes increase:

- **Ambiguous Requirements**: Without a written spec, different team members have different mental models of what should happen. "I thought it would work like X" versus "I built it to work like Y" becomes a recurring problem.

- **Missing Tests**: Vibe coding naturally skips tests. You test manually, which works great until you don't test that one edge case—the one that breaks in production at 3 AM.

- **Architecture Drift**: The code evolves organically, which is fine until the structure no longer supports new features. Adding the third variant of something reveals that the code wasn't designed for extensibility.

- **Knowledge Silos**: The person who wrote it understands it. The person who maintains it doesn't. Onboarding becomes painful because there's no written spec to explain the "why."

- **Refactoring Costs Explode**: By the time you realize the structure is wrong, you've built features on top of it. Changing the foundation now breaks everything. The technical debt compounds.

These aren't design flaws in vibe coding—they're natural properties of exploration-first development. They don't matter much when stakes are low. They matter enormously when you're shipping to production or working in a team.

---

## Spec-Driven Development: Method-Led Development

**Spec-Driven Development (SDD)** inverts the order. You write a specification first, defining what you're building, why, and how success looks. Then you write tests that encode that specification. Only then do you implement the feature. Your code's job is to pass the tests and satisfy the spec.

### How SDD Works

The sequence looks like this:

1. **Specification Phase**: Write a clear specification. What should this feature do? What are the edge cases? How does it interact with the rest of the system? This takes time—but it forces clarity before coding.

2. **Test Phase**: Write tests that validate the specification. These tests will initially fail because the feature doesn't exist yet. But they encode the spec in executable form. Anyone reading the tests understands what the feature should do.

3. **Implementation Phase**: Write the code to pass the tests. Your code's job is clear: satisfy the spec and pass the tests. This focus reduces false starts and rabbit holes.

4. **Review and Refinement**: Changes are reviewed against the spec and tests, not against personal preference. This creates shared ownership and reduces conflicts.

### Why SDD Works

- **Predictable Delivery**: Because requirements are clear upfront, estimates are more accurate. Surprises are fewer.

- **Sustainable Velocity**: As the codebase grows, SDD codebases remain navigable. New features don't require heroic refactoring because the structure was planned.

- **Team Collaboration**: A written spec means everyone has the same understanding. Code reviews focus on implementation quality, not debating what should be built.

- **Maintainability**: Someone joining the team six months later can read the spec and tests and understand not just what the code does, but why.

- **Confident Refactoring**: With tests in place, you can refactor internal structure without fear. The tests verify you haven't broken anything.

---

## A Concrete Comparison: Team A vs. Team B

Let's make this concrete. Imagine two teams building the same feature: **add a `/summarize` endpoint that takes a PDF file, extracts its content, and returns a summary.**

### Team A: Vibe Coding

**Week 1, Tuesday morning**: A developer opens a new file and starts coding. No spec. "I'll figure it out as I go."

- **Tuesday afternoon**: The endpoint works locally. It reads a PDF, extracts text, sends it to a summarization API, returns the result. The developer tests it manually and ships it.
- **Total time: 10 hours**

The code is fast. It works. Velocity looks amazing.

**Wednesday morning in staging**: The PDF parsing library behaves differently on the staging machine than locally. The code crashes on certain PDFs. The developer didn't test those cases—they just tested their sample PDF.

**Wednesday afternoon**: The fix is rolled out, but it's patch-y. The underlying architecture doesn't accommodate variations well.

**Friday**: A teammate asks, "Can we add support for Word documents too?" The developer looks at the code and realizes the PDF extraction is tightly coupled to the summarization logic. Adding Word support means rewriting half of it. The code wasn't designed for extensibility.

**Monday of week 2**: The team decides the `/summarize` endpoint needs to be rebuilt from scratch. They allocate three days for a proper redesign.

**Total cost: 10 hours of fast coding + 24 hours of rework = 34 hours. Plus damage to the team's confidence in the codebase.**

### Team B: Spec-Driven Development

**Week 1, Tuesday morning**: Before coding, the team writes a specification:

> "The `/summarize` endpoint accepts multipart form data containing a document file (initially PDF, designed for future extensions to Word, etc.). It extracts content, summarizes it using the external API, and returns structured JSON. Edge cases: files > 100MB, corrupted PDFs, missing API key, rate limiting. Design: a document parser abstraction that allows multiple format handlers."

- **Tuesday, 2 hours**: Specification complete. Everyone agrees on what "done" looks like.
- **Tuesday afternoon to Wednesday morning, 3 hours**: Write comprehensive tests. Tests validate the spec—what happens with large files, what happens with corrupted PDFs, what happens when the API is down. The tests fail because the feature doesn't exist yet.
- **Wednesday to Thursday, 4 hours**: Implement the feature to pass the tests. The developer knows exactly what to build.
- **Thursday afternoon, 1 hour**: Code review. The spec and tests make the review focused.
- **Total time: 10 hours, but the feature ships reliably. No staging surprises.**

**Friday**: A teammate asks, "Can we add Word support?" The developer looks at the spec and code. The parser is abstracted. Adding Word support means writing a Word parser handler. The existing code doesn't need to change.

- **Friday afternoon, 2 hours**: Word support added, tested, shipped.

**Total cost: 10 hours initial + 2 hours extension = 12 hours. Sustainable. Confident.**

### What's Different?

Team A's velocity *appears* high until you count rework. Team B's velocity appears lower initially but is actually *sustained* because the code doesn't accumulate friction.

This isn't a story about smart engineers versus careless ones. It's a story about **method matching the context**. Team A used exploration-mode thinking for production-mode stakes. That's the mistake.

---

## When Each Approach Fits

| **Context** | **Vibe Coding** | **Spec-Driven Development** |
|---|---|---|
| **Learning a new technology** | Excellent | Unnecessary friction |
| **Shipping to production** | High risk | Appropriate |
| **Solo project, low stakes** | Perfect | Overhead |
| **Team feature, production code** | Causes coordination costs | Essential |
| **Exploration/prototyping** | Ideal | Premature structure |
| **Extended maintenance, multiple contributors** | Knowledge silos form | Clarity and velocity |
| **Regulatory/safety requirements** | Insufficient | Required |
| **Technical debt acceptable** | Yes | No |

**The key insight**: Vibe coding is powerful. SDD is powerful. They're designed for different contexts. Using vibe coding for production features creates the "fast week one, slow week two" pattern. Using SDD for learning creates unnecessary ceremony that slows exploration.

---

## Why This Matters for AI Development

Here's where AI changes the stakes: **AI is an amplifier of whatever practice you bring to it.**

When you vibe code with Claude or ChatGPT, the AI will generate code quickly. It feels amazing—you ask for something, you get working code in seconds. But you're amplifying every weakness of vibe coding. The AI won't write a spec you didn't ask for. It won't write tests you didn't request. It will generate code at the speed of your intuition, which means you ship fast and encounter the same staging surprises Team A did—except now there's also AI-generated code that no one fully understands.

Conversely, when you use SDD with AI, the AI becomes a force multiplier for the things that matter. You ask it to help you write a clear spec. You ask it to generate tests from your spec. You ask it to implement against those tests. The AI handles the mechanical parts—boilerplate tests, obvious implementations—while you handle the judgment—is the spec right? Are the edge cases covered?

**The discipline becomes MORE critical with AI, not less.** AI makes it easier to code fast. That makes vibe coding more tempting. And that's precisely when you need discipline most.

This is why in the next lesson we'll introduce you to **DORA metrics**—a research-backed way to measure whether your development approach is actually working. Because "feels fast" and "is actually fast" are often different things.

---

## Quick Check: Test Your Understanding

**Question 1 (True/False)**: Vibe coding is inherently inferior to Spec-Driven Development and should never be used.

**Answer**: False. Vibe coding is appropriate for learning, exploration, and low-stakes solo work. The mistake is using it for production features in teams. Neither approach is universally "right"—context determines which is appropriate.

---

**Question 2 (Scenario)**: Your team is adding language support for Python 3.13 features to an existing production compiler. You have three days. Which approach fits better and why?

**Answer**: Spec-Driven Development. This is production code with existing structure and users. A specification ensures the new features integrate correctly. Tests ensure edge cases around type interactions are covered. A vibe-coding approach would risk subtle breakages that only surface after release.

---

**Question 3 (Consequence)**: Why does Team A's velocity appear high in week one but actually slow down in week two?

**Answer**: Team A shipped fast by skipping specification and testing. In week two, ambiguous requirements and missing tests created surprises. The architecture wasn't designed for extension, so adding Word support required rework. Rework costs more than upfront specification and testing would have. The true cost (10 hours + 24 hours rework) was higher than SDD (10 hours planned, sustainable).

---

## Summary & Transition

**Key Takeaways:**

- **Vibe coding** is intuition-led exploration. It's excellent for learning but creates predictable failure modes in production: missing tests, ambiguous requirements, architecture drift, knowledge silos.

- **Spec-Driven Development** enforces clarity upfront, making maintenance and team collaboration sustainable. It feels slower initially but compresses total cost and enables confident refactoring.

- **Context matters.** Neither approach is universally right. The question is: what are you building, and for whom? Solo learning project? Vibe coding. Team production feature? SDD.

- **AI amplifies everything.** Fast vibe coding with AI feels amazing and creates the same risks. Disciplined SDD with AI multiplies your leverage. The tools don't remove the need for judgment—they increase its importance.

In the next lesson, we'll move beyond intuition and introduce **DORA metrics**—a research-backed framework for measuring whether your development approach is *actually* working. You'll learn how leading teams measure and optimize for sustainable velocity, not just perceived speed.
