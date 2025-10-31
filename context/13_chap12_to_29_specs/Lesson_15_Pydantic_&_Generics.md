# Lesson 15 Pydantic & Generics

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>




# **Pydantic Tutorial for Beginners: A Complete Guide**

Pydantic is a **Python library** for **data validation and settings management** using Python type hints. It ensures your data is always in the correct format, making it perfect for:  
✅ **API request/response validation**  
✅ **Config management**  
✅ **Data parsing & serialization**

----------

## **📌 Table of Contents**

1.  Installation
2.  Basic Model
3.  Field Validation
4.  Nested Models
5.  JSON Serialization
6.  Settings Management
7.  Real-World Example

----------

## **1️⃣ Installation** <a name="installation"></a>

```python
%pip -q install pydantic pydantic_settings pydantic[email]
```

**Output:**
```
[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/313.6 kB[0m [31m?[0m eta [36m-:--:--[0m[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m313.6/313.6 kB[0m [31m12.7 MB/s[0m eta [36m0:00:00[0m
[?25h
```


----------

## **2️⃣ Basic Model** <a name="basic-model"></a>

### **Create a Simple Model**

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool = True  # Default value
```

### **Usage**

```python
user = User(name="Alice", age=25)
print(user.name)  # Output: "Alice"
print(user.age)   # Output: 25
print(user.is_active)  # Output: True (default)
```

**Output:**
```
Alice
25
True
```

### **Automatic Validation**

```python
# ❌ Error (age must be an int)
user = User(name="Bob", age="twenty")  # Raises ValidationError
```

**Error:**
```
ValidationError: 1 validation error for User
age
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='twenty', input_type=str]
    For further information visit https://errors.pydantic.dev/2.10/v/int_parsing
---------------------------------------------------------------------------
ValidationError                           Traceback (most recent call last)
<ipython-input-19-c9009add0fd0> in <cell line: 0>()
      1 # ❌ Error (age must be an int)
----> 2 user = User(name="Bob", age="twenty")  # Raises ValidationError

/usr/local/lib/python3.11/dist-packages/pydantic/main.py in __init__(self, **data)
    212         # `__tracebackhide__` tells pytest and some other tools to omit this function from tracebacks
    213         __tracebackhide__ = True
--> 214         validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
    215         if self is not validated_self:
    216             warnings.warn(

ValidationError: 1 validation error for User
age
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='twenty', input_type=str]
    For further information visit https://errors.pydantic.dev/2.10/v/int_parsing
```


----------

## **3️⃣ Field Validation** <a name="validation"></a>

### **Using `Field` for Extra Rules**

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)  # Must be > 0
    category: str = Field(min_length=3, max_length=50)
```

### **Example**

```python
# ✅ Valid
product = Product(name="Laptop", price=999.99, category="Electronics")
print(product.model_dump_json)
```

**Output:**
```
<bound method BaseModel.model_dump_json of Product(name='Laptop', price=999.99, category='Electronics')>
```

```python
# ❌ Invalid (price <= 0)
product = Product(name="Phone", price=0, category="Gadgets")  # Raises error
```

**Error:**
```
ValidationError: 1 validation error for Product
price
  Input should be greater than 0 [type=greater_than, input_value=0, input_type=int]
    For further information visit https://errors.pydantic.dev/2.10/v/greater_than
---------------------------------------------------------------------------
ValidationError                           Traceback (most recent call last)
<ipython-input-22-4f1578bd44af> in <cell line: 0>()
      1 # ❌ Invalid (price <= 0)
----> 2 product = Product(name="Phone", price=0, category="Gadgets")  # Raises error

/usr/local/lib/python3.11/dist-packages/pydantic/main.py in __init__(self, **data)
    212         # `__tracebackhide__` tells pytest and some other tools to omit this function from tracebacks
    213         __tracebackhide__ = True
--> 214         validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
    215         if self is not validated_self:
    216             warnings.warn(

ValidationError: 1 validation error for Product
price
  Input should be greater than 0 [type=greater_than, input_value=0, input_type=int]
    For further information visit https://errors.pydantic.dev/2.10/v/greater_than
```


----------

## **4️⃣ Nested Models** <a name="nested-models"></a>

```python
class Address(BaseModel):
    city: str
    country: str

class UserProfile(BaseModel):
    name: str
    address: Address  # Nested model
```

### **Usage**

```python
profile = UserProfile(
    name="Alice",
    address={"city": "New York", "country": "USA"}  # Auto-converted to Address
)
print(profile.address.city)  # Output: "New York"
```

**Output:**
```
New York
```


----------

## **5️⃣ JSON Serialization** <a name="json"></a>

### **Convert Model ↔ JSON**

```python
user = User(name="Bob", age=30)

# Model → JSON
user_json = user.model_dump_json()
print(user_json)
# Output: '{"name":"Bob","age":30,"is_active":true}'

# JSON → Model
new_user = User.model_validate_json('{"name":"Charlie","age":40}')
print(new_user.name)  # Output: "Charlie"
print(type(new_user))  # Output: <class 'int'>
```

**Output:**
```
{"name":"Bob","age":30,"is_active":true}
Charlie
<class '__main__.User'>
```


----------

## **6️⃣ Settings Management** <a name="settings"></a>

Pydantic is great for **config files** (e.g., `.env` files). `Use VSCode`

### **Example: Environment Variables**

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str = "123123" # run in VSCode without default value
    debug: bool = False

    class Config:
        env_file = ".env"  # Load from .env file
```

### **.env File**

```bash
API_KEY=my-secret-key
DEBUG=True
```

### **Usage**

```python
settings = Settings()
print(settings)  # Output: "my-secret-key"
```

**Output:**
```
api_key='123123' debug=False
```


----------

## **7️⃣ Using Validators for Custom Rules**

You can define **custom validation logic** using `@validator`.

### **🔹 Example: Validate Email Format**

```python
from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr

    @field_validator("name")
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty!")
        return value

# Valid user
user = User(name="David", email="david@example.com")
print(user)
```

**Output:**
```
name='David' email='david@example.com'
```

```python
# Invalid user (empty name)
User(name=" ", email="invalid_email")
```

**Error:**
```
ValidationError: 2 validation errors for User
name
  Value error, Name cannot be empty! [type=value_error, input_value=' ', input_type=str]
    For further information visit https://errors.pydantic.dev/2.10/v/value_error
email
  value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='invalid_email', input_type=str]
---------------------------------------------------------------------------
ValidationError                           Traceback (most recent call last)
<ipython-input-30-c436e91d6923> in <cell line: 0>()
      1 # Invalid user (empty name)
----> 2 User(name=" ", email="invalid_email")

/usr/local/lib/python3.11/dist-packages/pydantic/main.py in __init__(self, **data)
    212         # `__tracebackhide__` tells pytest and some other tools to omit this function from tracebacks
    213         __tracebackhide__ = True
--> 214         validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
    215         if self is not validated_self:
    216             warnings.warn(

ValidationError: 2 validation errors for User
name
  Value error, Name cannot be empty! [type=value_error, input_value=' ', input_type=str]
    For further information visit https://errors.pydantic.dev/2.10/v/value_error
email
  value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='invalid_email', input_type=str]
```

----------

## **🔥 Recap: Key Pydantic Features**

| Feature            | Example                          |   |   |
|--------------------|----------------------------------|---|---|
| Type Validation    | age: int → Fails if age="twenty" |   |   |
| Default Values     | is_active: bool = True           |   |   |
| Nested Models      | address: Address                 |   |   |
| JSON Serialization | .model_dump_json()               |   |   |
| Env Config         | class Settings(BaseSettings)     |   |   |


----------

## **🎯 Conclusion**

Pydantic ensures **your data is always correct** while keeping code clean and readable. It’s a must-have for **APIs, configs, and data pipelines**!

📌 **Key Takeaway:**  
**Pydantic = Type hints + Validation + Serialization** 🚀



---


# **Generics in Python 3.12: A Complete Beginner's Guide**

Python 3.12 introduced several improvements to generics, making them more powerful and easier to use. This tutorial covers everything you need to know about generics in Python 3.12, with clear examples and practical applications.

Generics in Python 3.12 are part of the type hinting system, which has evolved significantly since Python 3.5 introduced type annotations via PEP 484. Generics allow developers to write reusable, type-safe code by defining classes, functions, or data structures that can operate on different types while maintaining static type checking. With Python 3.12, generics have been refined with improvements in syntax and runtime behavior, building on earlier enhancements like those in PEP 695 (introduced in Python 3.12). Let’s break this down in depth.

## **Table of Contents**

1.  What Are Generics?
2.  New Features in Python 3.12
3.  Basic Generic Functions
4.  Generic Classes
5.  TypeVar and Bounds
6.  Generic Collections
7.  Overloading with `@overload`
8.  Real-World Examples
9.  Best Practices

----------


## **1. What Are Generics?** <a name="what-are-generics"></a>

Generics enable you to parameterize types, meaning you can create a blueprint for a class or function that works with any type (or a constrained set of types) specified by the user of that code. For example, a generic List can hold integers, strings, or custom objects, and the type checker ensures consistency without needing separate implementations for each type.

In Python, generics are primarily used with the typing module (e.g., List, Dict, Optional) and, starting with Python 3.12, with new syntax from PEP 695, such as type statements and TypeVar refinements. They don’t change runtime behavior directly—Python remains dynamically typed—but they enhance static analysis tools like mypy, pyright, or IDEs.

## **2. Why Are Generics Needed?**

1.  **Code Reusability**: Without generics, you’d need to write duplicate code for different types. For instance, a function to process a list of integers and a list of strings would require two separate implementations. Generics let you write one function that works for any type.
2.  **Type Safety**: Generics allow static type checkers to catch errors before runtime. For example, if a function expects a List[int] but receives a List[str], the type checker flags it.
3.  **Abstraction**: They enable abstract data structures (e.g., stacks, queues, or trees) that can work with any data type, making libraries more flexible and maintainable.
4.  **Interoperability**: Modern Python codebases often integrate with typed libraries or frameworks (e.g., FastAPI, Pydantic). Generics ensure compatibility and clarity in such ecosystems.

## **3. How Do Generics Work in Python 3.12?**

Python 3.12 introduces a cleaner syntax for generics via PEP 695, reducing reliance on the typing module’s older constructs. Here’s how they’re implemented:


❌ Example: A Function Without Generics

```python
def double(value):
    return value * 2

print(double(5))     # ✅ Works (int → 10)
print(double("Hi"))  # ✅ Works (str → 'HiHi')
print(double([1, 2])) # ✅ Works ([1,2,1,2])
```

**Output:**
```
10
HiHi
[1, 2, 1, 2]
```

📌 **Issue:**

-   The function accepts **any data type**.
    
-   While **multiplication works for `int` and `str`**, unintended behavior can happen for **custom types**.
    
-   There’s **no type safety**, so errors may **only appear at runtime**.
    

### **🔹 Solution: Use Generics for Type Safety**

Generics allow **type flexibility** while ensuring **type consistency**.


## **jupyter notebook use:**


`This automatically runs mypy on every cell before it is executed.`

This is just for convenience to show the mypy output for this talk.

```python
if "google.colab" in str(get_ipython()):
    !pip install nb-mypy -qqq
%load_ext nb_mypy
```

**Output:**
```
  Installing build dependencies ... [?25l[?25hdone
  Getting requirements to build wheel ... [?25l[?25hdone
  Preparing metadata (pyproject.toml) ... [?25l[?25hdone
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m826.7/826.7 kB[0m [31m16.4 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m12.3/12.3 MB[0m [31m62.7 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.6/1.6 MB[0m [31m36.5 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m85.4/85.4 kB[0m [31m2.0 MB/s[0m eta [36m0:00:00[0m
[?25h  Building wheel for nb-mypy (pyproject.toml) ... [?25l[?25hdone
[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
google-colab 1.0.0 requires ipython==7.34.0, but you have ipython 8.34.0 which is incompatible.[0m[31m
[0m
```

**Output:**
```
Version 1.0.5
INFO:nb-mypy:Version 1.0.5
```

```python
from typing import TypeVar

T = TypeVar("T", int, float)  # Restrict to int & float

def double(value: T) -> T:
    return value * 2

print(double(5))     # ✅ Works (int → 10)
print(double(3.14))  # ✅ Works (float → 6.28)
print(double("Hi"))  # ❌ TypeError: str not allowed
```

**Output:**
```
<cell>10: error: Value of type variable "T" of "double" cannot be "str"  [type-var]
ERROR:nb-mypy:<cell>10: error: Value of type variable "T" of "double" cannot be "str"  [type-var]
```

**Output:**
```
10
6.28
HiHi
```

```python
%%writefile test_mypy.py

def multiply(x: float | int, y: float | int) -> float  | int: #Create the data type according to the values given float or int
    return x * y

result: float = multiply(3, 4.5) #Change the value to string data tyoe to see error when validating with mypy
print(type(result)," = ", result)
```

**Output:**
```
Overwriting test_mypy.py
```

```python
!mypy test_mypy.py
```

**Output:**
```
[1m[32mSuccess: no issues found in 1 source file[m
```

## **For VSCode Use:**

**A - By Command:**
  1.  Open terminal window type 'uv add mypy' or 'pip install mypy'
  2.  Validate class typing by using command in terminal window 'mypy class_name.py'

**B - By Installing an Extension:**
  1.  Click on extensions icon on the left side search 'Mypy Type Checker' by Microsoft then install it.
  2.  Now the IDE it self is capable to figure out type error in source code while you are writing Python code.


## **Example With Generics**

```python
from typing import TypeVar, List

T = TypeVar('T', bound=int | str)  # Declare a generic type

def first_item(items: List[T]) -> T:  # Returns the correct type
    return items[0]

print(first_item([1, 2, 3]))       # Output: int
print(first_item(["a", "b"]))      # Output: str
#print(first_item([1.0, 2.0, 3.0])) # Uncomment to see error
```

**Output:**
```
1
a
```

----------

## **4. New Features in Python 3.12** <a name="new-features"></a>

| Feature               | Description                            | Example                              |   |
|-----------------------|----------------------------------------|--------------------------------------|---|
| Simpler Syntax        | No need for from typing import TypeVar | def func[T](): ...                   |   |
| Type Parameter Lists  | Declare generics inline                | class Stack[T]: ...                  |   |
| TypeVar Improvements  | Easier bounds and constraints          | T = TypeVar('T', bound=int)          |   |
| Better Error Messages | More readable type errors              | TypeError: Expected 'int', got 'str' |

# ⚠ **<font color="red">Important Note:</font>**

**In order to use new generic type syntax introduced in Python 3.12 we need to upgrade Python enviroment of Google Colab Notebook, below are the steps how to do that.**

```python
%%python --version
```

**Output:**
```
Python 3.12.9
```

## [**Step-by-Step Guide to Install Python 3.12 in Google Colab**](https://saturncloud.io/blog/how-to-update-google-colabs-python-version/)

```python
# Install python 3.12
!apt-get install python3.12
```

**Output:**
```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpython3.12-stdlib
Suggested packages:
  python3.12-venv
The following NEW packages will be installed:
  libpython3.12-stdlib python3.12
0 upgraded, 2 newly installed, 0 to remove and 30 not upgraded.
Need to get 5,418 kB of archives.
After this operation, 22.6 MB of additional disk space will be used.
Get:1 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 libpython3.12-stdlib amd64 3.12.9-1+jammy1 [2,892 kB]
Get:2 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 python3.12 amd64 3.12.9-1+jammy1 [2,526 kB]
Fetched 5,418 kB in 9s (612 kB/s)
Selecting previously unselected package libpython3.12-stdlib:amd64.
(Reading database ... 126210 files and directories currently installed.)
Preparing to unpack .../libpython3.12-stdlib_3.12.9-1+jammy1_amd64.deb ...
Unpacking libpython3.12-stdlib:amd64 (3.12.9-1+jammy1) ...
Selecting previously unselected package python3.12.
Preparing to unpack .../python3.12_3.12.9-1+jammy1_amd64.deb ...
Unpacking python3.12 (3.12.9-1+jammy1) ...
Setting up libpython3.12-stdlib:amd64 (3.12.9-1+jammy1) ...
Setting up python3.12 (3.12.9-1+jammy1) ...
Processing triggers for mailcap (3.70+nmu1ubuntu1) ...
Processing triggers for man-db (2.10.2-1) ...
```

```python
# Change default python3 to 3.12
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2

# Confirm version
!python3 --version
# Python 3.12.1
```

**Output:**
```
update-alternatives: using /usr/bin/python3.12 to provide /usr/bin/python3 (python3) in auto mode
Python 3.12.9
```

```python
!python3.12 --version
```

**Output:**
```
Python 3.12.9
```



---



---


## **<font color="red">Problem:</font>**


Google Colab's Python environment might not be fully configured to recognize the new generic type syntax introduced in Python 3.12, despite showing the correct version. This can lead to Syntax errors when you use new Syntax e.g.`swap[T]`.

## **<font color="Green">Solution:</font>**

While Colab might indicate it's running Python 3.12, it's actually still referencing the old environment files in the background where generic type Syntax is invalid.

<font color='orange' size=5>**To solve this issue we will use VSCode, the GitHub link for the new Generic Syntax is here.** </font>

[**Generic: Source Code**](https://github.com/panaversity/learn-modern-ai-python/tree/main/00_python_colab/Lesson_Source_Code/generics)


---


---





## **5. Basic Generic Functions** <a name="generic-functions"></a>

### **Example: Swap Two Values** <font color=red>**(Colab ERROR: Not recognizing Python Version 3.12)**</font>

```python
def swap[T](a: T, b: T) -> tuple[T, T]:
    return b, a

x, y = swap(10, 20)    # ✅ (int, int)
a, b = swap("A", "B")  # ✅ (str, str)
```

**Error:**
```
SyntaxError: expected '(' (<ipython-input-1-3ea64f7ec5cd>, line 1)
  File "<ipython-input-1-3ea64f7ec5cd>", line 1
    def swap[T](a: T, b: T) -> tuple[T, T]:
            ^
SyntaxError: expected '('

```


### **Example: Swap Two Values**




```python
def swap[T](a: T, b: T) -> tuple[T, T]:
    return b, a

x, y = swap(10, 20)    # ✅ (int, int)
a, b = swap("A", "B")  # ✅ (str, str)

```

### **Multiple Generic Types**



```python
def get_value[K, V](d: dict[K, V], key: K) -> V:
    return d[key]

person = {"name": "Alice", "age": 30}
print(get_value(person, "name"))  # Returns "Alice" (str)
```

## **6. Generic Classes** <a name="generic-classes"></a>

### **Example: Stack Data Structure**


```python
class Stack[T]:
    def __init__(self):
        self.items: list[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()

# Usage
int_stack = Stack[int]()
int_stack.push(10)
print(int_stack.pop())  # ✅ Returns int

str_stack = Stack[str]()
str_stack.push("hello")
print(str_stack.pop())  # ✅ Returns str

```

----------

## **7. TypeVar and Bounds** <a name="typevar"></a>

### **Restricting Types (`bound=`)**

```python
from typing import TypeVar

Numeric = TypeVar('Numeric', bound=int | float)  # Only int or float

def add(a: Numeric, b: Numeric) -> Numeric:
    return a + b

print(add(5, 10))      # ✅ Valid
print(add(3.14, 2.71)) # ✅ Valid
print(add("a", "b"))   # ❌ Error

```

### **Upper Bounds (Inheritance)**


```python
from typing import TypeVar

class Animal: ...

class Dog(Animal): ...

A = TypeVar('A', bound=Animal)  # Must be Animal or subclass

def make_sound(animal: A) -> None:
    print("Sound!")

make_sound(Dog())  # ✅ Valid

```

----------

## **8. Generic Collections** <a name="generic-collections"></a>

Python 3.12 supports **inline generic syntax** for collections:

| Collection | Old Syntax | New Syntax (Python 3.12) |   |
|------------|------------|--------------------------|---|
| list       | List[T]    | list[T]                  |   |
| dict       | Dict[K, V] | dict[K, V]               |   |
| set        | Set[T]     | set[T]                   |   |


### **Example**


```python
names: list[str] = ["Alice", "Bob"]
ages: dict[str, int] = {"Alice": 25, "Bob": 30}
unique: set[int] = {1, 2, 3}

```

----------

## **9. Overloading with `@overload`** <a name="overloading"></a>

Define **multiple function signatures** for different input types:


**How it Works:**

1.  **Multiple Signatures:** You define multiple function signatures using `@overload`. These signatures specify the expected input types and return types for different cases.

2.  **Implementation:** You provide a single, general implementation of the function. This implementation typically uses type hints that are compatible with all the overloaded signatures.

3.  **Type Checker's Role:** The type checker uses the overloaded signatures to determine the correct return type based on the input types. The implementation is used at runtime.

```python
from typing import overload

@overload
def double(x: int) -> int: ...
@overload
def double(x: str) -> str: ...

def double(x: int | str) -> int | str:
    return x * 2

print(double(5))     # Returns 10 (int)
print(double("A"))   # Returns "AA" (str)

```

----------

## **10. Real-World Examples** <a name="real-world-examples"></a>

### **Example 1: API Response Wrapper**



```python
class APIResponse[T, U]:
    def __init__(self, data: T, status: U):
        self.data = data
        self.status = status

# Usage
response = APIResponse[str, int]("Success!", 200)
print(response.data)  # Output: "Success!"

response2 = APIResponse[bool, float](True, 0.200)
print(response2.data)  # Output: True


```

### **Example 2: Caching System**


```python
class Cache[K, V]:
    def __init__(self):
        self.store: dict[K, V] = {}
    
    def set(self, key: K, value: V) -> None:
        self.store[key] = value
    
    def get(self, key: K) -> V:
        return self.store[key]

# Usage
cache = Cache[str, int]()
cache.set("count", 10)
print(cache.get("count"))  # Output: 10

```

----------

## **11`. Best Practices** <a name="best-practices"></a>

✅ **Use inline generics (`def func[T]()`) for simplicity**  
✅ **Apply `bound=` when restricting types**  
✅ **Prefer `list[T]` over `List[T]`**  
❌ **Avoid `Any` when generics can be used**

----------

## **Final Thoughts**

Python 3.12 makes generics:  
✔ **Easier to write**  
✔ **More readable**  
✔ **Better for large codebases**

