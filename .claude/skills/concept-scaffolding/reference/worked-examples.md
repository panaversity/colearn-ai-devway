# Worked Examples in Programming Education

## Overview

Worked examples are complete problem solutions with step-by-step explanations. Research shows that studying worked examples is more effective for novice learners than unguided problem-solving. Worked examples reduce cognitive load by showing the complete solution pattern before asking learners to practice.

## Key Principles

- **Demonstrate before practice**: Show the complete solution before asking learners to solve similar problems
- **Explain the reasoning**: Don't just show code—explain why each step is necessary
- **Integrate code and explanation**: Keep code and its explanation close together (avoid split attention)
- **Use subgoal labeling**: Break worked examples into clear, labeled steps
- **Follow with practice**: Worked examples are most effective when followed by similar practice problems

## Effective Worked Example Structure

### Components of a Good Worked Example

1. **Problem statement**: Clear description of what the code should accomplish
2. **Complete solution**: Runnable, correct code
3. **Step-by-step explanation**: Commentary explaining each significant step
4. **Reasoning**: Why this approach works (not just what it does)
5. **Connection to concepts**: Explicit links to underlying programming concepts

### Template Structure

```python
# PROBLEM: [Clear statement of what code should do]

# SOLUTION:
# Step 1: [Subgoal label]
[code for step 1]
# Explanation: [Why this step is necessary and how it works]

# Step 2: [Subgoal label]
[code for step 2]
# Explanation: [Why this step is necessary and how it works]

# Step 3: [Subgoal label]
[code for step 3]
# Explanation: [Why this step is necessary and how it works]

# RESULT: [Expected output or behavior]

# KEY CONCEPTS: [Programming principles demonstrated]
```

## Example: Worked Example for List Comprehensions

```python
# PROBLEM: Given a list of numbers, create a new list containing only the even numbers

# TRADITIONAL APPROACH (for comparison):
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Create an empty list to store results
even_numbers = []
# Explanation: We need a place to accumulate even numbers we find

# Step 2: Iterate through each number
for num in numbers:
    # Explanation: We check each number one at a time

    # Step 3: Check if the number is even
    if num % 2 == 0:
        # Explanation: Modulo (%) gives remainder after division
        # If remainder is 0, the number is evenly divisible by 2 (even)

        # Step 4: Add even numbers to our result list
        even_numbers.append(num)
        # Explanation: append() adds an item to the end of a list

# RESULT: even_numbers is now [2, 4, 6, 8, 10]

# LIST COMPREHENSION APPROACH (more concise):
even_numbers = [num for num in numbers if num % 2 == 0]
# Explanation: List comprehension combines steps 1-4 into one line
# Read as: "Create a list of num, for each num in numbers, if num is even"

# KEY CONCEPTS:
# - Iteration (processing each item in a sequence)
# - Conditional filtering (selecting items that meet a criterion)
# - List accumulation (building a new list from existing data)
```

## Worked Example Progression Pattern

### Pattern: Full Example → Partial Example → Practice Problem

**Stage 1: Complete Worked Example**
```python
# PROBLEM: Calculate the sum of all numbers in a list

numbers = [1, 2, 3, 4, 5]

# Step 1: Initialize accumulator
total = 0  # Start at zero

# Step 2: Add each number to total
for num in numbers:
    total += num  # Same as: total = total + num

# RESULT: total is now 15
```

**Stage 2: Partial Example (Completion Problem)**
```python
# PROBLEM: Calculate the product of all numbers in a list

numbers = [2, 3, 4]

# Step 1: Initialize accumulator
product = 1  # Why 1 instead of 0?

# Step 2: Multiply each number with product
# YOUR CODE HERE

# RESULT: product should be 24
```

**Stage 3: Independent Practice**
```python
# PROBLEM: Find the maximum number in a list without using max()
# Write your solution below:
```

## Subgoal Labeling Strategy

Subgoal labels help learners recognize patterns that apply to many problems.

### Common Python Subgoals

**For Data Processing**:
1. Initialize data structure (list, dict, set, accumulator)
2. Iterate through input data
3. Apply transformation or filter
4. Accumulate or store result
5. Return or display result

**For Problem Solving**:
1. Understand input (parse, validate)
2. Define edge cases
3. Implement core logic
4. Handle errors
5. Test with examples

**Example with Subgoal Labels**:
```python
# PROBLEM: Count word frequency in a sentence

sentence = "the quick brown fox jumps over the lazy dog"

# SUBGOAL 1: Prepare data (convert to lowercase, split into words)
words = sentence.lower().split()

# SUBGOAL 2: Initialize data structure (dictionary for counting)
word_count = {}

# SUBGOAL 3: Iterate and count each word
for word in words:
    if word in word_count:
        word_count[word] += 1  # Increment existing count
    else:
        word_count[word] = 1   # Initialize new word

# SUBGOAL 4: Display results
for word, count in word_count.items():
    print(f"{word}: {count}")

# RESULT: Shows each word and how many times it appears
```

## Self-Explanation Prompts

After presenting a worked example, ask learners to explain key parts:

- "Why do we initialize the accumulator to 0 (or 1, or empty list)?"
- "What would happen if we removed this step?"
- "How would you modify this to solve [slightly different problem]?"
- "What programming concept does this step demonstrate?"

## Worked Examples for Common Python Concepts

### Exception Handling
```python
# PROBLEM: Safely read a number from user input

# Step 1: Attempt the operation that might fail
try:
    user_input = input("Enter a number: ")
    number = int(user_input)  # This might raise ValueError

# Step 2: Handle the specific error
except ValueError:
    print("That's not a valid number!")
    number = None  # Use a default value

# Step 3: Continue with rest of program
if number is not None:
    print(f"You entered: {number}")
```

### File Operations
```python
# PROBLEM: Read and count lines in a file safely

# Step 1: Open file with context manager (ensures file is closed)
try:
    with open("data.txt", "r") as file:
        # Step 2: Read and process content
        lines = file.readlines()
        line_count = len(lines)
        print(f"File has {line_count} lines")

# Step 3: Handle case where file doesn't exist
except FileNotFoundError:
    print("File not found!")
    line_count = 0

# Context manager automatically closes file (no need for file.close())
```

### List Comprehensions
```python
# PROBLEM: Convert list of temperatures from Celsius to Fahrenheit

celsius_temps = [0, 10, 20, 30, 40]

# Traditional approach (for comparison)
fahrenheit_temps = []
for temp in celsius_temps:
    fahrenheit = (temp * 9/5) + 32
    fahrenheit_temps.append(fahrenheit)

# List comprehension approach (one line)
fahrenheit_temps = [(temp * 9/5) + 32 for temp in celsius_temps]

# RESULT: [32.0, 50.0, 68.0, 86.0, 104.0]
```

## Common Pitfalls

- **Insufficient explanation**: Showing code without explaining the reasoning
- **Split attention**: Code in one place, explanation elsewhere
- **Too complex**: Including too many concepts in one example
- **Missing the "why"**: Explaining what code does but not why it's designed that way
- **No follow-up practice**: Not providing similar problems for learners to solve

## Validation Checklist

A good worked example should:
- [ ] Demonstrate one primary concept clearly
- [ ] Include complete, runnable code
- [ ] Provide step-by-step explanation
- [ ] Explain reasoning (not just actions)
- [ ] Use clear subgoal labels
- [ ] Be followed by similar practice problems
- [ ] Avoid split attention (keep code and explanation together)

## Further Reading

- Atkinson, R. K., et al. (2000). "Learning from examples: Instructional principles"
- Renkl, A. (2014). "Toward an instructionally oriented theory of example-based learning"
- Margulieux, L., et al. (2012). "Subgoal-labeled instructional material improves performance"
