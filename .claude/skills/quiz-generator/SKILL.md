---
name: quiz-generator
description: |
  Generate college-level MCQ quizzes (5-10 questions) using interactive Quiz component. Produces MDX files
  with conceptual questions, meaningful distractors, and randomized correct answers. Quizzes test understanding
  through the globally-registered Quiz component with built-in features: progress tracking, answer validation,
  explanations, results page, and theme support. Follows ##_chapter_##_quiz.mdx naming convention.
allowed-tools: [Read, Bash, Write, Glob]
version: 2.0.0
---

# Quiz Generator: College-Level Interactive Chapter Assessments

**Version:** 2.0.0 | **Alignment:** Constitution v2.2.0, Principle 1 (AI-First Teaching)

---

## Purpose

Generate high-quality, college-level MCQ quizzes (5-10 questions) using the globally-registered Quiz component. Each quiz measures conceptual understanding with built-in interactive features including progress tracking, answer validation, instant explanations, and results scoring. The Quiz component automatically handles anti-cheating measures, theme switching, and mobile responsiveness.

**Core Principles:**
- Test understanding and application, not memorization
- Leverage Quiz component's built-in validation and anti-cheating features
- Randomize correct answer distribution across options (0-3 indices)
- Provide meaningful explanations for each answer
- Comprehensive coverage of chapter material (not comprehensive = fewer, focused questions)

---

## When to Activate

Use this skill when:
- Creating end-of-chapter assessments using the Quiz component
- Need college-level conceptual questions (5-10 focused questions)
- Want interactive quiz with built-in scoring and feedback
- Require randomized correct answers with consistent distribution
- Need instant explanations shown after answer selection
- Want fully responsive, accessible quiz with light/dark theme support
- Creating MDX-compatible quiz files using `<Quiz />` component

**Trigger phrases:**
- "Create a quiz for Chapter X using the Quiz component"
- "Generate interactive chapter assessment with 5-10 questions"
- "Build college-level quiz using Quiz component with explanations"
- "Create focused chapter quiz with instant feedback"

---

## Key Concepts

### College-Level Conceptual Questions

**Shift from Recall to Understanding:**

❌ **Recall (Avoid):**
> "What is a Python list?" → Tests memorization

✅ **Conceptual (Target):**
> "Given this code with list operations, what misconception does this error reveal?" → Tests understanding

**Why College-Level?**
1. Job readiness: Professional developers need to understand WHY, not just WHAT
2. AI-era skills: With AI generating code, understanding concepts matters more than syntax recall
3. Transfer learning: Conceptual knowledge transfers; memorized facts don't
4. Better assessment: Conceptual questions predict programming competence

**Cognitive Level Target:**
- 75%+ questions at Apply level or higher
- Focus on debugging, prediction, analysis (not recall)

---

### Quiz Component Architecture

**Built-in Features (No Manual Implementation Needed):**
- ✅ Progress bar showing completion percentage
- ✅ Question navigation (Back/Next buttons + number dots)
- ✅ Answer counter (X/Y answered)
- ✅ Validation: Can't submit until all answered
- ✅ Results page with score and review option
- ✅ Color-coded feedback (green = correct, red = incorrect)
- ✅ Instant explanations shown after submission
- ✅ Retake button to try again
- ✅ Light/Dark theme auto-switching
- ✅ Fully responsive (mobile, tablet, desktop)

**Why Fewer Questions (5-10)?**
- Quiz component excels at interactive, focused assessments
- 5-10 questions allows deeper explanations and engagement
- Mobile-friendly (scrolling 20+ questions frustrates users)
- Better learning outcomes: focused questions > quantity
- Matches pedagogical best practices (Bloom's taxonomy levels)

---

### Answer Randomization with Quiz Component

**Requirements:**
- Correct answers distributed across 0-3 indices (not a/b/c/d)
- For 8 questions: ~2 per index (25% each)
- No obvious patterns
- Maximum 2 consecutive same answers

**Quiz Component Format:**
```javascript
{
  question: "Your question?",
  options: ["Option A", "Option B", "Option C", "Option D"],
  correctOption: 2,  // Index 0-3, NOT 1-4!
  explanation: "Why this is correct..."
}
```

**How to Randomize:**
1. Write questions first (don't worry about position)
2. After ALL questions written, shuffle correctOption values
3. Verify distribution is roughly equal
4. Ensure no 3+ consecutive same answers

📖 **Reference:** [answer-distribution.md](./references/answer-distribution.md) for verification methods

---

### Explanation Quality (Critical)

**Quiz component shows explanations immediately after submission.** This enables deeper learning than traditional quizzes:

**Good Explanations (60-150 words):**
1. **Explain WHY correct** (2-3 sentences)
2. **Address why distractors wrong** (1-2 sentences each)
3. **Add context/examples** (connections, real-world usage)

**Example:**
```javascript
explanation: "Lists are mutable (changeable) in Python, so append() modifies the original list.
This is different from strings, which are immutable—you can't change them after creation.
The add() method doesn't exist in Python (that's Java), insert() requires a position,
and push() is JavaScript. Understanding mutability is crucial for debugging variable scope issues."
```

---

## Quiz Architecture

### Fixed Constraints (Non-Negotiable)

```yaml
question_count: 5-10  # Focused assessment (5-10 questions)
options_per_question: 4  # Always exactly 4 options
question_format: multiple_choice  # Only MCQ
correct_answer_distribution: random_equal  # indices 0-3 equally distributed
passing_score: 60-70  # 60% for beginners, 70% intermediate
file_naming: ##_chapter_##_quiz.md  # e.g., 05_chapter_02_quiz.md
output_format: Markdown with Quiz component  # <Quiz {...} /> (globally registered)
component_globally_registered: true  # No imports needed
```

**CRITICAL ANTI-PATTERNS:**
- ❌ Using array indices 1-4 (use 0-3!)
- ❌ Questions that test recall instead of understanding
- ❌ Explanations without addressing why distractors are wrong
- ❌ No randomization of correctOption values
- ❌ More than 10 questions (violates component UX patterns)
- ❌ File naming like `##_quiz.md` (use `##_chapter_##_quiz.md`)

---

### File Structure

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
        addressing why distractors are wrong, and providing additional context."
    },
    {
      question: "Question 2 text?",
      options: ["Option A", "Option B", "Option C", "Option D"],
      correctOption: 0,
      explanation: "..."
    }
    // ... 6-8 more questions
  ]}
  passingScore={70}
/>
```

**Key Requirements:**
- ✅ Exactly 4 options per question (no more, no less)
- ✅ `correctOption` uses 0-3 index (NOT 1-4)
- ✅ Explanations address why each distractor is wrong
- ✅ No imports needed for `<Quiz />` (globally registered)

📖 **Reference:** [file-naming.md](./references/file-naming.md) for naming conventions

---

## The Generation Process (Overview)

```
Chapter Content → Analyze → Select Topics → Generate Questions →
Design Distractors → Randomize Answers → Write Explanations →
Format Quiz Component → Validate → ##_chapter_##_quiz.mdx
```

### 7-Stage Process Summary

1. **Analyze Chapter Structure:** Identify core concepts and learning objectives
2. **Select 5-10 Key Topics:** Choose highest-impact concepts (not comprehensive coverage)
3. **Generate Conceptual Questions:** Write understanding-focused questions (no recall)
4. **Design Meaningful Distractors:** Create distractors testing specific misconceptions
5. **Randomize Correct Answers:** Shuffle correctOption indices (0-3); verify equal distribution
6. **Write Comprehensive Explanations:** 60-150 words explaining why correct AND why each distractor is wrong
7. **Format Quiz Component:** Use `<Quiz {...} />` with all 5-10 questions in questions array

📖 **Reference:** [generation-process.md](./references/generation-process.md) for detailed stage-by-stage workflow

---

## Quality Standards

### Content Quality
- ✅ 5-10 questions (focused, high-impact assessment)
- ✅ College-level conceptual (75%+ Apply or higher)
- ✅ Realistic scenarios (debugging, prediction, analysis)
- ✅ No obvious recall questions ("What is...?")

### Answer Randomization Quality (CRITICAL)
- ✅ Correct answers evenly distributed (indices 0-3: ~25% each)
- ✅ No 3+ consecutive same correctOption values
- ✅ No patterns (not 0,1,2,3,0,1,2,3...)
- ✅ All index values (0,1,2,3) represented

### Explanation Quality
- ✅ 60-150 words each (comprehensive, not rushed)
- ✅ Explain WHY correct (2-3 sentences)
- ✅ Address why EACH distractor is wrong (1 sentence each)
- ✅ Additional context (examples, connections, misconceptions)

### Component Format Quality
- ✅ Proper JSX syntax in MDX file
- ✅ Exactly 4 options per question (no more, no less)
- ✅ correctOption uses 0-3 indices (NOT 1-4!)
- ✅ File named: `##_chapter_##_quiz.mdx`
- ✅ No imports needed (Quiz globally registered)
- ✅ passingScore property set (60-70)

📖 **Reference:** [quality-checklist.md](./references/quality-checklist.md) for complete validation criteria

---

## Common Pitfalls (Top 5)

1. **Index Confusion (CRITICAL):** Using correctOption: 1-4 instead of 0-3
   - ❌ `correctOption: 4` → References non-existent 5th option
   - ✅ `correctOption: 3` → Correct (last option, 4th item)
   - Fix: Always use 0-3 indices

2. **Testing Recall:** "What is X?" questions → Memorization
   - ❌ "What is a Python list?"
   - ✅ "Which operation modifies a list in-place?"
   - Fix: Focus on Apply/Analyze/Evaluate levels

3. **Weak Distractors:** Options that are obviously wrong
   - ❌ "Which is correct?" with options including "banana" or "xyz"
   - ✅ "Which is correct?" where all options are plausible misconceptions
   - Fix: Every distractor should test a specific misconception

4. **Missing Explanation Details:** Not addressing why distractors are wrong
   - ❌ "Lists are mutable." (only explains correct answer)
   - ✅ "Lists are mutable; strings aren't. The append() method exists, but add() doesn't (that's Java)..." (explains all options)
   - Fix: Address each distractor explicitly

5. **Answer Patterns:** Obvious distribution patterns in correctOption
   - ❌ correctOption sequence: 0,1,2,3,0,1,2,3... (repeating pattern)
   - ✅ correctOption sequence: 2,0,1,3,1,0,2,1... (random distribution)
   - Fix: Shuffle after writing; verify no patterns

📖 **Reference:** [pitfalls-and-solutions.md](./references/pitfalls-and-solutions.md) for all common mistakes

---

## File Naming Convention

### Pattern: `##_chapter_##_quiz.md`

Where:
- First `##` = sidebar_position (lesson count + 1)
- Second `##` = chapter number (zero-padded)
- Extension: `.md` (Quiz component is globally registered, no imports needed)

**Examples:**
- Chapter 2 (4 lessons): `05_chapter_02_quiz.md`
- Chapter 5 (6 lessons): `07_chapter_05_quiz.md`
- Chapter 14 (5 lessons): `06_chapter_14_quiz.md`

**Why this naming:**
- Matches lesson naming convention
- Clear chapter identification
- `.md` extension (Quiz component handles JSX rendering)
- Natural sorting places quiz at chapter end

📖 **Reference:** [file-naming.md](./references/file-naming.md) for complete guidance

---

## Integration with Book Workflow

### Related Skills
- **learning-objectives:** Align questions to chapter objectives
- **assessment-builder:** General assessment principles
- **technical-clarity:** Ensure question language is accessible
- **content-evaluation-framework:** Validate quiz quality

### Related Infrastructure
- **Constitution:** Aligns with Principle 1 (AI-First Teaching) and Principle 5 (Progressive Complexity)
- **Chapter Index:** `specs/book/chapter-index.md`

---

## Handoff Criteria

The quiz is ready for human review when:

**Content Complete:**
- [ ] 5-10 questions generated (focused, not comprehensive)
- [ ] All questions conceptual (not recall)
- [ ] 75%+ at Apply level or higher
- [ ] Each question tests a distinct concept

**Answer Randomization Verified:**
- [ ] correctOption uses 0-3 indices only (NOT 1-4)
- [ ] Correct answers evenly distributed (0-3: ~25% each)
- [ ] No 3+ consecutive same correctOption values
- [ ] No obvious patterns detected
- [ ] All 4 indices (0,1,2,3) represented in distribution

**Quality Verified:**
- [ ] Distractors test specific misconceptions
- [ ] Explanations comprehensive (60-150 words each)
- [ ] Each explanation addresses why EACH distractor is wrong
- [ ] Technical accuracy confirmed
- [ ] No recall questions ("What is...?" avoided)

**Component Format Valid:**
- [ ] Valid JSX syntax in markdown file
- [ ] Exactly 4 options per question
- [ ] Quiz component used correctly (no imports needed - globally registered)
- [ ] passingScore property set (60-70)
- [ ] File named: `##_chapter_##_quiz.md`
- [ ] File uses `.md` extension
- [ ] Saved to correct directory

**Human Review:**
- [ ] Spot-check all 5-10 questions for conceptual rigor
- [ ] Verify distractor plausibility and misconception testing
- [ ] Confirm technical accuracy
- [ ] Test Quiz component rendering in Docusaurus
- [ ] Approve for deployment

📖 **Reference:** [quality-checklist.md](./references/quality-checklist.md) for complete validation

---

## Bundled Resources

This skill includes detailed reference documentation:

- **[generation-process.md](./references/generation-process.md)** - Complete 7-stage workflow for Quiz component generation with examples
- **[answer-distribution.md](./references/answer-distribution.md)** - Randomization strategies and verification methods for correctOption indices
- **[file-naming.md](./references/file-naming.md)** - Naming conventions with examples
- **[pitfalls-and-solutions.md](./references/pitfalls-and-solutions.md)** - Common mistakes and fixes for Quiz component quizzes
- **[quality-checklist.md](./references/quality-checklist.md)** - Complete validation checklist for Quiz component format

Use `Read` tool to access references as needed during quiz generation.

---

**Quiz Generator v3.0 creates interactive assessments using the globally-registered Quiz component. Focused 5-10 question quizzes measure conceptual understanding with instant feedback. Built-in features include progress tracking, answer validation, color-coded results, explanations, retake buttons, and full theme support—no manual implementation needed.**
