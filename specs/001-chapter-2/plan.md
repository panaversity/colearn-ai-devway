# Implementation Plan: Chapter 2 - Understanding AI Tools

**Branch**: `001-chapter-2` | **Date**: 2025-10-29 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/001-chapter-2/spec.md`

## Summary

Chapter 2, titled **"Understanding AI Tools: The Nine Revolutions That Made This Possible"**, bridges the conceptual understanding from Chapter 1 (mindset shift) with the hands-on tool setup in Chapter 3. It provides readers with a comprehensive yet accessible explanation of the technological foundations that enabled AI-driven development, combining:

1. **The Nine Technological Revolutions** (2020-2025) - Historical breakthroughs that converged to make AI-assisted development possible
2. **The New Wave of AI Coding Agents** - Practical understanding of Claude Code, Gemini CLI, OpenAI Codex, and Qwen Code

**Technical Approach**: Use concept scaffolding to break 9 revolutions + 4 tools into digestible lessons with progressive disclosure, visual aids, and clear learning objectives. Maintain Part 1 philosophy (LIGHT cognitive load, HEAVY scaffolding, zero gatekeeping language). Target 4,000-5,000 words across 3-4 lessons with simple English and concise explanations per user guidance.

## Pedagogical Context

**Content Type**: Educational book chapter (Part 1, Chapter 2 of 46-chapter book)
**Target Audience**: Absolute beginners, professionals pivoting to AI-driven development, solo entrepreneurs
**Prerequisites**: Chapter 1 completed (mindset shift from "coder to orchestrator")
**Learning Philosophy**: Show-then-explain, heavy scaffolding, evidence-based reasoning
**Cognitive Load**: LIGHT (3-4 key concepts per lesson maximum)
**Word Count Target**: 4,000-5,000 words total (per Part 1 spec)
**Reading Time**: 20-30 minutes (completable in one sitting)
**Visual Aids Required**: 2-3 timeline diagrams, 1 Snakes and Ladders visualization, 2-3 comparison tables
**Accessibility Requirements**: Alt text for all images, high contrast, clear language (Constitution Principle 8)

## Constitution Check

*GATE: Must pass before lesson writing begins.*

### ✅ Principle 1: AI-First Teaching Philosophy
- **Status**: PASS
- **Evidence**: Chapter explains how AI tools became viable for professional development, setting foundation for later hands-on AI usage
- **Application**: Chapter 2 demonstrates AI-first philosophy by explaining the technological infrastructure that enables AI collaboration

### ✅ Principle 2: Spec-Kit Methodology as Foundation
- **Status**: PASS
- **Evidence**: Chapter introduces "vibe coding vs. SDD" distinction, preparing readers for Part 5's formal Spec-Kit methodology
- **Application**: Conceptual introduction to specification-driven workflows as superior to undisciplined prompting

### ✅ Principle 3: Modern Python Standards (3.13+)
- **Status**: N/A (no code in Chapter 2)
- **Evidence**: Chapter 2 is conceptual/explanatory; Python coding begins in Chapter 4

### ✅ Principle 4: Production-Quality Code Standards
- **Status**: N/A (no code in Chapter 2)
- **Evidence**: Chapter 2 is conceptual/explanatory; code quality standards apply starting Chapter 4

### ✅ Principle 5: Test-Driven Mindset
- **Status**: PASS (conceptual introduction)
- **Evidence**: Chapter introduces TDD as part of "vibe coding vs. SDD" comparison, explaining why tests matter when AI generates code
- **Application**: Sets expectation that testing is essential even (especially) when AI writes code

### ✅ Principle 6: Clear, Accessible Technical Writing
- **Status**: PASS
- **Evidence**: Spec requires zero gatekeeping language, technical clarity skill application, simple English per user guidance
- **Application**: All 12 functional requirements emphasize accessible explanation with visual aids

### ✅ Principle 7: Incremental Complexity Through Book-Scaffolding
- **Status**: PASS
- **Evidence**: Chapter 2 is in Part 1 (chapters 1-9, HEAVY scaffolding per constitution v2.2.0)
- **Application**: Concept hierarchy (4 levels) ensures progressive disclosure; visual aids reduce cognitive load

### ✅ Principle 8: Inclusivity & Universal Design
- **Status**: PASS
- **Evidence**: Spec mandates alt text for all images, high contrast, clear language, multiple reading paths (narrative + bullet points)
- **Application**: Edge case handling addresses non-technical readers, skeptical readers, visual learners

### ✅ Principle 9: Show-Then-Explain Pedagogy
- **Status**: PASS
- **Evidence**: Chapter structure leads with evidence (ICPC World Finals, adoption metrics) before explaining implications
- **Application**: Each revolution presented with real-world examples before abstract explanation

### ✅ Principle 10: Progressive Real-World Projects
- **Status**: N/A (Chapter 2 is foundational knowledge)
- **Evidence**: Real-world projects begin in Chapter 4; Chapter 2 provides context for why those projects use AI tools

### ✅ Principle 11: Community & Continuous Improvement
- **Status**: PASS
- **Evidence**: Chapter includes references to open-source tools (Gemini CLI, Qwen Code), community-driven MCP ecosystem
- **Application**: Emphasizes community contribution and learning from others

**Gate Result**: ✅ **PASS** - All applicable principles satisfied. Ready for lesson design.

## Lesson Structure

Chapter 2 will be broken into **4 lessons** to maintain digestibility while covering all required content:

### Lesson 1: "The AI Inflection Point" (1,000-1,200 words)
**Purpose**: Hook readers with compelling evidence and establish that 2025 is genuinely different

**Key Concepts (3)**:
1. The 2025 AI Inflection Point - AI moved from experimental to default mode
2. Mainstream Adoption Evidence - 84% Stack Overflow, 95% DORA, enterprise reorganization
3. Capability Milestones - ICPC World Finals perfect score, GDPval benchmarks

**Content Flow**:
- **Hook**: ICPC World Finals 2025 - AI perfect score beats all human teams
- **Evidence Section**: Quantitative data from surveys and benchmarks
- **"Why This Matters for YOU"**: Personal relevance for readers
- **Preview**: What enabled this moment (tease the 9 revolutions)

**Visual Aids**:
- Timeline showing adoption curve (2020-2025)
- Bar chart comparing AI performance metrics (2024 vs 2025)

**Learning Objectives** (skill 1):
- LO-1.1: Cite at least two pieces of quantitative evidence for the 2025 inflection point
- LO-1.2: Explain why mainstream adoption (84%+) signals genuine paradigm shift
- LO-1.3: Recognize AI capability milestones (ICPC, GDPval) and their significance

**Assessment** (skill 5):
- Quick Check: "Can you name two surveys showing 80%+ AI adoption among developers?"
- Reflection: "Why does the ICPC perfect score matter more than autocomplete improvements?"

---

### Lesson 2: "The Nine Technological Revolutions" (1,500-1,800 words)
**Purpose**: Explain the technological foundation with structured, evidence-based breakdown

**Key Concepts (4)**:
1. Technological Convergence - Nine distinct breakthroughs that worked together
2. Three-Layer AI Development Stack - Frontier Models → AI-First IDEs → Development Agents
3. Critical Thresholds - What changed to make AI viable for production development
4. Snakes and Ladders Pattern - Why vertical market opportunities exist in Layer 3

**Content Flow**:
- **Introduction**: Why nine revolutions, not one big breakthrough
- **The Nine Revolutions** (structured presentation):
  - **Layer 1: Foundation Models & Adoption**
    1. Frontier LLMs Crossed Critical Thresholds (2023-2025)
    2. Mainstream Adoption Among Developers (2024-2025)
    3. AI Coding Agents Emerged (Late 2024-2025)
  - **Layer 2: Infrastructure & Standards**
    4. Natural Language Specifications Became Executable (2024-2025)
    5. Model Context Protocol (MCP) Standardized Tool Integration (2024)
    6. AI-Native IDEs Matured (2023-2025)
  - **Layer 3: Production Readiness**
    7. Cloud-Native Infrastructure Became Production-Ready (2020-2025)
    8. Composable Architectures Enabled Modular AI Systems (2024-2025)
    9. Universal Deployment Platforms Simplified Distribution (2023-2025)
- **The Three-Layer Stack**: How the layers interoperate
- **Snakes and Ladders**: Competitive dynamics and vertical opportunities
- **Synthesis**: Why convergence matters more than any single revolution

**Visual Aids**:
- Timeline diagram showing all 9 revolutions (2020-2025)
- Three-layer stack architecture illustration
- Snakes and Ladders competitive pattern diagram

**Scaffolding Strategy** (skill 2):
- Present revolutions in logical groups (3+3+3) rather than overwhelming list
- Use "Why This Matters" boxes after each group
- Provide concrete examples for each revolution (not abstract)
- Progressive disclosure: overview → details → synthesis

**Learning Objectives** (skill 1):
- LO-2.1: Name and briefly explain at least 3 of the 9 revolutions
- LO-2.2: Describe the three-layer AI development stack and how layers work together
- LO-2.3: Identify at least one vertical market opportunity using Snakes and Ladders pattern
- LO-2.4: Explain why technological convergence created unprecedented conditions

**Code Examples** (skill 3):
- No code in this lesson (conceptual explanation only)
- Future reference: "In Chapter 4, you'll use these tools to write your first AI-assisted program"

**Assessment** (skill 5):
- Quick Check: "Match each revolution to its layer (Foundation/Infrastructure/Production)"
- Reflection: "Which revolution surprised you most? Why?"
- Exercise Preview: Identify one industry vertical you could target

---

### Lesson 3: "The New Wave of AI Coding Agents" (1,200-1,400 words)
**Purpose**: Provide practical understanding of the four major tools readers will encounter

**Key Concepts (4)**:
1. What Makes AI Coding Agents Different - Autonomous execution vs. autocomplete
2. The Four Major Agents - Claude Code, Gemini CLI, OpenAI Codex, Qwen Code
3. Tool Selection Criteria - Pricing, licensing, capabilities, use cases
4. Model Context Protocol (MCP) - Why standardization enables interoperability

**Content Flow**:
- **The Shift**: From autocomplete (GitHub Copilot) to autonomous agents
- **The Four Major Tools** (structured comparison):
  - **Claude Code**: Best for deep contextual understanding and autonomous refactoring
    - Capabilities: Subagents, skills, hooks, checkpoints
    - Pricing: Pro/Max subscribers
    - Best for: Complex refactoring, large codebases
  - **Gemini CLI**: Most generous free tier and Google ecosystem integration
    - Capabilities: 1M token context, Google Search grounding, MCP-based
    - Pricing: 60 requests/min, 1,000/day free
    - Best for: Beginners, cost-conscious developers
  - **OpenAI Codex**: Strongest team collaboration and enterprise tooling
    - Capabilities: Slack integration, mobile support, admin tools
    - Pricing: ChatGPT Plus/Pro/Business/Enterprise
    - Best for: Team workflows, enterprise environments
  - **Qwen Code**: Most cost-effective and fully open for customization
    - Capabilities: 256K context (expandable to 1M), state-of-the-art open model
    - Pricing: 2,000 requests/day free, Apache 2.0 license
    - Best for: Customization, cost savings, transparency
- **Tool Selection Decision Framework**: How to choose based on needs
- **MCP Standard**: Why interoperability matters and how it works
- **The Open Source Advantage**: Community innovation, no vendor lock-in

**Visual Aids**:
- Comparison table: 4 tools across pricing, capabilities, use cases, context windows
- Decision tree: "Which tool should I use?" based on needs
- MCP ecosystem diagram showing tool interoperability

**Scaffolding Strategy** (skill 2):
- Present tools with consistent structure (capabilities, pricing, best for)
- Use comparison table for quick reference
- Provide decision framework before overwhelming with details
- Emphasize that readers can choose ONE tool initially (reduce anxiety)

**Learning Objectives** (skill 1):
- LO-3.1: Identify the key differentiator for each of the four major AI coding agents
- LO-3.2: Match tool capabilities to specific use cases (e.g., "I need free tier" → Gemini/Qwen)
- LO-3.3: Explain the advantages of open-source tools (Gemini CLI, Qwen Code) vs. proprietary
- LO-3.4: Understand how Model Context Protocol (MCP) enables tool interoperability

**Assessment** (skill 5):
- Quick Check: "Match each tool to its key strength (free tier, enterprise, customization, context)"
- Scenario: "You're a solo developer on a budget. Which tool should you try first? Why?"
- Preview Chapter 3: "In the next chapter, you'll install your chosen tool"

---

### Lesson 4: "Vibe Coding vs. Spec-Driven Development" (800-1,000 words)
**Purpose**: Introduce the methodological distinction and DORA perspective on discipline

**Key Concepts (3)**:
1. Two Development Patterns - Vibe coding (exploration) vs. SDD (production)
2. DORA Perspective - AI amplifies existing organizational capabilities (good or bad)
3. When to Use Each Approach - Learning/prototyping vs. production systems

**Content Flow**:
- **Introduction**: Speed without method accelerates defects
- **Vibe Coding** (Alexandr Wang's term):
  - Definition: Intuition-led, prompt-and-iterate exploration
  - Strengths: Rapid prototyping, low cognitive overhead, creative leaps
  - Failure modes: Ambiguous requirements, missing tests, architecture drift
  - Appropriate contexts: Learning, exploration, proof-of-concept
- **Spec-Driven Development**:
  - Definition: Specification-first workflow (spec → plan → tasks → implement)
  - Strengths: Predictable delivery, maintainable code, team collaboration
  - Guardrails: TDD (tests first), ADRs (document decisions), PRs (review)
  - Appropriate contexts: Production systems, multi-person projects
- **The Comparative Example**: Team A (vibe coding) vs. Team B (SDD + TDD)
  - Task: Add `/summarize` endpoint for PDF documents
  - Team A: Ships fast, breaks in staging, accumulates tech debt
  - Team B: Specs first, tests first, ships smoothly, extends confidently
- **DORA Findings**: AI amplifies strengths AND friction
  - High performers: Use AI for throughput AND stability
  - Strugglers: AI accelerates existing dysfunction
- **The Balanced Approach**: Vibe coding for discovery, SDD for delivery
- **Preview Part 5**: "Later in the book, you'll learn Spec-Kit Plus methodology in detail"

**Visual Aids**:
- Comparison table: Vibe Coding vs. SDD (strengths, failure modes, contexts)
- Team A vs. Team B workflow diagrams showing process differences

**Scaffolding Strategy** (skill 2):
- Present both approaches neutrally (avoid "bad vs. good")
- Use concrete example (Team A/B) before abstract principles
- Emphasize "when to use each" rather than prescriptive judgment
- Frame as "both have value" but production requires discipline

**Learning Objectives** (skill 1):
- LO-4.1: Describe the failure modes of vibe coding in production contexts
- LO-4.2: Explain when vibe coding is valuable (learning, exploration, prototyping)
- LO-4.3: Understand why specifications become more important when AI generates code faster
- LO-4.4: Recognize that AI amplifies existing organizational capabilities (DORA perspective)

**Assessment** (skill 5):
- Quick Check: "True or False: Vibe coding is bad and should never be used." (Answer: False)
- Scenario: "You're learning a new Python library. Should you use vibe coding or SDD? Why?"
- Reflection: "Think of a time you moved fast and broke things. What would specs have prevented?"

**Exercise Designer** (skill 4):
- **Exercise 1**: "What vertical could YOU dominate?" (connects to Snakes and Ladders)
- **Exercise 2**: "Match tools to use cases" (reinforces Lesson 3 learning)
- **Exercise 3**: "Explain to a skeptical colleague why 2025 is different" (synthesizes all lessons)

---

## Chapter-Level Learning Outcomes (Consolidated)

By the end of Chapter 2, readers will be able to:

1. **Foundation Knowledge** (Lesson 1):
   - Cite quantitative evidence (surveys, benchmarks) proving 2025 is an inflection point
   - Recognize AI capability milestones (ICPC, GDPval) and their significance

2. **Technological Understanding** (Lesson 2):
   - Name and explain at least 3 of the 9 technological revolutions
   - Describe the three-layer AI development stack (Frontier Models → IDEs → Agents)
   - Identify vertical market opportunities using Snakes and Ladders pattern

3. **Practical Tool Knowledge** (Lesson 3):
   - Compare the four major AI coding agents (Claude Code, Gemini CLI, Codex, Qwen)
   - Match tool capabilities to specific use cases based on needs
   - Understand the Model Context Protocol (MCP) and why standardization matters

4. **Methodological Awareness** (Lesson 4):
   - Distinguish between vibe coding (exploration) and SDD (production)
   - Recognize when each approach is appropriate
   - Understand that AI amplifies existing capabilities (DORA perspective)

5. **Readiness for Chapter 3**:
   - Feel motivated to install tools with confidence in their technological foundation
   - Have tool selection criteria to make informed decisions
   - Understand that discipline (specs, tests, reviews) makes AI collaboration sustainable

## Content Quality Standards

All lessons MUST meet these requirements per constitution and Part 1 spec:

### Language & Clarity (Principle 6 + User Guidance)
- ✅ Use simple English (per user: "keep the lessons concise to keep readers engaged")
- ✅ Define all jargon on first use with accessible analogies
- ✅ Zero gatekeeping language ("simple," "obvious," "just")
- ✅ Avoid superlatives and promotional language
- ✅ Maintain neutral, evidence-based tone

### Cognitive Load (Part 1 Philosophy)
- ✅ Maximum 3-4 key concepts per lesson
- ✅ Progressive disclosure (overview → details → synthesis)
- ✅ Visual aids to reduce text-heavy cognitive load
- ✅ Clear section headings for skimming
- ✅ "Why This Matters" context boxes for personalization

### Pedagogical Consistency (Principle 9)
- ✅ Show-then-explain pattern (examples before abstractions)
- ✅ Real-world evidence before claims
- ✅ Concrete scenarios before general principles
- ✅ Learning objectives stated upfront in each lesson

### Accessibility (Principle 8)
- ✅ Alt text for ALL images
- ✅ High contrast colors in diagrams
- ✅ Text descriptions as fallbacks for visual content
- ✅ Multiple reading paths (narrative + bullet points + tables)

### Assessment & Practice (Principle 5 + Skill 5)
- ✅ Quick Check questions after each major concept
- ✅ Reflection prompts connecting to reader experience
- ✅ End-of-chapter exercises reinforcing key learning
- ✅ Preview of next chapter to maintain continuity

## Success Metrics (From Spec)

Chapter 2 will be validated against these measurable outcomes:

| Metric | Target | Validation Method |
|--------|--------|-------------------|
| SC-001 | 85% can name/explain 3+ revolutions | Post-chapter quiz or reflection exercise |
| SC-002 | 80% can match tools to use cases | Scenario-based assessment in Lesson 3 |
| SC-003 | 90% cite 2+ evidence points for inflection | Quick check in Lesson 1 |
| SC-004 | 80% distinguish vibe coding vs. SDD | Scenario question in Lesson 4 |
| SC-005 | 85% explain Snakes and Ladders + identify vertical | Exercise 1 completion |
| SC-006 | 90% recognize AI amplifies capabilities | DORA perspective explanation |
| SC-007 | 80% describe three-layer stack | Quick check in Lesson 2 |
| SC-008 | 85% feel motivated for Chapter 3 | Reader feedback or survey |
| SC-009 | 90% report chapter was accessible | Reader feedback (no cognitive overload) |
| SC-010 | 80% complete end-of-chapter exercises | Exercise completion tracking |

## Visual Assets Required

**Note**: Visual assets will be created later. For initial lesson writing, use **placeholders** at appropriate locations in the content. Placeholders will be replaced with actual visuals in a subsequent phase.

**Placeholder Format**:
```markdown
<!-- VISUAL PLACEHOLDER: [Asset Name] -->
**[Asset Title]**

[Text description of what the visual will show - this serves as both placeholder and alt text]

*[Visual will be added in design phase]*
<!-- END VISUAL PLACEHOLDER -->
```

**Example**:
```markdown
<!-- VISUAL PLACEHOLDER: Timeline-AI-Adoption-Curve -->
**Timeline: AI Adoption Curve (2020-2025)**

This timeline shows the mainstream adoption acceleration of AI coding tools from 2020 (experimental phase) to 2025 (mainstream adoption). Key milestones include: GitHub Copilot launch (2021), Cursor rapid growth (2023-2024), Claude Code reaching $500M ARR (2025), and Stack Overflow survey showing 84% developer adoption (2025).

*[Visual will be added in design phase]*
<!-- END VISUAL PLACEHOLDER -->
```

### Lesson 1 Visuals
1. **Timeline: AI Adoption Curve (2020-2025)** - Shows mainstream adoption acceleration
   - Data points: GitHub Copilot launch, Cursor growth, Claude Code $500M ARR, 84% Stack Overflow survey
   - Alt text: "Timeline showing AI coding tool adoption from 2020 (experimental) to 2025 (mainstream)"

2. **Bar Chart: AI Performance Milestones** - Compares 2024 vs 2025 capability benchmarks
   - Data: GDPval scores (GPT-4o 13.7% → GPT-5 40.6%), ICPC results (human teams vs AI)
   - Alt text: "Bar chart comparing AI coding performance 2024 vs 2025 showing 3x improvement"

### Lesson 2 Visuals
3. **Timeline: The Nine Revolutions (2020-2025)** - Shows when each revolution occurred
   - Groups revolutions by layer (Foundation, Infrastructure, Production)
   - Alt text: "Timeline showing nine technological revolutions grouped by infrastructure layer"

4. **Architecture Diagram: Three-Layer Stack** - Illustrates how layers interoperate
   - Layer 1: Frontier Models (GPT-5, Claude 4.5+, Gemini 2.5+)
   - Layer 2: AI-First IDEs (Cursor, VS Code, Claude Code CLI)
   - Layer 3: Development Agents (Claude Code, Gemini CLI, Codex, Qwen)
   - Alt text: "Three-layer architecture showing Frontier Models feeding AI-First IDEs feeding Development Agents"

5. **Snakes and Ladders Diagram** - Shows competitive dynamics across three layers
   - Layer 1: Consumer AI → 2 winners (OpenAI 800M, Google Gemini)
   - Layer 2: Horizontal Agents → 2 winners per domain (Claude Code #1, Gemini CLI #2)
   - Layer 3: Vertical Agents → Unlimited winners across industry verticals
   - Alt text: "Competitive pattern showing market consolidation in layers 1-2 but unlimited opportunities in layer 3 vertical markets"

### Lesson 3 Visuals
6. **Comparison Table: Four Major AI Coding Agents** - Side-by-side comparison
   - Columns: Agent, Vendor, Pricing, Context Window, Key Capabilities, Best For
   - Rows: Claude Code, Gemini CLI, OpenAI Codex, Qwen Code
   - Alt text: "Comparison table of four AI coding agents showing pricing, capabilities, and ideal use cases"

7. **Decision Tree: Which Tool Should I Use?** - Guides tool selection
   - Branches: Budget (free tier needed?), Ecosystem (Google/OpenAI/Open Source?), Use Case (solo/team/enterprise?)
   - Alt text: "Decision tree helping readers choose between Claude Code, Gemini CLI, Codex, and Qwen Code based on needs"

### Lesson 4 Visuals
8. **Comparison Table: Vibe Coding vs. SDD** - Side-by-side workflow comparison
   - Columns: Approach, Definition, Strengths, Failure Modes, Appropriate Contexts
   - Rows: Vibe Coding, Spec-Driven Development
   - Alt text: "Comparison showing vibe coding suits exploration while SDD suits production"

9. **Workflow Diagram: Team A vs. Team B** - Illustrates process differences
   - Team A: Prompt → Code → Ship → Break → Fix (cycle repeats)
   - Team B: Spec → Tests → Code → Review → Ship (smooth progression)
   - Alt text: "Workflow comparison showing Team A's reactive cycle vs Team B's proactive process"

## Lesson Writing Guidelines (For lesson-writer subagent)

### Lesson Template Structure
Each lesson MUST follow this structure:

```markdown
# Lesson [N]: [Title]

## Learning Objectives
- [LO statements from plan]

## Introduction (Hook)
[Compelling opening that connects to reader's experience]

## [Section 1: Main Concept A]
[Content with scaffolding]

### Why This Matters for YOU
[Personalization box]

## [Section 2: Main Concept B]
[Content with scaffolding]

### Quick Check
[Assessment questions]

## [Section 3: Main Concept C]
[Content with scaffolding]

## Summary
[Key takeaways - 3-4 bullet points maximum]

## What's Next
[Preview next lesson with continuity]
```

### Visual Placeholder Guidelines

**IMPORTANT**: Visual assets are not yet created. Use placeholders at appropriate locations in lessons.

**When to Insert Visual Placeholders**:
- After introducing a concept that would benefit from visualization
- Before or after complex explanations (timelines, architectures, comparisons)
- At natural breaking points in the narrative flow
- Where specified in the lesson plan (see Visual Assets Required section)

**Placeholder Insertion Rules**:
1. **Always use the standard placeholder format** (see Visual Assets Required section above)
2. **Write comprehensive text descriptions** - These serve dual purposes:
   - Act as placeholder content so readers can understand the concept even without the visual
   - Provide specifications for future visual design
   - Serve as alt text when visuals are added
3. **Include all key information** - Data points, relationships, flow directions, labels
4. **Use consistent naming**: Match the asset names from the Visual Assets Required section
5. **Position strategically**: Place placeholders where they enhance understanding, not interrupt flow

**Example Placement in Lesson Flow**:
```markdown
## The 2025 AI Inflection Point

In the summer of 2025, something remarkable happened at the ICPC World Finals...

[narrative explanation of ICPC results]

<!-- VISUAL PLACEHOLDER: Timeline-AI-Adoption-Curve -->
**Timeline: AI Adoption Curve (2020-2025)**

This timeline shows the mainstream adoption acceleration...
[full description as specified in plan]

*[Visual will be added in design phase]*
<!-- END VISUAL PLACEHOLDER -->

This rapid adoption isn't just hype—it's backed by enterprise investment...
[continue narrative]
```

**Comparison Tables** (Lesson 3, Lesson 4):
- These can be implemented as **markdown tables immediately** (they don't require graphical design)
- Still use placeholder comments for consistency, but include the working table
- Example:
```markdown
<!-- VISUAL PLACEHOLDER: Comparison-Table-Four-AI-Agents -->
**Comparison: Four Major AI Coding Agents**

| Agent | Vendor | Pricing | Context Window | Best For |
|-------|--------|---------|----------------|----------|
| Claude Code | Anthropic | Pro/Max subscribers | 200K+ tokens | Complex refactoring, large codebases |
| Gemini CLI | Google | 60 req/min free | 1M tokens | Beginners, cost-conscious developers |
| OpenAI Codex | OpenAI | ChatGPT Plus/Pro | Varies | Team workflows, enterprise |
| Qwen Code | Alibaba | 2,000 req/day free | 256K-1M tokens | Customization, open source |

*[Table above is functional; graphical version may be added in design phase for enhanced readability]*
<!-- END VISUAL PLACEHOLDER -->
```

### Tone & Voice Guidelines
- **Conversational but authoritative**: "You might be wondering..." not "One might wonder..."
- **Evidence-based**: Lead with data, cite sources, let facts speak
- **Encouraging without condescending**: "This is complex, and that's okay" not "Don't worry, it's simple!"
- **Transparent about complexity**: Acknowledge when concepts are challenging
- **Future-focused**: "When you use Claude Code in Chapter 4..." creates anticipation

### Integration Points Between Lessons
- **Lesson 1 → Lesson 2**: "Now that you've seen the evidence, let's understand what made this possible..."
- **Lesson 2 → Lesson 3**: "These nine revolutions created the foundation. Now let's meet the tools you'll actually use..."
- **Lesson 3 → Lesson 4**: "You understand the tools. Now let's talk about how to use them effectively..."
- **Lesson 4 → Chapter 3**: "You're ready to install your chosen tool and start your hands-on journey..."

## Source Material Integration

**Primary Sources** (available in `context/03_chap2_spec/`):
1. **readme.md**: Complete combined content (Parts I + II)
2. **readme1.md**: Academic-style paper on AI Turning Point with DORA perspective
3. **readme2.md**: Developer-focused narrative on AI coding agents revolution
4. **Images**: `typist.jpg`, `shift.png`, `coding_agents.png`, `claude_code.png`, `gemini.png`, `codex.png`, `qwen.png`

**Content Extraction Strategy**:
- **Lesson 1**: Extract from readme1.md sections 1-2 (Introduction, Evidence)
- **Lesson 2**: Extract from readme1.md sections 2-3 (Evidence subsections, Modern Stack) + readme.md Part I sections
- **Lesson 3**: Extract from readme2.md (Tool-specific sections: Claude Code, Gemini CLI, Codex, Qwen)
- **Lesson 4**: Extract from readme1.md section 4 (Vibe Coding vs. SDD) + section 6 (DORA Perspective)

**Synthesis Approach**:
- Use readme1.md for evidence-based framing and DORA perspective
- Use readme2.md for practical tool details and developer narrative
- Combine both sources to create balanced, accessible lessons
- Simplify academic language while preserving factual accuracy
- Add pedagogical scaffolding not present in source material

## Domain Skills Application Matrix

| Skill | Lesson 1 | Lesson 2 | Lesson 3 | Lesson 4 | Chapter-Level |
|-------|----------|----------|----------|----------|---------------|
| **1. Learning Objectives** | 3 LOs stated upfront | 4 LOs stated upfront | 4 LOs stated upfront | 4 LOs stated upfront | 5 consolidated outcomes |
| **2. Concept Scaffolding** | Hook → Evidence → Personal relevance | Overview → 3 groups → Synthesis | Shift → 4 tools → Decision framework | Both approaches → Example → Balance | Progressive 4-lesson sequence |
| **3. Code Example Generator** | N/A (no code) | N/A (no code) | N/A (no code) | N/A (no code) | Code begins Chapter 4 |
| **4. Exercise Designer** | Quick checks + reflection | Quick checks + reflection | Scenario + preview | Scenario + reflection | 3 end-of-chapter exercises |
| **5. Assessment Builder** | 2 quick checks | 2 quick checks | 2 quick checks | 3 quick checks | Chapter-level validation metrics |
| **6. Technical Clarity** | Define "inflection point", "mainstream adoption" | Define "context window", "token", "MCP" | Define "autonomous", "licensing", "open source" | Define "TDD", "ADR", "PR" | All jargon defined on first use |
| **7. Book Scaffolding** | Part 1 Ch 2 position; references Ch 1 mindset | References Ch 1 context; previews Ch 3 tools | References Ch 1-2 foundation; sets up Ch 3 install | Synthesizes Ch 1-2; transitions to Ch 3 | Clear narrative arc across 4 lessons |
| **8. AI-Augmented Teaching** | Shows AI capabilities advancing | Explains AI-enabling infrastructure | Introduces actual AI tools | Teaches AI collaboration discipline | Prepares readers for AI partnership |

## Next Steps After Planning

Once this plan is approved:

1. ✅ **Phase 0 Complete**: Research complete (source materials in `context/03_chap2_spec/`)
2. ✅ **Phase 1 Complete**: Lesson structure defined, visual assets specified, content extraction strategy documented
3. ⏭️ **Next: /sp.tasks**: Generate task checklist for implementing all 4 lessons + exercises (with visual placeholders)
4. ⏭️ **Then: Invoke lesson-writer subagent**: Write Lessons 1-4 following plan structure and applying all 8 domain skills
   - **Note**: Lessons will use **visual placeholders** as specified in this plan
   - Actual visual assets will be created in a separate design phase after content is complete
5. ⏭️ **Then: Invoke technical-reviewer subagent**: Validate completed chapter content against constitution and quality standards
6. 🎨 **Future: Visual Asset Creation Phase** (separate workflow):
   - Design and create the 9 visual assets based on placeholder specifications
   - Replace placeholders with actual images/diagrams
   - Validate visual accessibility (alt text, high contrast, mobile rendering)
   - This phase can proceed in parallel with other chapters or after Chapter 2 content approval

## Notes & Decisions

### Stakeholder Questions Addressed (From Spec)

**Q1 (Depth vs. Breadth)**: Hybrid approach (1-C) - Main narrative accessible + optional "Deep Dive" context boxes for interested readers
- **Implementation**: Lessons use simple language in main flow; "Why This Matters" boxes provide deeper context
- **Rationale**: Serves both eager learners (main narrative) and skeptics/decision-makers (evidence boxes)

**Q2 (Tool Coverage)**: Focus on two main tools (2-B) - Claude Code and Gemini CLI prioritized, others covered concisely
- **Implementation**: Lesson 3 presents all four but emphasizes Claude Code (used in book examples) and Gemini CLI (best free tier)
- **Rationale**: Reduces cognitive load while ensuring readers can make informed choices

**Q3 (Chapter Length)**: Enforce 5,000-word limit (3-A) through judicious editing
- **Implementation**: Lesson 1 (1,000-1,200), Lesson 2 (1,500-1,800), Lesson 3 (1,200-1,400), Lesson 4 (800-1,000) = ~4,500-5,400 words
- **Rationale**: Respects Part 1 cognitive load philosophy; ensures 20-30 minute reading time

**Q4 (Exercise Design)**: All three optional exercises (4-D)
- **Implementation**: End-of-chapter section with three exercises readers can choose based on interests
- **Rationale**: Maximum learning opportunity without overwhelming; reader autonomy

**Q5 ("Vibe Coding" Emphasis)**: Brief mention (5-B) - Introduce conceptually, full treatment in Part 5
- **Implementation**: Lesson 4 explains both approaches neutrally; references Part 5 for Spec-Kit Plus methodology
- **Rationale**: Prevents bad habits early without overwhelming with methodology details

### User Guidance Integration

**"Use simple English and keep lessons concise"**:
- ✅ Word count targets ensure brevity (4,500-5,400 words total)
- ✅ Language guidelines emphasize accessibility (zero gatekeeping, define all jargon)
- ✅ Lesson structure prioritizes clarity (3-4 concepts maximum per lesson)
- ✅ Visual aids reduce text-heavy explanations

### Technical Clarity Targets

Terms requiring definition on first use:
- **Lesson 1**: Inflection point, mainstream adoption, capability benchmark, ARR (Annual Recurring Revenue)
- **Lesson 2**: Context window, token, frontier model, MCP, composable architecture, deployment platform
- **Lesson 3**: Autonomous agent, licensing (open vs. proprietary), Apache 2.0, context window, subagent
- **Lesson 4**: TDD (Test-Driven Development), ADR (Architecture Decision Record), PR (Pull Request), vibe coding, SDD

### Risk Mitigation (From Spec Risk Analysis)

**Risk 1 (Information Overload)**: Mitigated by 4-lesson structure, visual aids, progressive disclosure
**Risk 2 (Tool Obsolescence)**: Mitigated by focusing on enduring principles (three-layer stack, MCP, selection criteria)
**Risk 3 (Readers Skipping)**: Mitigated by strong hook (ICPC), "Why This Matters" boxes, clear Chapter 3 preview
**Risk 4 (Skepticism)**: Mitigated by evidence-first approach, acknowledging past hype cycles, balanced perspective
**Risk 5 (Visual Accessibility)**: Mitigated by alt text mandate, high contrast requirement, text fallbacks

### Visual Asset Strategy

**Decision**: Use placeholders for initial lesson writing; create actual visuals in separate design phase

**Rationale**:
- Allows content writing to proceed immediately without blocking on visual design
- Placeholder text descriptions serve triple purpose: placeholder content, design specifications, and alt text
- Enables parallel workflows: content team can write lessons while design team plans visual assets
- Reduces iteration risk: finalize content first, then create visuals to match approved narrative
- Comparison tables (Lessons 3-4) can be implemented as functional markdown tables immediately

**Implementation**:
- Standardized placeholder format specified in Visual Placeholder Guidelines section
- 9 visual assets identified with comprehensive specifications
- Comparison tables will be functional markdown (not graphical) in initial version
- Visual creation phase documented as future step (can run parallel to other chapters)

**Benefits**:
- ✅ No blocking dependencies on visual design resources
- ✅ Content can be validated and approved before visual investment
- ✅ Placeholder descriptions ensure readers understand concepts even without graphics
- ✅ Visual specifications embedded in placeholders guide future design work

---

**Plan Status**: ✅ Ready for task generation (`/sp.tasks`) and lesson writing (lesson-writer subagent)
