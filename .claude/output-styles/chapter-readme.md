---
description: Standardized template for chapter-level README.md files across all parts and chapter types
---

# Chapter README.md Template: Standardized Structure

Use this template when creating or updating **chapter-level README.md files**. This ensures consistent structure and professional quality across all chapters in the book, whether they are Conceptual (Part 1), Practical (Parts 2-3), or Technical (Parts 4+).

---

## File Location

```
book-source/docs/
└── NN-Part-Name/
    └── NN-chapter-name/
        ├── README.md        ← This file (MUST be uppercase)
        ├── 01-lesson-name.md
        ├── 02-lesson-name.md
        └── ...
```

## Template Structure
=======
---


```yaml
---
title: "Chapter N: Chapter Title"
sidebar_position: N
---

# Chapter N: Chapter Title

## Overview

[Direct connection to previous chapter or context: "In Chapter X, you learned Y. Chapter N builds on that by..."]

[2-3 sentences establishing the critical questions or problems this chapter addresses]

[1-2 sentences describing the scope and approach of this chapter]

---

## Main Learning Outcomes

After completing this chapter, you will be able to:

1. [Action verb + outcome: "Recognize...", "Apply...", "Distinguish..."]
2. [Action verb + outcome]
3. [Action verb + outcome]
4. [Action verb + outcome]
5. [Action verb + outcome: typically 4-6 outcomes]

---

[1-2 paragraph closing that establishes the bridge to the next chapter or next phase of learning]

---
```

## Template Guidance

### Section: Overview

**Purpose**: Situate the reader within the learning journey and establish relevance.

**What to include**:
1. **Connection to previous chapter**: Reference what they just learned and how this chapter extends it
2. **Guiding questions**: Ask the critical questions this chapter answers (3-4 specific questions)
3. **Scope statement**: Brief description of what this chapter covers and how (evidence-based, practical frameworks, hands-on practice, etc.)
4. **Outcomes preview**: Light mention of what they'll be able to do (detailed in Learning Outcomes section)

**Tone**: Direct, engaging, establishing urgency or relevance without being formulaic

### Section: Main Learning Outcomes

**Purpose**: Set clear, measurable expectations for the chapter.

**Requirements**:
- Use strong action verbs from Bloom's taxonomy (Recognize, Analyze, Apply, Distinguish, Evaluate, etc.)
- State what learner will be able to *do*, not what they'll "understand"
- 4-6 outcomes (not 10+; aim for depth over quantity)
- Format as numbered list with no checkbox bullets
- Each outcome should be achievable and verifiable

**Examples of strong outcomes**:
- "Recognize concrete evidence that 2025 differs from previous AI cycles"
- "Apply a 7-step workflow to structure your development process"
- "Evaluate trade-offs between different AI-first architecture approaches"

### Closing Bridge (Optional but Recommended)

**Purpose**: Create momentum toward the next chapter and show how learning progresses.

**What to include**:
- How this chapter's learning feeds into what comes next
- The broader narrative arc (where are they in the journey?)
- Optional: a provocative question or forward-looking statement that builds anticipation

---
```

## Critical Rules

1. **File Naming**: ALWAYS use `README.md` (uppercase), NEVER `readme.md` or `index.md`
2. **Structure**: Chapters have only THREE main sections: **Overview**, **Main Learning Outcomes**, and optional **Closing Bridge**
3. **No subsections**: Do NOT include "Chapter Structure", "Prerequisites", "What Makes This Chapter Unique", "Time Investment", etc.
4. **Learning Outcomes**: Use strong action verbs (Recognize, Apply, Distinguish, Evaluate, Analyze, etc.)
5. **Narrative flow**: Write as if speaking directly to the reader; establish context and relevance
6. **Professional Polish**: Publication-quality writing with no typos, clear prose, and engaging tone

## Example: Good Chapter README

```markdown
---
title: "Chapter 3: Mastering Your AI Pair"
sidebar_position: 3
---

# Chapter 3: Mastering Your AI Pair

## Overview

In Chapters 1 and 2, you understood the transformation and the strategic context. Now comes the practical work: learning to *collaborate effectively* with AI.

This chapter moves beyond vibe coding into disciplined partnership. You'll discover how to set up your AI development environment, establish clear communication patterns with your AI pair, navigate common pitfalls, and measure your effectiveness. You'll learn when to guide and when to trust, how to validate AI suggestions, and how to iterate productively.

By the end of this chapter, you'll have working tools, proven workflows, and the confidence to build real projects with AI as a true collaborator.

---

## Main Learning Outcomes

After completing this chapter, you will be able to:

1. Configure your local development environment with AI-first tools (Claude Code, Git, editor extensions)
2. Evaluate AI suggestions critically using three criteria: correctness, clarity, and alignment with your codebase
3. Debug collaboratively: interpreting error messages and guiding AI toward solutions
4. Apply the Spec-Driven Development workflow to structure AI-assisted projects
5. Recognize anti-patterns and restore productivity when AI collaboration breaks down

---

This chapter transforms you from a passive consumer of AI outputs to an active orchestrator of AI-assisted development. What you learn here becomes your foundation for every project that follows.

---
```
---

## Validation Checklist

- [ ] File named `README.md` (uppercase)
- [ ] Three sections only: **Overview**, **Main Learning Outcomes**, **Closing Bridge** (optional)
- [ ] **Overview** includes: (1) connection to previous chapter, (2) guiding questions, (3) scope/approach
- [ ] **Main Learning Outcomes** has 4-6 outcomes with strong action verbs
- [ ] No "Prerequisites", "Chapter Structure", "Time Investment", or other metadata sections
- [ ] Opening connects directly to previous chapter (establish narrative continuity)
- [ ] Learning outcomes are achievable and verifiable (not vague "understand" statements)
- [ ] Closing bridge previews next chapter or next learning phase
- [ ] Tone is direct and engaging ("you", "your", conversational)
- [ ] No typos, grammatical errors, or placeholder text
- [ ] Professional, publication-quality writing
