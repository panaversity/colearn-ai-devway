# Readability Metrics for Technical Writing

## Overview

Readability metrics quantify text complexity to ensure technical explanations match target audience comprehension level.

## Flesch-Kincaid Grade Level

**Formula**: 0.39 × (words/sentences) + 11.8 × (syllables/words) - 15.59

**Target Levels**:
- **Beginner** (Grade 6-8): Short sentences, simple vocabulary
- **Intermediate** (Grade 9-12): Moderate complexity
- **Advanced** (Grade 13+): Complex technical language acceptable

**Example Analysis**:
```
Text: "Python lists are mutable sequences."
- Words: 5
- Sentences: 1
- Syllables: 11
- Grade Level: ~9 (appropriate for intermediate)

Text: "The list data structure provides dynamic array functionality with O(1) amortized append complexity."
- Grade Level: ~16 (too complex for beginners)
```

## Sentence Length Guidelines

- **Beginner**: Average 10-15 words per sentence
- **Intermediate**: Average 15-20 words
- **Advanced**: Average 20-25 words

**Too Long**: Sentences >30 words risk losing reader attention

## Vocabulary Complexity

### Word Frequency
Common words (top 3000 English words) are easier to process.

**Beginner-Appropriate**:
- "use", "make", "get", "add", "find"

**Intermediate-Appropriate**:
- "implement", "execute", "iterate", "initialize"

**Advanced (use sparingly for beginners)**:
- "polymorphic", "memoization", "idempotent"

### Jargon Density

**Rule**: No more than 2-3 technical terms per paragraph for beginners

**Example - Too Dense**:
```
"Lambda expressions enable functional paradigms through lexical closures
with captured variables from enclosing scope via late binding semantics."
```

**Improved**:
```
"Lambda expressions are small, anonymous functions. They can use variables
from the surrounding code (this is called closure)."
```

## Paragraph Structure

- **Length**: 3-5 sentences per paragraph (beginners), 5-8 (advanced)
- **Focus**: One main idea per paragraph
- **Transitions**: Clear connections between paragraphs

## Active vs. Passive Voice

**Prefer Active**: More direct and easier to understand

**Passive** (weaker):
```
"The function is called by the program when needed."
```

**Active** (stronger):
```
"The program calls the function when needed."
```

**Passive acceptable**: When actor is unknown or unimportant
```
"The file was created." (we don't care who created it)
```

## Readability Tools

- **Hemingway Editor**: Highlights complex sentences
- **readability.py**: Python library for metrics
- **Grammarly**: Checks clarity and conciseness
- **LanguageTool**: Open-source grammar/style checker

## Cognitive Load Indicators

High cognitive load signs:
- Long sentences (>25 words)
- Many subordinate clauses
- Nested parentheticals
- Dense technical vocabulary
- Abstract concepts without examples

## Readability Checklist

- [ ] Grade level matches target audience
- [ ] Average sentence length appropriate
- [ ] Technical terms defined or familiar
- [ ] Active voice preferred
- [ ] Paragraphs focused and reasonable length
- [ ] Clear topic sentences

## Further Reading

- "The Elements of Style" (Strunk & White)
- "On Writing Well" (Zinsser)
