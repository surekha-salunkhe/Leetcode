# Tree DFS Practice

DFS (Depth-First Search) on trees explores as deep as possible before backtracking. The three classic traversals:

- **Preorder:** Node → Left → Right (process node first)
- **Inorder:** Left → Node → Right (process node in middle)
- **Postorder:** Left → Right → Node (process node last)

The key insight: most tree problems are solved by combining results from left and right subtrees.

---

## Part 1: Basic Traversals

### Problem 1: Preorder Traversal

Return the preorder traversal of a binary tree.

```
        1
         \
          2
         /
        3

preorder([1,null,2,3]) → [1, 2, 3]
```

**Pattern:**
```cpp
void preorder(Node* node, vector<int>& result) {
    if (!node) return;
    result.push_back(node->val);  // process
    preorder(node->left, result);  // left
    preorder(node->right, result); // right
}
```

---

### Problem 2: Inorder Traversal

Return the inorder traversal of a binary tree.

```
        1
         \
          2
         /
        3

inorder([1,null,2,3]) → [1, 3, 2]
```

---

### Problem 3: Postorder Traversal

Return the postorder traversal of a binary tree.

```
        1
         \
          2
         /
        3

postorder([1,null,2,3]) → [3, 2, 1]
```

---

### Problem 4: N-ary Tree Preorder Traversal

Return the preorder traversal of an N-ary tree.

```
          1
        / | \
       3  2  4
      / \
     5   6

preorder(root) → [1, 3, 5, 6, 2, 4]
```

---

### Problem 5: N-ary Tree Postorder Traversal

Return the postorder traversal of an N-ary tree.

```
          1
        / | \
       3  2  4
      / \
     5   6

postorder(root) → [5, 6, 3, 2, 4, 1]
```

---

## Part 2: Tree Properties

### Problem 6: Maximum Depth of Binary Tree

Find the maximum depth (number of nodes on the longest root-to-leaf path).

```
        3
       / \
      9  20
         / \
        15  7

max_depth(root) → 3
```

**Pattern:**
```cpp
int maxDepth(Node* node) {
    if (!node) return 0;
    return 1 + max(maxDepth(node->left), maxDepth(node->right));
}
```

---

### Problem 7: Minimum Depth of Binary Tree

Find the minimum depth (shortest root-to-leaf path).

```
        3
       / \
      9  20
         / \
        15  7

min_depth(root) → 2   # Path: 3 → 9
```

**Careful:** A node with only one child is NOT a leaf.

---

### Problem 8: Maximum Depth of N-ary Tree

Find the maximum depth of an N-ary tree.

```
          1
        / | \
       3  2  4
      / \
     5   6

max_depth(root) → 3
```

---

### Problem 9: Diameter of Binary Tree

Find the diameter — the longest path between any two nodes (may not pass through root).

```
          1
         / \
        2   3
       / \
      4   5

diameter(root) → 3   # Path: 4 → 2 → 1 → 3 or 5 → 2 → 1 → 3
```

**Key insight:** At each node, the longest path through it = left_height + right_height. Track the maximum across all nodes.

---

### Problem 10: Balanced Binary Tree

Check if a tree is height-balanced (left and right subtree depths differ by at most 1, for every node).

```
        3
       / \
      9  20
         / \
        15  7

is_balanced(root) → True
```

```
          1
         / \
        2   2
       / \
      3   3
     / \
    4   4

is_balanced(root) → False
```

---

### Problem 11: Same Tree

Check if two trees are structurally identical with same values.

```
    1         1
   / \       / \
  2   3     2   3

same_tree(p, q) → True
```

---

### Problem 12: Symmetric Tree

Check if a tree is symmetric around its center.

```
        1
       / \
      2   2
     / \ / \
    3  4 4  3

is_symmetric(root) → True
```

---

### Problem 13: Subtree of Another Tree

Check if tree t is a subtree of tree s.

```
s:      3          t:   4
       / \              / \
      4   5            1   2
     / \
    1   2

is_subtree(s, t) → True
```

---

### Problem 14: Count Complete Tree Nodes

Count nodes in a complete binary tree. Try to do better than O(n).

```
          1
         / \
        2   3
       / \ /
      4  5 6

count_nodes(root) → 6
```

**Hint:** If left and right heights are equal, left subtree is perfect. Otherwise, right subtree is perfect (of height h-1).

---

### Problem 15: Invert Binary Tree

Invert (mirror) a binary tree.

```
        4                 4
       / \               / \
      2   7     →       7   2
     / \ / \           / \ / \
    1  3 6  9         9  6 3  1

invert(root) → inverted tree
```

---

## Part 3: Path Problems

### Problem 16: Path Sum

Check if there's a root-to-leaf path with a given sum.

```
          5
         / \
        4   8
       /   / \
      11  13  4
     / \       \
    7   2       1

has_path_sum(root, 22) → True   # 5 → 4 → 11 → 2
```

---

### Problem 17: Path Sum II

Find all root-to-leaf paths that sum to target.

```
          5
         / \
        4   8
       /   / \
      11  13  4
     / \     / \
    7   2   5   1

path_sum(root, 22) → [[5,4,11,2], [5,8,4,5]]
```

---

### Problem 18: Path Sum III

Count paths that sum to target. Path can start and end anywhere (but must go downward).

```
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1

path_sum(root, 8) → 3
# Paths: 5→3, 5→2→1, -3→11
```

**Hint:** Use prefix sum technique with a hashmap.

---

### Problem 19: Binary Tree Maximum Path Sum

Find the maximum path sum. Path can start and end at any nodes.

```
        -10
        /  \
       9   20
          /  \
         15   7

max_path_sum(root) → 42   # Path: 15 → 20 → 7
```

---

### Problem 20: Sum Root to Leaf Numbers

Each root-to-leaf path represents a number. Return the total sum.

```
        1
       / \
      2   3

sum_numbers(root) → 25   # 12 + 13 = 25
```

```
        4
       / \
      9   0
     / \
    5   1

sum_numbers(root) → 1026   # 495 + 491 + 40 = 1026
```

---

### Problem 21: Binary Tree Paths

Return all root-to-leaf paths as strings.

```
        1
       / \
      2   3
       \
        5

binary_tree_paths(root) → ["1->2->5", "1->3"]
```

---

### Problem 22: Longest Univalue Path

Find the longest path where all nodes have the same value.

```
          5
         / \
        4   5
       / \   \
      1   1   5

longest_univalue_path(root) → 2   # Path: 5 → 5 → 5 (right side)
```

---

### Problem 23: Sum of Left Leaves

Find the sum of all left leaves.

```
        3
       / \
      9  20
         / \
        15  7

sum_of_left_leaves(root) → 24   # 9 + 15
```

---

## Part 4: Tree Modification

### Problem 24: Flatten Binary Tree to Linked List

Flatten tree to a "linked list" using right pointers (preorder).

```
        1
       / \
      2   5
     / \   \
    3   4   6

flatten(root) →

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
```

---

### Problem 25: Delete Leaves With a Given Value

Delete all leaf nodes with the given value. Repeat until no such leaves exist.

```
          1
         / \
        2   3
       /   / \
      2   2   4

remove_leaf_nodes(root, 2) →

          1
           \
            3
             \
              4
```

---

### Problem 26: Merge Two Binary Trees

Merge two trees by adding overlapping node values.

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

### Problem 27: Prune Binary Tree (Binary Tree Pruning)

Remove subtrees that don't contain a 1.

```
          1
         / \
        0   1
       / \   \
      0   0   1

prune_tree(root) →

          1
           \
            1
             \
              1
```

---

### Problem 28: Trim a Binary Search Tree

Trim BST so all nodes are within [low, high].

```
        3
       / \
      0   4
       \
        2
       /
      1

trim_bst(root, 1, 3) →

        3
       /
      2
     /
    1
```

---

## Part 5: Ancestor Problems

### Problem 29: Lowest Common Ancestor of a Binary Tree

Find the LCA of two nodes.

```
            3
           / \
          5   1
         / \ / \
        6  2 0  8
          / \
         7   4

lca(root, 5, 1) → 3
lca(root, 5, 4) → 5
```

**Pattern:** If current node is p or q, return it. Otherwise, search left and right. If both return non-null, current is LCA.

---

### Problem 30: Lowest Common Ancestor of a BST

Find LCA in a binary search tree.

```
            6
           / \
          2   8
         / \ / \
        0  4 7  9
          / \
         3   5

lca(root, 2, 8) → 6
lca(root, 2, 4) → 2
```

**BST property:** If both p and q are smaller, go left. If both larger, go right. Otherwise, current is LCA.

---

### Problem 31: Kth Ancestor of a Tree Node

Preprocess a tree to answer "kth ancestor" queries efficiently.

```
          0
         / \
        1   2
       / \
      3   4

get_kth_ancestor(3, 1) → 1
get_kth_ancestor(3, 2) → 0
get_kth_ancestor(3, 3) → -1
```

---

### Problem 32: Maximum Difference Between Node and Ancestor

Find the maximum value |a.val - b.val| where a is an ancestor of b.

```
            8
           / \
          3   10
         / \    \
        1   6    14
           / \   /
          4   7 13

max_ancestor_diff(root) → 7   # |8 - 1| = 7
```

---

## Part 6: BST-Specific Problems

### Problem 33: Validate Binary Search Tree

Check if a tree is a valid BST.

```
        2
       / \
      1   3
      
is_valid_bst(root) → True
```

```
        5
       / \
      1   4
         / \
        3   6
        
is_valid_bst(root) → False   # 4 is not > 5
```

**Pattern:** Pass down valid range (min, max) to each node.

---

### Problem 34: Search in a Binary Search Tree

Find a node with given value in a BST.

```
        4
       / \
      2   7
     / \
    1   3

search_bst(root, 2) → subtree rooted at 2
```

---

### Problem 35: Insert into a Binary Search Tree

Insert a value into a BST.

```
        4
       / \
      2   7
     / \
    1   3

insert_bst(root, 5) →

        4
       / \
      2   7
     / \ /
    1  3 5
```

---

### Problem 36: Delete Node in a BST

Delete a node from a BST while maintaining BST property.

```
        5
       / \
      3   6
     / \   \
    2   4   7

delete_node(root, 3) →

        5
       / \
      4   6
     /     \
    2       7
```

---

### Problem 37: Kth Smallest Element in a BST

Find the kth smallest element.

```
        3
       / \
      1   4
       \
        2

kth_smallest(root, 1) → 1
kth_smallest(root, 3) → 3
```

**Hint:** Inorder traversal of BST gives sorted order.

---

### Problem 38: Convert Sorted Array to BST

Create a height-balanced BST from a sorted array.

```
sorted_array_to_bst([-10,-3,0,5,9]) →

        0
       / \
     -3   9
     /   /
   -10  5
```

---

### Problem 39: Recover Binary Search Tree

Two nodes were swapped by mistake. Recover the BST.

```
        1              3
       /              /
      3      →       1
       \              \
        2              2
```

**Hint:** Inorder traversal should be sorted. Find the two out-of-place elements.

---

### Problem 40: Two Sum IV - Input is a BST

Check if there exist two elements in BST that sum to k.

```
        5
       / \
      3   6
     / \   \
    2   4   7

find_target(root, 9) → True   # 2 + 7 = 9
find_target(root, 28) → False
```

---

## Part 7: Tree Construction

### Problem 41: Construct Binary Tree from Preorder and Inorder

Build tree from preorder and inorder traversals.

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

build_tree(preorder, inorder) →

        3
       / \
      9  20
         / \
        15  7
```

**Key:** First element of preorder is root. Find it in inorder to split left/right subtrees.

---

### Problem 42: Construct Binary Tree from Inorder and Postorder

Build tree from inorder and postorder traversals.

```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

build_tree(inorder, postorder) →

        3
       / \
      9  20
         / \
        15  7
```

---

### Problem 43: Construct Binary Tree from Preorder and Postorder

Build tree from preorder and postorder (may not be unique).

```
preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]

build_tree(preorder, postorder) →

          1
         / \
        2   3
       / \ / \
      4  5 6  7
```

---

### Problem 44: Maximum Binary Tree

Build a tree where root is the max, left subtree is max tree of left portion, right subtree is max tree of right portion.

```
construct_max_tree([3,2,1,6,0,5]) →

          6
         / \
        3   5
         \  /
          2 0
           \
            1
```

---

### Problem 45: Serialize and Deserialize Binary Tree

Design an algorithm to serialize and deserialize a binary tree.

```
        1
       / \
      2   3
         / \
        4   5

serialize(root) → "1,2,null,null,3,4,null,null,5,null,null"
deserialize(data) → original tree
```

---

## Strategies and Patterns

### DFS Template

```cpp
// Return value approach
int dfs(Node* node) {
    if (!node) return base_case;
    
    int left = dfs(node->left);
    int right = dfs(node->right);
    
    // Combine results
    return combine(node->val, left, right);
}

// Path tracking approach
void dfs(Node* node, vector<int>& path, vector<vector<int>>& result) {
    if (!node) return;
    
    path.push_back(node->val);
    
    if (!node->left && !node->right) {
        // Leaf node - process path
        result.push_back(path);
    }
    
    dfs(node->left, path, result);
    dfs(node->right, path, result);
    
    path.pop_back();  // backtrack
}
```

### When to Use Each Traversal

| Traversal | Use When |
|-----------|----------|
| Preorder | Process parent before children (copy tree, serialize) |
| Inorder | BST problems (gives sorted order) |
| Postorder | Process children before parent (delete tree, calculate heights) |

### Common Patterns

| Pattern | Problems |
|---------|----------|
| Return value from subtrees | Height, depth, diameter, balanced check |
| Pass down parameters | Path sum, valid BST (with range), ancestor problems |
| Track path while traversing | All paths, path sum II |
| Modify tree structure | Invert, flatten, prune, merge |
| Use BST property | Search, insert, delete, kth smallest |

### Edge Cases

1. **Empty tree** (`root == nullptr`)
2. **Single node** (is both root and leaf)
3. **Skewed tree** (only left or only right children)
4. **Negative values** (for path sums)
5. **Duplicate values** (for BST problems, usually not allowed)

---

Good luck! Start with Part 1-2 to master basic traversals and properties, then Part 3 for path problems. BST problems in Part 6 are great for understanding how tree structure enables efficient operations.
