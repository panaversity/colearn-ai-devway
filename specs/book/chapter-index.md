# CoLearning Python & Agentic AI: Chapter Index

**32 chapters across 7 parts**

Reference this document when naming and organizing chapter files. Use the chapter number in filenames: `[chapter-number]-[chapter-name].md`

---

## Part 1: Introducing AI-Driven Development (Chapters 1-5)

Foundation building: orientation, setup, first programs with AI

| # | Chapter Title | File Name | Key Topics |
|---|---------------|-----------|------------|
| 1 | Welcome to AI-Driven Development | `01-Welcome-to-AI-Driven-Development.md` | AI as collaborative partner, course overview |
| 2 | Understanding AI Tools | `02-Understanding-AI-Tools.md` | AI tool landscape, capabilities, limitations |
| 3 | Setting Up Your Environment | `03-Setting-Up-Your-Environment.md` | Installation, configuration, first setup |
| 4 | Your First Program with AI | `04-Your-First-Program-with-AI.md` | Hello world, working with AI, basic workflow |
| 5 | Debugging and Iterating with AI | `05-Debugging-and-Iterating-with-AI.md` | Error handling, iteration cycles, AI assistance |

---

## Part 2: AI Tool Landscape (Chapters 6-9)

Tool literacy and comparison: deep dive into specific platforms

| # | Chapter Title | File Name | Key Topics |
|---|---------------|-----------|------------|
| 6 | Claude Code: Features and Workflows | `01-Claude-Code-Features-and-Workflows.md` | Claude capabilities, IDE integration |
| 7 | Gemini CLI: Installation and Basics | `02-Gemini-CLI-Installation-and-Basics.md` | Gemini setup, command-line usage |
| 8 | GitHub Copilot and Code Editors | `03-GitHub-Copilot-and-Code-Editors.md` | Copilot integration, editor support |
| 9 | Choosing the Right Tool for the Task | `04-Choosing-the-Right-Tool-for-the-Task.md` | Tool comparison, selection criteria |

---

## Part 3: Prompt & Context Engineering (Chapters 10-13)

Effective AI communication: prompting and context management

| # | Chapter Title | File Name | Key Topics |
|---|---------------|-----------|------------|
| 10 | Writing Effective Prompts | `01-Writing-Effective-Prompts.md` | Prompt structure, clarity, specificity |
| 11 | Context Management and Memory | `02-Context-Management-and-Memory.md` | Context windows, state management |
| 12 | Debugging AI-Generated Code | `03-Debugging-AI-Generated-Code.md` | Verification, testing, common issues |
| 13 | Advanced Prompt Techniques | `04-Advanced-Prompt-Techniques.md` | Few-shot learning, chaining, refinement |

---

## Part 4: Modern Python with Type Hints (Chapters 14-21)

Core language skills: production-quality Python

| # | Chapter Title | File Name | Key Topics |
|---|---------------|-----------|------------|
| 14 | Functions, Types, and Type Hints | `01-Functions-Types-and-Type-Hints.md` | Function definitions, type annotations |
| 15 | Data Structures with Type Safety | `02-Data-Structures-with-Type-Safety.md` | Lists, dicts, type hints for collections |
| 16 | Object-Oriented Programming (Modern) | `03-Object-Oriented-Programming-Modern.md` | Classes, inheritance, OOP patterns |
| 17 | Testing and Quality Assurance | `04-Testing-and-Quality-Assurance.md` | Unit tests, pytest, coverage |
| 18 | Error Handling and Debugging | `05-Error-Handling-and-Debugging.md` | Exceptions, debugging strategies |
| 19 | Working with APIs and Data | `06-Working-with-APIs-and-Data.md` | HTTP requests, JSON, data handling |
| 20 | Clean Code and Design Patterns | `07-Clean-Code-and-Design-Patterns.md` | Code organization, design patterns |
| 21 | Building Your First Real Project | `08-Building-Your-First-Real-Project.md` | Project structure, integration of all concepts |

---

## Part 5: Spec-Kit Methodology (Chapters 22-26)

Professional development workflow: specifications and planning

| # | Chapter Title | File Name | Key Topics |
|---|---------------|-----------|------------|
| 22 | Specification-Driven Development Fundamentals | `01-SDD-Fundamentals.md` | SDD concepts, why it matters |
| 23 | Writing Effective Specifications | `02-Writing-Effective-Specifications.md` | Spec structure, clarity, completeness |
| 24 | Planning and Tasking | `03-Planning-and-Tasking.md` | Project planning, task decomposition |
| 25 | Real-World Spec-Kit Workflows | `04-Real-World-Spec-Kit-Workflows.md` | Practical application, examples |
| 26 | Scaling Spec-Kit for Teams | `05-Scaling-Spec-Kit-for-Teams.md` | Collaboration, coordination, scaling |

---

## Part 6: Agentic AI Fundamentals (Chapters 27-29)

Building autonomous systems: agents and orchestration

| # | Chapter Title | File Name | Key Topics |
|---|---------------|-----------|------------|
| 27 | Introduction to Agentic AI | `01-Introduction-to-Agentic-AI.md` | What are agents, agent vs chatbot, architecture |
| 28 | Building Your First Agent | `02-Building-Your-First-Agent.md` | Simple agents, tool integration, execution |
| 29 | Agent Orchestration and Real-World Applications | `03-Agent-Orchestration-and-Real-World-Applications.md` | Complex agents, multi-agent systems, debugging |

---

## Part 7: MCP Fundamentals (Chapters 30-32)

Integration frameworks: Model Context Protocol

| # | Chapter Title | File Name | Key Topics |
|---|---------------|-----------|------------|
| 30 | Introduction to Model Context Protocol | `01-Introduction-to-Model-Context-Protocol.md` | MCP architecture, why standardization matters |
| 31 | Integrating MCP into Your Applications | `02-Integrating-MCP-into-Your-Applications.md` | Using existing MCP servers, configuration |
| 32 | Building Custom MCP Servers | `03-Building-Custom-MCP-Servers.md` | MCP server development, tools, best practices |

---

## Directory Structure Reference

Each chapter file should be placed in `book-source/docs/[NN-Part-Name]/[NN-Chapter-Name].md`

**Examples**:
- Chapter 1: `book-source/docs/01-Introducing-AI-Driven-Development/01-Welcome-to-AI-Driven-Development.md`
- Chapter 6: `book-source/docs/02-AI-Tool-Landscape/01-Claude-Code-Features-and-Workflows.md`
- Chapter 27: `book-source/docs/06-Agentic-AI/01-Introduction-to-Agentic-AI.md`

---

## Using This Index

**When creating a chapter**:
1. Find the chapter number and title in this index
2. Use the filename from this index
3. Place file in the correct part folder
4. Set `sidebar_position: [N]` in YAML frontmatter to the chapter number
5. Match the title exactly in frontmatter
6. Reference `.claude/output-styles/chapters.md` for formatting guidelines
