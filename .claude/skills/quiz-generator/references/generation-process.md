# Quiz Generation Process - 7 Stages

This document details the complete 7-stage process for generating college-level quizzes using the globally-registered Quiz component.

---

## Process Overview

```
Chapter Content (docs/) + Lessons
    ↓
1. Analyze Chapter Structure
2. Select 5-10 Key Topics
3. Generate Conceptual Questions
4. Design Meaningful Distractors
5. Randomize Correct Answers (indices 0-3)
6. Write Comprehensive Explanations
7. Format Quiz Component
    ↓
##_chapter_##_quiz.md (with <Quiz /> component)
```

---

## Stage 1: Analyze Chapter Structure

**Goal:** Understand chapter scope, identify all lessons, and map key concepts.

**Process:**

1. **Read chapter content:**
   - Examine docs/[chapter-path]/ directory
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

## Stage 2: Select 5-10 Key Topics

**Goal:** Choose highest-impact concepts for focused assessment (not comprehensive coverage).

**Selection Strategy:**

For a chapter with N lessons, choose 5-10 questions targeting:
- **Foundational concepts:** Topics that unlock understanding of other topics
- **Complex topics:** Concepts students struggle with most
- **Application scenarios:** Real-world usage demonstrating mastery
- **Misconception-prone areas:** Topics with documented common errors

**Why 5-10 Questions (Not 20-30)?**

The Quiz component is optimized for focused, interactive assessments:
- Better user experience (no excessive scrolling on mobile)
- Deeper explanations per question (60-150 words each)
- Higher engagement (instant feedback, progress tracking)
- Better learning outcomes (focused assessment > quantity)
- Pedagogically sound (Bloom's taxonomy emphasizes depth over breadth)

**Cognitive Level Distribution (College Standard):**

Target:
- **Remember:** 0-1 questions (0-10%) - Minimal recall
- **Understand:** 1-2 questions (10-20%) - Concept grasp
- **Apply:** 3-5 questions (40-60%) - Use in context
- **Analyze:** 1-2 questions (10-20%) - Debug, compare, diagnose
- **Evaluate:** 0-1 questions (0-10%) - Judge quality, tradeoffs

**Requirement:** 75%+ questions at Apply level or higher (college standard)

---

## Stage 3: Generate Conceptual Questions

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

## Stage 4: Design Meaningful Distractors

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

## Stage 5: Randomize Correct Answers (Indices 0-3)

**Goal:** Eliminate answer patterns and prevent test-taking shortcuts.

**Requirements:**

- **No patterns:** Correct answer must appear randomly (not 0,1,2,3,0,1,2,3...)
- **Equal distribution:** Each index (0/1/2/3) correct roughly equal times
- **No runs:** Avoid 3+ consecutive same answer indices
- **True randomness:** Shuffle correctOption values after writing questions (then verify distribution)

**Distribution Targets:**

For 8 questions:
```
Index 0 correct: 2 times (25%)
Index 1 correct: 2 times (25%)
Index 2 correct: 2 times (25%)
Index 3 correct: 2 times (25%)
Max consecutive same: 2
```

For 10 questions:
```
Index 0 correct: 2-3 times (20-30%)
Index 1 correct: 2-3 times (20-30%)
Index 2 correct: 2-3 times (20-30%)
Index 3 correct: 2-3 times (20-30%)
Max consecutive same: 2
```

**How to Randomize:**
1. Write all questions with correct answer in any position (don't overthink it)
2. After writing ALL questions, identify which position is correct for each
3. Shuffle the answer indices (move correct answer randomly to 0/1/2/3)
4. Verify distribution is roughly equal
5. Ensure no 3+ consecutive same correctOption values
6. Document the randomization in the questions array

See [answer-distribution.md](./answer-distribution.md) for verification methods.

---

## Stage 6: Write Comprehensive Explanations

**Goal:** Provide learning value through detailed answer explanations shown immediately after submission.

**Explanation Requirements:**

Every explanation must:
1. **Explain WHY it's correct** - 2-3 sentences explaining the concept deeply
2. **Address why EACH distractor is wrong** - 1 sentence each for each option explaining the misconception
3. **Provide additional context** - Reference lesson, provide examples, extend learning

**Explanation Template:**

```javascript
explanation: "This is correct because [concept explanation - 2-3 sentences].
Why not the others? Option [X] [addresses misconception]. Option [Y] [addresses misconception].
Option [Z] [addresses misconception]. [Additional insight or connection to other lessons]."
```

**Explanation Length and Depth:**
- **Minimum:** 60 words (comprehensive teaching)
- **Target:** 80-120 words (thorough, educational)
- **Maximum:** 150 words (avoid overwhelming, but depth matters more than brevity)
- Explanations are shown AFTER students answer, enabling deeper learning content

**Critical Feature of Quiz Component:**
- Shows explanation immediately after student submits an answer
- Enables instant feedback and learning reinforcement
- Allows more detailed explanations than traditional quizzes
- Color-coded: green for correct, red for incorrect

---

## Stage 7: Format Quiz Component

**Goal:** Create valid markdown file with Quiz component JSX.

**File Structure:**

```markdown
---
sidebar_position: X  # e.g., 06 (lessons + 1)
title: "Chapter X: [Topic] Quiz"
---

# Chapter X: [Topic] Quiz

Brief introduction about what students should test (1-2 sentences).

<Quiz
  title="Chapter X: [Topic] Assessment"
  questions={[
    {
      question: "Question 1 text here?",
      options: [
        "Option A",
        "Option B",
        "Option C (correct)",
        "Option D"
      ],
      correctOption: 2,  // Index 0-3
      explanation: "Comprehensive explanation (60-150 words) explaining why correct,
        addressing why each distractor is wrong, and providing additional context."
    },
    {
      question: "Question 2 text?",
      options: ["Option A", "Option B", "Option C", "Option D"],
      correctOption: 0,
      explanation: "Explanation for question 2..."
    }
    // ... 6-8 more questions
  ]}
  passingScore={70}
/>
```

**Formatting Rules:**

1. **YAML Frontmatter:** sidebar_position and title (description optional)
2. **Header:** Clear chapter and topic identification
3. **Introduction:** 1-2 sentences about what to expect
4. **Quiz Component:**
   - title prop: Quiz name/description
   - questions array: Array of 5-10 question objects
   - Each question has: question, options (exactly 4), correctOption (0-3), explanation
   - passingScore prop: 60-70 (60% for beginners, 70% for intermediate)
5. **No imports needed:** Quiz component is globally registered
6. **Valid JSX syntax:** Proper JavaScript object syntax within the component

**Key Requirements:**

✅ Exactly 4 options per question
✅ correctOption uses 0-3 index (NOT 1-4!)
✅ Explanations address why each distractor is wrong
✅ No imports needed for `<Quiz />`
✅ File named: `##_chapter_##_quiz.md`

See [file-naming.md](./file-naming.md) for naming conventions.

---

## Validation Checklist

**Content Validation:**
- [ ] 5-10 questions total (focused assessment)
- [ ] All questions are conceptual (75%+ Apply or higher)
- [ ] No recall-only questions ("What is X?")
- [ ] All scenarios are realistic and relevant
- [ ] Each question tests a distinct concept

**Component Format Validation (CRITICAL):**
- [ ] Valid JSX syntax in markdown file
- [ ] Exactly 4 options per question
- [ ] correctOption uses 0-3 indices only (NOT 1-4!)
- [ ] All question objects properly formatted
- [ ] explanations address all distractors
- [ ] passingScore property set (60-70)
- [ ] No syntax errors in options array

**Answer Distribution Validation:**
- [ ] Correct answers distributed evenly across 0-3 indices
- [ ] For 8 Qs: each index correct ~2 times (25%)
- [ ] For 10 Qs: each index correct 2-3 times (20-30%)
- [ ] No patterns (e.g., 0,1,2,3,0,1,2,3...)
- [ ] No 3+ consecutive same correctOption values
- [ ] Verified manually (not assumed)

**Format Validation:**
- [ ] Valid markdown syntax
- [ ] Proper YAML frontmatter
- [ ] Quiz component properly formatted
- [ ] File named correctly: ##_chapter_##_quiz.md
- [ ] File uses `.md` extension
- [ ] Saved to correct lesson directory

See [quality-checklist.md](./quality-checklist.md) for complete validation criteria.

---

**Keywords for grep:** process, stages, workflow, generation, analyze, select, generate, design, randomize, write, format, validate, step-by-step, methodology, Quiz component
