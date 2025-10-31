# Lesson 02 Data Types

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>



# **Python Data Types**


---

Data types determine the type of value a variable can hold and the operations that can be performed on it. They define the format, structure, size, range, and behavior of data, controlling how it's stored and used in a program. This helps ensure data is used correctly and efficiently.

# **1. Numeric Types**
Python has three main numeric types:

##a. Integer (int)
Whole numbers, positive or negative, without decimals.

```python
num_int: int = 42

print(type(num_int)," num_int = ",num_int,)  # <class 'int'>
```

**Output:**
```
<class 'int'>  num_int =  42
```

##b. Floating-Point (float)
Numbers with decimal points.

```python
num_float: float = 3.14
#num_float: float = .14

print(type(num_float), " num_float = ", num_float)  # <class 'float'>
```

**Output:**
```
<class 'float'>  num_float =  0.14
```

##c. Complex (complex)
Numbers with a real and imaginary part.

```python
num_complex: complex = 2 + 3j

print(type(num_complex), " num_complex = ", num_complex)  # <class 'complex'>
```

**Output:**
```
<class 'complex'>  num_complex =  (2+3j)
```

## **Accessing Real and Imaginary Parts**
Python provides attributes .real and .imag to extract the real and imaginary parts of a complex number.

*(Contributor: Areeba Zafar from Karachi)*

```python
z = 3 + 4j

print("Real Part:", z.real)   # Output: 3.0
print("Imaginary Part:", z.imag)  # Output: 4.0
```

**Output:**
```
Real Part: 3.0
Imaginary Part: 4.0
```

# **2. Boolean (bool)**
Represents True or False.

```python
is_python_fun: bool = True #False

print(type(is_python_fun), " is_python_fun = ", is_python_fun)  # <class 'bool'>
```

**Output:**
```
<class 'bool'>  is_python_fun =  True
```

# **3. Sequence Types**
These store multiple items in an ordered way.

##a. String (str)
A sequence of characters enclosed in quotes.

```python
text_double: str  = "Hello, Python!" # Strings with Double Quotes (")
text_single: str  = 'Hello, Python!' # Strings with Single Quotes (')
text_multi: str   = '''Hello, Python!''' # Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, Python!""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)    # <class 'str'>
print(type(text_single), " text_single   = ", text_single)    # <class 'str'>
print(type(text_multi), " text_multi    = ", text_multi)      # <class 'str'>
print(type(text_multi_1), " text_multi_1  = ", text_multi_1)  # <class 'str'>

```

**Output:**
```
<class 'str'>  text_double   =  Hello, Python!
<class 'str'>  text_single   =  Hello, Python!
<class 'str'>  text_multi    =  Hello, Python!
<class 'str'>  text_multi_1  =  Hello, Python!
```

##Key Takeaways
- Double Quotes ("): Use when the string contains single quotes.
- Single Quotes ('): Use when the string contains double quotes.
- Triple Quotes (''' or """): Use for multi-line strings or docstrings.

<br>

Understanding these variations allows you to `write cleaner, more readable, and error-free code`. As you progress in Python, you’ll find that strings are incredibly powerful, especially when combined with string methods, formatting, and manipulation techniques.

##b. List (list)
An ordered, mutable collection.

```python
my_list_1: int = [1, 2, 3, "Java", 3.14, True] #Type hinting is not enforced in python, but you should mention appropriate data type in this case 'list'
my_list: list = [1, 2, 3, "Python", 3.14, 3+2j]

print(type(my_list_1), " my_list_1 = ", my_list_1)  # <class 'list'>
print(type(my_list), " my_list   =  " + str(my_list)) # we will look into type casting in classes ahead
```

**Output:**
```
<class 'list'>  my_list_1 =  [1, 2, 3, 'Java', 3.14, True]
<class 'list'>  my_list   =  [1, 2, 3, 'Python', 3.14, (3+2j)]
```

##c. Tuple (tuple)
An ordered, immutable collection.

```python
my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3 , 3+2j )
print(type(my_tuple), " my_tuple = ", my_tuple )  # <class 'tuple'>
```

**Output:**
```
<class 'tuple'>  my_tuple =  (1, 2, 3, 'AI', 2.71, False, 0.3, (3+2j))
```

## d. Range (range)
Represents a sequence of numbers.

```python
num_range: range = range(1, 10, 2) # range(start, stop, step)
print(type(num_range), " num_range = ", num_range.step)  # <class 'range'>
```

**Output:**
```
<class 'range'>  num_range =  2
```

```python
for i in range(1, 10, 2): # we will study loops indepth in classes ahead
  print(i)
```

**Output:**
```
1
3
5
7
9
```

# **4. Set Types**
`(We will cover this indepth in classes ahead)`

Unordered collections with unique elements.

## a. Set (set)
`Mutable`, `unordered`, and contains `unique values`.

```python
my_set: set = {1, 2, 33, 4, 4, 5}
print(type(my_set), "my_set = ", my_set)  # <class 'set'>
```

**Output:**
```
<class 'set'> my_set =  {1, 2, 33, 4, 5}
```

## b. Frozen Set (frozenset)
Immutable version of a set.

```python
frozen_set = frozenset([11, 2, 3, 4, 4, 5])
#frozen_set = frozenset(my_set)
print(type(frozen_set), " frozen_set = ", frozen_set)  # <class 'frozenset'>
```

**Output:**
```
<class 'frozenset'>  frozen_set =  frozenset({1, 2, 33, 4, 5})
```

# **5. Mapping Type**

Dictionary (dict)
Stores key-value pairs.

```python
my_dict: dict = {"name": "Alice", "age": 25, "language": "Python"}
print(type(my_dict)," my_dict = ", my_dict )  # <class 'dict'>
```

**Output:**
```
<class 'dict'>  my_dict =  {'name': 'Alice', 'age': 25, 'language': 'Python'}
```

# **6. Binary Types**
In Python, binary types are used to handle binary data, such as raw bytes, binary files, or data exchanged over networks. Binary types are distinct from text types (str) and are specifically designed to represent and manipulate sequences of bytes. Python provides three built-in binary types:

<br>

## a. Bytes (bytes)

1.  **Definition**: An immutable sequence of bytes.

2.  **Purpose**: Used to represent binary data, such as byte sequences coming from files, network communications, or raw data.

3.  **Key Points**:
    * A bytes object is immutable, meaning you cannot modify its content after creation.
    * It is often used when you need to work with fixed binary data.
    * Literal syntax: b"..." or b'...'.

```python
byte_data: bytes = b"Hello"
print(type(byte_data), " byte_data = ", byte_data)  # <class 'bytes'>
```

**Output:**
```
<class 'bytes'>  byte_data =  b'Hello'
```

### **Its just an example to give you feel about how to work with binary data.**

`We will learn more about file handling in classes ahead.`

```python
# Open an image file in binary mode
with open("Apollo11.jpg", "rb") as image_file:
    image_data = image_file.read()

print(image_data)
```

```python
with open("Apollo11.jpg", "rb") as source_file:
    data = source_file.read()

# Write the binary data to a new image file
with open("copy.jpg", "wb") as target_file:
    target_file.write(data)

print("Image copied successfully!")
```

**Output:**
```
Image copied successfully!
```

## b. Bytearray (bytearray)

1.  **Definition**: A mutable sequence of bytes.

2.  **Purpose**: Like bytes, but allows modification of its content.

3.  **Key Points**:
    * You can modify the content of a bytearray object in place.
    * Suitable for cases where you need to update or manipulate binary data frequently.
    * Literal syntax: Does not have direct literal syntax (must use bytearray() constructor).



## **Number Systems**

* **ASCII**:

  The American Standard Code for Information Interchange (ASCII) is a character encoding standard that represents text in computers using numeric codes. It maps 128 characters (letters, digits, punctuation, and control characters) to values from 0 to 127.

* **Decimal**:

  The decimal system is the standard numerical system used in everyday life, based on 10 digits (0 through 9). It's a base-10 system, where each digit's position represents a power of 10.

* **Hexadecimal**:

  The hexadecimal system is a base-16 numbering system, using 16 symbols: 0–9 to represent values 0 to 9, and A–F (or a–f) to represent values 10 to 15. It's widely used in computing for compact representation of binary data.

* **Octal**:

  The octal system is a base-8 numbering system, using digits 0 through 7. It was more commonly used in older computer systems and is still occasionally used in modern computing, especially for file permissions in Unix/Linux.

* **Binary**:

  The binary system is a base-2 numbering system that uses only two digits: 0 and 1. It's the fundamental language of computers, where each binary digit (bit) represents a state of off or on.

<br>

### **What is a Base in Number Systems?**

A base (or radix) in a number system refers to the number of **`unique digits`** (including zero) used to represent numbers. It defines how place values are assigned to digits in a numeral.

<br>

[ASCII, decimal, hexadecimal, octal, and binary conversion table](https://www.ascii-code.com/ASCII)


```python
byte_array: bytearray = bytearray([65, 66, 67, 69]) #65=A, 66=B ....decimal number system
print(type(byte_array), " byte_array = ", byte_array)  # <class 'bytearray'>
print(byte_array[0])
print(chr(byte_array[0]))
print("Empty bytearray(): ",bytearray())
```

**Output:**
```
<class 'bytearray'>  byte_array =  bytearray(b'ABCE')
65
A
Empty bytearray():  bytearray(b'')
```

### **What is UTF-8?**

UTF-8 (8-bit Unicode Transformation Format) is a variable-length character encoding that can represent every character in the Unicode standard. It is designed for efficiency and compatibility:

```python
byte_array: bytearray = bytearray([65, 66, 67, 69])
# Converting the entire bytearray to a string using decode()
print("Decoded string: ", byte_array.decode('utf-8'))  # Output: ABCE
```

**Output:**
```
Decoded string:  ABCE
```

```python
# Creating a bytearray object
ba: bytearray = bytearray(b"hello")
print("Before: ba = ", ba)

# Modifying the bytearray
ba[0] = 72  # ASCII value of 'H'

print("After: ba = ",ba)  # Output: bytearray(b'Hello')
```

**Output:**
```
Before: ba =  bytearray(b'hello')
After: ba =  bytearray(b'Hello')
```

## c. Memoryview (memoryview)

The memoryview object in Python provides an efficient way to work with binary data by allowing you to access and manipulate the memory of another object (like bytes or bytearray) without copying the data. This is particularly useful when working with large datasets or binary streams, as it avoids the overhead of creating additional copies.

```python
mem_view: memoryview = memoryview(b"Operation Badar")
print(type(mem_view), " mem_view = ", mem_view)  # <class 'memoryview'>
print(bytes(mem_view[0:5]))
print( mem_view[6:11] ) #cast it to byte otherwise it will show memory address
```

**Output:**
```
<class 'memoryview'>  mem_view =  <memory at 0x7d294da28b80>
b'Opera'
<memory at 0x7d294da28f40>
```

**None Data Type in Python**
==========================

In Python, `None` is a special data type that represents the absence of a value or a null object reference. It is a `singleton object`, meaning that there is `only one instance` of `None` in the entire Python environment.

* **No value**: `None` represents the absence of a value or a null object reference.

```python
x: str = None
y: str = None
z: str = x

#display the data type of x:
print(type(x))
print("value of x = " + str(x) )
print("x == y = ", x == y)
print("id(x) = ", id(x))
print("id(y) = ", id(y))
print("id(z) = ", id(z))
print("x is y = ", x is y)
print("x is z = ", x is z)
print("id(x) is id(z) = ", id(x) is id(z)) # False :( why? you will get the answer in topic 'Integer Literals in Python'
print("id(x) == id(z) = ", id(x) == id(z)) # True
'''
In Python, `==` is the equality operator, which checks if the values of two objects are equal.
On the other hand, `is` is the identity operator, which checks if two objects are the same object in memory.
'''
```

**Output:**
```
<class 'NoneType'>
value of x = None
x == y =  True
id(x) =  9691392
id(y) =  9691392
id(z) =  9691392
x is y =  True
x is z =  True
id(x) is id(z) =  False
id(x) == id(z) =  True
```

```python
print("None is None            = ", None is None) # True
print("None == None            = ", None == None) # True
print("None == x               = ", None == x)
print("None is x               = ", None is x)
print("id(None) is id(None)    = ", id(None) is id(None)) # 'is' check memory space sharing
#If number is out of integer literal range -5 to 256 then even the same number are considered as seprate object
```

**Output:**
```
None is None            =  True
None == None            =  True
None == x               =  True
None is x               =  True
id(None) is id(None)    =  False
```

**id() Function in Python**
==========================

The `id()` function in Python returns the `unique identifier` for an `object`. This identifier is a small integer that is unique among all objects currently in existence of your python environment.

**What is the Purpose of id()**
-----------------------------

The `id()` function is used to:

* **Identify objects**: The `id()` function returns a `unique identifier` that can be used to identify objects in memory.
* **Check object equality**: By checking the `id()` of two objects, you can determine if they are the `same object in memory`.
* **Debugging**: The `id()` function can be useful for debugging purposes, such as identifying which object is being referenced by a variable.

```python
print("""Variable x, y & z have 'None' value, as we know that 'None' is a singleton object,
meaning that there is only one instance of `None` in the entire Python environment.
So the id(x), id(y) & id(z) represents the same object id in memory.\n""")

x: str = None
y: str = None
z: str = x

print("ID of variable x  = " + str(id(x)))
print("ID of variable y  = " + str(id(y)))
print("ID of variable z  = " + str(id(z)))

print("\nIs variable x & y shares the same memory space? \nThe answer is: " + str(id(x) == id(y)))
```

**Output:**
```
Variable x, y & z have 'None' value, as we know that 'None' is a singleton object,
meaning that there is only one instance of `None` in the entire Python environment.
So the id(x), id(y) & id(z) represents the same object id in memory.

ID of variable x  = 9691392
ID of variable y  = 9691392
ID of variable z  = 9691392

Is variable x & y shares the same memory space? 
The answer is: True
```

**False in a boolean context**: `None` is considered `False` in a boolean context, meaning that it can be used in conditional statements.


```python
if(None):
  print("if block: This line of code will not execute because in Python 'None' is considered False")
else:
  print("else block: As None is considered False, so this line of code will execute")
```

**Output:**
```
else block: As None is considered False, so this line of code will execute
```

**Integer Literals in Python**
==========================

In Python, an integer literal is a sequence of characters that represents an integer value. Integer literals are used to define integer constants in Python code.

**Memory Space Sharing**
================================

In Python, integer literals can share the `same memory space` under certain conditions. This is due to a process called **`interning`**, where Python stores a pool of interned objects that can be reused when the same value is needed again.

Lets assign value to variable x, y & z

```python
x: int = 1
y: int = 1
z: int = x

print("Value of x = " + str(x) + ", and id(x) = " + str(id(x))) # when you need to concatinate any thing with string you need to first cast it to str()
print("Value of y = " + str(y) + ", and id(y) = " + str(id(y)))
print("Value of z = " + str(z) + ", and id(z) = " + str(id(z)))
print("id(x) == id(y) = ", id(x) == id(y) )
print("id(x) is id(y) = ", id(x) is id(y) ) # ;)
```

**Output:**
```
Value of x = 1, and id(x) = 10750856
Value of y = 1, and id(y) = 10750856
Value of z = 1, and id(y) = 10750856
id(x) == id(y) =  True
id(x) is id(y) =  False
```

**Integer Interning in Python**
-----------------------------

In Python, integers in the range *`-5 to 256`* are interned, meaning that they are stored in a `pool of interned objects`. This means that when you create an integer literal within this range, Python returns a reference to the existing object in the pool.

```python
x = -6
y = -6
z = x

print("Value of x = " + str(x) + ", and id(x) = " + str(id(x)))
print("Value of y = " + str(y) + ", and id(y) = " + str(id(y)))
print("Value of z = " + str(z) + ", and id(z) = " + str(id(z)))

print("\n ===================== \n")

a = 257
b = 257
c = a

print("Value of x = " + str(a) + ", and id(a) = " + str(id(a)))
print("Value of y = " + str(b) + ", and id(b) = " + str(id(b)))
print("Value of z = " + str(c) + ", and id(c) = " + str(id(c)))
```

**Output:**
```
Value of x = -6, and id(x) = 133526994143664
Value of y = -6, and id(y) = 133526994150640
Value of z = -6, and id(y) = 133526994143664

 ===================== 

Value of x = 257, and id(a) = 133526994150128
Value of y = 257, and id(b) = 133526994151344
Value of z = 257, and id(c) = 133526994150128
```

Greenland Shark. Living in the waters of—you guessed it—Greenland, this shark lives for 300 to 500 years. It has the longest known lifespan of any vertebrate species

```python
shark1_age = 300
shark2_age = 300

print("Value of shark1_age = " + str(shark1_age) + ", and id(shark1_age) = " + str(id(shark1_age)))
print("Value of shark2_age = " + str(shark2_age) + ", and id(shark2_age) = " + str(id(shark2_age)))

if(shark1_age == shark2_age): #comparison by value
  print("shark1_age & shark2_age have same age")
else:
  print("shark1_age & shark2_age have different age")

print(" ===================== ")

if(id(shark1_age) == id(shark2_age)):#comparison by id()
  print("shark1_age & shark2_age have same id")
else:
  print("shark1_age & shark2_age have different id")
```

**Output:**
```
Value of shark1_age = 300, and id(shark1_age) = 133526994151600
Value of shark2_age = 300, and id(shark2_age) = 133526994146032
shark1_age & shark2_age have same age
 ===================== 
shark1_age & shark2_age have different id
```

# **Type Casting**
----------------

Type casting is the process of converting a value of one data type to another data type. Python supports several types of type casting, including:

1. **Implicit Type Casting**: Python automatically converts a value of one data type to another data type when necessary. For example, when you add an integer and a float, Python converts the integer to a float.
2. **Explicit Type Casting**: You can use functions like `int()`, `float()`, `str()`, and `bool()` to explicitly convert a value of one data type to another data type.

```python
i: int = 10
print("Value of i = " + str(i) + ",     Type of i = " + str(type(i)))

j: float = 20.6

f: float = i + j #Implicit Type Casting
print("Value of f = " + str(f) + ",   Type of f = " + str(type(f)))

f1: float = 66.89
print("Value of f1 = " + str(f1) + ", Type of i = " + str(type(f1)))

i1: int = int(f1) #When ever you type cast a float value into an integer it truncate
             #the decimal part and only keeps the whole number
print("Value of i1 = " + str(i1) + ",    Type of i = " + str(type(i1)))

s: str = "25.8"
f2: float = float(s)
print("Value of f2 = " + str(f2) + ",  Type of i = " + str(type(f2)))

#uncomment the below line of code to see error
#i2 = int(s) #correct this error by casting with float()
#print("Value of i2 = " + str(i2) + ", Type of i = " + str(type(i2)))

```

**Output:**
```
Value of i = 10,     Type of i = <class 'int'>
Value of f = 30.6,   Type of f = <class 'float'>
Value of f1 = 66.89, Type of i = <class 'float'>
Value of i1 = 66,    Type of i = <class 'int'>
Value of f2 = 25.8,  Type of i = <class 'float'>
```

**Truthy and Falsy Values in context of boolean data type**
-------------------------

In Python, some values are considered **truthy**, while others are considered **falsy**. Truthy values are treated as `True` in a boolean context, while falsy values are treated as `False`.

Here are some examples of truthy and falsy values:

* Truthy values:
	+ Non-zero integers (e.g., `1`, `2`, `-3`, etc.)
	+ Non-empty strings (e.g., `"hello"`, `"world"`, etc.)
	+ Non-empty lists (e.g., `[1, 2, 3]`, `["a", "b", "c"]`, etc.)
	+ Non-empty dictionaries (e.g., `{"a": 1, "b": 2}`, etc.)
* Falsy values:
	+ Zero (e.g., `0`)
	+ Empty strings (e.g., `""`)
	+ Empty lists (e.g., `[]`)
	+ Empty dictionaries (e.g., `{}`)
	+ `None`

```python
k: int = -9 #Any number either positive or negative, beside '0' ZERO is considered True
b: bool = bool(k)
print("Value of b = " + str(b) + ", Type of b = " + str(type(b)))

print("\n =================== \n")

if(k):
  print("""if block: This line of code will execute if we provide any integer value
          other then '0' ZERO""")
else:
  print("else block: As '0' is considered False, so this line of code will not execute")

print("\n =================== \n")

print("check: bool(\"55\")             = ", bool("55"))
print("check: bool(\"\")               = ", bool(""))
print("check: bool([1, 2, 3])        = ", bool([1, 2, 3]))
print("check: bool({\"key\", \"value\"}) = ", bool({"key", "value"}))

#Note: we will learn about list and dictionary in up comming classes
print("check: bool([])               = ", bool([])) #[] square brackets used to represent list
print("check: bool({})               = ", bool({})) #{} curly brackets used to represent dictionary
```

**Output:**
```
Value of b = True, Type of b = <class 'bool'>

 =================== 

if block: This line of code will execute if we provide any integer value
          other then '0' ZERO

 =================== 

check: bool("55")             =  True
check: bool("")               =  False
check: bool([1, 2, 3])        =  True
check: bool({"key", "value"}) =  True
check: bool([])               =  False
check: bool({})               =  False
```

**isinstance() Function in Python**
==================================

The `isinstance()` function in Python is used to check if an object (first argument) is an instance of a class (second argument). It returns `True` if the object is an instance of the class, and `False` otherwise.

**Syntax**
---------

The syntax of the `isinstance()` function is as follows:
```python
isinstance(object, classinfo)
```
Where:

* `object` is the object to be checked.
* `classinfo` is the class or a tuple of classes to check against.


```python
age: int = 20
weight: float = 66.89
print("check: isinstance(age, int)      = ", isinstance(age, int))
print("check: isinstance(weight, int)   = ", isinstance(weight, int))
print("check: isinstance(weight, float) = ", isinstance(weight, float))
```

**Output:**
```
check: isinstance(age, int)      =  True
check: isinstance(weight, int)   =  False
check: isinstance(weight, float) =  True
```

