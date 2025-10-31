# Lesson 06 Lists, Tuples & Dictionary

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>

# **Working with Lists and Tuples**

## **Introduction**

Python provides powerful sequence types: `lists and tuples`. These data structures help store and manage collections of data efficiently.

## **1. Lists in Python**

1. **Ordered**: Lists are `ordered`, meaning that the items in the list have a specific order and can be accessed by their index.
2. **Mutable**: Lists are `mutable`, meaning that they can be modified after they are created.
3. **Indexed**: Lists are `indexed`, meaning that each item in the list has a specific index that can be used to access it.
4. **Dynamic size**: Lists can `grow or shrink` dynamically as elements are added or removed.
5. **Heterogeneous**: Lists can contain elements of `different data types`, such as integers, strings, floats, and other lists.
6. **Supports duplicate values**: Lists can contain `duplicate values`.

<br>


Creating a List

```python
# Creating lists with different data types
fruits: list  = ["apple", "banana", "cherry"]
numbers: list = [10, 20, 30, 40]
mixed: list   = ["hello", 42, 3.14, True]

print("fruits  = ", fruits)
print("numbers = ", numbers)
print("mixed   = ", mixed)
```

**Output:**
```
fruits  =  ['apple', 'banana', 'cherry']
numbers =  [10, 20, 30, 40]
mixed   =  ['hello', 42, 3.14, True]
```

## **Accessing List Elements**

You can access elements using indexing (**starting from 0**) and negative indexing (**starting from -1**).

```python
fruits: list = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: apple
print(fruits[-3])  # Output: apple, accessing element in reverse order
```

**Output:**
```
apple
apple
```

## **Modifying Lists**

Lists are mutable, meaning their elements can be changed.

```python
fruits: list = ["apple", "banana", "cherry"]
fruits[-3] = "watermelon" # replacing "apple" with "watermelon"
print(fruits)  # Output: ['watermelon', 'banana', 'cherry']
```

**Output:**
```
['watermelon', 'banana', 'cherry']
```

## **List Slicing**

Extract multiple elements using slicing.

```python
print(fruits[0:2])  # Output: ['watermelon', 'banana'] 0 and 1
```

**Output:**
```
['watermelon', 'banana']
```

## **2. Common List Methods**

Lists provide built-in methods for efficient data manipulation.

Appending and Extending Lists

```python
fruits.append("mango")  # Adds a single element 'mango' to the end
print(fruits)  # Output: ['watermelon', 'banana', 'cherry', 'mango']
```

**Output:**
```
['watermelon', 'banana', 'cherry', 'mango']
```

```python
fruits.extend(["grape", "kiwi"])  # Adds multiple elements
print(fruits)  # Output: ['watermelon', 'banana', 'cherry', 'mango', 'grape', 'kiwi']
```

**Output:**
```
['watermelon', 'banana', 'cherry', 'mango', 'grape', 'kiwi']
```

## **Removing Elements**

In Python, `remove()` and `pop()` are two distinct methods used to manipulate lists. While they may seem similar, they have different purposes and behaviors.

**Remove() Method**

The `remove()` method is used to delete the first occurrence of a specified value from a list. If the value is not found in the list, a `ValueError` exception is raised.

**Key aspects of remove():**

1. **Value-based**: `remove()` searches for a specific value in the list.

2. **Returns None**: The `remove()` method does not return any value.
3. **Raises ValueError**: If the value is not found in the list, a `ValueError` exception is raised.

```python
fruits.remove("banana")  # Removes 'banana' # run multiple times to see error as "banana" is already removed
print(fruits)
```

**Output:**
```
['watermelon', 'cherry', 'mango', 'grape', 'kiwi']
```

## **Pop() Method**

The `pop()` method is used to delete an item at a specified index from a list. If no index is provided, it removes and returns the last item in the list.

**Key aspects of pop():**

1. **Index-based**: `pop()` searches for an item at a specific index in the list.

2. **Returns the removed item**: The `pop()` method returns the item that was removed from the list.
3. **Raises IndexError**: If the index is out of range, an `IndexError` exception is raised.

```python
deleted = fruits.pop(1)  # Removes and returns the element at index 1 # run it multiple time to see error
print("deleted element = ", deleted)  # Output: 'cherry'
print(fruits) # Output: ['watermelon', 'mango', 'grape', 'kiwi']
```

**Output:**
```
deleted element =  cherry
['watermelon', 'mango', 'grape', 'kiwi']
```

## **Sorting a List**

## **1. Default Sorting (Ascending Order)**

```python
numbers: list[int] = [3, 1, 4, 1, 5, 9] # unsorted list
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]
```

**Output:**
```
[1, 1, 3, 4, 5, 9]
```

## **2. Sorting in Descending Order (reverse=True)**

*(Contributor: Amna Aftab Kifayat from Karachi)*

```python
numbers = [4, 2, 9, 1]
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 4, 2, 1]
```

**Output:**
```
[9, 4, 2, 1]
```

## **3. Sorting by String Length (key=len)**

```python
words = ["apple", "kiwi", "banana"]
words.sort(key=len)
print(words)  # Output: ['kiwi', 'apple', 'banana']
```

**Output:**
```
['kiwi', 'apple', 'banana']
```

## **4. Sorting by Last Character (key=lambda word: word[-1])**

```python
words = ["apple", "kiwi", "banana"]
words.sort(key=lambda word: word[-1])
print(words)  # Output: ['banana', 'apple', 'kiwi']  # Sorted by last letter
```

**Output:**
```
['banana', 'apple', 'kiwi']
```

## **5. Reverse Sorting**

```python
numbers = [1, 2, 5, 7, 10]
numbers.reverse()
print(numbers)  # Output: [10, 7, 5, 2, 1]
```

**Output:**
```
[10, 7, 5, 2, 1]
```

## **3. Iterating Over Lists**

Use loops to process elements in a list.


**Using a for-loop**

```python
for fruit in fruits:
    print(fruit)
```

**Output:**
```
watermelon
mango
grape
kiwi
```

## **Custome Iterator: Agentic AI - Python - Lesson 13 - OOP: Objects & Classes - Part 2**

[How to Make a Custom Class Iterable](https://colab.research.google.com/drive/13i4LN9HrdFbp_GK-IEoKU8OCZh6F4Ilp?usp=sharing#scrollTo=AJrmBy8pgzSO)

# **Using list comprehension**

List comprehension is a powerful feature in Python that allows you to create new lists in a `concise` and `readable way`. It's a `compact way` to create lists from existing lists or other iterables by applying a transformation or filter to each element.

```python
new_list = [expression for element in iterable if condition]
```

* `expression` is the operation you want to perform on each element.
* `element` is the variable that takes on the value of each element in the `iterable`.
* `iterable` is the list or other iterable that you want to process.
* `condition` is an optional filter that determines whether an element is included in the new list.


```python
# Without if condition
squared: list = [x**2 for x in [1, 2, 3, 4, 5] ] #  if x > 3 place this if condition and see
print(squared, " : ", type(squared))  # Output: [1, 4, 9, 16, 25]
```

**Output:**
```
[1, 4, 9, 16, 25]  :  <class 'list'>
```

```python
# With if condition
squared: list = [x**2 for x in [1, 2, 3, 4, 5] if x > 3] #  if x > 3 place this if condition and see
print(squared, " : ", type(squared))  # Output: [1, 4, 9, 16, 25]
```

**Output:**
```
[16, 25]  :  <class 'list'>
```

**List comprehension is commonly used for:**

* **`Transforming data`**: List comprehension can be used to transform data from one format to another.
* **`Filtering data`**: List comprehension can be used to filter out unwanted data.
* **`Creating new data`**: List comprehension can be used to create new data by combining existing data.

[w3schools: List Methods](https://www.w3schools.com/python/python_lists_methods.asp)

# **4. Tuples in Python**

A tuple is an `ordered`, `immutable` (unchangeable) sequence of elements. Tuples are useful for fixed data collections.

In Python, a tuple is an immutable data type. This means that once a tuple is created, its elements cannot be changed, added, or removed.

### **1.  Cannot Modify Elements:**
  * Once a tuple is created, you cannot change its elements.

### **2. Cannot Add or Remove Elements:**
  * You cannot add new elements to a tuple or remove existing ones.



---



## **Why Use Tuples?**

  1.  **Immutable**: Since tuples cannot be changed, they are safer to use when you want to ensure that the data remains constant.

  2.  **Hashable**: Tuples can be used as keys in dictionaries because they are immutable.
  3.  **Performance**: Tuples are generally faster than lists because of their immutability.

## **When to Use Tuples vs Lists**

* Use tuples when you want to store data that should not change (e.g., coordinates, constants).

* Use lists when you need a collection that can be modified (e.g., adding or removing elements).

Creating a Tuple

```python
tuple1: tuple = tuple(["apple", "banana", "cherry"]) # cast a list into tuple
tuple2: tuple = (10, 20, 30) # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True) # tuple

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)
```

**Output:**
```
tuple1      = ('apple', 'banana', 'cherry')
tuple2      = (10, 20, 30)
mixed_tuple = ('hello', 42, 3.14, True)
```

Even though tuples are immutable, Python may create new instances in memory when you define identical tuples in separate assignments. This is why id(tuple_1) and id(tuple_2) may differ.

```python
tuple_1: tuple = (10, 20, 30) # tuple
tuple_2: tuple = (10, 20, 30) # tuple

print("id(tuple_1) = ", id(tuple_1)) # unique memory address
print("id(tuple_2) = ", id(tuple_2)) # unique memory address

print("tuple_1 == tuple_2 = ", tuple_1 == tuple_2) # comparing by value
```

**Output:**
```
id(tuple_1) =  139975700916672
id(tuple_2) =  139975700971648
tuple_1 == tuple_2 =  True
```

**Why are Tuples Immutable?**

There are several reasons why tuples are immutable:

1. **`Memory Efficiency`**: Immutable tuples can be stored in a single block of memory, which makes them more memory-efficient than lists.
2. **`Thread Safety`**: Immutable tuples are thread-safe, meaning that they can be safely accessed and shared between multiple threads without fear of modification.
3. **`Hashability`**: Immutable tuples are hashable, meaning that they can be used as keys in dictionaries.


*lets create an error.*

```python
tuple1[0] = "watermelon" # immutable
```

**Error:**
```
TypeError: 'tuple' object does not support item assignment
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-e330c10a0867> in <cell line: 0>()
----> 1 tuple1[0] = "watermelon" # immutable

TypeError: 'tuple' object does not support item assignment
```

```python
# Tuples in Python

# A tuple is an `ordered`, `immutable` (unchangeable) sequence of elements.
# Tuples are useful for fixed data collections.

# Creating a Tuple
tuple1: tuple      = tuple(["apple", "banana", "cherry"])  # cast a list into tuple
tuple2: tuple      = (10, 20, 30)  # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True)  # tuple

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)

# Accessing elements in a tuple
print("tuple1[0] =", tuple1[0])  # Accessing first element

# Tuple slicing
print("tuple2[1:] =", tuple2[1:])  # Slicing from index 1

# Tuple length
print("Length of tuple1:", len(tuple1))

# Iterating through a tuple
print("Iterating through tuple2:")
for item in tuple2:
  print(item)

# Checking if an item exists in a tuple
print("Is 20 in tuple2?", 20 in tuple2)

# Concatenating tuples
tuple3: tuple = tuple1 + tuple2
print("tuple1 + tuple2 =", tuple3)

# Repeating tuples
tuple4: tuple = tuple2 * 2
print("tuple2 * 2 =", tuple4)

# Nested tuples
nested_tuple = (tuple1, tuple2)
print("nested_tuple =", nested_tuple)

# Unpacking tuples
a, b, c = tuple1
print("Unpacking tuple1:", a, b, c)

# Using tuples as keys in dictionaries (because they are immutable)
my_dict = {tuple1: "This is a tuple key", tuple2: "Another tuple key"}
print("Dictionary with tuple keys:", my_dict)

#Trying to modify a tuple will result in a TypeError
# tuple1[0] = "watermelon" #immutable. This line will raise an error. Uncomment to test.
```

**Output:**
```
tuple1      = ('apple', 'banana', 'cherry')
tuple2      = (10, 20, 30)
mixed_tuple = ('hello', 42, 3.14, True)
tuple1[0] = apple
tuple2[1:] = (20, 30)
Length of tuple1: 3
Iterating through tuple2:
10
20
30
Is 20 in tuple2? True
tuple1 + tuple2 = ('apple', 'banana', 'cherry', 10, 20, 30)
tuple2 * 2 = (10, 20, 30, 10, 20, 30)
nested_tuple = (('apple', 'banana', 'cherry'), (10, 20, 30))
Unpacking tuple1: apple banana cherry
Dictionary with tuple keys: {('apple', 'banana', 'cherry'): 'This is a tuple key', (10, 20, 30): 'Another tuple key'}
```

```python
print(tuple1[0])   # Output: apple
print(tuple1[-3])  # Output: apple
print(tuple1.count("apple"))
print(tuple1.index("apple"))

#error
#tuple1.sort()
#tuple1.reverse()
#tuple1.append("mango")
#tuple1.extend(["grape", "kiwi"])
#tuple1.remove("banana")
#deleted = tuple1.pop(1)
```

**Output:**
```
apple
apple
1
0
```

```python
# prompt: print the complete list of methods and attribute of tuple, dont include dunders

# Get a list of all attributes and methods of a tuple
tuple_methods: list = [method for method in dir(tuple) if not method.startswith('__')]

# Print the list of methods (excluding dunder methods)
tuple_methods
```

**Output:**
```
['count', 'index']
```

```python
# prompt: generate a example of ['count', 'index'] in tuple

tuple1: tuple = tuple(["apple", "banana", "cherry"])
print(tuple1.count("apple"))  # Output: 1
print(tuple1.index("apple"))  # Output: 0
example_tuple: tuple = ('count', 'index')
print(example_tuple) # Output: ('count', 'index')
```

**Output:**
```
1
0
('count', 'index')
```

[w3schools: Tuples](https://www.w3schools.com/python/python_tuples.asp)

## **Python is Type Hint Language**

```python
a: int = input ("Enter your name: ")
print(a, type(a) )
```

**Output:**
```
Enter your name: Arif Rozani
Arif Rozani <class 'str'>
```

## **Type Hinting (a: int)**
* a: int is a type hint, which suggests that the variable a is expected to be an integer.
* `However, type hints are not enforced in Python`. They are only for documentation and tools like linters or type checkers.
* The actual value assigned to a will still be a string, because input() always returns a string.

# **Dictionaries in Python**

## **1. Introduction to Dictionaries**

A dictionary is a collection of `key-value pairs`. It is:


- **Ordered (since Python 3.7)**: Items are stored in the order they were inserted.

- **Mutable**: Items can be added, removed, or modified after the dictionary is created.
- **Un-indexed**: Items are accessed using keys, not indices.
- **Without duplicates**: **`Keys must be unique`**, but values can be duplicated.


Before Python 3.7, dictionaries were **unordered**, meaning that items were not stored in a specific order. However, with the introduction of Python 3.7, dictionaries now maintain their insertion order.

[OrderedDict vs dict in Python: The Right Tool for the Job](https://realpython.com/python-ordereddict/)

## **2. Creating a Dictionary**

Dictionaries are created using curly braces {} with key-value pairs separated by commas.

The syntax is:

``` Python
dictionary = {key1: value1, key2: value2, ...}
```

Example Code:

```python
# prompt: genrate a List of 5 american cities

american_cities: dict = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
american_cities
```

**Output:**
```
['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
```

```python
# Create a dictionary to store a person's details
person: dict = {
    "name": "Alice",
    "age": 25,
    "visited_cities": american_cities
}
print(person)
```

**Output:**
```
{'name': 'Alice', 'age': 25, 'visited_cities': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
```

```python
thisdict: dict = dict(name = "John", age = 36, country = "Norway") # It is also possible to use the dict() constructor to make a dictionary.
print(type(thisdict)," - ", thisdict, )
```

**Output:**
```
<class 'dict'>  -  {'name': 'John', 'age': 36, 'country': 'Norway'}
```

## **3. Accessing Values**
You can access the value associated with a key using square brackets [] or the get() method.


Example Code:

```python
# Access values using keys
print(person["name"])  # Output: Alice
print(person.get("age", "99"))  # Output: 25, if not found it will return 99 (default value)

# Access a non-existent key
print(person.get("country", "my_default_vlaue_if_key_not_found"))  # Output: my_default_vlaue (default value)
```

**Output:**
```
Alice
25
my_default_vlaue_if_key_not_found
```

## **4. Modifying a Dictionary**


You can add new key-value pairs or modify existing ones.

Example Code:

```python
# Add a new key-value pair
person["email"] = "alice@example.com"
print(person)

# Modify an existing value
person["age"] = 26
print(person)
```

**Output:**
```
{'name': 'Alice', 'age': 25, 'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 'email': 'alice@example.com'}
{'name': 'Alice', 'age': 26, 'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 'email': 'alice@example.com'}
```

## **5. Deleting Items**


You can remove a key-value pair using the del keyword or the pop() method.

Note that `pop()` returns the value of the removed key-value pair, whereas `del` does not return anything.

You can also use `pop()` with a default value, in case the key is not found in the dictionary:

Example Code:

```python
person: dict = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
print(person)
```

**Output:**
```
{'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
```

```python
# Remove a key-value pair using del
del person["city"]
print(person)
```

**Output:**
```
{'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}
```

```python
# Remove a key-value pair using pop
age: int = person.pop("age", -1)
print("Removed age:", age)
print(person)

print("\n-----\n")
#Again remove a key which is already removed to check the default value
age: int = person.pop("age", -1)
print("key 'age' not found in dict so returning default value: ", age)
```

**Output:**
```
Removed age: 25
{'name': 'Alice', 'email': 'alice@example.com'}

-----

key 'age' not found in dict so returning default value:  -1
```

## **6. Dictionary Methods**

Python provides several useful methods for working with dictionaries.


| Method   | Description                                                       |   |
|----------|-------------------------------------------------------------------|---|
| keys()   | Returns a list of all keys in the dictionary.                     |   |
| values() | Returns a list of all values in the dictionary.                   |   |
| items()  | Returns a list of key-value pairs as tuples.                      |   |
| clear()  | Removes all items from the dictionary.                            |   |
| update() | Adds or updates multiple key-value pairs from another dictionary. |   |

```python
# Get all keys
print("person.keys()         = ", person.keys()  )  # Output: dict_keys(['name', 'email', 'city', 'age'])

# Get all values
print("person.values()       = ", person.values())  # Output: dict_values(['Alice', 'alice@example.com', 'Los Angeles', 27])

# Get all key-value pairs
print("person.items()        = ", person.items())  # Output: dict_items([('name', 'Alice'), ('email', 'alice@example.com'), ('city', 'Los Angeles'), ('age', 27)])

# Update the dictionary
person.update({"city": "Los Angeles", "age": 27})
print("After: person.update  = ", person)

# Clear the dictionary
person.clear()
print("After: person.clear() = ", person)  # Output: {}
```

**Output:**
```
person.keys()         =  dict_keys(['name', 'email'])
person.values()       =  dict_values(['Alice', 'alice@example.com'])
person.items()        =  dict_items([('name', 'Alice'), ('email', 'alice@example.com')])
After: person.update  =  {'name': 'Alice', 'email': 'alice@example.com', 'city': 'Los Angeles', 'age': 27}
After: person.clear() =  {}
```

## **Duplicate Key Not Allowed**


Dictionaries cannot have two items with the same key:

```python
thisdict: dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # this will overwrite the previous key:vlaue
}
print(thisdict)
```

**Output:**
```
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

## **7. Iterating Over a Dictionary**

You can loop through a dictionary using for loops.

Example Code:

```python
for key in thisdict:
    print(key)
```

**Output:**
```
brand
model
year
```

```python
for key, value in thisdict.items():
    print(key," : ", value)
```

**Output:**
```
brand  :  Ford
model  :  Mustang
year  :  2020
```

## **8. Practical Examples**

Here are two practical examples to solidify these concepts.

Example 1: Building a Phonebook

```python
# Create a phonebook
phonebook: dict = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

# Add a new contact
phonebook["David"] = "111-222-3333"

# Search for a contact
name: str = input("Enter a name to search: ")
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}.")
else:
    print(f"{name} is not in the phonebook.")
```

**Output:**
```
Enter a name to search: Bob
Bob's phone number is 987-654-3210.
```

Example 2: Counting Word Frequencies in a Text

```python
sentence = """
**Projected Economy Size of AI:**

The projected economy size of AI is significant, with estimates varying depending on the source and methodology. Here are some notable projections:

1. **Global AI Market Size:**
	* By 2025: $190 billion (Source: MarketsandMarkets)
	* By 2030: $1.5 trillion (Source: PwC)
2. **AI-Driven Economic Growth:**
	* By 2025: AI is expected to contribute 10% to global GDP growth (Source: Accenture)
	* By 2030: AI is expected to contribute 14% to global GDP growth (Source: PwC)
3. **AI-Generated Revenue:**
	* By 2025: AI is expected to generate $15.7 trillion in revenue (Source: IDC)
	* By 2030: AI is expected to generate $33.5 trillion in revenue (Source: McKinsey)
4. **Job Market Impact:**
	* By 2025: AI is expected to create 133 million new jobs globally (Source: World Economic Forum)
	* By 2030: AI is expected to automate 30% of current jobs globally (Source: McKinsey)

**Industry-Specific Projections:**

1. **Healthcare:**
	* By 2025: AI is expected to generate $150 billion in revenue (Source: MarketsandMarkets)
2. **Financial Services:**
	* By 2025: AI is expected to generate $100 billion in revenue (Source: Accenture)
3. **Manufacturing:**
	* By 2025: AI is expected to generate $50 billion in revenue (Source: IDC)
4. **Transportation:**
	* By 2025: AI is expected to generate $20 billion in revenue (Source: MarketsandMarkets)

**Regional Projections:**

1. **North America:**
	* By 2025: AI is expected to generate $100 billion in revenue (Source: MarketsandMarkets)
2. **Europe:**
	* By 2025: AI is expected to generate $50 billion in revenue (Source: IDC)
3. **Asia-Pacific:**
	* By 2025: AI is expected to generate $200 billion in revenue (Source: MarketsandMarkets)

Note: These projections are based on various assumptions, including the pace of AI development, adoption rates, and economic trends. The actual economy size of AI may vary depending on several factors.

"""
```

```python
# Count the frequency of words in a sentence

words: list = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
```

**Output:**
```
{'**Projected': 1, 'Economy': 1, 'Size': 1, 'of': 5, 'AI:**': 1, 'The': 2, 'projected': 1, 'economy': 2, 'size': 2, 'AI': 17, 'is': 14, 'significant,': 1, 'with': 1, 'estimates': 1, 'varying': 1, 'depending': 2, 'on': 3, 'the': 2, 'source': 1, 'and': 2, 'methodology.': 1, 'Here': 1, 'are': 2, 'some': 1, 'notable': 1, 'projections:': 1, '1.': 3, '**Global': 1, 'Market': 2, 'Size:**': 1, '*': 15, 'By': 15, '2025:': 11, '$190': 1, 'billion': 8, '(Source:': 15, 'MarketsandMarkets)': 5, '2030:': 4, '$1.5': 1, 'trillion': 3, 'PwC)': 2, '2.': 3, '**AI-Driven': 1, 'Economic': 2, 'Growth:**': 1, 'expected': 13, 'to': 15, 'contribute': 2, '10%': 1, 'global': 2, 'GDP': 2, 'growth': 2, 'Accenture)': 2, '14%': 1, '3.': 3, '**AI-Generated': 1, 'Revenue:**': 1, 'generate': 9, '$15.7': 1, 'in': 9, 'revenue': 9, 'IDC)': 3, '$33.5': 1, 'McKinsey)': 2, '4.': 2, '**Job': 1, 'Impact:**': 1, 'create': 1, '133': 1, 'million': 1, 'new': 1, 'jobs': 2, 'globally': 2, 'World': 1, 'Forum)': 1, 'automate': 1, '30%': 1, 'current': 1, '**Industry-Specific': 1, 'Projections:**': 2, '**Healthcare:**': 1, '$150': 1, '**Financial': 1, 'Services:**': 1, '$100': 2, '**Manufacturing:**': 1, '$50': 2, '**Transportation:**': 1, '$20': 1, '**Regional': 1, '**North': 1, 'America:**': 1, '**Europe:**': 1, '**Asia-Pacific:**': 1, '$200': 1, 'Note:': 1, 'These': 1, 'projections': 1, 'based': 1, 'various': 1, 'assumptions,': 1, 'including': 1, 'pace': 1, 'development,': 1, 'adoption': 1, 'rates,': 1, 'economic': 1, 'trends.': 1, 'actual': 1, 'may': 1, 'vary': 1, 'several': 1, 'factors.': 1}
```

AI generated code:

```python
# prompt: sort the word count variable according to its value in descending order

# Sort the word_count dictionary by value in descending order
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

sorted_word_count
```

**Output:**
```
{'AI': 17,
 '*': 15,
 'By': 15,
 '(Source:': 15,
 'to': 15,
 'is': 14,
 'expected': 13,
 '2025:': 11,
 'generate': 9,
 'in': 9,
 'revenue': 9,
 'billion': 8,
 'of': 5,
 'MarketsandMarkets)': 5,
 '2030:': 4,
 'on': 3,
 '1.': 3,
 'trillion': 3,
 '2.': 3,
 '3.': 3,
 'IDC)': 3,
 'The': 2,
 'economy': 2,
 'size': 2,
 'depending': 2,
 'the': 2,
 'and': 2,
 'are': 2,
 'Market': 2,
 'PwC)': 2,
 'Economic': 2,
 'contribute': 2,
 'global': 2,
 'GDP': 2,
 'growth': 2,
 'Accenture)': 2,
 'McKinsey)': 2,
 '4.': 2,
 'jobs': 2,
 'globally': 2,
 'Projections:**': 2,
 '$100': 2,
 '$50': 2,
 '**Projected': 1,
 'Economy': 1,
 'Size': 1,
 'AI:**': 1,
 'projected': 1,
 'significant,': 1,
 'with': 1,
 'estimates': 1,
 'varying': 1,
 'source': 1,
 'methodology.': 1,
 'Here': 1,
 'some': 1,
 'notable': 1,
 'projections:': 1,
 '**Global': 1,
 'Size:**': 1,
 '$190': 1,
 '$1.5': 1,
 '**AI-Driven': 1,
 'Growth:**': 1,
 '10%': 1,
 '14%': 1,
 '**AI-Generated': 1,
 'Revenue:**': 1,
 '$15.7': 1,
 '$33.5': 1,
 '**Job': 1,
 'Impact:**': 1,
 'create': 1,
 '133': 1,
 'million': 1,
 'new': 1,
 'World': 1,
 'Forum)': 1,
 'automate': 1,
 '30%': 1,
 'current': 1,
 '**Industry-Specific': 1,
 '**Healthcare:**': 1,
 '$150': 1,
 '**Financial': 1,
 'Services:**': 1,
 '**Manufacturing:**': 1,
 '**Transportation:**': 1,
 '$20': 1,
 '**Regional': 1,
 '**North': 1,
 'America:**': 1,
 '**Europe:**': 1,
 '**Asia-Pacific:**': 1,
 '$200': 1,
 'Note:': 1,
 'These': 1,
 'projections': 1,
 'based': 1,
 'various': 1,
 'assumptions,': 1,
 'including': 1,
 'pace': 1,
 'development,': 1,
 'adoption': 1,
 'rates,': 1,
 'economic': 1,
 'trends.': 1,
 'actual': 1,
 'may': 1,
 'vary': 1,
 'several': 1,
 'factors.': 1}
```

## **9. Common Pitfalls**

* Using a non-existent key without checking first for e.g. "
``` python
print(my_dict.get("name_1")) # Output: None
print(my_dict.get("name_1", "No name found")) # Output: No name found
print(my_dict["name_1"])  # (raises a KeyError).
```

* Always use get() or check if the key exists with in to avoid error.
* Forgetting that dictionary keys must be immutable (e.g., strings, numbers, or tuples).
* Assuming dictionaries are ordered (in Python 3.6+, they retain insertion order, but this is not guaranteed in older versions).

```python
# prompt: generate a working example of all dictionary function

# Example Dictionary
my_dict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# 1. Accessing Items
print("1. Accessing Items")
print("Name:", my_dict["name"])  # Accessing by key
print("Age:", my_dict.get("age"))  # Accessing using get()
print("City (using get):", my_dict.get("city"))

# 2. Adding Items
print("\n2. Adding Items")
my_dict["email"] = "john@example.com"
print("Dictionary after adding email:", my_dict)

# 3. Modifying Items
print("\n3. Modifying Items")
my_dict["age"] = 31
print("Dictionary after modifying age:", my_dict)

# 4. Removing Items
print("\n4. Removing Items")
my_dict.pop("city")
print("Dictionary after removing city (using pop):", my_dict)
del my_dict["email"]
print("Dictionary after removing email (using del):", my_dict)

# 5. Dictionary Methods
print("\n5. Dictionary Methods")
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# 6. Clearing the Dictionary
print("\n6. Clearing the Dictionary")
my_dict.clear()
print("Dictionary after clearing:", my_dict)

# Adding items back for further examples
my_dict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# 7. Updating the Dictionary
print("\n7. Updating the Dictionary")
my_dict.update({"age": 32, "country": "USA"})
print("Dictionary after updating:", my_dict)

# 8. Iterating Through a Dictionary
print("\n8. Iterating Through a Dictionary")
print("Iterating through keys:")
for key in my_dict:
  print(key)

print("\nIterating through values:")
for value in my_dict.values():
  print(value)

print("\nIterating through items (key-value pairs):")
for key, value in my_dict.items():
  print(f"{key}: {value}")

#9 checking if a key exist
print("\n9. checking if a key exist")
if "name" in my_dict:
    print("Name exist")
else:
    print("Name do not exist")

# 10. Dictionary Length
print("\n10. Dictionary Length")
print("Length of the dictionary:", len(my_dict))

# 11. Creating a dictionary from iterable
print("\n11. Creating a dictionary from iterable")
iterable = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
new_dict = dict(iterable)
print("new dictionary:", new_dict)

# 12. Copying a dictionary
print("\n12. Copying a dictionary")
copied_dict = my_dict.copy()
print("Copied dictionary:", copied_dict)

# 13. Nested Dictionaries
print("\n13. Nested Dictionaries")
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print("Nested dictionary:", nested_dict)
print("Alice's age:", nested_dict["person1"]["age"])
```

**Output:**
```
1. Accessing Items
Name: John
Age: 30
City (using get): New York

2. Adding Items
Dictionary after adding email: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}

3. Modifying Items
Dictionary after modifying age: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}

4. Removing Items
Dictionary after removing city (using pop): {'name': 'John', 'age': 31, 'email': 'john@example.com'}
Dictionary after removing email (using del): {'name': 'John', 'age': 31}

5. Dictionary Methods
Keys: dict_keys(['name', 'age'])
Values: dict_values(['John', 31])
Items: dict_items([('name', 'John'), ('age', 31)])

6. Clearing the Dictionary
Dictionary after clearing: {}

7. Updating the Dictionary
Dictionary after updating: {'name': 'John', 'age': 32, 'city': 'New York', 'country': 'USA'}

8. Iterating Through a Dictionary
Iterating through keys:
name
age
city
country

Iterating through values:
John
32
New York
USA

Iterating through items (key-value pairs):
name: John
age: 32
city: New York
country: USA

9. checking if a key exist
Name exist

10. Dictionary Length
Length of the dictionary: 4

11. Creating a dictionary from iterable
new dictionary: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

12. Copying a dictionary
Copied dictionary: {'name': 'John', 'age': 32, 'city': 'New York', 'country': 'USA'}

13. Nested Dictionaries
Nested dictionary: {'person1': {'name': 'Alice', 'age': 25}, 'person2': {'name': 'Bob', 'age': 30}}
Alice's age: 25
```

### **Dictionary Comprehensions**

Dictionary comprehensions provide a concise way to create dictionaries in Python. They are similar to list comprehensions but used for creating dictionaries instead of lists. Let's explore how dictionary comprehensions work and see some examples.

#### **Basic Syntax**

The basic syntax of a dictionary comprehension is:

```python
{key_expression: value_expression for item in iterable if condition}
```

```python
original_dict = {'a': 1, 'b': 2, 'c': 3}
print("original_dict = ", original_dict)
doubled_dict = {k: v*2 for k, v in original_dict.items()}
print("doubled_dict  = ", doubled_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}
```

**Output:**
```
original_dict =  {'a': 1, 'b': 2, 'c': 3}
doubled_dict  =  {'a': 2, 'b': 4, 'c': 6}
```

#### **Practice Exercise**

Try to create a dictionary comprehension that converts a list of temperatures in Celsius to Fahrenheit. The formula to convert Celsius to Fahrenheit is `F = (C * 9/5) + 32`.

```python
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = {str(c)+"c":  str((c * 9/5) + 32)+"f" for c in celsius_temps}
print(fahrenheit_temps)  # Output: {0: 32, 10: 50, 20: 68, 30: 86, 40: 104}
```

**Output:**
```
{'0c': '32.0f', '10c': '50.0f', '20c': '68.0f', '30c': '86.0f', '40c': '104.0f'}
```

