# Skill Activation Reference

This document explains how CoLearning Python skills are activated semantically based on educator intent, provides detailed examples of activation patterns, and contrasts semantic understanding with keyword-based approaches.

## Table of Contents

1. [How Semantic Activation Works](#how-semantic-activation-works)
2. [Activation Patterns for Each Skill](#activation-patterns-for-each-skill)
3. [Multi-Skill Activation](#multi-skill-activation)
4. [Semantic vs. Keyword Matching](#semantic-vs-keyword-matching)
5. [Activation Checklist](#activation-checklist)
6. [Troubleshooting Activation](#troubleshooting-activation)

---

## How Semantic Activation Works

CoLearning Python skills use **semantic activation** - Claude understands the educator's intent from natural language rather than requiring explicit skill invocation.

### Activation Process

1. **Intent Recognition**: Claude analyzes the educator's request to understand:
   - What teaching task is being attempted (planning, creating, reviewing, assessing)
   - What pedagogical concern exists (clarity, scaffolding, measurability, engagement)
   - Who the target audience is (beginners, intermediate, advanced)
   - What Python concept is involved (functions, classes, loops, etc.)

2. **Skill Matching**: Claude matches the intent to skill descriptions in SKILL.md frontmatter using:
   - Purpose alignment
   - Context similarity
   - Task requirements
   - Pedagogical approach

3. **Skill Activation**: Once matched, Claude:
   - Loads the skill's process and guidance
   - Follows step-by-step instructions
   - References supporting materials as needed
   - Generates outputs according to skill specifications

4. **Multi-Skill Coordination**: For complex requests, Claude may activate multiple skills sequentially or in parallel.

### Why Semantic Activation?

**Benefits over keyword matching**:
- Natural language requests (no memorizing commands)
- Context-aware (understands implicit needs)
- Flexible phrasing (many ways to express the same intent)
- Intelligent defaults (chooses appropriate skill configuration)

---

## Activation Patterns for Each Skill

### 1. learning-objectives

**Activation Intent**: Define measurable outcomes for what students will achieve

**Semantic Triggers**:
- Expressing need for **measurable outcomes**
- Questions about **what students should achieve**
- References to **learning goals**, **objectives**, **outcomes**
- Concerns about **specificity** or **testability**
- Bloom's taxonomy mentions
- Assessment alignment needs

**Example Activations**:

| User Request | Why It Activates | Skill Focus |
|--------------|------------------|-------------|
| "Create learning objectives for teaching Python decorators" | Direct objective creation request | Generate objectives |
| "What should students be able to do after learning loops?" | Implicit outcome definition | Define achievements |
| "Are these objectives specific enough?" | Measurability concern | Validate objectives |
| "I need outcomes for my functions lesson" | Outcome planning | Create outcomes |
| "How do I make my objectives testable?" | Assessment alignment | Improve measurability |
| "Define what learners will achieve with list comprehensions" | Achievement focus | Generate objectives |

**Non-Activating Requests**:
- "Teach me about decorators" (direct teaching, not objective creation)
- "Show me loop examples" (example generation, not objectives)
- "My students don't understand functions" (troubleshooting, not planning)

---

### 2. concept-scaffolding

**Activation Intent**: Break complex concepts into progressive, manageable learning steps

**Semantic Triggers**:
- Expressing **complexity** or **difficulty**
- Need for **step-by-step** or **progressive** approach
- Mentions of **cognitive load**, **overwhelm**, **breaking down**
- Advanced topics: decorators, async/await, OOP, metaclasses, generators
- Concerns about **prerequisite knowledge**
- Need for **worked examples**

**Example Activations**:

| User Request | Why It Activates | Skill Focus |
|--------------|------------------|-------------|
| "How do I teach Python decorators incrementally?" | Progressive teaching need | Create scaffolding plan |
| "Break down async/await for beginners" | Complexity + simplification | Multi-step progression |
| "My students are overwhelmed by OOP" | Cognitive load concern | Reduce complexity |
| "What are the prerequisites for teaching generators?" | Prerequisite identification | Dependency analysis |
| "Scaffold list comprehensions into small steps" | Explicit scaffolding request | Step-by-step breakdown |
| "Introduce classes gradually" | Incremental teaching | Progressive introduction |

**Non-Activating Requests**:
- "Explain decorators" (direct explanation, not scaffolding)
- "Give me an OOP example" (example creation, not scaffolding)
- "Test students on async/await" (assessment, not scaffolding)

---

### 3. code-example-generator

**Activation Intent**: Create runnable, pedagogically sound code demonstrations

**Semantic Triggers**:
- Need for **code examples**, **demonstrations**, **samples**
- Requests for **runnable**, **working**, **executable** code
- Mentions of **show me**, **demonstrate**, **illustrate**
- Progressive sequences: **simple to complex**, **beginner to advanced**
- Validation needs: **check syntax**, **test this code**
- Best practices mentions

**Example Activations**:

| User Request | Why It Activates | Skill Focus |
|--------------|------------------|-------------|
| "Generate a beginner example for list comprehensions" | Example creation + level | Create example |
| "Show me a realistic example of exception handling" | Demonstration need | Generate code |
| "Create code examples demonstrating dictionary methods" | Code demonstration | Multiple examples |
| "Is this code example appropriate for beginners?" | Example validation | Review code |
| "I need progressive examples for functions" | Sequence creation | Simple to complex |
| "Validate this code example for teaching" | Example quality check | Syntax/pedagogy check |

**Non-Activating Requests**:
- "How do list comprehensions work?" (explanation, not code)
- "Create exercises for loops" (practice activities, not examples)
- "Test students on dictionaries" (assessment, not examples)

---

### 4. exercise-designer

**Activation Intent**: Create varied practice activities with evidence-based strategies

**Semantic Triggers**:
- Need for **exercises**, **practice**, **homework**, **assignments**
- Requests for **varied types** (not just "write code")
- Mentions of **spaced repetition**, **interleaving**, **retrieval practice**
- Concerns about **difficulty progression**
- Need for **test cases**, **rubrics**, **hints**
- Problem set creation

**Example Activations**:

| User Request | Why It Activates | Skill Focus |
|--------------|------------------|-------------|
| "Create 5 exercises for practicing list methods" | Exercise creation | Generate varied exercises |
| "Design exercises for loops that review conditionals" | Spaced repetition need | Interleaving concepts |
| "Generate a problem set with varied difficulty" | Progression concern | Easy to hard sequence |
| "I need debugging exercises for functions" | Specific exercise type | Debug-this exercises |
| "Create homework that applies evidence-based strategies" | Strategy application | Evidence-based design |
| "Add test cases to these exercises" | Test case generation | Validation creation |

**Non-Activating Requests**:
- "Show me loop syntax" (explanation, not practice)
- "Create a quiz for functions" (formal assessment, not exercises)
- "How do students practice lists?" (advice, not creation)

---

### 5. assessment-builder

**Activation Intent**: Create formal assessments with balanced question types and cognitive distribution

**Semantic Triggers**:
- Need for **quiz**, **test**, **exam**, **assessment**
- Mentions of **question types**, **MCQ**, **multiple choice**
- Concerns about **cognitive distribution**, **Bloom's levels**
- Need for **distractors**, **answer keys**, **rubrics**
- Assessment balance: **not just recall**, **application**, **higher-order thinking**
- Formal evaluation context

**Example Activations**:

| User Request | Why It Activates | Skill Focus |
|--------------|------------------|-------------|
| "Create a balanced assessment for Python functions" | Assessment creation | Balanced question design |
| "Design a quiz testing application skills, not just recall" | Cognitive balance concern | 60%+ non-recall |
| "Add meaningful distractors to these MCQs" | Distractor design | Misconception-based options |
| "I need a final exam for my OOP unit" | Formal assessment | Comprehensive test |
| "Create rubrics for coding questions" | Rubric creation | Grading criteria |
| "Validate this assessment for balance" | Assessment review | Cognitive distribution check |

**Non-Activating Requests**:
- "Create practice exercises" (exercises, not formal assessment)
- "Give me examples of loops" (examples, not assessment)
- "How do I grade projects?" (grading advice, not assessment creation)

---

### 6. technical-clarity

**Activation Intent**: Review content for readability, jargon, gatekeeping language, and completeness

**Semantic Triggers**:
- Need for **clarity review**, **readability check**
- Concerns about **jargon**, **technical terms**, **accessibility**
- Mentions of **gatekeeping language** ("obviously", "simply", etc.)
- Questions about **target audience appropriateness**
- Need for **readability metrics**, **grade level**
- Content review context (tutorials, documentation, chapters)

**Example Activations**:

| User Request | Why It Activates | Skill Focus |
|--------------|------------------|-------------|
| "Review this Python tutorial for clarity" | Clarity review request | Comprehensive analysis |
| "Is this explanation appropriate for beginners?" | Audience alignment | Readability + jargon |
| "Check this content for gatekeeping language" | Specific concern | Gatekeeping audit |
| "Is my tutorial too technical?" | Complexity concern | Grade level check |
| "Identify undefined jargon in this chapter" | Jargon analysis | Term identification |
| "Review this documentation for accessibility" | Accessibility focus | Complete clarity report |

**Non-Activating Requests**:
- "Teach me about functions" (teaching, not review)
- "Create clear examples" (example creation, not review)
- "Design a tutorial" (creation, not review)

---

### 7. book-architecture

**Activation Intent**: Structure book/course content with logical flow and dependency management

**Semantic Triggers**:
- Need for **book structure**, **course outline**, **curriculum architecture**
- Mentions of **chapter order**, **dependencies**, **prerequisites**
- Concerns about **concept flow**, **progression**, **sequence**
- Book/course planning context
- Structural validation needs

**Example Activations**:

| User Request | Why It Activates | Skill Focus |
|--------------|------------------|-------------|
| "Plan the structure for my Python book" | Book architecture | Complete structure design |
| "Validate these chapter dependencies" | Dependency analysis | Prerequisite chain check |
| "What order should I teach these concepts?" | Sequencing concern | Logical flow |
| "Design a course outline for web development" | Curriculum planning | Module organization |
| "Check for circular dependencies in my chapters" | Structural validation | Dependency analysis |
| "How do I organize a Python curriculum?" | Organizational planning | Structure patterns |

**Non-Activating Requests**:
- "Write a chapter on functions" (content creation, not structure)
- "Review this tutorial" (content review, not structure)
- "Create examples for my book" (example creation, not architecture)

---

### 8. ai-augmented-teaching

**Activation Intent**: Design learning experiences integrating AI tools while maintaining learning integrity

**Semantic Triggers**:
- Mentions of **AI**, **ChatGPT**, **GitHub Copilot**, **Claude**, **LLMs**
- Need for **AI integration**, **AI-assisted learning**
- Concerns about **AI ethics**, **academic integrity**, **over-reliance**
- References to **prompt engineering** teaching
- Balance between **AI assistance** and **independent learning**
- AI tool literacy needs

**Example Activations**:

| User Request | Why It Activates | Skill Focus |
|--------------|------------------|-------------|
| "How do I integrate AI tools into my Python course?" | AI integration planning | AI-augmented curriculum |
| "Design a lesson balancing AI assistance with independent learning" | Balance concern | 40/40/20 framework |
| "Create a prompt engineering curriculum" | Prompt teaching | Prompt pedagogy |
| "Establish ethical guidelines for AI use in class" | Ethics concern | Ethical framework |
| "My students over-rely on ChatGPT" | Over-reliance problem | Balance adjustment |
| "Assess AI integration in this lesson plan" | Integration validation | Balance assessment |

**Non-Activating Requests**:
- "Teach me Python" (direct teaching, not AI integration)
- "Create exercises" (exercise design, not AI integration)
- "Review this code" (code review, not AI pedagogy)

---

## Multi-Skill Activation

Complex requests often require multiple skills working together. Claude recognizes compound intents and activates skills sequentially or in parallel.

### Common Multi-Skill Patterns

#### Pattern 1: Curriculum Design

**Request**: "I need to teach Python decorators to intermediate learners. Create a complete lesson."

**Skills Activated**:
1. `learning-objectives` - Define measurable outcomes
2. `concept-scaffolding` - Break down decorators into steps
3. `code-example-generator` - Create demonstration examples
4. `exercise-designer` - Design practice activities
5. `assessment-builder` - Create quiz to measure achievement

**Coordination**: Sequential (objectives → scaffolding → examples → exercises → assessment)

---

#### Pattern 2: Content Review

**Request**: "Review my functions tutorial for beginners. Check clarity, examples, and exercises."

**Skills Activated**:
1. `technical-clarity` - Review readability and jargon
2. `code-example-generator` - Validate example quality
3. `exercise-designer` - Assess exercise variety and difficulty

**Coordination**: Parallel (all review independently, then synthesize)

---

#### Pattern 3: AI-Integrated Curriculum

**Request**: "Design a course on web development that uses GitHub Copilot appropriately."

**Skills Activated**:
1. `book-architecture` - Structure course modules
2. `ai-augmented-teaching` - Design AI integration strategy
3. `learning-objectives` - Define what students achieve independently vs. with AI
4. `assessment-builder` - Create AI-free assessments to verify learning

**Coordination**: Layered (architecture → AI strategy → objectives → assessment)

---

## Semantic vs. Keyword Matching

### Semantic Understanding (CoLearning Python Approach)

Claude understands **intent and context**, not just keywords.

**Example: "My students struggle with OOP concepts"**

**Semantic Interpretation**:
- **Intent**: Address learning difficulty
- **Context**: Object-oriented programming
- **Pedagogical Need**: Break down complexity
- **Skill Match**: `concept-scaffolding` (reduce cognitive load)

**Keyword Interpretation** (simpler systems might miss this):
- Contains "OOP" but no explicit "scaffold" keyword
- Might miss that "struggle" implies need for simplification
- Wouldn't recognize pedagogical intent

---

**Example: "Create a quiz that doesn't just test memorization"**

**Semantic Interpretation**:
- **Intent**: Formal assessment
- **Context**: Cognitive balance concern
- **Pedagogical Need**: Higher-order thinking (Apply, Analyze, Evaluate)
- **Skill Match**: `assessment-builder` (60%+ non-recall focus)

**Keyword Interpretation**:
- Contains "quiz" (assessment keyword)
- But the critical insight is the **anti-pattern** ("doesn't just test memorization")
- Semantic understanding recognizes this as a cognitive distribution concern

---

### Why Semantic Activation Is Superior

| Aspect | Keyword Matching | Semantic Understanding |
|--------|------------------|------------------------|
| **Phrasing** | Rigid (must use specific words) | Flexible (many ways to express intent) |
| **Context** | Ignores context | Understands situation |
| **Implicit Needs** | Misses unstated needs | Infers pedagogical requirements |
| **Anti-Patterns** | Can't recognize negation ("not just X") | Understands contrasts |
| **Domain Knowledge** | Generic matching | Pedagogically informed |
| **False Positives** | Common (keyword present but wrong intent) | Rare (intent-based) |

---

## Activation Checklist

Use this checklist to understand why a skill activates (or doesn't):

### For Any Request:

- [ ] **Teaching Task**: What am I trying to accomplish? (Plan, Create, Review, Assess)
- [ ] **Pedagogical Concern**: What teaching challenge exists? (Complexity, Clarity, Measurability, Engagement)
- [ ] **Target Audience**: Who are the learners? (Beginner, Intermediate, Advanced)
- [ ] **Content Type**: What artifact am I working with? (Objectives, Examples, Exercises, Assessment, Tutorial, Course)
- [ ] **Python Concept**: What programming topic is involved?

### Skill-Specific Indicators:

**learning-objectives**:
- [ ] Mentions outcomes, objectives, or achievements
- [ ] Concerned about measurability or testability
- [ ] Planning stage (what should students achieve?)

**concept-scaffolding**:
- [ ] Mentions complexity, difficulty, or cognitive load
- [ ] Advanced topic (decorators, async, OOP, metaclasses)
- [ ] Need for step-by-step or progressive approach

**code-example-generator**:
- [ ] Requests code demonstrations or samples
- [ ] Needs runnable, working examples
- [ ] Validation of existing code

**exercise-designer**:
- [ ] Requests practice activities or homework
- [ ] Needs varied exercise types
- [ ] Mentions evidence-based strategies

**assessment-builder**:
- [ ] Requests formal evaluation (quiz, test, exam)
- [ ] Concerned about question variety or cognitive balance
- [ ] Needs rubrics or answer keys

**technical-clarity**:
- [ ] Requests content review
- [ ] Concerned about jargon, readability, or gatekeeping
- [ ] Checking audience appropriateness

**book-architecture**:
- [ ] Planning book/course structure
- [ ] Concerned about chapter order or dependencies
- [ ] Organizational/structural focus

**ai-augmented-teaching**:
- [ ] Mentions AI tools (ChatGPT, Copilot, Claude)
- [ ] Concerned about AI integration balance
- [ ] Need for prompt engineering pedagogy or AI ethics

---

## Troubleshooting Activation

### Issue: Wrong Skill Activated

**Problem**: Claude activates a skill that doesn't match your intent.

**Diagnosis**:
- Your request may be ambiguous
- Multiple valid interpretations exist
- Keyword present but intent differs

**Solution**:
1. **Be more specific**: "I need learning objectives" vs. "I need help with functions"
2. **State the artifact type**: "Create exercises" vs. "Create a quiz"
3. **Clarify the task**: "Review for clarity" vs. "Review for correctness"
4. **Provide context**: "For beginners" vs. "For advanced students"

**Example**:
- Ambiguous: "Help me with Python classes"
- Specific: "Create a scaffolded lesson introducing Python classes to beginners"

---

### Issue: No Skill Activated

**Problem**: Claude doesn't activate any skill, provides generic response.

**Diagnosis**:
- Request is too vague
- No pedagogical intent (just asking for information)
- Outside skill domains

**Solution**:
1. **Add pedagogical intent**: "Explain classes" → "Create objectives for teaching classes"
2. **Specify the task**: "I'm teaching loops" → "Design exercises for practicing loops"
3. **Request an artifact**: "Functions are hard" → "Scaffold functions for beginners"

**Example**:
- Vague: "Tell me about decorators"
- Skill-Activating: "Break down decorators into teachable steps for intermediate learners"

---

### Issue: Partial Activation

**Problem**: Skill activates but doesn't follow the full process.

**Diagnosis**:
- Request is too narrow (only part of skill needed)
- Explicit constraint limits scope

**Solution**:
- This is often correct behavior (skill provides just what you need)
- If you want the full process, request it: "Follow the complete scaffolding process"

---

### Issue: Multi-Skill Coordination Needed

**Problem**: One skill isn't sufficient.

**Diagnosis**:
- Complex request requires multiple skills
- Compound intent (e.g., create AND review)

**Solution**:
- Claude should coordinate automatically
- If not, break request into steps: "First create objectives, then scaffold the concept"

---

## Examples of Effective Activation

### Example 1: Single Skill, Clear Intent

**Request**: "Create learning objectives for teaching list comprehensions to beginners. Make them measurable."

**Analysis**:
- **Task**: Create
- **Artifact**: Learning objectives
- **Concern**: Measurability
- **Audience**: Beginners
- **Concept**: List comprehensions

**Activated Skill**: `learning-objectives`

**Why It Works**: Clear intent, specific artifact, explicit concern.

---

### Example 2: Multi-Skill, Compound Intent

**Request**: "I need to teach Python decorators. Create a complete lesson with objectives, scaffolded steps, examples, and exercises."

**Analysis**:
- **Task**: Create (comprehensive lesson)
- **Artifacts**: Multiple (objectives, scaffolding, examples, exercises)
- **Audience**: (Implied intermediate/advanced based on topic)
- **Concept**: Decorators

**Activated Skills**:
1. `learning-objectives`
2. `concept-scaffolding`
3. `code-example-generator`
4. `exercise-designer`

**Why It Works**: Explicit listing of needed artifacts, clear sequence.

---

### Example 3: Review Intent, Specific Concern

**Request**: "Review this tutorial for gatekeeping language and jargon appropriate for beginners."

**Analysis**:
- **Task**: Review
- **Artifact**: Tutorial
- **Concerns**: Gatekeeping, jargon, audience appropriateness
- **Audience**: Beginners

**Activated Skill**: `technical-clarity`

**Why It Works**: Clear review intent, specific concerns, audience stated.

---

### Example 4: Problem-Focused, Implicit Skill

**Request**: "My students are overwhelmed when I introduce OOP. How do I break it down?"

**Analysis**:
- **Problem**: Cognitive overload
- **Need**: Simplification, step-by-step approach
- **Concept**: OOP (inherently complex)
- **Implicit Task**: Scaffold concept

**Activated Skill**: `concept-scaffolding`

**Why It Works**: Problem statement implies need for scaffolding, even without explicit request.

---

### Example 5: Anti-Pattern Recognition

**Request**: "Create a quiz that tests understanding, not just recall. I want students to apply what they learned."

**Analysis**:
- **Task**: Create
- **Artifact**: Quiz (formal assessment)
- **Anti-Pattern**: "not just recall" (avoid Remember level)
- **Cognitive Focus**: Apply level (Bloom's)

**Activated Skill**: `assessment-builder`

**Focus**: Cognitive balance (60%+ non-recall, emphasis on Apply)

**Why It Works**: Semantic understanding recognizes anti-pattern and maps to cognitive distribution concern.

---

## Summary

**Key Principles for Effective Activation**:

1. **Be Clear**: State your teaching task explicitly (create, review, assess, plan)
2. **Specify Artifacts**: Name what you want (objectives, examples, exercises, quiz, tutorial)
3. **Provide Context**: Mention audience level, Python concept, pedagogical concerns
4. **Express Intent**: Describe your goal, not just the topic
5. **Use Natural Language**: Don't try to guess "keywords" - just describe your need

**What Makes Semantic Activation Powerful**:
- Understands teaching context and pedagogical intent
- Recognizes implicit needs (e.g., "students struggle" → simplification needed)
- Handles flexible phrasing (many ways to express the same need)
- Coordinates multiple skills for complex requests
- Applies domain knowledge (teaching and learning science)

**When in Doubt**:
- Describe what you're trying to accomplish as an educator
- State what artifact you need (if you know)
- Mention any specific concerns (clarity, difficulty, balance, etc.)
- Specify your audience (beginners, intermediate, advanced)

Claude will understand your intent and activate the appropriate skill(s) to help you achieve your teaching goals.
