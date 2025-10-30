---
description: Comprehensive chapter output style for CoLearning Python & Agentic AI book (7-part structure, Docusaurus-ready)
---

# Book Chapter Output Style

Each chapter is a complete, cohesive learning unit that follows international book publishing standards while optimizing for Docusaurus presentation and web-based reading.

**Note**: This is a GENERIC OUTPUT STYLE (reusable template). For specific chapter assignments, consult **`specs/book/chapter-index.md`** which contains chapters, their numbers, titles, and filenames.

---

## File Organization & Directory Structure

**AUTHORITATIVE REFERENCE**: See **`specs/book/directory-structure.md`** for complete specification.

**Quick Summary**:

Chapters are organized in a **3-level hierarchy** within `book-source/docs/`:

```
book-source/docs/
├── NN-Part-Name/                        # Part folders (Title Case, 01-07)
│   ├── README.md                         # Part introduction (required)
│   ├── NN-chapter-name/                 # Chapter directories (lowercase)
│   │   ├── README.md                    # Chapter overview (required)
│   │   ├── 01-lesson-1.md               # Lesson files
│   │   ├── 02-lesson-2.md
│   │   └── 03-lesson-3.md

```

**Key Rules**:
- Part folders: **Title-Case-With-Hyphens** (e.g., `01-Introducing-AI-Driven-Development/`)
- Chapter folders: **lowercase-with-hyphens** (e.g., `01-welcome-to-ai-driven-development/`)
- Each part has `README.md`
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




