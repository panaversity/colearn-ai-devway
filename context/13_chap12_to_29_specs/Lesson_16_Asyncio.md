# Lesson 16 Asyncio

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>


**Introduction to Asyncio in Python**
=====================================

Asyncio is a library in Python that allows you to write single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, and implementing network clients and servers.


**Asyncio in Python: A Simplified Explanation**
=====================================================

Imagine you're at a coffee shop, and you want to order a coffee and a pastry. There are two ways to do this:

1.  **`Synchronous Approach`**: You order the coffee, wait for it to be prepared, and then order the pastry. You can't do anything else until both orders are completed.
2.  **`Asynchronous Approach`**: You order the coffee and, while it's being prepared, you order the pastry. You can do other things, like checking your phone or chatting with a friend, until both orders are ready.

**Asyncio in Python works similarly to the asynchronous approach**. It allows your program to perform multiple tasks concurrently, improving efficiency and responsiveness.

**Key Concepts**
----------------

*   **`Coroutines`**: A coroutine is a special type of function that can suspend and resume its execution at specific points. Think of it as a task that can be paused and resumed.
*   **`Event Loop`**: The event loop is the central component of Asyncio. It manages the execution of coroutines, handling I/O operations and scheduling tasks.
*   **`Tasks`**: A task is a coroutine that's scheduled to run concurrently with other tasks.
*   **`Futures`**: A future represents the result of a task. You can wait for a future to complete, allowing you to retrieve the result of a task.



<font color=orange> By design asyncio does not allow its event loop to be nested. This presents a practical problem: When in an environment where the event loop is already running it’s impossible to run tasks and wait for the result. Trying to do so will give the error “RuntimeError: This event loop is already running”.

<font color=orange>The issue pops up in various environments, such as web servers, GUI applications and in **`Jupyter notebooks`**. </font>

This module patches asyncio to allow nested use of asyncio.run and loop.run_until_complete. </font>

[nest-asyncio 1.6.0](https://pypi.org/project/nest-asyncio/)

```python
import nest_asyncio
nest_asyncio.apply()

print("\033[94m Successfully enable Colab/Jupyter Notebook to handle nested event loop \033[0m")
```

**Output:**
```
[94m Successfully enable Colab/Jupyter Notebook to handle nested event loop [0m
```

**Example: Making Coffee and Pastry**
------------------------------------

Let's create an example that demonstrates the synchronous and asynchronous approaches:

<font color=gold>In this example just focus on out put to get the feel how **`synchronous`** and **`asynchronous`** function work.</font>

```python
import asyncio
import time
import threading
from rich import print

# Synchronous approach
def make_coffee_sync():
    print(f"\tMaking coffee... : Thread Name: {threading.current_thread().name}")
    time.sleep(2)  # Simulate coffee preparation time
    print("\tCoffee is ready!")

def make_pastry_sync():
    print(f"\tMaking pastry... : Thread Name: {threading.current_thread().name}")
    time.sleep(3)  # Simulate pastry preparation time
    print("\tPastry is ready!")

def order_sync():
    make_coffee_sync()
    make_pastry_sync()

# Asynchronous approach using Asyncio
async def make_coffee_async():
    print(f"\tMaking coffee... : Thread Name: {threading.current_thread().name}")
    await asyncio.sleep(2)  # Simulate coffee preparation time
    print("\tCoffee is ready!")

async def make_pastry_async():
    print(f"\tMaking pastry... : Thread Name: {threading.current_thread().name}")
    await asyncio.sleep(3)  # Simulate pastry preparation time
    print("\tPastry is ready!")

async def order_async():
    tasks = [
        asyncio.create_task(make_coffee_async()),
        asyncio.create_task(make_pastry_async())
    ]
    await asyncio.gather(*tasks)

# Run the synchronous example
print("[red]Synchronous approach: [/red]")
start_time = time.time()

print("Main thread entring order_sync()")
order_sync()
print("Main thread exiting order_sync()")

print( f"[magenta]Total time: {time.time() - start_time} seconds[/magenta]")

# Run the asynchronous example
print("\n\n[red]Asynchronous approach: [/red]")

start_time = time.time()



print("Main thread entring order_async()")
asyncio.run(order_async())
print("Main thread exiting order_async()")

print(f"[magenta]Total time: {time.time() - start_time} seconds[/magenta]")
```

In the synchronous example, the `make_coffee_sync` and `make_pastry_sync` functions are called sequentially, resulting in a total execution time of `5 seconds`.

In the asynchronous example, the `make_coffee_async` and `make_pastry_async` coroutines are run concurrently using `asyncio.create_task` and `asyncio.gather`. This reduces the total execution time to approximately `3 seconds`, as the coffee and pastry are prepared simultaneously.

**Best Practices**
------------------

*   **Use `asyncio.run()`**: Run your asynchronous code using `asyncio.run()` to ensure proper event loop setup and teardown.
*   **Await Coroutines**: Use the `await` keyword to wait for the completion of coroutines.
*   **Use `asyncio.gather()`**: Run multiple coroutines concurrently using `asyncio.gather()`.

**Common Asyncio Functions**
---------------------------

*   `asyncio.sleep()`: Suspends the execution of the current coroutine for a specified amount of time.
*   `asyncio.create_task()`: Creates a new task from a coroutine, allowing it to run concurrently.
*   `asyncio.gather()`: Runs multiple coroutines concurrently and returns their results as a list.

By following these guidelines and using Asyncio effectively, you can write efficient and responsive asynchronous code in Python.

## **Understanding `asyncio` and `await`**

`asyncio` provides the event loop and tools to manage async operations, while `await` is the keyword that allows functions to yield control at specific points, enabling non-blocking waits. Using them together allows writing efficient `single-threaded concurrent code`, especially for I/O-bound tasks.

To address the question of understanding `asyncio` and `await` in Python, let's break down the concepts and their usage:

### Understanding `asyncio` and `await`

1. **`Asyncio`**:

   - **`Definition`**: Asyncio is a Python library that facilitates writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets, and other resources. It's ideal for handling I/O-bound tasks, such as network requests or database queries.

   - **`Key Components`**:
     - **`Event Loop`**: Manages the scheduling and switching between tasks.

     - **`Coroutines`**: Functions defined with `async def` that can suspend and resume execution.
     - **`Tasks`**: Used to run coroutines concurrently.
     - **`Futures`**: Represent the result of a task that may not have completed yet.(we will discuss `futures` later on)

2. **`Await`**:

   - **`Definition`**: `await` is a keyword used within async functions to suspend the execution of the coroutine until the awaited task is complete. It allows the event loop to handle other tasks while waiting.

   - **`Usage`**: It is used to wait for coroutines, tasks, or futures, enabling non-blocking operations.

### Difference Between `asyncio` and `await`

- **`Asyncio`**: The library provides the framework for asynchronous operations, including the event loop and tools for creating and managing tasks.
- **`Await`**: The keyword used within async functions to create points where execution can yield control back to the event loop, allowing other tasks to run.

### Using Them Together

1. **Basic Structure**:
   - Define an async function using `async def`.
   - Use `await` within the function to wait for coroutines.
   - Run the top-level async function with `asyncio.run()`.
   

2. **Example**:

```python
import asyncio

async def my_function():
  await asyncio.sleep(4)
  print("Hello! from my_function()")

async def main():
  await my_function()

asyncio.run(main())
```


## **Awaitable**

This function checks if an object is `awaitable`, meaning it supports `await`.

```python
import inspect

print("isawaitable = ", inspect.isawaitable(my_function()))
```

**Output:**
```
<ipython-input-32-cc8b88d46875>:3: RuntimeWarning: coroutine 'my_function' was never awaited
  print("isawaitable = ", inspect.isawaitable(my_function()))
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
```

## **Custom Awaitables (Implementing `__await__()`)**

-   Any class can be made **awaitable** by defining `__await__()`.
    

### **Example**

```python
class CustomAwaitable:
    def __await__(self):
        yield from asyncio.sleep(2).__await__()  # Delegate to asyncio
        return "Custom Awaitable Done"

async def main():
    result = await CustomAwaitable()
    print(result)

asyncio.run(main())
```

```python
import asyncio

async def task1():
       await asyncio.sleep(4)
       print("\tTask 1 done")

async def task2():
       await asyncio.sleep(1)
       print("\tTask 2 done")

async def main():
       t1 = asyncio.create_task(task1())
       t2 = asyncio.create_task(task2())
       print("Start main()...")
       await asyncio.gather(t1, t2)
       print("End main()...")

asyncio.run(main())
```

### Implications

- **`Efficiency`**: Ideal for I/O-bound tasks, allowing efficient handling of multiple operations without blocking.

- **`Single-Threaded`**: Not suitable for CPU-bound tasks, which may require multiprocessing.
- **`Correct Usage`**: Ensure all coroutines are awaited properly to avoid returning coroutine objects instead of results.

### Conclusion

`asyncio` and `await` work together to enable asynchronous programming in Python, allowing for efficient handling of concurrent operations, particularly in I/O-bound scenarios. Understanding their roles and correct usage is key to writing effective async code.



---


# **Futures**



---



In Python's `asyncio` library, **Futures** are a fundamental concept that represents the result of an asynchronous operation that may not have completed yet. Futures are closely related to coroutines and tasks, but they serve a specific purpose in handling asynchronous operations.

### **What Are Futures**?

A **Future** is an object that represents the result of a task that is not yet complete. It acts as a placeholder for the result, which will be available at some point in the future. Once the task completes, the Future is resolved, and its result (or exception, if the task failed) can be retrieved.

### **Key Characteristics of Futures**

1. **`Asynchronous Result`**:
   - A Future is created when an asynchronous operation is initiated, but the result of that operation is not immediately available.
   - The Future keeps track of the result and notifies any waiting code once the result is available.

2. **`States of a Future`**:
   - **`Pending`**: The initial state where the operation has not yet started or is still in progress.
   - **`Done`**: The operation has completed, and the result is available.
   - **`Cancelled`**: The operation was cancelled before it could complete.

3. **`Awaitable`**:
   - Futures are awaitable objects, meaning they can be used with the `await` keyword in async functions.

4. **`One-Time Use`**:
   - A Future can only be resolved once. Once it is done, it cannot be reset or reused.

### **Relationship Between Futures, Coroutines, and Tasks**

- **`Coroutines`**: Defined using `async def`, coroutines are functions that can be paused and resumed. They are not directly executable and must be scheduled as tasks.
  
- **`Tasks`**: A Task wraps a coroutine and is responsible for running it. When you create a Task, it automatically schedules the coroutine to run on the event loop. A Task returns a Future that represents the result of the coroutine.

- **`Futures`**: A Future is the result of a Task. When you await a Task, you are effectively awaiting its Future.

### **Example of Using Futures**

Here’s an example that demonstrates how Futures work:

```python
import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    print("\tTask done...")
    return "My Coroutine completed"

async def main():
    # Create a Task (which returns a Future)
    print("Starting Coroutine...")
    future = asyncio.create_task(my_coroutine())

    print("Going to Maldives on a 2 day vacation")
    await asyncio.sleep(10)
    print("Come back from vacation")


    # Await the Future
    result = await future
    print("future = ",result)

asyncio.run(main())
#await asyncio.create_task(main())
```

### **States of a `Future` in Python (`asyncio.Future`)**

A `Future` represents a **placeholder for a result** that is **not yet available** in asynchronous programming. It can be in the following states:

1️⃣ **`Pending`** – The initial state when the operation **has not started** or is **still in progress**.  
2️⃣ **`Done`** – The operation has **completed successfully**, and the result is available.  
3️⃣ **`Cancelled`** – The operation was **cancelled before completion**.

----------

### **Example: Understanding Future States in `asyncio`**

```python
import asyncio

async def example_future():
    future = asyncio.Future()  # Create a Future object
    print(f"Initial state: {future.done()}")  # False (Pending)

    # Simulate computation
    await asyncio.sleep(2)

    future.set_result("Task Completed")  # Mark future as done
    print(f"Final state: {future.done()}")  # True (Done)
    print(f"Result: {future.result()}")  # "Task Completed"

asyncio.run(example_future()) # Error, will see it indepth in next topic

#await example_future() # Directly await the coroutine instead of calling asyncio.run
```

**Output:**
```
Initial state: False
Final state: True
Result: Task Completed
```

✅ **Initially in `Pending` state**, then **transitions to `Done`** once the result is set.

### **Cancelling a Future**

A `Future` can be **cancelled** before completion

```python
import asyncio

async def example_cancellation():
    future = asyncio.Future()

    future.cancel()  # Cancelling the future
    print(f"Cancelled: {future.cancelled()}")  # True

asyncio.run(example_cancellation())
#await example_cancellation() # Directly await the coroutine instead of calling asyncio.run
```

**Output:**
```
Cancelled: True
```

```python
# prompt: examples of future methods

async def example_future():
    future = asyncio.Future()  # Create a Future object
    print(f"Initial state: {future.done()}")  # False (Pending)

    # Simulate computation
    await asyncio.sleep(2)

    future.set_result("Task Completed")  # Mark future as done
    print(f"Final state: {future.done()}")  # True (Done)
    print(f"Result: {future.result()}")  # "Task Completed"

asyncio.run(example_future()) # Error, will see it indepth in next topic

#await example_future() # Directly await the coroutine instead of calling asyncio.run
```

**Output:**
```
Initial state: False
Final state: True
Result: Task Completed
```



---


# What is an Event Loop?

An **event loop** is a core concept in asynchronous programming. It is a programming construct that waits for and dispatches events or messages in a program. The event loop is responsible for managing and executing asynchronous tasks, handling I/O operations, and coordinating the execution of coroutines (asynchronous functions).

In simpler terms, the event loop is the "engine" that drives asynchronous execution. It continuously checks for tasks that are ready to run, executes them, and waits for new tasks to be added.

```python
loop = asyncio.get_event_loop()
task = loop.create_task(example_future())
task
```

**Output:**
```
<Task pending name='Task-5' coro=<example_future() running at <ipython-input-8-8cc165c26d0d>:3>>
```

```python
task
```

**Output:**
```
<Task finished name='Task-5' coro=<example_future() done, defined at <ipython-input-8-8cc165c26d0d>:3> result=None>
```

### How Does an Event Loop Work?

1.  **Task Queue**: The event loop maintains a queue of tasks (coroutines, callbacks, etc.) that need to be executed.
2.  **Event Handling**: It listens for events (e.g., I/O operations, timers, or external signals) and schedules the corresponding tasks to run.
3.  **Execution**: When a task is ready to run (e.g., an I/O operation completes or a timer expires), the event loop executes it.
4.  **Non-blocking**: While one task is waiting (e.g., for I/O), the event loop can switch to other tasks, ensuring that the program remains responsive.

