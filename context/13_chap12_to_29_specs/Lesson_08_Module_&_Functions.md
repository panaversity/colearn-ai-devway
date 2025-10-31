# Lesson 08 Module & Functions

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>

# **What is a Module in Python?**

A module in Python is a file that contains Python code (functions, classes, variables, or even runnable code) and is used to organize and reuse code efficiently.

* A module is simply a .py file that can be imported and used in other Python programs.

* Modules help keep the code modular, readable, and maintainable.
* Python has built-in modules (like math, random, os) and also allows users to create custom modules.

## **Types of Modules in Python**

### **1. Built-in Modules (Standard Library)**

  * Pre-installed modules in Python.
  * Example: math, random, os, sys


### **Example usage:**



```python
import math
print(math.sqrt(25))  # Output: 5.0
```

**Output:**
```
5.0
```

### **2.  User-Defined Modules (Custom Modules)**

  * Any Python file (.py) you create can be used as a module.


### **Example:**

* Create a file called mymodule.py: `(use VSCode/Cursor on local computer)`

```python
def add(a, b):
    return a + b
```

* Import and use it in another script: `(use VSCode/Cursor on local computer)`

```python
import mymodule
print(mymodule.add(5, 3))  # Output: 8
```

### **3.  External Modules (Third-party Libraries)**

* Installed via pip (pip install module_name).
* Example: numpy, pandas, requests
* Example usage:


```python
!pip install requests
```

**Output:**
```
Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (2.32.3)
Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests) (3.4.1)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests) (2.3.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests) (2025.1.31)
```

```python
import requests
response = requests.get("https://www.example.com")
print(response.status_code)
```

**Output:**
```
200
```

## **How to Import a Module in Python?**

Python provides several ways to import modules:

### **1.  Basic Import**

```python
import math
print(math.pi)  # Output: 3.141592653589793
```

### **2.  Import with Alias (as)**

```python
import numpy as np
print(np.array([1, 2, 3]))
```

**Output:**
```
[1 2 3]
```

### **3. Import Specific Functions or Variables (from ... import ...)**



```python
from math import sqrt, pi
print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793
```

**Output:**
```
4.0
3.141592653589793
```

```python
from math import sqrt as s, pi as p

print(s(16))
print(p )
```

**Output:**
```
4.0
3.141592653589793
```

### **4. Import Everything (from module import *) (Not recommended for large modules)**  

```python
from math import * # wild card
print(sin(0))  # Output: 0.0
```

**Output:**
```
0.0
```

## **Advantages of Using Modules**

✔ **Code Reusability** – Write once, use anywhere.

✔ **Organization** – Keep related functions together.

✔ **Namespace Management** – Prevents variable conflicts.

✔ **Faster Development** – Use existing libraries instead of writing everything from scratch.

#**Understanding Functions in Python**


A Python function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.





```python
# This is a global function because it's defined at the top level of the module.
def my_function():
  print("Hello! World")

# The function can be called from anywhere in the module.
my_function()
```

**Output:**
```
Hello! World
```

A global function in Python is a function that’s defined in the main body of a module, rather than inside another function or class. This means that the function is available throughout the module, and if the module is imported into another file, the function can be accessed from there as well.

## **Key Points:**

### **Scope:**

* Global functions have a module-level scope. They can be called by any code within that module, and if imported, they can be used elsewhere too.

### **Usage:**

* Global functions are typically used to perform tasks that don't depend on a specific object's state. They’re ideal for utility functions, helper functions, or any code that can be reused in various parts of your program.

## **Types of Python Functions**

Python provides the following types of functions −


1)	**Built-in functions**

-   Python's standard library includes number of built-in functions. Some of Python's built-in functions are print(), int(), len(), sum(), etc. These functions are always available, as they are loaded into computer's memory as soon as you start Python interpreter.

2)  **Functions defined in built-in modules**

-   The standard library also bundles a number of modules. Each module defines a group of functions. These functions are not readily available. You need to import them into the memory from their respective modules.

3)  **User-defined functions**

-   In addition to the built-in functions and functions in the built-in modules, you can also create your own functions. These functions are called user-defined functions.

```python
# Built-in functions
print("Hello! World")
```

**Output:**
```
Hello! World
```

```python
# Functions defined in built-in modules
import random
print(random.random())
```

**Output:**
```
0.8194296546403051
```

```python
# User-defined functions
def my_function():
  print("Hello! Operation Badar")

my_function()
```

**Output:**
```
Hello! Operation Badar
```

## **Syntax to Define a Python Function**

```python
def function_name( parameters ):
   "function_docstring"
   function_suite
   return [expression]
   ```

```python
def greetings():
   "This is docstring of greetings function"
   greet = 'Hello World!'
   return greet

message = greetings()
print(message)
```

**Output:**
```
Hello World!
```

## **Pass by Reference vs Value**

Python uses pass by object reference. Immutable objects (e.g. integers) are unchanged, while mutable objects (e.g. lists) are modified. Examples:
* Integers: `x = 5` remains `5` after modification.
* Lists: `x = [1, 2, 3]` becomes `[1, 2, 3, 4]` after appending `4`.

In this example, `x` remains unchanged after the `modify_value` function, because it's an immutable integer. However, `lst` is modified after the `modify_list` function, because it's a mutable list.

```python
def modify_value(x):
    x = 10
    print("Within function:", x)

# Immutable object (integer)
x = 5
print("Original:", x)
modify_value(x)
print("After function:", x)
```

**Output:**
```
Original: 5
Within function: 10
After function: 5
```

```python
def modify_list(lst):
    lst.append(4)
    print("Within function: ", lst, " - ID:", id(lst))

# Mutable object (list)
lst = [1, 2, 3]
print("Original:", lst, " - ID:", id(lst))
modify_list(lst)
print("After function:", lst, " - ID:", id(lst))
```

**Output:**
```
Original: [1, 2, 3]  - ID: 136570433898880
Within function:  [1, 2, 3, 4]  - ID: 136570433898880
After function: [1, 2, 3, 4]  - ID: 136570433898880
```

## **Function Arguments**

Function arguments are the values or variables passed into a function when it is called.

```python
def greetings(name):
   "This is docstring of greetings function"
   print ("Hello {}".format(name))
   return

greetings("Ali")
greetings("Omar")
greetings("Usman")
```

**Output:**
```
Hello Ali
Hello Omar
Hello Usman
```

## **Keyword Arguments**

Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name. This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters.

```python
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="Arif" )
#printinfo(50, "Arif" )
```

**Output:**
```
Name:  Arif
Age  50
```

```python
def add(x: int,y: int=0) -> float:
   return float(x + y)

print(float(add(10,20)))

print(add(y=50.0, x=2.0)) # type hints are not enforced in Python

print(add(x=5))
```

**Output:**
```
30.0
52.0
5.0
```

## **\*  unpacking iterables**

In Python, the * operator is used for unpacking iterables (like lists, tuples, or sets) into individual elements. When you use * before a list (or any iterable) in a function call, it unpacks the list and passes its elements as separate positional arguments to the function.

Example:

```python
def my_sum(*nums):
  print(type(nums),", ", nums)

  return sum(nums)

print("Sum     = ", my_sum(1,2,3,4,5,8,5),"\n")
print("Sum *[] = ", my_sum(*[1,2,3,4,5,8,5]), "\n") # *  unpacking list
print("Sum *() = ", my_sum(*(1,2,3,4,5,8,5))) # *  unpacking tuple
```

**Output:**
```
<class 'tuple'> ,  (1, 2, 3, 4, 5, 8, 5)
Sum     =  28 

<class 'tuple'> ,  (1, 2, 3, 4, 5, 8, 5)
Sum *[] =  28 

<class 'tuple'> ,  (1, 2, 3, 4, 5, 8, 5)
Sum *() =  28
```

## **Default Arguments**

A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.

```python
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="Arif" )
printinfo( name="Arif" )
```

**Output:**
```
Name:  Arif
Age  50
Name:  Arif
Age  35
```

## **Positional-only arguments**

Those arguments that can only be specified by their position in the function call is called as `Positional-only arguments`. They are defined by placing a `"/"` in the function's parameter list after all positional-only parameters.

Example

  - In the following example, we have defined two positional-only arguments namely `"x"` and `"y"`. This method should be called with positional arguments in the order in which the arguments are declared, otherwise, we will get an error.

```python
def posFun(x, y, /, z):
    print(x + y + z)

print("Evaluating positional-only arguments: ")
posFun(1, 2, z=3)

# uncomment to see error
#posFun(x=1, y=2, z=3)
```

**Output:**
```
Evaluating positional-only arguments: 
6
```

```python
# Run to see error
posFun(x=1, y=2, z=3)
```

**Error:**
```
NameError: name 'posFun' is not defined
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-14-90cb35748f4a> in <cell line: 0>()
      1 # Run to see error
----> 2 posFun(x=1, y=2, z=3)

NameError: name 'posFun' is not defined
```

## **Error**

```python
posFun(x=1, y=2, z=3)
```

This means that arguments before the '/' must be specified by their position in the function call and cannot be passed using keyword arguments.

`x` and `y` are declared before the '/', making them positional-only. When you call `posFun(x=1, y=2, z=3)`, you're attempting to pass `x` and `y` as keyword arguments, violating this rule and hence the `TypeError` is raised.

## **Keyword-only arguments**

Those arguments that must be specified by their `name` while calling the function is known as `Keyword-only arguments`. They are defined by placing an `asterisk ("*")` in the function's parameter list before any keyword-only parameters. This type of argument can only be passed to a function as a keyword argument, not a positional argument.

```python
def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5)

posFun(num3=6, num1=8, num2=5)


# TypeError: posFun() takes 0 positional arguments but 3 were given
#posFun(6, 8, 5)
```

**Output:**
```
Evaluating keyword-only arguments: 
240
240
```

## **Arbitrary or Variable-length Arguments**

You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

Syntax for a function with non-keyword variable arguments is this −

```python
  def functionname([formal_args,] *var_args_tuple ):
    "function_docstring"
    function_suite
    return [expression]

```

```python
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print ("*",var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, 70, 90 )
```

**Output:**
```
Output is: 
10
Output is: 
70
* 60
* 50
* 70
* 90
```

## **Python Function with Return Value**

The return keyword as the last statement in function definition indicates end of function block, and the program flow goes back to the calling function. ***`Although reduced indent after the last statement in the block also implies return but using explicit return is a good practice`***.

Along with the flow control, the function can also return value of an expression to the calling function. The value of returned expression can be stored in a variable for further processing.

```python
def add(x,y):
   z=x+y
   return z

a=10
b=20
result = add(a,b)

print ("a = {} b = {} a+b = {}".format(a, b, result))
```

**Output:**
```
a = 10 b = 20 a+b = 30
```

## **The Anonymous Functions**

The functions are called anonymous when they are not declared in the standard manner by using the def keyword. Instead, they are defined using the `lambda keyword`.

### **Syntax**

The syntax of lambda functions contains only a single statement, which is as follows −

```python
lambda [arg1 [,arg2,.....argn]]:expression
```

```python
def add_two(x, y):
  return x + y

my_lambda = lambda x, y:  x + y;

print(my_lambda(1,2))
```

**Output:**
```
3
```

```python
# prompt: sort by value dictionary using lambda function

my_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

sorted_dict
```

**Output:**
```
{'date': 1, 'banana': 2, 'apple': 5, 'cherry': 8}
```

```python
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 50, 20 ))
```

**Output:**
```
Value of total :  30
Value of total :  70
```

## **Scope of Variables**

All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.

The scope of a variable determines the portion of the program where you can access a particular identifier. There are two basic scopes of variables in Python −

  - `Global variables`

  - `Local variables`


**Global vs. Local variables**

Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.

This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions. When you call a function, the variables declared inside it are brought into scope.

```python
total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total)
```

**Output:**
```
Inside the function local total :  30
Outside the function global total :  0
```

##**Arbitrary Keyword Arguments, **kwargs**

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:



```python
def my_function(**student):
  print("\nHis last name is " + student["lname"])

  for key, value in student.items():
    print(key, value)

  print(student)

my_function(fname = "Ali", lname = "Osman")

my_function(fname = "Ali", lname = "Osman", course = "Python - 101", day="Saturday", time="1400 - 1800")

my_dict = {"fname": "Arif", "lname": "Rozani", "course":"101 - 201", "day":"Saturday | Sunday", "role":"Student"}

#my_function(my_dict) # uncomment to see TypeError
my_function(**my_dict) # use ** to unpack the dictionary
```

**Output:**
```

His last name is Osman
fname Ali
lname Osman
{'fname': 'Ali', 'lname': 'Osman'}

His last name is Osman
fname Ali
lname Osman
course Python - 101
day Saturday
time 1400 - 1800
{'fname': 'Ali', 'lname': 'Osman', 'course': 'Python - 101', 'day': 'Saturday', 'time': '1400 - 1800'}

His last name is Rozani
fname Arif
lname Rozani
course 101 - 201
day Saturday | Sunday
role Student
{'fname': 'Arif', 'lname': 'Rozani', 'course': '101 - 201', 'day': 'Saturday | Sunday', 'role': 'Student'}
```

##**Generator Function**

A generator function in Python is a special type of function that allows you to iterate over a sequence of values `without storing the entire sequence in memory`. **Instead of returning a single value using return, a generator function uses the `yield` keyword to produce a series of values, `one at a time`, `on-the-fly`**. This makes generator functions highly `memory-efficient` for working with `large` or `infinite sequences`.

## **Key Features of Generator Functions**

1. **Lazy Evaluation**: Values are generated only when needed, not all at once.

2.  **Memory Efficiency**: Only one value is stored in memory at a time.
3.  **Iterable**: Generator functions return a generator object, which can be iterated over using a for loop or functions like next().
4.  **Resumable**: The state of the generator function is saved between yield calls, allowing it to resume execution from where it left off.

## **Syntax of a Generator Function**

A generator function is defined like a normal function but uses the yield keyword instead of return.

```python
def generator_function():
    yield value

```

## **How Generator Functions Work**

1.  When a generator function is called, it returns a generator object without executing the function body.

2.  The function body executes only when the generator object is iterated over (e.g., using a for loop or next()).
3.  When the yield statement is encountered, the function pauses and returns the yielded value. The function’s state (e.g., local variables) is saved.
4.  The function resumes execution from where it left off the next time next() is called or the generator is iterated over.

### **Example 1: Simple Generator Function**

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

print(gen, " : ", type(gen))

# Iterate over the generator
for value in gen:
    print(value, " : ", type(value))
```

**Output:**
```
<generator object simple_generator at 0x7fc33c3783b0>  :  <class 'generator'>
1  :  <class 'int'>
2  :  <class 'int'>
3  :  <class 'int'>
```

## **Lets produce an error:**

**Once the generator is exhausted, calling next() will raise a StopIteration exception.**

```python
print(next(gen)) #error: StopIteration
```

**Error:**
```
StopIteration: 
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-16-be0d7584d73f> in <cell line: 0>()
----> 1 print(next(gen))

StopIteration: 
```

### **Example 2: Infinite Sequence**

Generators are useful for generating infinite sequences since they don’t store all values in memory.

### **How It Works:**

1.  infinite_sequence():
    * This function starts with num = 0.

    * Inside an infinite while True loop, it yields num and then increments it by 1.
    * Since yield pauses execution, it remembers the state and resumes from there when next() is called.

2.  Creating the Generator:

    * gen = infinite_sequence() initializes the generator.
    

3.  Printing First 5 Numbers:

    * Using next(gen), we retrieve values from the generator five times inside a loop.

    * The next time we call next(gen), execution resumes from where it left off.

```python
def infinite_sequence():
    num = 0
    while True:
        yield num # Since yield pauses execution, it remembers the state and resumes from there when next() is called.
        num += 1

# Create a generator object
gen = infinite_sequence() #initializes the generator.

# Print the first 5 numbers, _ is a throw away variable
for _ in range(5):
    print(next(gen)) # The next time we call next(gen), execution resumes from where it left off.
```

**Output:**
```
0
1
2
3
4
```

```python
def infinite_loop(): #without yield it become infinite
   num = 0
   while True:
       #yield num   # with yield it become generator without yield its a infinite loop
       num += 1
       print("infinite_loop() : num = ", num)

infinite_loop()
```

**Output:**
```
infinite_loop() : num =  1
infinite_loop() : num =  2
infinite_loop() : num =  3
infinite_loop() : num =  4
infinite_loop() : num =  5
infinite_loop() : num =  6
infinite_loop() : num =  7
infinite_loop() : num =  8
infinite_loop() : num =  9
infinite_loop() : num =  10
infinite_loop() : num =  11
infinite_loop() : num =  12
infinite_loop() : num =  13
infinite_loop() : num =  14
infinite_loop() : num =  15
infinite_loop() : num =  16
infinite_loop() : num =  17
infinite_loop() : num =  18
infinite_loop() : num =  19
infinite_loop() : num =  20
infinite_loop() : num =  21
infinite_loop() : num =  22
infinite_loop() : num =  23
infinite_loop() : num =  24
infinite_loop() : num =  25
infinite_loop() : num =  26
infinite_loop() : num =  27
infinite_loop() : num =  28
infinite_loop() : num =  29
infinite_loop() : num =  30
infinite_loop() : num =  31
infinite_loop() : num =  32
infinite_loop() : num =  33
infinite_loop() : num =  34
infinite_loop() : num =  35
infinite_loop() : num =  36
infinite_loop() : num =  37
infinite_loop() : num =  38
infinite_loop() : num =  39
infinite_loop() : num =  40
infinite_loop() : num =  41
infinite_loop() : num =  42
infinite_loop() : num =  43
infinite_loop() : num =  44
infinite_loop() : num =  45
infinite_loop() : num =  46
infinite_loop() : num =  47
infinite_loop() : num =  48
infinite_loop() : num =  49
infinite_loop() : num =  50
infinite_loop() : num =  51
infinite_loop() : num =  52
infinite_loop() : num =  53
infinite_loop() : num =  54
infinite_loop() : num =  55
infinite_loop() : num =  56
infinite_loop() : num =  57
infinite_loop() : num =  58
infinite_loop() : num =  59
infinite_loop() : num =  60
infinite_loop() : num =  61
infinite_loop() : num =  62
infinite_loop() : num =  63
infinite_loop() : num =  64
infinite_loop() : num =  65
infinite_loop() : num =  66
infinite_loop() : num =  67
infinite_loop() : num =  68
infinite_loop() : num =  69
infinite_loop() : num =  70
infinite_loop() : num =  71
infinite_loop() : num =  72
infinite_loop() : num =  73
infinite_loop() : num =  74
infinite_loop() : num =  75
infinite_loop() : num =  76
infinite_loop() : num =  77
infinite_loop() : num =  78
infinite_loop() : num =  79
infinite_loop() : num =  80
infinite_loop() : num =  81
infinite_loop() : num =  82
infinite_loop() : num =  83
infinite_loop() : num =  84
infinite_loop() : num =  85
infinite_loop() : num =  86
infinite_loop() : num =  87
infinite_loop() : num =  88
infinite_loop() : num =  89
infinite_loop() : num =  90
infinite_loop() : num =  91
infinite_loop() : num =  92
infinite_loop() : num =  93
infinite_loop() : num =  94
infinite_loop() : num =  95
infinite_loop() : num =  96
infinite_loop() : num =  97
infinite_loop() : num =  98
infinite_loop() : num =  99
infinite_loop() : num =  100
infinite_loop() : num =  101
infinite_loop() : num =  102
infinite_loop() : num =  103
infinite_loop() : num =  104
infinite_loop() : num =  105
infinite_loop() : num =  106
infinite_loop() : num =  107
infinite_loop() : num =  108
infinite_loop() : num =  109
infinite_loop() : num =  110
infinite_loop() : num =  111
infinite_loop() : num =  112
infinite_loop() : num =  113
infinite_loop() : num =  114
infinite_loop() : num =  115
infinite_loop() : num =  116
infinite_loop() : num =  117
infinite_loop() : num =  118
infinite_loop() : num =  119
infinite_loop() : num =  120
infinite_loop() : num =  121
infinite_loop() : num =  122
infinite_loop() : num =  123
infinite_loop() : num =  124
infinite_loop() : num =  125
infinite_loop() : num =  126
infinite_loop() : num =  127
infinite_loop() : num =  128
infinite_loop() : num =  129
infinite_loop() : num =  130
infinite_loop() : num =  131
infinite_loop() : num =  132
infinite_loop() : num =  133
infinite_loop() : num =  134
infinite_loop() : num =  135
infinite_loop() : num =  136
infinite_loop() : num =  137
infinite_loop() : num =  138
infinite_loop() : num =  139
infinite_loop() : num =  140
infinite_loop() : num =  141
infinite_loop() : num =  142
infinite_loop() : num =  143
infinite_loop() : num =  144
infinite_loop() : num =  145
infinite_loop() : num =  146
infinite_loop() : num =  147
infinite_loop() : num =  148
infinite_loop() : num =  149
infinite_loop() : num =  150
infinite_loop() : num =  151
infinite_loop() : num =  152
infinite_loop() : num =  153
infinite_loop() : num =  154
infinite_loop() : num =  155
infinite_loop() : num =  156
infinite_loop() : num =  157
infinite_loop() : num =  158
infinite_loop() : num =  159
infinite_loop() : num =  160
infinite_loop() : num =  161
infinite_loop() : num =  162
infinite_loop() : num =  163
infinite_loop() : num =  164
infinite_loop() : num =  165
infinite_loop() : num =  166
infinite_loop() : num =  167
infinite_loop() : num =  168
infinite_loop() : num =  169
infinite_loop() : num =  170
infinite_loop() : num =  171
infinite_loop() : num =  172
infinite_loop() : num =  173
infinite_loop() : num =  174
infinite_loop() : num =  175
infinite_loop() : num =  176
infinite_loop() : num =  177
infinite_loop() : num =  178
infinite_loop() : num =  179
infinite_loop() : num =  180
infinite_loop() : num =  181
infinite_loop() : num =  182
infinite_loop() : num =  183
infinite_loop() : num =  184
infinite_loop() : num =  185
infinite_loop() : num =  186
infinite_loop() : num =  187
infinite_loop() : num =  188
infinite_loop() : num =  189
infinite_loop() : num =  190
infinite_loop() : num =  191
infinite_loop() : num =  192
infinite_loop() : num =  193
infinite_loop() : num =  194
infinite_loop() : num =  195
infinite_loop() : num =  196
infinite_loop() : num =  197
infinite_loop() : num =  198
infinite_loop() : num =  199
infinite_loop() : num =  200
infinite_loop() : num =  201
infinite_loop() : num =  202
infinite_loop() : num =  203
infinite_loop() : num =  204
infinite_loop() : num =  205
infinite_loop() : num =  206
infinite_loop() : num =  207
infinite_loop() : num =  208
infinite_loop() : num =  209
infinite_loop() : num =  210
infinite_loop() : num =  211
infinite_loop() : num =  212
infinite_loop() : num =  213
infinite_loop() : num =  214
infinite_loop() : num =  215
infinite_loop() : num =  216
infinite_loop() : num =  217
infinite_loop() : num =  218
infinite_loop() : num =  219
infinite_loop() : num =  220
infinite_loop() : num =  221
infinite_loop() : num =  222
infinite_loop() : num =  223
infinite_loop() : num =  224
infinite_loop() : num =  225
infinite_loop() : num =  226
infinite_loop() : num =  227
infinite_loop() : num =  228
infinite_loop() : num =  229
infinite_loop() : num =  230
infinite_loop() : num =  231
infinite_loop() : num =  232
infinite_loop() : num =  233
infinite_loop() : num =  234
infinite_loop() : num =  235
infinite_loop() : num =  236
infinite_loop() : num =  237
infinite_loop() : num =  238
infinite_loop() : num =  239
infinite_loop() : num =  240
infinite_loop() : num =  241
infinite_loop() : num =  242
infinite_loop() : num =  243
infinite_loop() : num =  244
infinite_loop() : num =  245
infinite_loop() : num =  246
infinite_loop() : num =  247
infinite_loop() : num =  248
infinite_loop() : num =  249
infinite_loop() : num =  250
infinite_loop() : num =  251
infinite_loop() : num =  252
infinite_loop() : num =  253
infinite_loop() : num =  254
infinite_loop() : num =  255
infinite_loop() : num =  256
infinite_loop() : num =  257
infinite_loop() : num =  258
infinite_loop() : num =  259
infinite_loop() : num =  260
infinite_loop() : num =  261
infinite_loop() : num =  262
infinite_loop() : num =  263
infinite_loop() : num =  264
infinite_loop() : num =  265
infinite_loop() : num =  266
infinite_loop() : num =  267
infinite_loop() : num =  268
infinite_loop() : num =  269
infinite_loop() : num =  270
infinite_loop() : num =  271
infinite_loop() : num =  272
infinite_loop() : num =  273
infinite_loop() : num =  274
infinite_loop() : num =  275
infinite_loop() : num =  276
infinite_loop() : num =  277
infinite_loop() : num =  278
infinite_loop() : num =  279
infinite_loop() : num =  280
infinite_loop() : num =  281
infinite_loop() : num =  282
infinite_loop() : num =  283
infinite_loop() : num =  284
infinite_loop() : num =  285
infinite_loop() : num =  286
infinite_loop() : num =  287
infinite_loop() : num =  288
infinite_loop() : num =  289
infinite_loop() : num =  290
infinite_loop() : num =  291
infinite_loop() : num =  292
infinite_loop() : num =  293
infinite_loop() : num =  294
infinite_loop() : num =  295
infinite_loop() : num =  296
infinite_loop() : num =  297
infinite_loop() : num =  298
infinite_loop() : num =  299
infinite_loop() : num =  300
infinite_loop() : num =  301
infinite_loop() : num =  302
infinite_loop() : num =  303
infinite_loop() : num =  304
infinite_loop() : num =  305
infinite_loop() : num =  306
infinite_loop() : num =  307
infinite_loop() : num =  308
infinite_loop() : num =  309
infinite_loop() : num =  310
infinite_loop() : num =  311
infinite_loop() : num =  312
infinite_loop() : num =  313
infinite_loop() : num =  314
infinite_loop() : num =  315
infinite_loop() : num =  316
infinite_loop() : num =  317
infinite_loop() : num =  318
infinite_loop() : num =  319
infinite_loop() : num =  320
infinite_loop() : num =  321
infinite_loop() : num =  322
infinite_loop() : num =  323
infinite_loop() : num =  324
infinite_loop() : num =  325
infinite_loop() : num =  326
infinite_loop() : num =  327
infinite_loop() : num =  328
infinite_loop() : num =  329
infinite_loop() : num =  330
infinite_loop() : num =  331
infinite_loop() : num =  332
infinite_loop() : num =  333
infinite_loop() : num =  334
infinite_loop() : num =  335
infinite_loop() : num =  336
infinite_loop() : num =  337
infinite_loop() : num =  338
infinite_loop() : num =  339
infinite_loop() : num =  340
infinite_loop() : num =  341
infinite_loop() : num =  342
infinite_loop() : num =  343
infinite_loop() : num =  344
infinite_loop() : num =  345
infinite_loop() : num =  346
infinite_loop() : num =  347
infinite_loop() : num =  348
infinite_loop() : num =  349
infinite_loop() : num =  350
infinite_loop() : num =  351
infinite_loop() : num =  352
infinite_loop() : num =  353
infinite_loop() : num =  354
infinite_loop() : num =  355
infinite_loop() : num =  356
infinite_loop() : num =  357
infinite_loop() : num =  358
infinite_loop() : num =  359
infinite_loop() : num =  360
infinite_loop() : num =  361
infinite_loop() : num =  362
infinite_loop() : num =  363
infinite_loop() : num =  364
infinite_loop() : num =  365
infinite_loop() : num =  366
infinite_loop() : num =  367
infinite_loop() : num =  368
infinite_loop() : num =  369
infinite_loop() : num =  370
infinite_loop() : num =  371
infinite_loop() : num =  372
infinite_loop() : num =  373
infinite_loop() : num =  374
infinite_loop() : num =  375
infinite_loop() : num =  376
infinite_loop() : num =  377
infinite_loop() : num =  378
infinite_loop() : num =  379
infinite_loop() : num =  380
infinite_loop() : num =  381
infinite_loop() : num =  382
infinite_loop() : num =  383
infinite_loop() : num =  384
infinite_loop() : num =  385
infinite_loop() : num =  386
infinite_loop() : num =  387
infinite_loop() : num =  388
infinite_loop() : num =  389
infinite_loop() : num =  390
infinite_loop() : num =  391
infinite_loop() : num =  392
infinite_loop() : num =  393
infinite_loop() : num =  394
infinite_loop() : num =  395
infinite_loop() : num =  396
infinite_loop() : num =  397
infinite_loop() : num =  398
infinite_loop() : num =  399
infinite_loop() : num =  400
infinite_loop() : num =  401
infinite_loop() : num =  402
infinite_loop() : num =  403
infinite_loop() : num =  404
infinite_loop() : num =  405
infinite_loop() : num =  406
infinite_loop() : num =  407
infinite_loop() : num =  408
infinite_loop() : num =  409
infinite_loop() : num =  410
infinite_loop() : num =  411
infinite_loop() : num =  412
infinite_loop() : num =  413
infinite_loop() : num =  414
infinite_loop() : num =  415
infinite_loop() : num =  416
infinite_loop() : num =  417
infinite_loop() : num =  418
infinite_loop() : num =  419
infinite_loop() : num =  420
infinite_loop() : num =  421
infinite_loop() : num =  422
infinite_loop() : num =  423
infinite_loop() : num =  424
infinite_loop() : num =  425
infinite_loop() : num =  426
infinite_loop() : num =  427
infinite_loop() : num =  428
infinite_loop() : num =  429
infinite_loop() : num =  430
infinite_loop() : num =  431
infinite_loop() : num =  432
infinite_loop() : num =  433
infinite_loop() : num =  434
infinite_loop() : num =  435
infinite_loop() : num =  436
infinite_loop() : num =  437
infinite_loop() : num =  438
infinite_loop() : num =  439
infinite_loop() : num =  440
infinite_loop() : num =  441
infinite_loop() : num =  442
infinite_loop() : num =  443
infinite_loop() : num =  444
infinite_loop() : num =  445
infinite_loop() : num =  446
infinite_loop() : num =  447
infinite_loop() : num =  448
infinite_loop() : num =  449
infinite_loop() : num =  450
infinite_loop() : num =  451
infinite_loop() : num =  452
infinite_loop() : num =  453
infinite_loop() : num =  454
infinite_loop() : num =  455
infinite_loop() : num =  456
infinite_loop() : num =  457
infinite_loop() : num =  458
infinite_loop() : num =  459
infinite_loop() : num =  460
infinite_loop() : num =  461
infinite_loop() : num =  462
infinite_loop() : num =  463
infinite_loop() : num =  464
infinite_loop() : num =  465
infinite_loop() : num =  466
infinite_loop() : num =  467
infinite_loop() : num =  468
infinite_loop() : num =  469
infinite_loop() : num =  470
infinite_loop() : num =  471
infinite_loop() : num =  472
infinite_loop() : num =  473
infinite_loop() : num =  474
infinite_loop() : num =  475
infinite_loop() : num =  476
infinite_loop() : num =  477
infinite_loop() : num =  478
infinite_loop() : num =  479
infinite_loop() : num =  480
infinite_loop() : num =  481
infinite_loop() : num =  482
infinite_loop() : num =  483
infinite_loop() : num =  484
infinite_loop() : num =  485
infinite_loop() : num =  486
infinite_loop() : num =  487
infinite_loop() : num =  488
infinite_loop() : num =  489
infinite_loop() : num =  490
infinite_loop() : num =  491
infinite_loop() : num =  492
infinite_loop() : num =  493
infinite_loop() : num =  494
infinite_loop() : num =  495
infinite_loop() : num =  496
infinite_loop() : num =  497
infinite_loop() : num =  498
infinite_loop() : num =  499
infinite_loop() : num =  500
infinite_loop() : num =  501
infinite_loop() : num =  502
infinite_loop() : num =  503
infinite_loop() : num =  504
infinite_loop() : num =  505
infinite_loop() : num =  506
infinite_loop() : num =  507
infinite_loop() : num =  508
infinite_loop() : num =  509
infinite_loop() : num =  510
infinite_loop() : num =  511
infinite_loop() : num =  512
infinite_loop() : num =  513
infinite_loop() : num =  514
infinite_loop() : num =  515
infinite_loop() : num =  516
infinite_loop() : num =  517
infinite_loop() : num =  518
infinite_loop() : num =  519
infinite_loop() : num =  520
infinite_loop() : num =  521
infinite_loop() : num =  522
infinite_loop() : num =  523
infinite_loop() : num =  524
infinite_loop() : num =  525
infinite_loop() : num =  526
infinite_loop() : num =  527
infinite_loop() : num =  528
infinite_loop() : num =  529
infinite_loop() : num =  530
infinite_loop() : num =  531
infinite_loop() : num =  532
infinite_loop() : num =  533
infinite_loop() : num =  534
infinite_loop() : num =  535
infinite_loop() : num =  536
infinite_loop() : num =  537
infinite_loop() : num =  538
infinite_loop() : num =  539
infinite_loop() : num =  540
infinite_loop() : num =  541
infinite_loop() : num =  542
infinite_loop() : num =  543
infinite_loop() : num =  544
infinite_loop() : num =  545
infinite_loop() : num =  546
infinite_loop() : num =  547
infinite_loop() : num =  548
infinite_loop() : num =  549
infinite_loop() : num =  550
infinite_loop() : num =  551
infinite_loop() : num =  552
infinite_loop() : num =  553
infinite_loop() : num =  554
infinite_loop() : num =  555
infinite_loop() : num =  556
infinite_loop() : num =  557
infinite_loop() : num =  558
infinite_loop() : num =  559
infinite_loop() : num =  560
infinite_loop() : num =  561
infinite_loop() : num =  562
infinite_loop() : num =  563
infinite_loop() : num =  564
infinite_loop() : num =  565
infinite_loop() : num =  566
infinite_loop() : num =  567
infinite_loop() : num =  568
infinite_loop() : num =  569
infinite_loop() : num =  570
infinite_loop() : num =  571
infinite_loop() : num =  572
infinite_loop() : num =  573
infinite_loop() : num =  574
infinite_loop() : num =  575
infinite_loop() : num =  576
infinite_loop() : num =  577
infinite_loop() : num =  578
infinite_loop() : num =  579
infinite_loop() : num =  580
infinite_loop() : num =  581
infinite_loop() : num =  582
infinite_loop() : num =  583
infinite_loop() : num =  584
infinite_loop() : num =  585
infinite_loop() : num =  586
infinite_loop() : num =  587
infinite_loop() : num =  588
infinite_loop() : num =  589
infinite_loop() : num =  590
infinite_loop() : num =  591
infinite_loop() : num =  592
infinite_loop() : num =  593
infinite_loop() : num =  594
infinite_loop() : num =  595
infinite_loop() : num =  596
infinite_loop() : num =  597
infinite_loop() : num =  598
infinite_loop() : num =  599
infinite_loop() : num =  600
infinite_loop() : num =  601
infinite_loop() : num =  602
infinite_loop() : num =  603
infinite_loop() : num =  604
infinite_loop() : num =  605
infinite_loop() : num =  606
infinite_loop() : num =  607
infinite_loop() : num =  608
infinite_loop() : num =  609
infinite_loop() : num =  610
infinite_loop() : num =  611
infinite_loop() : num =  612
infinite_loop() : num =  613
infinite_loop() : num =  614
infinite_loop() : num =  615
infinite_loop() : num =  616
infinite_loop() : num =  617
infinite_loop() : num =  618
infinite_loop() : num =  619
infinite_loop() : num =  620
infinite_loop() : num =  621
infinite_loop() : num =  622
infinite_loop() : num =  623
infinite_loop() : num =  624
infinite_loop() : num =  625
infinite_loop() : num =  626
infinite_loop() : num =  627
infinite_loop() : num =  628
infinite_loop() : num =  629
infinite_loop() : num =  630
infinite_loop() : num =  631
infinite_loop() : num =  632
infinite_loop() : num =  633
infinite_loop() : num =  634
infinite_loop() : num =  635
infinite_loop() : num =  636
infinite_loop() : num =  637
infinite_loop() : num =  638
infinite_loop() : num =  639
infinite_loop() : num =  640
infinite_loop() : num =  641
infinite_loop() : num =  642
infinite_loop() : num =  643
infinite_loop() : num =  644
infinite_loop() : num =  645
infinite_loop() : num =  646
infinite_loop() : num =  647
infinite_loop() : num =  648
infinite_loop() : num =  649
infinite_loop() : num =  650
infinite_loop() : num =  651
infinite_loop() : num =  652
infinite_loop() : num =  653
infinite_loop() : num =  654
infinite_loop() : num =  655
infinite_loop() : num =  656
infinite_loop() : num =  657
infinite_loop() : num =  658
infinite_loop() : num =  659
infinite_loop() : num =  660
infinite_loop() : num =  661
infinite_loop() : num =  662
infinite_loop() : num =  663
infinite_loop() : num =  664
infinite_loop() : num =  665
infinite_loop() : num =  666
infinite_loop() : num =  667
infinite_loop() : num =  668
infinite_loop() : num =  669
infinite_loop() : num =  670
infinite_loop() : num =  671
infinite_loop() : num =  672
infinite_loop() : num =  673
infinite_loop() : num =  674
infinite_loop() : num =  675
infinite_loop() : num =  676
infinite_loop() : num =  677
infinite_loop() : num =  678
infinite_loop() : num =  679
infinite_loop() : num =  680
infinite_loop() : num =  681
infinite_loop() : num =  682
infinite_loop() : num =  683
infinite_loop() : num =  684
infinite_loop() : num =  685
infinite_loop() : num =  686
infinite_loop() : num =  687
infinite_loop() : num =  688
infinite_loop() : num =  689
infinite_loop() : num =  690
infinite_loop() : num =  691
infinite_loop() : num =  692
infinite_loop() : num =  693
infinite_loop() : num =  694
infinite_loop() : num =  695
infinite_loop() : num =  696
infinite_loop() : num =  697
infinite_loop() : num =  698
infinite_loop() : num =  699
infinite_loop() : num =  700
infinite_loop() : num =  701
infinite_loop() : num =  702
infinite_loop() : num =  703
infinite_loop() : num =  704
infinite_loop() : num =  705
infinite_loop() : num =  706
infinite_loop() : num =  707
infinite_loop() : num =  708
infinite_loop() : num =  709
infinite_loop() : num =  710
infinite_loop() : num =  711
infinite_loop() : num =  712
infinite_loop() : num =  713
infinite_loop() : num =  714
infinite_loop() : num =  715
infinite_loop() : num =  716
infinite_loop() : num =  717
infinite_loop() : num =  718
infinite_loop() : num =  719
infinite_loop() : num =  720
infinite_loop() : num =  721
infinite_loop() : num =  722
infinite_loop() : num =  723
infinite_loop() : num =  724
infinite_loop() : num =  725
infinite_loop() : num =  726
infinite_loop() : num =  727
infinite_loop() : num =  728
infinite_loop() : num =  729
infinite_loop() : num =  730
infinite_loop() : num =  731
infinite_loop() : num =  732
infinite_loop() : num =  733
infinite_loop() : num =  734
infinite_loop() : num =  735
infinite_loop() : num =  736
infinite_loop() : num =  737
infinite_loop() : num =  738
infinite_loop() : num =  739
infinite_loop() : num =  740
infinite_loop() : num =  741
infinite_loop() : num =  742
infinite_loop() : num =  743
infinite_loop() : num =  744
infinite_loop() : num =  745
infinite_loop() : num =  746
infinite_loop() : num =  747
infinite_loop() : num =  748
infinite_loop() : num =  749
infinite_loop() : num =  750
infinite_loop() : num =  751
infinite_loop() : num =  752
infinite_loop() : num =  753
infinite_loop() : num =  754
infinite_loop() : num =  755
infinite_loop() : num =  756
infinite_loop() : num =  757
infinite_loop() : num =  758
infinite_loop() : num =  759
infinite_loop() : num =  760
infinite_loop() : num =  761
infinite_loop() : num =  762
infinite_loop() : num =  763
infinite_loop() : num =  764
infinite_loop() : num =  765
infinite_loop() : num =  766
infinite_loop() : num =  767
infinite_loop() : num =  768
infinite_loop() : num =  769
infinite_loop() : num =  770
infinite_loop() : num =  771
infinite_loop() : num =  772
infinite_loop() : num =  773
infinite_loop() : num =  774
infinite_loop() : num =  775
infinite_loop() : num =  776
infinite_loop() : num =  777
infinite_loop() : num =  778
infinite_loop() : num =  779
infinite_loop() : num =  780
infinite_loop() : num =  781
infinite_loop() : num =  782
infinite_loop() : num =  783
infinite_loop() : num =  784
infinite_loop() : num =  785
infinite_loop() : num =  786
infinite_loop() : num =  787
infinite_loop() : num =  788
infinite_loop() : num =  789
infinite_loop() : num =  790
infinite_loop() : num =  791
infinite_loop() : num =  792
infinite_loop() : num =  793
infinite_loop() : num =  794
infinite_loop() : num =  795
infinite_loop() : num =  796
infinite_loop() : num =  797
infinite_loop() : num =  798
infinite_loop() : num =  799
infinite_loop() : num =  800
infinite_loop() : num =  801
infinite_loop() : num =  802
infinite_loop() : num =  803
infinite_loop() : num =  804
infinite_loop() : num =  805
infinite_loop() : num =  806
infinite_loop() : num =  807
infinite_loop() : num =  808
infinite_loop() : num =  809
infinite_loop() : num =  810
infinite_loop() : num =  811
infinite_loop() : num =  812
infinite_loop() : num =  813
infinite_loop() : num =  814
infinite_loop() : num =  815
infinite_loop() : num =  816
infinite_loop() : num =  817
infinite_loop() : num =  818
infinite_loop() : num =  819
infinite_loop() : num =  820
infinite_loop() : num =  821
infinite_loop() : num =  822
infinite_loop() : num =  823
infinite_loop() : num =  824
infinite_loop() : num =  825
infinite_loop() : num =  826
infinite_loop() : num =  827
infinite_loop() : num =  828
infinite_loop() : num =  829
infinite_loop() : num =  830
infinite_loop() : num =  831
infinite_loop() : num =  832
infinite_loop() : num =  833
infinite_loop() : num =  834
infinite_loop() : num =  835
infinite_loop() : num =  836
infinite_loop() : num =  837
infinite_loop() : num =  838
infinite_loop() : num =  839
infinite_loop() : num =  840
infinite_loop() : num =  841
infinite_loop() : num =  842
infinite_loop() : num =  843
infinite_loop() : num =  844
infinite_loop() : num =  845
infinite_loop() : num =  846
infinite_loop() : num =  847
infinite_loop() : num =  848
infinite_loop() : num =  849
infinite_loop() : num =  850
infinite_loop() : num =  851
infinite_loop() : num =  852
infinite_loop() : num =  853
infinite_loop() : num =  854
infinite_loop() : num =  855
infinite_loop() : num =  856
infinite_loop() : num =  857
infinite_loop() : num =  858
infinite_loop() : num =  859
infinite_loop() : num =  860
infinite_loop() : num =  861
infinite_loop() : num =  862
infinite_loop() : num =  863
infinite_loop() : num =  864
infinite_loop() : num =  865
infinite_loop() : num =  866
infinite_loop() : num =  867
infinite_loop() : num =  868
infinite_loop() : num =  869
infinite_loop() : num =  870
infinite_loop() : num =  871
infinite_loop() : num =  872
infinite_loop() : num =  873
infinite_loop() : num =  874
infinite_loop() : num =  875
infinite_loop() : num =  876
infinite_loop() : num =  877
infinite_loop() : num =  878
infinite_loop() : num =  879
infinite_loop() : num =  880
infinite_loop() : num =  881
infinite_loop() : num =  882
infinite_loop() : num =  883
infinite_loop() : num =  884
infinite_loop() : num =  885
infinite_loop() : num =  886
infinite_loop() : num =  887
infinite_loop() : num =  888
infinite_loop() : num =  889
infinite_loop() : num =  890
infinite_loop() : num =  891
infinite_loop() : num =  892
infinite_loop() : num =  893
infinite_loop() : num =  894
infinite_loop() : num =  895
infinite_loop() : num =  896
infinite_loop() : num =  897
infinite_loop() : num =  898
infinite_loop() : num =  899
infinite_loop() : num =  900
infinite_loop() : num =  901
infinite_loop() : num =  902
infinite_loop() : num =  903
infinite_loop() : num =  904
infinite_loop() : num =  905
infinite_loop() : num =  906
infinite_loop() : num =  907
infinite_loop() : num =  908
infinite_loop() : num =  909
infinite_loop() : num =  910
infinite_loop() : num =  911
infinite_loop() : num =  912
infinite_loop() : num =  913
infinite_loop() : num =  914
infinite_loop() : num =  915
infinite_loop() : num =  916
infinite_loop() : num =  917
infinite_loop() : num =  918
infinite_loop() : num =  919
infinite_loop() : num =  920
infinite_loop() : num =  921
infinite_loop() : num =  922
infinite_loop() : num =  923
infinite_loop() : num =  924
infinite_loop() : num =  925
infinite_loop() : num =  926
infinite_loop() : num =  927
infinite_loop() : num =  928
infinite_loop() : num =  929
infinite_loop() : num =  930
infinite_loop() : num =  931
infinite_loop() : num =  932
infinite_loop() : num =  933
infinite_loop() : num =  934
infinite_loop() : num =  935
infinite_loop() : num =  936
infinite_loop() : num =  937
infinite_loop() : num =  938
infinite_loop() : num =  939
infinite_loop() : num =  940
infinite_loop() : num =  941
infinite_loop() : num =  942
infinite_loop() : num =  943
infinite_loop() : num =  944
infinite_loop() : num =  945
infinite_loop() : num =  946
infinite_loop() : num =  947
infinite_loop() : num =  948
infinite_loop() : num =  949
infinite_loop() : num =  950
infinite_loop() : num =  951
infinite_loop() : num =  952
infinite_loop() : num =  953
infinite_loop() : num =  954
infinite_loop() : num =  955
infinite_loop() : num =  956
infinite_loop() : num =  957
infinite_loop() : num =  958
infinite_loop() : num =  959
infinite_loop() : num =  960
infinite_loop() : num =  961
infinite_loop() : num =  962
infinite_loop() : num =  963
infinite_loop() : num =  964
infinite_loop() : num =  965
infinite_loop() : num =  966
infinite_loop() : num =  967
infinite_loop() : num =  968
infinite_loop() : num =  969
infinite_loop() : num =  970
infinite_loop() : num =  971
infinite_loop() : num =  972
infinite_loop() : num =  973
infinite_loop() : num =  974
infinite_loop() : num =  975
infinite_loop() : num =  976
infinite_loop() : num =  977
infinite_loop() : num =  978
infinite_loop() : num =  979
infinite_loop() : num =  980
infinite_loop() : num =  981
infinite_loop() : num =  982
infinite_loop() : num =  983
infinite_loop() : num =  984
infinite_loop() : num =  985
infinite_loop() : num =  986
infinite_loop() : num =  987
infinite_loop() : num =  988
infinite_loop() : num =  989
infinite_loop() : num =  990
infinite_loop() : num =  991
infinite_loop() : num =  992
infinite_loop() : num =  993
infinite_loop() : num =  994
infinite_loop() : num =  995
infinite_loop() : num =  996
infinite_loop() : num =  997
infinite_loop() : num =  998
infinite_loop() : num =  999
infinite_loop() : num =  1000
infinite_loop() : num =  1001
infinite_loop() : num =  1002
infinite_loop() : num =  1003
infinite_loop() : num =  1004
infinite_loop() : num =  1005
infinite_loop() : num =  1006
infinite_loop() : num =  1007
infinite_loop() : num =  1008
infinite_loop() : num =  1009
infinite_loop() : num =  1010
infinite_loop() : num =  1011
infinite_loop() : num =  1012
infinite_loop() : num =  1013
infinite_loop() : num =  1014
infinite_loop() : num =  1015
infinite_loop() : num =  1016
infinite_loop() : num =  1017
infinite_loop() : num =  1018
infinite_loop() : num =  1019
infinite_loop() : num =  1020
infinite_loop() : num =  1021
infinite_loop() : num =  1022
infinite_loop() : num =  1023
infinite_loop() : num =  1024
infinite_loop() : num =  1025
infinite_loop() : num =  1026
infinite_loop() : num =  1027
infinite_loop() : num =  1028
infinite_loop() : num =  1029
infinite_loop() : num =  1030
infinite_loop() : num =  1031
infinite_loop() : num =  1032
infinite_loop() : num =  1033
infinite_loop() : num =  1034
infinite_loop() : num =  1035
infinite_loop() : num =  1036
infinite_loop() : num =  1037
infinite_loop() : num =  1038
infinite_loop() : num =  1039
infinite_loop() : num =  1040
infinite_loop() : num =  1041
infinite_loop() : num =  1042
infinite_loop() : num =  1043
infinite_loop() : num =  1044
infinite_loop() : num =  1045
infinite_loop() : num =  1046
infinite_loop() : num =  1047
infinite_loop() : num =  1048
infinite_loop() : num =  1049
infinite_loop() : num =  1050
infinite_loop() : num =  1051
infinite_loop() : num =  1052
infinite_loop() : num =  1053
infinite_loop() : num =  1054
infinite_loop() : num =  1055
infinite_loop() : num =  1056
infinite_loop() : num =  1057
infinite_loop() : num =  1058
infinite_loop() : num =  1059
infinite_loop() : num =  1060
infinite_loop() : num =  1061
infinite_loop() : num =  1062
infinite_loop() : num =  1063
infinite_loop() : num =  1064
infinite_loop() : num =  1065
infinite_loop() : num =  1066
infinite_loop() : num =  1067
infinite_loop() : num =  1068
infinite_loop() : num =  1069
infinite_loop() : num =  1070
infinite_loop() : num =  1071
infinite_loop() : num =  1072
infinite_loop() : num =  1073
infinite_loop() : num =  1074
infinite_loop() : num =  1075
infinite_loop() : num =  1076
infinite_loop() : num =  1077
infinite_loop() : num =  1078
infinite_loop() : num =  1079
infinite_loop() : num =  1080
infinite_loop() : num =  1081
infinite_loop() : num =  1082
infinite_loop() : num =  1083
infinite_loop() : num =  1084
infinite_loop() : num =  1085
infinite_loop() : num =  1086
infinite_loop() : num =  1087
infinite_loop() : num =  1088
infinite_loop() : num =  1089
infinite_loop() : num =  1090
infinite_loop() : num =  1091
infinite_loop() : num =  1092
infinite_loop() : num =  1093
infinite_loop() : num =  1094
infinite_loop() : num =  1095
infinite_loop() : num =  1096
infinite_loop() : num =  1097
infinite_loop() : num =  1098
infinite_loop() : num =  1099
infinite_loop() : num =  1100
infinite_loop() : num =  1101
infinite_loop() : num =  1102
infinite_loop() : num =  1103
infinite_loop() : num =  1104
infinite_loop() : num =  1105
infinite_loop() : num =  1106
infinite_loop() : num =  1107
infinite_loop() : num =  1108
infinite_loop() : num =  1109
infinite_loop() : num =  1110
infinite_loop() : num =  1111
infinite_loop() : num =  1112
infinite_loop() : num =  1113
infinite_loop() : num =  1114
infinite_loop() : num =  1115
infinite_loop() : num =  1116
infinite_loop() : num =  1117
infinite_loop() : num =  1118
infinite_loop() : num =  1119
infinite_loop() : num =  1120
infinite_loop() : num =  1121
infinite_loop() : num =  1122
infinite_loop() : num =  1123
infinite_loop() : num =  1124
infinite_loop() : num =  1125
infinite_loop() : num =  1126
infinite_loop() : num =  1127
infinite_loop() : num =  1128
infinite_loop() : num =  1129
infinite_loop() : num =  1130
infinite_loop() : num =  1131
infinite_loop() : num =  1132
infinite_loop() : num =  1133
infinite_loop() : num =  1134
infinite_loop() : num =  1135
infinite_loop() : num =  1136
infinite_loop() : num =  1137
infinite_loop() : num =  1138
infinite_loop() : num =  1139
infinite_loop() : num =  1140
infinite_loop() : num =  1141
infinite_loop() : num =  1142
infinite_loop() : num =  1143
infinite_loop() : num =  1144
infinite_loop() : num =  1145
infinite_loop() : num =  1146
infinite_loop() : num =  1147
infinite_loop() : num =  1148
infinite_loop() : num =  1149
infinite_loop() : num =  1150
infinite_loop() : num =  1151
infinite_loop() : num =  1152
infinite_loop() : num =  1153
infinite_loop() : num =  1154
infinite_loop() : num =  1155
infinite_loop() : num =  1156
infinite_loop() : num =  1157
infinite_loop() : num =  1158
infinite_loop() : num =  1159
infinite_loop() : num =  1160
infinite_loop() : num =  1161
infinite_loop() : num =  1162
infinite_loop() : num =  1163
infinite_loop() : num =  1164
infinite_loop() : num =  1165
infinite_loop() : num =  1166
infinite_loop() : num =  1167
infinite_loop() : num =  1168
infinite_loop() : num =  1169
infinite_loop() : num =  1170
infinite_loop() : num =  1171
infinite_loop() : num =  1172
infinite_loop() : num =  1173
infinite_loop() : num =  1174
infinite_loop() : num =  1175
infinite_loop() : num =  1176
infinite_loop() : num =  1177
infinite_loop() : num =  1178
infinite_loop() : num =  1179
infinite_loop() : num =  1180
infinite_loop() : num =  1181
infinite_loop() : num =  1182
infinite_loop() : num =  1183
infinite_loop() : num =  1184
infinite_loop() : num =  1185
infinite_loop() : num =  1186
infinite_loop() : num =  1187
infinite_loop() : num =  1188
infinite_loop() : num =  1189
infinite_loop() : num =  1190
infinite_loop() : num =  1191
infinite_loop() : num =  1192
infinite_loop() : num =  1193
infinite_loop() : num =  1194
infinite_loop() : num =  1195
infinite_loop() : num =  1196
infinite_loop() : num =  1197
infinite_loop() : num =  1198
infinite_loop() : num =  1199
infinite_loop() : num =  1200
infinite_loop() : num =  1201
infinite_loop() : num =  1202
infinite_loop() : num =  1203
infinite_loop() : num =  1204
infinite_loop() : num =  1205
infinite_loop() : num =  1206
infinite_loop() : num =  1207
infinite_loop() : num =  1208
infinite_loop() : num =  1209
infinite_loop() : num =  1210
infinite_loop() : num =  1211
infinite_loop() : num =  1212
infinite_loop() : num =  1213
infinite_loop() : num =  1214
infinite_loop() : num =  1215
infinite_loop() : num =  1216
infinite_loop() : num =  1217
infinite_loop() : num =  1218
infinite_loop() : num =  1219
infinite_loop() : num =  1220
infinite_loop() : num =  1221
infinite_loop() : num =  1222
infinite_loop() : num =  1223
infinite_loop() : num =  1224
infinite_loop() : num =  1225
infinite_loop() : num =  1226
infinite_loop() : num =  1227
infinite_loop() : num =  1228
infinite_loop() : num =  1229
infinite_loop() : num =  1230
infinite_loop() : num =  1231
infinite_loop() : num =  1232
infinite_loop() : num =  1233
infinite_loop() : num =  1234
infinite_loop() : num =  1235
infinite_loop() : num =  1236
infinite_loop() : num =  1237
infinite_loop() : num =  1238
infinite_loop() : num =  1239
infinite_loop() : num =  1240
infinite_loop() : num =  1241
infinite_loop() : num =  1242
infinite_loop() : num =  1243
infinite_loop() : num =  1244
infinite_loop() : num =  1245
infinite_loop() : num =  1246
infinite_loop() : num =  1247
infinite_loop() : num =  1248
infinite_loop() : num =  1249
infinite_loop() : num =  1250
infinite_loop() : num =  1251
infinite_loop() : num =  1252
infinite_loop() : num =  1253
infinite_loop() : num =  1254
infinite_loop() : num =  1255
infinite_loop() : num =  1256
infinite_loop() : num =  1257
infinite_loop() : num =  1258
infinite_loop() : num =  1259
infinite_loop() : num =  1260
infinite_loop() : num =  1261
infinite_loop() : num =  1262
infinite_loop() : num =  1263
infinite_loop() : num =  1264
infinite_loop() : num =  1265
infinite_loop() : num =  1266
infinite_loop() : num =  1267
infinite_loop() : num =  1268
infinite_loop() : num =  1269
infinite_loop() : num =  1270
infinite_loop() : num =  1271
infinite_loop() : num =  1272
infinite_loop() : num =  1273
infinite_loop() : num =  1274
infinite_loop() : num =  1275
infinite_loop() : num =  1276
infinite_loop() : num =  1277
infinite_loop() : num =  1278
infinite_loop() : num =  1279
infinite_loop() : num =  1280
infinite_loop() : num =  1281
infinite_loop() : num =  1282
infinite_loop() : num =  1283
infinite_loop() : num =  1284
infinite_loop() : num =  1285
infinite_loop() : num =  1286
infinite_loop() : num =  1287
infinite_loop() : num =  1288
infinite_loop() : num =  1289
infinite_loop() : num =  1290
infinite_loop() : num =  1291
infinite_loop() : num =  1292
infinite_loop() : num =  1293
infinite_loop() : num =  1294
infinite_loop() : num =  1295
infinite_loop() : num =  1296
infinite_loop() : num =  1297
infinite_loop() : num =  1298
infinite_loop() : num =  1299
infinite_loop() : num =  1300
infinite_loop() : num =  1301
infinite_loop() : num =  1302
infinite_loop() : num =  1303
infinite_loop() : num =  1304
infinite_loop() : num =  1305
infinite_loop() : num =  1306
infinite_loop() : num =  1307
infinite_loop() : num =  1308
infinite_loop() : num =  1309
infinite_loop() : num =  1310
infinite_loop() : num =  1311
infinite_loop() : num =  1312
infinite_loop() : num =  1313
infinite_loop() : num =  1314
infinite_loop() : num =  1315
infinite_loop() : num =  1316
infinite_loop() : num =  1317
infinite_loop() : num =  1318
infinite_loop() : num =  1319
infinite_loop() : num =  1320
infinite_loop() : num =  1321
infinite_loop() : num =  1322
infinite_loop() : num =  1323
infinite_loop() : num =  1324
infinite_loop() : num =  1325
infinite_loop() : num =  1326
infinite_loop() : num =  1327
infinite_loop() : num =  1328
infinite_loop() : num =  1329
infinite_loop() : num =  1330
infinite_loop() : num =  1331
infinite_loop() : num =  1332
infinite_loop() : num =  1333
infinite_loop() : num =  1334
infinite_loop() : num =  1335
infinite_loop() : num =  1336
infinite_loop() : num =  1337
infinite_loop() : num =  1338
infinite_loop() : num =  1339
infinite_loop() : num =  1340
infinite_loop() : num =  1341
infinite_loop() : num =  1342
infinite_loop() : num =  1343
infinite_loop() : num =  1344
infinite_loop() : num =  1345
infinite_loop() : num =  1346
infinite_loop() : num =  1347
infinite_loop() : num =  1348
infinite_loop() : num =  1349
infinite_loop() : num =  1350
infinite_loop() : num =  1351
infinite_loop() : num =  1352
infinite_loop() : num =  1353
infinite_loop() : num =  1354
infinite_loop() : num =  1355
infinite_loop() : num =  1356
infinite_loop() : num =  1357
infinite_loop() : num =  1358
infinite_loop() : num =  1359
infinite_loop() : num =  1360
infinite_loop() : num =  1361
infinite_loop() : num =  1362
infinite_loop() : num =  1363
infinite_loop() : num =  1364
infinite_loop() : num =  1365
infinite_loop() : num =  1366
infinite_loop() : num =  1367
infinite_loop() : num =  1368
infinite_loop() : num =  1369
infinite_loop() : num =  1370
infinite_loop() : num =  1371
infinite_loop() : num =  1372
infinite_loop() : num =  1373
infinite_loop() : num =  1374
infinite_loop() : num =  1375
infinite_loop() : num =  1376
infinite_loop() : num =  1377
infinite_loop() : num =  1378
infinite_loop() : num =  1379
infinite_loop() : num =  1380
infinite_loop() : num =  1381
infinite_loop() : num =  1382
infinite_loop() : num =  1383
infinite_loop() : num =  1384
infinite_loop() : num =  1385
infinite_loop() : num =  1386
infinite_loop() : num =  1387
infinite_loop() : num =  1388
infinite_loop() : num =  1389
infinite_loop() : num =  1390
infinite_loop() : num =  1391
infinite_loop() : num =  1392
infinite_loop() : num =  1393
infinite_loop() : num =  1394
infinite_loop() : num =  1395
infinite_loop() : num =  1396
infinite_loop() : num =  1397
infinite_loop() : num =  1398
infinite_loop() : num =  1399
infinite_loop() : num =  1400
infinite_loop() : num =  1401
infinite_loop() : num =  1402
infinite_loop() : num =  1403
infinite_loop() : num =  1404
infinite_loop() : num =  1405
infinite_loop() : num =  1406
infinite_loop() : num =  1407
infinite_loop() : num =  1408
infinite_loop() : num =  1409
infinite_loop() : num =  1410
infinite_loop() : num =  1411
infinite_loop() : num =  1412
infinite_loop() : num =  1413
infinite_loop() : num =  1414
infinite_loop() : num =  1415
infinite_loop() : num =  1416
infinite_loop() : num =  1417
infinite_loop() : num =  1418
infinite_loop() : num =  1419
infinite_loop() : num =  1420
infinite_loop() : num =  1421
infinite_loop() : num =  1422
infinite_loop() : num =  1423
infinite_loop() : num =  1424
infinite_loop() : num =  1425
infinite_loop() : num =  1426
infinite_loop() : num =  1427
infinite_loop() : num =  1428
infinite_loop() : num =  1429
infinite_loop() : num =  1430
infinite_loop() : num =  1431
infinite_loop() : num =  1432
infinite_loop() : num =  1433
infinite_loop() : num =  1434
infinite_loop() : num =  1435
infinite_loop() : num =  1436
infinite_loop() : num =  1437
infinite_loop() : num =  1438
infinite_loop() : num =  1439
infinite_loop() : num =  1440
infinite_loop() : num =  1441
infinite_loop() : num =  1442
infinite_loop() : num =  1443
infinite_loop() : num =  1444
infinite_loop() : num =  1445
infinite_loop() : num =  1446
infinite_loop() : num =  1447
infinite_loop() : num =  1448
infinite_loop() : num =  1449
infinite_loop() : num =  1450
infinite_loop() : num =  1451
infinite_loop() : num =  1452
infinite_loop() : num =  1453
infinite_loop() : num =  1454
infinite_loop() : num =  1455
infinite_loop() : num =  1456
infinite_loop() : num =  1457
infinite_loop() : num =  1458
infinite_loop() : num =  1459
infinite_loop() : num =  1460
infinite_loop() : num =  1461
infinite_loop() : num =  1462
infinite_loop() : num =  1463
infinite_loop() : num =  1464
infinite_loop() : num =  1465
infinite_loop() : num =  1466
infinite_loop() : num =  1467
infinite_loop() : num =  1468
infinite_loop() : num =  1469
infinite_loop() : num =  1470
infinite_loop() : num =  1471
infinite_loop() : num =  1472
infinite_loop() : num =  1473
infinite_loop() : num =  1474
infinite_loop() : num =  1475
infinite_loop() : num =  1476
infinite_loop() : num =  1477
infinite_loop() : num =  1478
infinite_loop() : num =  1479
infinite_loop() : num =  1480
infinite_loop() : num =  1481
infinite_loop() : num =  1482
infinite_loop() : num =  1483
infinite_loop() : num =  1484
infinite_loop() : num =  1485
infinite_loop() : num =  1486
infinite_loop() : num =  1487
infinite_loop() : num =  1488
infinite_loop() : num =  1489
infinite_loop() : num =  1490
infinite_loop() : num =  1491
infinite_loop() : num =  1492
infinite_loop() : num =  1493
infinite_loop() : num =  1494
infinite_loop() : num =  1495
infinite_loop() : num =  1496
infinite_loop() : num =  1497
infinite_loop() : num =  1498
infinite_loop() : num =  1499
infinite_loop() : num =  1500
infinite_loop() : num =  1501
infinite_loop() : num =  1502
infinite_loop() : num =  1503
infinite_loop() : num =  1504
infinite_loop() : num =  1505
infinite_loop() : num =  1506
infinite_loop() : num =  1507
infinite_loop() : num =  1508
infinite_loop() : num =  1509
infinite_loop() : num =  1510
infinite_loop() : num =  1511
infinite_loop() : num =  1512
infinite_loop() : num =  1513
infinite_loop() : num =  1514
infinite_loop() : num =  1515
infinite_loop() : num =  1516
infinite_loop() : num =  1517
infinite_loop() : num =  1518
infinite_loop() : num =  1519
infinite_loop() : num =  1520
infinite_loop() : num =  1521
infinite_loop() : num =  1522
infinite_loop() : num =  1523
infinite_loop() : num =  1524
infinite_loop() : num =  1525
infinite_loop() : num =  1526
infinite_loop() : num =  1527
infinite_loop() : num =  1528
infinite_loop() : num =  1529
infinite_loop() : num =  1530
infinite_loop() : num =  1531
infinite_loop() : num =  1532
infinite_loop() : num =  1533
infinite_loop() : num =  1534
infinite_loop() : num =  1535
infinite_loop() : num =  1536
infinite_loop() : num =  1537
infinite_loop() : num =  1538
infinite_loop() : num =  1539
infinite_loop() : num =  1540
infinite_loop() : num =  1541
infinite_loop() : num =  1542
infinite_loop() : num =  1543
infinite_loop() : num =  1544
infinite_loop() : num =  1545
infinite_loop() : num =  1546
infinite_loop() : num =  1547
infinite_loop() : num =  1548
infinite_loop() : num =  1549
infinite_loop() : num =  1550
infinite_loop() : num =  1551
infinite_loop() : num =  1552
infinite_loop() : num =  1553
infinite_loop() : num =  1554
infinite_loop() : num =  1555
infinite_loop() : num =  1556
infinite_loop() : num =  1557
infinite_loop() : num =  1558
infinite_loop() : num =  1559
infinite_loop() : num =  1560
infinite_loop() : num =  1561
infinite_loop() : num =  1562
infinite_loop() : num =  1563
infinite_loop() : num =  1564
infinite_loop() : num =  1565
infinite_loop() : num =  1566
infinite_loop() : num =  1567
infinite_loop() : num =  1568
infinite_loop() : num =  1569
infinite_loop() : num =  1570
infinite_loop() : num =  1571
infinite_loop() : num =  1572
infinite_loop() : num =  1573
infinite_loop() : num =  1574
infinite_loop() : num =  1575
infinite_loop() : num =  1576
infinite_loop() : num =  1577
infinite_loop() : num =  1578
infinite_loop() : num =  1579
infinite_loop() : num =  1580
infinite_loop() : num =  1581
infinite_loop() : num =  1582
infinite_loop() : num =  1583
infinite_loop() : num =  1584
infinite_loop() : num =  1585
infinite_loop() : num =  1586
infinite_loop() : num =  1587
infinite_loop() : num =  1588
infinite_loop() : num =  1589
infinite_loop() : num =  1590
infinite_loop() : num =  1591
infinite_loop() : num =  1592
infinite_loop() : num =  1593
infinite_loop() : num =  1594
infinite_loop() : num =  1595
infinite_loop() : num =  1596
infinite_loop() : num =  1597
infinite_loop() : num =  1598
infinite_loop() : num =  1599
infinite_loop() : num =  1600
infinite_loop() : num =  1601
infinite_loop() : num =  1602
infinite_loop() : num =  1603
infinite_loop() : num =  1604
infinite_loop() : num =  1605
infinite_loop() : num =  1606
infinite_loop() : num =  1607
infinite_loop() : num =  1608
infinite_loop() : num =  1609
infinite_loop() : num =  1610
infinite_loop() : num =  1611
infinite_loop() : num =  1612
infinite_loop() : num =  1613
infinite_loop() : num =  1614
infinite_loop() : num =  1615
infinite_loop() : num =  1616
infinite_loop() : num =  1617
infinite_loop() : num =  1618
infinite_loop() : num =  1619
infinite_loop() : num =  1620
infinite_loop() : num =  1621
infinite_loop() : num =  1622
infinite_loop() : num =  1623
infinite_loop() : num =  1624
infinite_loop() : num =  1625
infinite_loop() : num =  1626
infinite_loop() : num =  1627
infinite_loop() : num =  1628
infinite_loop() : num =  1629
infinite_loop() : num =  1630
infinite_loop() : num =  1631
infinite_loop() : num =  1632
infinite_loop() : num =  1633
infinite_loop() : num =  1634
infinite_loop() : num =  1635
infinite_loop() : num =  1636
infinite_loop() : num =  1637
infinite_loop() : num =  1638
infinite_loop() : num =  1639
infinite_loop() : num =  1640
infinite_loop() : num =  1641
infinite_loop() : num =  1642
infinite_loop() : num =  1643
infinite_loop() : num =  1644
infinite_loop() : num =  1645
infinite_loop() : num =  1646
infinite_loop() : num =  1647
infinite_loop() : num =  1648
infinite_loop() : num =  1649
infinite_loop() : num =  1650
infinite_loop() : num =  1651
infinite_loop() : num =  1652
infinite_loop() : num =  1653
infinite_loop() : num =  1654
infinite_loop() : num =  1655
infinite_loop() : num =  1656
infinite_loop() : num =  1657
infinite_loop() : num =  1658
infinite_loop() : num =  1659
infinite_loop() : num =  1660
infinite_loop() : num =  1661
infinite_loop() : num =  1662
infinite_loop() : num =  1663
infinite_loop() : num =  1664
infinite_loop() : num =  1665
infinite_loop() : num =  1666
infinite_loop() : num =  1667
infinite_loop() : num =  1668
infinite_loop() : num =  1669
infinite_loop() : num =  1670
infinite_loop() : num =  1671
infinite_loop() : num =  1672
infinite_loop() : num =  1673
infinite_loop() : num =  1674
infinite_loop() : num =  1675
infinite_loop() : num =  1676
infinite_loop() : num =  1677
infinite_loop() : num =  1678
infinite_loop() : num =  1679
infinite_loop() : num =  1680
infinite_loop() : num =  1681
infinite_loop() : num =  1682
infinite_loop() : num =  1683
infinite_loop() : num =  1684
infinite_loop() : num =  1685
infinite_loop() : num =  1686
infinite_loop() : num =  1687
infinite_loop() : num =  1688
infinite_loop() : num =  1689
infinite_loop() : num =  1690
infinite_loop() : num =  1691
infinite_loop() : num =  1692
infinite_loop() : num =  1693
infinite_loop() : num =  1694
infinite_loop() : num =  1695
infinite_loop() : num =  1696
infinite_loop() : num =  1697
infinite_loop() : num =  1698
infinite_loop() : num =  1699
infinite_loop() : num =  1700
infinite_loop() : num =  1701
infinite_loop() : num =  1702
infinite_loop() : num =  1703
infinite_loop() : num =  1704
infinite_loop() : num =  1705
infinite_loop() : num =  1706
infinite_loop() : num =  1707
infinite_loop() : num =  1708
infinite_loop() : num =  1709
infinite_loop() : num =  1710
infinite_loop() : num =  1711
infinite_loop() : num =  1712
infinite_loop() : num =  1713
infinite_loop() : num =  1714
infinite_loop() : num =  1715
infinite_loop() : num =  1716
infinite_loop() : num =  1717
infinite_loop() : num =  1718
infinite_loop() : num =  1719
infinite_loop() : num =  1720
infinite_loop() : num =  1721
infinite_loop() : num =  1722
infinite_loop() : num =  1723
infinite_loop() : num =  1724
infinite_loop() : num =  1725
infinite_loop() : num =  1726
infinite_loop() : num =  1727
infinite_loop() : num =  1728
infinite_loop() : num =  1729
infinite_loop() : num =  1730
infinite_loop() : num =  1731
infinite_loop() : num =  1732
infinite_loop() : num =  1733
infinite_loop() : num =  1734
infinite_loop() : num =  1735
infinite_loop() : num =  1736
infinite_loop() : num =  1737
infinite_loop() : num =  1738
infinite_loop() : num =  1739
infinite_loop() : num =  1740
infinite_loop() : num =  1741
infinite_loop() : num =  1742
infinite_loop() : num =  1743
infinite_loop() : num =  1744
infinite_loop() : num =  1745
infinite_loop() : num =  1746
infinite_loop() : num =  1747
infinite_loop() : num =  1748
infinite_loop() : num =  1749
infinite_loop() : num =  1750
infinite_loop() : num =  1751
infinite_loop() : num =  1752
infinite_loop() : num =  1753
infinite_loop() : num =  1754
infinite_loop() : num =  1755
infinite_loop() : num =  1756
infinite_loop() : num =  1757
infinite_loop() : num =  1758
infinite_loop() : num =  1759
infinite_loop() : num =  1760
infinite_loop() : num =  1761
infinite_loop() : num =  1762
infinite_loop() : num =  1763
infinite_loop() : num =  1764
infinite_loop() : num =  1765
infinite_loop() : num =  1766
infinite_loop() : num =  1767
infinite_loop() : num =  1768
infinite_loop() : num =  1769
infinite_loop() : num =  1770
infinite_loop() : num =  1771
infinite_loop() : num =  1772
infinite_loop() : num =  1773
infinite_loop() : num =  1774
infinite_loop() : num =  1775
infinite_loop() : num =  1776
infinite_loop() : num =  1777
infinite_loop() : num =  1778
infinite_loop() : num =  1779
infinite_loop() : num =  1780
infinite_loop() : num =  1781
infinite_loop() : num =  1782
infinite_loop() : num =  1783
infinite_loop() : num =  1784
infinite_loop() : num =  1785
infinite_loop() : num =  1786
infinite_loop() : num =  1787
infinite_loop() : num =  1788
infinite_loop() : num =  1789
infinite_loop() : num =  1790
infinite_loop() : num =  1791
infinite_loop() : num =  1792
infinite_loop() : num =  1793
infinite_loop() : num =  1794
infinite_loop() : num =  1795
infinite_loop() : num =  1796
infinite_loop() : num =  1797
infinite_loop() : num =  1798
infinite_loop() : num =  1799
infinite_loop() : num =  1800
infinite_loop() : num =  1801
infinite_loop() : num =  1802
infinite_loop() : num =  1803
infinite_loop() : num =  1804
infinite_loop() : num =  1805
infinite_loop() : num =  1806
infinite_loop() : num =  1807
infinite_loop() : num =  1808
infinite_loop() : num =  1809
infinite_loop() : num =  1810
infinite_loop() : num =  1811
infinite_loop() : num =  1812
infinite_loop() : num =  1813
infinite_loop() : num =  1814
infinite_loop() : num =  1815
infinite_loop() : num =  1816
infinite_loop() : num =  1817
infinite_loop() : num =  1818
infinite_loop() : num =  1819
infinite_loop() : num =  1820
infinite_loop() : num =  1821
infinite_loop() : num =  1822
infinite_loop() : num =  1823
infinite_loop() : num =  1824
infinite_loop() : num =  1825
infinite_loop() : num =  1826
infinite_loop() : num =  1827
infinite_loop() : num =  1828
infinite_loop() : num =  1829
infinite_loop() : num =  1830
infinite_loop() : num =  1831
infinite_loop() : num =  1832
infinite_loop() : num =  1833
infinite_loop() : num =  1834
infinite_loop() : num =  1835
infinite_loop() : num =  1836
infinite_loop() : num =  1837
infinite_loop() : num =  1838
infinite_loop() : num =  1839
infinite_loop() : num =  1840
infinite_loop() : num =  1841
infinite_loop() : num =  1842
infinite_loop() : num =  1843
infinite_loop() : num =  1844
infinite_loop() : num =  1845
infinite_loop() : num =  1846
infinite_loop() : num =  1847
infinite_loop() : num =  1848
infinite_loop() : num =  1849
infinite_loop() : num =  1850
infinite_loop() : num =  1851
infinite_loop() : num =  1852
infinite_loop() : num =  1853
infinite_loop() : num =  1854
infinite_loop() : num =  1855
infinite_loop() : num =  1856
infinite_loop() : num =  1857
infinite_loop() : num =  1858
infinite_loop() : num =  1859
infinite_loop() : num =  1860
infinite_loop() : num =  1861
infinite_loop() : num =  1862
infinite_loop() : num =  1863
infinite_loop() : num =  1864
infinite_loop() : num =  1865
infinite_loop() : num =  1866
infinite_loop() : num =  1867
infinite_loop() : num =  1868
infinite_loop() : num =  1869
infinite_loop() : num =  1870
infinite_loop() : num =  1871
infinite_loop() : num =  1872
infinite_loop() : num =  1873
infinite_loop() : num =  1874
infinite_loop() : num =  1875
infinite_loop() : num =  1876
infinite_loop() : num =  1877
infinite_loop() : num =  1878
infinite_loop() : num =  1879
infinite_loop() : num =  1880
infinite_loop() : num =  1881
infinite_loop() : num =  1882
infinite_loop() : num =  1883
infinite_loop() : num =  1884
infinite_loop() : num =  1885
infinite_loop() : num =  1886
infinite_loop() : num =  1887
infinite_loop() : num =  1888
infinite_loop() : num =  1889
infinite_loop() : num =  1890
infinite_loop() : num =  1891
infinite_loop() : num =  1892
infinite_loop() : num =  1893
infinite_loop() : num =  1894
infinite_loop() : num =  1895
infinite_loop() : num =  1896
infinite_loop() : num =  1897
infinite_loop() : num =  1898
infinite_loop() : num =  1899
infinite_loop() : num =  1900
infinite_loop() : num =  1901
infinite_loop() : num =  1902
infinite_loop() : num =  1903
infinite_loop() : num =  1904
infinite_loop() : num =  1905
infinite_loop() : num =  1906
infinite_loop() : num =  1907
infinite_loop() : num =  1908
infinite_loop() : num =  1909
infinite_loop() : num =  1910
infinite_loop() : num =  1911
infinite_loop() : num =  1912
infinite_loop() : num =  1913
infinite_loop() : num =  1914
infinite_loop() : num =  1915
infinite_loop() : num =  1916
infinite_loop() : num =  1917
infinite_loop() : num =  1918
infinite_loop() : num =  1919
infinite_loop() : num =  1920
infinite_loop() : num =  1921
infinite_loop() : num =  1922
infinite_loop() : num =  1923
infinite_loop() : num =  1924
infinite_loop() : num =  1925
infinite_loop() : num =  1926
infinite_loop() : num =  1927
infinite_loop() : num =  1928
infinite_loop() : num =  1929
infinite_loop() : num =  1930
infinite_loop() : num =  1931
infinite_loop() : num =  1932
infinite_loop() : num =  1933
infinite_loop() : num =  1934
infinite_loop() : num =  1935
infinite_loop() : num =  1936
infinite_loop() : num =  1937
infinite_loop() : num =  1938
infinite_loop() : num =  1939
infinite_loop() : num =  1940
infinite_loop() : num =  1941
infinite_loop() : num =  1942
infinite_loop() : num =  1943
infinite_loop() : num =  1944
infinite_loop() : num =  1945
infinite_loop() : num =  1946
infinite_loop() : num =  1947
infinite_loop() : num =  1948
infinite_loop() : num =  1949
infinite_loop() : num =  1950
infinite_loop() : num =  1951
infinite_loop() : num =  1952
infinite_loop() : num =  1953
infinite_loop() : num =  1954
infinite_loop() : num =  1955
infinite_loop() : num =  1956
infinite_loop() : num =  1957
infinite_loop() : num =  1958
infinite_loop() : num =  1959
infinite_loop() : num =  1960
infinite_loop() : num =  1961
infinite_loop() : num =  1962
infinite_loop() : num =  1963
infinite_loop() : num =  1964
infinite_loop() : num =  1965
infinite_loop() : num =  1966
infinite_loop() : num =  1967
infinite_loop() : num =  1968
infinite_loop() : num =  1969
infinite_loop() : num =  1970
infinite_loop() : num =  1971
infinite_loop() : num =  1972
infinite_loop() : num =  1973
infinite_loop() : num =  1974
infinite_loop() : num =  1975
infinite_loop() : num =  1976
infinite_loop() : num =  1977
infinite_loop() : num =  1978
infinite_loop() : num =  1979
infinite_loop() : num =  1980
infinite_loop() : num =  1981
infinite_loop() : num =  1982
infinite_loop() : num =  1983
infinite_loop() : num =  1984
infinite_loop() : num =  1985
infinite_loop() : num =  1986
infinite_loop() : num =  1987
infinite_loop() : num =  1988
infinite_loop() : num =  1989
infinite_loop() : num =  1990
infinite_loop() : num =  1991
infinite_loop() : num =  1992
infinite_loop() : num =  1993
infinite_loop() : num =  1994
infinite_loop() : num =  1995
infinite_loop() : num =  1996
infinite_loop() : num =  1997
infinite_loop() : num =  1998
infinite_loop() : num =  1999
infinite_loop() : num =  2000
infinite_loop() : num =  2001
infinite_loop() : num =  2002
infinite_loop() : num =  2003
infinite_loop() : num =  2004
infinite_loop() : num =  2005
infinite_loop() : num =  2006
infinite_loop() : num =  2007
infinite_loop() : num =  2008
infinite_loop() : num =  2009
infinite_loop() : num =  2010
infinite_loop() : num =  2011
infinite_loop() : num =  2012
infinite_loop() : num =  2013
infinite_loop() : num =  2014
infinite_loop() : num =  2015
infinite_loop() : num =  2016
infinite_loop() : num =  2017
infinite_loop() : num =  2018
infinite_loop() : num =  2019
infinite_loop() : num =  2020
infinite_loop() : num =  2021
infinite_loop() : num =  2022
infinite_loop() : num =  2023
infinite_loop() : num =  2024
infinite_loop() : num =  2025
infinite_loop() : num =  2026
infinite_loop() : num =  2027
infinite_loop() : num =  2028
infinite_loop() : num =  2029
infinite_loop() : num =  2030
infinite_loop() : num =  2031
infinite_loop() : num =  2032
infinite_loop() : num =  2033
infinite_loop() : num =  2034
infinite_loop() : num =  2035
infinite_loop() : num =  2036
infinite_loop() : num =  2037
infinite_loop() : num =  2038
infinite_loop() : num =  2039
infinite_loop() : num =  2040
infinite_loop() : num =  2041
infinite_loop() : num =  2042
infinite_loop() : num =  2043
infinite_loop() : num =  2044
infinite_loop() : num =  2045
infinite_loop() : num =  2046
infinite_loop() : num =  2047
infinite_loop() : num =  2048
infinite_loop() : num =  2049
infinite_loop() : num =  2050
infinite_loop() : num =  2051
infinite_loop() : num =  2052
infinite_loop() : num =  2053
infinite_loop() : num =  2054
infinite_loop() : num =  2055
infinite_loop() : num =  2056
infinite_loop() : num =  2057
infinite_loop() : num =  2058
infinite_loop() : num =  2059
infinite_loop() : num =  2060
infinite_loop() : num =  2061
infinite_loop() : num =  2062
infinite_loop() : num =  2063
infinite_loop() : num =  2064
infinite_loop() : num =  2065
infinite_loop() : num =  2066
infinite_loop() : num =  2067
infinite_loop() : num =  2068
infinite_loop() : num =  2069
infinite_loop() : num =  2070
infinite_loop() : num =  2071
infinite_loop() : num =  2072
infinite_loop() : num =  2073
infinite_loop() : num =  2074
infinite_loop() : num =  2075
infinite_loop() : num =  2076
infinite_loop() : num =  2077
infinite_loop() : num =  2078
infinite_loop() : num =  2079
infinite_loop() : num =  2080
infinite_loop() : num =  2081
infinite_loop() : num =  2082
infinite_loop() : num =  2083
infinite_loop() : num =  2084
infinite_loop() : num =  2085
infinite_loop() : num =  2086
infinite_loop() : num =  2087
infinite_loop() : num =  2088
infinite_loop() : num =  2089
infinite_loop() : num =  2090
infinite_loop() : num =  2091
infinite_loop() : num =  2092
infinite_loop() : num =  2093
infinite_loop() : num =  2094
infinite_loop() : num =  2095
infinite_loop() : num =  2096
infinite_loop() : num =  2097
infinite_loop() : num =  2098
infinite_loop() : num =  2099
infinite_loop() : num =  2100
infinite_loop() : num =  2101
infinite_loop() : num =  2102
infinite_loop() : num =  2103
infinite_loop() : num =  2104
infinite_loop() : num =  2105
infinite_loop() : num =  2106
infinite_loop() : num =  2107
infinite_loop() : num =  2108
infinite_loop() : num =  2109
infinite_loop() : num =  2110
infinite_loop() : num =  2111
infinite_loop() : num =  2112
infinite_loop() : num =  2113
infinite_loop() : num =  2114
infinite_loop() : num =  2115
infinite_loop() : num =  2116
infinite_loop() : num =  2117
infinite_loop() : num =  2118
infinite_loop() : num =  2119
infinite_loop() : num =  2120
infinite_loop() : num =  2121
infinite_loop() : num =  2122
infinite_loop() : num =  2123
infinite_loop() : num =  2124
infinite_loop() : num =  2125
infinite_loop() : num =  2126
infinite_loop() : num =  2127
infinite_loop() : num =  2128
infinite_loop() : num =  2129
infinite_loop() : num =  2130
infinite_loop() : num =  2131
infinite_loop() : num =  2132
infinite_loop() : num =  2133
infinite_loop() : num =  2134
infinite_loop() : num =  2135
infinite_loop() : num =  2136
infinite_loop() : num =  2137
infinite_loop() : num =  2138
infinite_loop() : num =  2139
infinite_loop() : num =  2140
infinite_loop() : num =  2141
infinite_loop() : num =  2142
infinite_loop() : num =  2143
infinite_loop() : num =  2144
infinite_loop() : num =  2145
infinite_loop() : num =  2146
infinite_loop() : num =  2147
infinite_loop() : num =  2148
infinite_loop() : num =  2149
infinite_loop() : num =  2150
infinite_loop() : num =  2151
infinite_loop() : num =  2152
infinite_loop() : num =  2153
infinite_loop() : num =  2154
infinite_loop() : num =  2155
infinite_loop() : num =  2156
infinite_loop() : num =  2157
infinite_loop() : num =  2158
infinite_loop() : num =  2159
infinite_loop() : num =  2160
infinite_loop() : num =  2161
infinite_loop() : num =  2162
infinite_loop() : num =  2163
infinite_loop() : num =  2164
infinite_loop() : num =  2165
infinite_loop() : num =  2166
infinite_loop() : num =  2167
infinite_loop() : num =  2168
infinite_loop() : num =  2169
infinite_loop() : num =  2170
infinite_loop() : num =  2171
infinite_loop() : num =  2172
infinite_loop() : num =  2173
infinite_loop() : num =  2174
infinite_loop() : num =  2175
infinite_loop() : num =  2176
infinite_loop() : num =  2177
infinite_loop() : num =  2178
infinite_loop() : num =  2179
infinite_loop() : num =  2180
infinite_loop() : num =  2181
infinite_loop() : num =  2182
infinite_loop() : num =  2183
infinite_loop() : num =  2184
infinite_loop() : num =  2185
infinite_loop() : num =  2186
infinite_loop() : num =  2187
infinite_loop() : num =  2188
infinite_loop() : num =  2189
infinite_loop() : num =  2190
infinite_loop() : num =  2191
infinite_loop() : num =  2192
infinite_loop() : num =  2193
infinite_loop() : num =  2194
infinite_loop() : num =  2195
infinite_loop() : num =  2196
infinite_loop() : num =  2197
infinite_loop() : num =  2198
infinite_loop() : num =  2199
infinite_loop() : num =  2200
infinite_loop() : num =  2201
infinite_loop() : num =  2202
infinite_loop() : num =  2203
infinite_loop() : num =  2204
infinite_loop() : num =  2205
infinite_loop() : num =  2206
infinite_loop() : num =  2207
infinite_loop() : num =  2208
infinite_loop() : num =  2209
infinite_loop() : num =  2210
infinite_loop() : num =  2211
infinite_loop() : num =  2212
infinite_loop() : num =  2213
infinite_loop() : num =  2214
infinite_loop() : num =  2215
infinite_loop() : num =  2216
infinite_loop() : num =  2217
infinite_loop() : num =  2218
infinite_loop() : num =  2219
infinite_loop() : num =  2220
infinite_loop() : num =  2221
infinite_loop() : num =  2222
infinite_loop() : num =  2223
infinite_loop() : num =  2224
infinite_loop() : num =  2225
infinite_loop() : num =  2226
infinite_loop() : num =  2227
infinite_loop() : num =  2228
infinite_loop() : num =  2229
infinite_loop() : num =  2230
infinite_loop() : num =  2231
infinite_loop() : num =  2232
infinite_loop() : num =  2233
infinite_loop() : num =  2234
infinite_loop() : num =  2235
infinite_loop() : num =  2236
infinite_loop() : num =  2237
infinite_loop() : num =  2238
infinite_loop() : num =  2239
infinite_loop() : num =  2240
infinite_loop() : num =  2241
infinite_loop() : num =  2242
infinite_loop() : num =  2243
infinite_loop() : num =  2244
infinite_loop() : num =  2245
infinite_loop() : num =  2246
infinite_loop() : num =  2247
infinite_loop() : num =  2248
infinite_loop() : num =  2249
infinite_loop() : num =  2250
infinite_loop() : num =  2251
infinite_loop() : num =  2252
infinite_loop() : num =  2253
infinite_loop() : num =  2254
infinite_loop() : num =  2255
infinite_loop() : num =  2256
infinite_loop() : num =  2257
infinite_loop() : num =  2258
infinite_loop() : num =  2259
infinite_loop() : num =  2260
infinite_loop() : num =  2261
infinite_loop() : num =  2262
infinite_loop() : num =  2263
infinite_loop() : num =  2264
infinite_loop() : num =  2265
infinite_loop() : num =  2266
infinite_loop() : num =  2267
infinite_loop() : num =  2268
infinite_loop() : num =  2269
infinite_loop() : num =  2270
infinite_loop() : num =  2271
infinite_loop() : num =  2272
infinite_loop() : num =  2273
infinite_loop() : num =  2274
infinite_loop() : num =  2275
infinite_loop() : num =  2276
infinite_loop() : num =  2277
infinite_loop() : num =  2278
infinite_loop() : num =  2279
infinite_loop() : num =  2280
infinite_loop() : num =  2281
infinite_loop() : num =  2282
infinite_loop() : num =  2283
infinite_loop() : num =  2284
infinite_loop() : num =  2285
infinite_loop() : num =  2286
infinite_loop() : num =  2287
infinite_loop() : num =  2288
infinite_loop() : num =  2289
infinite_loop() : num =  2290
infinite_loop() : num =  2291
infinite_loop() : num =  2292
infinite_loop() : num =  2293
infinite_loop() : num =  2294
infinite_loop() : num =  2295
infinite_loop() : num =  2296
infinite_loop() : num =  2297
infinite_loop() : num =  2298
infinite_loop() : num =  2299
infinite_loop() : num =  2300
infinite_loop() : num =  2301
infinite_loop() : num =  2302
infinite_loop() : num =  2303
infinite_loop() : num =  2304
infinite_loop() : num =  2305
infinite_loop() : num =  2306
infinite_loop() : num =  2307
infinite_loop() : num =  2308
infinite_loop() : num =  2309
infinite_loop() : num =  2310
infinite_loop() : num =  2311
infinite_loop() : num =  2312
infinite_loop() : num =  2313
infinite_loop() : num =  2314
infinite_loop() : num =  2315
infinite_loop() : num =  2316
infinite_loop() : num =  2317
infinite_loop() : num =  2318
infinite_loop() : num =  2319
infinite_loop() : num =  2320
infinite_loop() : num =  2321
infinite_loop() : num =  2322
infinite_loop() : num =  2323
infinite_loop() : num =  2324
infinite_loop() : num =  2325
infinite_loop() : num =  2326
infinite_loop() : num =  2327
infinite_loop() : num =  2328
infinite_loop() : num =  2329
infinite_loop() : num =  2330
infinite_loop() : num =  2331
infinite_loop() : num =  2332
infinite_loop() : num =  2333
infinite_loop() : num =  2334
infinite_loop() : num =  2335
infinite_loop() : num =  2336
infinite_loop() : num =  2337
infinite_loop() : num =  2338
infinite_loop() : num =  2339
infinite_loop() : num =  2340
infinite_loop() : num =  2341
infinite_loop() : num =  2342
infinite_loop() : num =  2343
infinite_loop() : num =  2344
infinite_loop() : num =  2345
infinite_loop() : num =  2346
infinite_loop() : num =  2347
infinite_loop() : num =  2348
infinite_loop() : num =  2349
infinite_loop() : num =  2350
infinite_loop() : num =  2351
infinite_loop() : num =  2352
infinite_loop() : num =  2353
infinite_loop() : num =  2354
infinite_loop() : num =  2355
infinite_loop() : num =  2356
infinite_loop() : num =  2357
infinite_loop() : num =  2358
infinite_loop() : num =  2359
infinite_loop() : num =  2360
infinite_loop() : num =  2361
infinite_loop() : num =  2362
infinite_loop() : num =  2363
infinite_loop() : num =  2364
infinite_loop() : num =  2365
infinite_loop() : num =  2366
infinite_loop() : num =  2367
infinite_loop() : num =  2368
infinite_loop() : num =  2369
infinite_loop() : num =  2370
infinite_loop() : num =  2371
infinite_loop() : num =  2372
infinite_loop() : num =  2373
infinite_loop() : num =  2374
infinite_loop() : num =  2375
infinite_loop() : num =  2376
infinite_loop() : num =  2377
infinite_loop() : num =  2378
infinite_loop() : num =  2379
infinite_loop() : num =  2380
infinite_loop() : num =  2381
infinite_loop() : num =  2382
infinite_loop() : num =  2383
infinite_loop() : num =  2384
infinite_loop() : num =  2385
infinite_loop() : num =  2386
infinite_loop() : num =  2387
infinite_loop() : num =  2388
infinite_loop() : num =  2389
infinite_loop() : num =  2390
infinite_loop() : num =  2391
infinite_loop() : num =  2392
infinite_loop() : num =  2393
infinite_loop() : num =  2394
infinite_loop() : num =  2395
infinite_loop() : num =  2396
infinite_loop() : num =  2397
infinite_loop() : num =  2398
infinite_loop() : num =  2399
infinite_loop() : num =  2400
infinite_loop() : num =  2401
infinite_loop() : num =  2402
infinite_loop() : num =  2403
infinite_loop() : num =  2404
infinite_loop() : num =  2405
infinite_loop() : num =  2406
infinite_loop() : num =  2407
infinite_loop() : num =  2408
infinite_loop() : num =  2409
infinite_loop() : num =  2410
infinite_loop() : num =  2411
infinite_loop() : num =  2412
infinite_loop() : num =  2413
infinite_loop() : num =  2414
infinite_loop() : num =  2415
infinite_loop() : num =  2416
infinite_loop() : num =  2417
infinite_loop() : num =  2418
infinite_loop() : num =  2419
infinite_loop() : num =  2420
infinite_loop() : num =  2421
infinite_loop() : num =  2422
infinite_loop() : num =  2423
infinite_loop() : num =  2424
infinite_loop() : num =  2425
infinite_loop() : num =  2426
infinite_loop() : num =  2427
infinite_loop() : num =  2428
infinite_loop() : num =  2429
infinite_loop() : num =  2430
infinite_loop() : num =  2431
infinite_loop() : num =  2432
infinite_loop() : num =  2433
infinite_loop() : num =  2434
infinite_loop() : num =  2435
infinite_loop() : num =  2436
infinite_loop() : num =  2437
infinite_loop() : num =  2438
infinite_loop() : num =  2439
infinite_loop() : num =  2440
infinite_loop() : num =  2441
infinite_loop() : num =  2442
infinite_loop() : num =  2443
infinite_loop() : num =  2444
infinite_loop() : num =  2445
infinite_loop() : num =  2446
infinite_loop() : num =  2447
infinite_loop() : num =  2448
infinite_loop() : num =  2449
infinite_loop() : num =  2450
infinite_loop() : num =  2451
infinite_loop() : num =  2452
infinite_loop() : num =  2453
infinite_loop() : num =  2454
infinite_loop() : num =  2455
infinite_loop() : num =  2456
infinite_loop() : num =  2457
infinite_loop() : num =  2458
infinite_loop() : num =  2459
infinite_loop() : num =  2460
infinite_loop() : num =  2461
infinite_loop() : num =  2462
infinite_loop() : num =  2463
infinite_loop() : num =  2464
infinite_loop() : num =  2465
infinite_loop() : num =  2466
infinite_loop() : num =  2467
infinite_loop() : num =  2468
infinite_loop() : num =  2469
infinite_loop() : num =  2470
infinite_loop() : num =  2471
infinite_loop() : num =  2472
infinite_loop() : num =  2473
infinite_loop() : num =  2474
infinite_loop() : num =  2475
infinite_loop() : num =  2476
infinite_loop() : num =  2477
infinite_loop() : num =  2478
infinite_loop() : num =  2479
infinite_loop() : num =  2480
infinite_loop() : num =  2481
infinite_loop() : num =  2482
infinite_loop() : num =  2483
infinite_loop() : num =  2484
infinite_loop() : num =  2485
infinite_loop() : num =  2486
infinite_loop() : num =  2487
infinite_loop() : num =  2488
infinite_loop() : num =  2489
infinite_loop() : num =  2490
infinite_loop() : num =  2491
infinite_loop() : num =  2492
infinite_loop() : num =  2493
infinite_loop() : num =  2494
infinite_loop() : num =  2495
infinite_loop() : num =  2496
infinite_loop() : num =  2497
infinite_loop() : num =  2498
infinite_loop() : num =  2499
infinite_loop() : num =  2500
infinite_loop() : num =  2501
infinite_loop() : num =  2502
infinite_loop() : num =  2503
infinite_loop() : num =  2504
infinite_loop() : num =  2505
infinite_loop() : num =  2506
infinite_loop() : num =  2507
infinite_loop() : num =  2508
infinite_loop() : num =  2509
infinite_loop() : num =  2510
infinite_loop() : num =  2511
infinite_loop() : num =  2512
infinite_loop() : num =  2513
infinite_loop() : num =  2514
infinite_loop() : num =  2515
infinite_loop() : num =  2516
infinite_loop() : num =  2517
infinite_loop() : num =  2518
infinite_loop() : num =  2519
infinite_loop() : num =  2520
infinite_loop() : num =  2521
infinite_loop() : num =  2522
infinite_loop() : num =  2523
infinite_loop() : num =  2524
infinite_loop() : num =  2525
infinite_loop() : num =  2526
infinite_loop() : num =  2527
infinite_loop() : num =  2528
infinite_loop() : num =  2529
infinite_loop() : num =  2530
infinite_loop() : num =  2531
infinite_loop() : num =  2532
infinite_loop() : num =  2533
infinite_loop() : num =  2534
infinite_loop() : num =  2535
infinite_loop() : num =  2536
infinite_loop() : num =  2537
infinite_loop() : num =  2538
infinite_loop() : num =  2539
infinite_loop() : num =  2540
infinite_loop() : num =  2541
infinite_loop() : num =  2542
infinite_loop() : num =  2543
infinite_loop() : num =  2544
infinite_loop() : num =  2545
infinite_loop() : num =  2546
infinite_loop() : num =  2547
infinite_loop() : num =  2548
infinite_loop() : num =  2549
infinite_loop() : num =  2550
infinite_loop() : num =  2551
infinite_loop() : num =  2552
infinite_loop() : num =  2553
infinite_loop() : num =  2554
infinite_loop() : num =  2555
infinite_loop() : num =  2556
infinite_loop() : num =  2557
infinite_loop() : num =  2558
infinite_loop() : num =  2559
infinite_loop() : num =  2560
infinite_loop() : num =  2561
infinite_loop() : num =  2562
infinite_loop() : num =  2563
infinite_loop() : num =  2564
infinite_loop() : num =  2565
infinite_loop() : num =  2566
infinite_loop() : num =  2567
infinite_loop() : num =  2568
infinite_loop() : num =  2569
infinite_loop() : num =  2570
infinite_loop() : num =  2571
infinite_loop() : num =  2572
infinite_loop() : num =  2573
infinite_loop() : num =  2574
infinite_loop() : num =  2575
infinite_loop() : num =  2576
infinite_loop() : num =  2577
infinite_loop() : num =  2578
infinite_loop() : num =  2579
infinite_loop() : num =  2580
infinite_loop() : num =  2581
infinite_loop() : num =  2582
infinite_loop() : num =  2583
infinite_loop() : num =  2584
infinite_loop() : num =  2585
infinite_loop() : num =  2586
infinite_loop() : num =  2587
infinite_loop() : num =  2588
infinite_loop() : num =  2589
infinite_loop() : num =  2590
infinite_loop() : num =  2591
infinite_loop() : num =  2592
infinite_loop() : num =  2593
infinite_loop() : num =  2594
infinite_loop() : num =  2595
infinite_loop() : num =  2596
infinite_loop() : num =  2597
infinite_loop() : num =  2598
infinite_loop() : num =  2599
infinite_loop() : num =  2600
infinite_loop() : num =  2601
infinite_loop() : num =  2602
infinite_loop() : num =  2603
infinite_loop() : num =  2604
infinite_loop() : num =  2605
infinite_loop() : num =  2606
infinite_loop() : num =  2607
infinite_loop() : num =  2608
infinite_loop() : num =  2609
infinite_loop() : num =  2610
infinite_loop() : num =  2611
infinite_loop() : num =  2612
infinite_loop() : num =  2613
infinite_loop() : num =  2614
infinite_loop() : num =  2615
infinite_loop() : num =  2616
infinite_loop() : num =  2617
infinite_loop() : num =  2618
infinite_loop() : num =  2619
infinite_loop() : num =  2620
infinite_loop() : num =  2621
infinite_loop() : num =  2622
infinite_loop() : num =  2623
infinite_loop() : num =  2624
infinite_loop() : num =  2625
infinite_loop() : num =  2626
infinite_loop() : num =  2627
infinite_loop() : num =  2628
infinite_loop() : num =  2629
infinite_loop() : num =  2630
infinite_loop() : num =  2631
infinite_loop() : num =  2632
infinite_loop() : num =  2633
infinite_loop() : num =  2634
infinite_loop() : num =  2635
infinite_loop() : num =  2636
infinite_loop() : num =  2637
infinite_loop() : num =  2638
infinite_loop() : num =  2639
infinite_loop() : num =  2640
infinite_loop() : num =  2641
infinite_loop() : num =  2642
infinite_loop() : num =  2643
infinite_loop() : num =  2644
infinite_loop() : num =  2645
infinite_loop() : num =  2646
infinite_loop() : num =  2647
infinite_loop() : num =  2648
infinite_loop() : num =  2649
infinite_loop() : num =  2650
infinite_loop() : num =  2651
infinite_loop() : num =  2652
infinite_loop() : num =  2653
infinite_loop() : num =  2654
infinite_loop() : num =  2655
infinite_loop() : num =  2656
infinite_loop() : num =  2657
infinite_loop() : num =  2658
infinite_loop() : num =  2659
infinite_loop() : num =  2660
infinite_loop() : num =  2661
infinite_loop() : num =  2662
infinite_loop() : num =  2663
infinite_loop() : num =  2664
infinite_loop() : num =  2665
infinite_loop() : num =  2666
infinite_loop() : num =  2667
infinite_loop() : num =  2668
infinite_loop() : num =  2669
infinite_loop() : num =  2670
infinite_loop() : num =  2671
infinite_loop() : num =  2672
infinite_loop() : num =  2673
infinite_loop() : num =  2674
infinite_loop() : num =  2675
infinite_loop() : num =  2676
infinite_loop() : num =  2677
infinite_loop() : num =  2678
infinite_loop() : num =  2679
infinite_loop() : num =  2680
infinite_loop() : num =  2681
infinite_loop() : num =  2682
infinite_loop() : num =  2683
infinite_loop() : num =  2684
infinite_loop() : num =  2685
infinite_loop() : num =  2686
infinite_loop() : num =  2687
infinite_loop() : num =  2688
infinite_loop() : num =  2689
infinite_loop() : num =  2690
infinite_loop() : num =  2691
infinite_loop() : num =  2692
infinite_loop() : num =  2693
infinite_loop() : num =  2694
infinite_loop() : num =  2695
infinite_loop() : num =  2696
infinite_loop() : num =  2697
infinite_loop() : num =  2698
infinite_loop() : num =  2699
infinite_loop() : num =  2700
infinite_loop() : num =  2701
infinite_loop() : num =  2702
infinite_loop() : num =  2703
infinite_loop() : num =  2704
infinite_loop() : num =  2705
infinite_loop() : num =  2706
infinite_loop() : num =  2707
infinite_loop() : num =  2708
infinite_loop() : num =  2709
infinite_loop() : num =  2710
infinite_loop() : num =  2711
infinite_loop() : num =  2712
infinite_loop() : num =  2713
infinite_loop() : num =  2714
infinite_loop() : num =  2715
infinite_loop() : num =  2716
infinite_loop() : num =  2717
infinite_loop() : num =  2718
infinite_loop() : num =  2719
infinite_loop() : num =  2720
infinite_loop() : num =  2721
infinite_loop() : num =  2722
infinite_loop() : num =  2723
infinite_loop() : num =  2724
infinite_loop() : num =  2725
infinite_loop() : num =  2726
infinite_loop() : num =  2727
infinite_loop() : num =  2728
infinite_loop() : num =  2729
infinite_loop() : num =  2730
infinite_loop() : num =  2731
infinite_loop() : num =  2732
infinite_loop() : num =  2733
infinite_loop() : num =  2734
infinite_loop() : num =  2735
infinite_loop() : num =  2736
infinite_loop() : num =  2737
infinite_loop() : num =  2738
infinite_loop() : num =  2739
infinite_loop() : num =  2740
infinite_loop() : num =  2741
infinite_loop() : num =  2742
infinite_loop() : num =  2743
infinite_loop() : num =  2744
infinite_loop() : num =  2745
infinite_loop() : num =  2746
infinite_loop() : num =  2747
infinite_loop() : num =  2748
infinite_loop() : num =  2749
infinite_loop() : num =  2750
infinite_loop() : num =  2751
infinite_loop() : num =  2752
infinite_loop() : num =  2753
infinite_loop() : num =  2754
infinite_loop() : num =  2755
infinite_loop() : num =  2756
infinite_loop() : num =  2757
infinite_loop() : num =  2758
infinite_loop() : num =  2759
infinite_loop() : num =  2760
infinite_loop() : num =  2761
infinite_loop() : num =  2762
infinite_loop() : num =  2763
infinite_loop() : num =  2764
infinite_loop() : num =  2765
infinite_loop() : num =  2766
infinite_loop() : num =  2767
infinite_loop() : num =  2768
infinite_loop() : num =  2769
infinite_loop() : num =  2770
infinite_loop() : num =  2771
infinite_loop() : num =  2772
infinite_loop() : num =  2773
infinite_loop() : num =  2774
infinite_loop() : num =  2775
infinite_loop() : num =  2776
infinite_loop() : num =  2777
infinite_loop() : num =  2778
infinite_loop() : num =  2779
infinite_loop() : num =  2780
infinite_loop() : num =  2781
infinite_loop() : num =  2782
infinite_loop() : num =  2783
infinite_loop() : num =  2784
infinite_loop() : num =  2785
infinite_loop() : num =  2786
infinite_loop() : num =  2787
infinite_loop() : num =  2788
infinite_loop() : num =  2789
infinite_loop() : num =  2790
infinite_loop() : num =  2791
infinite_loop() : num =  2792
infinite_loop() : num =  2793
infinite_loop() : num =  2794
infinite_loop() : num =  2795
infinite_loop() : num =  2796
infinite_loop() : num =  2797
infinite_loop() : num =  2798
infinite_loop() : num =  2799
infinite_loop() : num =  2800
infinite_loop() : num =  2801
infinite_loop() : num =  2802
infinite_loop() : num =  2803
infinite_loop() : num =  2804
infinite_loop() : num =  2805
infinite_loop() : num =  2806
infinite_loop() : num =  2807
infinite_loop() : num =  2808
infinite_loop() : num =  2809
infinite_loop() : num =  2810
infinite_loop() : num =  2811
infinite_loop() : num =  2812
infinite_loop() : num =  2813
infinite_loop() : num =  2814
infinite_loop() : num =  2815
infinite_loop() : num =  2816
infinite_loop() : num =  2817
infinite_loop() : num =  2818
infinite_loop() : num =  2819
infinite_loop() : num =  2820
infinite_loop() : num =  2821
infinite_loop() : num =  2822
infinite_loop() : num =  2823
infinite_loop() : num =  2824
infinite_loop() : num =  2825
infinite_loop() : num =  2826
infinite_loop() : num =  2827
infinite_loop() : num =  2828
infinite_loop() : num =  2829
infinite_loop() : num =  2830
infinite_loop() : num =  2831
infinite_loop() : num =  2832
infinite_loop() : num =  2833
infinite_loop() : num =  2834
infinite_loop() : num =  2835
infinite_loop() : num =  2836
infinite_loop() : num =  2837
infinite_loop() : num =  2838
infinite_loop() : num =  2839
infinite_loop() : num =  2840
infinite_loop() : num =  2841
infinite_loop() : num =  2842
infinite_loop() : num =  2843
infinite_loop() : num =  2844
infinite_loop() : num =  2845
infinite_loop() : num =  2846
infinite_loop() : num =  2847
infinite_loop() : num =  2848
infinite_loop() : num =  2849
infinite_loop() : num =  2850
infinite_loop() : num =  2851
infinite_loop() : num =  2852
infinite_loop() : num =  2853
infinite_loop() : num =  2854
infinite_loop() : num =  2855
infinite_loop() : num =  2856
infinite_loop() : num =  2857
infinite_loop() : num =  2858
infinite_loop() : num =  2859
infinite_loop() : num =  2860
infinite_loop() : num =  2861
infinite_loop() : num =  2862
infinite_loop() : num =  2863
infinite_loop() : num =  2864
infinite_loop() : num =  2865
infinite_loop() : num =  2866
infinite_loop() : num =  2867
infinite_loop() : num =  2868
infinite_loop() : num =  2869
infinite_loop() : num =  2870
infinite_loop() : num =  2871
infinite_loop() : num =  2872
infinite_loop() : num =  2873
infinite_loop() : num =  2874
infinite_loop() : num =  2875
infinite_loop() : num =  2876
infinite_loop() : num =  2877
infinite_loop() : num =  2878
infinite_loop() : num =  2879
infinite_loop() : num =  2880
infinite_loop() : num =  2881
infinite_loop() : num =  2882
infinite_loop() : num =  2883
infinite_loop() : num =  2884
infinite_loop() : num =  2885
infinite_loop() : num =  2886
infinite_loop() : num =  2887
infinite_loop() : num =  2888
infinite_loop() : num =  2889
infinite_loop() : num =  2890
infinite_loop() : num =  2891
infinite_loop() : num =  2892
infinite_loop() : num =  2893
infinite_loop() : num =  2894
infinite_loop() : num =  2895
infinite_loop() : num =  2896
infinite_loop() : num =  2897
infinite_loop() : num =  2898
infinite_loop() : num =  2899
infinite_loop() : num =  2900
infinite_loop() : num =  2901
infinite_loop() : num =  2902
infinite_loop() : num =  2903
infinite_loop() : num =  2904
infinite_loop() : num =  2905
infinite_loop() : num =  2906
infinite_loop() : num =  2907
infinite_loop() : num =  2908
infinite_loop() : num =  2909
infinite_loop() : num =  2910
infinite_loop() : num =  2911
infinite_loop() : num =  2912
infinite_loop() : num =  2913
infinite_loop() : num =  2914
infinite_loop() : num =  2915
infinite_loop() : num =  2916
infinite_loop() : num =  2917
infinite_loop() : num =  2918
infinite_loop() : num =  2919
infinite_loop() : num =  2920
infinite_loop() : num =  2921
infinite_loop() : num =  2922
infinite_loop() : num =  2923
infinite_loop() : num =  2924
infinite_loop() : num =  2925
infinite_loop() : num =  2926
infinite_loop() : num =  2927
infinite_loop() : num =  2928
infinite_loop() : num =  2929
infinite_loop() : num =  2930
infinite_loop() : num =  2931
infinite_loop() : num =  2932
infinite_loop() : num =  2933
infinite_loop() : num =  2934
infinite_loop() : num =  2935
infinite_loop() : num =  2936
infinite_loop() : num =  2937
infinite_loop() : num =  2938
infinite_loop() : num =  2939
infinite_loop() : num =  2940
infinite_loop() : num =  2941
infinite_loop() : num =  2942
infinite_loop() : num =  2943
infinite_loop() : num =  2944
infinite_loop() : num =  2945
infinite_loop() : num =  2946
infinite_loop() : num =  2947
infinite_loop() : num =  2948
infinite_loop() : num =  2949
infinite_loop() : num =  2950
infinite_loop() : num =  2951
infinite_loop() : num =  2952
infinite_loop() : num =  2953
infinite_loop() : num =  2954
infinite_loop() : num =  2955
infinite_loop() : num =  2956
infinite_loop() : num =  2957
infinite_loop() : num =  2958
infinite_loop() : num =  2959
infinite_loop() : num =  2960
infinite_loop() : num =  2961
infinite_loop() : num =  2962
infinite_loop() : num =  2963
infinite_loop() : num =  2964
infinite_loop() : num =  2965
infinite_loop() : num =  2966
infinite_loop() : num =  2967
infinite_loop() : num =  2968
infinite_loop() : num =  2969
infinite_loop() : num =  2970
infinite_loop() : num =  2971
infinite_loop() : num =  2972
infinite_loop() : num =  2973
infinite_loop() : num =  2974
infinite_loop() : num =  2975
infinite_loop() : num =  2976
infinite_loop() : num =  2977
infinite_loop() : num =  2978
infinite_loop() : num =  2979
infinite_loop() : num =  2980
infinite_loop() : num =  2981
infinite_loop() : num =  2982
infinite_loop() : num =  2983
infinite_loop() : num =  2984
infinite_loop() : num =  2985
infinite_loop() : num =  2986
infinite_loop() : num =  2987
infinite_loop() : num =  2988
infinite_loop() : num =  2989
infinite_loop() : num =  2990
infinite_loop() : num =  2991
infinite_loop() : num =  2992
infinite_loop() : num =  2993
infinite_loop() : num =  2994
infinite_loop() : num =  2995
infinite_loop() : num =  2996
infinite_loop() : num =  2997
infinite_loop() : num =  2998
infinite_loop() : num =  2999
infinite_loop() : num =  3000
infinite_loop() : num =  3001
infinite_loop() : num =  3002
infinite_loop() : num =  3003
infinite_loop() : num =  3004
infinite_loop() : num =  3005
infinite_loop() : num =  3006
infinite_loop() : num =  3007
infinite_loop() : num =  3008
infinite_loop() : num =  3009
infinite_loop() : num =  3010
infinite_loop() : num =  3011
infinite_loop() : num =  3012
infinite_loop() : num =  3013
infinite_loop() : num =  3014
infinite_loop() : num =  3015
infinite_loop() : num =  3016
infinite_loop() : num =  3017
infinite_loop() : num =  3018
infinite_loop() : num =  3019
infinite_loop() : num =  3020
infinite_loop() : num =  3021
infinite_loop() : num =  3022
infinite_loop() : num =  3023
infinite_loop() : num =  3024
infinite_loop() : num =  3025
infinite_loop() : num =  3026
infinite_loop() : num =  3027
infinite_loop() : num =  3028
infinite_loop() : num =  3029
infinite_loop() : num =  3030
infinite_loop() : num =  3031
infinite_loop() : num =  3032
infinite_loop() : num =  3033
infinite_loop() : num =  3034
infinite_loop() : num =  3035
infinite_loop() : num =  3036
infinite_loop() : num =  3037
infinite_loop() : num =  3038
infinite_loop() : num =  3039
infinite_loop() : num =  3040
infinite_loop() : num =  3041
infinite_loop() : num =  3042
infinite_loop() : num =  3043
infinite_loop() : num =  3044
infinite_loop() : num =  3045
infinite_loop() : num =  3046
infinite_loop() : num =  3047
infinite_loop() : num =  3048
infinite_loop() : num =  3049
infinite_loop() : num =  3050
infinite_loop() : num =  3051
infinite_loop() : num =  3052
infinite_loop() : num =  3053
infinite_loop() : num =  3054
infinite_loop() : num =  3055
infinite_loop() : num =  3056
infinite_loop() : num =  3057
infinite_loop() : num =  3058
infinite_loop() : num =  3059
infinite_loop() : num =  3060
infinite_loop() : num =  3061
infinite_loop() : num =  3062
infinite_loop() : num =  3063
infinite_loop() : num =  3064
infinite_loop() : num =  3065
infinite_loop() : num =  3066
infinite_loop() : num =  3067
infinite_loop() : num =  3068
infinite_loop() : num =  3069
infinite_loop() : num =  3070
infinite_loop() : num =  3071
infinite_loop() : num =  3072
infinite_loop() : num =  3073
infinite_loop() : num =  3074
infinite_loop() : num =  3075
infinite_loop() : num =  3076
infinite_loop() : num =  3077
infinite_loop() : num =  3078
infinite_loop() : num =  3079
infinite_loop() : num =  3080
infinite_loop() : num =  3081
infinite_loop() : num =  3082
infinite_loop() : num =  3083
infinite_loop() : num =  3084
infinite_loop() : num =  3085
infinite_loop() : num =  3086
infinite_loop() : num =  3087
infinite_loop() : num =  3088
infinite_loop() : num =  3089
infinite_loop() : num =  3090
infinite_loop() : num =  3091
infinite_loop() : num =  3092
infinite_loop() : num =  3093
infinite_loop() : num =  3094
infinite_loop() : num =  3095
infinite_loop() : num =  3096
infinite_loop() : num =  3097
infinite_loop() : num =  3098
infinite_loop() : num =  3099
infinite_loop() : num =  3100
infinite_loop() : num =  3101
infinite_loop() : num =  3102
infinite_loop() : num =  3103
infinite_loop() : num =  3104
infinite_loop() : num =  3105
infinite_loop() : num =  3106
infinite_loop() : num =  3107
infinite_loop() : num =  3108
infinite_loop() : num =  3109
infinite_loop() : num =  3110
infinite_loop() : num =  3111
infinite_loop() : num =  3112
infinite_loop() : num =  3113
infinite_loop() : num =  3114
infinite_loop() : num =  3115
infinite_loop() : num =  3116
infinite_loop() : num =  3117
infinite_loop() : num =  3118
infinite_loop() : num =  3119
infinite_loop() : num =  3120
infinite_loop() : num =  3121
infinite_loop() : num =  3122
infinite_loop() : num =  3123
infinite_loop() : num =  3124
infinite_loop() : num =  3125
infinite_loop() : num =  3126
infinite_loop() : num =  3127
infinite_loop() : num =  3128
infinite_loop() : num =  3129
infinite_loop() : num =  3130
infinite_loop() : num =  3131
infinite_loop() : num =  3132
infinite_loop() : num =  3133
infinite_loop() : num =  3134
infinite_loop() : num =  3135
infinite_loop() : num =  3136
infinite_loop() : num =  3137
infinite_loop() : num =  3138
infinite_loop() : num =  3139
infinite_loop() : num =  3140
infinite_loop() : num =  3141
infinite_loop() : num =  3142
infinite_loop() : num =  3143
infinite_loop() : num =  3144
infinite_loop() : num =  3145
infinite_loop() : num =  3146
infinite_loop() : num =  3147
infinite_loop() : num =  3148
infinite_loop() : num =  3149
infinite_loop() : num =  3150
infinite_loop() : num =  3151
infinite_loop() : num =  3152
infinite_loop() : num =  3153
infinite_loop() : num =  3154
infinite_loop() : num =  3155
infinite_loop() : num =  3156
infinite_loop() : num =  3157
infinite_loop() : num =  3158
infinite_loop() : num =  3159
infinite_loop() : num =  3160
infinite_loop() : num =  3161
infinite_loop() : num =  3162
infinite_loop() : num =  3163
infinite_loop() : num =  3164
infinite_loop() : num =  3165
infinite_loop() : num =  3166
infinite_loop() : num =  3167
infinite_loop() : num =  3168
infinite_loop() : num =  3169
infinite_loop() : num =  3170
infinite_loop() : num =  3171
infinite_loop() : num =  3172
infinite_loop() : num =  3173
infinite_loop() : num =  3174
infinite_loop() : num =  3175
infinite_loop() : num =  3176
infinite_loop() : num =  3177
infinite_loop() : num =  3178
infinite_loop() : num =  3179
infinite_loop() : num =  3180
infinite_loop() : num =  3181
infinite_loop() : num =  3182
infinite_loop() : num =  3183
infinite_loop() : num =  3184
infinite_loop() : num =  3185
infinite_loop() : num =  3186
infinite_loop() : num =  3187
infinite_loop() : num =  3188
infinite_loop() : num =  3189
infinite_loop() : num =  3190
infinite_loop() : num =  3191
infinite_loop() : num =  3192
infinite_loop() : num =  3193
infinite_loop() : num =  3194
infinite_loop() : num =  3195
infinite_loop() : num =  3196
infinite_loop() : num =  3197
infinite_loop() : num =  3198
infinite_loop() : num =  3199
infinite_loop() : num =  3200
infinite_loop() : num =  3201
infinite_loop() : num =  3202
infinite_loop() : num =  3203
infinite_loop() : num =  3204
infinite_loop() : num =  3205
infinite_loop() : num =  3206
infinite_loop() : num =  3207
infinite_loop() : num =  3208
infinite_loop() : num =  3209
infinite_loop() : num =  3210
infinite_loop() : num =  3211
infinite_loop() : num =  3212
infinite_loop() : num =  3213
infinite_loop() : num =  3214
infinite_loop() : num =  3215
infinite_loop() : num =  3216
infinite_loop() : num =  3217
infinite_loop() : num =  3218
infinite_loop() : num =  3219
infinite_loop() : num =  3220
infinite_loop() : num =  3221
infinite_loop() : num =  3222
infinite_loop() : num =  3223
infinite_loop() : num =  3224
infinite_loop() : num =  3225
infinite_loop() : num =  3226
infinite_loop() : num =  3227
infinite_loop() : num =  3228
infinite_loop() : num =  3229
infinite_loop() : num =  3230
infinite_loop() : num =  3231
infinite_loop() : num =  3232
infinite_loop() : num =  3233
infinite_loop() : num =  3234
infinite_loop() : num =  3235
infinite_loop() : num =  3236
infinite_loop() : num =  3237
infinite_loop() : num =  3238
infinite_loop() : num =  3239
infinite_loop() : num =  3240
infinite_loop() : num =  3241
infinite_loop() : num =  3242
infinite_loop() : num =  3243
infinite_loop() : num =  3244
infinite_loop() : num =  3245
infinite_loop() : num =  3246
infinite_loop() : num =  3247
infinite_loop() : num =  3248
infinite_loop() : num =  3249
infinite_loop() : num =  3250
infinite_loop() : num =  3251
infinite_loop() : num =  3252
infinite_loop() : num =  3253
infinite_loop() : num =  3254
infinite_loop() : num =  3255
infinite_loop() : num =  3256
infinite_loop() : num =  3257
infinite_loop() : num =  3258
infinite_loop() : num =  3259
infinite_loop() : num =  3260
infinite_loop() : num =  3261
infinite_loop() : num =  3262
infinite_loop() : num =  3263
infinite_loop() : num =  3264
infinite_loop() : num =  3265
infinite_loop() : num =  3266
infinite_loop() : num =  3267
infinite_loop() : num =  3268
infinite_loop() : num =  3269
infinite_loop() : num =  3270
infinite_loop() : num =  3271
infinite_loop() : num =  3272
infinite_loop() : num =  3273
infinite_loop() : num =  3274
infinite_loop() : num =  3275
infinite_loop() : num =  3276
infinite_loop() : num =  3277
infinite_loop() : num =  3278
infinite_loop() : num =  3279
infinite_loop() : num =  3280
infinite_loop() : num =  3281
infinite_loop() : num =  3282
infinite_loop() : num =  3283
infinite_loop() : num =  3284
infinite_loop() : num =  3285
infinite_loop() : num =  3286
infinite_loop() : num =  3287
infinite_loop() : num =  3288
infinite_loop() : num =  3289
infinite_loop() : num =  3290
infinite_loop() : num =  3291
infinite_loop() : num =  3292
infinite_loop() : num =  3293
infinite_loop() : num =  3294
infinite_loop() : num =  3295
infinite_loop() : num =  3296
infinite_loop() : num =  3297
infinite_loop() : num =  3298
infinite_loop() : num =  3299
infinite_loop() : num =  3300
infinite_loop() : num =  3301
infinite_loop() : num =  3302
infinite_loop() : num =  3303
infinite_loop() : num =  3304
infinite_loop() : num =  3305
infinite_loop() : num =  3306
infinite_loop() : num =  3307
infinite_loop() : num =  3308
infinite_loop() : num =  3309
infinite_loop() : num =  3310
infinite_loop() : num =  3311
infinite_loop() : num =  3312
infinite_loop() : num =  3313
infinite_loop() : num =  3314
infinite_loop() : num =  3315
infinite_loop() : num =  3316
infinite_loop() : num =  3317
infinite_loop() : num =  3318
infinite_loop() : num =  3319
infinite_loop() : num =  3320
infinite_loop() : num =  3321
infinite_loop() : num =  3322
infinite_loop() : num =  3323
infinite_loop() : num =  3324
infinite_loop() : num =  3325
infinite_loop() : num =  3326
infinite_loop() : num =  3327
infinite_loop() : num =  3328
infinite_loop() : num =  3329
infinite_loop() : num =  3330
infinite_loop() : num =  3331
infinite_loop() : num =  3332
infinite_loop() : num =  3333
infinite_loop() : num =  3334
infinite_loop() : num =  3335
infinite_loop() : num =  3336
infinite_loop() : num =  3337
infinite_loop() : num =  3338
infinite_loop() : num =  3339
infinite_loop() : num =  3340
infinite_loop() : num =  3341
infinite_loop() : num =  3342
infinite_loop() : num =  3343
infinite_loop() : num =  3344
infinite_loop() : num =  3345
infinite_loop() : num =  3346
infinite_loop() : num =  3347
infinite_loop() : num =  3348
infinite_loop() : num =  3349
infinite_loop() : num =  3350
infinite_loop() : num =  3351
infinite_loop() : num =  3352
infinite_loop() : num =  3353
infinite_loop() : num =  3354
infinite_loop() : num =  3355
infinite_loop() : num =  3356
infinite_loop() : num =  3357
infinite_loop() : num =  3358
infinite_loop() : num =  3359
infinite_loop() : num =  3360
infinite_loop() : num =  3361
infinite_loop() : num =  3362
infinite_loop() : num =  3363
infinite_loop() : num =  3364
infinite_loop() : num =  3365
infinite_loop() : num =  3366
infinite_loop() : num =  3367
infinite_loop() : num =  3368
infinite_loop() : num =  3369
infinite_loop() : num =  3370
infinite_loop() : num =  3371
infinite_loop() : num =  3372
infinite_loop() : num =  3373
infinite_loop() : num =  3374
infinite_loop() : num =  3375
infinite_loop() : num =  3376
infinite_loop() : num =  3377
infinite_loop() : num =  3378
infinite_loop() : num =  3379
infinite_loop() : num =  3380
infinite_loop() : num =  3381
infinite_loop() : num =  3382
infinite_loop() : num =  3383
infinite_loop() : num =  3384
infinite_loop() : num =  
```

**Error:**
```
KeyboardInterrupt: 
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-10-4d16da1a3db1> in <cell line: 0>()
      6        print("infinite_loop() : num = ", num)
      7 
----> 8 infinite_loop()

<ipython-input-10-4d16da1a3db1> in infinite_loop()
      4        #yield num   # with yield it become generator without yield its a infinite loop
      5        num += 1
----> 6        print("infinite_loop() : num = ", num)
      7 
      8 infinite_loop()

/usr/local/lib/python3.11/dist-packages/ipykernel/iostream.py in write(self, string)
    400             is_child = (not self._is_master_process())
    401             # only touch the buffer in the IO thread to avoid races
--> 402             self.pub_thread.schedule(lambda : self._buffer.write(string))
    403             if is_child:
    404                 # mp.Pool cannot be trusted to flush promptly (or ever),

/usr/local/lib/python3.11/dist-packages/ipykernel/iostream.py in schedule(self, f)
    201             self._events.append(f)
    202             # wake event thread (message content is ignored)
--> 203             self._event_pipe.send(b'')
    204         else:
    205             f()

/usr/local/lib/python3.11/dist-packages/zmq/sugar/socket.py in send(self, data, flags, copy, track, routing_id, group)
    618                 )
    619             data.group = group
--> 620         return super().send(data, flags=flags, copy=copy, track=track)
    621 
    622     def send_multipart(

KeyboardInterrupt: 
```

## **Generator Expressions**
Generator expressions are a concise way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets.

Example:

```python
# Generator expression
gen = (x * x for x in range(5))
print(type(gen))

# Iterate over the generator
for value in gen:
    print(value, " : ", type(value))
```

**Output:**
```
<class 'generator'>
0  :  <class 'int'>
1  :  <class 'int'>
4  :  <class 'int'>
9  :  <class 'int'>
16  :  <class 'int'>
```

##**Recursive Function in Python**

A **recursive function** is a function that calls itself during its execution. It breaks down a problem into smaller, more manageable subproblems, solving each one recursively until a **base case** is reached. The base case is the condition that stops the recursion, preventing infinite loops.


## **Key Components of a Recursive Function**

*   **Base Case**: The condition that stops the recursion.
*   **Recursive Case**: The part of the function where it calls itself with a modified input.

## **Example: Factorial of a Number**

The factorial of a number n (denoted as n!) is the product of all positive integers from 1 to n. It can be defined recursively as:

-   n! = n * (n-1)! (Recursive Case)
-   0! = 1 (Base Case)

```python
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
```

**Output:**
```
120
```

**How It Works**

1.  factorial(5) calls factorial(4).
2.  factorial(4) calls factorial(3).
3.  This continues until factorial(0) is called, which returns 1.
4.  The results are propagated back up the chain:
  -   1 * 1 = 1
  -   2 * 1 = 2
  -   3 * 2 = 6
  -   4 * 6 = 24
  -   5 * 24 = 120

## **Example: Fibonacci Sequence**

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, ...

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(fibonacci(6))  # Output: 8
```

**Output:**
```
8
```

## **Advantages of Recursive Functions**

1.    Simplifies Code: Breaks complex problems into smaller, easier-to-understand parts.
2.    Elegant Solutions: Often provides a clean and concise solution for problems like tree traversals, sorting, and mathematical computations.
3.    Natural Fit for Certain Problems: Works well for problems with recursive structures (e.g., factorial, Fibonacci, tree traversals).

## **Disadvantages of Recursive Functions**

*   Stack Overflow: Deep recursion can lead to a stack overflow if the base case is not reached.
*   Performance Issues: Recursive functions can be slower and use more memory compared to iterative solutions due to repeated function calls.
*   Debugging Complexity: Recursive logic can be harder to debug and trace.

## **When to Use Recursive Functions**

* When the problem can be naturally divided into smaller subproblems.
* When the depth of recursion is limited and won’t cause stack overflow.
* For problems like tree traversals, divide-and-conquer algorithms, or mathematical sequences.

By understanding and using recursion effectively, you can solve complex problems in a clean and elegant way!

```python
# prompt: generate an example of recursive function

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
```

**Output:**
```
The factorial of 5 is 120
```

## **Multi Type Return in Function**


In Python, a function can return multiple values of different types by packaging them into a tuple, list, dictionary, or even a custom object. This is often referred to as a multi-type return. For example, a function can return an int, a list, and a dict together, providing flexibility in handling complex data. Type annotations (e.g., Tuple[int, List[str], Dict[str, int]]) can be used to specify the expected return types, making the code more readable and maintainable. Multi-type returns are useful when a function needs to provide diverse outputs, such as a status code, a list of results, and a dictionary of metadata, all in a single call.

```python
def example_function(a: int, b: int = 0, *args: float, **kwargs: str) -> Tuple[int, List[float], Dict[str, str]]:
    """Example function demonstrating various parameter types.
    Args:
        a: An integer.
        b: An integer with a default value of 0.
        *args: Variable-length positional arguments of type float.
        **kwargs: Variable-length keyword arguments of type string.
    Returns:
        A tuple containing:
        - The sum of 'a' and 'b'.
        - A list of the variable-length positional arguments ('args').
        - A dictionary of the variable-length keyword arguments ('kwargs').
    """
    sum_ab = a + b
    args_list = list(args)  # Convert tuple to a list
    return sum_ab, args_list, kwargs

# Example usage
result = example_function(1, 2, 3.14, 2.71, name="Alice", city="New York")
print(result)

result = example_function(10, *[1.0, 2.0, 3.0], **{"country": "USA", "language": "English"})
result
```

**Output:**
```
(3, [3.14, 2.71], {'name': 'Alice', 'city': 'New York'})
```

**Output:**
```
(11.0, [2.0, 3.0], {'country': 'USA', 'language': 'English'})
```

## **Order of args in function**



---



