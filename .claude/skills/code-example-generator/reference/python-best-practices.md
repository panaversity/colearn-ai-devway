# Python Best Practices for Teaching Examples

## Overview

Code examples in educational contexts must balance pedagogical clarity with real-world best practices. This guide covers Python conventions and patterns that should be demonstrated in teaching examples, adapted for different learner levels.

## PEP 8 Style Guidelines (Summary)

### Naming Conventions

**Variables and Functions**: `lowercase_with_underscores`
```python
user_name = "Alice"
total_count = 42

def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

**Constants**: `UPPERCASE_WITH_UNDERSCORES`
```python
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
```

**Classes**: `CapitalizedWords` (PascalCase)
```python
class StudentRecord:
    pass

class HTTPResponse:
    pass
```

**Private/Internal**: `_leading_underscore`
```python
def _internal_helper():
    pass

class MyClass:
    def __init__(self):
        self._internal_state = []
```

### Indentation and Spacing

- **Use 4 spaces** per indentation level (never tabs)
- **Two blank lines** between top-level functions and classes
- **One blank line** between methods in a class
- **Spaces around operators**: `x = y + z` (not `x=y+z`)
- **No trailing whitespace**

```python
# Good
def first_function():
    pass


def second_function():
    pass


class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass
```

### Line Length

- **Maximum 79 characters** for code
- **Maximum 72 characters** for docstrings/comments
- Use parentheses for implicit line continuation

```python
# Good: implicit continuation
result = (first_value + second_value +
          third_value + fourth_value)

# Also good: explicit backslash (less preferred)
result = first_value + second_value + \
         third_value + fourth_value
```

### Import Organization

1. Standard library imports
2. Related third-party imports
3. Local application/library imports

Separate each group with a blank line.

```python
# Standard library
import os
import sys

# Third-party
import numpy as np
import requests

# Local
from myapp import models
from myapp.utils import helper
```

## Type Hints (Python 3.5+)

### When to Use Type Hints in Teaching

**Beginner Level**: Avoid initially; introduce variables and functions first
**Intermediate Level**: Introduce gradually for clarity
**Advanced Level**: Use consistently

### Basic Type Hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add_numbers(a: int, b: int) -> int:
    return a + b

# Variables (Python 3.6+)
age: int = 25
scores: list[int] = [90, 85, 88]
```

### Common Type Hints

```python
from typing import List, Dict, Optional, Union

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

def find_user(user_id: int) -> Optional[dict]:
    # Returns dict if found, None otherwise
    return user_dict if user_id in database else None

def parse_value(value: Union[int, str]) -> int:
    return int(value)
```

## Docstrings

### When to Include Docstrings

**Always**: Module-level, class, and public function docstrings
**Teaching Context**: Even simple examples benefit from docstrings

### Docstring Formats

**One-line docstring** (for simple cases):
```python
def square(n):
    """Return the square of n."""
    return n ** 2
```

**Multi-line docstring** (for complex functions):
```python
def calculate_statistics(numbers):
    """
    Calculate mean, median, and mode of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        Dictionary with 'mean', 'median', and 'mode' keys

    Raises:
        ValueError: If numbers list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate statistics of empty list")
    # Implementation...
```

## Error Handling Best Practices

### Specific Exception Handling

```python
# Good: Catch specific exceptions
try:
    value = int(user_input)
except ValueError:
    print("Invalid number format")

# Bad: Catch all exceptions (too broad)
try:
    value = int(user_input)
except:  # Don't do this
    print("Something went wrong")
```

### Use Context Managers

```python
# Good: Context manager (automatically closes file)
with open("data.txt", "r") as file:
    content = file.read()

# Bad: Manual file handling (easy to forget close())
file = open("data.txt", "r")
content = file.read()
file.close()  # Might not execute if error occurs
```

### Fail Explicitly

```python
def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Better than returning None or -1 as error indicator
```

## Pythonic Patterns for Teaching

### List Comprehensions (vs. loops)

```python
# Traditional loop (good for beginners)
squares = []
for n in range(10):
    squares.append(n ** 2)

# List comprehension (introduce to intermediate)
squares = [n ** 2 for n in range(10)]
```

### Enumerate (vs. range(len()))

```python
# Less Pythonic
items = ["apple", "banana", "cherry"]
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# More Pythonic
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

### Dictionary Get Method

```python
# Less safe
if key in my_dict:
    value = my_dict[key]
else:
    value = default

# More Pythonic
value = my_dict.get(key, default)
```

### String Formatting

```python
# Old style (Python 2)
message = "Hello, %s" % name

# .format() method
message = "Hello, {}".format(name)

# f-strings (Python 3.6+, preferred)
message = f"Hello, {name}"
```

## Common Anti-Patterns to Avoid in Examples

### Mutable Default Arguments

```python
# BAD: Mutable default argument
def add_item(item, items=[]):  # BUG!
    items.append(item)
    return items

# GOOD: Use None and create new list
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Bare Except Clauses

```python
# BAD: Catches everything including KeyboardInterrupt
try:
    risky_operation()
except:
    handle_error()

# GOOD: Catch specific exceptions
try:
    risky_operation()
except (ValueError, TypeError) as e:
    handle_error(e)
```

### Testing for None

```python
# BAD: Doesn't work for empty collections
if not value:
    # False for None, [], 0, "", etc.

# GOOD: Explicitly test for None
if value is None:
    # Only True for None
```

## Level-Appropriate Complexity

### Beginner Examples
- Focus on clarity over cleverness
- One concept per example
- Explicit over implicit
- Verbose variable names
- Avoid advanced features (comprehensions, decorators, etc.)

```python
# Beginner-appropriate: explicit and clear
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total = total + number

average = total / len(numbers)
print(f"Average: {average}")
```

### Intermediate Examples
- Introduce Pythonic patterns
- Use list comprehensions, enumerate, etc.
- Type hints for clarity
- Basic error handling

```python
# Intermediate-appropriate: Pythonic patterns
def calculate_average(numbers: list[int]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)

# Using comprehension for filtering
even_numbers = [n for n in numbers if n % 2 == 0]
```

### Advanced Examples
- Production-ready patterns
- Comprehensive error handling
- Advanced features (decorators, generators, context managers)
- Full type hints

```python
# Advanced-appropriate: production patterns
from typing import List, Optional
from contextlib import contextmanager

@contextmanager
def timing_context(operation: str):
    """Context manager for timing operations."""
    import time
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{operation} took {elapsed:.2f} seconds")

def process_data(data: List[dict]) -> Optional[dict]:
    """Process data with proper error handling and logging."""
    with timing_context("Data processing"):
        # Implementation with comprehensive error handling
        pass
```

## Code Comments in Teaching Examples

### When to Comment

**Always comment**:
- Non-obvious logic
- Why something is done (not just what)
- Edge case handling
- Complex algorithms

**In teaching examples, also comment**:
- What each major section does
- Connections to concepts being taught
- Expected values or outputs

### Comment Style

```python
# Good: Explains why
# Use binary search because list is already sorted
result = binary_search(sorted_list, target)

# Less helpful: States the obvious
# Search the list
result = binary_search(sorted_list, target)
```

## Magic Numbers and Constants

```python
# BAD: Magic numbers
if age > 18:
    allow_access()

# GOOD: Named constants
ADULT_AGE = 18
if age >= ADULT_AGE:
    allow_access()
```

## Testing Examples

Include simple assertions or test cases when appropriate:

```python
def add(a, b):
    """Add two numbers."""
    return a + b

# Example usage with expected output
result = add(5, 3)
assert result == 8, "5 + 3 should equal 8"
print(f"add(5, 3) = {result}")  # Output: add(5, 3) = 8
```

## Further Reading

- PEP 8: https://pep8.org/
- PEP 257 (Docstring Conventions): https://www.python.org/dev/peps/pep-0257/
- Python Type Hints: https://docs.python.org/3/library/typing.html
- The Hitchhiker's Guide to Python: https://docs.python-guide.org/
