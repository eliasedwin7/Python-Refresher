
## **Step 3: Iterators & Generators**

---

### **A. Iterators**

An **iterator** is any object with `__iter__()` and `__next__()` methods.

```python
nums = [1, 2, 3]
it = iter(nums)       # Get iterator object

print(next(it))       # 1
print(next(it))       # 2
print(next(it))       # 3
```

If you call `next()` after the last item, it raises `StopIteration`.

---

### **B. Custom Iterator (just for understanding)**

```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for num in Counter(3):
    print(num)  # 0 1 2
```

---

### **C. Generators**
Generators are **iterators**, but simpler to write using `yield`.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)  # 3 2 1
```

> `yield` pauses the function, remembers its state, and resumes on the next iteration.

---

### **D. Generator Expressions**
Just like list comprehensions but with `()` instead of `[]`.

```python
squares = (x*x for x in range(1000))  # Doesn't compute all at once
print(next(squares))  # 0
```

---

### **Why They Matter for Testing**
- Perfect for simulating **large logs or test data**.
- Useful for **lazy loading** and **streaming inputs**.

---

**Mini Challenge**:  
Write a generator that yields only even numbers up to a given `n`.

---
