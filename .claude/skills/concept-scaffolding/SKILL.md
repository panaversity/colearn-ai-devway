---
name: concept-scaffolding
description: |
  Breaks down complex programming concepts into progressive learning steps with cognitive load management.
  Activate when educators need to teach advanced topics incrementally, explain how to introduce
  difficult concepts progressively, or need guidance on managing learner cognitive load. Applies
  Cognitive Load Theory and scaffolding strategies to create 3-7 step learning progressions.
  Use for concepts like: object-oriented programming, decorators, async/await, metaclasses,
  comprehensions, generators, context managers, or any Python feature requiring prerequisite knowledge.
allowed-tools: [Read, Bash, Write]
---

## Purpose

The concept-scaffolding skill helps educators break down complex Python concepts into manageable, progressive learning steps that respect cognitive load limitations. This skill applies evidence-based strategies from Cognitive Load Theory and scaffolding research to create effective learning progressions.

## When to Activate

Use this skill when:
- An educator needs to teach a complex Python concept incrementally
- Planning how to introduce advanced topics to learners
- A concept has multiple prerequisite dependencies
- Learners are struggling with cognitive overload
- Designing a progression from simple to complex understanding
- Creating worked examples with fading support
- Breaking down topics like: OOP, decorators, async/await, metaclasses, closures, generators

## Inputs

Required:
- **Concept name**: The complex Python concept to scaffold (e.g., "Python decorators")
- **Target audience**: beginner | intermediate | advanced

Optional:
- **Known prerequisites**: Concepts the learner already understands
- **Learning context**: classroom, self-paced, bootcamp, etc.
- **Time constraints**: Available instructional time

## Process

### Step 1: Understand the Concept Complexity

Analyze the target concept to identify:
- Core sub-concepts that must be understood
- Prerequisite knowledge required
- Common misconceptions or difficulty points
- Intrinsic cognitive load (inherent complexity)

### Step 2: Load Cognitive Load Theory Reference

Read the cognitive load theory reference for guidance:

```bash
Read reference/cognitive-load-theory.md
```

Key considerations:
- Working memory can hold 7±2 chunks
- Beginners: max 2 new concepts per step
- Intermediate: max 3 new concepts per step
- Advanced: max 4 new concepts per step

### Step 3: Design Scaffolding Progression

Create 3-7 progressive steps following these principles:

1. **Start Simple**: Begin with the simplest case or foundational concept
2. **Build Incrementally**: Each step adds 1-3 new concepts
3. **Check Prerequisites**: Ensure each step's prerequisites are met
4. **Include Worked Examples**: Provide complete examples for each step
5. **Add Checkpoints**: Include verification questions after each step

Load scaffolding strategies reference:

```bash
Read reference/scaffolding-strategies.md
```

Apply patterns:
- Worked examples (show complete solution)
- Completion problems (partial code to finish)
- Faded guidance (progressive support reduction)
- Chunking with checkpoints

### Step 4: Create Worked Examples

For each scaffolding step, create clear worked examples:

```bash
Read reference/worked-examples.md
```

Each example should:
- Demonstrate one primary concept clearly
- Include step-by-step explanation
- Explain reasoning (why, not just what)
- Use subgoal labels
- Be runnable and correct

### Step 5: Assess Cognitive Load

Create the scaffolding plan in YAML format following the template:

```bash
Read templates/scaffolding-plan-template.yml
```

Then validate cognitive load using the assessment script:

```bash
python .claude/skills/concept-scaffolding/scripts/assess-cognitive-load.py scaffolding-plan.yml
```

The script will:
- Calculate load for each step
- Identify overload warnings
- Check prerequisite chains
- Provide recommendations

### Step 6: Refine Based on Assessment

Review assessment output and refine if:
- Any step has "high" cognitive load (consider splitting)
- More than half the steps have high load (too much too fast)
- Circular dependencies detected (prerequisite issues)
- More than 7 steps total (consider consolidating)

### Step 7: Document Final Scaffolding Plan

Output the complete scaffolding plan with:
- Clear step titles and descriptions
- Worked examples for each step
- Checkpoint questions
- Cognitive load assessment
- Time estimates
- Prerequisites clearly stated

## Output Format

Provide scaffolding plan as structured markdown or YAML:

```markdown
# Scaffolding Plan: [Concept Name]

**Target Audience**: [beginner/intermediate/advanced]
**Total Steps**: [3-7]
**Estimated Time**: [X minutes]

## Prerequisite Knowledge
- [Concept 1]
- [Concept 2]
- [...]

## Step 1: [Title]

**New Concepts**: [List]
**Cognitive Load**: [low/medium/high]
**Time**: [X minutes]

### Explanation
[How this step builds toward target concept]

### Worked Example
```python
[Complete, runnable code with comments]
```

### Checkpoint
[Verification question or task]

## Step 2: [Title]
[Same structure...]

[Continue for all steps...]

## Final Integration
[How learner synthesizes all steps to understand complete concept]

## Cognitive Load Analysis
- **Overall Load**: [low/medium/high]
- **Warnings**: [Any overload concerns]
- **Recommendations**: [Suggestions for improvement]
```

## Examples

### Example 1: Scaffolding Python Decorators

**Input**: "How do I teach Python decorators to intermediate learners?"

**Process**:
1. Identify prerequisites: functions, closures, higher-order functions
2. Design 5-step progression:
   - Step 1: Functions as objects (can be assigned to variables)
   - Step 2: Functions returning functions
   - Step 3: Functions taking functions as arguments (higher-order)
   - Step 4: Simple decorator without arguments
   - Step 5: Decorators with arguments
3. Create worked examples for each step
4. Add checkpoints to verify understanding
5. Assess cognitive load (intermediate learners, 3 concepts max per step)

**Output**: Structured scaffolding plan with 5 steps, worked examples, checkpoints, and cognitive load warnings.

---

### Example 2: Scaffolding Async/Await

**Input**: "Break down async/await for beginners who understand functions and loops"

**Process**:
1. Identify high intrinsic load (concurrency is conceptually difficult)
2. Design 7-step progression:
   - Step 1: Synchronous execution review (baseline)
   - Step 2: Concept of "waiting" in code
   - Step 3: Basic async function definition
   - Step 4: Using await with async functions
   - Step 5: Running async functions with asyncio.run()
   - Step 6: Multiple async operations
   - Step 7: Error handling in async code
3. Use heavy scaffolding (worked examples, analogies)
4. Assess load (beginners, max 2 concepts per step)

**Output**: 7-step plan with extensive worked examples, real-world analogies, and frequent checkpoints.

---

### Example 3: Reviewing Existing Scaffolding

**Input**: "Is this scaffolding plan for list comprehensions effective?"
[Educator provides existing plan]

**Process**:
1. Load plan into assessment script
2. Check cognitive load per step
3. Verify prerequisite chains
4. Identify missing checkpoints or worked examples
5. Provide specific recommendations

**Output**: Assessment report with warnings and actionable recommendations.

## Common Patterns

### Pattern 1: Simple → Realistic → Complex
```python
# Step 1: Simple (one concept)
def greet(name):
    return f"Hello, {name}"

# Step 2: Realistic (add common feature)
def greet(name, formal=False):
    return "Good day" if formal else f"Hello, {name}"

# Step 3: Complex (production-ready)
def greet(name: str, formal: bool = False, title: str = None) -> str:
    # [Full implementation with validation]
```

### Pattern 2: Concrete → Abstract
Start with specific, tangible examples before introducing general patterns.

### Pattern 3: Procedural → Object-Oriented
Introduce concepts procedurally first, then show OOP approach.

## Validation

Before finalizing scaffolding plan:
- [ ] Each step introduces ≤3 new concepts (≤2 for beginners)
- [ ] Total steps: 3-7
- [ ] Prerequisites explicitly stated
- [ ] Worked examples provided for each step
- [ ] Checkpoints included for verification
- [ ] Cognitive load assessed and acceptable
- [ ] Clear progression from simple to complex
- [ ] No circular dependencies in prerequisite chain

## Acceptance Checks

- [ ] Per-step verifiability: each step lists entry knowledge, single outcome, and a micro-check
- [ ] Cognitive Load Budget present for the lesson (Beginner default ≤ 5 new concepts total)

### Step snippet
```
Entry: knows lists, for-loops
Outcome: implement list comprehension with filter
Micro-check: “Write one comprehension that filters even numbers”
```

## References

Supporting documentation (loaded as needed):
- `reference/cognitive-load-theory.md` - CLT principles and load management
- `reference/scaffolding-strategies.md` - Worked examples, fading, chunking patterns
- `reference/worked-examples.md` - Effective example structure for programming

## Error Handling

If validation fails:
1. Report specific issues (e.g., "Step 3 introduces 5 concepts for beginner audience")
2. Suggest remediation (e.g., "Split step 3 into two steps")
3. Halt and require user intervention (hard failure mode)
