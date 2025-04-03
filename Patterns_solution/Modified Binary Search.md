Alright! Now we’re onto **6. Modified Binary Search** — same powerful tool, but now it’s wearing a cool disguise. 🕵️‍♂️

---

### 🧠 Imagine You Are...

Looking for a book in a shelf that's **almost sorted**, but someone rotated the middle section. It’s not in perfect order, but still not a mess. You can’t use normal Binary Search. So… we **tweak the rules a little**. That’s Modified Binary Search!

---

### 🔍 What Is Modified Binary Search?

It’s just **Binary Search with a twist**—still fast (`O(log n)`), but used when:
- The array is **rotated**.
- You want **first/last position** of a number.
- You’re searching by **condition**, not exact match.

---

### 🌪 Example Problem: Find a number in a rotated sorted array

Input:  
`[4, 5, 6, 7, 0, 1, 2]`, target = `0`  
Output: `4` (index of 0)

---

### 🛠 Python Code

```python
def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Search left side
            else:
                left = mid + 1   # Search right side
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Search right side
            else:
                right = mid - 1  # Search left side

    return -1  # Not found

# Example
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print("Target found at index:", search_rotated_array(nums, target))
```

---

### 🪄 Like You're a Kid:

- You have a toy box sorted in a circle.
- You still try to find your toy by checking the **middle**.
- But now you also check **which side is neat**, and search only that part.

---

### 💡 Other Modified Binary Searches:

- **First/last position** of a number:
  → Great for duplicates.
- **Find smallest/largest with condition**:
  → Like “first true value” in a list of booleans.

---

### Bonus Use Case:
Want to **find the square root** of a number without using `math.sqrt()`? Use binary search on the range!

---

Up next: **7. Subset / Subset Sum / Power Set** — ready to generate some magic combinations?