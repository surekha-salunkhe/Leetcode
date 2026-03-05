# Tree BFS Practice: Level-Order Traversal

BFS on trees processes nodes **level by level**, from top to bottom, left to right. This is also called **level-order traversal**.

**When to use BFS over DFS:**
- Need to process level by level
- Find something at the shallowest depth
- Need to know the level/depth of nodes
- Connect nodes at the same level

**Core Pattern:**
```cpp
void bfs(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();  // nodes at current level
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            
            // Process node
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        // Finished one level
    }
}
```

---

## Part 1: Basic Level-Order Traversal

### Problem 1: Binary Tree Level Order Traversal

Return the level order traversal as a list of lists.

```
        3
       / \
      9  20
         / \
        15  7

level_order(root) → [[3], [9, 20], [15, 7]]
```

---

### Problem 2: Binary Tree Level Order Traversal II

Return level order traversal from bottom to top.

```
        3
       / \
      9  20
         / \
        15  7

level_order_bottom(root) → [[15, 7], [9, 20], [3]]
```

**Hint:** Same as level order, then reverse. Or insert at front.

---

### Problem 3: N-ary Tree Level Order Traversal

Return level order traversal of an N-ary tree.

```
          1
        / | \
       3  2  4
      / \
     5   6

level_order(root) → [[1], [3, 2, 4], [5, 6]]
```

---

### Problem 4: Binary Tree Zigzag Level Order Traversal

Traverse level by level, alternating direction (left-to-right, then right-to-left).

```
        3
       / \
      9  20
         / \
        15  7

zigzag_level_order(root) → [[3], [20, 9], [15, 7]]
```

---

### Problem 5: Average of Levels in Binary Tree

Return the average value of nodes at each level.

```
        3
       / \
      9  20
         / \
        15  7

average_of_levels(root) → [3.0, 14.5, 11.0]
```

---

### Problem 6: Sum of Nodes at Each Level

Return the sum of values at each level.

```
        1
       / \
      2   3
     / \   \
    4   5   6

level_sums(root) → [1, 5, 15]
```

---

### Problem 7: Largest Value in Each Row

Find the largest value in each row.

```
        1
       / \
      3   2
     / \   \
    5   3   9

largest_values(root) → [1, 3, 9]
```

---

### Problem 8: Find Largest Value in Each Tree Row (Same as above)

```
        1
       / \
      2   3

largest_values(root) → [1, 3]
```

---

## Part 2: Views and Boundaries

### Problem 9: Binary Tree Right Side View

Return values visible from the right side (last node at each level).

```
        1
       / \
      2   3
       \   \
        5   4

right_side_view(root) → [1, 3, 4]
```

**Pattern:** BFS, take the last node of each level. Or DFS with right-first traversal.

---

### Problem 10: Binary Tree Left Side View

Return values visible from the left side (first node at each level).

```
        1
       / \
      2   3
       \   \
        5   4

left_side_view(root) → [1, 2, 5]
```

---

### Problem 11: Find Bottom Left Tree Value

Find the leftmost value in the last row.

```
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

find_bottom_left(root) → 7
```

---

### Problem 12: Find Bottom Right Tree Value

Find the rightmost value in the last row.

```
        1
       / \
      2   3
     /   / \
    4   5   6

find_bottom_right(root) → 6
```

---

### Problem 13: Boundary of Binary Tree

Return the boundary of the tree: left boundary, leaves, and right boundary (in order, no duplicates).

```
          1
         / \
        2   3
       / \   \
      4   5   6
         / \
        7   8

boundary(root) → [1, 2, 4, 7, 8, 6, 3]
# Left boundary: 1, 2, 4
# Leaves: 4, 7, 8, 6  (4 already counted)
# Right boundary (reverse): 6, 3  (6 already counted)
```

---

## Part 3: Depth and Distance

### Problem 14: Maximum Depth of Binary Tree (BFS approach)

Find maximum depth using BFS.

```
        3
       / \
      9  20
         / \
        15  7

max_depth(root) → 3
```

**Pattern:** Count levels during BFS.

---

### Problem 15: Minimum Depth of Binary Tree

Find minimum depth (shortest root-to-leaf path).

```
        3
       / \
      9  20
         / \
        15  7

min_depth(root) → 2   # Path: 3 → 9
```

**BFS advantage:** Stop as soon as you find the first leaf.

---

### Problem 16: Find All Nodes at Distance K from Target

Given a target node, find all nodes at distance k from it.

```
            3
           / \
          5   1
         / \ / \
        6  2 0  8
          / \
         7   4

Target = 5, K = 2
Result → [7, 4, 1]
```

**Hint:** Convert tree to graph (add parent pointers), then BFS from target.

---

### Problem 17: Deepest Leaves Sum

Return the sum of values of the deepest leaves.

```
          1
         / \
        2   3
       / \   \
      4   5   6
     /         \
    7           8

deepest_leaves_sum(root) → 15   # 7 + 8
```

---

### Problem 18: Maximum Level Sum of a Binary Tree

Return the level with the maximum sum (1-indexed).

```
          1
         / \
        7   0
       / \
      7  -8

max_level_sum(root) → 2   # Level 2 sum = 7
```

---

## Part 4: Connecting Nodes

### Problem 19: Populating Next Right Pointers in Each Node

Connect each node to its next right node at the same level. Tree is a **perfect binary tree**.

```
        1                   1 → NULL
       / \                 / \
      2   3      →        2 → 3 → NULL
     / \ / \             / \ / \
    4  5 6  7           4→5→6→7 → NULL
```

---

### Problem 20: Populating Next Right Pointers in Each Node II

Same as above, but tree may not be perfect (any binary tree).

```
        1                   1 → NULL
       / \                 / \
      2   3      →        2 → 3 → NULL
     / \   \             / \   \
    4   5   7           4→5 → → 7 → NULL
```

---

### Problem 21: Connect All Siblings

Connect all nodes at the same level using next pointers.

```
        1                   1 → 2 → 3 → 4 → 5 → 6 → 7 → NULL
       / \
      2   3
     / \ / \
    4  5 6  7
```

---

## Part 5: Cousins and Relatives

### Problem 22: Cousins in Binary Tree

Two nodes are cousins if they are at the same depth but have different parents. Check if two values are cousins.

```
        1
       / \
      2   3
     /     \
    4       5

are_cousins(root, 4, 5) → True   # Same depth, different parents
are_cousins(root, 4, 3) → False  # Different depths
```

---

### Problem 23: Cousins in Binary Tree II

Replace each node's value with the sum of all its cousins' values.

```
          5
         / \
        4   9
       / \ / \
      1  10 7 null

replace_with_cousins(root) →

          0
         / \
        7   4
       / \ /
      7  7 11
```

---

### Problem 24: Check if Two Nodes are Siblings

Check if two nodes have the same parent.

```
        1
       / \
      2   3
     / \
    4   5

are_siblings(root, 4, 5) → True
are_siblings(root, 2, 3) → True
are_siblings(root, 4, 3) → False
```

---

## Part 6: Tree Completeness and Structure

### Problem 25: Check Completeness of a Binary Tree

A complete binary tree has all levels full except possibly the last, which is filled left to right.

```
        1
       / \
      2   3
     / \ /
    4  5 6

is_complete(root) → True
```

```
        1
       / \
      2   3
     / \   \
    4   5   7

is_complete(root) → False   # Gap at level 3
```

**Pattern:** BFS, once you see a null, all remaining nodes must be null.

---

### Problem 26: Count Complete Tree Nodes

Count nodes in a complete binary tree. Try to do better than O(n).

```
          1
         / \
        2   3
       / \ /
      4  5 6

count_nodes(root) → 6
```

**Hint:** Compare left and right heights. If equal, left subtree is perfect.

---

### Problem 27: Maximum Width of Binary Tree

Find the maximum width (number of nodes between the leftmost and rightmost non-null nodes at any level, including nulls).

```
          1
         / \
        3   2
       / \   \
      5   3   9

max_width(root) → 4   # Level 3: width from 5 to 9 = 4
```

**Hint:** Assign indices (root=1, left child=2i, right child=2i+1).

---

### Problem 28: Add One Row to Tree

Add a row of nodes with given value at given depth.

```
        4
       / \
      2   6
     / \ / \
    3  1 5  null

add_row(root, 1, 2) →

          4
         / \
        1   1
       /     \
      2       6
     / \     /
    3   1   5
```

---

## Part 7: Deletion and Modification

### Problem 29: Even Odd Tree

Check if a tree is an "even-odd tree":
- Level 0: all odd values, strictly increasing
- Level 1: all even values, strictly decreasing
- Alternates...

```
          1
         / \
        10   4
       /  \ / \
      3  7 9  12

is_even_odd_tree(root) → True
```

---

### Problem 30: Flip Binary Tree To Match Preorder Traversal

Flip nodes (swap left and right children) to match a given preorder traversal. Return list of flipped node values, or [-1] if impossible.

```
        1
       / \
      2   3

flip_match(root, [1, 3, 2]) → [1]   # Flip node 1
flip_match(root, [1, 2, 3]) → []    # No flips needed
```

---

### Problem 31: Complete Binary Tree Inserter

Design a data structure that inserts into a complete binary tree, maintaining completeness.

```
CBTInserter(root)
insert(v)  → returns parent's value
get_root() → returns root
```

**Pattern:** Use BFS to find the first node with an empty child slot.

---

## Part 8: Miscellaneous BFS Problems

### Problem 32: Binary Tree Vertical Order Traversal

Return nodes grouped by vertical column (left to right, top to bottom within each column).

```
        3
       / \
      9  20
         / \
        15  7

vertical_order(root) → [[9], [3, 15], [20], [7]]
```

**Hint:** Track column index. BFS ensures top-to-bottom order.

---

### Problem 33: Vertical Order Traversal of a Binary Tree

Same as above, but if two nodes have the same position, sort by value.

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7

vertical_traversal(root) → [[4], [2], [1, 5, 6], [3], [7]]
```

---

### Problem 34: Print Binary Tree

Return a 2D representation of the tree.

```
        1
       / \
      2   null

print_tree(root) →
[
  ["", "1", ""],
  ["2", "", ""]
]
```

---

### Problem 35: Find Nearest Right Node in Binary Tree

Find the nearest node to the right of a given node at the same level.

```
          1
         / \
        2   3
         \   \
          4   5
         /
        6

find_nearest_right(root, 4) → 5
find_nearest_right(root, 5) → null
find_nearest_right(root, 6) → null
```

---

### Problem 36: Symmetric Tree (BFS approach)

Check if a tree is symmetric using BFS.

```
        1
       / \
      2   2
     / \ / \
    3  4 4  3

is_symmetric(root) → True
```

**Pattern:** Compare pairs of nodes from left and right subtrees.

---

### Problem 37: Same Tree (BFS approach)

Check if two trees are identical using BFS.

```
    1         1
   / \       / \
  2   3     2   3

is_same(p, q) → True
```

---

### Problem 38: Invert Binary Tree (BFS approach)

Invert a binary tree using BFS.

```
        4                 4
       / \               / \
      2   7     →       7   2
     / \ / \           / \ / \
    1  3 6  9         9  6 3  1
```

---

### Problem 39: Univalued Binary Tree

Check if all nodes have the same value.

```
        1
       / \
      1   1
     / \   \
    1   1   1

is_univalued(root) → True
```

---

### Problem 40: Count Good Nodes (BFS approach)

A node is "good" if there's no node with a greater value on the path from root to it.

```
        3
       / \
      1   4
     /   / \
    3   1   5

good_nodes(root) → 4   # Nodes: 3, 3, 4, 5
```

---

## Part 9: Multi-tree and Forest Problems

### Problem 41: Merge Two Binary Trees (BFS approach)

Merge two trees by adding overlapping values.

```
     1              2
    / \            / \
   3   2          1   3
  /                \   \
 5                  4   7

merge(t1, t2) →

         3
        / \
       4   5
      / \   \
     5   4   7
```

---

### Problem 42: Leaf-Similar Trees

Two trees are leaf-similar if their leaf sequences are the same.

```
Tree 1:        Tree 2:
    3              3
   / \            / \
  5   1          5   1
 / \   \        / \   \
6   2   9      6   7   4
   / \
  7   4

leaf_similar(root1, root2) → True
# Both have leaves: [6, 7, 4, 9] -- wait, let me fix this

Actually:
Tree 1 leaves: 6, 7, 4, 9
Tree 2 leaves: 6, 7, 4

leaf_similar(root1, root2) → False
```

---

### Problem 43: All Possible Full Binary Trees

Generate all full binary trees with n nodes (every node has 0 or 2 children).

```
all_possible_fbt(7) → list of 5 different full binary trees
```

---

### Problem 44: Find Elements in a Contaminated Binary Tree

Tree was contaminated (all values set to -1). Recover it where root = 0, left child = 2*x+1, right child = 2*x+2. Then answer find(target) queries.

```
        -1                    0
       /  \                  / \
     -1   -1       →        1   2
     /                     /
   -1                     3

find(1) → True
find(3) → True
find(5) → False
```

---

### Problem 45: Sum of Nodes with Even-Valued Grandparent

Find sum of nodes whose grandparent has an even value.

```
            6
           / \
          7   8
         / \ / \
        2  7 1  3
       /  / \    \
      9  1   4    5

sum_even_grandparent(root) → 18   # 2+7+1+3+5 = 18? Let me verify
# Nodes with even grandparent (6 or 8):
# 6's grandchildren: 2, 7, 1, 3
# 8's grandchildren: 1, 4, 5
# Sum = 2+7+1+3+1+4+5 = 23
```

---

## Strategies and Patterns

### Standard BFS Template

```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            currentLevel.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(currentLevel);
    }
    return result;
}
```

### BFS with Index Tracking

```cpp
// For problems like max width, vertical order
queue<pair<TreeNode*, int>> q;  // {node, index}
q.push({root, 0});

while (!q.empty()) {
    auto [node, idx] = q.front();
    q.pop();
    
    if (node->left) q.push({node->left, 2*idx});
    if (node->right) q.push({node->right, 2*idx + 1});
}
```

### BFS with Parent Tracking

```cpp
// For problems needing to go "up" the tree
unordered_map<TreeNode*, TreeNode*> parent;
queue<TreeNode*> q;
q.push(root);

while (!q.empty()) {
    TreeNode* node = q.front();
    q.pop();
    
    if (node->left) {
        parent[node->left] = node;
        q.push(node->left);
    }
    if (node->right) {
        parent[node->right] = node;
        q.push(node->right);
    }
}
```

### When to Use BFS vs DFS

| Use BFS When | Use DFS When |
|--------------|--------------|
| Level-by-level processing | Path from root to leaf |
| Finding minimum depth | Need to backtrack |
| Connecting nodes at same level | Postorder processing needed |
| Shortest path in tree | Space is very limited (BFS uses more) |
| Right/left side views | Preorder/inorder/postorder needed |

### Common Patterns Summary

| Pattern | Problems |
|---------|----------|
| Level grouping | Level order, averages, sums |
| First/last of level | Right view, left view, bottom left |
| Track depth/level | Min depth, max depth, level sum |
| Connect at same level | Next pointers |
| Column tracking | Vertical order |
| Index tracking | Max width |
| Early termination | Min depth (stop at first leaf) |

### Edge Cases

1. **Empty tree** (`root == nullptr`)
2. **Single node** (one level only)
3. **Skewed tree** (one node per level)
4. **Perfect tree** (all levels full)
5. **Complete vs incomplete** (for completeness checks)

---

Good luck! Start with Part 1 for basic level-order traversal, then Part 2 for view problems. The standard BFS template handles 80% of these problems — the key is knowing what to track at each level.
