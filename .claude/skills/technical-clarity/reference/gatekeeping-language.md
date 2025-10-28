# Gatekeeping Language to Avoid

## Overview

Certain words and phrases create barriers to learning by assuming knowledge, minimizing difficulty, or implying inadequacy. This guide identifies and replaces gatekeeping language.

## Dismissive Minimizers

These words make concepts seem trivial, discouraging learners who struggle.

### "Obviously" / "Clearly"

**Problem**: Implies anyone who doesn't understand is deficient

**Example**:
```
❌ "Obviously, you should use a dictionary here."
✅ "A dictionary works well here because..."
```

### "Simply" / "Just" / "Merely"

**Problem**: Minimizes difficulty, ignores legitimate struggles

**Example**:
```
❌ "Just add a decorator to the function."
✅ "Add a decorator to the function by placing @decorator_name above the function definition."
```

### "Easy" / "Trivial" / "Straightforward"

**Problem**: What's easy for experts is often hard for learners

**Example**:
```
❌ "It's easy to implement a linked list."
✅ "Here's how to implement a linked list step-by-step."
```

## Ableist Language

### "Crazy" / "Insane" / "Dumb" / "Lame"

**Problem**: Uses disability/mental health as negative metaphors

**Replacements**:
- "surprising", "unexpected", "unusual"
- "illogical", "incorrect", "flawed"
- "inefficient", "problematic"

**Example**:
```
❌ "This code is crazy complicated."
✅ "This code is very complex."

❌ "That's a dumb way to do it."
✅ "That approach has some drawbacks."
```

## Assumptive Language

### "Of course" / "Naturally"

**Problem**: Assumes shared knowledge or perspective

**Example**:
```
❌ "Of course, you're familiar with lambda calculus."
✅ "Lambda calculus is... [brief explanation]"
```

### "Everyone knows"

**Problem**: Excludes those who don't know

**Example**:
```
❌ "Everyone knows Python is dynamically typed."
✅ "Python is dynamically typed, meaning..."
```

## Experience-Based Assumptions

### "Real programmers..."

**Problem**: Creates artificial hierarchy

**Example**:
```
❌ "Real programmers use vim."
✅ "Many developers prefer vim because..."
```

### "You should already know..."

**Problem**: Shames learners for knowledge gaps

**Example**:
```
❌ "You should already know how functions work."
✅ "Functions are... [quick review if needed]"
```

## Gendered Assumptions

### "He" / "His" (generic)

**Problem**: Assumes male default

**Replacements**:
- Use "they/their" (singular)
- Alternate "he" and "she"
- Rewrite to avoid pronouns

**Example**:
```
❌ "When a programmer writes his code..."
✅ "When programmers write their code..."
✅ "When you write code..."
```

## Replacement Strategies

### Instead of Minimizing

Replace dismissive words with explanatory phrases:

| Avoid | Use Instead |
|-------|-------------|
| "simply" | [explain the actual steps] |
| "obviously" | [explain the reasoning] |
| "just" | [describe what to do] |
| "trivially" | [show how it works] |
| "clearly" | [make it clear by explaining] |

### Instead of Assuming

Provide context:

```
❌ "As you know, decorators modify functions."
✅ "Decorators are functions that modify other functions. They..."
```

### Instead of Shaming

Be descriptive and neutral:

```
❌ "This is the wrong way to do it."
✅ "This approach has these trade-offs... An alternative is..."
```

## Inclusive Alternatives

### Acknowledging Difficulty

```
✅ "This is a complex topic that takes time to master."
✅ "Many people find this challenging at first."
✅ "This concept builds on several prerequisites."
```

### Providing Context

```
✅ "If you're familiar with X, this is similar. If not, here's a quick overview."
✅ "Background: [concept] means [definition]"
✅ "Prerequisites for this section: [list]"
```

### Normalizing Struggle

```
✅ "If this feels confusing, that's normal—let's break it down."
✅ "This is a common point of confusion."
✅ "Many learners need multiple exposures to this concept."
```

## Voice and Tone

### Encouraging

```
✅ "Let's explore how this works."
✅ "Here's one way to approach this."
✅ "You're building important skills."
```

### Neutral-Descriptive

```
✅ "This approach has these characteristics..."
✅ "One pattern is... Another pattern is..."
✅ "The trade-offs include..."
```

## Checklist: Gatekeeping Audit

Review text for:
- [ ] No "obviously", "clearly", "simply", "just"
- [ ] No "everyone knows", "of course"
- [ ] No "easy", "trivial", "straightforward" (without context)
- [ ] No ableist metaphors (crazy, dumb, lame)
- [ ] No gendered generic pronouns
- [ ] No assumptions about prior knowledge (or explicitly stated)
- [ ] Difficulty acknowledged where appropriate
- [ ] Encouraging, neutral tone

## Further Reading

- "Writing Inclusive Documentation" (Write the Docs community)
- "The Responsible Communication Style Guide"
- "Teaching Technical Writing" (Google developer documentation style guide)
