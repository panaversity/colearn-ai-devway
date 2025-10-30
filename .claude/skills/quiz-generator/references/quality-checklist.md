# Quality Checklist v2.0 - Complete Validation

This document provides a comprehensive checklist for validating quiz quality before submission.

---

## How to Use This Checklist

1. **After generating quiz:** Go through each section sequentially
2. **Check every box:** Don't skip items; each is critical
3. **Fix issues immediately:** Don't defer validation to end
4. **Re-check after fixes:** Verify fixes didn't introduce new issues

---

## Content Quality

### Question Count and Coverage
- [ ] 20-30 questions total (flexible based on chapter complexity)
- [ ] ALL major topics and lessons represented (no omissions)
- [ ] Balanced distribution across lessons (proportional to importance/depth)
- [ ] No rigid adherence to exactly 25 questions (comprehensive coverage prioritized)

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

## Option Design Quality (CRITICAL ANTI-CHEATING)

### Distractor Quality
- [ ] Every distractor tests a specific misconception
- [ ] Distractors are plausible (not obviously wrong)
- [ ] Based on common student errors from chapter
- [ ] No "joke" or filler options
- [ ] Diagnostic value (reveals thinking errors)

### Option Length Strategy (CRITICAL)
- [ ] ONE consistent strategy applied throughout quiz (equal OR random)
- [ ] For equal length: all options within ±2 words of each other
- [ ] For random variation: correct answer distributed across all length categories
- [ ] **Longest option ≠ always correct** (verified manually)
- [ ] **Shortest option ≠ always correct** (verified manually)
- [ ] **Word counts per question option verified** (counted manually, not assumed)
- [ ] No option >50 words (too long, creates obvious difference)
- [ ] No option <3 words (too short, seems incomplete)

### Option Length Validation Checklist
For EVERY question, verify:
- [ ] Q1: Word counts checked (a: __, b: __, c: __, d: __)
- [ ] Q2: Word counts checked (a: __, b: __, c: __, d: __)
- [ ] Q3: Word counts checked (a: __, b: __, c: __, d: __)
- [ ] ... (continue for all 20-30 questions)

**Quick validation method:**
1. List all questions (1-25 or 1-30)
2. For each question, count words for options a, b, c, d
3. Mark questions where longest option = correct answer
4. If more than 3 questions have longest = correct, FAIL (fix required)

---

## Answer Distribution Quality

### Distribution Targets
- [ ] Correct answers distributed evenly across a/b/c/d
- [ ] For 20 Qs: ~5 per letter (20-30% each)
- [ ] For 25 Qs: 6-7 per letter (24-28% each)
- [ ] For 30 Qs: 7-8 per letter (23-27% each)
- [ ] Total adds up to expected question count

### Pattern Checks
- [ ] No patterns (never a, b, c, d, a, b, c, d...)
- [ ] Maximum 2 consecutive same answers (no 3+ consecutive)
- [ ] Distribution verified manually (count each letter)
- [ ] Randomness is TRUE (not forced or artificial)

### Answer Distribution Verification Table

| Letter | Count | Percentage | Target (25Q) | Status |
|--------|-------|------------|--------------|--------|
| a      | __    | __%        | 24-28%       | ☐ Pass |
| b      | __    | __%        | 24-28%       | ☐ Pass |
| c      | __    | __%        | 24-28%       | ☐ Pass |
| d      | __    | __%        | 20-24%       | ☐ Pass |
| Total  | __    | 100%       | 100%         | ☐ Pass |

**Fill in counts manually and verify targets.**

### Consecutive Answer Check

List first 10 correct answers: __, __, __, __, __, __, __, __, __, __

- [ ] No 3+ consecutive same answers in first 10
- [ ] No 3+ consecutive same answers in last 10
- [ ] No 3+ consecutive same answers anywhere in quiz

---

## Explanation Quality (Answer Key Only)

### Explanation Presence
- [ ] All explanations present in answer key section (one per question)
- [ ] Each explanation 60-150 words (comprehensive, not rushed)
- [ ] No explanations visible in questions section (true assessment)

### Explanation Content
- [ ] Confirms correct answer clearly (**a/b/c/d** bold)
- [ ] Explains WHY correct (concept teaching, 2-3 sentences)
- [ ] Addresses why distractors are wrong (specific misconceptions, 1-2 sentences each)
- [ ] Provides additional context (examples, connections, application, 1-2 sentences)

### Explanation Quality Spot-Check

Check 5 random explanations in detail:

**Explanation 1 (Q__):**
- [ ] 60+ words
- [ ] Explains WHY correct
- [ ] Addresses distractors
- [ ] Additional context provided

**Explanation 2 (Q__):**
- [ ] 60+ words
- [ ] Explains WHY correct
- [ ] Addresses distractors
- [ ] Additional context provided

**Explanation 3 (Q__):**
- [ ] 60+ words
- [ ] Explains WHY correct
- [ ] Addresses distractors
- [ ] Additional context provided

**Explanation 4 (Q__):**
- [ ] 60+ words
- [ ] Explains WHY correct
- [ ] Addresses distractors
- [ ] Additional context provided

**Explanation 5 (Q__):**
- [ ] 60+ words
- [ ] Explains WHY correct
- [ ] Addresses distractors
- [ ] Additional context provided

---

## Format and Structure Quality

### File Format
- [ ] Valid MDX/Markdown syntax (plain markdown, no JSX)
- [ ] Proper YAML frontmatter (title, description, sidebar_position)
- [ ] No syntax errors (renders correctly in Docusaurus)

### Structure
- [ ] Questions section SEPARATE from answer key (clear `---` divider)
- [ ] NO explanations visible in questions section (true assessment)
- [ ] Answer key section clearly labeled "## Answer Key"
- [ ] Correct answer format: **Correct answer: [a/b/c/d]** (bold, clear)

### File Naming and Location
- [ ] File named correctly: `##_chapter_##_quiz.md`
- [ ] First `##` = sidebar_position (lesson count + 1)
- [ ] Second `##` = chapter number (zero-padded)
- [ ] Saved to correct directory (chapter folder, after all lessons)
- [ ] Sidebar_position in frontmatter matches first `##` in filename

---

## Pre-Submission Validation

### Final Content Review
- [ ] Read through all 20-30 questions for clarity and accuracy
- [ ] Verify all questions are conceptual (not recall)
- [ ] Check all scenarios are realistic and relevant
- [ ] Ensure ALL chapter material is covered (no omissions)

### Final Anti-Cheating Review
- [ ] Spot-check 10 questions: count word lengths for options
- [ ] Verify longest option ≠ correct answer pattern
- [ ] Verify correct answer distribution: a(__), b(__), c(__), d(__)
- [ ] Ensure no 3+ consecutive same answers

### Final Format Review
- [ ] Questions section has NO explanations visible
- [ ] Answer key section clearly separated by `---`
- [ ] All explanations present and comprehensive (60-150 words)
- [ ] File naming follows convention: `##_chapter_##_quiz.md`
- [ ] YAML frontmatter correct and complete

---

## Human Review Needed

After completing all checks above, the following require human review:

### Content Review
- [ ] Spot-check 5-10 questions for technical accuracy
- [ ] Verify distractor plausibility and misconception alignment
- [ ] Confirm scenarios match chapter difficulty level
- [ ] Review cognitive level distribution (75%+ Apply or higher)

### Anti-Cheating Review
- [ ] Verify option length consistency (spot-check 10 questions)
- [ ] Check answer distribution manually (count a/b/c/d)
- [ ] Verify no obvious patterns in correct answers
- [ ] Confirm longest options don't reveal correct answers

### Format Review
- [ ] Test markdown rendering in Docusaurus (if possible)
- [ ] Verify proper separation of questions/answers
- [ ] Check that quiz appears at chapter end (sidebar_position)
- [ ] Confirm file naming matches lesson convention

### Final Approval
- [ ] All validation checks passed
- [ ] All human review items completed
- [ ] Quiz ready for deployment
- [ ] Approve for student use

---

## Validation Failure: Common Issues and Fixes

### Issue 1: Option Length Imbalance

**Symptoms:**
- [ ] Longest option is correct in 5+ questions
- [ ] Word counts vary wildly (5 words vs. 30 words)

**Fixes:**
1. Identify questions where longest = correct
2. Adjust wording to equalize option lengths
3. Re-verify word counts for all options
4. Ensure consistent strategy (equal or random)

---

### Issue 2: Uneven Answer Distribution

**Symptoms:**
- [ ] One letter appears 10+ times (for 25 questions)
- [ ] One letter appears <4 times
- [ ] 3+ consecutive same answers

**Fixes:**
1. List all correct answer positions
2. Identify over-represented and under-represented letters
3. Swap correct answer positions for 2-3 questions
4. Re-verify distribution and consecutive checks

---

### Issue 3: Weak Explanations

**Symptoms:**
- [ ] Explanations <60 words
- [ ] Doesn't explain WHY correct
- [ ] Doesn't address distractors

**Fixes:**
1. Identify weak explanations (spot-check all)
2. Expand to 80-120 words per explanation
3. Add WHY reasoning (2-3 sentences)
4. Add distractor analysis (1-2 sentences each)
5. Add additional context (1-2 sentences)

---

### Issue 4: Incomplete Coverage

**Symptoms:**
- [ ] One or more lessons have zero questions
- [ ] Major topics omitted
- [ ] Heavy focus on early lessons, light on later lessons

**Fixes:**
1. List all lessons and major topics
2. Count questions per lesson
3. Add questions for under-represented lessons
4. Remove or consolidate questions from over-represented lessons
5. Re-verify total stays within 20-30 range

---

## Checklist Summary

**Critical checks (must pass):**
1. ✅ Option lengths validated (equal or random, no longest = correct pattern)
2. ✅ Answer distribution verified (a/b/c/d evenly distributed)
3. ✅ Questions/answers separated (no inline explanations)
4. ✅ File naming correct (`##_chapter_##_quiz.md`)
5. ✅ ALL material covered (no omissions)

**Secondary checks (important):**
1. ✅ 75%+ questions at Apply level or higher
2. ✅ Explanations 60-150 words each
3. ✅ Distractors test specific misconceptions
4. ✅ No 3+ consecutive same answers
5. ✅ Technical accuracy verified

**If all critical checks pass:** Quiz ready for human review
**If any critical check fails:** Fix immediately before proceeding

---

## Passing Score: 72% Rationale

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

**Keywords for grep:** quality, checklist, validation, verification, review, standards, criteria, requirements, checks, anti-cheating, distribution, option-length, explanations, format
