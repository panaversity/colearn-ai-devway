# Effective Teaching Example Patterns

## Overview

Programming examples for teaching must balance multiple goals: demonstrating concepts clearly, being runnable and correct, following best practices, and avoiding cognitive overload. This guide presents proven patterns for creating effective teaching examples.

## Core Principles

### One Concept Per Example
Each example should clearly demonstrate ONE primary concept. Additional concepts should only be included if they're prerequisites that learners already understand.

**Good** (focuses on list append):
```python
# Demonstrates: list.append() method
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]
```

**Bad** (too many concepts at once):
```python
# Tries to demonstrate: append, extend, list comprehension, filter
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.extend([f.upper() for f in ["date", "fig"] if len(f) > 3])
```

### Progressive Complexity
Introduce concepts in stages: simple → realistic → complex.

**Stage 1: Simplest Case**
```python
# Most basic example: single parameter, no edge cases
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # Hello, Alice
```

**Stage 2: Realistic Use**
```python
# Add common real-world feature: optional parameter
def greet(name, formal=False):
    if formal:
        return f"Good day, {name}"
    return f"Hello, {name}"

print(greet("Alice"))          # Hello, Alice
print(greet("Alice", True))    # Good day, Alice
```

**Stage 3: Production-Ready**
```python
# Full implementation: validation, type hints, docstring
def greet(name: str, formal: bool = False) -> str:
    """
    Generate a greeting for the given name.

    Args:
        name: Person's name
        formal: If True, use formal greeting

    Returns:
        Greeting string

    Raises:
        ValueError: If name is empty
    """
    if not name:
        raise ValueError("Name cannot be empty")

    greeting = "Good day" if formal else "Hello"
    return f"{greeting}, {name}"
```

### Show Expected Output
Always include the expected output or result. This helps learners verify understanding.

```python
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)  # [2, 4, 6, 8, 10]
```

### Runnable and Self-Contained
Examples should be complete and executable without external dependencies (when possible).

**Good**: Self-contained
```python
# Complete example - can copy and run immediately
def calculate_total(prices):
    return sum(prices)

items = [10.99, 5.50, 3.25]
total = calculate_total(items)
print(f"Total: ${total:.2f}")  # Total: $19.74
```

**Bad**: Incomplete
```python
# Incomplete - where does 'items' come from?
total = calculate_total(items)
print(f"Total: ${total:.2f}")
```

## Pattern Categories

### Pattern 1: Before/After Comparisons

Show the old way, then introduce the new concept.

```python
# BEFORE: Manual iteration with index
items = ["apple", "banana", "cherry"]
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# AFTER: Using enumerate (Pythonic way)
items = ["apple", "banana", "cherry"]
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

### Pattern 2: Problem → Solution

State a problem, then show how to solve it.

```python
# PROBLEM: Need to filter a list for even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# SOLUTION: List comprehension with condition
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]
```

### Pattern 3: Incremental Building

Build complexity step by step, each example adding one feature.

```python
# Step 1: Basic function
def calculate_price(quantity, unit_price):
    return quantity * unit_price

# Step 2: Add tax calculation
def calculate_price(quantity, unit_price, tax_rate=0.08):
    subtotal = quantity * unit_price
    tax = subtotal * tax_rate
    return subtotal + tax

# Step 3: Add validation
def calculate_price(quantity, unit_price, tax_rate=0.08):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if unit_price < 0:
        raise ValueError("Price cannot be negative")

    subtotal = quantity * unit_price
    tax = subtotal * tax_rate
    return subtotal + tax
```

### Pattern 4: Common Mistakes → Correct Way

Show a common error, explain the problem, then show the fix.

```python
# COMMON MISTAKE: Modifying list during iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # BUG: Skips elements!
print(numbers)  # [1, 3, 5] - but 4 might remain!

# CORRECT WAY: Create new list
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)  # [1, 3, 5]
```

### Pattern 5: Multiple Approaches

Show different ways to solve the same problem, discussing tradeoffs.

```python
# APPROACH 1: Traditional loop (explicit, easy to understand)
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)  # 15

# APPROACH 2: Built-in sum (more concise, Pythonic)
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # 15

# APPROACH 3: functools.reduce (functional style)
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)  # 15

# BEST CHOICE: sum() - readable and efficient
```

### Pattern 6: Real-World Context

Frame examples in familiar, real-world scenarios.

```python
# Example: Managing a shopping cart (relatable context)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        """Add an item to the cart."""
        self.items.append({"name": name, "price": price})

    def get_total(self):
        """Calculate the total cost of all items."""
        return sum(item["price"] for item in self.items)

# Usage
cart = ShoppingCart()
cart.add_item("Banana", 0.99)
cart.add_item("Apple", 1.29)
print(f"Total: ${cart.get_total():.2f}")  # Total: $2.28
```

## Anti-Patterns to Avoid

### Anti-Pattern 1: Toy Examples That Obscure Concepts

```python
# BAD: Using foo/bar obscures purpose
def foo(x, y):
    return x + y

result = foo(2, 3)

# GOOD: Meaningful names clarify purpose
def calculate_total_price(base_price, tax):
    return base_price + tax

result = calculate_total_price(100, 8)
```

### Anti-Pattern 2: Examples That Don't Run

```python
# BAD: Pseudocode or incomplete examples
# Load data from file
data = load_data(filename)  # Where is load_data defined?
process(data)

# GOOD: Complete, runnable example
def load_data(filename):
    with open(filename) as f:
        return f.read()

data = load_data("data.txt")
print(data)
```

### Anti-Pattern 3: Kitchen Sink Examples

```python
# BAD: Trying to demonstrate everything at once
class UserManager(DatabaseMixin, CacheMixin, LoggingMixin):
    def create_user(self, username, email, password, **kwargs):
        # Too much happening: validation, hashing, database, caching, logging...
        pass

# GOOD: Focus on one aspect
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"
```

### Anti-Pattern 4: Unexplained Magic

```python
# BAD: Unexplained complex expression
result = [x for x in range(100) if all(x % i for i in range(2, int(x**0.5) + 1))]

# GOOD: Break down and explain
def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find all prime numbers under 100
primes = [x for x in range(100) if is_prime(x)]
```

## Example Structure Template

Use this template for consistently well-structured examples:

```python
# [Brief description of what this example demonstrates]

# [Optional: Prerequisites or concepts learner should know]

# [Optional: Problem statement or context]

# EXAMPLE CODE
[code here with inline comments]

# EXPECTED OUTPUT
[show what running this code produces]

# EXPLANATION
# [1-3 sentences explaining how it works and why]

# [Optional: Common mistakes or variations]
```

### Applied Template

```python
# Demonstrates: Using dictionary.get() with default values

# Prerequisites: Understanding dictionaries and key-value pairs

# Problem: Safely access dictionary values without KeyError

user_data = {"name": "Alice", "age": 30}

# Access existing key
name = user_data.get("name", "Unknown")
print(name)  # Alice

# Access non-existent key with default
country = user_data.get("country", "Not specified")
print(country)  # Not specified

# EXPLANATION:
# get() returns the value if key exists, otherwise returns the default.
# This prevents KeyError exceptions when accessing potentially missing keys.

# COMMON MISTAKE: Using user_data["country"] would raise KeyError
```

## Comments in Teaching Examples

### What to Comment

```python
# GOOD: Explain non-obvious logic
# Calculate factorial using recursion
def factorial(n):
    if n <= 1:  # Base case: 0! = 1! = 1
        return 1
    return n * factorial(n - 1)  # Recursive case

# GOOD: Explain "why" not "what"
# Sort by last name, then first name for consistent ordering
students.sort(key=lambda s: (s.last_name, s.first_name))

# BAD: State the obvious
# Increment i by 1
i += 1
```

### Comment Density for Teaching

More comments than production code—explain each significant step:

```python
# Calculate the average of a list of numbers

numbers = [10, 20, 30, 40, 50]

# Step 1: Calculate the sum of all numbers
total = sum(numbers)  # sum() adds all elements

# Step 2: Count how many numbers we have
count = len(numbers)  # len() returns list length

# Step 3: Divide sum by count to get average
average = total / count

# Step 4: Display the result
print(f"Average: {average}")  # Average: 30.0
```

## Variable Naming for Clarity

In teaching examples, err on the side of explicit, descriptive names:

```python
# Production code might use:
t = s.split()
c = len(t)

# Teaching examples should use:
sentence = "The quick brown fox"
words = sentence.split()
word_count = len(words)
```

## Testing and Validation

Include simple assertions to verify example correctness:

```python
def calculate_area(length, width):
    """Calculate area of a rectangle."""
    return length * width

# Test with known values
area = calculate_area(5, 3)
assert area == 15, "5 × 3 should equal 15"
print(f"Area: {area}")  # Area: 15
```

## Further Reading

- "How to Design Programs" (pedagogical approach to examples)
- "Think Python" by Allen Downey (excellent example style)
- "Python Cookbook" (practical patterns)
