---
name: book-architecture
description: |
  Design comprehensive book structures with cohesive chapter flow, content organization,
  and balance between tutorial progression and reference material. Use this skill when
  authors are planning multi-chapter books, course curricula, or comprehensive technical
  guides requiring structural design decisions. This skill helps create learning
  trajectories that manage cognitive load, prevent circular dependencies, and serve
  both sequential learners and reference users. Activate when tasks involve organizing
  large amounts of content, deciding chapter sequences, managing prerequisites, or
  balancing different organizational patterns for technical documentation.
allowed-tools: ["Read", "Bash", "Write"]
version: "1.0.0"
---

# Book Architecture Skill

## Purpose

Enable technical authors to design **cohesive, well-structured books** that balance pedagogical progression with practical accessibility. This skill helps:
- Organize multi-chapter content into coherent learning trajectories
- Choose appropriate chapter flow patterns (linear, spiral, modular, hybrid, project-based)
- Manage chapter dependencies and prevent circular references
- Balance tutorial content (learning) with reference material (lookup)
- Design for multiple reading paths serving different audiences
- Validate structural integrity and cognitive load progression

## When to Activate

Use this skill when:
- Planning the structure of a comprehensive technical book (10+ chapters)
- Designing course curricula that need careful sequencing
- Creating learning resources that serve multiple audience levels
- Organizing complex content with interdependencies between topics
- Authors ask about "book structure", "chapter organization", "how to sequence content"
- Reviewing existing book structures for improvements
- Deciding between different organizational patterns
- Balancing beginner-friendly progression with experienced-user reference needs

## Process

### Step 1: Understand the Scope and Audience

When a request comes in to design or review book structure, first clarify:
- **What is the book about?** (Python programming, web development, data science, etc.)
- **Who is the primary audience?** (Absolute beginners, practitioners, mixed levels)
- **What is the book's main purpose?** (Tutorial/learning, reference, cookbook, project-based)
- **How long should it be?** (Rough page count or chapter count estimate)
- **Will readers read sequentially or selectively?** (Cover-to-cover vs. targeted reading)
- **What are the learning outcomes?** (What should readers be able to do after finishing?)

### Step 2: Choose Appropriate Flow Pattern

Based on the audience and purpose, review flow pattern options:
📖 [reference/chapter-flow-patterns.md](reference/chapter-flow-patterns.md)

This document covers:
- **Linear Curriculum**: Strict sequential reading (best for absolute beginners)
- **Spiral Curriculum**: Concepts revisited at increasing depth (intermediate learners)
- **Modular/Independent Chapters**: Read in any order (practitioners, reference use)
- **Hybrid Pattern**: Tutorial core + modular extensions (mixed audience)
- **Project-Based Flow**: Building a complete project chapter by chapter

**Decision Framework**:
1. Beginners with no prior knowledge → Linear or Hybrid (tutorial core)
2. Intermediate learners exploring a language/framework → Spiral or Hybrid
3. Practitioners needing reference → Modular or Hybrid (modular extensions)
4. Mixed audience → Hybrid pattern with multiple reading paths
5. Hands-on learners building portfolios → Project-based

### Step 3: Design Structural Organization

Review structural pattern options:
📖 [reference/structural-patterns.md](reference/structural-patterns.md)

This document covers:
- **Tutorial vs. Reference Balance**: How much narrative vs. lookup content
- **Chapter Internal Structure**: IBS (Intro-Body-Summary), MCA (Motivation-Concept-Application), Cookbook, EEE (Exploration-Experimentation-Explanation)
- **Part and Section Organization**: Skill-level parts, domain-based parts, theory-practice pairing
- **Appendices and Supporting Material**: Quick references, glossaries, solutions
- **Page-Level Design**: Sidebars, callouts, code examples, exercises

**Key Decisions**:
- Will the book be used once for learning or revisited for reference? (Affects structure)
- Should concepts be self-contained or build cumulatively? (Affects modularity)
- How will you visually distinguish tutorial from reference sections?

### Step 4: Organize Content with Chunking Strategies

Review content organization best practices:
📖 [reference/content-organization.md](reference/content-organization.md)

This document covers:
- **Chunking Strategies**: Micro (paragraphs), Mini (sections), Standard (chapters), Macro (parts)
- **Hierarchical Organization**: 3-level (Part > Chapter > Section) vs. 4-level with modules
- **Cross-Referencing Techniques**: Forward, backward, lateral references
- **Managing Complexity**: Progressive disclosure, concept maps, layered information
- **Indexing and Navigation**: Making content findable

**Key Principles**:
- Chunk information into 5-9 items per level (working memory limits)
- Use progressive disclosure (simple → complex)
- Provide cross-references but don't overdo it (distracting)
- Design comprehensive index with multiple entry points

### Step 5: Map Chapter Dependencies

Review dependency management strategies:
📖 [reference/chapter-dependencies.md](reference/chapter-dependencies.md)

This document covers:
- **Dependency Types**: Strong (must read prior), weak (helpful but not required), conceptual (related), optional (enrichment)
- **Dependency Patterns**: Linear chain, tree, diamond, DAG (directed acyclic graph)
- **Core vs. Optional Chapters**: Identifying essential vs. skippable content
- **Reading Path Design**: Linear, fast track, topic-specific, modular
- **Preventing Circular Dependencies**: Critical validation

**Key Actions**:
1. List all chapters and their prerequisites
2. Draw dependency graph to visualize structure
3. Identify cycles (circular dependencies) and break them
4. Mark core vs. optional chapters
5. Design reading paths for different audiences

### Step 6: Create Book Outline

Use the template as a starting point:
📄 [templates/book-outline-template.yml](templates/book-outline-template.yml)

Fill in:
- **Book metadata**: Title, audience, prerequisites, learning outcomes
- **Parts**: Major divisions with purposes and learning outcomes
- **Chapters**: For each chapter:
  - ID, number, title
  - Purpose (Core | Optional | Enhancement)
  - Dependencies (required, recommended, optional)
  - Synopsis and learning objectives
  - Key concepts
  - Estimated page count
- **Reading paths**: Define multiple paths (beginner, fast track, topic-specific)
- **Dependency graph**: Visual representation
- **Appendices**: Reference materials

**Best Practices**:
- Aim for 3-7 chapters per part (chunking)
- Keep chapter length consistent (20-30 pages is standard)
- Ensure every chapter has clear learning objectives
- Balance core vs. optional content (70/30 or 80/20)

### Step 7: Validate Structure

Once the outline is complete, invoke the structure validation script:

```bash
python .claude/skills/book-architecture/scripts/validate-structure.py book-outline.yml
```

**The script checks**:
- ✅ No circular chapter dependencies (critical)
- ✅ All dependency references are valid (no broken links)
- ✅ Prerequisite chains are complete
- ✅ No orphaned chapters (unreachable content)
- ✅ Required fields are present

**Interpret Results**:
- **Errors**: Must fix before structure is valid
  - Circular dependencies → Reorder chapters or split content
  - Invalid dependencies → Fix chapter IDs
  - Missing fields → Add required metadata
- **Warnings**: Should address for quality
  - Orphaned chapters → Add to reading paths or remove
  - Deep prerequisite chains → Consider simplifying

**If validation fails**:
1. Review error messages
2. Fix structural issues (reorder, split, merge chapters)
3. Re-validate until clean

### Step 8: Analyze Chapter Flow

Once structure is valid, analyze cognitive progression:

```bash
python .claude/skills/book-architecture/scripts/analyze-flow.py book-outline.yml
```

**The script analyzes**:
- **Concept Density**: How many concepts per chapter (identifies overloaded chapters)
- **Difficulty Progression**: Identifies sudden difficulty jumps
- **Bloom's Distribution**: Balance of cognitive levels (Remember through Create)
- **Learning Pace**: Pages per concept, exercises per chapter
- **Reordering Suggestions**: Structural improvements

**Interpret Results**:
- **High Concept Density** (6+ concepts): Consider splitting chapter or adding scaffolding
- **Difficulty Jumps** (score increase > 20): Add intermediate chapter or exercises
- **Bloom's Imbalance**:
  - Too much Remember/Understand (>50%): Add higher-order objectives
  - Too little Analyze/Evaluate/Create (<20%): Add analytical/creative tasks
- **Pace Issues**:
  - <3 pages per concept: Ensure adequate explanation
  - >10 pages per concept: Break down into sub-concepts

**Refine Based on Analysis**:
1. Split high-density chapters
2. Add scaffolding for difficulty jumps
3. Balance Bloom's levels across chapters
4. Adjust page estimates for realistic pacing

### Step 9: Design Individual Chapter Structures

For detailed chapter planning, use the chapter structure template:
📄 [templates/chapter-structure-template.yml](templates/chapter-structure-template.yml)

This template provides detailed structure for:
- Chapter metadata and learning objectives
- Section-by-section breakdown
- Pedagogical features (examples, exercises, callouts)
- Cross-references to other chapters
- Cognitive load management

**When to use**: After book outline is validated, when planning individual chapters in detail

### Step 10: Finalize and Document

After validation and refinement:
1. **Document design decisions**: Why did you choose this flow pattern? Why this structure?
2. **Create dependency visualization**: Include in book's front matter
3. **Write reading path guide**: Help readers navigate effectively
4. **Plan appendices**: What reference material will support learning?
5. **Consider supplementary materials**: Code repository, videos, instructor resources?

## Output Format

Present book architecture in structured YAML format following the book-outline-template.yml structure:

```yaml
book_title: "Title"
subtitle: "Subtitle"
target_audience: "Who this is for"
prerequisites: "What readers should know"

learning_outcomes:
  - "Outcome 1"
  - "Outcome 2"

flow_pattern: "Linear | Spiral | Modular | Hybrid | Project-Based"

parts:
  - id: "part-01"
    title: "Part Title"
    purpose: "Foundation | Application | Advanced | Reference"
    chapters:
      - id: "ch-01"
        title: "Chapter Title"
        purpose: "Core | Optional | Enhancement"
        dependencies:
          required: []
          recommended: []
        synopsis: "What this chapter covers"
        learning_objectives: [...]
        key_concepts: [...]

reading_paths:
  - name: "Linear Path"
    chapters: ["ch-01", "ch-02", ...]
  - name: "Fast Track"
    chapters: ["ch-01", "ch-03", ...]

dependency_graph: |
  Visual representation of chapter relationships
```

## Examples

### Example 1: Beginner Python Book (Linear Pattern)

**User Request**: "I'm writing a Python book for absolute beginners. How should I structure it?"

**Analysis**:
- Audience: Absolute beginners (no programming experience)
- Purpose: Learning/tutorial
- Flow pattern: Linear (strong scaffolding needed)

**Recommended Structure**:

```yaml
book_title: "Python from Zero to Hero"
target_audience: "Absolute beginners with no programming experience"
prerequisites: "None - starts from basics"
flow_pattern: "Linear"

parts:
  - id: "part-01"
    title: "Python Fundamentals"
    purpose: "Foundation"
    chapters:
      - id: "ch-01"
        title: "Getting Started with Python"
        purpose: "Core"
        dependencies: {required: []}

      - id: "ch-02"
        title: "Variables and Data Types"
        purpose: "Core"
        dependencies: {required: ["ch-01"]}

      - id: "ch-03"
        title: "Control Flow: Making Decisions"
        purpose: "Core"
        dependencies: {required: ["ch-02"]}

      - id: "ch-04"
        title: "Functions: Reusable Code"
        purpose: "Core"
        dependencies: {required: ["ch-03"]}

      - id: "ch-05"
        title: "Data Structures: Lists and Dictionaries"
        purpose: "Core"
        dependencies: {required: ["ch-04"]}

      - id: "ch-06"
        title: "Working with Files"
        purpose: "Core"
        dependencies: {required: ["ch-05"]}

  - id: "part-02"
    title: "Building Projects"
    purpose: "Application"
    chapters:
      - id: "ch-07"
        title: "Project 1: Command-Line Calculator"
        purpose: "Core"
        dependencies: {required: ["ch-04", "ch-05"]}

      - id: "ch-08"
        title: "Project 2: Contact Manager"
        purpose: "Core"
        dependencies: {required: ["ch-06", "ch-07"]}

reading_paths:
  - name: "Linear Path (Recommended for Beginners)"
    description: "Read all chapters in order"
    chapters: ["ch-01", "ch-02", "ch-03", "ch-04", "ch-05", "ch-06", "ch-07", "ch-08"]

dependency_graph: |
  Ch1 → Ch2 → Ch3 → Ch4 → Ch5 → Ch6
                           ↓       ↓
                          Ch7  →  Ch8
```

**Validation**: Run validate-structure.py → No cycles, clean dependencies
**Flow Analysis**: Run analyze-flow.py → Gradual difficulty progression, balanced Bloom's levels

---

### Example 2: Intermediate Python Book (Hybrid Pattern)

**User Request**: "I'm writing for Python developers who want to learn advanced features. Some have experience, some don't."

**Analysis**:
- Audience: Mixed (some intermediate, some advanced)
- Purpose: Learning + reference
- Flow pattern: Hybrid (tutorial core + modular advanced topics)

**Recommended Structure**:

```yaml
book_title: "Advanced Python Techniques"
target_audience: "Intermediate Python developers"
prerequisites: "Basic Python knowledge (variables, functions, OOP basics)"
flow_pattern: "Hybrid"

parts:
  - id: "part-01"
    title: "Core Concepts (Read in Order)"
    purpose: "Foundation"
    chapters:
      - id: "ch-01"
        title: "Python Refresher"
        purpose: "Core"
        dependencies: {required: []}

      - id: "ch-02"
        title: "Advanced Functions and Closures"
        purpose: "Core"
        dependencies: {required: ["ch-01"]}

      - id: "ch-03"
        title: "Decorators and Metaprogramming"
        purpose: "Core"
        dependencies: {required: ["ch-02"]}

  - id: "part-02"
    title: "Advanced Topics (Read as Needed)"
    purpose: "Advanced"
    chapters:
      - id: "ch-04"
        title: "Concurrency with asyncio"
        purpose: "Optional"
        dependencies: {required: ["ch-01"], recommended: ["ch-02"]}

      - id: "ch-05"
        title: "Performance Optimization"
        purpose: "Optional"
        dependencies: {required: ["ch-01"]}

      - id: "ch-06"
        title: "Type Hints and Static Analysis"
        purpose: "Optional"
        dependencies: {required: ["ch-01"]}

      - id: "ch-07"
        title: "Design Patterns in Python"
        purpose: "Optional"
        dependencies: {required: ["ch-03"]}

reading_paths:
  - name: "Complete Path"
    description: "Read all chapters for comprehensive coverage"
    chapters: ["ch-01", "ch-02", "ch-03", "ch-04", "ch-05", "ch-06", "ch-07"]

  - name: "Fast Track (Experienced Developers)"
    description: "Skip refresher, focus on advanced topics"
    chapters: ["ch-02", "ch-03", "ch-04", "ch-05", "ch-06", "ch-07"]
    skip_chapters: ["ch-01"]

  - name: "Web Development Focus"
    chapters: ["ch-01", "ch-02", "ch-03", "ch-04"]

  - name: "Performance Focus"
    chapters: ["ch-01", "ch-02", "ch-05"]

dependency_graph: |
       Ch1 (Foundation)
        ↓
       Ch2
        ↓
       Ch3
      ↙ ↓ ↘
    Ch4 Ch7  (Part II: Independent modules)
            ↖
    Ch5   Ch6
```

**Validation**: validate-structure.py → Tree structure, no cycles
**Flow Analysis**: analyze-flow.py → Part I has gradual progression, Part II has balanced density

---

### Example 3: Cookbook (Modular Pattern)

**User Request**: "I want to write a Python cookbook with practical recipes. How should it be organized?"

**Analysis**:
- Audience: Practitioners needing quick solutions
- Purpose: Reference/cookbook
- Flow pattern: Modular (chapters can be read independently)

**Recommended Structure**:

```yaml
book_title: "Python Cookbook: Practical Solutions"
target_audience: "Python developers needing practical solutions"
prerequisites: "Intermediate Python knowledge"
flow_pattern: "Modular"

parts:
  - id: "part-01"
    title: "Foundation (Read First)"
    purpose: "Foundation"
    chapters:
      - id: "ch-01"
        title: "How to Use This Cookbook"
        purpose: "Core"
        dependencies: {required: []}

  - id: "part-02"
    title: "Data Manipulation Recipes"
    purpose: "Reference"
    chapters:
      - id: "ch-02"
        title: "Working with Lists and Tuples"
        purpose: "Core"
        dependencies: {required: ["ch-01"]}

      - id: "ch-03"
        title: "Dictionary and Set Techniques"
        purpose: "Core"
        dependencies: {required: ["ch-01"]}

      - id: "ch-04"
        title: "String Processing and Regex"
        purpose: "Core"
        dependencies: {required: ["ch-01"]}

  - id: "part-03"
    title: "File and Network I/O"
    purpose: "Reference"
    chapters:
      - id: "ch-05"
        title: "File Operations"
        purpose: "Core"
        dependencies: {required: ["ch-01"]}

      - id: "ch-06"
        title: "JSON, CSV, and XML"
        purpose: "Core"
        dependencies: {required: ["ch-01"]}

      - id: "ch-07"
        title: "HTTP Requests and APIs"
        purpose: "Core"
        dependencies: {required: ["ch-01"]}

reading_paths:
  - name: "Modular (Recommended)"
    description: "Read Ch1, then jump to any chapter based on your needs"
    chapters: ["ch-01", "then any chapter"]

dependency_graph: |
         Ch1
    ↙ ↓ ↓ ↓ ↓ ↓ ↘
  Ch2 Ch3 Ch4 Ch5 Ch6 Ch7 (All independent after Ch1)
```

**Validation**: validate-structure.py → Flat structure, no complex dependencies
**Flow Analysis**: analyze-flow.py → Balanced concept density across chapters

---

## Common Patterns and Anti-Patterns

### Pattern 1: Foundation + Modules (Hybrid)

**Use**: Serve both beginners and experienced readers

```
Part I: Foundation (Linear, 3-6 chapters)
Part II: Modules (Independent, 6-12 chapters)
```

**Advantages**: Clear graduation point, flexible after foundation

---

### Pattern 2: Spiral Learning

**Use**: Complex topics needing multiple passes

```
Ch1: Intro to Classes (basic)
Ch5: Advanced Classes (deeper)
Ch10: OOP Design Patterns (complete)
```

**Advantages**: Reduces initial cognitive load, allows practical use before mastery

---

### Anti-Pattern 1: Circular Dependencies ❌

**Problem**: Ch5 requires Ch8, but Ch8 requires Ch5

**Solution**: Reorder or split chapters to break cycle

---

### Anti-Pattern 2: Overloaded First Chapter ❌

**Problem**: Chapter 1 introduces 10+ concepts

**Solution**: Split into 2-3 chapters, each with 3-5 concepts

---

### Anti-Pattern 3: Optional Content Before Core ❌

**Problem**: Optional chapters appear early, core content appears late

**Solution**: Move optional chapters to end or clearly mark reading paths

---

## Troubleshooting

### Structure Validation Fails with Circular Dependencies

**Problem**: validate-structure.py reports cycles

**Solution**:
1. Identify the cycle (e.g., Ch3 → Ch5 → Ch7 → Ch3)
2. Review chapter content to find unnecessary dependencies
3. Options to break cycle:
   - Reorder chapters
   - Split concepts into separate chapters
   - Make one dependency "recommended" instead of "required"
   - Add recap in one chapter so it doesn't require prior chapter

---

### Flow Analysis Shows High Difficulty Jumps

**Problem**: analyze-flow.py reports score jumps > 20 points

**Solution**:
1. Identify the gap (e.g., Ch4 difficulty 25 → Ch5 difficulty 50)
2. Options:
   - Add intermediate chapter between Ch4 and Ch5
   - Move advanced content from Ch5 to later chapter
   - Add more exercises in Ch4 to build skills
   - Add "bridge" section at start of Ch5 with recap

---

### Too Many Concepts Per Chapter

**Problem**: Some chapters have 8-10 key concepts

**Solution**:
- Split chapter into 2 chapters
- Move some concepts to appendix (if not essential)
- Reduce scope of chapter
- Combine related concepts into one larger concept

---

### Book Feels Too Linear (Can't Skip Chapters)

**Problem**: Every chapter depends on every prior chapter

**Solution**:
- Identify which dependencies are truly required vs. helpful
- Change some "required" to "recommended"
- Create independent modules after foundation
- Provide "fast track" reading path that skips review content

---

## Integration with Other Skills

This skill works well with:

**→ learning-objectives skill**: Once book structure is designed, use learning-objectives to define chapter-level objectives

**→ concept-scaffolding skill**: For chapters with complex topics, use concept-scaffolding to break them down into progressive steps

**→ assessment-builder skill**: Design end-of-chapter assessments aligned with learning objectives

**→ technical-clarity skill**: Review chapter synopses and descriptions for clarity

---

## Tips for Success

1. **Start with learning outcomes**: Know what readers should achieve before designing structure
2. **Design for multiple reading paths**: Not everyone reads cover-to-cover
3. **Validate early and often**: Run validate-structure.py after major changes
4. **Use visual dependency maps**: Help readers (and you) see the structure
5. **Balance core and optional**: 70-80% core, 20-30% optional/advanced
6. **Chunk appropriately**: 3-7 chapters per part, 3-5 concepts per chapter
7. **Test with beta readers**: Different audiences navigate books differently
8. **Provide clear prerequisites**: Help readers self-assess readiness
9. **Plan appendices**: Quick references make books more useful long-term
10. **Document your decisions**: Why did you choose this structure? Future-you will thank you

---

**Ready to design your book structure?** Provide:
- Book topic and scope
- Target audience (beginner/intermediate/advanced)
- Book purpose (tutorial/reference/cookbook/project-based)
- Rough chapter count or page estimate
- Any specific organizational challenges

Or paste an existing structure and I'll analyze and suggest improvements!
