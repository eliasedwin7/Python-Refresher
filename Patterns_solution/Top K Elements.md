# 5. Top K Elements
 
 this one is super handy when you want to find the **most important things** from a big pile. 🥇

---

🧱 What is a Heap?
A heap is a special kind of binary tree (usually stored in an array) that always keeps the biggest or smallest element on top.
There are two types:

Type	Top Element
Min Heap	Smallest
Max Heap	Largest
In Python, the default is a Min Heap using the heapq module.



### 🧠 Imagine You Are...

In a race with 100 people, and you want to know who the **top 3 fastest runners** are. You don’t care about sorting everyone—just the best 3. This is where “**Top K Elements**” comes in.

We only care about **K best**, **K largest**, or **K most frequent**.

---

### 💼 Common Problems:

- Top 3 highest scores.
- Top 5 most common words.
- Top K largest/smallest numbers.

---

### 🛠 Python Code Example: Top K Largest Numbers

We’ll use a **heap** (a special tree-like structure) to do this fast.

```python
import heapq

def find_top_k_largest(nums, k):
    # Create a min-heap with the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # Go through the rest of the numbers
    for num in nums[k:]:
        if num > min_heap[0]:  # Only add if it's larger than the smallest in heap
            heapq.heappop(min_heap)  # Remove smallest
            heapq.heappush(min_heap, num)  # Add new number

    return list(min_heap)

# Example
nums = [3, 1, 5, 12, 2, 11]
k = 3
print("Top", k, "largest numbers:", find_top_k_largest(nums, k))
```

---

### 🪄 Explanation Like You’re a Kid:

- Imagine you have a basket that can only hold 3 apples.
- You go through a big pile of apples.
- You only keep the **3 biggest apples** in your basket.
- Every time you find a bigger one, throw the smallest out!

---

### 🧠 Want Frequency-Based Example?

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Example
nums = [1,1,1,2,2,3,3,3,3]
k = 2
print("Top", k, "frequent numbers:", top_k_frequent(nums, k))
```

This finds numbers that **appear most often**.

---

### 💡 Where It’s Used:

- Leaderboards (games/sports)
- Popular hashtags or searches
- Machine learning (feature selection)

---




### 🧱 What is a Heap?

A **heap** is a special kind of binary tree (usually stored in an array) that always keeps the **biggest or smallest element on top**.

There are two types:

| Type           | Top Element |
|----------------|-------------|
| **Min Heap**   | Smallest    |
| **Max Heap**   | Largest     |

In Python, the default is a **Min Heap** using the `heapq` module.


### 🛠 What Is It Used For?

- Getting the **top K smallest or largest** elements quickly.
- **Priority queues** (like handling urgent tasks first).
- Efficient **sorting**.
- **Greedy algorithms** (like Dijkstra’s shortest path).

---

### 🧰 Python Code Example

```python
import heapq

nums = [5, 1, 9, 3, 7]
heapq.heapify(nums)  # Turn it into a min-heap

print("Smallest element:", nums[0])  # Always the root (min)

heapq.heappush(nums, 0)  # Add new number
print("After push:", nums)

print("Pop smallest:", heapq.heappop(nums))  # Removes min
print("Heap now:", nums)
```

---

### 💡 Max Heap in Python?

Python doesn’t have one by default, but you can simulate it by **pushing negative numbers**:

```python
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)

largest = -heapq.heappop(max_heap)
print("Largest value:", largest)
```

---