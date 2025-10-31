# Lesson 09 Exception Handling

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>

# **Exception Handling with try, except, else, and finally**


Exception handling is a crucial part of writing robust Python programs. It allows you to handle errors gracefully and ensure your program doesn't crash unexpectedly. In this tutorial, we'll cover the try, except, else, and finally blocks with examples.

## **Importance of Exception Handling in Python**

Exception handling is essential for creating robust and reliable Python programs. Here’s why it matters and the consequences of not using it:

## **Why Use Exception Handling?**

*   **Prevents Program Crashes**: Ensures your program doesn’t terminate abruptly due to unexpected errors.

*   **Graceful Error Recovery**: Allows you to handle errors gracefully and provide meaningful feedback to users.
*   **Clean Code**: Separates error-handling logic from the main program flow, making code more readable and maintainable.
*   **Resource Management**: Ensures resources (e.g., files, connections) are properly released, even if an error occurs.

## **What Happens If You Don’t Use Exception Handling?**

*   **Program Crashes**: Unhandled exceptions cause the program to terminate, leading to a poor user experience.

*  ** Data Loss**: Critical operations (e.g., saving data) may fail, resulting in data corruption or loss.
*   **Security Risks**: Exposing raw error messages can reveal sensitive information or system details to attackers.
*   **Unpredictable Behavior**: Errors propagate through the program, making debugging difficult and increasing development time.

## **Scenarios Where Exception Handling is Crucial**

*   **File Operations**: Handling missing files or permission errors during file access.

*   **User Input**: Validating and handling invalid or unexpected input from users.
*   **Network Operations**: Managing connection errors or timeouts in network requests.
*   **Mathematical Operations**: Preventing division by zero or invalid calculations.

## **Consequences of Not Handling Exceptions**

*   **User Frustration**: Users see cryptic error messages instead of helpful feedback.

*   **Increased Debugging Effort**: Developers spend more time tracing and fixing errors.
*   **System Instability**: Unhandled errors can cause cascading failures in larger systems.
*   **Loss of Trust**: Frequent crashes or errors can damage the program’s credibility.

By incorporating exception handling, you ensure your program is robust, user-friendly, and resilient to unexpected issues.

## **1. The try Block**

The try block is used to test a block of code for errors. If an error occurs within the try block, the program will immediately jump to the except block (if provided).

```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except:
    print("An error occurred!")
```

**Output:**
```
An error occurred!
```

## **2. The except Block**


The except block is used to handle specific errors that occur in the try block. You can specify the type of error to catch, or use a generic except to catch all errors.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

**Output:**
```
Cannot divide by zero!
```

## **3. The else Block**


The else block is executed if no errors occur in the try block. It is optional and is used for code that should only run when the try block is successful.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful. Result: {result}")
```

**Output:**
```
Division successful. Result: 5.0
```

## **4. The finally Block**


The finally block is executed regardless of whether an error occurred or not. It is often used for cleanup operations, such as closing files or releasing resources.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")
```

**Output:**
```
Cannot divide by zero!
This will always execute.
```

## **5. Putting It All Together**

Here’s an example that combines all four blocks:

```python
def divide_numbers(a, b):
    try:
        result = a / b  # Test this block for errors
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete.")

# Test cases
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers(10, "2")  # TypeError
```

**Output:**
```
Division successful. Result: 5.0
Operation complete.
Error: Cannot divide by zero!
Operation complete.
Error: Invalid input type. Numbers required.
Operation complete.
```

## **Key Points Covered:**

1.  try Block: Used to test a block of code for errors.
2.  except Block: Used to handle specific or generic errors.
3.  else Block: Executes when no errors occur in the try block.
4.  finally Block: Executes regardless of whether an error occurred.

```python
# prompt: generate a learning code on error handling covering all the expects

import random
from typing import Tuple, Dict, List

def generate_random_data(num_samples: int) -> List[Tuple[int, int]]:
    """Generates a list of random number pairs."""
    try:
        if not isinstance(num_samples, int) or num_samples <= 0:
            raise ValueError("Number of samples must be a positive integer.")
        data = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(num_samples)]
        return data
    except ValueError as ve:
        print(f"Error: {ve}")
        return []  # Return empty list on error
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []


def calculate_ratios(data: List[Tuple[int, int]]) -> List[float]:
    """Calculates the ratio of the first number to the second in each pair."""
    ratios = []
    try:
        for pair in data:
            num1, num2 = pair
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            if not isinstance(num1,int) or not isinstance(num2,int):
                raise TypeError("Input data must be integers.")
            ratio = num1 / num2
            ratios.append(ratio)
        return ratios
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        return []  # Return empty list on error.
    except TypeError as te:
        print(f"Error: {te}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during ratio calculation: {e}")
        return []


def process_data(num_samples: int) -> List[float]:
    """Combines data generation and ratio calculation with comprehensive error handling."""

    data = generate_random_data(num_samples)
    if not data: # check if generate_random_data returns an empty list which means it had an error
        return []

    ratios = calculate_ratios(data)

    return ratios

# Example usage with error handling
try:
  num_samples = 10
  results = process_data(num_samples)

  if results:
    print("Calculated ratios:", results)
  else: # if process_data returned an empty list it means there was some error
      print("Data processing failed due to an error.")

except Exception as e: # catching unexpected errors
    print(f"An unexpected error occurred: {e}")

# example of invalid input
results = process_data(-5)
if not results:
  print("Negative number of samples, data processing failed.")

results = process_data("abc")
if not results:
    print("Invalid input type, data processing failed.")


```

**Output:**
```
Calculated ratios: [0.48, 2.3, 1.3870967741935485, 2.9285714285714284, 0.5945945945945946, 0.8, 16.25, 0.723404255319149, 4.142857142857143, 0.922077922077922]
Error: Number of samples must be a positive integer.
Negative number of samples, data processing failed.
Error: Number of samples must be a positive integer.
Invalid input type, data processing failed.
```

## **Practice Problem:**

Write a Python program that asks the user for two numbers and divides them. Use exception handling to catch any errors that might occur (e.g., division by zero or invalid input).

```python
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the program!")
```

**Output:**
```
Enter the first number: 0
Enter the second number: 0
Error: Cannot divide by zero.
Thank you for using the program!
```

* By following this tutorial, you should now have a solid understanding of how to handle exceptions in Python using try, except, else, and finally. Happy coding!

* Now we will learn how to throw exception from a custome defined function.


## **How a Function Throws an Exception in Python?**

In Python, a function can throw an exception using the raise keyword. This is used to indicate that an error has occurred, and it interrupts the normal flow of the program.

### **When an exception is raised:**

1.  Python immediately stops executing the function.
2.  The error message is displayed unless the exception is handled using try-except.


### **Basic Example of Throwing an Exception**

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")  # Raising an exception
    return a / b

print(divide(10, 2))  # Output: 5.0
print(divide(5, 0))   # Raises: ValueError: Division by zero is not allowed!
```

**Output:**
```
5.0
```

**Error:**
```
ValueError: Division by zero is not allowed!
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-18-956cb8f45dc3> in <cell line: 0>()
      5 
      6 print(divide(10, 2))  # Output: 5.0
----> 7 print(divide(5, 0))   # Raises: ValueError: Division by zero is not allowed!

<ipython-input-18-956cb8f45dc3> in divide(a, b)
      1 def divide(a, b):
      2     if b == 0:
----> 3         raise ValueError("Division by zero is not allowed!")  # Raising an exception
      4     return a / b
      5 

ValueError: Division by zero is not allowed!
```

🔹 In this example, if b == 0, we explicitly raise a ValueError.

🔹 The function stops execution at raise and does not return anything.


## **Handling the Exception with try-except**

To prevent the program from crashing, we can use try-except to handle the exception.

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

try:
    result = divide(5, 0)  # This will raise an exception
    print(result)  # This line won't run if exception occurs
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Division by zero is not allowed!

print("Program continues...")  # This line will always execute
```

**Output:**
```
Error: Division by zero is not allowed!
Program continues...
```

## **Throwing Custom Exceptions**

Python also allows you to define custom exceptions by creating a new class that inherits from Exception.

```python
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"{n} is positive"

try:
    print(check_positive(-5))  # Raises NegativeNumberError
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}", " - Exception Class Type: ", type(e))  # Output: Custom Exception Caught: Negative numbers are not allowed!
```

**Output:**
```
Custom Exception Caught: Negative numbers are not allowed!  - Exception Class Type:  <class '__main__.NegativeNumberError'>
```

## **Summary**

✔ Use raise to throw an exception inside a function.

✔ Use try-except to handle exceptions and prevent crashes.

✔ Create custom exceptions by inheriting from Exception.



## **Equivalent of throw and throws in Python**

In Java, **throw** and **throws** are used for exception handling. Python doesn’t have a direct equivalent to throws, but throw is equivalent to Python's raise.

## **1️⃣ Equivalent of throw in Python → raise**

* In Java, throw is used to explicitly raise an exception.
* In Python, raise is used to do the same thing.


## **2️⃣ Equivalent of throws in Python**

* In Java, throws is used in method signatures to declare checked exceptions that the method might raise.

* Python does not require explicit declaration of exceptions in function signatures.
* However, you can document it using **`docstrings`** or **`type hints`**.

<br>

✔ Python doesn’t enforce throws, but you can document exceptions in docstrings or use type hints (NoReturn).




## **What is NoReturn?**

**NoReturn** is a special type hint from Python's typing module. It is used to indicate that a function will not return normally. This means the function either:

* Always raises an exception,

* Enters an infinite loop,
* Or otherwise never reaches the end of the function body to return a value.

<br>

## **When Would You Use NoReturn?**

* Functions that Always Raise Exceptions:
For example, a function that immediately raises an error can be annotated with NoReturn to signal that it doesn't produce a return value.

* Infinite Loops:
A function that runs forever (or until the program is terminated) is a candidate for NoReturn.

<br>

## **Example: Using NoReturn**



```python
from typing import NoReturn

def terminate_program() -> NoReturn:
    """Terminate the program by raising an exception."""
    raise SystemExit("Terminating the program.")

# When you call terminate_program, it never returns normally:
try:
    terminate_program()
except SystemExit as e:
    print(f"Program terminated: {e}")
```

**Output:**
```
Program terminated: Terminating the program.
```

### **In this example:**

* The function terminate_program() is annotated with -> NoReturn, indicating that it will not return normally.

* Instead, it raises a SystemExit exception, causing the program to exit (or be caught as shown).

## **Why Use NoReturn?**

* **Improved Readability**: It makes your intent clear to anyone reading your code.

* **Better Static Analysis**: Tools like mypy can use these annotations to detect issues in your code, ensuring that functions marked with NoReturn truly do not return a value.

Using `NoReturn` helps set clear expectations about a function's behavior, making your code more robust and easier to understand.

## **Alternative to NoReturn in Python**


`NoReturn` from the `typing module` is used to indicate that a function never returns normally. However, if you don’t want to use NoReturn, you have a few alternative approaches.

## **1️⃣ Alternative: Using `None` Instead of `NoReturn`**

If your function does not return any meaningful value but does not necessarily terminate the program (e.g., it performs logging, prints messages, etc.), you can use `None` as the return type `instead of NoReturn`.

### **Example: Using None**

```python
def log_error(message: str) -> None:
    """Logs an error message but does not terminate the program."""
    print(f"Error: {message}")

log_error("Something went wrong!")
```

**Output:**
```
Error: Something went wrong!
```

✔ Use -> None when the function completes execution but does not return a value.

❌ Do NOT use -> None if the function always raises an exception or runs indefinitely.

## **2️⃣ Alternative: Omitting the Return Type Hint**

Python does not require type hints, so if you are not using static type checking tools like mypy, you can simply omit the return type hint.

### **Example: No Type Hint**

```python
def terminate_program():
    """Terminates the program by raising an exception."""
    raise SystemExit("Program is terminating.")

terminate_program()
```

**Error:**
```
SystemExit: Program is terminating.
An exception has occurred, use %tb to see the full traceback.

SystemExit: Program is terminating.

```

**Output:**
```
/usr/local/lib/python3.11/dist-packages/IPython/core/interactiveshell.py:3561: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
  warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)
```

✔ Works fine, but loses clarity for static analysis tools.

## **When Should You Stick to NoReturn?**

If you are using type checking tools like mypy, NoReturn is still the best choice for functions that:

* Always raise an exception

* Never return (e.g., an infinite loop)
* Terminate the program (sys.exit())

✅ But if you are not using static type checking, omitting the type hint or using None may be enough.

