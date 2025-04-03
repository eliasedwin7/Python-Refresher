## **Step 4A: Functions**

### **Basic Function**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Edwin"))  # Hello, Edwin!
```

### **Default Arguments**
```python
def greet(name="Guest"):
    return f"Hi, {name}"
```

### **Keyword & Positional Arguments**
```python
def order(item, price):
    print(f"{item}: ${price}")

order(price=15, item="Book")
```

### **Variable Arguments**
*args and **kwargs allow you to pass multiple arguments or keyword arguments to a function. 
Bear in mind that the iterable object you’ll get using the unpacking operator * is not a list but a tuple

**kwargs accepts keyword (or named) arguments.

```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))  # 6

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Edwin", age=25)
```

---

## **Step 4B: Error Handling**

### **Try-Except**
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### **Catch Multiple**
```python
try:
    val = int("abc")
except (ValueError, TypeError) as e:
    print("Invalid conversion:", e)
```

### **Finally Block**
```python
try:
    f = open("file.txt")
finally:
    f.close()
```

---

## **Step 4C: Decorators**

### **What is a Decorator?**
A function that wraps another to add functionality.

```python
def shout(func):
    def wrapper():
        return func().upper()
    return wrapper

@shout
def greet():
    return "hello"

print(greet())  # HELLO
```

### **With Arguments**
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 4)
```

---

### **Special Decorators**
- `@staticmethod`: No access to `self` or `cls`
- `@classmethod`: Takes `cls` instead of `self`
- `@property`: Makes a method behave like an attribute

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

---

Absolutely. Decorators are one of the most elegant and powerful features in Python. Let’s unpack them properly.

---

## **What Is a Decorator?**

A **decorator** is a function that takes another function as input and returns a modified version of that function—**without changing its actual code**.

You "decorate" a function to **extend or change its behavior**.

---

### **1. Basic Decorator Structure**
```python
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Before the function
Hello!
After the function
```

> The `@my_decorator` is just syntactic sugar for `say_hello = my_decorator(say_hello)`

---

### **2. Decorator with Arguments**
```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(3, 4)
```

> Works with any number of arguments thanks to `*args` and `**kwargs`.

---

### **3. Nested Decorators**
You can stack multiple decorators:
```python
@logger
@timer
def process_data():
    ...
```

Python applies them from **bottom to top**.

---

### **4. Real-World Use Cases**
- **Logging**  
- **Authorization** (check if user is admin)
- **Caching**
- **Performance measurement** (`timeit`)
- **Retry logic**

---

### **5. Class-Based Decorators**
For more complex state or reusability:
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def greet():
    print("Hey!")

greet()
greet()
```

---

### **6. Preserving Metadata (important!)**
Use `functools.wraps` to keep the original function’s name and docstring.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Without `@wraps`, `func.__name__` would be `'wrapper'`.

---

Great question—knowing **when to use `*args` and `**kwargs`** is key to writing flexible, reusable functions.

---

## 🔹 **When to Use `*args`**

Use `*args` when:
- You want to accept **any number of positional arguments**.

```python
def total(*args):
    return sum(args)

total(1, 2, 3, 4)  # returns 10
```

---

## 🔹 **When to Use `**kwargs`**

Use `**kwargs` when:
- You want to accept **any number of keyword arguments**.

```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_details(name="Edwin", age=25)
```

---

## 🔹 **When to Use Both**

Use both when:
- You need to support **both** kinds of inputs.

```python
def log(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

log(1, 2, user="edwin", active=True)
```

---

## 🔹 **In Decorators or Wrappers**

This is where it’s most important:
You don’t always know the signature of the function being decorated, so you use both to make the decorator **universal**.

```python
def universal_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
```

---

## ✅ Rule of Thumb

Use them when:
- You're **wrapping** other functions (e.g., decorators)
- You're **forwarding** arguments to other functions
- You're building **utility functions** or **framework-like tools**

---
