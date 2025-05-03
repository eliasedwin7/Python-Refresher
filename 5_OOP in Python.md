# 🧱 Python OOP (Object-Oriented Programming)

Object-Oriented Programming allows structuring code as **objects** (instances of classes) which bundle **data + behavior**.

---

## 🔹 Python is Fully Object-Oriented

In Python, **everything is an object**, including:

```python
x = 1
print(type(x))         # <class 'int'>

print(type("hello"))   # <class 'str'>

def greet():
    print("Hi")
print(type(greet))     # <class 'function'>
```

Even user-defined classes behave like objects:

```python
class Dog:
    pass

d = Dog()
print(type(d))  # <class '__main__.Dog'>
```

---

## 🔸 A. Defining a Class & Creating Objects

```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand      # Instance variable
        self.year = year

    def drive(self):
        print(f"{self.brand} is driving!")

car1 = Car("Toyota", 2020)
car1.drive()
```

### ✅ Key Points:

* `__init__()` is the **constructor**, automatically called during object creation.
* `self` is a reference to the current instance (like `this` in Java/C++).
* Methods defined inside the class are **bound to instances** by default.

---

## 🔸 B. Instance vs Class Variables

```python
class Dog:
    species = "Canine"       # Class variable (shared)

    def __init__(self, name):
        self.name = name     # Instance variable (unique per object)

dog1 = Dog("Rex")
dog2 = Dog("Tom")

print(dog1.name)      # Rex
print(dog2.name)      # Tom
print(dog1.species)   # Canine
```

### ✅ Interview Insight:

* Use **class variables** for constants or shared values.
* Use **instance variables** for object-specific state.

---

## 🔸 C. Class Method vs Static Method vs Instance Method

### 1. **Class Method**

Used to operate on **class-level data**.

```python
class People:
    number = 0

    @classmethod
    def add_person(cls):
        cls.number += 1
```

### 2. **Static Method**

Independent utility — no access to `self` or `cls`.

```python
class Utils:
    @staticmethod
    def add5(x):
        return x + 5
```

### 3. **Instance Method (default)**

Operates on the current object (`self`) — most common.

---

## 🧠 Common Interview Questions:

| Question                                   | What to Say                                                              |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| What is `self`?                            | It's a reference to the current object (like `this` in other languages). |
| Difference between class and instance var? | Class vars are shared, instance vars are unique per object.              |
| Why use `@classmethod`?                    | To modify or access class variables without instantiating the class.     |
| When to use `@staticmethod`?               | For helper functions that don't need object or class data.               |

---



Perfect — let's expand **Section 2: Inheritance** into a solid, interview-ready format with all essential types, code samples, and theory for Python OOP.

---

# 🧬 Section 2: Inheritance in Python OOP

Inheritance lets a class **reuse methods and properties** from another class. It allows building **hierarchies** and promotes **code reusability**.

---

## 🔹 A. Basic Inheritance

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()  # Woof!
```

✅ `Dog` overrides the `speak()` method from `Animal`.

---

## 🔹 B. Using `super()` to Call Parent Methods

```python
class Cat(Animal):
    def speak(self):
        super().speak()   # Calls Animal.speak()
        print("Meow!")
```

✅ `super()` is used to:

* Call a parent class’s method (`super().method()`)
* Initialize parent’s constructor (`super().__init__()`)

---

## 🧠 Common Inheritance Use Cases

| Case                 | Use it for...                             |
| -------------------- | ----------------------------------------- |
| Code reuse           | Share logic in parent class               |
| Polymorphism         | Same method, different behavior           |
| Specializing a class | Extend behavior without rewriting         |
| Enforcing design     | Create abstract base classes (with `abc`) |

---

## 🧬 Types of Inheritance in Python

### 1. **Single Inheritance**

One child inherits from one parent.

```python
class A: pass
class B(A): pass
```

---

### 2. **Multiple Inheritance**

Child inherits from **multiple parents**.

```python
class A: pass
class B: pass
class C(A, B): pass
```

⚠️ Handle method resolution carefully (MRO).

---

### 3. **Multilevel Inheritance**

A → B → C (inheritance chain).

```python
class A: pass
class B(A): pass
class C(B): pass
```

---

### 4. **Hierarchical Inheritance**

Multiple classes inherit from the same parent.

```python
class A: pass
class B(A): pass
class C(A): pass
```

---

### 5. **Hybrid Inheritance**

A mix of two or more types (complex). Python handles it using **MRO (Method Resolution Order)**.

---

## 🔍 MRO (Method Resolution Order)

* Python uses the **C3 linearization algorithm** to determine the order in which base classes are searched.
* Use `ClassName.__mro__` or `help(ClassName)` to inspect it.

```python
print(C.__mro__)
```

---

## 📌 Interview Tips

| Question                           | Sample Insight                                              |
| ---------------------------------- | ----------------------------------------------------------- |
| What's the purpose of inheritance? | Reuse code, specialize behavior, build class hierarchies.   |
| How does `super()` work?           | Refers to the next class in the MRO chain.                  |
| Is Python fully OOP?               | Yes — everything is an object, including functions & types. |
| What is MRO?                       | It resolves method calls in multiple inheritance cases.     |

---

Absolutely, Edwin — here’s a **clean and interview-ready Section on Polymorphism** in Python OOP, with theory, examples, and clear connections to real use cases and dunder methods.

---

# 🌀 Section 3: Polymorphism in Python OOP

---

## 🔹 What is Polymorphism?

**Polymorphism** means **“many forms.”** In OOP, it allows the **same interface (method or operator) to behave differently** depending on the object.

In Python, polymorphism is both **built-in** and **flexible**, thanks to **duck typing**:

> *“If it walks like a duck and quacks like a duck, it's a duck.”*

---

## 🔸 A. Method Polymorphism (Overriding)

Different classes can define the same method name, but with their own logic:

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for a in animals:
    print(a.speak())  # Woof! Meow!
```

✅ This is **runtime polymorphism** via **method overriding**.

---

## 🔸 B. Polymorphism with Built-in Functions

```python
print(len("hello"))   # 5
print(len([1, 2, 3]))  # 3
```

Python internally uses **`__len__()`** method on both types.

✅ This is an example of **polymorphism via dunder methods**.

---

## 🔸 C. Operator Overloading (via Dunder Methods)

Python lets you **override built-in operators** for your own class:

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return f"Book with {self.pages} pages"

b1 = Book(100)
b2 = Book(150)
print(b1 + b2)  # Book with 250 pages
```

✅ This is polymorphism through **special/dunder methods** like `__add__`.

---

## 🔸 D. Built-in Polymorphic Methods

| Function | Polymorphic Behavior                          |
| -------- | --------------------------------------------- |
| `len()`  | Works on strings, lists, dicts, etc.          |
| `+`      | Adds numbers, merges strings/lists            |
| `*`      | Multiplies numbers, repeats strings/lists     |
| `str()`  | Converts any object to string via `__str__()` |

---

## 📌 Interview Points

| Question                                       | What to Say                                                            |
| ---------------------------------------------- | ---------------------------------------------------------------------- |
| What is polymorphism?                          | Ability for same interface to work across multiple types               |
| Does Python support method overloading?        | No, but supports **dynamic argument handling** via `*args`, `**kwargs` |
| How is polymorphism implemented?               | Through **method overriding** and **dunder methods**                   |
| Difference between overriding and overloading? | Python supports overriding but not classic function overloading        |

---

## 🧠 Tip

Use polymorphism to **write clean, extensible code** — especially in scenarios like:

* Test automation frameworks (e.g., `click()`, `type()` on different UI elements)
* API clients (e.g., `send()` method for multiple request types)

---


# 🛡️ Section 4: Encapsulation in Python OOP

---

## 🔹 What is Encapsulation?

**Encapsulation** is the OOP principle of **hiding internal state** and only exposing a **controlled interface** to the outside world.

In Python, it's about:

* **Protecting data**
* **Restricting direct access**
* Allowing interaction via **methods** (getters/setters)

---

## 🔸 A. Access Modifiers in Python

While Python doesn't enforce strict access control like Java/C++, it follows **naming conventions**:

| Modifier  | Syntax        | Meaning                                 |
| --------- | ------------- | --------------------------------------- |
| Public    | `self.name`   | Accessible from anywhere                |
| Protected | `self._name`  | Suggests internal use (*convention*)    |
| Private   | `self.__name` | Name-mangled to prevent external access |

---

## 🔸 B. Example: Private Variable

```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private

    def get_name(self):
        return self.__name

p = Person("Edwin")
print(p.get_name())      # ✅ Edwin
# print(p.__name)        # ❌ AttributeError
print(p._Person__name)   # ⚠️ Possible, but breaks encapsulation
```

---

## 🔸 C. Using Setters and Getters

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

✅ Only `deposit()` can change the balance — this protects internal state.

---

# 🧊 Section 5: Abstraction in Python OOP

---

## 🔹 What is Abstraction?

**Abstraction** is the process of hiding **implementation details** and showing only the **relevant features**.

In OOP, abstraction helps you:

* Focus on **what** an object does, not **how** it does it
* Create **flexible and extendable** code
* Design **blueprints (abstract base classes)** for consistent structure

---

## 🧱 Python’s Approach to Abstraction

Python uses the `abc` module to define **abstract base classes** with one or more **abstract methods** (methods with no implementation).

---

## 🔸 A. Abstract Class Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

### ✅ Key Points:

* `Animal` is an **abstract class**.
* `speak()` is an **abstract method** — must be overridden.
* You **cannot instantiate** `Animal` directly.

---

## 🔸 B. Why Use Abstraction?

* Enforce a **contract** for subclasses
* Separate **interface** from **implementation**
* Enable **plug-and-play architecture** (e.g., test frameworks, APIs)

---

## 🧠 Real-World Analogy

> Think of a **TV remote** — you press a button (interface), but you don’t care how it changes channels (implementation).

---

## 🔍 Abstract Class vs Interface

| Feature                   | Abstract Class       | Interface (Java-style, not native in Python) |
| ------------------------- | -------------------- | -------------------------------------------- |
| Can have concrete methods | ✅ Yes                | ❌ Purely abstract                            |
| Multiple inheritance      | ✅ Supported via ABC  | ✅ Mixins or multiple ABCs                    |
| Instantiable?             | ❌ No (must subclass) | ❌ No                                         |

---

## 📌 Interview Points

| Question                              | What to Say                                                  |
| ------------------------------------- | ------------------------------------------------------------ |
| What is abstraction?                  | Hiding internal details and exposing essential behavior      |
| How is it implemented in Python?      | Using `abc.ABC` and `@abstractmethod` decorators             |
| Can you instantiate abstract classes? | No, you must subclass and implement all abstract methods     |
| Why is it useful?                     | Helps enforce consistent APIs, enables plug-and-play designs |

---

# ✨ Section 6: Special / Dunder Methods in Python

---

## 🔹 What are Dunder Methods?

**Dunder** = “Double UNDERSCORE” (e.g. `__init__`, `__str__`)
These are **special methods** that let you define or customize how your objects behave with **built-in Python operations**.

They enable:

* **Constructor behavior**
* **Operator overloading**
* **Object representation**
* **Comparison, hashing, length, callable behavior**

---

## 🔸 A. Commonly Used Dunder Methods

| Method     | Purpose                                 | Example Use             |
| ---------- | --------------------------------------- | ----------------------- |
| `__init__` | Constructor (called on object creation) | `obj = MyClass()`       |
| `__str__`  | Human-readable string                   | `print(obj)`            |
| `__repr__` | Developer-friendly string               | `repr(obj)` / debugging |
| `__len__`  | Return length                           | `len(obj)`              |
| `__eq__`   | Equality check                          | `obj1 == obj2`          |
| `__hash__` | Hashing (for sets/dicts)                | `hash(obj)`             |
| `__add__`  | Operator overloading (`+`)              | `obj1 + obj2`           |
| `__del__`  | Destructor                              | `del obj`               |
| `__call__` | Make object callable                    | `obj()`                 |

---

## 🔸 B. Example: Custom Book Class

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book(title='{self.title}')"

    def __eq__(self, other):
        return self.title == other.title

    def __add__(self, other):
        return Book(self.title + " & " + other.title)

    def __del__(self):
        print(f"Deleted book: {self.title}")

    def __call__(self):
        print(f"You opened the book: {self.title}")
```

```python
book1 = Book("Tron")
book2 = Book("Legacy")
print(book1)           # Book: Tron
print(repr(book2))     # Book(title='Legacy')
print(book1 == book2)  # False

combo = book1 + book2
print(combo)           # Book: Tron & Legacy

book1()                # You opened the book: Tron

del book1              # Deleted book: Tron
```

---

## 🔸 C. Use Cases in Real Projects

* `__str__` / `__repr__`: For better logging and debugging
* `__eq__` / `__hash__`: To use custom objects in `set`, `dict`
* `__call__`: To make objects behave like functions
* `__add__`, `__mul__`: For **operator overloading** in custom classes (e.g., vectors, money, matrices)

---

## 📌 Interview Insights

| Question                                                | Sample Answer                                                       |
| ------------------------------------------------------- | ------------------------------------------------------------------- |
| What are dunder methods?                                | Special methods with double underscores that define object behavior |
| What's the difference between `__str__` and `__repr__`? | `__str__` is user-friendly, `__repr__` is for debugging             |
| Can you override built-in operators?                    | Yes, using dunder methods like `__add__`, `__eq__`, etc.            |
| What's `__call__` used for?                             | It lets you call an object like a function (`obj()`)                |
| When does `__del__` run?                                | When the object is garbage collected (not always predictable)       |

---


## 🔸 D. Using `@property` (Pythonic Way)

Python provides `@property` decorators to **create getter/setter behavior** in a clean style.

```python
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
```

```python
p = Product(50)
print(p.price)    # ✅ calls getter
p.price = 100     # ✅ calls setter
```

---

## 📌 Interview Points

| Question                      | Suggested Answer                                            |
| ----------------------------- | ----------------------------------------------------------- |
| What is encapsulation?        | Binding data + behavior and hiding internal implementation  |
| How does Python enforce it?   | Uses `_` and `__` naming conventions (soft enforcement)     |
| Why use getters/setters?      | To validate and control access to internal variables        |
| What is `@property` used for? | To expose attributes like public variables but with control |

---



Here’s your finalized and polished **Section 7: `@property` Decorator** — with theory, clean examples, analogies, interview insights, and a challenge to show your understanding in interviews.

---

# 🏷️ Section 7: `@property` Decorator in Python

---

## 🔹 What is `@property`?

`@property` is a **Pythonic way to use methods like attributes**, often used to **encapsulate data access** cleanly and safely.

It helps you:

* **Expose private data** without exposing internal implementation
* Add **logic or validation** during get/set
* Write **clean and intuitive** API

---

## 🔸 A. Basic Example

```python
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
```

```python
p = Product(50)
print(p.price)     # ✅ Calls getter
p.price = 100      # ✅ Calls setter
```

✅ No parentheses needed like `p.get_price()` — it's as clean as direct access, but with control.

---

## 🔸 B. Full Example: Validated Radius

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
```

```python
c = Circle(5)
print(c.radius)     # 5
c.radius = 10       # ✅ Works
c.radius = -3       # ❌ Raises ValueError
```

---

## 🧠 Analogy

> `@property` is like a **car's speedometer**:
> You can read it easily, but under the hood there's complex logic.

---

## 📌 Interview Points

| Question                  | Suggested Answer                                     |
| ------------------------- | ---------------------------------------------------- |
| What does `@property` do? | Converts a method into a getter-accessible attribute |
| Why use it?               | To hide internal logic but expose values cleanly     |
| Can it validate data?     | Yes, use `@<prop>.setter` for validation             |
| Is it encapsulation?      | Yes — a very Pythonic form of encapsulation          |

---

## 🧪 BONUS: Read-Only Property

```python
class User:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username  # No setter = read-only
```

---

## 🧩 Mini Challenge (Interview Demo)

> Create a `Rectangle` class with:

* Attributes: width and height
* `area()` method
* `__str__` method to return: `"Rectangle(4x5)"`

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Rectangle({self._width}x{self._height})"
```

```python
r = Rectangle(4, 5)
print(r)            # Rectangle(4x5)
print(r.area)       # 20
```
