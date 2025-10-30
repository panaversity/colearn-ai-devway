---
description: Template for chapter-level README.md files
---

# Chapter README.md Template

Use this template when creating chapter-level README.md files. Adapt structure based on chapter type (Conceptual, Technical, or Hybrid).

---

## File Location
```
book-source/docs/
└── NN-Part-Name/
    └── NN-chapter-name/
        ├── README.md        ← This file (MUST be uppercase)
        ├── 01-lesson-1.md
        ├── 02-lesson-2.md
        └── ...
```

## Template Structure
```
---
sidebar_position: N
title: "Chapter N: Chapter Title"
---

# Chapter N: Chapter Title

**Chapter Type**: [Conceptual | Technical | Hybrid]
**Estimated Time**: [X minutes reading | X-Y hours with hands-on]
**Level**: [Beginner | Intermediate | Advanced]

## What You'll Learn

[2-3 paragraph overview: What is this chapter about? Why does it matter? Who is it for?]

By the end of this chapter, you will be able to:

- ✅ [Learning outcome 1 - use Bloom's taxonomy verb]
- ✅ [Learning outcome 2]
- ✅ [Learning outcome 3]
- ✅ [Learning outcome N]

## Chapter Structure

### [Descriptive Section Title 1]
**Duration**: [X-Y minutes] | **Type**: [Narrative | Technical | Tutorial]
[1-2 sentence description of what this section covers]

**Key Concepts**: [List 2-3 main concepts]

---

### [Descriptive Section Title 2]
**Duration**: [X-Y minutes] | **Type**: [Narrative | Technical | Tutorial]
[1-2 sentence description]

**What You'll Do**: [For technical sections, list hands-on activities]
- [Activity 1]
- [Activity 2]

**Success Target**: [e.g., "95% install successfully on first attempt"]

---

[Repeat for all sections - use descriptive titles, NEVER "Lesson 1", "Lesson 2", etc.]

## Learning Path

[1-2 paragraphs explaining how sections build on each other and the pedagogical strategy]

## Prerequisites

Before starting this chapter, you should have:

- ✅ [Prerequisite 1]
- ✅ [Prerequisite 2]
- ✅ [Prerequisite N]

## What Makes This Chapter Unique

[1-2 paragraphs highlighting what's special about this chapter's approach or content]

## Time Investment (Required)

**Minimum Path** (Reading only): [X minutes]
**Full Engagement** (Reading + exercises): [X-Y hours]
**Mastery Path** (Including supplementary practice): [X-Y hours]

**Recommended Approach**: [Suggest how to break up the chapter into sessions]

## Success Indicators

You'll know you've mastered this chapter when you can:

1. [Measurable success criterion 1]
2. [Measurable success criterion 2]
3. [Measurable success criterion N]

## What's Next: Chapter [N+1]

[1-2 paragraphs explaining how this chapter connects to the next chapter]

**Preview**: [Brief description of next chapter's topic and approach]

## Getting Started

Ready to begin? Start with [Section 1 Title](./01-filename.md) to [brief motivation for starting there].

---

**Have questions or need help?** [Include guidance on where to get support]
```

## Critical Rules

1. **File Naming**: ALWAYS use `README.md` (uppercase), NEVER `readme.md` or `index.md`
2. **Section Headings**: NEVER use "Lesson 1", "Lesson 2", "Lesson N" - use descriptive titles only
3. **Learning Outcomes**: Use appropriate Bloom's taxonomy verbs for chapter type
4. **Consistency**: Match terminology and structure with individual lesson files
5. **Professional Polish**: No typos, clear language, engaging overview

## Examples of Good vs Bad Headings

**CORRECT** (Descriptive, no "Lesson N"):
```
### Installing and Authenticating Claude Code
### Creating and Using Agent Skills
### Connecting MCP Servers and Common Workflows
```

**INCORRECT** (Uses "Lesson N"):
```
### Lesson 1: Installing and Authenticating Claude Code
### Lesson 2: Creating and Using Agent Skills
### Lesson 3: Connecting MCP Servers and Common Workflows
```

## Validation Checklist

- [ ] File named `README.md` (uppercase)
- [ ] No "Lesson N" in any section heading
- [ ] All required sections present
- [ ] Learning outcomes use appropriate Bloom's taxonomy
- [ ] Prerequisites clearly stated
- [ ] Time investment section included and filled in
- [ ] All referenced lesson files exist
- [ ] No typos or grammatical errors
- [ ] Professional tone and formatting
