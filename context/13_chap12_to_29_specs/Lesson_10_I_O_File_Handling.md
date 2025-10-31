# Lesson 10 I O File Handling

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>

#File Handling in Python: A Comprehensive Tutorial with Examples

File handling is essential for reading and writing data to files, enabling persistent storage. Python provides built-in functions and methods to handle files efficiently. This tutorial covers the fundamentals with examples.

---------


1. Opening a File
  
  Use the open() function to open a file. Specify the mode (read, write, append, etc.).


* Modes:

  * r: Read (default)

  * w: Write (Opens the file for writing. Creates the file if it doesn't exist, or overwrites it if it does.)

  * a: Append (Opens the file for appending. Creates the file if it doesn't exist, or adds to it if it does.)

  * x: Exclusive creation (fails if file exists)

  * b: Binary mode (Used with the other modes (e.g., "rb", "wb") for working with binary files.)

  * +: Update mode (Can be combined with other modes (e.g., "r+", "w+") to allow both reading and writing.)
<br>
------------------
<br>

###OK, Let's create a file in Colab.

<br>

**`w: Write mode`**. Opens the file for writing. Creates the file if it doesn't exist, or overwrites it if it does.

```python
file = open("new_file.txt", "w")
```

###Writing to Files:

To write to a file, open it in write ("w") or append ("a") mode.

write(string): Writes the given string to the file.

```python
file.write("Hello, world!\n")  # \n creates a new line
file.write("This is another line.\n")
file.close()
```

writelines(list): Writes a list of strings to the file.

```python
lines = ["Line 1: Karachi\n", "Line 2: Lahore\n", "Line 3: Peshawar\n"]
file = open("new_file.txt", "a") # run with mode w, and see the result
file.writelines(lines)
file.close()
```

#### Uptill now we have created a file with 'w' & 'a' mode and also write some lines in it.

#### Now let start reading the file what we have created earlier.

Run the below line of code and see the error 😞

Explain why?

```python
file = open("my_file.txt", "r")  # Opens "my_file.txt" in read mode ("r")
```

So lets correct the name of the file 😀

```python
file = open("new_file.txt", "r")  # Opens "my_file.txt" in read mode ("r")
```

```python
content = file.read()
print(content)
```

**Output:**
```
Line 1: Karchi
Line 2: Lahore
Line 3: Peshawar
Line 1: Karchi
Line 2: Lahore
Line 3: Peshawar
Line 1: Karachi
Line 2: Lahore
Line 3: Peshawar

```

```python
line = file.readline()
print(line)
```

####Nothing Printed ☹

###Here you need to know the concept of file pointer

---------

In Python, a `file pointer` (also called a `file cursor` or `file position indicator`) is an internal marker that keeps track of the `current position` in a file where the next read or write operation will occur. When you open a file, the file pointer is initialized to a specific position (`usually 0, the beginning of the file`), and it moves automatically as you read from or write to the file.

<br>

Key Concepts:
1. Starting Position:
  * r (read mode): Pointer starts at 0 (beginning of the file).
  * a (append mode): Pointer starts at the end of the file.
  * w (write mode): The file is truncated (erased), and the pointer starts at 0.

2. How It Moves:
  * When you read/write data, the pointer moves forward by the number of bytes/characters processed.
  * Example: Reading 10 characters moves the pointer 10 positions forward.

3. Manual Control:
  * Use seek(offset) to move the pointer to a specific byte position.
  * Use tell() to check the current pointer position.

###Move pointer back to start.

```python
file.seek(0)
```

**Output:**
```
0
```

###Check the file cursor/pointer position after running seek(0) method.

```python
print("Position after seek(0):", file.tell())
```

**Output:**
```
Position after seek(0): 0
```

```python
line = file.readline()
print(line)
```

**Output:**
```
Line 1: Karchi

```

### readlines(): Reads all lines into a list.

```python
file.seek(0) # First move the pointer to the start

lines = file.readlines()
for line in lines:
    print(line)
```

**Output:**
```
Line 1: Karchi

Line 2: Lahore

Line 3: Peshawar

Line 1: Karchi

Line 2: Lahore

Line 3: Peshawar

Line 1: Karachi

Line 2: Lahore

Line 3: Peshawar

```

```python
file = open("new_file.txt", "r")
for line in file:  # Iterating directly over the file reads line by line
    print(line.strip()) # .strip() removes leading/trailing whitespace
```

**Output:**
```
Line 1: Karchi
Line 2: Lahore
Line 3: Peshawar
Line 1: Karchi
Line 2: Lahore
Line 3: Peshawar
Line 1: Karachi
Line 2: Lahore
Line 3: Peshawar
```

Closing Files:

* It's crucial to close files after you're finished with them.  This releases system resources and ensures that data is properly written to the disk.  The `close()` method is used for this:

```python
file.close()
```

### Additional Tips
- Exclusive Creation (x mode):

### Best Practices:
- Use `with` for automatic cleanup.
- Handle exceptions to avoid crashes.

```python
try:
    with open('unique.txt', 'x') as file:
        file.write('Created exclusively!')
except FileExistsError:
    print("File already exists.")
```

**Output:**
```
File already exists.
```

### The `with` Statement (Context Manager):

- The best practice for file handling is to use the `with` statement.  This ensures that the file is `automatically closed, even if errors occur`.

```python
with open("new_file.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here
```

**Output:**
```
Line 1: Karchi
Line 2: Lahore
Line 3: Peshawar
Line 1: Karchi
Line 2: Lahore
Line 3: Peshawar
Line 1: Karachi
Line 2: Lahore
Line 3: Peshawar

```

The above cell use the `with` statement which close the file after use, let's validate it.

```python
file.tell() # will produce error, file is already closed because of with statement
```

### Example: Copying a file

```python
def copy_file(source_path, destination_path):
    try:
        with open(source_path, "r") as source_file, open(destination_path, "w") as dest_file:
            for line in source_file:
                dest_file.write(line)
        print(f"File '{source_path}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_file("unique.txt", "unique_copy.txt")
```

**Output:**
```
File 'unique.txt' copied to 'unique_copy.txt' successfully.
```

## Full Example: File Operations Demo

```python
# Create and write to a file
with open('demo.txt', 'w') as file:
    file.write('Python File Handling\n')
    file.write('Line 1\nLine 2\n')

# Read and print content
with open('demo.txt', 'r') as file:
    print("Content:")
    print(file.read())

# Append a new line
with open('demo.txt', 'a') as file:
    file.write('Appended line\n')

# Read lines using seek
with open('demo.txt', 'r+') as file:
    file.seek(0)
    print("First line:", file.readline())
```

**Output:**
```
Content:
Python File Handling
Line 1
Line 2

First line: Python File Handling

```

# Conclusion
- Python’s file handling is straightforward with **`open(), read(), write(), and close()`**. Always use the **`with`** statement for safety and leverage exception handling for robustness. Experiment with modes and methods to manage files effectively!

```python
# prompt: generate a comprehensive example of file handling using all the functions

# Create a file and write to it
with open('example.txt', 'w') as f:
  f.write("This is line 1.\n")
  f.write("This is line 2.\n")
  f.writelines(["This is line 3.\n", "This is line 4.\n"])

# Read the file and print its content
with open('example.txt', 'r') as f:
  content = f.read()
  print("--- Full Content ---")
  print(content)

# Read the file line by line and print each line
with open('example.txt', 'r') as f:
  print("--- Line by Line ---")
  for line in f:
    print(line, end='')

# Read a single line
with open('example.txt', 'r') as f:
  print("\n--- Readline ---")
  print(f.readline(), end='')

# Read all lines into a list
with open('example.txt', 'r') as f:
  lines = f.readlines()
  print("\n--- Readlines ---")
  for line in lines:
    print(line, end='')

# Append to the file
with open('example.txt', 'a') as f:
  f.write("This is appended line 1.\n")
  f.write("This is appended line 2.\n")

# Reading with seek and tell
with open('example.txt', 'r') as f:
  print("\n--- Seek and Tell ---")
  print("Current position:", f.tell())
  print("First line:", f.readline(), end="")
  print("Current position:", f.tell())
  f.seek(0)
  print("After seek(0):", f.tell())
  print("First line again:", f.readline(), end="")

# Demonstrating 'x' mode (exclusive creation)
try:
    with open('new_file.txt', 'x') as f:
        f.write("This is a new file created in 'x' mode.")
        print("new_file.txt created successfully!")
except FileExistsError:
    print("File 'new_file.txt' already exists!")

# Copy file example
def copy_file(source, destination):
  try:
    with open(source, 'r') as src, open(destination, 'w') as dest:
      for line in src:
        dest.write(line)
      print(f"'{source}' successfully copied to '{destination}'")
  except FileNotFoundError:
    print(f"Error: File not found '{source}'")
  except Exception as e:
    print(f"Error during copying: {e}")

copy_file("example.txt", "example_copy.txt")
```

**Output:**
```
--- Full Content ---
This is line 1.
This is line 2.
This is line 3.
This is line 4.

--- Line by Line ---
This is line 1.
This is line 2.
This is line 3.
This is line 4.

--- Readline ---
This is line 1.

--- Readlines ---
This is line 1.
This is line 2.
This is line 3.
This is line 4.

--- Seek and Tell ---
Current position: 0
First line: This is line 1.
Current position: 16
After seek(0): 0
First line again: This is line 1.
new_file.txt created successfully!
'example.txt' successfully copied to 'example_copy.txt'
```

