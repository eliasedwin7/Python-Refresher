Let’s go! 🧙‍♂️ Now we dive into **7. Subset / Subset Sum / Power Set** — this one’s all about making combinations. Think of it like playing dress-up with all your toys, mixing and matching outfits.

---

### 🧠 Imagine You Are...

You have 3 superhero stickers: 🦸, 🧙, 🧛  
You want to find **all the combinations** of stickers you can stick on your book — including using none at all!

These combinations are called the **Power Set**.

---

### 🎯 What is a Subset?

A subset is **any group of items taken from a set**, possibly empty.  
The Power Set is the **set of all subsets**.

Example:  
Input: `[1, 2]`  
Output: `[[], [1], [2], [1, 2]]`

---

### 🛠 Python Code: Backtracking Method

```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(list(current))  # Add current subset to result

        for i in range(start, len(nums)):
            current.append(nums[i])         # Choose
            backtrack(i + 1, current)       # Explore
            current.pop()                   # Un-choose (backtrack)

    backtrack(0, [])
    return result

# Example
nums = [1, 2, 3]
print("All subsets:", subsets(nums))
```

---

### 🪄 Like You're a Kid:

You’re building LEGO teams:
- Sometimes you use no bricks.
- Sometimes just 1.
- Sometimes all of them.
You try **every possible combo**!

---

### 💡 Related Variants:

#### ✅ Subset Sum:
Find if any subset adds up to a target value.

```python
def subset_sum(nums, target):
    def dfs(i, total):
        if total == target:
            return True
        if i == len(nums) or total > target:
            return False
        return dfs(i + 1, total + nums[i]) or dfs(i + 1, total)

    return dfs(0, 0)

# Example
print("Subset sum exists?", subset_sum([3, 4, 5, 2], 9))
```

#### ✅ Combination Sum:
Find all subsets that sum to a target.

---

### 💡 Where It’s Used:

- Decision trees
- Permissions/flags
- Subset sum problems in dynamic programming
- Game logic (equip this, skip that)

---

🔥 This one's a classic in interviews and competitions. Want to try problems using this pattern?

Next: **8. Sliding Window** — the final one on your pattern sheet! Ready?