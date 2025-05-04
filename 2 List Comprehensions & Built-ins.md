Great! Let’s dive into **List Comprehensions** and essential **Built-in Functions**.

---

## **Step 2: List Comprehensions & Built-ins**

---

### **A. List Comprehensions**
A compact way to create lists.

```python
# Traditional way
squares = []
for i in range(5):
    squares.append(i * i)

# List comprehension
squares = [i * i for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

#### **With Conditionals**
```python
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

names = ["edwin", "alex", "bob"]
capitalized = [name.capitalize() for name in names if len(name) > 3]
```

---

#### **Nested Comprehensions**
```python
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

---

### **B. Built-in Functions**
#### 1. **`map()`** – apply a function to every item
```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
```

#### 2. **`filter()`** – keep items that match a condition
```python
even = list(filter(lambda x: x % 2 == 0, nums))
```

#### 3. **`zip()`** – combine multiple iterables
```python
names = ["a", "b", "c"]
scores = [90, 80, 85]
zipped = list(zip(names, scores))  # [('a', 90), ('b', 80), ('c', 85)]
```

#### 4. **`enumerate()`** – get index + value
```python
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)
```

---

### **C. Set & Dict Comprehensions**
```python
unique = {char for char in "hello"}
squares_dict = {i: i*i for i in range(5)}
```

---

