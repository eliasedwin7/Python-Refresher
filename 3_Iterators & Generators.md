
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

# 🔁 Section C: Generators in Python

---

### ✅ What are Generators?

Generators are **special iterators** that allow you to iterate over data **lazily** — **one value at a time** — using the `yield` keyword.

They are memory-efficient alternatives to lists when dealing with **large data** or **infinite sequences**.

---

### 🔹 Key Characteristics

* Defined using **`yield`** instead of `return`
* **Lazy evaluation**: generates values on-the-fly, not all at once
* **Memory efficient**: does **not store** the entire sequence in memory
* **Single-use only**: once exhausted, cannot be reset or re-used

---

### 🔸 Generator Example

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
```

```python
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen)      # Raises StopIteration
```

---

### 🧠 Comparison with Lists

| Feature      | List                           | Generator               |
| ------------ | ------------------------------ | ----------------------- |
| Data storage | Stores all values              | Generates one at a time |
| Memory usage | High for large datasets        | Low (no storage)        |
| Syntax       | `return` and list              | `yield`                 |
| Reusability  | Can re-use/loop multiple times | One-time use only       |

---

### 🧪 Use Cases

* Reading large files
* Streaming data from APIs
* Processing large datasets
* Infinite sequences (e.g., Fibonacci)

---

### 📌 Interview Insights

| Question                           | Sample Answer                                                    |
| ---------------------------------- | ---------------------------------------------------------------- |
| What is a generator?               | A special iterator that yields values one by one using `yield`.  |
| Why use it?                        | To save memory and work efficiently with large or infinite data. |
| Can it be reused?                  | No, generators are exhausted after one complete iteration.       |
| What’s the difference from return? | `return` ends the function, `yield` pauses and resumes later.    |

