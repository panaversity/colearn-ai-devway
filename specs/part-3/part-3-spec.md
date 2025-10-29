# Part 3 Specification: Prompt & Context Engineering

**Feature**: Book Structure - Part 3 Detailed Specification
**Created**: 2025-10-29
**Status**: Ready for chapter-planner subagent
**Input**: Book structure + Part 3 actual implementation in book-source/docs/03-Prompt-and-Context-Engineering/
**Output**: For chapter-planner: `specs/part-3/chapter-10-plan.md` through `specs/part-3/chapter-13-plan.md`

---

## Part 3 Overview

### Title
**"Prompt & Context Engineering: Mastering AI Communication"**

### Purpose

Part 3 teaches readers how to communicate effectively with AI systems through structured prompting frameworks and context management. Readers transition from ad-hoc prompting to systematic, framework-driven approaches that produce consistent, high-quality results.

### Target Audience

- Developers who have completed Parts 1-2
- Comfortable with AI tools but want to improve prompt effectiveness
- Ready to learn structured frameworks for AI communication
- Seeking to debug and refine AI-generated outputs systematically

### Part 3 Philosophy

- **Cognitive Load**: MODERATE (building on Part 1-2 foundations)
- **Scaffolding**: HEAVY (2-3 review cycles expected, framework-driven)
- **Review Cycles**: 2-3 (structured frameworks require practice)
- **Concept Density**: 4-5 key concepts per chapter (moderate-high)

### Part 3 Learning Outcomes

By the end of Part 3, readers will be able to:

1. **Foundation**: Write effective, specific prompts using structured frameworks
2. **Six-Part Framework**: Apply the six-part prompting framework to craft powerful prompts
3. **Multimodal**: Work with text, images, and video inputs effectively
4. **Advanced Techniques**: Use few-shot learning, chain-of-thought, and prompt chaining
5. **Context Management**: Manage context windows and token budgets intelligently
6. **Debugging**: Debug AI-generated code systematically and refine prompts based on output quality

---

## Chapter Breakdown

### Chapter 10: The Architect Toolkit: Prompting Foundations
**Subtitle**: "Structure, Clarity, and Good vs. Bad Prompts"

#### Purpose
Establish foundational prompting skills. Answer: "What makes a good prompt, and why do some prompts fail?"

#### Learning Outcomes
By the end of this chapter, readers will:
- Understand the anatomy of effective prompts (structure, clarity, specificity)
- Recognize common prompt failures and how to avoid them
- Write clear, specific prompts that produce consistent results
- Understand context management basics (what is context? why does it matter?)
- Know the difference between imperative and declarative prompts
- Have practiced writing prompts using good/bad examples

#### Key Topics to Cover
1. **Anatomy of a Good Prompt**
   - Clear intent: What do you want the AI to do?
   - Specificity: Concrete requirements, not vague requests
   - Context: What background information does the AI need?
   - Constraints: What should the AI NOT do?
   - Output format: What should the result look like?

2. **Common Prompt Failures**
   - Too vague: "Write some code" → AI doesn't know what to build
   - Missing context: "Fix this bug" → AI doesn't know what file/function
   - Conflicting instructions: "Be brief but comprehensive" → AI is confused
   - Implicit assumptions: "Use the standard approach" → AI doesn't know which standard
   - No success criteria: "Make it better" → AI doesn't know what "better" means

3. **Good vs. Bad Examples**
   - Side-by-side comparisons: Bad prompt → Why it fails → Good prompt → Why it works
   - Real-world scenarios: Email validation, API integration, data processing
   - Progressive refinement: Show how to turn a bad prompt into a good one

4. **Context Management Basics**
   - What is context? (conversation history, files, code snippets)
   - Why does context matter? (AI needs it to understand your request)
   - How much context is enough? (too little → confusion; too much → overwhelm)
   - Token budgets: What they are and why they limit context

5. **Imperative vs. Declarative Prompts**
   - Imperative: "Do X, then do Y, then do Z" (step-by-step instructions)
   - Declarative: "I need a system that does X" (describe the outcome)
   - When to use each approach
   - Hybrid: Combining both for complex tasks

#### Prerequisites
- Part 1 completion (AI-driven development mindset)
- Part 2 completion (familiar with at least one AI tool)
- Basic understanding of software requirements

#### Success Criteria
- Readers can identify what makes a prompt effective
- Readers can explain why common prompts fail
- Readers have written 3+ prompts using good/bad examples as guides
- Readers understand context management basics
- Readers can distinguish imperative from declarative prompts

#### Pedagogical Approach
- **Show-then-explain**: Start with examples, then explain principles
- **Good/bad comparisons**: Visual side-by-side contrasts
- **Progressive refinement**: Show iteration from bad → mediocre → good
- **Hands-on exercises**: Write prompts, see results, refine based on output
- **Real scenarios**: Use realistic tasks (not toy examples)

#### Approximate Content
- 3,500-4,500 words
- 10-12 good/bad prompt comparisons (side-by-side)
- 3-4 context management examples
- 2 diagrams (prompt anatomy, context window)
- 3-4 hands-on exercises (write, test, refine prompts)
- 1 decision tree: "Is my prompt specific enough?"

---

### Chapter 11: Six-Part Prompting Framework
**Subtitle**: "A Structured Approach to Crafting Powerful Prompts"

#### Purpose
Teach a reusable framework for consistent prompting. Answer: "How do I systematically write prompts that work every time?"

#### Learning Outcomes
By the end of this chapter, readers will:
- Understand the six-part prompting framework and why each part matters
- Apply the framework to write structured, effective prompts
- Know when to include each part (and when to skip optional parts)
- Have practiced using the framework on multiple tasks
- Understand how the framework prevents common failures
- Be able to teach the framework to others

#### Key Topics to Cover
1. **The Six-Part Framework Overview**
   - **Part 1: Role/Persona**: "You are an expert Python developer with..."
   - **Part 2: Context**: "Given this codebase/situation/background..."
   - **Part 3: Task**: "Your task is to..."
   - **Part 4: Constraints**: "You must NOT... You should ONLY..."
   - **Part 5: Format**: "Output should be... Include... Exclude..."
   - **Part 6: Examples** (optional): "For example, ... Another example is..."

2. **Deep Dive: Each Part Explained**
   - **Role/Persona**: Why does framing the AI's role help? When to use it?
   - **Context**: What context is essential? What can be omitted?
   - **Task**: How to state the task clearly without over-specifying?
   - **Constraints**: What should you constrain? What should you leave open?
   - **Format**: When to specify format? How detailed should it be?
   - **Examples**: When do examples help? When do they constrain too much?

3. **Framework in Action**
   - Real-world task: "Build an API client for Stripe"
   - Step-by-step: Apply each part of the framework
   - Result: A complete, structured prompt
   - Execution: What AI generates from this prompt
   - Reflection: Why this worked better than ad-hoc prompting

4. **Optional Parts and Variations**
   - When to skip Role/Persona (if it's obvious)
   - When to skip Examples (if task is straightforward)
   - When to expand Context (for complex situations)
   - Framework variations: 4-part minimal, 8-part comprehensive

5. **Common Mistakes with the Framework**
   - Over-constraining: Too many constraints → AI can't be creative
   - Under-specifying task: Vague task → AI doesn't know what to build
   - Missing context: AI makes wrong assumptions
   - Conflicting parts: Role says "be creative" but Constraints say "follow exactly"

#### Hands-On Exercise
Apply the six-part framework to 3 different tasks:
- **Task 1**: Email validation function (simple)
- **Task 2**: REST API client (moderate)
- **Task 3**: Multi-step data processing pipeline (complex)

#### Prerequisites
- Chapter 10 completion (prompting foundations)
- Understanding of software requirements and specifications

#### Success Criteria
- Readers can name and explain all six parts of the framework
- Readers have applied the framework to 3+ different tasks
- Readers can identify when to include optional parts
- Readers understand common mistakes and how to avoid them
- Readers feel confident using the framework consistently

#### Pedagogical Approach
- **Framework as template**: Provide copy-paste template
- **Worked examples**: Show framework applied to 5+ different scenarios
- **Hands-on practice**: Readers write prompts using the framework
- **Comparison**: Framework-driven vs. ad-hoc (show the difference)
- **Checklists**: Provide validation checklist ("Did I include...?")

#### Approximate Content
- 4,000-5,000 words
- 1 framework template (copy-paste ready)
- 5-7 worked examples (framework applied to real tasks)
- 1 decision tree: "Which parts should I include?"
- 3 hands-on exercises (apply framework to tasks)
- 1 checklist: "Is my prompt complete?"
- 2 comparison tables: Framework vs. ad-hoc prompting

---

### Chapter 12: Multimodal and Advanced Input
**Subtitle**: "Beyond Text: Images, Video, and Tool Invocation"

#### Purpose
Expand prompting to multimodal inputs. Answer: "How do I work with images, videos, and advanced capabilities like function calling?"

#### Learning Outcomes
By the end of this chapter, readers will:
- Understand what multimodal AI means and why it matters
- Work with image inputs (upload, describe, ask questions about images)
- Work with video inputs (understanding, transcription, analysis)
- Use function calling / tool invocation to connect AI to external systems
- Understand when to use multimodal inputs vs. text-only
- Have practiced multimodal prompting with real tasks

#### Key Topics to Cover
1. **Multimodal AI: What and Why**
   - What is multimodal? (text + images + video + audio)
   - Why does it matter? (richer context, more powerful interactions)
   - Current capabilities: What AI can do with images/video today
   - Limitations: What AI still struggles with

2. **Working with Images**
   - Uploading images to AI (how to format prompts with images)
   - Describing images: "What is in this image?"
   - Asking questions: "Does this UI follow accessibility guidelines?"
   - Code from screenshots: "Generate code for this UI design"
   - Real-world use cases: UI debugging, accessibility checks, diagram analysis

3. **Working with Video**
   - Video understanding: What AI can extract (frames, transcripts, events)
   - Prompts for video: "Summarize this tutorial video"
   - Limitations: Processing time, cost, complexity
   - When video input is worth it vs. when text is sufficient

4. **Function Calling and Tool Invocation**
   - What is function calling? (AI invokes functions you define)
   - Why use it? (connect AI to databases, APIs, external systems)
   - How it works: Define function signature → AI decides when to call → You execute → Return result
   - Examples: Database queries, API calls, file operations
   - MCP integration preview: Connecting AI to tools via Model Context Protocol

5. **When to Use Multimodal vs. Text-Only**
   - Decision framework: Is the visual/audio information essential?
   - Cost considerations: Multimodal inputs are more expensive
   - Latency considerations: Images/video take longer to process
   - Accuracy considerations: When is text actually better?

#### Hands-On Exercise
Three multimodal tasks:
- **Task 1**: Upload a UI screenshot and ask AI to generate code
- **Task 2**: Use function calling to query a database
- **Task 3**: Analyze an accessibility issue from an image

#### Prerequisites
- Chapters 10-11 completion (prompting fundamentals and framework)
- Basic understanding of APIs and functions

#### Success Criteria
- Readers understand what multimodal AI can do
- Readers have uploaded an image and received AI analysis
- Readers have used function calling to connect AI to an external system
- Readers can decide when multimodal input is appropriate
- Readers understand cost and latency trade-offs

#### Pedagogical Approach
- **Show capabilities first**: Demonstrate what's possible with images/video
- **Then explain how**: Walk through technical details
- **Hands-on exercises**: Readers upload images, define functions, see results
- **Decision frameworks**: Help readers choose the right input type
- **Real-world scenarios**: Use realistic tasks (UI debugging, accessibility, API integration)

#### Approximate Content
- 4,000-5,000 words
- 5-7 image examples (screenshots with AI analysis)
- 2-3 function calling examples (code + explanations)
- 1 decision tree: "Should I use multimodal input?"
- 3 hands-on exercises (image, video, function calling)
- 1 cost/latency comparison table
- 2 diagrams: Function calling flow, MCP integration overview

---

### Chapter 13: Advanced Prompt Techniques
**Subtitle**: "Few-Shot Learning, Chain-of-Thought, and Debugging"

#### Purpose
Master advanced prompting strategies. Answer: "How do I handle complex tasks that require reasoning, examples, and systematic debugging?"

#### Learning Outcomes
By the end of this chapter, readers will:
- Use few-shot learning to guide AI with examples
- Apply chain-of-thought prompting for complex reasoning tasks
- Use prompt chaining to break large tasks into manageable steps
- Debug AI-generated code systematically
- Refine prompts based on output quality and failures
- Understand when to use each advanced technique
- Have confidence tackling complex, multi-step problems with AI

#### Key Topics to Cover
1. **Few-Shot Learning**
   - What is few-shot learning? (providing examples to guide AI)
   - Why does it work? (AI learns patterns from examples)
   - How to structure examples: Input → Output pairs
   - How many examples? (1-shot, 3-shot, 5-shot)
   - Real-world use cases: Data formatting, code style, domain-specific tasks

2. **Chain-of-Thought Prompting**
   - What is chain-of-thought? (asking AI to show reasoning steps)
   - Why does it improve accuracy? (explicit reasoning reduces errors)
   - How to prompt: "Let's think step by step..."
   - When to use it: Complex logic, math, multi-step decisions
   - Examples: Algorithm design, debugging, system architecture

3. **Prompt Chaining**
   - What is prompt chaining? (breaking large tasks into sequential prompts)
   - Why chain prompts? (manage complexity, control each step)
   - How to chain: Output of prompt 1 → Input to prompt 2 → ...
   - Real-world examples: Multi-file refactoring, full-stack feature development
   - Tools for chaining: Scripts, CI/CD pipelines, automation

4. **Debugging AI-Generated Code**
   - Common code failures: Syntax errors, logic bugs, edge case failures
   - Systematic debugging: Isolate → Reproduce → Report → Fix → Verify
   - Prompting for debugging: "Here's the error. Here's the context. Fix it."
   - Iteration loop: AI generates → You test → Report failure → AI refines
   - When to iterate vs. when to start over

5. **Refining Prompts Based on Output**
   - Analyzing failures: What went wrong? (vague prompt, missing context, wrong assumption)
   - Refining systematically: Add specificity → Add examples → Add constraints
   - Tracking refinements: Keep a prompt journal to learn over time
   - When to pivot: If 3+ iterations don't work, try a different approach

6. **Combining Techniques**
   - Few-shot + chain-of-thought: Examples with reasoning
   - Chaining + debugging: Multi-step refinement
   - Framework + advanced techniques: Structure + sophistication
   - Real-world scenario: Build a complex feature using all techniques

#### Hands-On Exercise
Three advanced prompting challenges:
- **Task 1**: Use few-shot learning to format data consistently
- **Task 2**: Use chain-of-thought to debug a complex algorithm
- **Task 3**: Use prompt chaining to build a multi-file feature (backend + frontend + tests)

#### Prerequisites
- Chapters 10-12 completion (prompting foundations, framework, multimodal)
- Comfortable with debugging and iteration

#### Success Criteria
- Readers can explain and use few-shot learning
- Readers can apply chain-of-thought prompting to reasoning tasks
- Readers have successfully chained multiple prompts to complete a large task
- Readers can systematically debug AI-generated code
- Readers understand when to use each advanced technique
- Readers have completed all 3 hands-on exercises

#### Pedagogical Approach
- **Technique-by-technique breakdown**: Explain each technique separately, then combine
- **Worked examples**: Show each technique applied to real tasks
- **Hands-on practice**: Readers apply techniques to progressively harder challenges
- **Debugging as a skill**: Normalize failures and teach systematic refinement
- **Decision frameworks**: Help readers choose the right technique for each situation

#### Approximate Content
- 5,000-6,000 words
- 5-7 few-shot learning examples (input/output pairs)
- 3-4 chain-of-thought examples (reasoning walkthroughs)
- 2-3 prompt chaining scenarios (multi-step workflows)
- 5-7 debugging scenarios (common failures + fixes)
- 3 hands-on exercises (few-shot, chain-of-thought, chaining)
- 2 decision trees: "Which technique should I use?" and "Should I refine or start over?"
- 1 prompt journal template (for tracking refinements)

---

## Part 3 Connection to Rest of Book

### Chapter 10 Prepares You For:
- **Chapter 11**: Foundation for applying the six-part framework
- **Part 4**: Writing clear specs for Python code generation
- **Part 5**: Specification-driven development requires clear prompting

### Chapter 11 Prepares You For:
- **Chapter 12-13**: Framework becomes the foundation for advanced techniques
- **Part 5**: Spec-Kit Plus methodology uses structured specifications
- **All future parts**: Consistent framework for all AI interactions

### Chapter 12 Prepares You For:
- **Part 6**: Function calling is essential for building agents
- **Part 7**: MCP integration uses function calling patterns
- **Part 9**: Realtime voice agents use multimodal capabilities

### Chapter 13 Prepares You For:
- **Part 4**: Debugging AI-generated Python code systematically
- **Part 5**: Complex specs require prompt chaining
- **Part 6**: Multi-agent systems use chaining patterns
- **All future parts**: Advanced techniques apply everywhere

---

## Part 3 Success Metrics

| Metric | Success Measure | Target |
|--------|-----------------|--------|
| **Prompt Quality** | Readers write effective prompts using framework | 90%+ apply framework correctly |
| **Framework Mastery** | Readers can explain all six parts | 85%+ explain clearly |
| **Multimodal Usage** | Readers have used images and function calling | 80%+ complete multimodal exercises |
| **Advanced Techniques** | Readers use few-shot, chain-of-thought, chaining | 85%+ apply techniques correctly |
| **Debugging Confidence** | Readers can debug AI code systematically | 80%+ demonstrate systematic debugging |
| **Exercise Completion** | Readers complete all hands-on exercises | 80%+ complete all exercises |
| **Readiness for Part 4** | Readers feel confident prompting for code generation | 85%+ agree |

---

## Part 3 Quality Standards

All Part 3 content MUST:
- ✅ Use the 8 domain skills (learning-objectives, concept-scaffolding, code-example-generator, exercise-designer, assessment-builder, technical-clarity, book-scaffolding, ai-augmented-teaching)
- ✅ Include type hints on all Python code examples
- ✅ Follow pedagogical principle: Show → Explain → Practice → Assess
- ✅ Zero gatekeeping language ("simple", "obvious", "just")
- ✅ Align with Constitution principles (esp. Principle 1: AI-First, Principle 8: Inclusivity, Principle 9: Show-then-Explain)
- ✅ Include hands-on exercises for every major concept
- ✅ Provide multiple examples (good/bad, simple/complex, realistic/toy)
- ✅ Heavy scaffolding: Break complex frameworks into digestible steps
- ✅ Include accessibility considerations (alt text, high contrast, clear language)

---

## Part 3 Review Cycles

Expect 2-3 review cycles:

1. **First Draft**: Content complete, structure sound, framework clearly explained
2. **First Review**: Check for clarity, correctness, alignment with Constitution, hands-on exercises work
3. **Second Review** (if needed): Refine based on feedback, update examples, improve scaffolding
4. **Final**: Ready for readers

---

## Next Steps After Part 3

Once Part 3 is approved and ready for writing:

1. **Invoke chapter-planner subagent** with this spec as input
2. **Output**: `specs/part-3/chapter-10-plan.md` through `specs/part-3/chapter-13-plan.md`
3. **Then invoke lesson-writer subagent** to write each chapter's lessons iteratively
4. **Finally invoke technical-reviewer** to validate completed Part 3
5. **Once Part 3 is in implementation**: Proceed to Part 4 (Python: The Language of AI Agents)

---

## Dependencies

**Part 3 depends on**:
- Part 1 completion (AI-driven development mindset, tools installed)
- Part 2 completion (familiar with Claude Code, Gemini CLI, or similar tools)

**Parts that depend on Part 3**:
- Part 4 (Python): Effective prompting is essential for code generation
- Part 5 (Spec-Kit Plus): Specifications are structured prompts
- Part 6 (Agentic AI): Agent instructions use prompting frameworks
- All future parts: Prompting skills are foundational

---
