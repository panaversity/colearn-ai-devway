# Quiz Component - Usage Guide

## ✅ No Imports Needed!

The Quiz component is **globally registered**. Just use `<Quiz />` directly in your MDX files.

## 🚀 Basic Usage

```mdx
---
title: Chapter 1 Quiz
---

# Chapter 1 Quiz

<Quiz
  title="Python Basics Quiz"
  questions={[
    {
      question: "What is the correct way to create a variable in Python?",
      options: ["int x = 5", "var x = 5", "x = 5", "let x = 5"],
      correctOption: 2,
      explanation: "Python uses dynamic typing, so you simply assign a value without declaring the type."
    },
    {
      question: "Which data type is mutable in Python?",
      options: ["Tuple", "String", "List", "Integer"],
      correctOption: 2,
      explanation: "Lists are mutable - you can change their contents after creation."
    }
  ]}
  passingScore={70}
/>
```

## 📋 Props

### Required
- **`questions`** - Array of question objects

### Optional
- **`title`** - Quiz title (default: "Quiz")
- **`passingScore`** - Pass percentage 0-100 (default: 70)

## 📝 Question Format

Each question must have:

```javascript
{
  question: "Your question text?",
  options: ["Option A", "Option B", "Option C", "Option D"],  // Exactly 4 options
  correctOption: 2,  // Index 0-3 of correct answer
  explanation: "Why this is correct (optional)"
}
```

**Important:**
- ✅ Must have exactly **4 options**
- ✅ `correctOption` must be **0, 1, 2, or 3** (not 1-4!)
- ✅ Add `explanation` to help students learn

## 💡 Complete Example

```mdx
---
sidebar_position: 3
title: Chapter 3 Quiz
---

# Chapter 3: Functions - Quiz

Test your understanding of Python functions:

<Quiz
  title="Functions and Scope"
  questions={[
    {
      question: "What keyword is used to define a function in Python?",
      options: ["function", "def", "func", "define"],
      correctOption: 1,
      explanation: "Python uses the 'def' keyword to define functions."
    },
    {
      question: "What does a function return if no return statement is specified?",
      options: ["None", "0", "Empty string", "undefined"],
      correctOption: 0,
      explanation: "Functions without a return statement automatically return None."
    },
    {
      question: "Which is the correct syntax for a function with default parameters?",
      options: [
        "def greet(name = 'World'):",
        "def greet(name: 'World'):",
        "def greet(name -> 'World'):",
        "def greet(name := 'World'):"
      ],
      correctOption: 0,
      explanation: "Default parameters use the equals sign: parameter = default_value"
    },
    {
      question: "What is a lambda function?",
      options: [
        "A function with no name",
        "An anonymous single-expression function",
        "A function that returns nothing",
        "A function with multiple return statements"
      ],
      correctOption: 1,
      explanation: "Lambda functions are anonymous functions limited to a single expression."
    },
    {
      question: "Can a function modify a list passed as an argument?",
      options: [
        "No, never",
        "Yes, because lists are mutable",
        "Only with special syntax",
        "Only if you use 'global'"
      ],
      correctOption: 1,
      explanation: "Lists are mutable objects, so functions can modify them directly."
    }
  ]}
  passingScore={60}
/>
```

## 🎯 Best Practices

### 1. Question Count
- **5-10 questions** per chapter quiz
- Covers main concepts without overwhelming

### 2. Passing Score Guidelines
- **Beginners:** 60-70%
- **Intermediate:** 70-80%
- **Advanced:** 80-90%

### 3. Always Add Explanations
Help students learn from mistakes:

```javascript
{
  question: "Which method adds an item to a list?",
  options: ["add()", "append()", "insert()", "push()"],
  correctOption: 1,
  explanation: "The append() method adds an item to the end of a list."  // ← Important!
}
```

### 4. Make Options Plausible
```javascript
// ❌ Bad - too obvious
options: ["append()", "banana", "xyz", "hello"]

// ✅ Good - all seem reasonable
options: ["add()", "append()", "insert()", "push()"]
```

### 5. Be Specific
```javascript
// ❌ Bad - vague
question: "What about lists?"

// ✅ Good - clear and specific
question: "Which method removes the last item from a list?"
```

## 📁 Where to Add Quizzes

Add at the end of chapter files:

```
docs/
├── part-1-foundations/
│   ├── 01-intro.mdx
│   ├── 02-variables.mdx
│   ├── 02-variables-quiz.mdx  ← Separate quiz file
│   ├── 03-control-flow.mdx
│   └── 03-control-flow-quiz.mdx
```

Or at the bottom of each chapter:

```mdx
---
title: Chapter 2: Variables
---

# Variables and Data Types

[Your lesson content...]

---

## Chapter Quiz

<Quiz
  title="Variables Quiz"
  questions={[...]}
/>
```

## 🎨 Features (Built-in)

Your quiz automatically includes:

- ✅ **Progress bar** showing completion
- ✅ **Back/Next buttons** for navigation
- ✅ **Question dots** - click to jump to any question
- ✅ **Answer counter** - shows X/Y answered
- ✅ **Validation** - can't submit until all answered
- ✅ **Results page** with score and review
- ✅ **Color-coded feedback** (green = correct, red = incorrect)
- ✅ **Explanations** shown after submission
- ✅ **Retake button** to try again
- ✅ **Light/Dark theme** support
- ✅ **Fully responsive** (mobile, tablet, desktop)

## 🎨 Colors

Automatically matches your site theme:

- **Primary:** Navy blue (`#004d99`)
- **Success:** Green (correct answers)
- **Error:** Red (incorrect answers)
- **Auto theme switching** between light/dark mode

## ❓ Common Questions

### Q: Do I need to import the Quiz component?
**A:** No! It's globally registered. Just use `<Quiz />` directly.

### Q: Can I have multiple quizzes on one page?
**A:** Yes! Add multiple `<Quiz />` components with different questions.

### Q: Why must I have exactly 4 options?
**A:** The component is designed for 4 options (A, B, C, D). If you need more, let me know.

### Q: What if I use the wrong index for correctOption?
**A:** Remember: arrays start at 0!
- First option = 0
- Second option = 1
- Third option = 2
- Fourth option = 3

### Q: Can I customize the colors?
**A:** Yes! Edit `src/components/Quiz.module.css` to change styles.

## ✅ Quick Checklist

When creating a quiz:

- [ ] Exactly 4 options per question
- [ ] `correctOption` is 0, 1, 2, or 3
- [ ] Added explanations for each question
- [ ] Title is descriptive
- [ ] Passing score is appropriate (60-80%)
- [ ] Questions are clear and specific
- [ ] All options are plausible

## 🚀 That's It!

No imports, no configuration. Just copy the example above, customize your questions, and you're done! 🎉

**Test it:** See [`docs/quiz-test.md`](../../docs/quiz-test.md) for a working example.
