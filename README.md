# CoLearning Python: The AI-Driven Way

## Vision

"CoLearning Python: The AI-Driven Way" is a 26-chapter technical book that teaches modern AI-driven development using Python (3.13+) through systematic collaboration between human learners and AI assistants. 

Our vision is to pioneer a new agent-native paradigm of CS education where AI is a co-learner and a collaborator, reflecting the reality of modern software development.

## Core Philosophy

*   **AI as a Collaborative Partner:** We treat AI tools as intelligent co-workers, working together within shared constraints.
*   **Specification-First Methodology:** Clear requirements precede all work. We use the "Spec-Kit" methodology for iterative, AI-friendly development.
*   **Learning by Doing:** Every concept is practiced through realistic, AI-assisted hands-on work.
*   **Transparency:** We teach our methodology and demonstrate it throughout the book.

## Target Audience

*   **Primary:** Programming beginners with no prior coding experience.
*   **Secondary:** Professional developers transitioning to AI-driven development.

## Key Features

*   **AI-First Learning:** Learn Python with AI as a partner from day one.
*   **Modern Python:** All code uses Python 3.13+ features with mandatory type hints.
*   **Pedagogically Sound:** Content is guided by 8 specialized "co-learning skills" based on educational research.
*   **Structured and Consistent:** A project constitution and defined output styles ensure a high-quality, consistent reading experience.
*   **Tool Diversity:** Learn to work with a variety of AI tools, including Claude Code, Gemini CLI, and OpenAI Codex.

## The 8 CoLearning Skills

1.  **learning-objectives:** Generate measurable learning outcomes.
2.  **concept-scaffolding:** Break down complex topics into manageable steps.
3.  **code-example-generator:** Create high-quality, runnable code examples.
4.  **exercise-designer:** Design effective practice exercises.
5.  **assessment-builder:** Build meaningful quizzes and assessments.
6.  **technical-clarity:** Ensure all explanations are clear and accessible.
7.  **book-architecture:** Structure the book's content for a logical flow.
8.  **ai-augmented-teaching:** Design lessons that effectively integrate AI tools.

## 📘 Book Directory & Generation Structure

This book is structured as a technical guide. Each part contains multiple **chapters**, which in turn contain multiple **topics**. This hierarchy ensures clarity, modularity, and scalability.

All content is published as a [Docusaurus](https://docusaurus.io/) site, with auto-generated sidebars and strict adherence to Docusaurus-compatible Markdown.

The content is organized under:

- `docs/`: All book content (chapters, lessons, topics, projects, appendices)

---

### 📂 Folder Structure

```
book-source/
├── docs/
│   ├── 01-Intro.md                           # Book introduction
│   │
│   ├── 02-AI-Driven-Development/
│   │   ├── 01-Welcome-to-AI-Coding       # Chapter overview
│   │   ├── 02-Understanding-AI-Tools     # Chapter overview
│   │   └── 03-Collaboration-Basics       # Chapter overview
│   │
│   ├── 03-Python-Fundamentals/
│   │   ├── 01-Python-Basics/
│   │   │   ├── 01-Getting-Started.md       # Lesson
│   │   │   ├── 02-Variables-and-Types.md   # Lesson
│   │   │   └── 03-Basic-Operations.md      # Lesson
│   │   ├── 02-Data-Structures/
│   │   │   ├── 01-Lists-and-Tuples.md      # Lesson
│   │   │   ├── 02-Dictionaries.md          # Lesson
│   │   │   └── 03-Sets.md                  # Lesson
│   │   └── 03-Control-Flow/
│   │       ├── 01-Conditionals.md          # Lesson
│   │       ├── 02-Loops.md                 # Lesson
│   │       └── 03-Functions.md             # Lesson
│   │
│   ├── 04-Real-World-Projects/
│   │   ├── 01-Todo-CLI-Application/
│   │   │   ├── 01-Project-Setup.md        # Lesson
│   │   │   ├── 02-Core-Features.md        # Lesson
│   │   │   └── 03-Advanced-Features.md   # Lesson
│   │   ├── 02-API-Client-Project/
│   │   │   ├── 01-HTTP-Requests.md       # Lesson
│   │   │   ├── 02-Data-Parsing.md        # Lesson
│   │   │   └── 03-Error-Handling.md       # Lesson
│   │   └── 03-Data-Analysis-Tool/
│   │       ├── 01-Data-Loading.md         # Lesson
│   │       ├── 02-Data-Processing.md     # Lesson
│   │       └── 03-Visualization.md       # Lesson
│   │
│   ├── 06-Best-Practices/
│   │   ├── 01-Code-Quality/
│   │   │   ├── 01-Coding-Standards.md    # Lesson
│   │   │   ├── 02-Documentation.md       # Lesson
│   │   │   └── 03-Code-Review.md        # Lesson
│   │   ├── 02-Testing-Strategies/
│   │   │   ├── 01-Unit-Testing.md       # Lesson
│   │   │   ├── 02-Integration-Testing.md # Lesson
│   │   │   └── 03-Test-Automation.md    # Lesson
│   │   └── 03-Deployment-Guide/
│   │       ├── 01-Environment-Setup.md  # Lesson
│   │       ├── 02-Deployment-Options.md  # Lesson
│   │       └── 03-Monitoring.md         # Lesson
│   │
│   ├── 07-Appendix/
│   │   ├── 01-Glossary.md
│   │   └── 02-Troubleshooting.md
│   │
│   └── 08-Projects/
│       ├── 01-Todo-CLI.md
│       └── 02-API-Client.md
│

```

---

### 🏷️ Naming Conventions

| Level          | Format                | Example                                  |
| -------------- | --------------------- | ---------------------------------------- |
| Part folder    | `##-Name/`            | `02-AI-Driven-Development/`      |
| Chapter folder | `##-Chapter-Name/`    | `01-Python-Basics/`                      |
| Lesson file    | `##-Lesson-Name.md`   | `01-Getting-Started.md`                 |

---

### 📐 Docusaurus Compatibility

This structure uses **Docusaurus number prefixes** for automatic sidebar ordering.

- Each folder/file uses `##-Name` format for automatic ordering
- Docusaurus automatically removes number prefixes from URLs and titles
- Folders become sidebar categories, files become sidebar items

#### 🔗 Internal Linking

Use relative links between topics:

```md
See [Variables and Types](./02-Variables-and-Types.md) for more details.
```

---

### ✅ Book Agent Output Rules

The book-generation agent must:

1. Write Docusaurus-compatible Markdown with frontmatter
2. Follow strict numbered naming conventions (`##-Name` format)
3. Use number prefixes for automatic sidebar ordering
4. Include the 3-level hierarchy:
   - **Part folders** (`##-Part-##-Name/`)
   - **Chapter folders** (`##-Chapter-Name/`)
   - **Lesson files** (`##-Lesson-Name.md`)
5. Avoid duplicate names or invalid characters

---

### 💡 Best Practices

- Use consistent number prefixes (`01-`, `02-`, etc.) for proper ordering
- Keep folder/file names descriptive but concise
- Use hyphens instead of underscores for better URL readability
---

## 🔍 Summary

This structure supports:

- **3-level hierarchy**: Part → Chapter → Lesson
- **Automatic sidebar ordering** using Docusaurus number prefixes
- **Clean URLs** with automatic prefix removal
- **Simple file management** without complex configuration files
- **Scalable book expansion** with consistent numbering