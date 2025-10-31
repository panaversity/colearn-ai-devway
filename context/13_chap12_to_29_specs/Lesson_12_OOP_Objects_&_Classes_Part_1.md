# Lesson 12 OOP Objects & Classes Part 1

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>


# OOPS WHAT'S THAT...

She started working as MIT Programmer in 1959. Margaret Hamilton became the led programmer of this project. She used to spent hours in the lab writing code and making it error free. **She often brought her 4 years old daughter Lauren to work at night and on weekends**.

This Code was written so perfectly that no bugs were founded in code at the time of future Apollo missions.
In 2003, NASA honored her achievements with the largest financial award. She also got the Presidential Medal of Freedom.

**Lesson for us: America is America because of these kind of hard working people, with persistence and dedication we can also achieve greatness, whether it's landing on the moon, exploring Mars, or tackling other seemingly insurmountable (too great to be overcome) challenges.**

# **Thanks God! we have OOP, but what is OOP?**

# **1.  What is OOP?**
**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software design around **objects and classes**, rather than functions and logic. An object is an instance of a class, which is a blueprint for creating objects. **OOP focuses on modeling real-world entities and their relationships in a more intuitive and structured way.**

For example, if you’re building a car simulation, you might create a Car class. Each car in your program would be an object (instance) of that class, with attributes like color, speed, and model, and behaviors like accelerate() or brake().

# **Why use OOP?**

1.  **Modularity**: OOP allows you to break down complex problems into smaller, reusable components (objects).

2.  **Reusability**: Classes and objects can be reused across different parts of a program or in entirely different programs.

3.  **Maintainability**: Code is easier to maintain and update because it’s organized into logical units.

4.  **Scalability**: OOP makes it easier to scale and extend programs as requirements grow.

5.  **Real-world modeling**: OOP closely mirrors real-world entities, making it easier to understand and design systems.

# **Key Principles of OOP**
OOP is built on four fundamental principles:

## 1. **Encapsulation:**

Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit (a class). It also restricts direct access to some of an object’s components, which is a way of preventing unintended interference.
Example:

```python
class Car:
    def __init__(self, color, speed):
        self.color = color  # Public attribute
        self.__speed = speed  # Private attribute (encapsulated)

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed
```

## **Test Case:**

```python
car = Car("red", 0)  # Provide values for color and speed
print("Current speed: ", car.get_speed()) # Call the get_speed method

# speed up bro
for i in range(10):
    car.accelerate()

print("Speed after acceleration: ", car.get_speed()) # Call the get_speed method
```

**Output:**
```
Current speed:  0
Speed after acceleration:  100
```

# 2.  **Abstraction:**
Abstraction means hiding complex implementation details and exposing only the necessary features of an object. It helps reduce complexity and allows the programmer to focus on interactions at a higher level.

Example:

You don’t need to know how a car’s engine works to drive it. Similarly, a Car class might expose a drive() method without revealing the internal mechanics.

```python
# Define a Car class with abstraction and idle stop engine feature
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._engine_status = False
        self._idling_time = 0
        self._traffic_signal = None

    # Expose a drive method without revealing internal mechanics
    def drive(self):
        if self._engine_status and self._traffic_signal == "green":
            print(f"You are driving a {self.brand} {self.model}.")
        elif self._traffic_signal == "red":
            print(f"You stopped at the red light in a {self.brand} {self.model}.")
            self._idle_stop_engine()
        else:
            self._start_engine()
            print(f"You are driving a {self.brand} {self.model}.")

    # Expose a stop method to stop the car
    def stop(self):
        if self._engine_status:
            print(f"You stopped the {self.brand} {self.model}.")
            self._idle_stop_engine()
        else:
            print(f"The {self.brand} {self.model} is already stopped.")

    # Expose a set_traffic_signal method to set the traffic signal
    def set_traffic_signal(self, signal):
        self._traffic_signal = signal
        if signal == "red":
            print(f"Traffic signal turned red. You stopped in a {self.brand} {self.model}.")
            self._idle_stop_engine()
        elif signal == "green":
            print(f"Traffic signal turned green. You can drive your {self.brand} {self.model}.")
            if not self._engine_status:
                self._start_engine()

    # Internal method to start the engine (hidden from user)
    def _start_engine(self):
        self._engine_status = True
        self._idling_time = 0
        print("Engine started.")

    # Internal method to stop the engine if idling for 5 seconds (hidden from user)
    def _idle_stop_engine(self):
        import time
        print("Engine is idling...")
        for i in range(5):
            print(f"Idling time: {i+1} seconds")
            time.sleep(1)
            self._idling_time += 1
        if self._idling_time >= 5:
            self._engine_status = False
            print("Engine stopped (idle stop) to save fule.")

```

```python
# Create a Car object and use the methods
my_car = Car("Toyota", "Camry")
my_car.set_traffic_signal("green")
my_car.drive()
my_car.set_traffic_signal("red")
my_car.set_traffic_signal("green")
my_car.drive()
```

**Output:**
```
Traffic signal turned green. You can drive your Toyota Camry.
Engine started.
You are driving a Toyota Camry.
Traffic signal turned red. You stopped in a Toyota Camry.
Engine is idling...
Idling time: 1 seconds
Idling time: 2 seconds
Idling time: 3 seconds
Idling time: 4 seconds
Idling time: 5 seconds
Engine stopped (idle stop) to save fule.
Traffic signal turned green. You can drive your Toyota Camry.
Engine started.
You are driving a Toyota Camry.
Engine started.
```

## **How Abstraction Works in this Example:**

1. The `Car` class exposes `drive`, `stop`, and `set_traffic_signal` methods, which are the only methods that the user needs to interact with.

2. The internal mechanics of the car (e.g., starting and stopping the engine, idling time, and traffic signal logic) are hidden from the user and are handled by the `_start_engine` and `_idle_stop_engine` methods.
3. The user doesn't need to know how the engine works or how the idle stop feature is implemented; they just need to call the `drive`, `stop`, and `set_traffic_signal` methods.

This example demonstrates abstraction by hiding the complex implementation details (engine status, idling time, and traffic signal logic) and exposing only the necessary features (driving, stopping, and responding to traffic signals).

```python
class ShoppingMall:
  def basement_parking():
    my_car = Car("Toyota", "Camry")
    my_car._start_engine()

  basement_parking();
```

**Output:**
```
Engine started.
```

**Calling `_start_engine` Method Directly**

In Python, methods that start with an underscore (`_`) are considered private or internal methods. This means they are not intended to be called directly from outside the class.

However, Python does not enforce this rule strictly, and you can still call these methods directly if you want to.


**Why is it not recommended to call `_start_engine` directly?**

1. **Encapsulation**: By making `_start_engine` a private method, we are encapsulating the internal implementation details of the `Car` class. This means that users of the class should not need to know how the engine is started, only that it is started when the `drive` method is called.

2. **Abstraction**: Calling `_start_engine` directly breaks the abstraction of the `Car` class. Users of the class should only interact with the public methods (`drive`, `stop`, etc.), not the internal implementation details.
3. **Future changes**: If the internal implementation of the `Car` class changes, the `_start_engine` method may no longer be needed or may need to be modified. By calling it directly, you are tightly coupling your code to the internal implementation of the class, which can make it harder to maintain.


```python
class BMW(Car):
  def __init__(self, brand, model):
    super().__init__(brand, model)

  def start_engine(self):
    self._start_engine() # Car class private method is visible in child class

  def _start_engine(self): # Overrides the parent method with the same name
    print("BMW engine started") # Even you can override it

bmw: BMW = BMW("BMW", "i5");
bmw.start_engine();

```

**Output:**
```
BMW engine started
```

# 3.  **Inheritance:**
Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reuse and establishes a hierarchical relationship between classes.
Example:

```python
class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        print("Driving Speed = ", self.speed)

    def accelerate(self):
        self.speed += 10


class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, color, speed):
        super().__init__(color, speed)


class Truck(Vehicle):  # Truck inherits from Vehicle
    def __init__(self, color, speed):
        super().__init__(color, speed)
```

## **Test Case:**

```python
car = Car("red", 120)
truck = Truck("blue", 80)

car.drive()
truck.drive()
```

**Output:**
```
Driving Speed =  120
Driving Speed =  80
```

Student's task: accelerate car upto 180 Kph

```python
for i in range(6):
  car.accelerate()

car.drive()
# check truck speed
truck.drive()
```

**Output:**
```
Driving Speed =  360
Driving Speed =  80
```

# 4.  **Polymorphism:**
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables flexibility and dynamic behavior in your code.

Example:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> None:
        pass

class Dog(Animal):
    def speak(self) -> None:
        print(type(self), ":  Woof!")

class Cat(Animal):
    def speak(self) -> None:
        print(type(self), ":  Meow!")

def animal_sound(animal: Animal) -> None:
    animal.speak()

dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
```

**Output:**
```
<class '__main__.Dog'> :  Woof!
<class '__main__.Cat'> :  Meow!
```

# **OOP vs. Procedural Programming**

| Aspect              | OOP                                         | Procedural Programming                                 |
|---------------------|---------------------------------------------|--------------------------------------------------------|
| Focus               | Objects and their interactions              | Functions and procedures                               |
| Data and Behavior   | Bundled together in classes and objects     | Separated into functions and data                      |
| Reusability         | High (through inheritance and polymorphism) | Limited (functions can be reused, but less structured) |
| Complexity          | Easier to manage for large, complex systems | Can become unwieldy for large systems                  |
| Real-world Modeling | More intuitive and natural                  | Less intuitive for modeling real-world entities        |
|                     |                                             |                                                        |

## **Conclusion**

Object-Oriented Programming is a powerful paradigm that helps you write clean, modular, and maintainable code. By mastering encapsulation, abstraction, inheritance, and polymorphism, you’ll be well-equipped to tackle complex programming challenges. Whether you’re building a small script or a large-scale application, OOP is an essential tool in your programming toolkit.

Happy coding! 🚀

# **2.  Basics of Classes and Objects**

In this section, we’ll dive into the foundational concepts of **classes** and **objects** in Python. These are the building blocks of Object-Oriented Programming (OOP), and understanding them is crucial to writing effective and organized code.

# **What is a Class?**

A class is a blueprint or template for creating objects. It defines the **attribute** (data) and **methods** (functions) that the objects created from the class will have. Think of a class as a cookie cutter, and the objects as the cookies made from it.

For example, if you’re creating a program to manage vehicles, you might define a Vehicle class with attributes like color, speed, and model, and methods like accelerate() and brake().

# **What is an Object?**

An **object** is an instance of a class. It’s a specific realization of the class, with its own unique data. For example, if Vehicle is a class, then my_car and your_car could be objects (instances) of that class, each with its own color, speed, and model.

# **Creating a Class in Python**

To create a class in Python, you use the class keyword, followed by the class name (by convention, class names use PascalCase). Here’s the basic syntax:

```python
class ClassName:
  pass
    # Class body
```

# **Defining Attributes and Methods**

- **Attributes** are variables that belong to an object. They represent the object’s state or properties.
- **Methods** are functions that belong to an object. They define the object’s behavior.

For example, in a Vehicle class, color and speed could be attributes, and accelerate() and brake() could be methods.



# **Instantiating Objects**

To create an object (instance) of a class, you call the class name like a function. This invokes the **\_\_init\_\_** method (**the constructor**) to initialize the object.

__ (double underscore)

# **The self Keyword**

The self keyword refers to the current instance of the class. It’s used to access attributes and methods of the object within the class. It’s always the first parameter of any method in a class.

# **Example: Creating a Simple Class and Object**

Let’s create a simple Vehicle class with attributes (color and speed) and methods (accelerate() and brake()).

```python
# Define the Vehicle class
class Vehicle:
    # Constructor method (called when an object is created)
    def __init__(self, color, speed):
        self.color = color  # Attribute
        self.speed = speed  # Attribute

    # Method to accelerate the vehicle
    def accelerate(self, increment):
        self.speed += increment
        print(f"Accelerating! New speed: {self.speed} km/h")

    # Method to brake the vehicle
    def brake(self, decrement):
        self.speed -= decrement
        print(f"Braking! New speed: {self.speed} km/h")

    # Method to display vehicle details
    def display(self):
        print(f"Vehicle color: {self.color}, Current speed: {self.speed} km/h")

# Create an object (instance) of the Vehicle class
my_car = Vehicle("Red", 60)

# Access attributes
print(f"My car is {my_car.color}.")  # Output: My car is Red.

# Call methods
my_car.accelerate(20)  # Output: Accelerating! New speed: 80 km/h
my_car.brake(10)       # Output: Braking! New speed: 70 km/h
my_car.display()       # Output: Vehicle color: Red, Current speed: 70 km/h
```

**Output:**
```
My car is Red.
Accelerating! New speed: 80 km/h
Braking! New speed: 70 km/h
Vehicle color: Red, Current speed: 70 km/h
```

# **Explanation of the Code**

1.  **Class Definition:**
The Vehicle class is defined with the class keyword. It has a constructor (__init__), two methods (accelerate and brake), and a method to display details (display).

2.  **Attributes**:
The color and speed attributes are initialized in the constructor using the self keyword.

3.  **Methods**:
The accelerate and brake methods modify the speed attribute, while the display method prints the current state of the object.

4.  **Object Creation:**
An object my_car is created from the Vehicle class with the color "Red" and speed 60.

5.  **Accessing Attributes and Methods:**
Attributes are accessed using dot notation (my_car.color), and methods are called using parentheses (my_car.accelerate(20)).

## **Key Takeaways**

* A **class** is a blueprint for creating objects.
* An **object** is an instance of a class.
* Attributes define the state of an object, and methods define its behavior.
* The **self** keyword is used to refer to the current instance of the class.
* Objects are created by calling the class name like a function.

This example demonstrates the basics of creating and using classes and objects in Python. As you progress, you’ll see how these concepts form the foundation of more advanced OOP techniques! 🚀

# **3.  Constructors and Destructors**

In this section, we’ll explore **constructors** and **destructors** in Python. These are special methods that are automatically called when an object is created or destroyed, respectively. Understanding these concepts is essential for managing the lifecycle of objects in your programs.

# **What is a Constructor?**

A **constructor** is a special method that is automatically called when an object of a class is created. It’s used to initialize the object’s attributes or perform any setup required for the object.

In Python, the constructor method is named __init__.

# **The \_\_init__ Method**

The \_\_init__ method is the most commonly used constructor in Python. It’s called whenever a new instance of a class is created. You can define this method to initialize the object’s attributes or perform other setup tasks.

Syntax:

```python
class ClassName:
    def __init__(self, parameters):
      pass
        # Initialization code
```

# **Parameterized Constructors**

A **parameterized constructor** takes parameters (arguments) when creating an object. These parameters are used to initialize the object’s attributes.

Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object with a parameterized constructor
person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
```

**Output:**
```
Alice
30
```

# **Default Constructors**

If you don’t define an \_\_init__ method in your class, Python provides a **default constructor** that does nothing. However, you can define an __init__ method without parameters to act as a default constructor.

Example:

```python
class Dog:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

# Create an object with a default constructor
dog1 = Dog()
print(dog1.name)  # Output: Unknown
print(dog1.age)   # Output: 0
```

**Output:**
```
Unknown
0
```

# **The \_\_del__ Method (Destructor)**

A **destructor** is a special method that is called when an object is about to be destroyed. In Python, the destructor method is named \_\_del__. It’s used to perform cleanup tasks, such as releasing resources or closing files.

Syntax:

```python
class ClassName:
    def __del__(self):
      pass
        # Cleanup code
```

## **Example: Using Constructors and Destructors**

Let’s create a Car class with a parameterized constructor and a destructor.

```python
class Car:
    # Parameterized constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"A {self.brand} {self.model} has been created.")

    # Destructor
    def __del__(self):
        print(f"The {self.brand} {self.model} has been destroyed.")

    # Method to display car details
    def display(self):
        print(f"Car: {self.brand} {self.model}")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla")

# Access attributes and call methods
print(f"My car is a {my_car.brand} {my_car.model}.")  # Output: My car is a Toyota Corolla.
my_car.display()  # Output: Car: Toyota Corolla

# Explicitly delete the object (triggers the destructor)
del my_car  # Output: The Toyota Corolla has been destroyed.
```

**Output:**
```
A Toyota Corolla has been created.
My car is a Toyota Corolla.
Car: Toyota Corolla
The Toyota Corolla has been destroyed.
```

## **Explanation of the Code**

1.  **Constructor (\_\_init__):**
The \_\_init__ method initializes the brand and model attributes of the Car class and prints a message when the object is created.

2.  **Destructor (\_\_del__):**
The \_\_del__ method prints a message when the object is destroyed. This is triggered automatically when the object goes out of scope or is explicitly deleted using the del keyword.

3.  **Object Creation:**
An object my_car is created with the brand "Toyota" and model "Corolla". The constructor is called automatically.

4.  **Object Deletion:**
The del keyword is used to explicitly delete the my_car object, which triggers the destructor.

# **Key Takeaways**

- A **constructor** (\_\_init__) is used to initialize an object when it is created.
- A **parameterized constructor** takes arguments to initialize object attributes.
- A **default constructor** is provided by Python if you don’t define an __init__ method.
A **destructor** (\_\_del__) is called when an object is about to be destroyed, and it’s used for cleanup tasks.
- The **self** keyword is used to refer to the current instance of the class.

This example demonstrates how to use constructors and destructors in Python to manage the lifecycle of objects effectively. 🚀

# **4.  Class Attributes and Instance Attributes**

In this section, we’ll explore the difference between **class attributes** and **instance attributes** in Python. Understanding these concepts is crucial for managing data in your classes and objects effectively.

| Aspect     | Class Attributes                                       | Instance Attributes                                         |
|------------|--------------------------------------------------------|-------------------------------------------------------------|
| Definition | Defined directly inside the class, outside any method. | Defined inside the constructor (__init__) or other methods. |
| Scope      | Shared among all instances of the class.               | Unique to each instance of the class.                       |
| Memory     | Stored once for the class.                             | Stored separately for each instance.                        |
| Usage      | Used for attributes common to all instances.           | Used for attributes specific to an instance.                |
|            |                                                        |                                                             

# **Accessing and Modifying Attributes**

- Class attributes can be accessed using the class name or an instance of the class.
- Instance attributes can only be accessed using an instance of the class.
- Modifying a class attribute through an instance creates a new instance attribute with the same name, shadowing the class attribute.

# **The \_\_dict__ Attribute**

Every class and instance in Python has a \_\_dict__ attribute, which is a dictionary that stores the attributes and their values. This is a useful way to inspect the attributes of a class or object.

# **Example: Working with Class and Instance Attributes**

Let’s create a Dog class with both class attributes and instance attributes to demonstrate these concepts.

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (instance attributes)
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Method to display dog details
    def display(self):
        print(f"{self.name} is {self.age} years old and is a {self.species}.")

# Create instances of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Access class attribute
print(f"Dog species: {Dog.species}")  # Output: Dog species: Canis familiaris
print(f"Buddy's species: {dog1.species}")  # Output: Buddy's species: Canis familiaris
print(f"Max's species: {dog2.species}")    # Output: Max's species: Canis familiaris

# Access instance attributes
print(f"Buddy's name: {dog1.name}")  # Output: Buddy's name: Buddy
print(f"Max's age: {dog2.age}")       # Output: Max's age: 3

# Modify class attribute (affects all instances)
Dog.species = "Canis lupus"
print(f"Buddy's species after modification: {dog1.species}")  # Output: Buddy's species after modification: Canis lupus
print(f"Max's species after modification: {dog2.species}")    # Output: Max's species after modification: Canis lupus

# Modify class attribute through an instance (creates a new instance attribute)
dog1.species = "Canis aureus"
print(f"Buddy's species after shadowing: {dog1.species}")  # Output: Buddy's species after shadowing: Canis aureus
print(f"Max's species remains: {dog2.species}")            # Output: Max's species remains: Canis lupus

# Inspect attributes using __dict__
print(f"Dog class attributes: {Dog.__dict__}")
print(f"dog1 instance attributes: {dog1.__dict__}")
print(f"dog2 instance attributes: {dog2.__dict__}")
```

**Output:**
```
Dog species: Canis familiaris
Buddy's species: Canis familiaris
Max's species: Canis familiaris
Buddy's name: Buddy
Max's age: 3
Buddy's species after modification: Canis lupus
Max's species after modification: Canis lupus
Buddy's species after shadowing: Canis aureus
Max's species remains: Canis lupus
Dog class attributes: {'__module__': '__main__', 'species': 'Canis lupus', '__init__': <function Dog.__init__ at 0x78cc0bdae0c0>, 'display': <function Dog.display at 0x78cc0bdae160>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}
dog1 instance attributes: {'name': 'Buddy', 'age': 5, 'species': 'Canis aureus'}
dog2 instance attributes: {'name': 'Max', 'age': 3}
```

## **Explanation of the Code**

1. **Class Attribute (species):**

  The species attribute is defined at the class level and is shared by all instances of the Dog class.

2. **Instance Attributes (name and age):**

  The name and age attributes are defined in the __init__ method and are unique to each instance of the Dog class.

3. **Accessing Attributes:**

  - Class attributes can be accessed using the class name (Dog.species) or an instance (dog1.species).
  - Instance attributes are accessed using an instance (dog1.name).

4. **Modifying Attributes:**

  - Modifying a class attribute through the class (Dog.species = "Canis lupus") affects all instances.
  - Modifying a class attribute through an instance (dog1.species = "Canis aureus") creates a new instance attribute, shadowing the class attribute.

5. **Inspecting Attributes with __dict__:**

  The __dict__ attribute provides a dictionary of all attributes and their values for a class or instance.

## **Key Takeaways**

- **Class attributes** are shared by all instances of a class, while **instance attributes** are unique to each instance.

- **Class attributes** can be accessed using the class name or an instance, but modifying them through an instance creates a new instance attribute.

- The **\_\_dict\_\_ attribute** is useful for inspecting the attributes of a class or object.

This example demonstrates how to work with class and instance attributes in Python effectively. 🚀

# **5.  Methods in Python Classes**

In Python, methods are functions defined within a class that operate on the class’s data. There are three types of methods in Python: **instance methods**, **class methods**, and **static methods**. Each type has a specific purpose and use case. Let’s explore them in detail.

## **1. Instance Methods**

- **Definition**: Instance methods are the most common type of methods. They operate on an instance of the class and can access and modify instance attributes.

- **First Parameter**: The first parameter is always self, which refers to the instance of the class.

- **Usage**: Used for methods that need to access or modify instance-specific data.

## **2. Class Methods (@classmethod)**

- **Definition**: Class methods operate on the class itself rather than on instances. They can access and modify class attributes.

- **First Parameter**: The first parameter is always cls, which refers to the class.
- **Decorator**: Defined using the @classmethod decorator.

- **Usage**: Used for methods that need to work with class-level data or perform operations related to the class.

## **3. Static Methods (@staticmethod)**

- **Definition**: Static methods are independent of both the class and its instances. They don’t have access to self or cls.

- **Decorator**: Defined using the @staticmethod decorator.

- **Usage**: Used for utility functions that don’t depend on class or instance data.

## **Difference Between Instance, Class, and Static Methods**

| Aspect               | Instance Methods                          | Class Methods                          | Static Methods                             |
|----------------------|-------------------------------------------|----------------------------------------|--------------------------------------------|
| First Parameter      | self (refers to the instance)             | cls (refers to the class)              | No specific parameter                      |
| Access to Attributes | Can access and modify instance attributes | Can access and modify class attributes | Cannot access instance or class attributes |
| Decorator            | None                                      | @classmethod                           | @staticmethod                              |
| Usage                | For methods that work with instance data  | For methods that work with class data  | For utility functions                      |
|                      |                                           |                                        

## **Example: Implementing Different Types of Methods**

Let’s create a Person class to demonstrate instance, class, and static methods.

```python
class Person:
    # Class attribute
    species = "Homo sapiens"

    # Constructor
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def display(self):
        print(f"{self.name} is {self.age} years old and is a {self.species}.")

    # Class method
    @classmethod
    def update_species(cls, new_species):
        cls.species = new_species
        print(f"Species updated to {cls.species}.")

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Create an instance of the Person class
person1 = Person("Alice", 25)

# Call instance method
person1.display()  # Output: Alice is 25 years old and is a Homo sapiens.

# Call class method to update species
Person.update_species("Homo sapiens sapiens")  # Output: Species updated to Homo sapiens sapiens.
person1.display()  # Output: Alice is 25 years old and is a Homo sapiens sapiens.

# Call static method to check if the person is an adult
print(f"Is Alice an adult? {Person.is_adult(person1.age)}")  # Output: Is Alice an adult? True
```

**Output:**
```
Alice is 25 years old and is a Homo sapiens.
Species updated to Homo sapiens sapiens.
Alice is 25 years old and is a Homo sapiens sapiens.
Is Alice an adult? True
```

## **Explanation of the Code**

1. **Instance Method (display):**
Operates on the instance (self) and accesses instance attributes (name and age) and the class attribute (species).

2.  **Class Method (update_species):**
Operates on the class (cls) and modifies the class attribute (species).

3.  **Static Method (is_adult):**
Doesn’t depend on the class or instance. It’s a utility function that checks if a given age is 18 or older.

## **Key Takeaways**

* **Instance methods** are used for operations on instance data.

* **Class methods** are used for operations on class-level data.

* **Static methods** are used for utility functions that don’t depend on class or instance data.

* The **self** keyword refers to the instance, and the cls keyword refers to the class.

This example demonstrates how to implement and use different types of methods in Python classes effectively. 🚀

# **6. Encapsulation**

**Encapsulation** is one of the **core principles of Object-Oriented Programming (OOP)**. It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit (a class). Encapsulation also involves restricting direct access to some of an object’s components, which is a way of preventing unintended interference and misuse of data.

## **Access Modifiers: Public, Private, and Protected**

In Python, access control is implemented using naming conventions rather than strict access modifiers like in other languages (e.g., Java or C++). Here’s how it works:

1.  **Public**:
  * Attributes and methods are accessible from anywhere.
  * No special syntax is used.
Example: name

2.  Protected:
  - Attributes and methods are intended for internal use within the class and its **subclasses**.
  - A single underscore _ is used as a prefix.
Example: _age

3.  Private:
  - Attributes and methods are accessible only within the class itself.
  - A double underscore __ is used as a prefix.
Example: __salary

## **Using _ and __ for Access Control**

  - A single underscore _ indicates that an attribute or method is protected. It’s a convention to signal that it should not be accessed directly from outside the class.
  
  - A double underscore __ indicates that an attribute or method is private. Python performs name mangling to make it harder to access from outside the class.

## **Getter and Setter Methods**

To access or modify private or protected attributes, **getter** and **setter** methods are used. These methods provide controlled access to the data, ensuring that any changes are validated or processed appropriately.

## **Example: Implementing Encapsulation in Python**

Let’s create a BankAccount class to demonstrate encapsulation using private and protected attributes, along with getter and setter methods.

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance               # Protected attribute
        self.__pin = "1234"                   # Private attribute

    # Getter method for balance
    def get_balance(self):
        return self._balance

    # Setter method for balance
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            print(f"Balance updated to {self._balance}.")
        else:
            print("Invalid amount. Balance cannot be negative.")

    # Getter method for pin (private attribute)
    def get_pin(self):
        return "Access denied. PIN is private."

    # Method to display account details
    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self._balance}")

# Create an instance of the BankAccount class
account = BankAccount("Alice", 1000)

# Access public attribute
print(f"Account Holder: {account.account_holder}")  # Output: Account Holder: Alice

# Access protected attribute (not recommended, but possible)
print(f"Balance: {account._balance}")  # Output: Balance: 1000

# Access private attribute (name mangling makes it harder)
# This will raise an AttributeError:
# print(account.__pin)

# Use getter method for private attribute
print(account.get_pin())  # Output: Access denied. PIN is private.

# Use getter and setter methods for protected attribute
print(f"Initial Balance: {account.get_balance()}")  # Output: Initial Balance: 1000
account.set_balance(1500)  # Output: Balance updated to 1500.
account.set_balance(-500)  # Output: Invalid amount. Balance cannot be negative.

# Display account details
account.display()  # Output: Account Holder: Alice, Balance: 1500
```

**Output:**
```
Account Holder: Alice
Balance: 1000
Access denied. PIN is private.
Initial Balance: 1000
Balance updated to 1500.
Invalid amount. Balance cannot be negative.
Account Holder: Alice
Balance: 1500
```

## **Explanation of the Code**

  1.  **Public Attribute (account_holder):**
Can be accessed directly from outside the class.

  2.  **Protected Attribute (_balance):**
Intended for internal use but can still be accessed directly (though not recommended). Getter and setter methods (get_balance and set_balance) are provided for controlled access.

  3.  **Private Attribute (__pin):**
Cannot be accessed directly due to name mangling. A getter method (get_pin) is provided, but it intentionally restricts access.

  4.  **Getter and Setter Methods:**
get_balance retrieves the value of the protected attribute _balance.
set_balance updates the value of _balance after validating the input.

## **Key Takeaways**

  - Encapsulation bundles data and methods into a single unit (class) and restricts direct access to some components.

  - Public attributes/methods are accessible from anywhere.

  - Protected attributes/methods are indicated by a single underscore _ and are intended for internal use.

  - Private attributes/methods are indicated by a double underscore __ and are accessible only within the class.

  - Getter and setter methods provide controlled access to protected and private attributes.
  
This example demonstrates how to implement encapsulation in Python effectively. 🚀

# **7.  Inheritance**

**Inheritance** is one of the core principles of Object-Oriented Programming (OOP). It allows a class (called a **child class** or **subclass**) to inherit attributes and methods from another class (called a **parent class** or **superclass**). This promotes code reuse and establishes a hierarchical relationship between classes.

## **Types of Inheritance**

  1.  **Single Inheritance:**

      A subclass inherits from a single superclass.

  2.  **Multiple Inheritance:**

      A subclass inherits from multiple superclasses.

## **The super() Function**
The super() function is used to call methods from the parent class. It’s particularly useful in the constructor (__init__) to initialize attributes from the parent class.

## **Method Overriding**

**Method overriding** occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The subclass method **overrides** the superclass method.

## **Example: Implementing Inheritance in**

Let’s create a hierarchy of classes to demonstrate inheritance in Python.

## **Single Inheritance**

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Create an instance of the Dog class
dog = Dog("Buddy")
print(f"{dog.name} says {dog.speak()}")  # Output: Buddy says Woof!
```

**Output:**
```
Buddy says Woof!
```

## **Multiple Inheritance**

```python
# First parent class
class Bird:
    def fly(self):
        return "Flying high!"

# Second parent class
class Fish:
    def swim(self):
        return "Swimming deep!"

# Child class (inherits from both Bird and Fish)
class FlyingFish(Bird, Fish):
    pass

# Create an instance of the FlyingFish class
flying_fish = FlyingFish()
print(flying_fish.fly())  # Output: Flying high!
print(flying_fish.swim())  # Output: Swimming deep!
```

**Output:**
```
Flying high!
Swimming deep!
```

## **Using super() and Method Overriding**

```python
# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"{self.brand} {self.model}"

# Child class (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)  # Call the parent class constructor
        self.year = year

    # Override the display method
    def display(self):
        return f"{self.brand} {self.model} ({self.year})"

# Create an instance of the Car class
car = Car("Toyota", "Corolla", 2022)
print(car.display())  # Output: Toyota Corolla (2022)
```

**Output:**
```
Toyota Corolla (2022)
```

## **Explanation of the Code**

1.  **Single Inheritance:**

  The Dog class inherits from the Animal class and overrides the speak method.

2.  **Multiple Inheritance:**
  
  The FlyingFish class inherits from both the Bird and Fish classes, gaining access to their methods.

3.  **Using super():**

  The Car class uses super() to call the constructor of the Vehicle class and extends it with an additional attribute (year).

4.  **Method Overriding:**

  The Car class overrides the display method of the Vehicle class to include the year attribute.


## **Key Takeaways**

- **Inheritance** allows a class to inherit attributes and methods from another class.

- **Single inheritance** involves one parent class and one child class.
- **Multiple inheritance** involves multiple parent classes and one child class.
- **The super() function** is used to call methods from the parent class.
- **Method overriding** allows a subclass to provide a specific implementation of a method defined in its superclass.

This example demonstrates how to implement inheritance in Python effectively. 🚀

# **8.  Polymorphism**

**Polymorphism** is one of the `core principles` of Object-Oriented Programming (OOP). It refers to the ability of different classes to be treated as instances of the same class through a common interface. In simpler terms, polymorphism allows objects of different types to be used interchangeably if they share a common behavior.

## **Types of Polymorphism in Python**

1.  **Method Overriding:**

  A subclass provides a specific implementation of a method that is already defined in its superclass.
  

2.  **Operator Overloading:**

  Customizing the behavior of operators (e.g., +, -, *, etc.) for user-defined classes using special methods like __add__, __sub__, etc.


3.  **Duck Typing:**

  Python uses duck typing, which means that the type or class of an object is determined by its behavior (methods and properties) rather than its inheritance. If an object behaves like a duck, it’s treated as a duck.

## **Example: Demonstrating Polymorphism**

Let’s create examples to demonstrate method overriding, operator overloading, and duck typing.

## **Method Overriding**

```python
# Parent class
class Animal:
    def speak(self):
        return "Animal sound"

# Child classes
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function to demonstrate polymorphism
def animal_sound(animal):
    print(animal.speak())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the function with different objects
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
```

**Output:**
```
Woof!
Meow!
```

## **Operator Overloading**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overload the str() function for printing
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Create instances of Point
p1 = Point(1, 2)
p2 = Point(3, 4)

# Use the + operator to add two points
p3 = p1 + p2
print(p3)  # Output: Point(4, 6)
```

**Output:**
```
Point(4, 6)
```

## **Duck Typing**

```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I can quack like a duck!"

# Function to demonstrate duck typing
def make_it_quack(thing):
    print(thing.quack())

# Create instances of Duck and Person
duck = Duck()
person = Person()

# Call the function with different objects
make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I can quack like a duck!
```

**Output:**
```
Quack!
I can quack like a duck!
```

## **Explanation of the Code**

1.  Method Overriding:

  The Dog and Cat classes override the speak method of the Animal class. The animal_sound function demonstrates polymorphism by accepting any object that has a speak method.

2.  Operator Overloading:

  The Point class overloads the + operator using the __add__ method. It also overrides the __str__ method to customize how the object is printed.

3.  Duck Typing:

  The make_it_quack function accepts any object that has a quack method, regardless of its class. This demonstrates Python’s duck typing philosophy.

## **Key Takeaways**

  * **Polymorphism** allows objects of different types to be treated as instances of the same class through a common interface.

  * **Method overriding** enables a subclass to provide a specific implementation of a method defined in its superclass.

  * **Operator overloading** customizes the behavior of operators for user-defined classes using special methods like __add__ and __sub__.

  * **Duck typing** in Python focuses on an object’s behavior (methods and properties) rather than its class or inheritance.

  
This example demonstrates how to implement polymorphism in Python effectively. 🚀

# **9.  Abstraction**

Abstraction helps us focus on what something does, not how it does it. Think of it like a TV remote—you press buttons without needing to know the internal circuits. In Python, we use abstract classes to create blueprints for other classes.



## **What is Abstraction?**

Abstraction simplifies complex systems by breaking them into manageable parts. For example, all vehicles (cars, bikes) must have a start() method, but each vehicle starts differently. Abstraction lets us enforce this rule without worrying about implementation details.

## **Abstract Classes and Methods**

These are "incomplete" templates you can't use directly. They:
  * Define required methods for child classes
  * Ensure consistency across related classes
  * Prevent creating objects from the abstract class itself

<br>

Using Python's abc Module

We create abstract classes using:


```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
```

## **Key components:**

1.  **ABC** makes the class abstract

2.  **@abstractmethod** marks required methods

3.  Child classes **must** implement all **abstract** **methods**

## **Example: Shape Calculator**

Let's create shapes that can calculate area:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side
```

## **How this works:**

1.  Shape is our abstract blueprint

2.  Circle and Square provide actual area calculations
3.  Trying to create Shape() directly causes an error



Abstraction acts like a parenting agreement—"All my children must do these tasks, but I don't care how they do them." This makes code more organized and prevents forgetting important methods when creating new classes.

## **Test Case:**

```python
import pytest
#import Shape, Circle, Square  # Replace with actual import path

# Test abstract class behavior
def test_cannot_instantiate_abstract_shape():
    with pytest.raises(TypeError) as error:
        Shape()
    assert "abstract" in str(error.value).lower()

# Test Circle functionality
class TestCircle:
    def test_normal_radius_area(self):
        circle = Circle(5)
        assert circle.calculate_area() == pytest.approx(78.5)  # 3.14 * 5²

    def test_zero_radius_area(self):
        assert Circle(0).calculate_area() == 0

    def test_large_radius(self):
        assert Circle(100).calculate_area() == 3.14 * 100**2

# Test Square functionality
class TestSquare:
    def test_standard_square(self):
        square = Square(4)
        assert square.calculate_area() == 16  # 4²

    def test_zero_size_square(self):
        assert Square(0).calculate_area() == 0

    def test_negative_side(self):
        """Demonstrates handling of negative values (current code allows this)"""
        assert Square(-3).calculate_area() == 9  # (-3)² = 9
```

## **Let's call the test case**

```python
circle = Circle(5)
print("circle.calculate_area(): ",circle.calculate_area())

square = Square(4)
print("square.calculate_area(): ", square.calculate_area())
```

**Output:**
```
circle.calculate_area():  78.5
square.calculate_area():  16
```

## **Key test components:**

1.  **Abstract class protection:** Ensures Shape can't be instantiated directly14

2.  **Core calculations:** Verifies area formulas using both normal and edge cases

3.  **Behavior verification:** Checks mathematical properties (e.g., negative values squared become positive)

# **10. The object class**


In Python, the object class is the most base type, from which all other classes are derived. Every class in Python, whether built-in or user-defined, directly or indirectly inherits from object. This means that all classes in Python are part of a single inheritance tree with object at the root.

## **Key Characteristics of the object Class:**

**1.  Base Class:**

  - object is the root of the class hierarchy. If you define a class without specifying a base class, it implicitly inherits from object.

**2.  Default Methods:**

  - The object class provides default implementations for several important methods that are inherited by all other classes.

**3.  Universal Behavior:**

  - Since all classes inherit from object, methods and attributes defined in object are available to all objects in Python.

In Python, the object class is the root of the class hierarchy and provides default implementations for many fundamental methods. While you cannot directly inspect the internal structure of the object class (as it is implemented in C in CPython), you can explore its methods and attributes using built-in functions like dir() and help().

Here’s an overview of the structure and key methods provided by the object class:


### **Key Methods of the `object` Class**

The `object` class defines several special methods (also called "dunder" methods because they are surrounded by double underscores, e.g., `__init__`). These methods are inherited by all other classes unless overridden.

#### 1. **Initialization and Representation**

-   `__init__(self)`: The default constructor. It does nothing but can be overridden in derived classes.
-   `__new__(cls)`: The method responsible for creating a new instance of a class. It is rarely overridden unless you need custom instance creation behavior.
-   `__repr__(self)`: Returns a string representation of the object, typically used for debugging. The default implementation returns something like `<ClassName object at 0x...>`.
-   `__str__(self)`: Returns a string representation of the object, typically used for user-friendly output. The default implementation calls `__repr__`.

#### 2. **Comparison and Hashing**

-   `__eq__(self, other)`: Defines behavior for the `==` operator. The default implementation checks if two objects are the same instance (`self is other`).
-   `__hash__(self)`: Returns a hash value for the object. The default implementation uses the object's memory address.
-   `__ne__(self, other)`: Defines behavior for the `!=` operator. The default implementation is the negation of `__eq__`.

#### 3. **Attribute Access**

-   `__getattribute__(self, name)`: Handles attribute access. It is called whenever an attribute is accessed (e.g., `obj.attr`).
-   `__setattr__(self, name, value)`: Handles attribute assignment. It is called whenever an attribute is assigned (e.g., `obj.attr = value`).
-   `__delattr__(self, name)`: Handles attribute deletion. It is called whenever an attribute is deleted (e.g., `del obj.attr`).

#### 4. **Class and Type Information**

-   `__class__`: A special attribute that refers to the class of the object.
-   `__dict__`: A dictionary containing the object's attributes.

#### 5. **Other Methods**

-   `__dir__(self)`: Returns a list of valid attributes for the object. The default implementation includes all attributes in `__dict__` and those defined in the class.

----------

### **Exploring the `object` Class**

You can use `dir()` and `help()` to explore the methods and attributes of the `object` class:

```python
# List all attributes and methods of the object class
print(dir(object))

```

**Output:**
```
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

```python
# Get detailed help on the object class
help(object)
```

**Output:**
```
Help on class object in module builtins:

class object
 |  The base class of the class hierarchy.
 |  
 |  When called, it accepts no arguments and returns a new featureless
 |  instance that has no instance attributes and cannot be given any.
 |  
 |  Built-in subclasses:
 |      anext_awaitable
 |      async_generator
 |      async_generator_asend
 |      async_generator_athrow
 |      ... and 95 other subclasses
 |  
 |  Methods defined here:
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __dir__(self, /)
 |      Default dir() implementation.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getstate__(self, /)
 |      Helper for pickle.
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(self, /)
 |      Helper for pickle.
 |  
 |  __reduce_ex__(self, protocol, /)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |  
 |  __sizeof__(self, /)
 |      Size of object in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __init_subclass__(...)
 |      This method is called when a class is subclassed.
 |      
 |      The default implementation does nothing. It may be
 |      overridden to extend subclasses.
 |  
 |  __subclasshook__(...)
 |      Abstract classes can override this to customize issubclass().
 |      
 |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
 |      It should return True, False or NotImplemented.  If it returns
 |      NotImplemented, the normal algorithm is used.  Otherwise, it
 |      overrides the normal algorithm (and the outcome is cached).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __class__ = <class 'type'>
 |      type(object) -> the object's type
 |      type(name, bases, dict, **kwds) -> a new type

```

## **Python's Unified Type System**

Yes, Python's Unified Type System is one of its core design principles. It means that everything in Python is an object, and all objects ultimately inherit from the object class. This includes:

  - Primitive types (e.g., integers, strings, floats)
  
  - Data structures (e.g., lists, dictionaries, sets)
  - Functions and classes
  - Modules and types themselves
  - This design ensures a consistent and predictable behavior across all objects in Python.

## **Key Aspects of the Unified Type System**

### **1. Everything is an Object:**

  - In Python, even basic types like integers (int), strings (str), and booleans (bool) are instances of classes.

  - For example, the integer 5 is an instance of the int class, and the string "hello" is an instance of the str class.

```python
print(type(5))         # Output: <class 'int'>
print(type("hello"))    # Output: <class 'str'>
print(type(3.14))       # Output: <class 'float'>
```

**Output:**
```
<class 'int'>
<class 'str'>
<class 'float'>
```

Since int, str, and float are classes, and all classes inherit from object, these types are also objects.

### **2. Consistent Behavior:**

  - Because all objects inherit from object, they share common methods and behaviors.
  - For example, all objects can be converted to a string using the __str__() method, and their type can be checked using the type() function.

```python
print(str(42))          # Output: "42" (uses __str__ method of int)
print(str([1, 2, 3]))   # Output: "[1, 2, 3]" (uses __str__ method of list)
```

**Output:**
```
42
[1, 2, 3]
```

### **3. Dynamic Typing:**

  - Python's unified type system allows for dynamic typing, meaning the type of a variable is determined at runtime and can change.

  - For example, a variable can hold an integer at one point and a string at another.

```python
x = 42          # x is an int
x = "hello"     # x is now a str
```

**4. Uniform Access to Attributes and Methods:**

  - All objects have attributes and methods that can be accessed in the same way, regardless of their type.

  - For example, you can use the dir() function to list all attributes and methods of an object.

```python
print(dir(5))           # Lists attributes and methods of int
print(dir("hello"))    # Lists attributes and methods of str
```

**Output:**
```
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### **5.  Inheritance from object:**

  - All classes, whether built-in or user-defined, inherit from object directly or indirectly.

  - This ensures that even custom classes have access to default methods like __str__, __repr__, and __eq__.

```python
class MyClass:
    pass

obj = MyClass()
print(isinstance(obj, object))  # Output: True
```

**Output:**
```
True
```

## **Benefits of the Unified Type System**

### **1. Simplicity:**

  * The unified type system makes Python intuitive and easy to learn. You don’t need to worry about different rules for different types.


### **2. Consistency:**

  * Since all objects behave similarly, you can apply the same concepts (e.g., methods, attributes, inheritance) across all types.

### **3. Extensibility:**

  * You can create custom classes that behave like built-in types, thanks to the unified object model.

### **4. Polymorphism:**

  * The unified type system enables polymorphism, where objects of different types can be used interchangeably if they share the same interface.

## **Example: Unified Behavior in Action**

```python
# All objects can use the same methods
print(str(42))          # Output: "42"
print(str([1, 2, 3]))  # Output: "[1, 2, 3]"

# All objects inherit from object
print(isinstance(42, object))        # Output: True
print(isinstance("hello", object))   # Output: True
print(isinstance([1, 2, 3], object)) # Output: True

# Custom classes also inherit from object
class MyClass:
    pass

obj = MyClass()
print(isinstance(obj, object))  # Output: True
```

**Output:**
```
42
[1, 2, 3]
True
True
True
True
```

## **Conclusion**

Python's **unified type system** ensures that everything in Python is an object, all derived from the object class. This design provides **consistency**, **simplicity**, and **flexibility**, making Python a powerful and user-friendly language. Whether you're working with built-in types, functions, or custom classes, the same principles and behaviors apply, creating a seamless programming experience.

## **Special (Magic/Dunder) Methods**

Special methods are Python's secret commands that make objects work with regular operations like + or print(). Think of them as hidden buttons that bring your custom objects to life! Here's how they work using a Toy Store analogy.

**Essential Special Methods**

**1. \_\_init\_\_ - The Setup Crew**

Prepares new objects like unboxing toys:

```python
class ToyShelf:
    def __init__(self):
        self.toys = []

shelf = ToyShelf()  # Crew sets up empty shelf
```

**2. \_\_str\_\_ vs \_\_repr\_\_ - Toy Labels**

  - \_\_str\_\_: Friendly display (for customers)
  - \_\_repr\_\_: Exact specs (for warehouse staff)

```python
class Puzzle:
    def __init__(self, pieces):
        self.pieces = pieces

    def __str__(self):
        return f"Puzzle with {self.pieces} fun pieces!"

    def __repr__(self):
        return f"Puzzle({self.pieces})"

puzzle = Puzzle(100)
print(str(puzzle))   # "Puzzle with 100 fun pieces!"
print(repr(puzzle))  # "Puzzle(100)"
```

**Output:**
```
Puzzle with 100 fun pieces!
Puzzle(100)
```

**3. \_\_len\_\_ & \_\_getitem\_\_ - Inventory Control**

Make objects work with `len()` and `[]`:

```python
class ToyBox:
    def __init__(self):
        self.toys = ["teddy", "car", "blocks"]

    def __len__(self):
        return len(self.toys)

    def __getitem__(self, index):
        return self.toys[index]

box = ToyBox()
print(len(box))  # 3
print(box[1])    # "car"
```

**Output:**
```
3
car
```

**4. Comparison Methods (\_\_eq\_\_, \_\_lt\_\_) - Toy Sorting**

Enable == and < comparisons:

```python
class Doll:
    def __init__(self, height):
        self.height = height

    def __eq__(self, other):
        return self.height == other.height

    def __lt__(self, other):
        return self.height < other.height

doll_A = Doll(30)  # 30cm tall
doll_B = Doll(25)
print(doll_A > doll_B)  # True (uses __lt__ automatically)
```

**Output:**
```
True
```

## **Complete Example: Magic Toy Catal**

```python
class ToyCatalog:
    def __init__(self):
        self.toys = {}

    def __setitem__(self, name, price):
        self.toys[name] = price

    def __getitem__(self, name):
        return self.toys.get(name, "Not in stock")

    def __contains__(self, name):
        return name in self.toys

    def __len__(self):
        return len(self.toys)

# Usage
store = ToyCatalog()
store["RoboDog"] = 49.99  # Uses __setitem__
print(store["RoboDog"])   # 49.99 (__getitem__)
print("Train" in store)   # False (__contains__)
```

**Output:**
```
49.99
False
```

## **Why Special Methods Matter**

  1.  **Natural integration:** Your objects work with Python's built-in functions

  2.  **Readable code:** len(box) instead of box.get_length()

  3.  **Custom behavior:** Define how YOUR objects should add/compare/display

  
Like teaching toys to follow store rules, these methods help your objects interact properly with Python's ecosystem. They turn your classes from basic containers into fully functional Python citizens!

## **Here's an expanded Magic Toy Catalog implementation demonstrating key special methods in action:**

```python
class MagicToyCatalog:
    def __init__(self):
        self.toys = {}
        self._secret_offer = "Free plushie with any purchase!"

    def __setitem__(self, name, details):
        """Add/update toys like catalog['RoboDog'] = (49.99, 'RC dog')"""
        self.toys[name] = details

    def __getitem__(self, name):
        """Get toy details using catalog['RoboDog']"""
        return self.toys.get(name, ("Unknown", "Not in stock"))

    def __delitem__(self, name):
        """Remove items with del catalog['RoboDog']"""
        if name in self.toys:
            del self.toys[name]
            print(f"Poof! {name} vanished from the catalog!")
        else:
            raise MagicToyError(f"✨ {name} doesn't exist in our dimension")

    def __contains__(self, name):
        """Check existence with 'RoboDog' in catalog"""
        return name in self.toys

    def __len__(self):
        """Get count with len(catalog)"""
        return len(self.toys)

    def __iter__(self):
        """Iterate with for toy in catalog"""
        return iter(self.toys.items())

    def __add__(self, other):
        """Combine catalogs: mega_catalog = catalog1 + catalog2"""
        combined = MagicToyCatalog()
        combined.toys = {**self.toys, **other.toys}
        return combined

    def __str__(self):
        """User-friendly display"""
        header = "🔮 Magic Toy Catalog 🔮\n"
        items = "\n".join([f"- {name}: ${price} ({desc})"
                          for name, (price, desc) in self.toys.items()])
        return header + (items if items else "✨ Empty (for now)")

    def __repr__(self):
        """Developer representation"""
        return f"<MagicToyCatalog: {len(self)} toys>"

    def __call__(self, discount=0):
        """Activate special offers: catalog(10) for 10% off"""
        return "\n".join([f"{name}: ${price * (1 - discount/100):.2f}"
                         for name, (price, desc) in self.toys.items()])

class MagicToyError(Exception):
    pass
```

## **Example Usage:**

```python
# Create catalogs
kids_toys = MagicToyCatalog()
collector_editions = MagicToyCatalog()

# Add items using __setitem__
kids_toys["RoboDog"] = (49.99, "Self-charging robot dog")
kids_toys["MagicKit"] = (29.95, "150 magic tricks set")
collector_editions["DragonStatue"] = (199.99, "Limited edition crystal dragon")

# Combine catalogs using __add__
mega_catalog = kids_toys + collector_editions

# Access items with __getitem__
print(mega_catalog["RoboDog"])  # (49.99, 'Self-charging robot dog')

# Check existence with __contains__
print("DragonStatue" in mega_catalog)  # True

# Get count with __len__
print(f"Total toys: {len(mega_catalog)}")  # Total toys: 3

# Iterate with __iter__
for name, details in mega_catalog:
    print(f"{name}: {details[1]}")

# String representation with __str__
print(mega_catalog)

# Callable discount with __call__
print("\n🔥 FLASH SALE 🔥")
print(mega_catalog(20))  # 20% off prices

# Remove item with __delitem__
del mega_catalog["MagicKit"]
```

**Output:**
```
(49.99, 'Self-charging robot dog')
True
Total toys: 3
RoboDog: Self-charging robot dog
MagicKit: 150 magic tricks set
DragonStatue: Limited edition crystal dragon
🔮 Magic Toy Catalog 🔮
- RoboDog: $49.99 (Self-charging robot dog)
- MagicKit: $29.95 (150 magic tricks set)
- DragonStatue: $199.99 (Limited edition crystal dragon)

🔥 FLASH SALE 🔥
RoboDog: $39.99
MagicKit: $23.96
DragonStatue: $159.99
Poof! MagicKit vanished from the catalog!
```

## **Key Features Demonstrated:**

  1.  Dictionary-like Interface (__setitem__, __getitem__, __delitem__)
  
  2.  Container Protocols (__len__, __contains__, __iter__)
  3.  Operator Overloading (__add__ for catalog merging)
  4.  String Representation (__str__ vs __repr__)
  5.  Callable Objects (__call__ for activating sales)
  6.  Custom Error Handling (MagicToyError class)

This implementation shows how special methods transform a class into a Python-native feeling component that integrates seamlessly with language features. The catalog now behaves like a magical store inventory that responds intuitively to standard Python operations.

