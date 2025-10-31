# Lesson 17 CPython & GIL

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>




---



## **Python or CPython?**

**CPython is the Original Version**: CPython is the most common and original version of Python. When people say "Python," they usually mean CPython. It’s like the official version of the language.

Open cmd type python and then type below code line by line


```python
>>> import platform
>>> print(platform.python_implementation())
CPython
```



---



## **CPython is the main version of the Python programming language.**

```python
import platform
print(platform.python_implementation())
```

**Output:**
```
CPython
```



---



## **what is CPython?**


CPython is the reference implementation of the Python programming language. It is written in C and serves as the most widely used version of Python. Here are some key points about CPython:

1.  **Reference Implementation**:

  CPython is the original and most commonly used implementation of Python. It adheres closely to the specifications of the Python language, making it the standard against which other implementations are compared.

2.  **Interpreted Language**:

  CPython is an interpreted language, meaning that Python code is executed line by line. This allows for interactive programming and rapid prototyping, but it can also lead to slower execution speeds compared to compiled languages.

3.  **Memory Management**:

  CPython uses automatic memory management, which includes a built-in garbage collector for reclaiming memory that is no longer in use. This helps prevent memory leaks and makes it easier for developers to manage resources.

4.  **Extensibility**:

  CPython allows for the integration of C and C++ code, enabling developers to write performance-critical components in these languages and call them from Python. This is particularly useful for computationally intensive tasks.

5.  **Standard Library**:

  CPython comes with a comprehensive standard library that provides modules and functions for a wide range of tasks, from file I/O to web development, data manipulation, and more.

6.  **Cross-Platform**:

  CPython is available on various operating systems, including Windows, macOS, and Linux, making it a versatile choice for developers.

7.  **Community and Ecosystem**:

  Being the most popular implementation, CPython has a large community and a rich ecosystem of third-party libraries and frameworks, such as NumPy, Pandas, Flask, and Django, which enhance its capabilities.

8.  **Versioning**:

  CPython has undergone several major versions, with Python 2.x and Python 3.x being the most notable. Python 3 introduced many improvements and changes, and it is now the recommended version for new projects.

In summary, CPython is the foundational implementation of Python that serves as the backbone for the language's development and usage in various applications. Its design and features have significantly influenced the growth and popularity of Python as a programming language.

<br>


---


While CPython is the most widely used Python implementation, there are other alternatives available, including:

1. **PyPy**:

  PyPy is a just-in-time (JIT) compiler that provides high-performance execution of Python code.

2. **IronPython**:

  IronPython is a Python implementation that runs on the .NET Common Language Runtime (CLR).

3. **Jython**:

  Jython is a Python implementation that runs on the Java Virtual Machine (JVM).

4. **MicroPython**:

  MicroPython is a lightweight Python implementation that is designed for embedded systems and microcontrollers.

## **Cpython vs .pyc**


CPython and .pyc files are related but serve different purposes in the Python execution process. Here's how they compare:

1. CPython
    - CPython is the reference implementation of Python, written in C.
    - It compiles Python source code (.py files) into bytecode and then executes it.
    
    - It includes a bytecode interpreter, memory management, and standard libraries.
    - CPython is responsible for running Python code efficiently on different platforms.

2. .pyc Files
    - .pyc (Python Compiled) files are the compiled bytecode versions of Python scripts.

    - When you run a Python script using CPython, it first compiles the .py file into bytecode and stores it as a .pyc file in the __pycache__ directory.
    - These files help speed up execution by avoiding recompilation when the script runs again.
    - They are platform-independent but can only be executed by a Python interpreter.

## **Key Differences**


| Feature    | CPython                 | .pyc File                   |   |
|------------|-------------------------|-----------------------------|---|
| Type       | Interpreter & Compiler  | Compiled Bytecode           |   |
| Role       | Runs Python code        | Stores precompiled bytecode |   |
| Written in | C                       | Binary (bytecode)           |   |
| Execution  | Interprets and executes | Needs CPython to run        |   |
| Location   | Installed system-wide   | Stored in __pycache__       |   |



---


## **What is Global Interpreter Lock (GIL)**

The Global Interpreter Lock (GIL) is a mechanism used in CPython, the reference implementation of Python, to ensure that only one thread executes Python bytecode at a time. This design choice has several implications for multi-threaded programming in Python. Here are the key points about the GIL:

### **Key Points about the GIL:**
1.  **Single Thread Execution**:

  The GIL allows only one thread to execute Python bytecode at a time, even on multi-core processors. This means that multi-threaded Python programs may not achieve true parallelism in CPU-bound tasks.

2.  **Thread Safety**:

  The GIL simplifies memory management and makes the CPython interpreter thread-safe. It prevents race conditions and other concurrency issues that can arise when multiple threads access shared data.

3.  **Impact on Performance**:

  * **CPU-bound Programs**: For CPU-bound tasks (tasks that require significant CPU processing), the GIL can be a bottleneck. In such cases, using multiple threads may not lead to performance improvements, as only one thread can execute at a time.

  * **I/O-bound Programs**: For I/O-bound tasks (tasks that spend time waiting for input/output operations, such as network requests or file reading), the GIL is less of an issue. In these cases, threads can release the GIL while waiting for I/O operations to complete, allowing other threads to run.

4.  **Alternatives for Parallelism**: To achieve true parallelism in CPU-bound tasks, Python developers often use:

  * **Multiprocessing**: The multiprocessing module allows the creation of separate processes, each with its own Python interpreter and memory space. This bypasses the GIL and allows for parallel execution on multiple CPU cores.
  * **C Extensions**: Writing performance-critical code in C or using libraries that release the GIL during execution can also help mitigate its impact.

5.  **Other Implementations**: It's worth noting that not all Python implementations have a GIL. For example, Jython (Python on the Java platform) and IronPython (Python on the .NET framework) do not have a GIL and can achieve true multi-threading.

6.  **Controversy and Discussion**: The GIL has been a topic of debate within the Python community. Some argue that it simplifies the implementation and usage of Python, while others believe it limits the language's performance in multi-threaded applications. Various proposals have been made to remove or mitigate the GIL, but none have been adopted in CPython as of now.

**Conclusion**

In summary, the Global Interpreter Lock (GIL) is a key feature of CPython that affects how multi-threading works in Python. While it simplifies certain aspects of thread safety, it can also limit the performance of CPU-bound applications. Developers often need to consider alternative approaches, such as multiprocessing or using C extensions, to achieve better performance in multi-threaded scenarios.

Below is a simple example that demonstrates the impact of the Global Interpreter Lock (GIL) in Python using the threading module. This example compares the performance of a CPU-bound task executed using threads versus using the multiprocessing module.



---


## **Example: Comparing Threading and Multiprocessing**

In this example, we will create a CPU-bound function that performs a large number of calculations. We will then run this function using both threading and multiprocessing to observe the difference in execution time.

```python
import threading
import multiprocessing
import time

# A CPU-bound function that performs a large number of calculations
def cpu_bound_task(n):
    total = 0
    for i in range(n):
        total += (i ** 2) ** 0.5  # Some arbitrary computation
    return total

# Function to run the task using threading
def run_with_threads(n, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=cpu_bound_task, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Function to run the task using multiprocessing
def run_with_multiprocessing(n, num_processes):
    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=cpu_bound_task, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    n = 15**6  # Number of calculations
    num_threads = 4
    num_processes = 4

    # Measure time for threading
    start_time = time.time()
    run_with_threads(n, num_threads)
    threading_time = time.time() - start_time
    print(f"Time taken with threading: {threading_time:.2f} seconds")

    # Measure time for multiprocessing
    start_time = time.time()
    run_with_multiprocessing(n, num_processes)
    multiprocessing_time = time.time() - start_time
    print(f"Time taken with multiprocessing: {multiprocessing_time:.2f} seconds")

    # If output is verbose, restart session. On top menu bar click on Runtime --> click on Restart Session
```

**Output:**
```
Time taken with threading: 11.39 seconds
Time taken with multiprocessing: 9.62 seconds
```

**Explanation**:

1.  **CPU-bound Task**:

  The `cpu_bound_task` function performs a large number of calculations. This is a CPU-bound task, meaning it requires significant CPU processing.

2.  **Threading**:

  The `run_with_threads` function creates multiple threads to execute the cpu_bound_task. Each thread runs the task independently, but due to the GIL, only one thread can execute Python bytecode at a time.

3.  **Multiprocessing**:

  The `run_with_multiprocessing` function creates multiple processes to execute the same task. Each process has its own Python interpreter and memory space, allowing them to run in parallel without being affected by the GIL.

4.  **Timing**:

  The script measures the time taken to complete the tasks using both threading and multiprocessing.

**Expected Output**:

When you run this script, you will likely observe that the time taken with multiprocessing is significantly lower than the time taken with threading, especially for CPU-bound tasks. This demonstrates the impact of the GIL on multi-threaded performance in Python.

**`Note`**:

Keep in mind that the actual execution time may vary based on your machine's specifications and current load. Additionally, for I/O-bound tasks, the performance difference may not be as pronounced.

## **Summary**

- You cannot directly "open" or "unlock" the GIL in CPython, as it is a fundamental part of how CPython manages thread safety.

- For CPU-bound tasks, use the multiprocessing module to achieve true parallelism.
- For I/O-bound tasks, consider using asyncio to handle concurrency without being blocked by the GIL.
- If you are writing C extensions, you can release the GIL while executing C code to allow other threads to run Python code concurrently.

## **What is CPU-bound Task?**

A CPU-bound task is a type of task that requires significant processing power from the Central Processing Unit (CPU) to complete. These tasks are typically computationally intensive and spend most of their time executing instructions on the CPU.


## **Characteristics of CPU-Bound Tasks**

- **High CPU Utilization**: CPU-bound tasks utilize a large percentage of the CPU's processing power, often leaving little room for other tasks to run concurrently.

- **Computationally Intensive**: These tasks involve complex calculations, data processing, or algorithmic operations that require significant CPU resources.

- **Low I/O Operations**: CPU-bound tasks typically involve minimal input/output (I/O) operations, such as reading or writing to files, networks, or databases.

- **Sequential Execution**: CPU-bound tasks often require sequential execution, meaning that each instruction must be completed before the next one can begin.

## **Examples of CPU-Bound Tasks**

- **Scientific Simulations**: Tasks like weather forecasting, fluid dynamics, or molecular dynamics simulations are CPU-bound, as they require complex calculations and data processing.

- **Data Compression**: Compressing large datasets using algorithms like gzip or lzma is a CPU-bound task, as it involves complex calculations and data transformation.

- **Cryptography**: Tasks like encryption, decryption, or hashing are CPU-bound, as they require complex mathematical operations and data processing.

- **Machine Learning**: Training machine learning models, especially those involving deep learning, can be CPU-bound, as they require complex calculations and data processing.

- **Video Encoding**: Encoding video files using codecs like H.264 or H.265 is a CPU-bound task, as it involves complex calculations and data transformation.

## **Impact of CPU-Bound Tasks on Concurrency**

- **Limited Concurrency**: CPU-bound tasks can limit concurrency, as they utilize a large percentage of the CPU's processing power, leaving little room for other tasks to run concurrently.

- **GIL Limitations**: In Python, the Global Interpreter Lock (GIL) can limit concurrency for CPU-bound tasks, as it prevents multiple threads from executing Python bytecode simultaneously.

- **Multiprocessing**: To achieve concurrency for CPU-bound tasks, you can use multiprocessing, which creates separate processes that can run concurrently on multiple CPU cores.


## **Summary**

CPU-bound tasks are computationally intensive tasks that require significant processing power from the CPU. They are characterized by high CPU utilization, low I/O operations, and sequential execution. Examples of CPU-bound tasks include scientific simulations, data compression, cryptography, machine learning, and video encoding. Understanding CPU-bound tasks is essential for optimizing concurrency and parallelism in your applications.

