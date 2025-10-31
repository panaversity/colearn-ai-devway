# Lesson 07 The Set, Frozenset & GC

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>

# **The Set Data Type**
----

Set is one of `4 built-in data types` in Python used to store collections of data, the other 3 are **`List, Tuple, and Dictionary`**, all with different qualities and usage.

A set is:
  - **unordered**
  - **unindexed**
  - **mutable**

An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.



Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

```python
my_set: set = {123, 452, 5, 6}
my_set2: set = set([123, 452, 5, 6])
unknown: set = {} # set or dectionary
empty_set: set = set()

print("my_set            = ", my_set)
print("my_set2           = ", my_set2)
print("type(my_set)      = ", type(my_set))
print("type(my_set2)     = ", type(my_set2))
print("type(unknown)     = ", type(unknown))
print("type(empty_set)   = ", type(empty_set))
print("my_set == my_set2 = ", my_set == my_set2)
```

**Output:**
```
my_set            =  {123, 452, 5, 6}
my_set2           =  {123, 452, 5, 6}
type(my_set)      =  <class 'set'>
type(my_set2)     =  <class 'set'>
type(unknown)     =  <class 'dict'>
type(empty_set)   =  <class 'set'>
my_set == my_set2 =  True
```

###Holds only Immutable Objects
----

A set can store only immutable objects such as number `(int, float, complex or bool), string or tuple`. If you try to put a *list or a dictionary* in the set collection, Python raises a TypeError.

Lets check set if it can hold mutable object like **`list[]`**

```python
my_set = {[123, 452, 5, 6]} # TypeError: unhashable type: 'list'
print(my_set)
```

**Error:**
```
TypeError: unhashable type: 'list'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-33-7d7d29830862> in <cell line: 0>()
----> 1 my_set = {[123, 452, 5, 6]} # TypeError: unhashable type: 'list'
      2 print(my_set)

TypeError: unhashable type: 'list'
```

### It can hold multiple data types at once.

```python
multi_type_set: set = {7, 9.0, False, True, "Hello! World", (1,5,9,'hi') }
print(multi_type_set)
```

**Output:**
```
{False, True, 7, 9.0, 'Hello! World', (1, 5, 9, 'hi')}
```

##The set is **unordered**
----
Note that items in the set collection may not follow the same order in which they are entered. The position of items is optimized by Python to perform operations over set as defined in mathematics.


```python
set2: set = {'Java', 'Python', 'JavaScript', 'java'}
print(set2)
```

**Output:**
```
{'Python', 'Java', 'java', 'JavaScript'}
```

"*Python sets are unordered collections, but internally, elements are stored based on their hash values. However, this internal structure is not predictable or stable across operations*".

We will dive in to the details of hashing later in this tutorial.

##The set can not be  **Change Directly using [ ]**
----
When we say that set items are unchangeable, it means that you cannot modify an individual item in a set directly. **`However, you can add or remove items from the set.`**

Here is an example to illustrate this concept:

```python
# Create a set
my_set: set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Try to change an item (this will raise an error)
try:
    my_set[0] = 10  # Sets are unordered, so indexing doesn't work
except TypeError as e:
    print(e)  # Output: 'set' object does not support item assignment
```

  - set's are unordered, so indexing doesn't work ~my_set[0]~
  - set object does not support item assignment ~my_set[0] = 10~

```python
# Create a set
my_set: set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Try to change an item (this will raise an error)
try:
    my_set[0] = 10  # Sets are unordered, so indexing doesn't work
except TypeError as e:
    print("*TypeError*  ABC : ", e)  # Output: 'set' object does not support item assignment

print("Program execution continues as normal because we handle the error condition in try except block")
```

**Output:**
```
{1, 2, 3, 4, 5}
*TypeError*  ABC :  'set' object does not support item assignment
Program execution continues as normal because we handle the error condition in try except block
```

As you can see, you can't change an individual item in a set directly. Instead, you can remove the item and add a new one with the updated value. Alternatively, you can use the `discard()` or `remove()` methods to remove items and the `add()` or `update()` methods to add new items.

```python
my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print(my_set)
# Remove an item
my_set.remove(3)
my_set.remove('A')
print(my_set)  # Output: {1, 2, 4, 5}
```

**Output:**
```
{1, 2, 3, 4, 5, 'A', 'a'}
{1, 2, 4, 5, 'a'}
```

```python
my_set.add(6)
print(my_set)  # Output: {1, 2, 4, 5, 6}
```

**Output:**
```
{1, 2, 4, 5, 6, 'a'}
```

```python
my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("my_set = ", my_set)

# discard() only removes a single element.
# {1, 2, 3} is a set itself, not an element within my_set.
# Therefore, discard does not find it and returns None, without modifying the set.
print(my_set.discard({1,2,3}))

print("After: my_set = ", my_set) # return None

# To remove multiple elements, iterate and discard each one individually:
for item in {1, 2, 3}:
    my_set.discard(item)

print("After removing multiple elements: my_set = ", my_set)
```

**Output:**
```
my_set =  {1, 2, 3, 4, 5, 'A', 'a'}
None
After: my_set =  {1, 2, 3, 4, 5, 'A', 'a'}
After removing multiple elements: my_set =  {4, 5, 'A', 'a'}
```

**Use difference_update() method to remove multiple element at once.**

```python
my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("Before: my_set = ", my_set)
my_set.difference_update({1, 5, 3, 'A'})
print("After:  my_set = ", my_set)
```

**Output:**
```
Before: my_set =  {1, 2, 3, 4, 5, 'A', 'a'}
After:  my_set =  {2, 4, 'a'}
```

```python
print("Before: ", my_set)
# Add multiple items
my_set.update([7, 8, 9, "Hello"])
print(my_set)  # Output: {4, 5, 6, 7, 8, 9}
```

**Output:**
```
Before:  {2, 4, 'a'}
{2, 4, 'Hello', 7, 8, 9, 'a'}
```

**Using the union() method or | operator:**

In Python, the `union()` method or the `|` operator is used to combine two sets into a single set. This operation returns a new set containing all unique elements from both sets.

**Using the union() method:**

The `union()` method is a built-in method of the set data type in Python. It takes an iterable (such as a set, list, or tuple) as an argument and returns a new set containing all unique elements from both the original set and the iterable.

```python
my_set: set   = {1, 2, 3, 5}
my_set_2: set = {1, 5, 6, 7}

my_set3: set  = my_set.union(my_set_2)
print(my_set3)
```

**Output:**
```
{1, 2, 3, 5, 6, 7}
```

**Using the | operator:**

The `|` operator is a binary operator that can be used to combine two sets into a single set. It has the same effect as the `union()` method, but is often more concise and readable.

```python
my_set: set   = {1, 2, 3, 5}
my_set_2: set = {1, 5, 6, 7}

my_set3: set  = my_set | my_set_2 # | operator
print(my_set3)
```

**Output:**
```
{1, 2, 3, 5, 6, 7}
```

**Key aspects of union() and | operator:**

1. **Unique elements**: The resulting set contains only unique elements from both sets.

2. **Order does not matter**: The order in which the sets are combined does not affect the result.
3. **Original sets remain unchanged**: The original sets are not modified by the union operation.

### **Unique Elements**
----

Note that sets only store unique elements, so if you try to add a duplicate item, it will be ignored. For example:

```python
my_set: set = {1,2,3,4,5, "Hello! World"}
print("Before : ", my_set)

my_set.add(2)
my_set.add("Hello! World")

print("After  : ", my_set)
```

**Output:**
```
Before :  {1, 2, 3, 4, 5, 'Hello! World'}
After  :  {1, 2, 3, 4, 5, 'Hello! World'}
```

`discard()` and `remove()` methods
----
In Python, both `discard()` and `remove()` methods are used to remove items from a set. However, there is a key difference between the two methods:

1. **`remove()` method:**
   - The `remove()` method removes the specified item from the set.
   - If the item is not found in the set, it raises a `KeyError`.
   - This method is suitable when you are sure that the item exists in the set.

2. **`discard()` method:**
   - The `discard()` method also removes the specified item from the set.
   - However, if the item is not found in the set, it does not raise any error. It simply does nothing.
   - This method is suitable when you are not sure if the item exists in the set.

Here's an example to illustrate the difference:

```python
# Lets create an error to understand
my_set: set = {1,2,3}

my_set.remove(4)
print(my_set)
```

**Error:**
```
KeyError: 4
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-6-bb3f2e8ccea7> in <cell line: 0>()
      2 my_set: set = {1,2,3}
      3 
----> 4 my_set.remove(4)
      5 print(my_set)

KeyError: 4
```

```python
print("Before pop() = ", my_set)

#When you call `my_set.pop()`, it removes and returns an arbitrary element from the set.
#Since sets are unordered data structures, the element that is removed and returned is not predictable.
my_set.pop()
print("Before pop() = ", my_set)
```

**Output:**
```
Before pop() =  {1, 2, 3}
Before pop() =  {2, 3}
```

```python
my_set = {1,2,3}

my_set.discard(4) # method
print(my_set)
```

**Output:**
```
{1, 2, 3}
```

In summary:

- Use `remove()` when you are sure that the item exists in the set and you want to handle the error if it does not exist.
- Use `discard()` when you are not sure if the item exists in the set and you want to avoid raising an error if it does not exist.

When to use each method:

- **`remove()`**:
  - When working with small sets where performance is not a concern.
  - When you need to handle the error if the item does not exist.
- **`discard()`**:
  - When working with large sets where performance is a concern.
  - When you do not care about handling the error if the item does not exist.

In general, if you are not sure which method to use, `discard()` is a safe choice as it does not raise an error if the item does not exist.

## **The Inner Working of SET (Advance Topic)**
----

##The Hashing
  - Hashing is a mechanism in computer science which enables quicker searching of objects in computer's memory. Only immutable objects are hashable.

  - Immutable data types in Python come with a built-in method for computing their hash value, which is called __hash__.

  - A hash table is a data structure that can map keys to values and that implements a hash function to compute the index to an array of buckets or slots

```python
a: str = "Hello! World"
b: str = "Hello! World"

print("id(a) = ", id(a))
print("id(b) = ", id(b))
```

**Output:**
```
id(a) =  132467750244336
id(b) =  132466877525360
```

```python
print("hash(a) = ", hash(a))
print("hash(b) = ", hash(b))
print("-----------")
print("hash(a)      = ",hash(a))
print("a.__hash__() = ", a.__hash__()) # __dunder__()
```

**Output:**
```
hash(a) =  9090330697819382555
hash(b) =  9090330697819382555
-----------
hash(a)      =  9090330697819382555
a.__hash__() =  9090330697819382555
```

###Important Note:
----
  - Even if a set only allows `immutable items`, the set itself is **`mutable`**. Hence, add/delete/update operations are permitted on a set object

  - In Python, a dictionary **`key`** must be an **`immutable`** object, meaning its value cannot be changed after it's created. This is because dictionaries use a hash table to store key-value pairs, and mutable objects cannot be hashed.

  - Lets pass the set as key in dictionary which only accept immutable item as a key.

```python
# TypeError: unhashable type: 'set'
my_set: set   = {1,2,3,4,5, "Hello! World"}
my_dict: dict = {my_set: "Hello! World"} # dictionary only accept immutable objects as a key
print(my_dict)
```

**Error:**
```
TypeError: unhashable type: 'set'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-4e734c8deef1> in <cell line: 0>()
      1 # TypeError: unhashable type: 'set'
      2 my_set: set   = {1,2,3,4,5, "Hello! World"}
----> 3 my_dict: dict = {my_set: "Hello! World"} # dictionary only accept immutable objects as a key
      4 print(my_dict)

TypeError: unhashable type: 'set'
```

## **How Hashing Determines Internal Storage in Sets**

In Python, sets are implemented using hash tables (specifically, dictionaries under the hood). This allows O(1) average-time complexity for lookups, insertions, and deletions. However, the way elements are stored in memory depends on hashing, which can lead to unpredictable ordering.

## **O(1) average-time complexity**

Time complexity is the number of operations needed to run an algorithm on large amounts of data. And the number of operations can be considered as time because the computer uses some time for each operation. When talking about "operations" here, "one operation" might take one or several CPU cycles.

O(1) average-time complexity in Python, also known as constant time complexity, signifies that the time taken for an operation to complete remains constant, irrespective of the input data size. In simpler terms, the execution time of the operation does not grow as the input size increases.

When we talk about "input size" in the context of algorithms and time complexity, we're referring to the amount of data that an algorithm processes. It's a measure of how much "stuff" the algorithm has to work with. The input size is a crucial factor in determining how long an algorithm will take to run

## **Imagine you have a box of toys.**

- `O(1) is like`: You know exactly where your favorite toy car is in the box. No matter how many other toys are in the box (10 toys or 100 toys), it always takes you the same amount of time to grab that specific car because you know exactly where it is. It doesn't take longer even if you have more toys. It's super fast and consistent!

## **Key Points About Hashing in Sets:**


1. Each element in a set is hashed to determine its storage position.

2.  The internal order is based on hash values, not insertion order.
3.  The order can change dynamically when elements are added or removed.

## **Understanding Rehashing and Changing Order**

### **What is Rehashing?**

* Rehashing occurs when the underlying hash table needs to expand due to increasing elements.

* Python dynamically resizes the hash table when it reaches a certain load factor (a ratio of stored elements to available slots).

* **`During rehashing, all elements get redistributed, meaning their storage positions can change, even if no explicit sorting is done.`**

### **Example: How Set Order Can Change Dynamically**

```python
# Initial set
my_set = {10, 3, 5, 8}
print(my_set)  # Output may be {8, 10, 3, 5} or another order

# Adding an element
my_set.add(20)
print(my_set)  # The order might change unpredictably

# Removing an element
my_set.remove(10)
print(my_set)  # Again, the order can change
```

**Output:**
```
{8, 10, 3, 5}
{3, 5, 8, 10, 20}
{3, 5, 8, 20}
```

### **Why Does the Order Change?**

* New elements may trigger rehashing, leading to reallocation of storage.

* Removing an element can also affect the layout, especially if rehashing is triggered due to shrinking.

### **Does This Mean Sets Are Ordered Internally?**
🚫 No.

Even though elements are stored based on their hash values, this does not mean sets are ordered in the way lists or tuples are. Order can change unexpectedly, so it’s unreliable for ordered operations like indexing.

## **Conclusion**

* Hashing determines where elements are stored, but this structure is not stable across operations.

* Adding or removing elements can trigger rehashing, which causes internal storage reallocation and an unpredictable order.


# **The Frozenset**
----
In Python, a `frozenset` is an `immutable` (unchangeable) version of a set. It is a collection of unique elements, just like a set, but it cannot be modified after it is created.

Unlike regular sets, frozensets in Python are immutable, meaning their contents cannot be changed once created. They are unordered collections of unique elements, similar to sets, but with the added restriction of immutability. This characteristic makes frozensets hashable, allowing them to be used as dictionary keys or elements within other sets. While sets are dynamic, frozensets provide a static and unchanging representation of data, making them suitable for scenarios requiring immutability.

*(Contributor: Daniel Hashmi from Karachi)*

Here are the key features of a `frozenset`:

1. **Immutable**: A `frozenset` cannot be modified after it is created. You cannot add, remove, or change elements in a `frozenset`.

2. **Unordered**: In Python, frozenset objects are unordered collections of unique, immutable, and hashable elements.
3. **Hashable**: `frozensets` are hashable, meaning they can be used as keys in dictionaries or elements in other sets.
4. **Unique elements**: A `frozenset` can only contain unique elements, just like a set.

Here are the key differences between a `set` and a `frozenset` in Python:

1. **Immutability**:
   - `set`: Mutable (can be modified after creation)
   - `frozenset`: Immutable (cannot be modified after creation)

2. **Modification methods**:
   - `set`: Supports methods like `add()`, `remove()`, `discard()`, `clear()`, `pop()`, `update()`
   - `frozenset`: Does not support any modification methods

3. **Hashability**:
   - `set`: Not hashable (cannot be used as keys in dictionaries or elements in other sets)
   - `frozenset`: Hashable (can be used as keys in dictionaries or elements in other sets)

4. **Thread safety**:
   - `set`: Not thread-safe (multiple threads can modify the set simultaneously, leading to inconsistencies)
   - `frozenset`: Thread-safe (since it's immutable, it's safe to access from multiple threads)

5. **Syntax**:
   - `set`: Created using the `set()` function or the `{}` syntax (e.g., `my_set = {1, 2, 3}`)
   - `frozenset`: Created using the `frozenset()` function (e.g., `my_frozenset = frozenset([1, 2, 3])`)

6. **Use cases**:
   - `set`: Suitable for situations where you need to frequently add or remove elements (e.g., when filtering data)
   - `frozenset`: Suitable for situations where you need an immutable collection (e.g., when using it as a key in a dictionary or as an element in another set)


   Here's a summary of the differences:

| Feature | Set | Frozenset |
| --- | --- | --- |
| Immutability | Mutable | Immutable |
| Modification methods | Yes | No |
| Hashability | No | Yes |
| Thread safety | No | Yes |
| Syntax | `set()` or `{}` | `frozenset()` |
| Use cases | Frequent modifications | Immutable collection |

```python
my_frozenset: frozenset = frozenset([1,2,3, "Hello! World"])
print("my_frozenset  = ", my_frozenset)

my_set: set = {1,2,3, "Hello! World"}
my_frozenset2: frozenset = frozenset(my_set)
print("my_frozenset2 = ",my_frozenset2)
```

**Output:**
```
my_frozenset  =  frozenset({1, 2, 3, 'Hello! World'})
my_frozenset2 =  frozenset({1, 2, 3, 'Hello! World'})
```

### **Conclusion:**

In conclusion, sets and frozensets exhibit distinct characteristics while representing unordered collections of unique elements in Python. Sets offer mutability, allowing for dynamic modifications, while frozensets provide immutability, making them suitable for use as dictionary keys or elements within other sets. Understanding these fundamental data structures is essential for effective data manipulation and problem-solving in Python.

Set Methods
----


```python
my_set:  set = {1,2,3, "Hello! World", 4,5,6}
my_set2: set = {1,2,3, "Hello! World", 8,9}
my_set3: set = {1,2,3, "Hello! World", 77}

print("difference()           = ", my_set.difference(my_set2, my_set3)) #Returns a set containing the difference between two or more sets
print("intersection()         = ", my_set.intersection(my_set2, my_set3))#Return a set that contains the items that exist in both set
print("union()                = ", my_set.union(my_set2, my_set3))#Return a set that contains all items from both sets, duplicates are excluded:
print("symmetric_difference() = ", my_set.symmetric_difference(my_set2))#One argument only, #Return a set that contains only unique items from both sets

#my_set = {55,66}

print("isdisjoint()           = ", my_set.isdisjoint(my_set2))#Return True if no items in set x is present in set y

my_set2 = {1,2,3, "Hello! World"}
print("issuperset()           = ", my_set.issuperset(my_set2))#Return True if all items in set x are present in set y
print("issubset()             = ", my_set2.issubset(my_set))
```

**Output:**
```
difference()           =  {4, 5, 6}
intersection()         =  {1, 2, 3, 'Hello! World'}
union()                =  {1, 2, 3, 4, 5, 6, 8, 9, 77, 'Hello! World'}
symmetric_difference() =  {4, 5, 6, 8, 9}
isdisjoint()           =  False
issuperset()           =  True
issubset()             =  True
```

```python
# prompt: generate examples of all the method of set

# Example usage of set methods

# Initialize two sets for demonstration
set1: set = {1, 2, 3, 4, 5}
set2: set = {4, 5, 6, 7, 8}

# 1. add(): Adds an element to the set.
set1.add(6)
print(f"add(6): {set1}")  # Output: {1, 2, 3, 4, 5, 6}

# 2. clear(): Removes all elements from the set.
set_copy: set = set1.copy()
set_copy.clear()
print(f"clear(): {set_copy}")  # Output: set()

# 3. copy(): Returns a copy of the set.
set_copy: set = set1.copy()
print(f"copy(): {set_copy}")  # Output: {1, 2, 3, 4, 5, 6}

# 4. difference(): Returns a set containing the difference between two or more sets.
difference_set: set = set1.difference(set2)
print(f"difference(): {difference_set}")  # Output: {1, 2, 3}

# 5. difference_update(): Removes the items in this set that are also included in another, specified set.
set1.difference_update(set2)
print(f"difference_update(): {set1}")  # Output: {1, 2, 3}
set1: set = {1, 2, 3, 4, 5,6} #reset set1

# 6. discard(): Remove the specified item.
set1.discard(6)
print(f"discard(6): {set1}")  # Output: {1, 2, 3, 4, 5}

# 7. intersection(): Returns a set, that is the intersection of two other sets.
intersection_set: set = set1.intersection(set2)
print(f"intersection(): {intersection_set}")  # Output: {4, 5}

# 8. intersection_update(): Removes the items in this set that are not present in other, specified set(s)
set1.intersection_update(set2)
print(f"intersection_update(): {set1}") # Output: {4, 5}
set1 = {1, 2, 3, 4, 5,6} #reset set1

# 9. isdisjoint(): Returns whether two sets have a intersection or not.
print(f"isdisjoint(): {set1.isdisjoint(set2)}")  # Output: False
print(f"isdisjoint(): {set1.isdisjoint({9,10})}") # Output: True

# 10. issubset(): Returns whether another set contains this set or not.
print(f"issubset(): {set1.issubset(set2)}")  # Output: False
print(f"issubset(): {{1,2}}.issubset({set1})")  # Output: True
print(f"issubset(): {{1,2}}.issubset({{1,2}})")  # Output: True


# 11. issuperset(): Returns whether this set contains another set or not.
print(f"issuperset(): {set1.issuperset(set2)}")  # Output: False
print(f"issuperset(): {set1.issuperset({1,2})}")  # Output: True
print(f"issuperset(): {{1,2}}.issuperset({{1,2}})")  # Output: True

# 12. pop(): Removes a random element from the set.
removed_element: int = set1.pop()
print(f"pop(): {removed_element}")  # Output: (random element)
print(f"set after pop(): {set1}")  # Output: (set without removed_element)
set1.add(removed_element)#put back the element for others test

# 13. remove(): Removes the specified element. Raises an error if the element is not present.
set1.remove(1)
print(f"remove(1): {set1}")  # Output: {2, 3, 4, 5,6}
set1.add(1)#put back the element for others test

# 14. symmetric_difference(): Returns a set with the symmetric differences of two sets.
symmetric_difference_set: set = set1.symmetric_difference(set2)
print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: {1, 2, 3, 6, 7, 8}

# 15. symmetric_difference_update(): Inserts the symmetric differences from this set and another
set1.symmetric_difference_update(set2)
print(f"symmetric_difference_update(): {set1}")  # Output: {1, 2, 3, 6, 7, 8}
set1 = {1, 2, 3, 4, 5,6} #reset set1

# 16. union(): Returns a set containing the union of sets.
union_set = set1.union(set2)
print(f"union(): {union_set}")  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# 17. update(): Update the set with the union of this set and others
set1.update(set2)
print(f"update(): {set1}") # Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

**Output:**
```
add(6): {1, 2, 3, 4, 5, 6}
clear(): set()
copy(): {1, 2, 3, 4, 5, 6}
difference(): {1, 2, 3}
difference_update(): {1, 2, 3}
discard(6): {1, 2, 3, 4, 5}
intersection(): {4, 5}
intersection_update(): {4, 5}
isdisjoint(): False
isdisjoint(): True
issubset(): False
issubset(): {1,2}.issubset({1, 2, 3, 4, 5, 6})
issubset(): {1,2}.issubset({1,2})
issuperset(): False
issuperset(): True
issuperset(): {1,2}.issuperset({1,2})
pop(): 1
set after pop(): {2, 3, 4, 5, 6}
remove(1): {2, 3, 4, 5, 6}
symmetric_difference(): {1, 2, 3, 7, 8}
symmetric_difference_update(): {1, 2, 3, 7, 8}
union(): {1, 2, 3, 4, 5, 6, 7, 8}
update(): {1, 2, 3, 4, 5, 6, 7, 8}
```

## **frozensets Methods:**

```python
# Create some example frozensets
frozen_set1: frozenset = frozenset([1, 2, 3, 4])
frozen_set2: frozenset = frozenset([3, 4, 5, 6])
frozen_set3: frozenset = frozenset([1, 2])

print(f"frozen_set1: {frozen_set1}")
print(f"frozen_set2: {frozen_set2}")
print(f"frozen_set3: {frozen_set3}")
print("\n----------\n")
# Methods that work with frozensets (since they are immutable)
# These methods return a new frozenset or a boolean value

# 1. difference(): Returns a new frozenset with elements present in the first frozenset but not in the second.
difference_set: frozenset = frozen_set1.difference(frozen_set2)
print(f"difference(): {difference_set}")  # Output: frozenset({1, 2})

# 2. intersection(): Returns a new frozenset containing only elements common to both frozensets.
intersection_set: frozenset = frozen_set1.intersection(frozen_set2)
print(f"intersection(): {intersection_set}")  # Output: frozenset({3, 4})

# 3. union(): Returns a new frozenset containing all unique elements from both frozensets.
union_set: frozenset = frozen_set1.union(frozen_set2)
print(f"union(): {union_set}")  # Output: frozenset({1, 2, 3, 4, 5, 6})

# 4. symmetric_difference(): Returns a new frozenset with elements that are in either of the sets but not in both.
symmetric_difference_set: frozenset = frozen_set1.symmetric_difference(frozen_set2)
print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: frozenset({1, 2, 5, 6})

# 5. isdisjoint(): Returns True if the two frozensets have no elements in common; otherwise, False.
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozen_set2)}")  # Output: False
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozenset([7, 8]))}")  # Output: True

# 6. issubset(): Returns True if all elements of the first frozenset are present in the second frozenset.
print(f"issubset(): {frozen_set3.issubset(frozen_set1)}")  # Output: True
print(f"issubset(): {frozen_set1.issubset(frozen_set3)}")  # Output: False

# 7. issuperset(): Returns True if all elements of the second frozenset are present in the first frozenset.
print(f"issuperset(): {frozen_set1.issuperset(frozen_set3)}")  # Output: True
print(f"issuperset(): {frozen_set3.issuperset(frozen_set1)}")  # Output: False

# 8. copy(): Returns a new frozenset that is a shallow copy of the original.
copy_set: frozenset = frozen_set1.copy()
print(f"copy(): {copy_set}")  # Output: frozenset({1, 2, 3, 4})
print(f"copy() is same object?: {copy_set is frozen_set1}") # Output: True because frozensets are immutable
```

**Output:**
```
frozen_set1: frozenset({1, 2, 3, 4})
frozen_set2: frozenset({3, 4, 5, 6})
frozen_set3: frozenset({1, 2})

----------

difference(): frozenset({1, 2})
intersection(): frozenset({3, 4})
union(): frozenset({1, 2, 3, 4, 5, 6})
symmetric_difference(): frozenset({1, 2, 5, 6})
isdisjoint(): False
isdisjoint(): True
issubset(): True
issubset(): False
issuperset(): True
issuperset(): False
copy(): frozenset({1, 2, 3, 4})
copy() is same object?: True
```

## **GC: Garbage Collection**

**Python has a garbage collection mechanism.**

Python's garbage collector is a **`Memory Management System`** that **`automatically`** frees up memory occupied by objects that are no longer needed or referenced. This helps prevent memory leaks and allows Python to manage memory efficiently.

### **Here's how it works:**

1. **Reference Counting**: Python uses a reference counting algorithm to track the number of references to each object. When an object is created, its reference count is set to 1. Each time a new reference to the object is created (e.g., assigning it to a variable or passing it as an argument), the reference count is incremented.

2. **Garbage Collection**: When an object's reference count reaches 0, it is no longer needed and becomes eligible for garbage collection. The garbage collector periodically runs in the background to identify and free up memory occupied by these objects.

### **Python's garbage collector is:**

* **Automatic**: You don't need to manually manage memory or explicitly free up memory.

* **Periodic**: The garbage collector runs periodically to clean up memory.
* **Reference-based**: It uses reference counting to determine which objects are no longer needed.

You can also manually trigger the garbage collector using the `gc.collect()` function from the `gc` module:

```python
import gc

gc.collect()
print(gc.get_count())  # prints the number of collected objects, unreachable objects, and reference cycles
```

**Output:**
```
(43, 0, 0)
```

However, this is usually not necessary, as the garbage collector runs automatically in the background.

Some benefits of Python's garbage collection:

* **Memory safety**: Prevents memory leaks and ensures memory is freed up when no longer needed.
* **Convenience**: You don't need to worry about manually managing memory.
* **Efficiency**: The garbage collector runs periodically to optimize memory usage.

Note that Python's garbage collection is not perfect, and there are some cases where it may not work as expected (e.g., circular references, file descriptors). However, it provides a convenient and efficient way to manage memory in most cases.

