---
description: Docusaurus-specific chapter formatting for CoLearning Python & Agentic AI book
---

# Docusaurus Chapter Output Style

This style provides specific guidance for creating chapters that integrate perfectly with Docusaurus static site generation. Follow this guide when creating chapter files for the CoLearning Python & Agentic AI book.

## File Organization & Naming

### Directory Structure

Chapters are organized in a 2-level hierarchy within `docs/`:

```
docs/
├── 01-part-intro.md                           # Part introduction (optional)
├── 02-Introducing-AI-Driven-Development/
│   ├── 01-Welcome-to-AI-Coding.md            # Chapter 1
│   ├── 02-Understanding-AI-Tools.md          # Chapter 2
│   ├── 03-Collaboration-Basics.md            # Chapter 3
│   ├── 04-Your-First-Program.md              # Chapter 4
│   └── 05-Debugging-with-AI.md               # Chapter 5
│
├── 03-AI-Tool-Landscape/
│   ├── 01-Claude-Code-Essentials.md          # Chapter 6
│   ├── 02-Gemini-CLI-Basics.md               # Chapter 7
│   ├── 03-GitHub-Copilot-Integration.md      # Chapter 8
│   └── 04-Choosing-Your-Tools.md             # Chapter 9
│
├── 04-Prompt-Context-Engineering/
│   ├── 01-Writing-Effective-Prompts.md       # Chapter 10
│   ├── 02-Context-Management.md              # Chapter 11
│   ├── 03-Debugging-AI-Code.md               # Chapter 12
│   └── 04-Advanced-Techniques.md             # Chapter 13
│
├── 05-Modern-Python-Type-Hints/
│   ├── 01-Functions-Types-Hints.md           # Chapter 14
│   ├── 02-Data-Structures.md                 # Chapter 15
│   ├── 03-Object-Oriented-Programming.md     # Chapter 16
│   ├── 04-Testing-Quality.md                 # Chapter 17
│   ├── 05-Error-Handling.md                  # Chapter 18
│   ├── 06-APIs-Data.md                       # Chapter 19
│   ├── 07-Clean-Code.md                      # Chapter 20
│   └── 08-First-Real-Project.md              # Chapter 21
│
├── 06-Spec-Kit-Methodology/
│   ├── 01-SDD-Fundamentals.md                # Chapter 22
│   ├── 02-Writing-Specifications.md          # Chapter 23
│   ├── 03-Planning-Tasking.md                # Chapter 24
│   ├── 04-Real-World-Workflows.md            # Chapter 25
│   └── 05-Scaling-for-Teams.md               # Chapter 26
│
├── 07-Agentic-AI/
│   ├── 01-Agentic-AI-Intro.md                # Chapter 27
│   ├── 02-Building-Your-First-Agent.md       # Chapter 28
│   └── 03-Agent-Orchestration.md             # Chapter 29
│
└── 08-MCP-Fundamentals/
    ├── 01-MCP-Intro.md                       # Chapter 30
    ├── 02-Integrating-MCP.md                 # Chapter 31
    └── 03-Building-MCP-Servers.md            # Chapter 32
```

### Naming Conventions

- **Part folder**: `NN-Part-Name/` (e.g., `02-Introducing-AI-Driven-Development/`)
- **Chapter file**: `NN-Chapter-Name.md` (e.g., `01-Welcome-to-AI-Coding.md`)
- Use hyphens between words, NO underscores or spaces
- Numbers help with ordering: `01-`, `02-`, etc.
- Docusaurus automatically removes numbers from URLs and titles
- Keep names descriptive but concise (3-6 words ideal)

---

## Docusaurus YAML Frontmatter

Every chapter file MUST begin with YAML frontmatter. Here's the complete template:

```yaml
---
sidebar_position: [N]                    # Chapter number (1-32)
title: "Chapter N: [Full Descriptive Title]"
description: "[One-sentence description for search and sidebar preview]"
keywords: [key, words, for, search]     # 3-5 relevant keywords
---
```

### Frontmatter Details

#### `sidebar_position`
- **Purpose**: Controls chapter ordering in Docusaurus sidebar
- **Value**: Chapter number (1-32)
- **Example**: `sidebar_position: 1` for Chapter 1

#### `title`
- **Purpose**: Appears in sidebar, page header, and browser tab
- **Format**: Include chapter number and full descriptive title
- **Example**: `title: "Chapter 1: Welcome to AI-Driven Development"`

#### `description`
- **Purpose**: Appears in search results and as sidebar hover text
- **Format**: One clear sentence, 8-15 words
- **Example**: `description: "Understand AI as your coding partner and set up your development environment"`

#### `keywords` (Optional but Recommended)
- **Purpose**: Improves search discoverability
- **Format**: Array of 3-5 lowercase terms
- **Example**: `keywords: [ai, python, coding-assistant, setup, getting-started]`

### Complete Frontmatter Example

```yaml
---
sidebar_position: 1
title: "Chapter 1: Welcome to AI-Driven Development"
description: "Understand how AI can be your coding partner and set up your first development environment"
keywords: [ai-driven-development, python, introduction, setup, learning]
---
```

---

## Content Structure After Frontmatter

After the frontmatter, follow this exact structure:

### 1. Chapter Header (H1)

```markdown
# Chapter 1: Welcome to AI-Driven Development
```

**Rules**:
- Use H1 (single `#`) exactly once per file
- Must match the title in frontmatter
- Appears as page heading

### 2. Opening Elements (Optional)

If desired, include an epigraph or opening quote:

```markdown
> "The best programmer is the one who leverages their tools effectively."
> — [Attribution]
```

### 3. Introduction Section (No header needed)

Start immediately with prose introduction (300-500 words):

```markdown
In this chapter, you'll learn...

[2-3 paragraphs of engaging introduction]
```

### 4. Learning Objectives Section

```markdown
## What You'll Learn

By the end of this chapter, you will be able to:

- [Specific, measurable objective 1]
- [Specific, measurable objective 2]
- [Specific, measurable objective 3]
```

### 5. Lesson Sections

Use H2 (`##`) for main lessons:

```markdown
## Lesson 1: [Lesson Title]

[Lesson introduction and content...]

### Subsection Title

[Detailed content...]
```

**Structure**:
- Each chapter has 2-5 lessons
- Each lesson is 1,500-3,000 words
- Use H3 (`###`) for subsections within lessons
- Include code blocks, examples, and callouts throughout

### 6. Summary Section

```markdown
## Chapter Summary

[Synthesis of all lessons, connecting them into a cohesive theme...]

[2-3 paragraphs wrapping up the chapter]
```

### 7. Key Takeaways

```markdown
## Key Takeaways

- [Important point 1]
- [Important point 2]
- [Important point 3]
- [Important point 4]
```

### 8. Review Questions

```markdown
## Review Questions

1. [Question testing basic recall]
2. [Question testing understanding]
3. [Question testing application]
4. [Question testing analysis]
5. [Question testing evaluation]

<details>
<summary>Answer Key</summary>

1. [Answer 1]
2. [Answer 2]
3. [Answer 3]
4. [Answer 4]
5. [Answer 5]

</details>
```

### 9. What's Next Section

```markdown
## What's Next

In the next chapter, [brief preview of next chapter]...

[1-2 paragraphs explaining how upcoming content builds on this chapter]
```

---

## Docusaurus-Specific Formatting

### Code Blocks

Always include language identifier:

```python
# Python example
def my_function():
    return "Hello, World!"
```

Docusaurus supports: python, javascript, typescript, jsx, tsx, bash, shell, yaml, json, xml, html, css, etc.

### Callouts (Alerts)

Docusaurus uses blockquote syntax with specific prefixes:

```markdown
> **Note**: This is a note callout
>
> Multiple lines work fine.

> **Tip**: This is a helpful tip

> **Warning**: This is important information

> **Info**: General information
```

Renders as colored callout boxes in HTML.

### Admonitions (Alternative)

Some Docusaurus configs support:

```markdown
:::note
This is a note
:::

:::tip
This is a tip
:::

:::warning
This is a warning
:::

:::info
This is info
:::
```

**Use blockquote format** (top method) if unsure—it's more compatible.

### Internal Links

Link to other chapters using relative paths:

```markdown
See [Chapter 2: Understanding AI Tools](./02-Understanding-AI-Tools.md) for more details.

Or reference other docs:
Learn about [Spec-Kit Methodology](../06-Spec-Kit-Methodology/01-SDD-Fundamentals.md)
```

### Code References in Text

When referencing code constructs:

```markdown
The `my_function()` method accepts a `string` parameter.

In the example above (lines 5-10), we define the class structure.
```

### Tables

Standard Markdown tables (Docusaurus renders them well):

```markdown
| Tool | Best For | Learning Curve |
|------|----------|-----------------|
| Claude Code | Complex projects | Moderate |
| Gemini CLI | Quick scripts | Easy |
| Copilot | IDE integration | Easy |
```

---

## Cross-Chapter Consistency

### Maintaining Narrative Flow

When chapter content references previous chapters:

```markdown
As we learned in [Chapter 3: Collaboration Basics](../02-Introducing-AI-Driven-Development/03-Collaboration-Basics.md),
AI tools work best when you provide clear context...
```

### Consistent Code Example Style

All code examples should follow consistent patterns:

1. **Setup comment**: Explain what this demonstrates
2. **Clear, annotated code**: Comments explain key lines
3. **Expected output**: Show what the code should produce
4. **Learning prompt**: Suggest how to explore further

```python
# Example: Demonstrating type hints in function definitions
from typing import List

def greet_people(names: List[str]) -> str:
    """Return a greeting for a list of names."""
    return f"Hello, {', '.join(names)}!"

result = greet_people(["Alice", "Bob"])
print(result)
# Output: Hello, Alice, Bob!
```

### Terminology Consistency

Maintain consistent terminology across chapters:
- Use "AI tool" not sometimes "AI tool", sometimes "tool", sometimes "assistant"
- Use "agent" vs "chatbot" distinction consistently (especially Parts 6-7)
- Define specialized terms once per part, then reference by name

---

## SEO and Discoverability

### Meta Description

The `description` frontmatter field is critical for search:

```yaml
description: "Short, clear sentence that would make sense in a search result"
```

**Good**:
- `"Learn how to write effective prompts for Python development with AI assistance"`

**Bad**:
- `"Chapter about prompting"`
- `"Various prompt engineering concepts"`

### Keywords

Optional but improves search:

```yaml
keywords: [prompt-engineering, python, ai-driven-development, coding-tips, best-practices]
```

### Heading Hierarchy

Proper heading hierarchy helps Docusaurus generate accurate table of contents:

```markdown
# Chapter Title (H1 - one per file)

## Major Section (H2)

### Subsection (H3)

#### Details (H4, use sparingly)
```

DON'T skip heading levels (e.g., don't jump from H1 to H3).

---

## File Size and Performance

Docusaurus performs best with:

- **Ideal file size**: 4,000-10,000 words per chapter
- **Maximum recommended**: 15,000 words (consider splitting if larger)
- **Maximum heading depth**: H3 is recommended, H4 acceptable, avoid H5+

Longer chapters load fine but are harder to navigate. If a chapter exceeds 12,000 words, consider:
1. Splitting into two chapters, OR
2. Moving some content to appendices

---

## Building and Testing Locally

Before submitting chapters, test locally:

```bash
cd /path/to/colearning-python
npm install  # If not already done
npm run start  # Starts development server
# Visit http://localhost:3000 to preview
```

Check:
- [ ] Chapter appears in sidebar in correct position
- [ ] All links work (especially cross-chapter references)
- [ ] Code blocks display correctly with syntax highlighting
- [ ] Images/diagrams render properly
- [ ] Table of contents is generated correctly
- [ ] No broken Markdown syntax

---

## Complete Frontmatter+Structure Template

Use this as a starting point:

```yaml
---
sidebar_position: [N]
title: "Chapter [N]: [Title]"
description: "[One-sentence description]"
keywords: [keyword1, keyword2, keyword3, keyword4, keyword5]
---

# Chapter [N]: [Title]

> "[Optional opening quote]"
> — [Attribution]

[2-3 paragraph introduction explaining chapter importance and preview]

## What You'll Learn

By the end of this chapter, you will be able to:

- [Objective 1]
- [Objective 2]
- [Objective 3]

## Lesson 1: [First Lesson Title]

[Content with H3 subsections...]

### Subsection

[Details...]

## Lesson 2: [Second Lesson Title]

[Content...]

## Chapter Summary

[Wrap-up and synthesis...]

## Key Takeaways

- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

## Review Questions

[Questions and hidden answers...]

## What's Next

[Preview of next chapter...]
```

---

## Special Handling for Advanced Topics

### Agentic AI Chapters (27-29)

In frontmatter:

```yaml
keywords: [agentic-ai, agents, autonomous-systems, goal-seeking, tool-use]
```

In content:
- Include ASCII diagrams for agent loops
- Use consistent terminology: agent, goal, state, action, tool
- Include debug traces showing agent reasoning

### MCP Chapters (30-32)

In frontmatter:

```yaml
keywords: [model-context-protocol, mcp, integration, tools, servers]
```

In content:
- Include protocol diagrams (ASCII or description)
- Show client and server code in parallel where appropriate
- Emphasize standardization and reusability

---

## Validation Checklist

Before submitting a chapter, verify:

- [ ] Frontmatter is complete (sidebar_position, title, description, keywords)
- [ ] H1 title matches frontmatter title
- [ ] File is named correctly: `NN-Chapter-Name.md`
- [ ] File is in correct directory: `docs/NN-Part-Name/`
- [ ] All internal links use relative paths and work
- [ ] Code blocks include language identifiers
- [ ] No broken Markdown syntax
- [ ] Heading hierarchy is proper (H1 > H2 > H3)
- [ ] Chapter length is 4,000-10,000 words
- [ ] All 9 sections present: Intro, Objectives, Lessons, Summary, Takeaways, Review, Next
- [ ] For advanced topics: Includes required diagrams/elements
- [ ] Local Docusaurus build succeeds with no warnings
