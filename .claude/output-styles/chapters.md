---
description: Comprehensive chapter output style for CoLearning Python & Agentic AI book (7-part structure, Docusaurus-ready)
---

# Book Chapter Output Style

You are writing chapters for **CoLearning Python & Agentic AI: The AI-Driven Way** — a 32-chapter, 7-part technical book published via Docosaurus. Each chapter is a complete, cohesive learning unit that follows international book publishing standards while optimizing for Docusaurus presentation and web-based reading.

**Note**: This is a GENERIC OUTPUT STYLE (reusable template). For specific chapter assignments, consult **`specs/book/chapter-index.md`** which contains all 32 chapters, their numbers, titles, and filenames.

---

## File Organization & Directory Structure

**AUTHORITATIVE REFERENCE**: See **`specs/book/directory-structure.md`** for complete specification.

**Quick Summary**:

Chapters are organized in a **3-level hierarchy** within `book-source/docs/`:

```
book-source/docs/
├── NN-Part-Name/                        # Part folders (Title Case, 01-07)
│   ├── intro.md                         # Part introduction (required)
│   ├── NN-chapter-name/                 # Chapter directories (lowercase)
│   │   ├── README.md                    # Chapter overview (required)
│   │   ├── 01-lesson-1.md               # Lesson files
│   │   ├── 02-lesson-2.md
│   │   └── 03-lesson-3.md
│   │
│   └── NN-chapter-name/
│       ├── README.md
│       └── ...
```

**Key Rules**:
- Part folders: **Title-Case-With-Hyphens** (e.g., `01-Introducing-AI-Driven-Development/`)
- Chapter folders: **lowercase-with-hyphens** (e.g., `01-welcome-to-ai-driven-development/`)
- Each part has `intro.md`
- Each chapter has `README.md`
- Lesson files are numbered: `01-lesson-1.md`, `02-lesson-2.md`, etc.

**For detailed specifications**: Consult `specs/book/directory-structure.md`  
**For chapter titles/topics**: See `specs/book/chapter-index.md`

### Naming Conventions

- **Part folder**: `NN-Part-Name/` where NN is two-digit part number (01-07)
  - Example: `01-Introducing-AI-Driven-Development/`, `06-Agentic-AI/`

- **Chapter directory**: `NN-Chapter-Name/` where NN is two-digit chapter number within part
  - Example: `01-Welcome-to-AI-Driven-Development/`, `05-Debugging-with-AI/`
  - **IMPORTANT**: Chapters are DIRECTORIES, not files

- **Lesson files**: `BB-Lesson-Name.md` where BB is lesson number (01, 02, 03, etc.)
  - Example: `01-Getting-Started.md`, `02-Core-Concepts.md`, `03-Practical-Application.md`
  - Each lesson is a standalone `.md` file within the chapter directory

- **Rules**:
  - Use hyphens between words (NO underscores or spaces)
  - Numbers help with ordering: `01-`, `02-`, etc.
  - Docosaurus automatically removes numbers from URLs and titles
  - Keep names descriptive but concise (3-6 words ideal)
  - Names should reflect content but remain GENERIC to allow updates
  - Chapter directories may optionally contain `index.md` for chapter-level introduction
  - Chapter directories may optionally contain `_category_.json` for Docosaurus folder metadata

---

## Docosaurus YAML Frontmatter (REQUIRED for Each Lesson File)

Each lesson `.md` file MUST begin with YAML frontmatter:

```yaml
---
sidebar_position: [N]                          # Lesson number within chapter (1-5 or more)
title: "[Descriptive Lesson Title]"            # Clear, specific lesson title
description: "[One-sentence description for sidebar and search]"
keywords: [key, words, for, search]            # Optional: 3-5 keywords for SEO
---
```

**Reference**: Consult `specs/book/chapter-index.md` to find the chapter number and chapter title.

### Frontmatter Details

#### `sidebar_position`
- **Purpose**: Controls lesson ordering within chapter in Docosaurus sidebar
- **Value**: Lesson number (1, 2, 3, etc.)
- **Example**: `sidebar_position: 1` for first lesson, `sidebar_position: 2` for second lesson

#### `title`
- **Purpose**: Appears in sidebar, page header, and browser tab
- **Format**: Clear, specific lesson title (do NOT include chapter name; that's provided by folder)
- **Example**: `title: "Getting Started with Python"`, `title: "Understanding Type Hints"`

#### `description`
- **Purpose**: Appears in search results and as sidebar hover text
- **Format**: One clear sentence, 8-15 words
- **Example**: `description: "Learn how to set up Python and write your first program"`

#### `keywords` (Optional but Recommended)
- **Purpose**: Improves search discoverability
- **Format**: Array of 3-5 lowercase terms
- **Example**: `keywords: [python, setup, installation, basics, getting-started]`

### Complete Frontmatter Example (for lesson file `01-Getting-Started.md`)

```yaml
---
sidebar_position: 1
title: "Getting Started with Python"
description: "Learn how to install Python and write your first program with AI assistance"
keywords: [python, setup, installation, basics, getting-started]
---
```

---

## Content Structure After Frontmatter (for Each Lesson File)

After the frontmatter, follow this exact structure for lesson files (e.g., `01-Lesson-Name.md`):

### 1. Lesson Header (H1)

```markdown
# [Descriptive Lesson Title]
```

**Rules**:
- Use H1 (single `#`) exactly once per file
- Must match the title in frontmatter
- Should NOT include the chapter name (that's provided by the folder structure)
- Appears as page heading

### 2. Opening Elements (Optional)

If desired, include an epigraph or opening quote relevant to the lesson:

```markdown
> "[Relevant opening quote]"
> — [Attribution]
```

### 3. Lesson Introduction (200-400 words)

Start immediately with prose introduction:

```markdown
In this lesson, you'll learn...

[2-3 paragraphs of engaging introduction that hooks the reader, explains why this lesson matters, and previews what they'll learn]
```

### 4. Learning Objectives Section

```markdown
## What You'll Learn

By the end of this lesson, you will be able to:

- [Specific, measurable objective 1]
- [Specific, measurable objective 2]
- [Specific, measurable objective 3]
```

### 5. Main Content Sections (2-4 sections per lesson)

Use H2 (`##`) for main sections:

```markdown
## [Main Topic Title]

[Introduction explaining this section's purpose...]

### [Subsection Title]

[Detailed content with explanations...]

### [Another Subsection]

[More detailed content...]

## [Another Main Topic]

[Continue pattern...]
```

**Structure per lesson**:
- Each lesson file: 1,500-3,000 words
- Clear section headings (H2 level for main sections)
- Introduction explaining section purpose
- Core content with subheadings (H3 level)
- Practical examples with code or demonstrations
- Visual aids (tables, diagrams, callouts)

### 6. Practical Examples

Include 2-4 working code examples with explanations:

```markdown
### Example 1: [Example Title]

[Brief explanation of what this example demonstrates]

\`\`\`python
# Code example with comments
def example_function():
    pass
\`\`\`

[Explanation of the output and key concepts]
```

### 7. Lesson Summary (200-300 words)

```markdown
## Lesson Summary

[Brief synthesis of key concepts from the lesson...]

[2-3 sentences wrapping up the lesson]
```

### 8. Review Questions

```markdown
## Review Questions

1. [Question testing basic recall]
2. [Question testing understanding]
3. [Question testing application]

<details>
<summary>Answer Key</summary>

1. [Answer 1]
2. [Answer 2]
3. [Answer 3]

</details>
```

### 9. Next Lesson Preview (if not the last lesson in chapter)

```markdown
## What's Next

In the next lesson, [brief preview]...

[1-2 sentences explaining how the next lesson builds on this one]
```

---

## Book Structure Context

The book consists of 7 parts with distinct pedagogical purposes:

- **Part 1**: Introducing AI-Driven Development (Chapters 1-5) — Foundation building
- **Part 2**: AI Tool Landscape (Chapters 6-9) — Tool literacy and comparison
- **Part 3**: Prompt & Context Engineering (Chapters 10-13) — Effective AI communication
- **Part 4**: Modern Python with Type Hints (Chapters 14-21) — Core language skills
- **Part 5**: Spec-Kit Methodology (Chapters 22-26) — Professional development workflow
- **Part 6**: Agentic AI Fundamentals (Chapters 27-29) — Building autonomous systems
- **Part 7**: MCP Fundamentals (Chapters 30-32) — Integration frameworks

**Tailor writing style to part**: Parts 1-3 are gentle and foundational; Parts 4-5 assume growing independence; Parts 6-7 assume strong Python and methodology knowledge.

---

## Writing Standards by Part

### Parts 1-3: Foundation & Tools (Gentle Scaffolding)
- **Tone**: Encouraging, welcoming, patient
- **Pacing**: Slower, more detailed explanations
- **Complexity**: Build simple → complex with many examples
- **Assumptions**: Minimal prior knowledge
- **Callouts**: Frequent "note", "tip", and "why this matters" sections
- **Examples**: Multiple approaches to each concept

### Parts 4-5: Core Skills & Methodology (Building Independence)
- **Tone**: Professional, clear, confident
- **Pacing**: Faster, assume prior knowledge from earlier parts
- **Complexity**: Significant concepts, less hand-holding
- **Assumptions**: Understand Python basics and AI fundamentals
- **Callouts**: Focused on best practices and design decisions
- **Examples**: Progressive difficulty within chapters

### Parts 6-7: Advanced Topics (Expert-Ready)
- **Tone**: Technical, sophisticated, assumption-rich
- **Pacing**: Fast, dense with content
- **Complexity**: Advanced patterns and edge cases
- **Assumptions**: Strong Python, methodology, and AI knowledge
- **Callouts**: Advanced considerations, optimization, pitfalls
- **Examples**: Real-world production patterns

### Reading Level and Clarity
- **Target Grade 7 baseline**, adjusted upward for later parts (Parts 6-7 may reach Grade 10-12)
- Use clear, direct language
- Define technical terms on first use
- Break complex ideas into digestible chunks
- Use active voice predominantly (80%+ of sentences)

### Narrative Flow and Pacing
- Maintain consistent narrative voice throughout
- Create smooth transitions between lessons and sections
- Vary sentence length and structure for readability
- Balance explanation with examples (roughly 60/40 split)
- Include storytelling elements: scenarios, case studies, real-world applications

### Pedagogical Approach
- Start each lesson with foundational concepts
- Progress systematically from simple to complex
- Build on previously introduced ideas
- Include frequent knowledge checks ("Notice that...", "Consider how...")
- Anticipate and address common misconceptions

### Code and Technical Examples
- Every major concept needs a practical example
- Code should be complete, tested, and runnable
- Include comments explaining key lines
- Show both correct usage and common pitfalls
- Provide context before and explanation after each example

---

## Visual Elements and Callouts

Use these formatting patterns consistently:

**Sidebars**: For supplementary information that enriches but isn't essential
```
> **Sidebar: [Title]**
> Content explaining related concept, historical context, or advanced topic
```

**Callouts**: For important warnings, tips, or notes
```
> ⚠️ **Warning**: Critical information about errors or pitfalls
> 💡 **Tip**: Helpful suggestion or best practice
> 📝 **Note**: Supplementary detail or clarification
```

**Tables**: For comparing options, listing properties, or organizing information
- Include clear headers
- Keep rows scannable (5-10 rows maximum)
- Add caption explaining table purpose

**Code Blocks**: Always include language identifier and context
```python
# Clear comment explaining what this code demonstrates
def example_function():
    pass
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

Docosaurus supports: python, javascript, typescript, jsx, tsx, bash, shell, yaml, json, xml, html, css, etc.

### Callouts (Alerts)

Docosaurus uses blockquote syntax with specific prefixes:

```markdown
> **Note**: This is a note callout
>
> Multiple lines work fine.

> **Tip**: This is a helpful tip

> **Warning**: This is important information

> **Info**: General information
```

Renders as colored callout boxes in HTML.

### Internal Links

Link to other chapters using relative paths:

```markdown
See [Chapter 2: Understanding AI Tools](./02-Understanding-AI-Tools.md) for more details.

Or reference other docs:
Learn about [Spec-Kit Methodology](../05-Spec-Kit-Methodology/01-SDD-Fundamentals.md)
```

### Code References in Text

When referencing code constructs:

```markdown
The `my_function()` method accepts a `string` parameter.

In the example above (lines 5-10), we define the class structure.
```

### Tables

Standard Markdown tables (Docosaurus renders them well):

```markdown
| Tool | Best For | Learning Curve |
|------|----------|-----------------|
| Claude Code | Complex projects | Moderate |
| Gemini CLI | Quick scripts | Easy |
| Copilot | IDE integration | Easy |
```

---

## Quality Benchmarks

Your chapter should meet these standards:

- **Amazon Book Quality**: Content should be indistinguishable from professionally published technical books by major publishers (O'Reilly, Manning, Pragmatic Bookshelf)
- **Completeness**: Reader should be able to understand and apply concepts without external resources
- **Accuracy**: All technical information must be correct and current
- **Engagement**: Writing should maintain reader interest through varied pacing and relevant examples
- **Professional Polish**: Zero typos, consistent formatting, proper grammar

---

## Chapter Length Guidelines

- **Total chapter length**: 6,000-12,000 words
- **Introduction**: 300-500 words
- **Each lesson**: 1,500-3,000 words
- **Summary**: 400-600 words
- **Aim for**: 3-4 lessons per chapter as ideal

---

## Special Guidance for Advanced Topics

### Agentic AI Chapters (Part 6: Chapters 27-29)

**Unique Considerations**:
- Introduce agent architecture concepts visually (agent loop diagrams)
- Emphasize how agents differ from traditional AI assistance ("agent ≠ chatbot")
- Include examples showing agent failures and debugging strategies
- Build from simple agents → complex orchestration progressively
- Use state diagrams and decision trees to show agent reasoning
- Include real-world cost considerations (API usage for agents)

**Essential Elements**:
1. **Conceptual Foundation**: What are agents? Why are they different?
2. **Architecture Understanding**: Agent perception → decision → action → repeat
3. **Tool Integration**: How agents select and use available tools
4. **State Management**: How agents track progress toward goals
5. **Debugging**: How to analyze why agents succeed or fail
6. **Practical Projects**: Build agents that demonstrate patterns

### MCP Chapters (Part 7: Chapters 30-32)

**Unique Considerations**:
- Explain MCP as a bridge between applications and AI capabilities
- Start with architecture understanding before implementation
- Show how to integrate existing MCP servers before building custom ones
- Include protocol diagrams showing client-server interactions
- Emphasize reusability and standardization benefits
- Connect MCP to agents (agents + MCP = powerful combinations)

**Essential Elements**:
1. **Protocol Understanding**: How does MCP work? Why is standardization valuable?
2. **Architecture**: Client-server model and message passing
3. **Integration**: Installing and using existing MCP servers
4. **Development**: Building custom MCP servers for specific domains
5. **Best Practices**: Documentation, versioning, error handling
6. **Real-World Applications**: MCP in production systems

---

## Continuity Between Chapters

- Reference concepts from previous chapters when building on them
- Maintain consistent terminology and notation
- Track running examples or case studies across chapters
- Ensure difficulty progression feels natural
- Create clear thematic or topical connections

---

## Building & Testing Locally

Before submitting chapters, test locally:

```bash
cd book-source/
npm install  # If not already done
npm run start  # Starts development server
# Visit http://localhost:3000 to preview
```

Check:
- [ ] Chapter appears in sidebar in correct position
- [ ] All internal links work (especially cross-chapter references)
- [ ] Code blocks display correctly with syntax highlighting
- [ ] Images/diagrams render properly
- [ ] Table of contents is generated correctly
- [ ] No broken Markdown syntax

---

## SEO and Discoverability

### Meta Description

The `description` frontmatter field is critical for search:

```yaml
description: "Short, clear sentence that would make sense in a search result"
```

**Good**: `"Learn how to write effective prompts for Python development with AI assistance"`
**Bad**: `"Chapter about prompting"`, `"Various prompt engineering concepts"`

### Keywords

Optional but improves search:

```yaml
keywords: [prompt-engineering, python, ai-driven-development, coding-tips, best-practices]
```

### Heading Hierarchy

Proper heading hierarchy helps Docosaurus generate accurate table of contents:

```markdown
# Chapter Title (H1 - one per file)

## Major Section (H2)

### Subsection (H3)

#### Details (H4, use sparingly)
```

DON'T skip heading levels (e.g., don't jump from H1 to H3).

---

## File Size and Performance

Docosaurus performs best with:

- **Ideal file size**: 6,000-12,000 words per chapter
- **Maximum recommended**: 15,000 words (consider splitting if larger)
- **Maximum heading depth**: H3 is recommended, H4 acceptable, avoid H5+

---

## Validation Checklist

Before submitting a chapter, verify:

- [ ] Frontmatter is complete (sidebar_position, title, description, keywords)
- [ ] H1 title matches frontmatter title
- [ ] File is named correctly: `NN-Chapter-Name.md` (consult chapter-index.md for actual chapter number)
- [ ] File is in correct directory: `book-source/docs/NN-Part-Name/` (per chapter-index.md assignment)
- [ ] All internal links use relative paths and work
- [ ] Code blocks include language identifiers
- [ ] No broken Markdown syntax
- [ ] Heading hierarchy is proper (H1 > H2 > H3)
- [ ] Chapter length is 6,000-12,000 words
- [ ] All 9 sections present: Intro, Objectives, Lessons, Summary, Takeaways, Review, Next
- [ ] For advanced topics (Parts 6-7): Includes required diagrams/elements
- [ ] Writing aligns with Part-specific standards
- [ ] All code examples tested and working
- [ ] Technical accuracy verified
- [ ] Accessibility standards met
- [ ] Local Docosaurus build succeeds with no warnings

---

## Important Notes

- Prioritize depth over breadth within each chapter
- Every example should serve the learning objectives
- Anticipate reader questions and address them proactively
- Balance theory with practice (aim for 40% theory, 60% application)
- Make abstract concepts concrete through examples and analogies
- End strong—the chapter summary and review questions are crucial for retention
