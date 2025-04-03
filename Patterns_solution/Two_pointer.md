# Two Pointer
Let’s start with the **Two Pointer** pattern. Imagine you have a row of toy blocks, each with a number on it, and they are arranged in order from the smallest number on the left to the biggest on the right. Now, suppose you want to find two blocks that add up to a magic number (a target). You can use two fingers (pointers) to help you look at the blocks—one finger at the beginning (left) and one at the end (right).

### How Does It Work?

1. **Start at the Ends:**  
   - Place one pointer at the very beginning of the list.  
   - Place the other pointer at the very end of the list.

2. **Add and Compare:**  
   - Look at the numbers where your two pointers are. Add them together.
   - If their sum is the magic number, you found your pair!
   - If the sum is too small, move the left pointer to the next block (because the list is sorted, the next block has a bigger number).
   - If the sum is too big, move the right pointer one block to the left (to get a smaller number).

3. **Repeat Until You Find a Pair or Pointers Cross:**  
   - Keep doing this until your two pointers meet or pass each other. If they pass each other, it means no pair was found.

### Python Code Example

Below is a simple Python code example that shows how the Two Pointer pattern works. In this example, we’re trying to find two numbers in a sorted list that add up to a target sum.

```python
def find_pair_with_target(nums, target):
    # Start with one pointer at the beginning (left) and one at the end (right)
    left = 0
    right = len(nums) - 1

    # Loop until the two pointers meet
    while left < right:
        # Calculate the sum of the numbers at the left and right pointers
        current_sum = nums[left] + nums[right]
        
        # Check if the current sum is the target
        if current_sum == target:
            return (nums[left], nums[right])  # We found the pair!
        
        # If the sum is less than the target, move the left pointer to the right
        if current_sum < target:
            left += 1
        # If the sum is greater than the target, move the right pointer to the left
        else:
            right -= 1

    # If we exit the loop, it means no pair was found
    return None

# Example usage:
numbers = [1, 2, 3, 4, 6]  # A sorted list of numbers
target_sum = 6
result = find_pair_with_target(numbers, target_sum)

if result:
    print("Pair found:", result)
else:
    print("No pair found that adds up to", target_sum)
```

### Breaking Down the Code

- **Function Definition:** We create a function called `find_pair_with_target` that takes a sorted list `nums` and a `target` number.
- **Pointers Initialization:**  
  - `left` starts at the first element (index 0).  
  - `right` starts at the last element (index `len(nums) - 1`).
- **Loop:** The loop runs while the left pointer is before the right pointer.
- **Comparison:**  
  - We add the numbers at `left` and `right`.  
  - If their sum is exactly the target, we return those numbers.
  - If the sum is too small, we move `left` one step right.
  - If the sum is too large, we move `right` one step left.
- **Result:** If no pair is found by the time the pointers meet, the function returns `None`.

This approach is simple and efficient because you only go through the list once. If you understand this, you’re ready to move on to more exciting patterns! Let me know if you’d like to explore another example or have any questions.