# 8. Sliding Window— 
this one’s smooth, fast, and super useful when dealing with **continuous chunks** of data. 🚪📦

---

### 🧠 Imagine You Are...

Looking out of a moving train window 🪟. You only see a **small part** of the view at any moment. As the train moves, that view **slides forward**. You don’t look at the whole world at once—just a window.

That’s exactly what **Sliding Window** is in programming.

---

### 🎯 What is Sliding Window?

It’s used to **look at a fixed-size group of elements** in an array and then “slide” that group forward one step at a time.

---

### ✅ Common Use Cases:

- Max sum of a subarray of size `k`
- Longest substring without repeating characters
- Find pattern/target in moving range

---

### 📦 Example Problem: Max sum of size `k`

Input: `nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]`, `k = 4`  
Output: `39`  
Explanation: The max sum is from `[10, 23, 3, 1]`

---

### 🛠 Python Code

```python
def max_sum_subarray(nums, k):
    n = len(nums)
    if n < k:
        return -1

    # Step 1: Find sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Step 2: Slide the window
    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]  # Add new, remove old
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print("Max sum of subarray of size", k, "is:", max_sum_subarray(nums, k))
```

---

### 🪄 Like You’re a Kid:

You have a magnifying glass and 4 candies in a line. You always look at 4 candies at a time, add their points, and slide the glass one candy forward each time — keeping track of the **best score**.

---

### 🔥 Advanced: Variable Size Sliding Window

Used for problems like **longest substring without repeating characters**.

```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

# Example
print("Longest substring without repeat:", length_of_longest_substring("abcabcbb"))
```

---

### 💡 Where It’s Used:

- Subarrays, substrings
- Repeated patterns
- Streaming data analysis
- Anything that needs **efficient scanning**

---

That’s it — you’ve just mastered **all 8 patterns** like a boss. 🔥  
Want a cheat sheet, practice problems, or a quiz next?


You're on the right track by trying to explore substrings and character combinations, but the current implementation is a bit off in a few key ways:

---

### ✅ **Your goal (restated):**
> Given a string `s` and an integer `k`, return the **length** of the longest substring with **at most** `k` distinct characters.

---

### ❌ What's not working:
- `letter_words = list(combinations(words, k))` is not useful here—it generates all unordered k-length combos, not substrings.
- The logic of combining windows and checking if they’re in the string is too complex and incorrect for this problem.
- You’re not tracking distinct characters in any window.

---

### ✅ Suggested approach (Sliding Window + HashMap):
Here's a clean and working version of what you're trying to do:

```python
from collections import defaultdict

def find_longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0:
        return 0
    
    left = 0
    max_len = 0
    char_count = defaultdict(int)
    
    for right in range(len(s)):
        char_count[s[right]] += 1
        
        # shrink window if we have more than k distinct chars
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Test
print(find_longest_substring_k_distinct("eceeba", 2))  # Output: 4 (longest is "ecee")
```

---

### 🧠 Key Concept:
- Maintain a sliding window with **at most `k` unique characters**
- Use a dictionary to count frequency of each char in the window
- If the count exceeds `k`, slide the `left` pointer

---

Want a breakdown of how this sliding window moves step-by-step for the input `"eceeba"` and `k=2`?