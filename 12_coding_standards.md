# **coding standards** 
---

### ✅ **1. Write Clean, Readable Code**
- Use meaningful variable and function names: `user_count` > `uc`
- Keep functions small and focused: do **one** thing well
- Add comments only when necessary (your code should mostly explain itself)

---

### ✅ **2. Follow PEP 8 (Python Style Guide)**
- Use **4 spaces** per indentation level
- Keep line length ≤ 79 characters (or 120 if modern team allows)
- Leave **2 blank lines** between top-level functions
- Use **snake_case** for variable and function names
- Use **CapWords** (PascalCase) for class names

---

### ✅ **3. Structure Your Code**
- Group imports: built-in, third-party, your own
```python
import os
from collections import defaultdict

import numpy as np
```
- Put function definitions at the top, execution in `if __name__ == "__main__":`

---

### ✅ **4. Handle Edge Cases**
Always think:
- What if `input is empty`?
- What if `k = 0` or negative?
- What if `data is not sorted` or `null`?
You can add assert statements or raise exceptions.

---

### ✅ **5. Optimize**
- Avoid repeated work (like calling `sum()` in loops)
- Use appropriate data structures (`set` for lookups, `deque` for sliding window, etc.)

---

### ✅ **6. Test Your Code**
- Write minimal test cases (edge, base, and expected inputs)
- If time: use `unittest` or `pytest` style tests

---

### ✅ **7. Don’t Overcomplicate**
- Prefer clarity over cleverness (especially in interviews)
- If your code solves the problem clearly in 10 lines, that’s better than 6 cryptic ones

---

### ✅ **8. Time and Space Complexity Awareness**
- After coding, **state and analyze** your solution's complexity
- Example: "This is O(n) time and O(k) space due to the sliding window and hash map"

---

### ✅ **9. Use Pythonic Idioms (but don’t overuse)**
Examples:
- `if not list:` instead of `if len(list) == 0`
- `for idx, val in enumerate(arr):` instead of manual indexing

---

### ✅ **10. Graceful Error Handling**
Use `try/except` blocks if needed, especially around user inputs or external file/DB interactions.

---

Would you like me to review and refactor one of your earlier scripts using these principles?
