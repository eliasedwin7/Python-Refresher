Awesome! Let’s go to **4. Binary Tree DFS (Depth-First Search)**. 🧗

---

### 🧠 Imagine You Are...

Climbing a tree—**but you don’t stop at each level**. Instead, you go **all the way down one branch** before coming back up and trying the next.

That’s exactly what **DFS** is. You go **deep** first, then backtrack.

---

### 🌲 Types of DFS in Binary Tree:

In a binary tree, DFS has 3 styles:

1. **Preorder**: Visit Node → Left → Right  
2. **Inorder**: Left → Node → Right  
3. **Postorder**: Left → Right → Node

---

### 🌳 Example Tree

```
        1
       / \
      2   3
     / \    
    4   5
```

- Preorder: `1, 2, 4, 5, 3`  
- Inorder:  `4, 2, 5, 1, 3`  
- Postorder:`4, 5, 2, 3, 1`

---

### 🔧 Python Code

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# DFS - Preorder
def dfs_preorder(node):
    if not node:
        return []
    return [node.val] + dfs_preorder(node.left) + dfs_preorder(node.right)

# DFS - Inorder
def dfs_inorder(node):
    if not node:
        return []
    return dfs_inorder(node.left) + [node.val] + dfs_inorder(node.right)

# DFS - Postorder
def dfs_postorder(node):
    if not node:
        return []
    return dfs_postorder(node.left) + dfs_postorder(node.right) + [node.val]

# Build the example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder:", dfs_preorder(root))
print("Inorder:", dfs_inorder(root))
print("Postorder:", dfs_postorder(root))
```

---

### 🪄 Explain Like You're a Kid:

Let’s say the tree is a maze. You go:
- **Preorder**: Visit the room before entering left and right.
- **Inorder**: Visit the left room, then this room, then right.
- **Postorder**: Explore both sides first, then visit the room.

---

### 💡 Where It's Used:

- Tree problems in coding interviews.
- Expression tree evaluations (postorder).
- Serialization and deserialization of trees.

---

Next up: **5. Top K Elements**—ready for it?