---
name: quiz-generator
description: |
  Generate college-level MCQ quizzes (20-30 questions) with equal/random option lengths to prevent
  length-based guessing. Produces MDX quizzes with conceptual questions, meaningful distractors,
  randomly distributed answers (a/b/c/d), and answer key at quiz end. Follows ##_chapter_##_quiz.md
  naming convention.
allowed-tools: [Read, Bash, Write, Glob]
version: 2.0.0
---

# Quiz Generator: College-Level Interactive Chapter Assessments

**Version:** 2.0.0 | **Alignment:** Constitution v2.2.0, Principle 1 (AI-First Teaching)

---

## Purpose

Generate high-quality, college-level MCQ quizzes (20-30 questions) that comprehensively cover all chapter material. Each quiz measures conceptual understanding, prevents cheating through equal/random option length, randomizes correct answer positions, and places the answer key at quiz end for independent assessment.

**Core Principles:**
- Test understanding and application, not memorization
- Prevent length-based guessing (equal or random option lengths)
- Randomize correct answer distribution across a/b/c/d
- Answer key at end of quiz (not inline) for true assessment
- Comprehensive coverage of all chapter material

---

## When to Activate

Use this skill when:
- Creating end-of-chapter assessments covering all chapter material
- Need college-level conceptual questions (20-30 recommended, max 30)
- Want balanced coverage across all chapter lessons
- Need equal or randomly varied option lengths (preventing length-based guessing)
- Require randomly distributed correct answers (no patterns)
- Want answer key at quiz end (not inline) for true assessment
- Creating MDX-compatible quiz files with proper naming conventions

**Trigger phrases:**
- "Create a quiz for Chapter X covering all material"
- "Generate chapter assessment with 20-30 questions"
- "Build college-level quiz for [chapter] with answer key at end"
- "Create comprehensive chapter quiz preventing length-based guessing"

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

### Anti-Cheating Design (Critical)

**v1.0 Critical Flaw:** All correct answers were longest options → Students achieved 100% by always choosing longest option.

**v2.0 Solution:** Equal or randomly varied option lengths

**Choose ONE strategy per quiz:**

**Approach 1: Equal Length (Recommended)**
- All four options approximately same word count (±2 words)
- Example: Each option 8-10 words
- Prevents any length-based guessing

**Approach 2: Randomly Varied Length**
- Options deliberately varied: some 5 words, some 15 words
- Correct answer distributed equally across length categories
- Use when equal length creates awkward phrasing

**What NOT to Do:**
- ❌ Correct answers consistently longest
- ❌ One option 50+ words while others 5 words
- ❌ Ignoring length variation (allows shortcuts)

📖 **Reference:** [option-length-strategy.md](./references/option-length-strategy.md) for detailed implementation

---

### Answer Randomization

**Requirements:**
- Correct answers distributed evenly across a/b/c/d
- For 25 questions: ~6-7 per letter (24-28% each)
- No patterns (not a, b, c, d, a, b, c, d...)
- Maximum 2 consecutive same answers

**How to Randomize:**
1. Write questions first (don't worry about position)
2. After ALL questions written, shuffle answer positions
3. Verify distribution is roughly equal
4. Ensure no 3+ consecutive same answers

📖 **Reference:** [answer-distribution.md](./references/answer-distribution.md) for verification methods

---

### Two-Part Format (No Inline Answers)

**v1.0 Problem:** Explanations inline → Students saw answers while taking quiz

**v2.0 Solution:** Two-part format

**Part 1: Questions Section (No Explanations)**
- Display 20-30 questions without correct answer indicators
- No inline explanations
- Options at equal or random length

**Part 2: Answer Key Section (At Quiz End)**
- Comprehensive answer key with explanations
- Shown AFTER students complete quiz
- 60-150 words per explanation

---

## Quiz Architecture

### Fixed Constraints (Non-Negotiable)

```yaml
question_count: 20-30  # Flexible for comprehensive coverage (max 30)
options_per_question: 4  # Always a, b, c, d
option_length_strategy: equal_or_random  # CRITICAL: Prevent length-based guessing
question_format: multiple_choice  # Only MCQ
correct_answer_distribution: random_equal  # a/b/c/d equally distributed
answer_key_location: end_of_quiz  # NOT inline
passing_score: 72  # ~72% (18/25 or 21/30)
file_naming: ##_chapter_##_quiz.md  # e.g., 05_chapter_02_quiz.md
output_format: MDX  # Plain markdown with answer key section
```

**CRITICAL ANTI-PATTERNS:**
- ❌ Correct answer always/usually has longest option
- ❌ Inline answer explanations
- ❌ Obvious patterns in correct answers
- ❌ Options of vastly different lengths
- ❌ Exactly 25 questions (be flexible: 20-30)
- ❌ File naming like `##_quiz.md` (use `##_chapter_##_quiz.md`)

---

### File Structure

```markdown
---
title: "Chapter X: [Topic] Quiz"
description: "College-level assessment covering all material from Chapter X"
---

# Chapter X: [Topic] Quiz

[Instructions about quiz purpose and expected time]

---

## Questions

1. Question text here?
   a) Option A (similar length)
   b) Option B (similar length)
   c) Option C (similar length)
   d) Option D (similar length)

2. Another question?
   a) Option A
   b) Option B
   c) Option C
   d) Option D

[... 18-28 more questions ...]

---

## Answer Key

**1.** Correct answer: **a**

[Comprehensive explanation: why correct, why others wrong, additional context - 60-150 words]

**2.** Correct answer: **c**

[Comprehensive explanation for question 2]

[... all remaining answers ...]
```

📖 **Reference:** [file-naming.md](./references/file-naming.md) for naming conventions

---

## The Generation Process (Overview)

```
Chapter Content → Analyze → Map Concepts → Generate Questions →
Design Distractors → Randomize Answers → Write Explanations →
Format MDX → Validate → ##_chapter_##_quiz.md
```

### 8-Stage Process Summary

1. **Analyze Chapter Structure:** Identify lessons, concepts, learning objectives
2. **Map Concepts to Question Distribution:** Allocate questions proportionally across lessons
3. **Generate 20-30 Conceptual Questions:** Write understanding-focused questions
4. **Design Meaningful Distractors:** Create distractors testing specific misconceptions with equal/random lengths
5. **Randomize Correct Answers:** Shuffle positions; verify even distribution (a/b/c/d)
6. **Write Comprehensive Explanations:** 60-150 words each explaining why correct/wrong
7. **Format as MDX:** Two-part structure (questions + answer key)
8. **Validate Structure:** Check all requirements before saving

📖 **Reference:** [generation-process.md](./references/generation-process.md) for detailed stage-by-stage workflow

---

## Quality Standards

### Content Quality
- ✅ 20-30 questions (comprehensive coverage of ALL material)
- ✅ College-level conceptual (75%+ Apply or higher)
- ✅ Realistic scenarios (debugging, prediction, analysis)
- ✅ Balanced across all lessons (no omissions)

### Anti-Cheating Quality (CRITICAL)
- ✅ Equal or random option lengths (ONE strategy consistently applied)
- ✅ Longest option ≠ always correct (manually verified)
- ✅ Correct answers evenly distributed (a/b/c/d: ~25% each)
- ✅ No 3+ consecutive same answers
- ✅ Questions/answers separated (no inline explanations)

### Explanation Quality
- ✅ 60-150 words each (comprehensive, not rushed)
- ✅ Explain WHY correct (2-3 sentences)
- ✅ Address why distractors wrong (1-2 sentences each)
- ✅ Additional context (examples, connections)

### Format Quality
- ✅ Plain markdown (no JSX)
- ✅ Two-part structure (questions + answer key)
- ✅ File named: `##_chapter_##_quiz.md`
- ✅ Correct answer format: **Correct answer: [a/b/c/d]** (bold)

📖 **Reference:** [quality-checklist.md](./references/quality-checklist.md) for complete validation criteria

---

## Common Pitfalls (Top 5)

1. **Length-Based Guessing:** All correct answers longest → Students guess without learning
   - Fix: Equal or random lengths; verify manually

2. **Inline Explanations:** Answers visible during quiz → Defeats assessment
   - Fix: Answer key section AFTER quiz (separated by `---`)

3. **Testing Recall:** "What is X?" questions → Memorization
   - Fix: "Why does X fail here?" → Understanding

4. **Random Distractors:** Joke options → No diagnostic value
   - Fix: Every distractor tests specific misconception

5. **No Validation:** Assume lengths equal → Patterns emerge
   - Fix: Count words manually; verify distributions

📖 **Reference:** [pitfalls-and-solutions.md](./references/pitfalls-and-solutions.md) for all 10 common mistakes

---

## File Naming Convention

### Pattern: `##_chapter_##_quiz.md`

Where:
- First `##` = sidebar_position (lesson count + 1)
- Second `##` = chapter number (zero-padded)

**Examples:**
- Chapter 2 (4 lessons): `05_chapter_02_quiz.md`
- Chapter 5 (6 lessons): `07_chapter_05_quiz.md`
- Chapter 14 (5 lessons): `06_chapter_14_quiz.md`

**Why this naming:**
- Matches lesson naming convention
- Clear chapter identification
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
- [ ] 20-30 questions generated
- [ ] ALL major topics covered
- [ ] All questions conceptual (not recall)
- [ ] 75%+ at Apply level or higher

**Anti-Cheating Verified:**
- [ ] Option lengths equal (±2) OR deliberately random (consistent strategy)
- [ ] Word counts verified for all questions
- [ ] Longest option ≠ correct answer pattern
- [ ] Correct answers evenly distributed (a/b/c/d)
- [ ] No 3+ consecutive same answers

**Quality Verified:**
- [ ] Distractors test specific misconceptions
- [ ] Explanations comprehensive (60-150 words each)
- [ ] Technical accuracy confirmed

**Format Valid:**
- [ ] Plain markdown (no JSX)
- [ ] Questions SEPARATE from answer key
- [ ] File named: `##_chapter_##_quiz.md`
- [ ] Saved to correct directory

**Human Review:**
- [ ] Spot-check 5-10 questions for option length
- [ ] Verify distractor plausibility
- [ ] Confirm technical accuracy
- [ ] Approve for deployment

📖 **Reference:** [quality-checklist.md](./references/quality-checklist.md) for complete validation

---

## Bundled Resources

This skill includes detailed reference documentation:

- **[generation-process.md](./references/generation-process.md)** - Complete 8-stage workflow with examples
- **[option-length-strategy.md](./references/option-length-strategy.md)** - Equal vs. random approaches; anti-cheating measures
- **[answer-distribution.md](./references/answer-distribution.md)** - Randomization and verification methods
- **[file-naming.md](./references/file-naming.md)** - Naming conventions with examples
- **[pitfalls-and-solutions.md](./references/pitfalls-and-solutions.md)** - 10 common mistakes and fixes
- **[quality-checklist.md](./references/quality-checklist.md)** - Complete validation checklist

Use `Read` tool to access references as needed during quiz generation.

---

**Quiz Generator v2.0 creates assessments that measure what matters: conceptual understanding without cheating shortcuts. Options prevent length-based guessing, answers are randomized, assessment is true (not inline answers), and every explanation deepens learning.**
