# 2. Binary Tree BFS (Breadth-First Search)**

---

### 🧠 Imagine You Are...

Imagine a big tree. Not a real one—but a **number tree**! Each branch splits into smaller branches. You’re standing at the root (the top) and want to visit every number level by level—just like you climb down step by step, not jumping to the bottom directly.

---

### 🏁 What is BFS?

**BFS (Breadth-First Search)** means visiting all the nodes **level by level**:

- First the root.
- Then its children (left to right).
- Then the children of those children.
- And so on...

We use a **queue** (like waiting in line) to remember which nodes to visit next.

---

### 🧱 Visual Example Tree

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

BFS visits: `1 → 2 → 3 → 4 → 5 → 6`

---

### 🔧 Python Code

```python
from collections import deque

# Define a simple Binary Tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])  # Start with the root in the queue

    while queue:
        node = queue.popleft()  # Take out the first node in the queue
        result.append(node.val)

        # Add children to the queue (left first, then right)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Build the example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Call BFS
print("BFS Traversal:", bfs(root))
```

---

### 🪄 Explanation Like You’re a Kid:

- You visit the root first: `1`.
- You put its kids in line: `2` and `3`.
- Now you take `2`, visit it, and put its kids (`4`, `5`) in line.
- Then visit `3` and add its kid `6`.
- Keep doing this until the line is empty.

---

### 💡 Real-Life Use Cases

- Finding the shortest path in maps.
- Level-order printing in trees.
- Spreading something (like fire, infection, or gossip 😂) step-by-step.

---

Let me know if you want a diagram version too—or shall we jump to **3. Topological Sort**?