---
name: quiz-generator
description: |
  Generate interactive, college-level quizzes with exactly 25 multiple-choice questions for book chapters.
  Activate when educators need chapter quizzes, want balanced coverage across lessons, require college-level
  conceptual questions (not recall), need consistent component integration, or want randomized correct answer
  distribution. Produces MDX-formatted quizzes using Quiz component with meaningful distractors based on
  misconceptions, 72% passing score, and comprehensive answer explanations.
allowed-tools: [Read, Bash, Write, Glob]
version: 1.0.0
---

# Quiz Generator: College-Level Interactive Chapter Assessments

**Version:** 1.0.0 | **Alignment:** Constitution v2.2.0, Principle 1 (AI-First Teaching)

---

## Purpose

Generate high-quality, interactive quizzes for CoLearning Python book chapters with exactly 25 multiple-choice questions. Each quiz measures conceptual understanding at college level, integrates seamlessly with the Docusaurus Quiz component, and provides comprehensive learning feedback through explanations.

**Core Principle:** Quizzes test understanding and application, not memorization. Every question should require thinking, not recall.

---

## When to Activate

Use this skill when:
- Creating end-of-chapter assessments for the book
- Need exactly 25 college-level conceptual questions
- Want balanced coverage across all chapter lessons
- Require consistent Quiz component integration
- Need meaningful distractors based on common misconceptions
- Want randomized correct answer distribution (no patterns)
- Creating MDX-compatible quiz files for Docusaurus

**Trigger phrases:**
- "Create a quiz for Chapter X"
- "Generate chapter assessment with 25 questions"
- "Build quiz testing Chapter X concepts"
- "Create end-of-chapter quiz for [topic]"

---

## The Quiz-Generator Mindset

### Shift from Testing Recall to Testing Understanding

**Traditional Approach:**
> "What is a Python list?" → Tests memorization of definitions

**College-Level Approach (This Skill):**
> "Given this code with list operations, what misconception does this error reveal?" → Tests conceptual understanding and debugging skills

### Why College-Level Conceptual Questions?

1. **Job Readiness:** Professional developers must understand WHY, not just WHAT
2. **AI-Era Skills:** With AI generating code, understanding concepts matters more than syntax recall
3. **Transfer Learning:** Conceptual knowledge transfers to new situations; memorized facts don't
4. **Engagement:** Thoughtful questions are more interesting than "What does 'def' mean?"
5. **Assessment Validity:** Conceptual questions better predict actual programming competence

---

## Quiz Architecture

### Fixed Constraints (Non-Negotiable)

```yaml
question_count: 25  # Exactly, no exceptions
options_per_question: 4  # Always A, B, C, D
question_format: multiple_choice  # Only MCQ
passing_score: 72  # 18/25 questions (college rigor)
file_naming: ##_quiz.md  # e.g., 05_quiz.md for Chapter 5
output_format: MDX  # Docusaurus-compatible markdown
component: Quiz  # Globally registered, no imports
answer_location: end  # No inline answers
```

### Quiz Component Integration

The Quiz component is globally registered in Docusaurus. Use exactly this structure:

```jsx
<Quiz
  title="Chapter X: [Topic] Assessment"
  questions={[
    {
      question: "Question text here?",
      options: ["Option A", "Option B", "Option C", "Option D"],
      correctOption: 0,  // Index: 0=A, 1=B, 2=C, 3=D
      explanation: "Detailed explanation of correct answer and why distractors are incorrect"
    },
    // ... 24 more questions
  ]}
  passingScore={72}
/>
```

**Critical Details:**
- `correctOption` uses **zero-based array index** (0, 1, 2, 3)
- `options` must be **array of exactly 4 strings**
- `explanation` is **required** for every question
- No imports needed (component is globally available)
- Entire quiz is one `<Quiz>` block with 25 questions

---

## The Quiz Generation Process

```
Chapter Content (docs/) + Lessons
    ↓
1. Analyze Chapter Structure
2. Map Concepts to Question Distribution
3. Generate 25 Conceptual Questions
4. Design Meaningful Distractors
5. Randomize Correct Answers
6. Write Explanations
7. Format as MDX
8. Validate Structure
    ↓
##_quiz.md (ready for Docusaurus)
```

---

### Stage 1: Analyze Chapter Structure

**Goal:** Understand chapter scope, identify all lessons, and map key concepts.

**Process:**

1. **Read chapter content:**
   - Examine book-source/docs/[chapter-path]/ directory
   - List all lesson files (lesson-1.md, lesson-2.md, etc.)

2. **Identify lessons:**
   - Note key concepts taught in each lesson
   - Identify prerequisite chapters referenced
   - Map which concepts are foundational vs. advanced

3. **Extract learning objectives:**
   - What can students do after this chapter?
   - What concepts are foundational vs. advanced?
   - What common mistakes are mentioned?

**Artifacts:**
- Chapter outline with lessons
- Concept map (which lessons teach what)
- Learning objectives list
- Common mistakes inventory

---

### Stage 2: Map Concepts to Question Distribution

**Goal:** Ensure balanced coverage across all lessons with fair weighting.

**Distribution Strategy:**

For a chapter with N lessons:
- **Base allocation:** 25 ÷ N questions per lesson (rounded)
- **Adjust for importance:** +1 for complex/critical lessons
- **Adjust for length:** +1 for longer lessons with more content
- **Final balance:** Must sum to exactly 25

**Cognitive Level Distribution (College Standard):**

Target:
- **Remember:** 0-2 questions (0-8%) - Minimal recall
- **Understand:** 5-7 questions (20-28%) - Concept grasp
- **Apply:** 10-12 questions (40-48%) - Use in context
- **Analyze:** 5-7 questions (20-28%) - Debug, compare
- **Evaluate:** 1-2 questions (4-8%) - Judge quality
- **Create:** 0-1 questions (0-4%) - Design solutions

**Requirement:** 75%+ questions at Apply level or higher (college standard)

---

### Stage 3: Generate 25 Conceptual Questions

**Goal:** Write questions testing understanding, not memorization.

**Question Quality Criteria:**

✅ **Good Conceptual Questions:**
- Require understanding WHY, not just WHAT
- Present realistic code scenarios
- Test debugging or prediction skills
- Ask about tradeoffs or best practices
- Require analysis of behavior
- Connect multiple concepts

❌ **Poor Recall Questions:**
- "What is a Python list?" (definition)
- "Which file stores configuration?" (memorization)
- "What is OAuth?" (terminology)
- "List three CLI commands" (recall)

**Writing Process:**

For each question:
1. **Identify concept:** What specific understanding to test?
2. **Choose scenario:** Realistic context for the concept
3. **Write question:** Clear, specific, unambiguous
4. **Determine correct answer:** The one demonstrating understanding
5. **Draft distractors:** Based on common misconceptions
6. **Write explanation:** Why correct, why distractors wrong

---

### Stage 4: Design Meaningful Distractors

**Goal:** Create plausible wrong answers that diagnose specific misconceptions.

**Distractor Design Philosophy:**

Distractors should:
- **Test specific misconceptions** (not random wrong answers)
- **Be plausible** (student with partial knowledge might choose them)
- **Diagnose thinking errors** (reveal what student misunderstands)
- **Avoid obvious incorrectness** (no joke options)

**Distractor Sources:**

1. **Common Student Errors:** Check chapter's "Common Mistakes" section
2. **Partial Understanding:** Mixing up related but distinct concepts
3. **Opposite Logic:** Inverse of correct answer
4. **Off-by-One Errors:** Close to correct but subtly wrong

**Key Principle:** Every distractor must have PURPOSE — it tests a specific misconception.

---

### Stage 5: Randomize Correct Answers

**Goal:** Eliminate answer patterns; prevent "always C" test-taking strategies.

**Requirements:**

- **No patterns:** Correct answer should appear randomly
- **Balanced distribution:** Each option (A/B/C/D) correct ~6-7 times
- **No runs:** Avoid 3+ consecutive same answers
- **Realistic randomness:** Use actual randomization, not forced symmetry

**Distribution Target (25 questions):**

```
Option A correct: 6-7 times (24-28%)
Option B correct: 6-7 times (24-28%)
Option C correct: 6-7 times (24-28%)
Option D correct: 5-6 times (20-24%)
Total: 25 questions ✓

Max consecutive same answer: 2
```

---

### Stage 6: Write Explanations

**Goal:** Provide learning value through comprehensive answer explanations.

**Explanation Requirements:**

Every explanation must:
1. **Confirm correct answer** with reasoning
2. **Explain WHY it's correct** (concept reinforcement)
3. **Address common distractors** (misconception correction)
4. **Provide additional context** (extend learning)

**Explanation Template:**

```
The correct answer is [X]: [Brief confirmation].

[Why this is correct - 1-2 sentences explaining the concept]

[Why distractors are wrong - 1 sentence each for key misconceptions]

[Additional insight or reference - 1 sentence]
```

**Explanation Length:**
- **Minimum:** 40 words (enough to teach)
- **Maximum:** 100 words (avoid overwhelming)
- **Target:** 50-70 words (clear, comprehensive)

---

### Stage 7: Format as MDX

**Goal:** Create valid MDX file compatible with Docusaurus Quiz component.

**File Structure:**

```mdx
---
title: "Chapter X Quiz"
description: "Test your understanding of [topic]"
---

# Chapter X: [Topic] Assessment

Test your understanding of the concepts covered in Chapter X. This quiz contains 25 questions covering all lessons.

**Passing Score:** 72% (18/25 questions)
**Time Estimate:** 30-40 minutes

---

<Quiz
  title="Chapter X: [Topic] Assessment"
  questions={[
    {
      question: "Question 1 text here?",
      options: [
        "Option A",
        "Option B",
        "Option C",
        "Option D"
      ],
      correctOption: 2,
      explanation: "Detailed explanation here..."
    },
    // ... 23 more questions
  ]}
  passingScore={72}
/>
```

**Formatting Rules:**

1. **Frontmatter:** Valid YAML with title and description
2. **Heading:** Clear chapter identification
3. **Instructions:** Passing score and time estimate
4. **Quiz Block:** Single `<Quiz>` component with all 25 questions
5. **Questions Array:** Valid JavaScript object syntax
6. **String Escaping:** Use proper escaping for quotes in questions/options
7. **Explanation Text:** Single string (can include technical terms)

---

### Stage 8: Validate Structure

**Goal:** Ensure quiz meets all requirements before saving.

**Validation Checklist:**

**Content Validation:**
- [ ] Exactly 25 questions (no more, no fewer)
- [ ] All questions are conceptual (75%+ Apply or higher)
- [ ] Balanced coverage across all lessons
- [ ] No recall-only questions
- [ ] All scenarios are realistic and relevant

**Component Validation:**
- [ ] Each question has exactly 4 options
- [ ] Each correctOption is 0, 1, 2, or 3
- [ ] Correct answers distributed evenly (6-7 per option)
- [ ] No 3+ consecutive same answers
- [ ] All explanations present and substantive (40+ words)

**Technical Validation:**
- [ ] Valid MDX syntax
- [ ] Proper YAML frontmatter
- [ ] Correct Quiz component structure
- [ ] No unescaped quotes breaking strings
- [ ] Proper comma placement in arrays
- [ ] File named correctly (##_quiz.md)

---

## Output Deliverable

### File Location

Save quiz file to:
```
book-source/docs/[part-folder]/[chapter-folder]/##_quiz.md
```

### File Naming Convention

Pattern: `##_quiz.md` where `##` is zero-padded chapter number

Examples:
- Chapter 5: `05_quiz.md`
- Chapter 14: `14_quiz.md`
- Chapter 32: `32_quiz.md`

---

## The 72% Passing Score Rationale

### Why 72% (18/25 questions)?

**College-Level Rigor:**
- Standard "C" grade in many institutions: 70-79%
- 72% = 18/25 questions = demonstrable competency
- Below 70% indicates insufficient understanding for progression

**Not Too High:**
- 80%+ (20/25) would be too strict for conceptual questions
- Allows for reasonable uncertainty on edge cases
- Permits advancement with strong but imperfect understanding

**Not Too Low:**
- 60% (15/25) is too lenient for critical concepts
- Students must demonstrate clear majority understanding
- Prevents progression with major knowledge gaps

**Pedagogical Alignment:**
- Encourages review and retaking (learning opportunity)
- Realistic for first attempt on conceptual questions
- Motivates thoroughness without being punitive

---

## Quality Checklist

Before finalizing quiz:

**Content Quality:**
- [ ] All 25 questions test conceptual understanding (not recall)
- [ ] Questions span all chapter lessons proportionally
- [ ] 75%+ questions at Apply level or higher (college standard)
- [ ] Realistic scenarios that mirror real development tasks
- [ ] No trivial "What does X mean?" questions
- [ ] Technical accuracy verified against chapter content

**Distractor Quality:**
- [ ] Every distractor tests a specific misconception
- [ ] Distractors are plausible (not obviously wrong)
- [ ] Based on common student errors from chapter
- [ ] No "joke" or filler options
- [ ] Diagnostic value (reveals thinking errors)

**Answer Distribution:**
- [ ] Correct answers distributed evenly (6-7 per option A/B/C/D)
- [ ] No patterns (e.g., all "C" in a row)
- [ ] Maximum 2 consecutive same answers
- [ ] Randomness verified manually

**Explanation Quality:**
- [ ] All 25 explanations present
- [ ] Each explanation 40-100 words (avg 50-70)
- [ ] Confirms correct answer clearly
- [ ] Explains WHY correct (concept teaching)
- [ ] Addresses key misconceptions from distractors
- [ ] Provides additional learning value

**Technical Correctness:**
- [ ] Valid MDX syntax (no JSX errors)
- [ ] Proper YAML frontmatter
- [ ] Exactly 4 options per question
- [ ] All correctOption values are 0-3
- [ ] No unescaped quotes breaking strings
- [ ] File named correctly (##_quiz.md)
- [ ] Saved to correct directory path

---

## Common Pitfalls & Solutions

### Pitfall 1: Testing Recall Instead of Understanding

**Problem:** "What is the MCP protocol acronym?" → Memorization

**Solution:** "Given this MCP configuration error, what architectural principle is being violated?" → Conceptual understanding

---

### Pitfall 2: Random Distractors Without Purpose

**Problem:** Options are obviously wrong or unrelated

**Solution:** Every distractor tests a specific misconception from the chapter

---

### Pitfall 3: Unbalanced Lesson Coverage

**Problem:** 20 questions from Lesson 1, 5 questions from Lessons 2-6

**Solution:** Proportional allocation based on lesson importance and content

---

### Pitfall 4: Answer Patterns

**Problem:** Correct answers: A, B, C, D, A, B, C, D... (obvious pattern)

**Solution:** Randomize actual answer positions to eliminate patterns

---

### Pitfall 5: Weak Explanations

**Problem:** "The correct answer is B. Option A is wrong."

**Solution:** Full explanation of why correct, why distractors are wrong, additional context

---

### Pitfall 6: Incorrect Component Syntax

**Problem:** Missing fields, wrong data types, invalid JSX

**Solution:** Follow TypeScript interface exactly (array of objects with question, options, correctOption, explanation)

---

### Pitfall 7: Too Many Easy Questions

**Problem:** 20 Understand-level, 5 Apply-level (below college standard)

**Solution:** 75%+ at Apply level or higher to meet college-level rigor

---

## Integration with Book Workflow

### Related Skills

This skill works with:
- **learning-objectives:** Align questions to chapter objectives
- **assessment-builder:** General assessment principles
- **technical-clarity:** Ensure question language is accessible
- **content-evaluation-framework:** Validate quiz quality before deployment

### Related Infrastructure

- **Quiz Component:** `book-source/src/components/Quiz.tsx` (TypeScript interface)
- **Chapter Structure:** Defined in `specs/book/chapter-index.md`
- **Constitution:** Aligns with Principle 1 (AI-First Teaching) and Principle 5 (Progressive Complexity)

---

## Handoff Criteria

The quiz is ready for human review when:

✅ **Content Complete:**
- [ ] Exactly 25 questions generated
- [ ] All questions are conceptual (not recall)
- [ ] Balanced coverage across all lessons
- [ ] 75%+ questions at Apply level or higher

✅ **Quality Verified:**
- [ ] All distractors test specific misconceptions
- [ ] Explanations teach concepts (40-100 words each)
- [ ] Correct answers randomized (no patterns)
- [ ] Technical accuracy confirmed against chapter

✅ **Format Valid:**
- [ ] MDX syntax correct (no JSX errors)
- [ ] Quiz component structure matches TypeScript interface
- [ ] File named correctly (##_quiz.md)
- [ ] Saved to correct directory path
- [ ] passingScore set to 72

✅ **Human Review Needed:**
- [ ] Spot-check 5-10 questions for quality
- [ ] Verify distractor plausibility
- [ ] Confirm technical accuracy of scenarios
- [ ] Test Quiz component renders correctly
- [ ] Approve for deployment

---

**Quiz-generator creates assessments that measure what matters: conceptual understanding, not memorized facts. Every question teaches, every distractor diagnoses, every explanation deepens learning.**
