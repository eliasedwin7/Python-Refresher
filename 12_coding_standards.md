# **coding standards** 
---

### ✅ **1. Write Clean, Readable Code**
- Use meaningful variable and function names: `user_count` > `uc`
- Keep functions small and focused: do **one** thing well
- Add comments only when necessary (your code should mostly explain itself)

---

### ✅ **2. Follow PEP 8 (Python Style Guide)**
- Use **4 spaces** per indentation level
- Keep line length ≤ 79 characters (or 120 if modern team allows)
- Leave **2 blank lines** between top-level functions
- Use **snake_case** for variable and function names
- Use **CapWords** (PascalCase) for class names

---

### ✅ **3. Structure Your Code**
- Group imports: built-in, third-party, your own
```python
import os
from collections import defaultdict

import numpy as np
```
- Put function definitions at the top, execution in `if __name__ == "__main__":`

---

### ✅ **4. Handle Edge Cases**
Always think:
- What if `input is empty`?
- What if `k = 0` or negative?
- What if `data is not sorted` or `null`?
You can add assert statements or raise exceptions.

---

### ✅ **5. Optimize**
- Avoid repeated work (like calling `sum()` in loops)
- Use appropriate data structures (`set` for lookups, `deque` for sliding window, etc.)

---

### ✅ **6. Test Your Code**
- Write minimal test cases (edge, base, and expected inputs)
- If time: use `unittest` or `pytest` style tests

---

### ✅ **7. Don’t Overcomplicate**
- Prefer clarity over cleverness (especially in interviews)
- If your code solves the problem clearly in 10 lines, that’s better than 6 cryptic ones

---

### ✅ **8. Time and Space Complexity Awareness**
- After coding, **state and analyze** your solution's complexity
- Example: "This is O(n) time and O(k) space due to the sliding window and hash map"

---

### ✅ **9. Use Pythonic Idioms (but don’t overuse)**
Examples:
- `if not list:` instead of `if len(list) == 0`
- `for idx, val in enumerate(arr):` instead of manual indexing

---

### ✅ **10. Graceful Error Handling**
Use `try/except` blocks if needed, especially around user inputs or external file/DB interactions.


---

# ✅ Section 11: Type Hinting & Dynamic Typing in Python

---

## 🔹 What is Dynamic Typing?

Python is a **dynamically typed language**, meaning:

* You **don’t need to declare data types** explicitly.
* The type is **determined at runtime**, not during compilation.

```python
x = 10        # int
x = "hello"   # now it's a str
```

✅ This gives Python flexibility, but also makes it easier to introduce bugs — especially in large projects.

---

## 🔸 Why Use Type Hinting?

**Type hinting** adds **optional type information** to your Python code to improve:

* **Readability**
* **Static analysis**
* **Editor autocompletion**
* **Bug detection with tools** like `mypy`, `pylance`

---

### 🔸 Basic Type Hinting Example

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

✅ This says: `greet()` takes a `str` and returns a `str`.

---

## 🔸 Common Type Hints

| Type     | Syntax Example                           |
| -------- | ---------------------------------------- |
| Int      | `def square(x: int) -> int`              |
| String   | `def say(name: str)`                     |
| Boolean  | `def flag(is_valid: bool)`               |
| List     | `List[int]`                              |
| Tuple    | `Tuple[int, str]`                        |
| Dict     | `Dict[str, int]`                         |
| Optional | `Optional[int]` (can be `int` or `None`) |
| Any      | `Any` (from `typing`)                    |

```python
from typing import List, Dict, Tuple, Optional

def get_scores() -> List[int]:
    return [80, 90, 100]
```

---

## 🔸 Dynamic Attribute Access

Python allows you to **access object attributes dynamically** using built-in functions like:

```python
getattr(obj, "attribute_name")      # Same as obj.attribute_name
setattr(obj, "attr", value)         # Sets obj.attr = value
hasattr(obj, "attr")                # Checks if attr exists
```

✅ This is powerful in frameworks, APIs, and reflection.

---

### 🔹 Example: Dynamic Attribute

```python
class Person:
    def __init__(self):
        self.name = "Edwin"

p = Person()
print(getattr(p, "name"))   # Edwin

setattr(p, "age", 30)
print(p.age)                # 30
```

---

## 📌 Interview Highlights

| Question                                 | Suggested Answer                                               |
| ---------------------------------------- | -------------------------------------------------------------- |
| What does dynamic typing mean?           | Variables can change type at runtime; no need to declare types |
| Why use type hints if Python is dynamic? | Improves readability, tooling, and helps catch bugs early      |
| What is `getattr()` used for?            | Dynamically access attributes when the name is a variable      |

---

Let me know if you want to add advanced type hinting like `Union`, `Literal`, or `TypedDict`.
