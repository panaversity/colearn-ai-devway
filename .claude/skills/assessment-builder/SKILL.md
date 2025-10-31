---
name: assessment-builder
description: |
  Creates assessments with varied question types (MCQ, code-completion, debugging, projects) aligned
  to learning objectives with meaningful distractors based on common misconceptions. Activate when
  educators design quizzes, exams, or tests measuring understanding; need questions at appropriate
  cognitive levels (Bloom's taxonomy); want balanced cognitive distribution (60%+ non-recall); or
  require rubrics for open-ended questions. Generates MCQs with diagnostic distractors, code-writing
  prompts, debugging challenges, and project-based assessments targeting deep understanding.
allowed-tools: [Read, Bash, Write]
---

## Purpose

The assessment-builder skill helps educators create comprehensive, balanced assessments that measure conceptual understanding (not just memorization). This skill generates varied question types, designs meaningful distractors for MCQs, aligns questions with Bloom's taxonomy levels, and provides rubrics for open-ended questions.

## When to Activate

Use this skill when:
- Educators need to create quizzes, tests, or exams
- Designing assessments aligned with learning objectives
- Creating varied question types (MCQ, code-writing, debugging, projects)
- Need meaningful distractors based on common student errors
- Want balanced cognitive distribution (not just recall questions)
- Generating rubrics for open-ended programming questions
- Evaluating existing assessments for quality and balance
- Ensuring 60%+ questions test application or higher-order thinking

## Inputs

Required:
- **Learning objectives**: What learners should be able to demonstrate
- **Concept/topic**: Python concepts to assess

Optional:
- **Number of questions**: How many questions to generate
- **Question types**: Preferred formats (MCQ, code-writing, debugging, etc.)
- **Target audience**: beginner | intermediate | advanced
- **Time limit**: Available assessment time
- **Bloom's distribution**: Desired cognitive level mix

## Process

### Step 1: Clarify Assessment Goals

Understand:
- What specific skills/knowledge to assess
- Depth of understanding required
- Format constraints (time, delivery method)
- Stakes (formative check vs. high-stakes exam)

### Step 2: Load Question Type Reference

Read question type patterns:

```bash
Read reference/question-types.md
```

Available types:
- **MCQ**: Concept recognition, decision-making
- **Code-completion**: Apply syntax, fill strategic gaps
- **Code-tracing**: Test mental execution model
- **Debugging**: Error recognition and fixing
- **Code-writing**: Implementation from specification
- **Explanation**: Test conceptual understanding
- **Code-review**: Evaluate code quality
- **Prediction**: Anticipate behavior
- **Comparison**: Distinguish approaches
- **Project**: Integrate multiple concepts

### Step 3: Load Bloom's Assessment Alignment

Read cognitive level guidelines:

```bash
Read reference/blooms-assessment-alignment.md
```

Map question types to Bloom's levels:
- **Remember** (10-15%): MCQ recall, terminology
- **Understand** (15-20%): Tracing, prediction, explanation
- **Apply** (30-40%): Code-completion, simple code-writing
- **Analyze** (20-25%): Debugging, comparison, code-review
- **Evaluate** (10-15%): Best-approach selection, trade-offs
- **Create** (5-10%): Projects, design problems

**Target**: 60%+ non-recall (Apply and higher)

### Step 4: Design Varied Question Set

Create 5-10 questions with variety:

**Example Distribution**:
```
Q1: MCQ (Understand) - Concept check
Q2: Code-tracing (Understand) - Predict output
Q3: Code-completion (Apply) - Fill strategic blank
Q4: Code-writing (Apply) - Implement function
Q5: Debugging (Analyze) - Find and fix errors
Q6: Code-review (Evaluate) - Assess quality
Q7: Project (Create) - Integrate concepts
```

Avoid: 10 identical MCQs (tests memorization, not understanding)

### Step 5: Design MCQ Distractors

For multiple-choice questions, load distractor design guide:

```bash
Read reference/distractor-design.md
```

Create meaningful distractors based on common misconceptions:

**Process**:
1. Identify correct answer
2. List common errors students make
3. Create distractor for each specific misconception
4. Ensure distractors are plausible (not obviously wrong)

**Example**:
```
Q: After this code, what does x contain?
x = [1, 2, 3]
y = x
y.append(4)

A) [1, 2, 3, 4]  ← Correct (understands references)
B) [1, 2, 3]     ← Thinks x is independent of y
C) [4]           ← Misunderstands append
D) Error         ← Thinks modification through y is invalid

Distractor Analysis:
B tests: Understanding of assignment vs. copy
C tests: Understanding of append operation
D tests: Understanding of reference semantics
```

### Step 6: Create Rubrics for Open-Ended Questions

For code-writing, projects, and explanations, load rubric guidelines:

```bash
Read reference/rubric-guidelines.md
```

Create analytic rubric with criteria:
- **Correctness** (40%): Produces correct output
- **Code Quality** (25%): Readable, well-structured
- **Efficiency** (20%): Appropriate algorithm
- **Error Handling** (10%): Edge cases
- **Style** (5%): Python best practices

Each criterion has 4 levels: excellent, good, fair, poor

Load templates:

```bash
Read templates/rubric-template.yml
```

### Step 7: Validate Cognitive Distribution

Check assessment balance using validation script:

```bash
python .claude/skills/assessment-builder/scripts/validate-assessment.py assessment.yml
```

The script checks:
- **Cognitive distribution**: 60%+ non-recall?
- **Question variety**: Multiple question types?
- **MCQ distractors**: Analysis provided?
- **Rubrics**: Present for open-ended questions?
- **Objective alignment**: Questions map to objectives?

Review output:
- **Validation score**: >80 is good, <60 needs revision
- **Issues**: Critical problems to fix
- **Warnings**: Quality improvements
- **Recommendations**: Specific suggestions

### Step 8: Refine Based on Validation

If validation identifies issues:

**Issue**: "Only 40% non-recall questions"
**Fix**: Replace 2-3 MCQ recall questions with code-writing or debugging

**Issue**: "MCQs lack distractor analysis"
**Fix**: Document what misconception each distractor tests

**Issue**: "Missing rubrics for code-writing"
**Fix**: Add rubric with correctness, quality, efficiency criteria

### Step 9: Add Answer Key and Explanations

For each question:
- **Correct answer**: What is right
- **Explanation**: Why it's correct
- **Common errors**: Why distractors are wrong
- **Grading guidance**: How to score

**Example**:
```
Q3: Write function to sum even numbers

Answer:
def sum_evens(numbers):
    return sum(num for num in numbers if num % 2 == 0)

Explanation:
- Iterates through numbers
- Filters even (num % 2 == 0)
- Sums filtered values
- Handles empty list (sum returns 0)

Common Errors:
- Forgetting to check if num % 2 == 0
- Using == instead of %= for modulo
- Not handling empty list
```

### Step 10: Package Complete Assessment

Structure assessment following template:

```bash
Read templates/assessment-template.yml
```

Include:
- **Metadata**: Title, audience, time limit, points
- **Learning objectives**: What's being assessed
- **Questions**: All with type, points, Bloom's level
- **Answer key**: Solutions and explanations
- **Rubrics**: For open-ended questions
- **Cognitive analysis**: Distribution breakdown

## Output Format

Provide assessment as structured markdown:

```markdown
# Assessment: [Title]

**Target Audience**: [beginner/intermediate/advanced]
**Time Limit**: [X minutes]
**Total Points**: [X]
**Passing Score**: [X]

## Learning Objectives Assessed

- [Objective 1]
- [Objective 2]
- [...]

## Cognitive Distribution

- Remember/Understand: X%
- Apply: X%
- Analyze/Evaluate: X%
- Create: X%

---

## Question 1 (X points) [Type: MCQ] [Bloom: Understand]

[Question text]

A) [Option]
B) [Option]
C) [Option]
D) [Option]

---

## Question 2 (X points) [Type: Code-Writing] [Bloom: Apply]

Write a function that [specification].

**Requirements**:
- [Requirement 1]
- [Requirement 2]

**Test Cases**:
1. Input: [x], Expected: [y]
2. Input: [x], Expected: [y]

---

[Continue for all questions...]

---

## Answer Key

### Question 1
**Answer**: B

**Explanation**: [Why B is correct and why A, C, D are wrong]

**Distractor Analysis**:
- A tests: [misconception]
- C tests: [misconception]
- D tests: [misconception]

### Question 2
**Solution**:
```python
[Complete correct solution]
```

## Acceptance Checks

- [ ] SpecRef present and each question maps to at least one objective ID
- [ ] Objective Coverage Matrix included (question → objective IDs, Bloom level)
- [ ] ≥ 60% non‑recall; variety of question types present
- [ ] Validation Pack attached: answer key, explanations, distractor analyses, and rubric(s)

### Objective Coverage Matrix (example)
```
Q1 → [LO-001] (Understand)
Q2 → [LO-002] (Apply)
Q3 → [LO-002, LO-003] (Analyze)
...
```

**Rubric**:

**Correctness (40 pts)**:
- Excellent (40): Works for all test cases
- Good (30): Works for standard cases
- Fair (20): Partial functionality
- Poor (10): Significant errors

**Code Quality (25 pts)**:
- Excellent (25): Clear names, good structure
- Good (19): Mostly readable
- Fair (13): Some confusion
- Poor (6): Poor quality

[Continue for all criteria...]

---

[Continue for all questions...]
```

## Examples

### Example 1: Create Balanced Assessment for Functions

**Input**: "Create 6-question assessment for Python functions (beginner level)"

**Process**:
1. Identify objectives: Define functions, use parameters, return values
2. Design variety:
   - Q1: MCQ on function syntax (Understand)
   - Q2: Trace execution (Understand)
   - Q3: Complete function (Apply)
   - Q4: Write function from spec (Apply)
   - Q5: Debug function (Analyze)
   - Q6: Mini-project combining functions (Create)
3. Create MCQ distractors based on common errors
4. Add rubric for Q4, Q6
5. Validate (check 60%+ non-recall)

**Output**: Complete 6-question assessment with answer key and rubrics

---

### Example 2: Add Distractors to Existing MCQ

**Input**: "Improve distractors for this MCQ" [provides question]

**Process**:
1. Load distractor design reference
2. Identify concept being tested
3. List common student misconceptions
4. Create diagnostic distractor for each misconception
5. Document what each distractor tests

**Output**: Improved MCQ with meaningful, plausible distractors and analysis

---

### Example 3: Validate Assessment Balance

**Input**: "Is this assessment balanced?" [provides 10-question exam]

**Process**:
1. Analyze cognitive distribution
2. Check for question variety
3. Validate MCQ distractors
4. Check for rubrics on open-ended
5. Calculate non-recall percentage
6. Provide specific recommendations

**Output**: Validation report with issues and recommendations

## Common Patterns

### Pattern 1: Formative Assessment (Quick Check)

```
3-5 questions
30% Understand (quick concept check)
50% Apply (demonstrate skill)
20% Analyze (identify errors)
15-20 minutes
```

### Pattern 2: Summative Assessment (Unit Exam)

```
10-15 questions
15% Understand
40% Apply
30% Analyze/Evaluate
15% Create (project)
60-90 minutes
```

### Pattern 3: Skills Demonstration

```
5-7 questions, mostly code-writing and projects
20% Apply (basic implementations)
40% Analyze (debugging, optimization)
40% Create (design and build)
```

## Validation Checklist

Before finalizing assessment:
- [ ] 60%+ questions test application or higher-order thinking
- [ ] Multiple question types used (not all MCQ)
- [ ] MCQs have meaningful, diagnostic distractors
- [ ] Open-ended questions have rubrics
- [ ] Questions align with learning objectives
- [ ] Clear instructions for each question
- [ ] Answer key and explanations provided
- [ ] Reasonable time allocation
- [ ] Validation score >80

## References

Supporting documentation (loaded as needed):
- `reference/question-types.md` - MCQ, code-writing, debugging, projects, etc.
- `reference/distractor-design.md` - Misconception-based distractor creation
- `reference/blooms-assessment-alignment.md` - Cognitive levels and question types
- `reference/rubric-guidelines.md` - Analytic rubric creation

## Error Handling

If validation fails:
1. Report specific issues (e.g., "Only 30% non-recall questions", "Missing rubrics")
2. Suggest remediation (e.g., "Replace 3 MCQs with code-writing questions")
3. Halt and require user intervention (hard failure mode)

Assessments must meet quality standards: balanced cognitive distribution, varied types, meaningful distractors, clear rubrics.
