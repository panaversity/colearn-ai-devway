# PEP 8 Style Guide Summary

## Overview

PEP 8 is Python's official style guide. Following these conventions makes code more readable and consistent. This summary covers the most important PEP 8 rules for teaching examples.

## Indentation

**Use 4 spaces per indentation level. Never use tabs.**

```python
# Correct
def example():
    if condition:
        do_something()
        do_another_thing()

# Wrong
def example():
  if condition:  # Only 2 spaces
    do_something()
```

### Line Continuation

Use implied line continuation inside parentheses:

```python
# Correct: Aligned with opening delimiter
result = function_name(param_one, param_two,
                       param_three, param_four)

# Also correct: Hanging indent
result = function_name(
    param_one, param_two,
    param_three, param_four)
```

## Maximum Line Length

- **79 characters** for code
- **72 characters** for docstrings and comments

```python
# Good: Under 79 characters
def short_function(param1, param2):
    return param1 + param2

# Good: Split long lines
def long_function(param1, param2, param3, param4):
    result = (param1 + param2 +
              param3 + param4)
    return result
```

## Blank Lines

- **2 blank lines** before and after top-level function/class definitions
- **1 blank line** between methods inside a class
- **1 blank line** between logical sections within functions (sparingly)

```python
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

## Imports

### Import Organization

1. Standard library imports
2. Related third-party imports
3. Local application imports

Separate each group with a blank line.

```python
import os
import sys

import numpy as np
import pandas as pd

from myapp import models
from myapp.utils import helper
```

### Import Style

```python
# Correct: Each import on separate line
import os
import sys

# Wrong: Multiple imports on one line (except from)
import os, sys

# Correct: from imports can be grouped
from subprocess import Popen, PIPE
```

## Whitespace

### Around Operators

```python
# Correct
x = 1
y = 2
z = x + y

# Wrong
x=1
y = 2
z = x+y
```

### In Function Calls

```python
# Correct
function(arg1, arg2, kwarg1=value1)

# Wrong: Extra spaces
function( arg1, arg2, kwarg1 = value1 )
```

### In Slicing

```python
# Correct
my_list[1:3]
my_list[start:end]
my_list[start:end:step]

# Wrong
my_list[1: 3]
my_list[start :end]
```

### Avoid Extraneous Whitespace

```python
# Correct
spam(ham[1], {eggs: 2})

# Wrong
spam( ham[ 1 ], { eggs: 2 } )
```

## Naming Conventions

### Functions and Variables

`lowercase_with_underscores`

```python
def calculate_total(price_list):
    item_count = len(price_list)
    return sum(price_list)
```

### Constants

`UPPERCASE_WITH_UNDERSCORES`

```python
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159
```

### Classes

`CapitalizedWords` (PascalCase)

```python
class StudentRecord:
    pass

class HTTPResponseHandler:
    pass
```

### Methods and Instance Variables

`lowercase_with_underscores`

Use one leading underscore for internal/private:

```python
class MyClass:
    def __init__(self):
        self.public_variable = 1
        self._internal_variable = 2

    def public_method(self):
        pass

    def _internal_method(self):
        pass
```

### Special Cases

- **Module-level constants**: `UPPERCASE_WITH_UNDERSCORES`
- **Non-public methods**: `_single_leading_underscore`
- **Name mangling** (to avoid name clashes): `__double_leading_underscore`

## Comments

### Inline Comments

Use sparingly. Separate from code by at least 2 spaces.

```python
x = x + 1  # Compensate for border
```

### Block Comments

```python
# This is a block comment
# explaining what the following code does.
# Each line starts with # and a single space.

def complex_function():
    pass
```

### Documentation Strings (Docstrings)

For all public modules, functions, classes, and methods:

```python
def function_with_docstring(param1, param2):
    """
    Brief description of what the function does.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value
    """
    pass
```

One-line docstrings:

```python
def simple_function():
    """Return the square of 5."""
    return 5 ** 2
```

## String Quotes

Python accepts both `'single'` and `"double"` quotes. **Choose one and be consistent.**

PEP 8 doesn't mandate one over the other, but within a project, pick one style.

```python
# Consistent: all single quotes
name = 'Alice'
message = 'Hello, world!'

# Or consistent: all double quotes
name = "Alice"
message = "Hello, world!"

# Use the other quote type to avoid escaping
message = "It's a beautiful day"  # No escaping needed
```

## Comparisons

### None Comparisons

Use `is` or `is not`, never equality operators:

```python
# Correct
if value is None:
    pass

if value is not None:
    pass

# Wrong
if value == None:
    pass
```

### Boolean Comparisons

Don't compare boolean values to True or False:

```python
# Correct
if greeting:
    pass

# Wrong
if greeting == True:
    pass

# Correct
if not greeting:
    pass

# Wrong
if greeting is False:
    pass
```

### Empty Sequences

```python
# Correct: Use truthiness
if not sequence:
    pass

if sequence:
    pass

# Wrong: Explicit comparison
if len(sequence) == 0:
    pass
```

## Function and Method Arguments

### Default Arguments

Don't use mutable objects as default arguments:

```python
# Wrong: Mutable default argument (dangerous!)
def append_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

# Correct: Use None and create new list
def append_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

### Keyword Arguments

```python
# Correct
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

# Function call styles
greet("Alice")
greet("Alice", greeting="Hi")
greet(name="Alice", greeting="Hi")
```

## Programming Recommendations

### Use `is not` Instead of `not ... is`

```python
# Correct
if value is not None:
    pass

# Wrong
if not value is None:
    pass
```

### Use `.startswith()` and `.endswith()`

```python
# Correct
if filename.endswith('.txt'):
    pass

# Wrong
if filename[-4:] == '.txt':
    pass
```

### Use `isinstance()` for Type Checks

```python
# Correct
if isinstance(obj, int):
    pass

# Wrong
if type(obj) is int:
    pass

# Even better: Duck typing (don't check types when not necessary)
```

## Common PEP 8 Violations to Avoid

### Too Much Whitespace

```python
# Wrong
def function( x , y ):
    return x + y

# Correct
def function(x, y):
    return x + y
```

### Whitespace Before Comma, Semicolon, or Colon

```python
# Wrong
x = (1 , 2)

# Correct
x = (1, 2)
```

### Missing Whitespace After Comma

```python
# Wrong
def function(x,y,z):
    pass

# Correct
def function(x, y, z):
    pass
```

## PEP 8 Checking Tools

Use automated tools to check PEP 8 compliance:

- **pycodestyle** (formerly pep8): `pip install pycodestyle`
- **flake8**: `pip install flake8`
- **pylint**: `pip install pylint`
- **black** (auto-formatter): `pip install black`

```bash
# Check a file
pycodestyle myfile.py
flake8 myfile.py

# Auto-format
black myfile.py
```

## When to Break the Rules

> "A foolish consistency is the hobgoblin of little minds." - PEP 8

Break PEP 8 rules when:
1. Following the rule makes code less readable
2. Consistency with surrounding code is more important
3. Code needs to remain compatible with older versions
4. Breaking 79-character limit improves readability (e.g., long URLs)

## Quick Checklist

- [ ] 4 spaces for indentation (no tabs)
- [ ] Lines ≤ 79 characters
- [ ] 2 blank lines before top-level definitions
- [ ] Imports at top, organized by type
- [ ] `lowercase_with_underscores` for functions/variables
- [ ] `CapitalizedWords` for classes
- [ ] `UPPERCASE_WITH_UNDERSCORES` for constants
- [ ] Docstrings for public functions/classes
- [ ] Spaces around operators: `x = y + z`
- [ ] Use `is` and `is not` for None comparisons
- [ ] No mutable default arguments

## Further Reading

- Full PEP 8: https://pep8.org/
- PEP 257 (Docstrings): https://www.python.org/dev/peps/pep-0257/
- Real Python PEP 8 Guide: https://realpython.com/python-pep8/
