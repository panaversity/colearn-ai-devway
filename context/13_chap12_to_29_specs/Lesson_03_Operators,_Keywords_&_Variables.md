# Lesson 03 Operators, Keywords & Variables

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>



# **Operator and Operand**

In Python (and programming in general), an operand is a value or variable that an operator acts on. Think of it like this:

* **Operator**: A symbol that performs an operation (e.g., +, -, *, /).
* **Operand**: The value(s) or variable(s) that the operator works with.



## **Key Points:**

* Operands are the "inputs" for an operator.
* The number of operands depends on the operator:
    * **Unary operators** (e.g., not, -) work with one operand.
    * **Binary operators** (e.g., +, -, *, /) work with two operands.

## **Unary Operators**
Unary operators work with one operand (a single value or variable). They perform operations on just one thing.

## **Examples:**
1.  **Negative (-):**
      * Changes the sign of the operand.

```python
x = 5
y = -x  # y is now -5
print("y = ", y)
```

**Output:**
```
y =  -5
```

2.  **Logical NOT (not):**
      * Reverses a boolean value.

```python
a = True
b = not a  # b is now False
print("b = ", b)
```

**Output:**
```
b =  False
```

## **Bitwise NOT (~):**

  * Inverts the bits of a number (used in binary operations).

```python
x: int = 5  # Binary: 0101
y: int = ~x  # y is now -6 (binary: 1010, but in two's complement form)
print("y = ", y)
```

**Output:**
```
y =  -6
```

You can print an integer as a binary number in Python using the `bin()` function. Here's an example:

The binary string is prefixed with `'0b'` to indicate that it's a binary number.

```python
print("bin(x) = ",bin(x), type(bin(x)))
```

**Output:**
```
bin(x) =  0b101 <class 'str'>
```

```python
num: int = x
print(format(num, 'b'))  # Output: 1010
print(f"{num:b}")  # Output: 1010
```

**Output:**
```
101
101
```

## **Binary Operators**

Binary operators work with two operands (two values or variables). They perform operations between two things.

### **Examples:**

1. **Arithmetic Operators (+, -, *, /, etc.):**
    * Perform basic math operations.

2. **Comparison Operators (==, !=, >, <, etc.):**
    * Compare two values and return True or False.

3. **Logical Operators (and, or):**
    * Combine boolean values.

4. **Assignment Operators (=, +=, -=, etc.):**
    * Assign values to variables or perform operations while assigning.

<br>

Note: (we will see these operators in action in next topic)


## **Key Difference:**

1.  **Unary Operators**: Work with one operand (e.g., -x, not a).
2.  **Binary Operators**: Work with two operands (e.g., a + b, x > y).

# **Operators in Python**
Operators in Python are `symbols` used to perform operations on variables and values. Python supports several types of operators:





##**1. Arithmetic Operators**
Used for basic mathematical operations.

<br>

| Operator | Name                | Example                           |
|----------|---------------------|-----------------------------------|
| +        | Addition            | 5 + 2 = 7                         |
| -        | Subtraction         | 5 - 2 = 3                         |
| *        | Multiplication      | 5 * 2 = 10                        |
| /        | Division (float)    | 5 / 2 = 2.5                       |
| //       | Floor Division      | 5 // 2 = 2 (removes decimal part) |
| %        | Modulus (remainder) | 5 % 2 = 1                         |
| **       | Exponentiation      | 5 ** 2 = 25                       |
|          |                     |                                   |


<br>

### **Example**

```python
a: int = 10
b: int = 3
print("a + b  = ", a + b)   # 13 Addition
print("a - b  = ", a - b)   # 7 Subtraction
print("a * b  = ", a * b)   # 30 Multiplication
print("a / b  = ", a / b)   # 3.3333333333333335
print("a // b = ", a // b)  # 3 Floor Division
print("a % b  = ", a % b)   # 1 Modulus (remainder)
print("a % b  = ", a ** b)  # 1000 Exponentiation (10 * 10 * 10)
```

**Output:**
```
a + b  =  13
a - b  =  7
a * b  =  30
a / b  =  3.3333333333333335
a // b =  3
a % b  =  1
a % b  =  1000
```

## **2. Comparison (Relational) Operators**
Used to compare two values.

<br>

| Operator | Name                  | Example        |
|----------|-----------------------|----------------|
| ==       | Equal                 | 5 == 5 → True  |
| !=       | Not equal             | 5 != 3 → True  |
| >        | Greater than          | 5 > 3 → True   |
| <        | Less than             | 5 < 3 → False  |
| >=       | Greater than or equal | 5 >= 5 → True  |
| <=       | Less than or equal    | 5 <= 3 → False |
|          |                       |                |
|          |                       |                |  

<br>

### **Example**

```python
x: int = 10
y: int = 5

print("x == y = ", x == y)  # False, Equal
print("x != y = ", x != y)  # True, Not equal
print("x > y  = ", x > y)   # True, Greater than
print("x < y  = ", x < y)   # False, Less than
print("x >= y = ", x >= y)  # True, Greater than or equal
print("x <= y = ", x <= y)  # False, Less than or equal
```

**Output:**
```
x == y =  False
x != y =  True
x > y  =  True
x < y  =  False
x >= y =  True
x <= y =  False
```

Contributor: Hadiqa Gohar from Karachi
## **❓What Are Chained Comparison Operators?**


In Python, we can chain comparison operators together to express multiple comparisons in a single line. This allows for more readable and concise code. Rather than writing multiple comparisons with the same variable repeatedly, Python lets us combine them.


## **Example:**


```python
x: int = 15
if 10 < x < 20:
    print("x is between 10 and 20")
```

**Output:**
```
x is between 10 and 20
```

```python
#Internally, Python interprets this as:
if 10 < x and x < 20:
    print("x is between 10 and 20")
```

## **3. Logical Operators**
Used to combine conditional statements.

<br>

| Operator | Name        | Example                   |
|----------|-------------|---------------------------|
| and      | Logical AND | (5 > 3 and 10 > 5) → True |
| or       | Logical OR  | (5 > 3 or 10 < 5) → True  |
| not      | Logical NOT | not(5 > 3) → False        |


<br>

### **Example**

```python
x: bool = True
y: bool = False

print("x and y = ", x and y)  # False
print("x or y  = ", x or y)   # True
print("not x   = ", not x)    # False
```

**Output:**
```
x and y =  False
x or y  =  True
not x   =  False
```

## **4. Assignment Operators**
Used to assign values to variables.

<br>

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| =        | x = 5   | x = 5         |
| +=       | x += 3  | x = x + 3     |
| -=       | x -= 3  | x = x - 3     |
| *=       | x *= 3  | x = x * 3     |
| /=       | x /= 3  | x = x / 3     |
| //=      | x //= 3 | x = x // 3    |
|          |         |               |
|          |         |               |


```python
x = 5
print("Assignment: x = 5                    ",x)  # Output: 5

x += 3  # Equivalent to x = x + 3
print("Addition Assignment: x += 3          ",x)  # Output: 8

x -= 3  # Equivalent to x = x - 3
print("Subtraction Assignment: x -= 3       ",x)  # Output: 5

x *= 3  # Equivalent to x = x * 3
print("Multiplication Assignment: x *= 3    ",x)  # Output: 15

x /= 3  # Equivalent to x = x / 3
print("Division Assignment: x /= 3          ",x)  # Output: 5.0

x //= 3  # Equivalent to x = x // 3
print("Floor Division Assignment: x //= 3   ",x)  # Output: 1.0
```

**Output:**
```
Assignment: x = 5                     5
Addition Assignment: x += 3           8
Subtraction Assignment: x -= 3        5
Multiplication Assignment: x *= 3     15
Division Assignment: x /= 3           5.0
Floor Division Assignment: x //= 3    1.0
```

Why Use Shorthand Operators?

* `Readability`: Makes the code more concise and easier to read.
* `Efficiency`: Reduces the need to repeat the variable name.
* `Common Practice`: Widely used in Python and other programming languages.

## **walrus operator**



-   The **walrus operator** `:=` was introduced in Python 3.8.
    
-   It allows **assignment and evaluation** in a single expression.
    
-   Great for use in **loops** or **conditional statements** to reduce redundancy.
    
-   Example: `if (n := len(data)) > 10:` assigns and checks in one go.
    
-   It improves readability and efficiency when used wisely!

```python
if (user_input := input("Enter a number: ")) and user_input.isdigit():
    print(f"user_input =  {user_input}")
else:
    print("Invalid input. Please enter a valid number.")
```

**Output:**
```
Enter a number: 7
user_input =  7
```

## **5. Identity Operators**
Used to compare `memory locations.`

<br>

| Operator | Name                                                         | Example    |
|----------|--------------------------------------------------------------|------------|
| is       | Returns True if objects have the same memory location        | x is y     |
| is not   | Returns True if objects do not have the same memory location | x is not y |


### **Example**

```python
a: list = [1, 2, 3]
b: list = [1, 2, 3]
c: list = a

print("a is c     =  ",a is c)       # True  (same object, sharing same memmory space)
print("a is b     =  ",a is b)       # False (different objects, seperate memmory space)
print("a == b     =  ", a == b)      # True  (same values, different memmory space but having same vlaues)
print("a is not b =  ", a is not b)  # True  (True because of different memmory space, although having same memmory space)

print('\n-----\n') # seperator for better output readability

print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("id(c) = ", id(c))
```

**Output:**
```
a is c     =   True
a is b     =   False
a == b     =   True
a is not b =   True

-----

id(a) =  134193929171776
id(b) =  134193940649408
id(c) =  134193929171776
```

## **6. Membership Operators**
Used to check if a value is in a sequence (list, tuple, set, dictionary, etc.).

<br>

| Operator | Name                                         | Example       |
|----------|----------------------------------------------|---------------|
| in       | Returns True if value is in the sequence     | x in list     |
| not in   | Returns True if value is NOT in the sequence | x not in list |

```python
my_list: list = [1, 2, 3, 4, 5]

print("my_list           = ", my_list)            # [1, 2, 3, 4, 5]
print("3 in my_list      = ", 3 in my_list)       # True
print("10 not in my_list = ", 10 not in my_list)  # True

print("\n-----\n")

my_string: str = "Operation Badar"

print("my_string                 = ", my_string)                # Operation Badar
print("'O' in my_string          = ", 'O' in my_string)         # True
print("'Hello' not in my_string  = ", 'Hello' not in my_string) # True
```

**Output:**
```
my_list           =  [1, 2, 3, 4, 5]
3 in my_list      =  True
10 not in my_list =  True

-----

my_string                 =  Operation Badar
'O' in my_string          =  True
'Hello' not in my_string  =  True
```

# **Python Keywords**

Keywords in Python are `reserved words` that have special meanings and serve specific purposes in the language syntax. Python keywords cannot be used as the names of variables, functions, and classes or any other identifier.

```python
import keyword

# Line continuation (`\`) allows printing a statement over multiple lines, improving code readability without breaking the string.
print("The list of \
keywords is : ")

# printing all keywords at once using "kwlist()"
print(keyword.kwlist)
```

**Output:**
```
The list of keywords is : 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

You cant use keywords/ reserved words as variable name.
Uncomment below line to see error

```python
#and: bool = True
```

# **Python Variables**

In Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value. Unlike many other programming languages, **Python variables do not require explicit declaration of type. The type of the variable is `inferred` based on the value assigned.**

(**`inferred`** *meaning deduce or conclude (something) from evidence and reasoning rather than from explicit statements.*)


Variables act as placeholders for data. They allow us to store and reuse values in our program.

<br>


## **Rules for Naming Variables**
To use variables effectively, we must follow Python’s naming rules:

* Variable names can only contain `letters, digits and underscores` (`_`).
* A variable name `cannot` start with a `digit`.
* Variable names are `case-sensitive` (`myVar` and `myvar` are different).
* Avoid using Python keywords (e.g., if, else, for) as variable names.


``` python
# Valid variable names
name = "Alice"
_age = 25
salary2024 = 50000
my_variable = "Python"

# Invalid variable names
2name = "Bob"          # ❌ Starts with a digit
my-variable = "Error"  # ❌ Contains a hyphen
class = "CS101"        # ❌ Uses a reserved keyword
```

## **Different naming conventions**

[Naming Conventions — Camel Case, Pascal Case, Kebab Case, and More](https://medium.com/@code.ceeker/naming-conventions-camel-case-pascal-case-kebab-case-and-more-dc4e515b9652)

## **Special Naming Cases**

<br>

| Type                       | Example      | Used For                                 |
|----------------------------|--------------|------------------------------------------|
| Regular Variable           | total_cost   | General use                              |
| Constant                   | PI = 3.14159 | Constants                                |
| Class Name                 | BankAccount  | Class names                              |
| Private Variable           | _password    | Internal use (not enforced)              |
| Private with Name Mangling | __secret_key | Avoid accidental overrides in subclasses |
| Special Method             | \_\_init\_\_     | Built-in methods                         |



<br>
<br>

## Summary of Naming Conventions

| Convention          | Used For                              | Example                       |
|---------------------|---------------------------------------|-------------------------------|
| snake_case          | Variables & functions                 | user_name, total_price        |
| CamelCase           | Classes                               | BankAccount, DataScienceModel |
| UPPER_CASE          | Constants                             | MAX_SPEED, PI                 |
| _single_underscore  | Private variable (by convention)      | _config                       |
| __double_underscore | Name mangling (avoid external access) | __password                    |
| \_\_dunder\_\_          | Special methods                       | \_\_init\_\_, \_\_str\_\_             |

Here are the naming conventions in Python with their respective names:

1. **CapWords** or **PascalCase**: Class names
2. **snake_case**: Variable names, function names, method names, module names, package names
3. **UPPER_CASE**: Constant names
4. **dunder** (double underscore): Special method names (e.g. `__init__`, `__str__`)

<br>

It's worth noting that the official Python style guide, PEP 8, recommends using **`CapWords`** for `class names` and **`snake_case`** for `variable names`, `function names`, and `other identifiers`.

[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

## **Assigning Different Values**

We can assign different values to multiple variables simultaneously, making the code concise and easier to read.

```python
x, y, z = 1, 2.5, "Python" # Using type hints while assigning mutiple variables simultaneously cause and error invalid syntax

print(x, y, z)
```

**Output:**
```
1 2.5 Python
```

```python
x: int, y: float, z: str = 1, 2.5, "Python" # Using type hints while assigning mutiple variables simultaneously cause and error invalid syntax

print(x, y, z)
```

**Error:**
```
SyntaxError: invalid syntax (<ipython-input-2-1b71593066e5>, line 1)
  File "<ipython-input-2-1b71593066e5>", line 1
    x: int, y: float, z: str = 1, 2.5, "Python" # Using type hints while assigning mutiple variables simultaneously cause and error invalid syntax
          ^
SyntaxError: invalid syntax

```

## **Delete a Variable Using del Keyword**

We can remove a variable from the namespace using the del keyword. This effectively deletes the variable and frees up the memory it was using.

```python
# Assigning value to variable
x: int = 10
print(x)
```

**Output:**
```
10
```

```python
# Removing the variable from memory using del keyword
del x
```

```python
# Trying to print x after deletion will raise an error
# print(x)  # Uncommenting this line will raise NameError: name 'x' is not defined
print(x) # NameError: name 'x' is not defined, because we already delete variable x (del x)
```

**Error:**
```
NameError: name 'x' is not defined
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-29-ef036dc207a0> in <cell line: 0>()
----> 1 print(x) # NameError: name 'x' is not defined, because we already delete variable x (del x)

NameError: name 'x' is not defined
```

### Explanation:

`del` x removes the variable x from memory.
After deletion, trying to access the variable x results in a NameError, indicating that the variable no longer exists.

