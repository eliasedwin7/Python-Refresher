# **Step 5: Object-Oriented Programming (OOP) in Python**

---

## **Step 5: OOP in Python**

---

### **A. Defining a Class**
```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def drive(self):
        print(f"{self.brand} is driving!")

car1 = Car("Toyota", 2020)
car1.drive()
```

> `__init__` is the constructor; `self` refers to the instance.

---

### **B. Instance vs Class Variables**
```python
class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Rex")
print(dog1.species)  # Canine
```

---

### **C. Inheritance**
```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()
```

> `Dog` overrides the `speak()` method from `Animal`.

---

### **D. `super()` Function**
Calls the parent class method.

```python
class Cat(Animal):
    def speak(self):
        super().speak()  # Calls Animal.speak()
        print("Meow!")
```

---

### **E. Special / Dunder Methods**
- `__str__` → string representation
- `__len__` → custom length
- `__eq__` → equality
- `__hash__` → used in sets and dicts

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

    def __eq__(self, other):
        return self.title == other.title
```

---

### **F. Encapsulation**
- `_var`: "Protected" (by convention)
- `__var`: Name mangled to prevent access
```python
class Person:
    def __init__(self, name):
        self.__name = name  # private

    def get_name(self):
        return self.__name
```

---

### **G. @property Decorator**
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2
```

---

**Mini Challenge**:  
Create a class `Rectangle` with width and height, a method to compute area, and use `__str__` to print like: `Rectangle(4x5)`.
