## **Step 7: Essential Algorithms & Patterns**


## ✅ **Why These Patterns Matter**

In interviews like at SIG, you’ll get real-world coding scenarios where brute-force won’t cut it. These patterns help solve problems **efficiently**, and they’re often hidden inside more complex logic.

Let’s go through them slowly, with the *what*, *why*, and *how*.

---

### 🔹 1. **Recursion**  
**What?** A function that calls itself.  
**Why?** Useful when the problem can be broken into similar smaller problems.

#### Example: `factorial(5)` → `5 * 4 * 3 * 2 * 1`

```python
def factorial(n):
    if n == 0:
        return 1  # base case
    return n * factorial(n - 1)
```

🔸 **Think of it like this**: you're stacking up tasks (calls) and completing them as you return.

---

### 🔹 2. **Sliding Window**  
**What?** A "window" moves across the array to track things like max sum or unique chars.  
**Why?** Avoids recalculating from scratch every time. Much faster than nested loops.

#### Example: max sum of any 3 consecutive elements

```python
def max_sum(arr, k):
    current = sum(arr[:k])  # first window
    result = current
    for i in range(k, len(arr)):
        current += arr[i] - arr[i - k]
        result = max(result, current)
    return result
```

🔸 Instead of summing from scratch every time, we just adjust the window with one add + one subtract. Efficient!

---

### 🔹 3. **Two Pointers**  
**What?** Use two indexes that "meet" or "move" through data together.  
**Why?** Great for sorted lists, partitioning, or finding pairs.

#### Example: find if a sorted list has two numbers that sum to a target.

```python
def has_pair(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False
```

🔸 Much better than checking every possible pair (O(n²)).

---

### 🔹 4. **Hashing (Using Dicts/Sets)**  
**What?** Store values with constant-time lookup.  
**Why?** Super fast for checking if something exists.

#### Example: first non-repeating character

```python
from collections import Counter

def first_unique_char(s):
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
```

🔸 Without hashing, this would take two full passes or be much slower.

---

### 🔹 5. **Prefix Sum**  
**What?** Build an array where each element is the sum of everything before it.  
**Why?** Allows instant calculation of any subarray sum.

#### Example:
```python
arr = [1, 2, 3, 4]
prefix = [0, 1, 3, 6, 10]  # prefix[i] = sum(arr[:i])

# sum of arr[1:3] = prefix[3] - prefix[1] = 6 - 1 = 5
```

🔸 Amazing for range-sum queries—often used in test automation data validation too.

---

### 🔹 6. **Dynamic Programming (DP)**  
**What?** Store intermediate results instead of recalculating.  
**Why?** Massive speedup when problems have overlapping sub-problems.

#### Example: Fibonacci
```python
def fib(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

🔸 Without memoization: O(2ⁿ)  
🔸 With memoization: O(n)

---

Let me know if you'd like me to create visual examples or tiny problem sets for these.  
When you’re ready, we’ll tackle **file handling, parsing, and regex**—very practical for test engineer work.

### 🔹 **7. Sorting Algorithms (Basics)**

- **Bubble Sort** – O(n²), basic
- **Merge Sort** – O(n log n), divide & conquer
- **Quick Sort** – O(n log n) avg, in-place

For interviews, just understand the logic behind `Merge Sort` and `Quick Sort`.

---
# **Merge Sort** is a **Divide and Conquer** algorithm.

It works by:
1. **Dividing** the list into smaller sublists.
2. **Sorting** each sublist.
3. **Merging** them back together in the correct order.

---

## How Merge Sort Works (Step-by-Step)

| Step | What Happens |
|:---|:---|
| 1 | Split the list into two halves. |
| 2 | Keep splitting each half until you reach lists with only **one element**. |
| 3 | Merge two sorted lists into one sorted list. |
| 4 | Keep merging until you have the full sorted list. |

---

## Example:

Suppose you want to sort `[5, 2, 4, 1, 3]`

 Splitting Phase:

```
[5, 2, 4, 1, 3] → [5, 2] and [4, 1, 3]
[5, 2] → [5] and [2]
[4, 1, 3] → [4] and [1, 3]
[1, 3] → [1] and [3]
```

 Merging Phase:

```
[5] and [2] → [2, 5]
[1] and [3] → [1, 3]
[4] and [1, 3] → [1, 3, 4]
[2, 5] and [1, 3, 4] → [1, 2, 3, 4, 5]
```

Sorted!

---

## Merge Sort Code (Simple Python Version)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    ## Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    ## Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
```

---


### ✅ Summary of Patterns

| Pattern         | Use Case                             |
|-----------------|--------------------------------------|
| Recursion       | Tree, divide & conquer               |
| Sliding Window  | Subarrays, strings, contiguous sums  |
| Two Pointers    | Sorted arrays, partitions            |
| Hashing         | Lookup, frequency, duplicates        |
| DP              | Optimized recursion                  |
| Prefix Sum      | Range sums, quick accumulations      |

---

**Mini Challenge**:  
Use the sliding window technique to return the longest substring without repeating characters.

---

Once you’re done practicing this, we can move on to **Step 8: File Handling, Parsing, and Regex**—useful for any test automation or scripting role. Shall we?
