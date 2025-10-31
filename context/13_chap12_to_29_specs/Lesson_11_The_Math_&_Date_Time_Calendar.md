# Lesson 11 The Math & Date Time Calendar

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>

# **The Date & Time**
----

## **What are Tick Intervals**

Time intervals are floating-point numbers in units of seconds. Particular instants in time are expressed in seconds since 12:00am, January 1, 1970.(epoch=a particular period of time in history or a person's life.).


## **What is Epoch?**

*Sounds: ee·pok (British), eh·puhk (American)*

<br>

In Python, the `epoch` is a reference `point in time` from which time is measured. It's the moment when time `"begins"` for a particular system or standard.

Think of it like the zero point on a number line.

The most commonly used epoch in Python (and many other systems) is:

**`January 1, 1970, 00:00:00 (UTC)`**




---




## **Why is there an epoch?**


- **Consistent Timekeeping**: Using a fixed point in the past allows computers and systems to calculate and compare time in a standardized way, regardless of when the system was built or where it's located.

- **Simplified Calculations**: It's easier to perform calculations with a single number representing the seconds (or milliseconds, etc.) that have passed since a fixed point, rather than dealing with complex date and time formats.


---





## **How is the epoch used in Python?**

Python's time module provides functions to work with time based on the epoch:

- **`time.time()`**: Returns the current time as a floating-point number of seconds since the epoch.
- **`time.gmtime(seconds)`**: Converts seconds since the epoch to a time tuple in Coordinated Universal Time (UTC).
- **`time.localtime(seconds)`**: Converts seconds since the epoch to a time tuple in local time.

```python
import time # This is required to include time module.
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)
```

**Output:**
```
Number of ticks since 12:00am, January 1, 1970: 1737690101.884116
```

## **Getting the Current Time**
----
To translate a time instant from seconds since the epoch floating-point value into a time-tuple, pass the floating-point value to a function (e.g., localtime) that returns a time-tuple with all valid nine items.

```python
import time
localtime = time.localtime(time.time())
print ("Local current time :", localtime)
```

**Output:**
```
Local current time : time.struct_time(tm_year=2025, tm_mon=1, tm_mday=24, tm_hour=3, tm_min=41, tm_sec=48, tm_wday=4, tm_yday=24, tm_isdst=0)
```

## **Getting the Formatted Time**
----
You can format any time as per your requirement, but a simple method to get time in a readable format is asctime() −

```python
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
```

**Output:**
```
Local current time : Thu Jan 23 20:55:57 2025
```

# **The Calendar**
----

## **Getting the Calendar for a Month**
----
The calendar module gives a wide range of methods to play with yearly and monthly calendars. Here, we print a calendar for a given month (Jan 2025).

```python
import calendar
cal = calendar.month(2025, 1)
print ("Here is the calendar:")
print (cal)
```

**Output:**
```
Here is the calendar:
    January 2025
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

```

## **The Date Time**
----

```python
from datetime import date

date1 = date(2023, 4, 19)
print("Date:", date1)
date2 = date(2023, 4, 30)
print("Date2:", date2)
```

**Output:**
```
Date: 2023-04-19
Date2: 2023-04-30
```

```python
import datetime

x = datetime.datetime.now() #The date contains year, month, day, hour, minute, second, and microsecond.
print(x)
```

**Output:**
```
2025-01-23 21:01:49.119953
```

## **The strftime() Method**
----
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

```python
import datetime

x = datetime.datetime(2025, 1, 1)

print(x.strftime("%f")) #Display Microsecond 000000-999999
print(x.strftime("%A")) #Display the name of the Day
print(x.strftime("%Y")) #Display the Year
print(x.strftime("%B")) #Display the name of the month

```

**Output:**
```
000000
Wednesday
2025
January
```

A reference of all the legal format codes:
[w3school](https://www.w3schools.com/python/python_datetime.asp)

# **Python Math Module**
----
The math module is a built-in module in Python that is used for performing mathematical operations. This module provides various built-in methods for performing different mathematical tasks.

Let see the different functions in action

```python
import math

# abs() returns the absolute value of a number
# In Python, abs() is a built-in function, which means it's a global function
# available in the standard library without needing to import any specific modules.
# You can use it directly in your code.
print("abs(-5) = ", abs(-5))  # outputs: 5

# pow() raises a number to a power
print("pow(2, 3) = ", pow(2, 3))  # outputs: 8

# round() rounds a number to a specified number of decimal places
print("round(3.14159, 2) = ", round(3.14159, 2))  # outputs: 3.14

# max() returns the largest of a set of numbers
print("max(1, 2, 3, 4, 5) = ", max(1, 2, 3, 4, 5))  # outputs: 5

# min() returns the smallest of a set of numbers
print("min(1, 2, 3, 4, 5) = ", min(1, 2, 3, 4, 5))  # outputs: 1

# math.sin() returns the sine of an angle in radians
print("math.sin(math.pi/2) = ", math.sin(math.pi/2))  # outputs: 1.0

# math.cos() returns the cosine of an angle in radians
print("math.cos(0) = ", math.cos(0))  # outputs: 1.0

# math.tan() returns the tangent of an angle in radians
print("math.tan(math.pi/4) = ", math.tan(math.pi/4))  # outputs: 1.0

# math.sqrt() returns the square root of a number
print("math.sqrt(9) = ", math.sqrt(9))  # outputs: 3.0

# math.factorial() returns the factorial of a number
print("math.factorial(5) = ", math.factorial(5))  # outputs: 120

# math.log() returns the natural logarithm of a number
print("math.log(10) = ", math.log(10))  # outputs: 2.302585092994046

# math.log10() returns the base-10 logarithm of a number
print("math.log10(100) = ", math.log10(100))  # outputs: 2.0

# math.exp() returns the value of e raised to a power
print("math.exp(2) = ", math.exp(2))  # outputs: 7.38905609893065

# math.ceil() returns the smallest integer greater than or equal to a number
print("math.ceil(4.7) = ", math.ceil(4.7))  # outputs: 5

# math.floor() returns the largest integer less than or equal to a number
print("math.floor(4.7) = ", math.floor(4.7))  # outputs: 4

# math.pi is a constant representing the ratio of a circle's circumference to its diameter
print("math.pi = ", math.pi)  # outputs: 3.14159265359

# math.e is a constant representing the base of the natural logarithm
print("math.e = ", math.e)  # outputs: 2.718281828459045

# math.tau is a constant representing the ratio of a circle's circumference to its radius
print("math.tau = ", math.tau)  # outputs: 6.283185307179586

# math.inf is a constant representing infinity
print("math.inf = ", math.inf)  # outputs: inf

# math.nan is a constant representing "not a number"
print("math.nan = ", math.nan)  # outputs: nan
```

**Output:**
```
abs(-5) =  5
pow(2, 3) =  8
round(3.14159, 2) =  3.14
max(1, 2, 3, 4, 5) =  5
min(1, 2, 3, 4, 5) =  1
math.sin(math.pi/2) =  1.0
math.cos(0) =  1.0
math.tan(math.pi/4) =  0.9999999999999999
math.sqrt(9) =  3.0
math.factorial(5) =  120
math.log(10) =  2.302585092994046
math.log10(100) =  2.0
math.exp(2) =  7.38905609893065
math.ceil(4.7) =  5
math.floor(4.7) =  4
math.pi =  3.141592653589793
math.e =  2.718281828459045
math.tau =  6.283185307179586
math.inf =  inf
math.nan =  nan
```

## **NaN**

In Python, `NaN` stands for `"Not a Number"`. It's a special floating-point value that represents an undefined or unrepresentable numerical result. It's a way for Python to indicate that a calculation or operation couldn't produce a valid numerical outcome.




```python
# Uncomment to see error

# result = 0 / 0  # Division by zero
# print(result)      # Output: nan

# result = math.sqrt(-1)  # Square root of a negative number
# print(result)      # Output: nan

result = float('nan')  # Explicitly creating NaN
print(result)      # Output: nan
```

**Output:**
```
nan
```

## **Working with NaN:**


Checking for NaN: You can use the math.isnan() function to check if a value is NaN

```python
import math

x = float('nan')
if math.isnan(x):
  print("x is NaN")
```

**Output:**
```
x is NaN
```

## **Important Notes:**

NaN compares unequal to any number, including itself. So, NaN == NaN is False.
Calculations involving NaN often result in NaN.

```python
x = float('nan')
y = float('nan')

print( x == y) # prints False
```

**Output:**
```
False
```

## **Infinity**

In Python, math.inf represents positive infinity, and it is indeed displayed as inf when you print it.

Here's a quick confirmation:

```python
import math

positive_infinity = math.inf
#positive_infinity = -math.inf # Negative infinity

print(positive_infinity)  # Output: inf
print(type(positive_infinity))  # Output: <class 'float'>
```

**Output:**
```
-inf
<class 'float'>
```

### **Key points to remember about math.inf:**

- Floating-point: math.inf is a floating-point value, not an integer.
- Comparisons: It's greater than any finite number.
- Operations: Many mathematical operations involving infinity will result in infinity (or NaN in some cases, like infinity minus infinity).
- Negative Infinity: For negative infinity, you would use -math.inf.

```python
import math

positive_infinity_1 = math.inf
positive_infinity_2 = math.inf

print(positive_infinity_1 - positive_infinity_2)  # Output: nan
print(positive_infinity_1 * 2)  # Output: inf
```

**Output:**
```
nan
inf
```

```python
import math

positive_infinity = math.inf
print(positive_infinity > 999999999999999999999999) #It's greater than any finite number.
```

**Output:**
```
True
```

