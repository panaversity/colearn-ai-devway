# Quality Checklist v3.0 - Quiz Component Validation

This document provides a comprehensive checklist for validating quiz quality when using the globally-registered Quiz component.

---

## How to Use This Checklist

1. **After generating quiz:** Go through each section sequentially
2. **Check every box:** Don't skip items; each is critical
3. **Fix issues immediately:** Don't defer validation to end
4. **Re-check after fixes:** Verify fixes didn't introduce new issues

---

## Content Quality

### Question Count and Focus
- [ ] 5-10 questions total (focused assessment, not comprehensive)
- [ ] Key concepts selected for highest impact
- [ ] Balanced distribution across major topics
- [ ] No attempt at comprehensive coverage (5-10 is by design)

### Question Type and Cognitive Level
- [ ] All questions test conceptual understanding (not recall)
- [ ] 75%+ questions at Apply level or higher (college standard)
- [ ] Realistic scenarios that mirror real development tasks
- [ ] No trivial "What does X mean?" questions
- [ ] Questions require debugging, prediction, or analysis (not memorization)

### Technical Accuracy
- [ ] Technical accuracy verified against chapter content
- [ ] All code examples are syntactically correct
- [ ] Scenarios are realistic and relevant to chapter material
- [ ] Terminology matches chapter usage
- [ ] No contradictions with lesson content

---

## Quiz Component Format Quality (CRITICAL)

### Component Syntax
- [ ] Valid JSX syntax (proper JavaScript object format)
- [ ] No syntax errors in questions array
- [ ] Proper curly braces and comma placement
- [ ] Question objects properly formatted
- [ ] No missing colons or semicolons in object properties

### Question Structure
- [ ] `question` property: Clear, specific question text
- [ ] `options` property: Exactly 4 options (no more, no less)
- [ ] `correctOption` property: Uses 0-3 index (NOT 1-4!)
- [ ] `explanation` property: Present for every question

### Critical: correctOption Index Values
- [ ] ALL correctOption values are 0, 1, 2, or 3 (never 4 or higher)
- [ ] No correctOption values use letters (not "a", "b", "c", "d")
- [ ] Index 0 = first option, 1 = second, 2 = third, 3 = fourth
- [ ] Every question has exactly ONE correctOption value

### Component Props
- [ ] `title` prop: Descriptive quiz name
- [ ] `questions` prop: Array with 5-10 question objects
- [ ] `passingScore` prop: Set to 60-70 (60% for beginners, 70% for intermediate)

---

## Answer Randomization Quality (CRITICAL)

### Distribution Targets
- [ ] Correct answers distributed evenly across indices 0-3
- [ ] For 8 questions: ~2 per index (25% each)
- [ ] For 10 questions: 2-3 per index (20-30% each)
- [ ] Total adds up to expected question count

### Index Distribution Verification Table

| Index | Count | Percentage | Target (10Q) | Status |
|-------|-------|------------|--------------|--------|
| 0     | __    | __%        | 20-30%       | ☐ Pass |
| 1     | __    | __%        | 20-30%       | ☐ Pass |
| 2     | __    | __%        | 20-30%       | ☐ Pass |
| 3     | __    | __%        | 20-30%       | ☐ Pass |
| Total | __    | 100%       | 100%         | ☐ Pass |

**Fill in counts manually and verify targets.**

### Pattern Checks
- [ ] No patterns (never 0,1,2,3,0,1,2,3...)
- [ ] Maximum 2 consecutive same indices (no 3+ consecutive)
- [ ] Distribution verified manually (count each index)
- [ ] Randomness is TRUE (not forced or artificial)

### Consecutive Index Check

List correctOption sequence: __, __, __, __, __, __, __, __, __, __

- [ ] No 3+ consecutive same indices in first 5
- [ ] No 3+ consecutive same indices in last 5
- [ ] No 3+ consecutive same indices anywhere in quiz

---

## Option Design Quality

### Distractor Quality
- [ ] Every distractor tests a specific misconception
- [ ] Distractors are plausible (not obviously wrong)
- [ ] Based on common student errors from chapter
- [ ] No "joke" or filler options
- [ ] Diagnostic value (reveals thinking errors)

### Option Clarity
- [ ] All 4 options are distinct and different
- [ ] Options avoid near-duplicates or subtle variations
- [ ] Options are clear, concise, and specific
- [ ] No grammatical or spelling errors in options

---

## Explanation Quality (CRITICAL)

### Explanation Presence
- [ ] All explanations present (one per question)
- [ ] Each explanation 60-150 words (comprehensive teaching)
- [ ] Explanations are immediate feedback (after student answers)

### Explanation Content Structure
- [ ] **Explains WHY correct** (2-3 sentences explaining concept deeply)
- [ ] **Addresses EACH distractor** (1 sentence per option explaining misconception)
- [ ] **Provides additional context** (examples, connections, application, 1-2 sentences)
- [ ] **Total addresses all 4 options** (correct + 3 distractors)

### Explanation Quality Template

Each explanation should follow this pattern:

```
[Why the correct option is right - 2-3 sentences]
Why not the others? [Option A misconception]. [Option B misconception].
[Option C misconception]. [Additional insight or connection]
```

### Explanation Quality Spot-Check

Check ALL 5-10 explanations for quality:

**Questions 1-3:**
- [ ] 60+ words
- [ ] Explains WHY correct
- [ ] Addresses all 3 distractors
- [ ] Additional context provided

**Questions 4-6:**
- [ ] 60+ words
- [ ] Explains WHY correct
- [ ] Addresses all 3 distractors
- [ ] Additional context provided

**Questions 7-10 (if applicable):**
- [ ] 60+ words
- [ ] Explains WHY correct
- [ ] Addresses all 3 distractors
- [ ] Additional context provided

---

## File Format Quality

### YAML Frontmatter
- [ ] Valid YAML syntax
- [ ] `sidebar_position` property included (number, e.g., 06)
- [ ] `title` property included (string, e.g., "Chapter X: Topic - Quiz")
- [ ] Optional: `description` property

### File Location and Naming
- [ ] File named: `##_chapter_##_quiz.md`
- [ ] First `##` = sidebar_position (lesson count + 1)
- [ ] Second `##` = chapter number (zero-padded)
- [ ] Saved to correct chapter directory
- [ ] Sidebar_position in frontmatter matches first `##` in filename

### Markdown Structure
- [ ] H1 title matches YAML title
- [ ] Brief introduction (1-2 sentences) before `<Quiz />` component
- [ ] Quiz component properly indented and formatted
- [ ] No syntax errors

### Component Rendering
- [ ] Quiz component tag opens: `<Quiz`
- [ ] Quiz component tag closes: `/>`
- [ ] All props properly formatted
- [ ] No missing quotes around string values
- [ ] Proper spacing and indentation

---

## Pre-Submission Validation

### Final Content Review
- [ ] Read through all 5-10 questions for clarity and accuracy
- [ ] Verify all questions are conceptual (not recall)
- [ ] Check all scenarios are realistic and relevant
- [ ] Ensure high-impact topics are covered

### Final Component Syntax Review
- [ ] Spot-check first 3 question objects: syntax valid
- [ ] Spot-check last 2 question objects: syntax valid
- [ ] Verify all correctOption values are 0-3
- [ ] Verify all options arrays have exactly 4 items
- [ ] Verify all explanations are present

### Final Randomization Review
- [ ] Count correct answer indices (0, 1, 2, 3): ____, ____, ____, ____
- [ ] Verify distribution is roughly balanced
- [ ] Ensure no 3+ consecutive same indices
- [ ] Verify no obvious patterns

### Final Format Review
- [ ] YAML frontmatter complete and valid
- [ ] File naming follows convention: `##_chapter_##_quiz.md`
- [ ] `.md` extension (not `.mdx`)
- [ ] Markdown renders without errors
- [ ] Quiz component would work in Docusaurus

---

## Human Review Needed

After completing all checks above, the following require human review:

### Content Review
- [ ] Spot-check 3-5 questions for technical accuracy
- [ ] Verify distractor plausibility and misconception alignment
- [ ] Confirm scenarios match chapter difficulty level
- [ ] Review cognitive level distribution (75%+ Apply or higher)

### Component Review
- [ ] Test Quiz component rendering in Docusaurus (if possible)
- [ ] Verify explanations display correctly after answer selection
- [ ] Check color-coded feedback (green/red) works as expected
- [ ] Test on mobile to verify responsive design

### Final Approval
- [ ] All validation checks passed
- [ ] All human review items completed
- [ ] Component displays and functions correctly
- [ ] Quiz ready for student use

---

## Validation Failure: Common Issues and Fixes

### Issue 1: Incorrect Index Values

**Symptoms:**
- [ ] correctOption uses 1-4 instead of 0-3
- [ ] Syntax error when rendering

**Fixes:**
1. Convert all indices: 1→0, 2→1, 3→2, 4→3
2. Example: `correctOption: 4` becomes `correctOption: 3`
3. Verify all 5-10 questions use 0-3 indices
4. Test component rendering after fix

---

### Issue 2: Wrong Options Count

**Symptoms:**
- [ ] Some questions have 3 options
- [ ] Some questions have 5 options
- [ ] Quiz component breaks or displays incorrectly

**Fixes:**
1. Identify questions with wrong option count
2. Add missing options (creating meaningful distractors)
3. Remove extra options
4. Ensure EVERY question has exactly 4 options
5. Test component rendering

---

### Issue 3: Uneven Index Distribution

**Symptoms:**
- [ ] One index appears 5+ times (for 8 questions)
- [ ] One index never appears
- [ ] 3+ consecutive same indices

**Fixes:**
1. List all correctOption values in order
2. Identify over-represented and under-represented indices
3. Swap correctOption values for 2-3 questions
4. Shuffle question order if helpful
5. Re-verify distribution

---

### Issue 4: Weak Explanations

**Symptoms:**
- [ ] Explanations <60 words
- [ ] Doesn't explain WHY correct
- [ ] Doesn't address distractors

**Fixes:**
1. Identify all weak explanations
2. Expand to 80-120 words per explanation
3. Add WHY reasoning (2-3 sentences)
4. Add distractor analysis (1 sentence each for all 3 wrong answers)
5. Add additional context (1-2 sentences)

---

### Issue 5: Distractor Problems

**Symptoms:**
- [ ] Options are obviously wrong (not plausible)
- [ ] Options don't test misconceptions
- [ ] Options are duplicative

**Fixes:**
1. Identify weak distractors
2. Research common student misconceptions for concept
3. Replace with plausible wrong answers
4. Ensure each tests different misconception
5. Verify all options are distinct

---

## Checklist Summary

**Critical checks (must pass):**
1. ✅ correctOption uses 0-3 indices (NOT 1-4 or letters)
2. ✅ Every question has exactly 4 options
3. ✅ Index distribution verified (0-3 evenly distributed)
4. ✅ No 3+ consecutive same indices
5. ✅ All explanations present (60-150 words)
6. ✅ File named correctly (`##_chapter_##_quiz.md`)

**Secondary checks (important):**
1. ✅ 75%+ questions at Apply level or higher
2. ✅ Distractors test specific misconceptions
3. ✅ Explanations address all 3 distractors
4. ✅ Quiz component syntax valid
5. ✅ YAML frontmatter complete

**If all critical checks pass:** Quiz ready for human review
**If any critical check fails:** Fix immediately before proceeding

---

## Passing Score Rationale

### Default: 70%

**College-Level Rigor:**
- 70% = demonstrated competency
- Below 70% indicates insufficient understanding for progression
- 60% acceptable for beginners, 70-80% for intermediate/advanced

**Why These Targets:**
- 70% (7/10 questions) = 3 wrong answers acceptable
- Allows for reasonable uncertainty on edge cases
- Permits advancement with strong understanding
- Realistic for first attempt on conceptual questions

**When to Adjust:**
- **Beginners:** 60% (6/10) to encourage first attempts
- **Intermediate:** 70% (7/10) standard for most chapters
- **Advanced:** 80% (8/10) for critical concepts

---

## Example Implementation

See `example-quiz.md` for a fully-worked example with:
- Proper YAML frontmatter
- 8 conceptual questions at Apply/Analyze levels
- Exactly 4 options per question
- Randomized correctOption indices (0-3)
- Comprehensive explanations addressing all distractors
- Proper Quiz component syntax

---

**Keywords for grep:** quality, checklist, validation, verification, review, standards, criteria, requirements, checks, component, correctOption, index, distribution, explanations, format, Quiz
