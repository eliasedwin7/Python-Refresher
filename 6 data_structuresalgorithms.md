## **Step 6: Data Structures & Algorithms**

---

### 🔹 **1. Lists (Dynamic Arrays)**

**Why use it?**  
- Ordered collection, resizable, fast appends.

```python
arr = [1, 2, 3]
arr.append(4)
arr.pop()          # Removes last
arr.insert(1, 10)  # Inserts at index 1
```

🔸 Time complexity:
- `append()` → O(1)
- `insert(i)` → O(n)
- `pop()` → O(1) from end, O(n) from start

**Use when:** You need fast iteration and dynamic sizing.

---

### 🔹 **2. Sets**

**Why use it?**  
- No duplicates, fast membership checks.

```python
s = {1, 2, 3}
s.add(4)
s.remove(2)
print(3 in s)  # True
```

🔸 Time complexity:
- `add`, `remove`, `in` → O(1) average

**Use when:** You need fast checks or unique elements.

---

### 🔹 **3. Dictionaries (Hash Maps)**

**Why use it?**  
- Key-value lookup, great for counting, mapping.

```python
d = {"name": "Edwin", "age": 25}
d["location"] = "Canberra"
d.get("job", "None")  # Returns "None" if not found
```

🔸 Time complexity:
- `get`, `set`, `delete` → O(1) average

**Use when:** Fast access by key is needed.

---

### 🔹 **4. Stacks (LIFO)**

**Why use it?**  
- "Last in, first out" logic – useful for backtracking, undo, expression parsing.

```python
stack = []
stack.append(1)
stack.append(2)
stack.pop()     # 2
```

🔸 Use list or `collections.deque`.

---

### 🔹 **5. Queues (FIFO)**

**Why use it?**  
- "First in, first out" logic – great for task scheduling, breadth-first search.

```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()   # 1
```

---

### 🔹 **6. Counter & DefaultDict**

```python
from collections import Counter, defaultdict

words = ["a", "b", "a"]
c = Counter(words)  # {'a': 2, 'b': 1}

d = defaultdict(int)
for w in words:
    d[w] += 1
```

🔸 Use when:
- You need to count things (`Counter`)
- You want default values in a dict (`defaultdict`)

---

### 🔹 7. Sorting

**Built-in Sort**
```python
arr = [3, 1, 2]
arr.sort()  # in-place
sorted_arr = sorted(arr)  # returns a new list
```

**Custom Key**
```python
words = ["apple", "bat", "banana"]
words.sort(key=len)  # Sort by length
```

🔸 `sort()` → O(n log n) using Timsort

---

### 🔹 8. Searching

#### Linear Search (O(n))
```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

#### Binary Search (O(log n)) – requires sorted list
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

---

### ✅ Summary: When to Use What?

| Structure   | Use When…                            |
|-------------|--------------------------------------|
| List        | You need order & indexing            |
| Set         | Fast membership, no duplicates       |
| Dict        | Fast key-value access                |
| Stack       | Backtracking / Undo logic            |
| Queue       | Task pipelines / BFS                 |
| Counter     | Frequency counting                   |
| DefaultDict | Avoid key errors with default values |

---

**Mini Task**:  
Create a function that counts how many times each letter appears in a string using `Counter`.

---