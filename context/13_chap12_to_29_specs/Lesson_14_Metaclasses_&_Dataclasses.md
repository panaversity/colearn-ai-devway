# Lesson 14 Metaclasses & Dataclasses

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>




#  **Metaclasses in Python</font> (Simplified! 🎯)**

Metaclasses are like **"classes of classes"**—they define how classes themselves behave, just like classes define how instances behave.

#### **Key Idea:**

-   **Classes** are **instances of metaclasses** (just like objects are instances of classes).
-   By default, most classes use `type` as their metaclass.

----------

## **1. What Problem Do Metaclasses Solve?**

Metaclasses let you:  
✅ **Control class creation** (e.g., enforce rules, modify attributes automatically).  
✅ **Add hidden features** to all classes that use your metaclass.  
✅ **Prevent bad class design** (e.g., ensure all subclasses implement a method).

**Example Use Cases:**

-   ORMs (like Django models)
-   Automatic registration of classes
-   Singleton patterns
-   API validation

----------

## **2. How Metaclasses Work (Step-by-Step 🛠️)**

### **(1) Default Behavior (`type` metaclass)**

Normally, when you define a class:

```python
class Dog:
    pass
```

Python silently uses type to create it:

```python
Dog = type("Dog", (), {})  # Same as `class Dog: pass`
```

### **(2) Custom Metaclass**

You can create your own metaclass by inheriting from `type`:

```python
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # Runs when a class is created
        print(f"MyMeta: Creating class: {name}")
        return super().__new__(cls, name, bases, attrs)
```


### **(3) Using a Metaclass**

Apply it to a class with `metaclass=MyMeta`:

```python
class Cat(metaclass=MyMeta):
    pass
```

**Output:**
```
MyMeta: Creating class: Cat
```


✅ Now, `MyMeta` controls how `Cat` is created!

----------

## **3. Real-World Example: Enforce Class Rules**

Let’s **force all subclasses** to have a `say_hello()` method &  class name must start with `'A'`:

```python
class EnforceHelloMeta(type):
    def __new__(cls, name, bases, attrs):
        # Check if the class defines 'say_hello'
        if "say_hello" not in attrs: # enforcing law to have say_hello() method
            raise TypeError(f"{name} must define 'say_hello()'!")

        if not name.startswith("A"):
            raise ValueError("Class name must start with 'A'")

        return super().__new__(cls, name, bases, attrs)
```

```python
class Animal(metaclass=EnforceHelloMeta):
    def say_hello(self):
        pass
```

```python
class Anaconda(Animal):
    def say_hello(self):
        print("Hisss!")  # ✅ Works!
```

```python
#Test case
anaconda: Anaconda = Anaconda()
anaconda.say_hello()
```

**Output:**
```
Hisss!
```

## **Enforce Class Rules:**

Let’s force all subclasses to have a say_hello() method and class name starts with 'A':

```python
class Animal(metaclass=EnforceHelloMeta):
    pass  # ❌ Error: Must define 'say_hello'!
```

**Error:**
```
TypeError: Animal must define 'say_hello()'!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-991f280bd7bb> in <cell line: 0>()
----> 1 class Animal(metaclass=EnforceHelloMeta):
      2     pass  # ❌ Error: Must define 'say_hello'!

<ipython-input-5-7a539430a4fd> in __new__(cls, name, bases, attrs)
      3         # Check if the class defines 'say_hello'
      4         if "say_hello" not in attrs: # enforcing law to have say_hello() method
----> 5             raise TypeError(f"{name} must define 'say_hello()'!")
      6 
      7         if not name.startswith("A"):

TypeError: Animal must define 'say_hello()'!
```

```python
class Dog(Animal): # ❌ Error: Must define a class name starts with 'A'
    def say_hello(self):
        print("Woof!")
```

**Error:**
```
ValueError: Class name must start with 'A'
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-10-20fb20ecdc57> in <cell line: 0>()
----> 1 class Dog(Animal): # ❌ Error: Must define a class name starts with 'A'
      2     def say_hello(self):
      3         print("Woof!")

<ipython-input-5-7a539430a4fd> in __new__(cls, name, bases, attrs)
      6 
      7         if not name.startswith("A"):
----> 8             raise ValueError("Class name must start with 'A'")
      9 
     10         return super().__new__(cls, name, bases, attrs)

ValueError: Class name must start with 'A'
```

## **Example: Singleton Metaclass (ensures only 1 instance exists)**

```python
# Example: Singleton Metaclass (ensures only 1 instance exists)
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass

db1: Database = Database()
db2: Database = Database()
print(db1 is db2)  # True (same instance!)
```

**Output:**
```
True
```

## **4. Metaclass vs. Class Decorator**

| Feature      | Metaclass          | Class Decorator       |   |
|--------------|--------------------|-----------------------|---|
| When it runs | Class creation     | After class creation  |   |
| Use case     | Deep class control | Simpler modifications |   |
| Example      | Enforce methods    | Add logging           |   |


**Prefer class decorators** if you don’t need metaclass power!

----------

## **5. Should You Use Metaclasses?**

-   **✅ YES:** For advanced frameworks (Django, SQLAlchemy).
-   **❌ NO:** For everyday code (use simpler tools like decorators instead).

### **Metaclass Pros & Cons**

| Pros                  | Cons                    |   |   |
|-----------------------|-------------------------|---|---|
| Extremely powerful    | Hard to debug           |   |   |
| Great for APIs        | Overkill for most cases |   |   |
| Used in big libraries | Can make code confusing |   |   |


----------

### **Final Verdict 🏆**

-   **Metaclasses = "Class factories".**
-   **Use them sparingly** (only when absolutely needed).
-   **Most devs never write one**—but understanding them helps debug big frameworks!



---


# **Dataclasses in Python: A Complete Guide**

Dataclasses are a powerful Python feature introduced in Python 3.7 (via PEP 557) that automatically generate common boilerplate code for classes. They're designed to simplify class creation when the class primarily stores data.


## **What is a `dataclass` in Python?**

A `dataclass` in Python is a decorator introduced in Python 3.7 that simplifies the creation of classes used primarily for storing data. A `dataclass` automatically adds special methods to the class, like:

-   `__init__`: a constructor method to initialize attributes.
    
-   `__repr__`: a method that provides a human-readable string representation of the object.
    
-   `__eq__`: a method for comparing instances for equality based on their attributes.
    
-   `__hash__`: a method that allows instances of the class to be used as dictionary keys or in sets.
    

These methods are automatically generated, reducing the need for boilerplate code and making the code more concise and readable.

## **Why do we need `dataclass`?**

In traditional Python, when we create a class to store data, we have to manually implement special methods like `__init__`, `__repr__`, `__eq__`, and others. This can result in repetitive and error-prone code, especially if the class is primarily used to hold data with little additional logic.

Before `dataclass`, a typical Python class for holding data might look like this:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
```

```python
# prompt: use person class

person: Person = Person("Alice", 30)
print(person)
```

**Output:**
```
Person(name=Alice, age=30)
Alice
30
True
```

**With `dataclass`, the code becomes much simpler:**

```python
from dataclasses import dataclass

@dataclass(unsafe_hash=True) # We will discuss unsafe_hash later in the tutorial
class Person:
    name: str
    age: int
```

✅ Same functionality in 6 lines instead of 12!

```python
# prompt: use person class in example showing repr eq and hash dunders

# Example usage
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 30)

print("person1               = ", person1)  # Output using __repr__
print("person1 == person2    = ", person1 == person2)  # Output using __eq__
print("person1 == person3    = ", person1 == person3)  # Output using __eq__

# Demonstrate hashing
person_set = {person1, person2}
print("person1 in person_set = ", person1 in person_set)  # True
print("person3 in person_set = ", person3 in person_set)  # True (because person1 and person3 are equal)

person_dict = {person1: "Alice's data"}
print("person_dict[person3]  = ", person_dict[person3]) # Access using person3 (equal to person1)

print(person1.__hash__())
person1.age = 40
print(person1.__hash__())
person1.age = 30
print(person1.__hash__())
```

**Output:**
```
person1               =  Person(name='Alice', age=30)
person1 == person2    =  False
person1 == person3    =  True
person1 in person_set =  True
person3 in person_set =  True
person_dict[person3]  =  Alice's data
-7826415278014884702
2850418376737584128
-7826415278014884702
```


✅ **Same functionality in 3 lines instead of 10!**

----------

## **Why Do We Need Dataclasses?**

### **Problem: Boilerplate Code**

A typical Python class requires:

-   `__init__` (initialization)
-   `__repr__` (string representation)
-   `__eq__` (equality comparison)
-   And often `__hash__`, ordering methods, etc.

**Manual implementation is:**

-   Time-consuming
-   Error-prone
-   Hard to maintain

### **Solution: `@dataclass`**

Automatically generates all these methods while keeping:  
✔ **Type hints support**  
✔ **Clean syntax**  
✔ **Customizability when needed**

----------

## **Key Benefits of Dataclasses**

### **1. Automatic Method Generation**

| Method   | What It Does           | Automatically Generated?    |   |
|----------|------------------------|-----------------------------|---|
| __init__ | Initializes attributes | ✅ Yes                       |   |
| __repr__ | String representation  | ✅ Yes                       |   |
| __eq__   | Compares instances     | ✅ Yes                       |   |
| __hash__ | Makes objects hashable | Optional (unsafe_hash=True) |   |


### **2. Type Hints Integration**

Dataclasses **require type hints**, improving code clarity and enabling better IDE support:[link text](https://)

```python
@dataclass
class Point:
    x: float  # Type hints are mandatory
    y: float
```

### **3. Default Values**

```python
@dataclass
class User:
    username: str
    is_active: bool = True  # Default value
```

### **4. Immutability (frozen=True)**

```python
@dataclass(frozen=True)
class Config:
    api_key: str

config = Config("secret")
#config.api_key = "new"  # ❌ Error: frozen instance, uncomment to see error
```

### **5. Post-Initialization Processing**

```python
@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        self.adult = self.age >= 18
        print("Post init...")

Person("Alice", 25)
```

**Output:**
```
Post init...
```

**Output:**
```
Person(name='Alice', age=25)
```

## **When to Use Dataclasses?**

✅ **DTOs (Data Transfer Objects)**  
✅ **Configuration objects**  
✅ **Simple domain models**  
✅ **Any class storing data with little logic**

❌ **Not ideal for complex behavior-heavy classes**

----------

## **Comparison: Dataclass vs. Alternatives**

| Feature        | Dataclass      | NamedTuple | Plain Class    |
|----------------|----------------|------------|----------------|
| Mutable        | ✅ Yes          | ❌ No       | ✅ Yes          |
| Default Values | ✅ Yes          | ✅ Yes      | ✅ Yes          |
| Methods        | ✅ Full support | ❌ Limited  | ✅ Full support |
| Inheritance    | ✅ Yes          | ❌ No       | ✅ Yes          |
| Memory Usage   | Higher         | Lowest     | Highest        |


# **Python Typing & Dataclasses: Instance, Class, and Static Members**

This tutorial shows how to properly type instance variables/methods, class variables/methods, and static variables/methods using Python's `dataclasses` and `typing` modules.


## **Key Points Explained**

### **Instance Members**

-   **Variables**: Defined directly in class with type hints (handled by `@dataclass`)
-   **Methods**: First parameter is `self`, can access both instance and class data
-   **Default values**: Use `field()` for mutable defaults to avoid shared state issues

### **Class Members**

-   **Variables**: Annotated with `ClassVar` to indicate they belong to the class
-   **Final variables**: Use `ClassVar[Final]` for constants that shouldn't change
-   **Methods**: Decorated with `@classmethod`, first parameter is `cls`

### **Static Members**

-   **Variables**: In dataclasses, these become instance variables with defaults
-   **Methods**: Decorated with `@staticmethod`, no access to `self` or `cls`


## **When to Use Each**

1.  **Instance members**: For data/behavior specific to each object
2.  **Class members**: For data/behavior shared by all instances
3.  **Static members**: For utility functions that don't need instance/class access


## **Instance Variables and Methods**

Instance variables are attributes that are unique to each instance of a class. Instance methods are functions that belong to an instance of a class.



#### **Instance Variables**:

-   **Definition**: These variables are specific to each instance (object) of the class.
    
-   **Scope**: They are created and assigned when an object is instantiated, and they hold data specific to that object.
    
-   **Access**: Accessed through an instance of the class using `self`.
    

#### **Instance Methods**:

-   **Definition**: These are the regular methods in a class that operate on instance variables.
    
-   **Scope**: They work on a specific instance (object) of the class and can modify or retrieve instance variables using `self`.
    
-   **Access**: Accessed through an instance of the class.

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    """A person with a name and age."""
    name: str
    age: int
    occupation: Optional[str] = None

    def greet(self) -> None:
        """Print a greeting message."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of Person
person = Person("John Doe", 30, "Software Engineer")
print(person)  # Person(name='John Doe', age=30, occupation='Software Engineer')
person.greet()  # Hello, my name is John Doe and I am 30 years old.
```

**Output:**
```
Person(name='John Doe', age=30, occupation='Software Engineer')
Hello, my name is John Doe and I am 30 years old.
```


In this example, `name`, `age`, and `occupation` are instance variables, and `greet` is an instance method.

## **Class Variables and Methods**

Class variables are attributes that are shared by all instances of a class. Class methods are functions that belong to a class.



#### **Class Variables**:

-   **Definition**: These variables are shared by all instances of the class.
    
-   **Scope**: They belong to the class itself, not to any particular instance.
    
-   **Access**: Accessed using the class name or via an instance, but modifying it via instances will change the variable for that specific instance, not globally.
    

#### **Class Methods**:

-   **Definition**: These methods work on the class itself rather than on a specific instance. They can modify or access class variables.
    
-   **Scope**: Defined using the `@classmethod` decorator. They take `cls` as the first argument, representing the class.
    
-   **Access**: Accessed using the class name or an instance, but typically meant to operate at the class level.

```python
from dataclasses import dataclass, field
from typing import ClassVar, Final

@dataclass
class Person:
    """A person with a name and age."""
    name: str
    age: int
    occupation: str = "Unknown"
    species: ClassVar[str] = "Homo sapiens"

    # Final class variable (shouldn't be modified)
    #MAX_AGE: ClassVar[Final[int]] = 70

    @classmethod
    def get_species(cls) -> str:
        """Return the species of the person."""
        return cls.species

# Create an instance of Person
john = Person("John Doe", 30, "Software Engineer")
alex = Person("Alex", 25, "Accountant")

print(john.get_species())
print(alex.get_species())

Person.species = "New Species"

print(john.get_species())
print(alex.get_species())
```

**Output:**
```
Homo sapiens
Homo sapiens
New Species
New Species
```


In this example, `species` is a class variable, and `get_species` is a class method.

## **Static Variables and Methods**

Static variables are attributes that are shared by all instances of a class, but are not instance-specific. Static methods are functions that belong to a class, but do not have access to the class or instance.


#### **Static Variables**:

-   **Definition**: Static variables are variables that don't depend on the instance or class. In Python, we don’t typically use static variables, but they can be simulated using class variables or just constants.
    
-   **Scope**: They are often used as constants or utility values that don’t change. They can be accessed without an instance or class.
    

#### **Static Methods**:

-   **Definition**: Static methods are utility methods that don’t need to access or modify instance or class-level data.
    
-   **Scope**: Defined using the `@staticmethod` decorator. They do not take `self` or `cls` as parameters and are independent of both instance and class state.
    
-   **Access**: Accessed directly through the class or an instance, but typically don't interact with instance or class variables.

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    """A person with a name and age."""
    name: str
    age: int
    occupation: Optional[str] = None

    VERSION: Final[str] = '1.0.0'

    @staticmethod
    def get_version() -> str:
        """Get the Person class version"""
        return Person.VERSION

# Create an instance of Person
person = Person("John Doe", 30, "Software Engineer")
print(person.get_version())  # 1.0


# Create instances of Person
person1 = Person("John Doe", 30, "Software Engineer")
person2 = Person("Jane Doe", 25, "Doctor")

print(Person.get_version())  # 2
```

**Output:**
```
1.0.0
1.0.0
```

In this example, `COUNT` is a static variable, and `increment_count` is a static method.

## **Summary of Differences:**

| Feature          | Instance                                      | Class                                              | Static                                                        |
|------------------|-----------------------------------------------|----------------------------------------------------|---------------------------------------------------------------|
| Variables        | Belongs to a specific instance (object).      | Shared by all instances of the class.              | Doesn't depend on instance or class.                          |
| Methods          | Operates on instance variables (via self).    | Operates on class variables (via cls).             | Does not operate on instance or class data.                   |
| Access           | Accessed through an instance (obj.method())   | Accessed through class or instance (cls.method())  | Accessed via class or instance (cls.method() or obj.method()) |
| Typical Use Case | Data specific to an object (e.g., name, age). | Data shared by all instances (e.g., company name). | Utility functions or constants that don’t change state.       |
| Decorator        | None (normal method).                         | @classmethod                                       | @staticmethod                                                 |
|





## **Recap**:

-   **Instance Variables and Methods**: These are tied to specific instances and are accessed through the instance (`emp1`).
    
-   **Class Variables and Methods**: These are shared across all instances and can be accessed with `cls` in a class method. They can also be accessed directly using `ClassName`.
    
-   **Static Variables and Methods**: These don't depend on the instance or class and are typically used for `utility functions`. Static methods are defined using `@staticmethod`.
    

This example covers all the concepts you asked about, with simple use of the `dataclasses` module to make the class definition concise and readable!

## **Conclusion**

We have explored how to use the `typing` module to define instance variables and methods, class variables and methods, and static variables and methods using dataclasses. We have seen how to use the `@dataclass` decorator to define a class, and how to use the `ClassVar` and `Optional` types to define class variables and optional instance variables. We have also seen how to use the `@classmethod` and `@staticmethod` decorators to define class methods and static methods.


# The `Any` Type in Python's `typing` Module

**Definition:** `Any` represents any type, including built-in types, custom classes, and other types defined in the `typing` module.

**Usage:**

-   Use `Any` when a variable or function parameter can be any type.
-   Example: `def print_value(value: Any) -> None: print(value)`

**Advantages:**

-   Flexibility
-   Simplification

**Disadvantages:**

-   Loss of type safety
-   Less informative

**Best Practices:**

-   Use `Any` sparingly
-   Document expected type
-   Test thoroughly

**Example:**

```python
from typing import Any
import random

def print_value(value: Any) -> None:
    print("print_value = ", type(value), " : ", value)

print_value(123)  # prints: 123
print_value("hello")  # prints: hello

def get_value() -> Any:
    data_list: list = [1, "name", 2.0, True, {"key": "value"}]
    random_index: int = random.randint(0, len(data_list) - 1)
    return data_list[random_index]


value = get_value()
print("get_value   = ", type(value), " : ", value)
```

**Output:**
```
print_value =  <class 'int'>  :  123
print_value =  <class 'str'>  :  hello
get_value   =  <class 'float'>  :  2.0
```

### **Example: NamedTuple vs. Dataclass**

```python
from typing import NamedTuple
from dataclasses import dataclass

# NamedTuple (immutable)
class PointNT(NamedTuple):
    x: float
    y: float

# Dataclass (mutable)
@dataclass
class PointDC:
    x: float
    y: float

pnt: PointNT = PointNT(1, 2)
pdc: PointDC = PointDC(1, 2)

print(pdc)
pdc.x = 5 # ✅ mutable
print(pdc)

#pnt.x = 3 # ❌ immutable, uncomment to see error
```

**Output:**
```
PointDC(x=1, y=2)
PointDC(x=5, y=2)
```

----------

## **Advanced Features**

### **1. Field Customization**

```python
from dataclasses import field

@dataclass
class InventoryItem:
    name: str
    price: float = field(default=0.0)
    tags: list[str] = field(default_factory=list)

print(InventoryItem("Apple"))
```

**Output:**
```
InventoryItem(name='Apple', price=0.0, tags=[])
```

### **2. Ordering (order=True)**

```python
@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("Alice", 25)
bob = Person("Bob", 30)
print(alice < bob)  # Compares age
```

**Output:**
```
True
```

### **3. Inheritance**

```python
from dataclasses import dataclass

@dataclass
class Base:
    x: int

@dataclass
class Child(Base):
    y: int

    def print_x(self):
        """Print the value of x from the Base class."""
        print(self.x)  # Access x through self

# Create an instance of Child and call print_x
child_instance = Child(x=10, y=20)
print(child_instance)  # Child(x=10, y=20)
child_instance.print_x()  # Output: 10
```

**Output:**
```
Child(x=10, y=20)
10
```


----------

## **Real-World Example: API Response**

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class APIResponse:
    success: bool
    data: Optional[dict] = None
    error: Optional[str] = None

response = APIResponse(
    success=True,
    data={"user_id": 123}
)

print(response)
```

**Output:**
```
APIResponse(success=True, data={'user_id': 123}, error=None)
```

### **Let's play with hashing**

```python
# prompt: create person object an use it in dict

from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Person:
    name: str
    age: int
    _ssn: str = field(repr=False)  # _ssn will not appear in __repr__

# Create Person objects
person1 = Person("Alice", 30, _ssn="123-45-6789")
person2 = Person("Bob", 25, _ssn="333-44-6666")

print("person1 = ", person1) # _ssn will not print in __repr__
print("person2 = ", person2) # _ssn will not print in __repr__

# Use Person objects in a dictionary
person_dict = {person1: "Alice's data", person2: "Bob's data"}

# Access data using Person objects as keys
print(person_dict[person1])  # Output: Alice's data
print(person_dict[person2])  # Output: Bob's data

print(person1.__hash__())

# Uncomment below code to see error
# person1.age = 40 #❌ it change the hash value
# print(person1.__hash__())
# print(person_dict[person1])  # Output: Bob's data
```

**Output:**
```
person1 =  Person(name='Alice', age=30)
person2 =  Person(name='Bob', age=25)
Alice's data
Bob's data
4745862593296028892
```

The unsafe_hash=True argument in Python's @dataclass decorator is considered "unsafe" because it generates a hash method (__hash__) that relies on the mutable fields of the dataclass.

Here's a breakdown of why this is problematic:


-   `@dataclass(unsafe_hash=True)` generates a hash relying on mutable fields.

-   Mutable fields changing after hashing alter the object's hash.
-   This violates the requirement for constant hash values in dictionaries/sets.
-   Using such objects as dictionary keys leads to lookup failures.
-   "Unsafe" warns of potential errors due to mutability's impact.
-   It's safe only if mutable fields never change after creation.
-   `frozen=True` makes all fields immutable, ensuring safe hashing.
-   Manually defining `__hash__` with immutable fields is another safe option.
-   Avoid `unsafe_hash` if using dataclass as dictionary keys with mutable data.
-   It prioritizes convenience over safety, requiring careful usage.


----------

## **Performance Considerations**

-   **Slightly slower** than `NamedTuple` due to mutability overhead
-   **Still faster** than manual class implementations
-   **Memory usage** is higher than `NamedTuple`


----------

## **Key Takeaways**

1.  **Reduces Boilerplate** - Automatic `__init__`, `__repr__`, etc.
2.  **Type-Safe** - Requires type hints
3.  **Flexible** - Defaults, immutability, post-init processing
4.  **Pythonic** - Cleaner than manual classes or NamedTuples
5.  **Great for Data Containers** - Perfect for configs, DTOs, simple models


Dataclasses make Python **more maintainable** while keeping it **clean and readable**. They're now the **recommended way** to create data-oriented classes in modern Python. 🚀

