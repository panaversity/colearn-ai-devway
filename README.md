# 📘 CoLearning Python Book Directory & Generation Structure

This document defines the canonical folder structure and file organization strategy for the "CoLearning Python: The AI-Driven Way" technical book project. It serves as the reference for all contributors, especially book generation agents and Docusaurus site maintainers.

---

## 🧭 Overview

This book is structured as a 5-part technical guide. Each part contains multiple **chapters**, which include multiple **lessons**, which in turn contain multiple **topics**. This three-tier hierarchy (Chapter → Lesson → Topic) ensures clarity, modularity, and scalability.

All content is published as a [Docusaurus](https://docusaurus.io/) site, with auto-generated sidebars and strict adherence to Docusaurus-compatible Markdown.

The content is organized under:

- `docs/`: All book content (chapters, lessons, topics, projects, appendices)

---

## 📂 Folder Structure

```
book-source/
├── docs/
│   ├── 01-Intro.md                           # Book introduction
│   │
│   ├── 02-AI-Driven-Development/
│   │   ├── 01-Welcome-to-AI-Coding.md       # Chapter overview
│   │   ├── 02-Understanding-AI-Tools.md     # Chapter overview
│   │   └── 03-Collaboration-Basics.md       # Chapter overview
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
│   ├── 04-Advanced-Python/
│   │   ├── 01-Functions-and-Modules/
│   │   │   ├── 01-Function-Basics.md       # Lesson
│   │   │   ├── 02-Advanced-Functions.md   # Lesson
│   │   │   └── 03-Modules-and-Packages.md # Lesson
│   │   ├── 02-Object-Oriented-Programming/
│   │   │   ├── 01-Classes-and-Objects.md # Lesson
│   │   │   ├── 02-Inheritance.md          # Lesson
│   │   │   └── 03-Polymorphism.md        # Lesson
│   │   └── 03-Error-Handling/
│   │       ├── 01-Exceptions.md           # Lesson
│   │       ├── 02-Debugging.md            # Lesson
│   │       └── 03-Logging.md              # Lesson
│   │
│   ├── 05-Real-World-Projects/
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

## 🏷️ Naming Conventions

| Level          | Format                | Example                                  |
| -------------- | --------------------- | ---------------------------------------- |
| Part folder    | `##-Name/`            | `02-AI-Driven-Development/`      |
| Chapter folder | `##-Chapter-Name/`    | `01-Python-Basics/`                      |
| Lesson file    | `##-Lesson-Name.md`   | `01-Getting-Started.md`                 |

---

## 📐 Docusaurus Compatibility

This structure uses **Docusaurus number prefixes** for automatic sidebar ordering.

- Each folder/file uses `##-Name` format for automatic ordering
- Docusaurus automatically removes number prefixes from URLs and titles
- Folders become sidebar categories, files become sidebar items

### 🔗 Internal Linking

Use relative links between topics:

```md
See [Variables and Types](./02-Variables-and-Types.md) for more details.
```

---

## ✅ Book Agent Output Rules

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

## 💡 Best Practices

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



