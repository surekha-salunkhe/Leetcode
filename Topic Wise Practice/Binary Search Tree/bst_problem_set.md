# Binary Search Tree Practice

The BST property: For every node, all values in the left subtree are **less than** the node's value, and all values in the right subtree are **greater than** the node's value.

Key insight: **Inorder traversal of a BST gives elements in sorted order.**

---

## Part 1: Basic BST Operations

### Problem 1: Search in a Binary Search Tree

Find a node with the given value. Return the subtree rooted at that node, or null if not found.

```
        4
       / \
      2   7
     / \
    1   3

search_bst(root, 2) → subtree rooted at 2
search_bst(root, 5) → null
```

**Pattern:** Compare with current node. Go left if smaller, right if larger.

```cpp
TreeNode* search(TreeNode* node, int val) {
    if (!node || node->val == val) return node;
    if (val < node->val) return search(node->left, val);
    return search(node->right, val);
}
```

---

### Problem 2: Insert into a Binary Search Tree

Insert a value into a BST. Return the root of the modified tree.

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

### Problem 3: Delete Node in a BST

Delete a node with the given value. Return the root of the modified tree.

Three cases:
1. Node is a leaf → simply remove
2. Node has one child → replace with child
3. Node has two children → replace with inorder successor (or predecessor)

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

### Problem 4: Minimum Value in BST

Find the minimum value in a BST.

```
        4
       / \
      2   7
     / \
    1   3

find_min(root) → 1
```

**Pattern:** Keep going left until you can't.

---

### Problem 5: Maximum Value in BST

Find the maximum value in a BST.

```
        4
       / \
      2   7
     / \
    1   3

find_max(root) → 7
```

---

### Problem 6: Inorder Successor in BST

Find the inorder successor of a given node (the node with the smallest key greater than the given node's key).

```
          20
         /  \
        8    22
       / \
      4  12
        /  \
       10  14

inorder_successor(root, 8) → 10
inorder_successor(root, 14) → 20
inorder_successor(root, 22) → null
```

**Two cases:**
1. Node has right subtree → successor is leftmost node in right subtree
2. No right subtree → successor is the nearest ancestor where node is in left subtree

---

### Problem 7: Inorder Predecessor in BST

Find the inorder predecessor of a given node.

```
          20
         /  \
        8    22
       / \
      4  12
        /  \
       10  14

inorder_predecessor(root, 12) → 10
inorder_predecessor(root, 8) → 4
inorder_predecessor(root, 4) → null
```

---

## Part 2: BST Validation and Properties

### Problem 8: Validate Binary Search Tree

Check if a binary tree is a valid BST.

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

is_valid_bst(root) → False   # 3 is not > 5
```

**Pattern:** Pass valid range (min, max) down to each node.

```cpp
bool isValid(TreeNode* node, long minVal, long maxVal) {
    if (!node) return true;
    if (node->val <= minVal || node->val >= maxVal) return false;
    return isValid(node->left, minVal, node->val) &&
           isValid(node->right, node->val, maxVal);
}
```

---

### Problem 9: Minimum Absolute Difference in BST

Find the minimum absolute difference between values of any two nodes.

```
        4
       / \
      2   6
     / \
    1   3

min_diff(root) → 1   # |2-1|, |3-2|, |4-3| are all 1
```

**Hint:** Inorder traversal gives sorted order. Min diff is between adjacent elements.

---

### Problem 10: Minimum Distance Between BST Nodes

Same as Problem 9 — find minimum difference between any two nodes.

```
        1
         \
          3
         /
        2

min_distance(root) → 1
```

---

### Problem 11: Range Sum of BST

Find the sum of all node values within a given range [low, high].

```
          10
         /  \
        5   15
       / \    \
      3   7   18

range_sum(root, 7, 15) → 32   # 7 + 10 + 15
```

**Optimization:** Use BST property to prune branches outside range.

---

### Problem 12: Count Nodes in Range

Count nodes with values in the range [low, high].

```
          10
         /  \
        5   15
       / \    \
      3   7   18

count_in_range(root, 5, 15) → 4   # 5, 7, 10, 15
```

---

### Problem 13: Closest Value in BST

Find the value closest to the target.

```
        4
       / \
      2   5
     / \
    1   3

closest_value(root, 3.7) → 4
closest_value(root, 3.2) → 3
```

---

### Problem 14: Closest K Values in BST

Find k values closest to the target.

```
        4
       / \
      2   5
     / \
    1   3

closest_k_values(root, 3.7, 2) → [4, 3]
```

---

## Part 3: Kth Element Problems

### Problem 15: Kth Smallest Element in BST

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

**Pattern:** Inorder traversal, count nodes, stop at k.

---

### Problem 16: Kth Largest Element in BST

Find the kth largest element.

```
        5
       / \
      3   6
     / \
    2   4
   /
  1

kth_largest(root, 3) → 4   # 6, 5, 4
```

**Hint:** Reverse inorder (right → node → left) gives descending order.

---

### Problem 17: Second Minimum Node

Find the second minimum value in a special BST where each node's value is the minimum of its subtree.

```
        2
       / \
      2   5
         / \
        5   7

second_min(root) → 5
```

---

## Part 4: BST Construction

### Problem 18: Convert Sorted Array to BST

Create a height-balanced BST from a sorted array.

```
sorted_array_to_bst([-10, -3, 0, 5, 9]) →

        0
       / \
     -3   9
     /   /
   -10  5
```

**Pattern:** Middle element becomes root. Recursively build left and right subtrees.

---

### Problem 19: Convert Sorted List to BST

Create a height-balanced BST from a sorted linked list.

```
-10 → -3 → 0 → 5 → 9

sorted_list_to_bst(head) →

        0
       / \
     -3   9
     /   /
   -10  5
```

---

### Problem 20: Construct BST from Preorder Traversal

Build a BST from its preorder traversal.

```
bst_from_preorder([8, 5, 1, 7, 10, 12]) →

          8
         / \
        5  10
       / \   \
      1   7  12
```

**Pattern:** First element is root. Elements less than root go to left subtree, greater go to right.

---

### Problem 21: Unique Binary Search Trees II

Generate all structurally unique BSTs that store values 1 to n.

```
generate_trees(3) →

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

---

### Problem 22: Unique Binary Search Trees (Count)

Count the number of structurally unique BSTs with n nodes.

```
num_trees(3) → 5
num_trees(1) → 1
num_trees(4) → 14
```

These are the **Catalan numbers**: C(n) = C(0)×C(n-1) + C(1)×C(n-2) + ... + C(n-1)×C(0)

---

## Part 5: BST Modification

### Problem 23: Trim a Binary Search Tree

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

### Problem 24: Convert BST to Greater Tree

Convert BST so each node's value is the sum of all values greater than or equal to it.

```
          4
         / \
        1   6
       / \ / \
      0  2 5  7
            \   \
             3   8

convert_bst(root) →

          30
         /  \
       36   21
       / \  / \
     36 35 26 15
           \    \
           33    8
```

**Pattern:** Reverse inorder (right → node → left) with running sum.

---

### Problem 25: Increasing Order Search Tree

Rearrange BST so it's a right-skewed tree in inorder.

```
        5
       / \
      3   6
     / \   \
    2   4   8
   /       / \
  1       7   9

increasing_bst(root) →

1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9
```

---

### Problem 26: Balance a Binary Search Tree

Given a BST, return a balanced BST with the same node values.

```
          1
           \
            2
             \
              3
               \
                4

balance_bst(root) →

        2
       / \
      1   3
           \
            4
```

**Approach:** Inorder to get sorted array, then build balanced BST from array.

---

### Problem 27: Recover Binary Search Tree

Two nodes were swapped by mistake. Recover the BST without changing structure.

```
        1              3
       /              /
      3      →       1
       \              \
        2              2
```

**Pattern:** Inorder should be sorted. Find the two out-of-place elements and swap their values.

---

### Problem 28: Split BST

Split a BST into two subtrees: one with all values ≤ target, one with all values > target.

```
          4
         / \
        2   6
       / \ / \
      1  3 5  7

split_bst(root, 2) → 

Tree 1 (≤2):     Tree 2 (>2):
    2                4
   /                / \
  1                3   6
                      / \
                     5   7
```

---

## Part 6: Two-Pointer / Two-Node Problems

### Problem 29: Two Sum IV - Input is a BST

Check if there exist two elements that sum to k.

```
        5
       / \
      3   6
     / \   \
    2   4   7

find_target(root, 9) → True    # 2 + 7 = 9
find_target(root, 28) → False
```

**Approaches:**
1. Inorder to array, then two pointers
2. HashSet while traversing
3. BST iterator (two pointers, one forward, one backward)

---

### Problem 30: Lowest Common Ancestor of a BST

Find the LCA of two nodes in a BST.

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

**BST optimization:** If both p and q are less than current, go left. If both greater, go right. Otherwise, current is LCA.

---

### Problem 31: All Elements in Two BSTs

Return a sorted list of all elements from two BSTs.

```
BST 1:      BST 2:
    2           1
   / \         / \
  1   4       0   3

all_elements(root1, root2) → [0, 1, 1, 2, 3, 4]
```

**Approach:** Inorder both trees, then merge two sorted lists.

---

### Problem 32: Merge Two BSTs

Merge two BSTs into one balanced BST.

```
BST 1:      BST 2:
    3          5
   / \        / \
  1   4      2   7

merge_bsts(root1, root2) →

          4
         / \
        2   5
       / \   \
      1   3   7
```

---

## Part 7: BST with Additional Constraints

### Problem 33: Contains Duplicate III

Check if there are two distinct indices i and j such that:
- `|nums[i] - nums[j]| <= valueDiff`
- `|i - j| <= indexDiff`

```
contains_nearby_almost_duplicate([1,2,3,1], 3, 0) → True
contains_nearby_almost_duplicate([1,5,9,1,5,9], 2, 3) → False
```

**Hint:** Use a balanced BST (TreeSet/set) to maintain a sliding window and find floor/ceiling.

---

### Problem 34: Count of Smaller Numbers After Self

For each element, count elements to its right that are smaller.

```
count_smaller([5,2,6,1]) → [2,1,1,0]
# 5 has 2 smaller to its right: 2, 1
# 2 has 1 smaller to its right: 1
# 6 has 1 smaller to its right: 1
# 1 has 0 smaller to its right
```

**Approach:** Process from right to left, insert into BST while counting smaller elements.

---

### Problem 35: Count of Range Sum

Count range sums that lie in [lower, upper].

```
count_range_sum([-2, 5, -1], -2, 2) → 3
# Ranges: [-2], [-2,5,-1]=2, [-1] all in [-2, 2]
```

---

### Problem 36: Reverse Pairs

Count pairs (i, j) where i < j and nums[i] > 2 * nums[j].

```
reverse_pairs([1,3,2,3,1]) → 2
reverse_pairs([2,4,3,5,1]) → 3
```

---

## Part 8: BST Iterator and Design

### Problem 37: Binary Search Tree Iterator

Implement an iterator over a BST with next() and hasNext().

```
        7
       / \
      3  15
         / \
        9  20

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
...
```

**Challenge:** O(h) space where h is tree height.

**Pattern:** Use a stack to simulate inorder traversal.

---

### Problem 38: Kth Largest Element in a Stream

Design a class that finds the kth largest element in a stream.

```
KthLargest(3, [4, 5, 8, 2])
add(3)  → 4
add(5)  → 5
add(10) → 5
add(9)  → 8
add(4)  → 8
```

**Hint:** Maintain a BST (or min-heap) of size k.

---

### Problem 39: My Calendar I

Implement a calendar that prevents double booking.

```
MyCalendar cal = new MyCalendar();
cal.book(10, 20) → true
cal.book(15, 25) → false  // Overlaps with [10, 20)
cal.book(20, 30) → true   // [20, 30) doesn't overlap
```

**Approach:** Use a balanced BST keyed by start time. Check for overlaps using floor/ceiling.

---

### Problem 40: My Calendar II

Allow double booking but not triple booking.

```
MyCalendarTwo cal = new MyCalendarTwo();
cal.book(10, 20) → true
cal.book(50, 60) → true
cal.book(10, 40) → true   // Double booked [10, 20)
cal.book(5, 15)  → false  // Would triple book [10, 15)
cal.book(5, 10)  → true
cal.book(25, 55) → true   // Double booked [25, 40) and [50, 55)
```

---

## Part 9: Advanced BST Problems

### Problem 41: Maximum Sum BST in Binary Tree

Find the maximum sum of a subtree that is also a valid BST.

```
            1
           / \
          4   3
         / \ / \
        2  4 2  5
                 \
                  4
                   \
                    6

max_sum_bst(root) → 20   # Subtree rooted at 3 with sum 2+3+5+4+6=20
```

---

### Problem 42: Convert Binary Tree to BST

Convert a binary tree to BST while keeping the structure (only change values).

```
        10                8
       /  \              / \
      2   7      →      4  10
     / \               / \
    8   4             2   7
```

**Approach:** Inorder to get values, sort, inorder again to assign back.

---

### Problem 43: Largest BST Subtree

Find the size of the largest subtree which is also a BST.

```
          10
         /  \
        5   15
       / \    \
      1   8   7

largest_bst_subtree(root) → 3   # Subtree rooted at 5
```

---

### Problem 44: Serialize and Deserialize BST

Design an algorithm to serialize and deserialize a BST. Use BST property for efficiency.

```
        2
       / \
      1   3

serialize(root) → "2,1,3"
deserialize("2,1,3") → original tree
```

**Optimization over general trees:** BST can be reconstructed from preorder alone (no nulls needed).

---

### Problem 45: Delete Nodes And Return Forest

Delete given nodes and return the resulting forest (list of remaining trees).

```
          1
         / \
        2   3
       / \ / \
      4  5 6  7

del_nodes(root, [3, 5]) → 

    1       6     7
   /
  2
 /
4
```

---

## Strategies and Patterns

### BST Property

```cpp
// For every node:
// all left subtree values < node->val < all right subtree values
```

### Inorder = Sorted

```cpp
void inorder(TreeNode* node, vector<int>& result) {
    if (!node) return;
    inorder(node->left, result);
    result.push_back(node->val);  // Ascending order
    inorder(node->right, result);
}
```

### Reverse Inorder = Descending

```cpp
void reverseInorder(TreeNode* node, vector<int>& result) {
    if (!node) return;
    reverseInorder(node->right, result);
    result.push_back(node->val);  // Descending order
    reverseInorder(node->left, result);
}
```

### Search Pattern

```cpp
TreeNode* search(TreeNode* node, int val) {
    if (!node) return nullptr;
    if (val == node->val) return node;
    if (val < node->val) return search(node->left, val);
    return search(node->right, val);
}
```

### Validate with Range

```cpp
bool isValid(TreeNode* node, long min, long max) {
    if (!node) return true;
    if (node->val <= min || node->val >= max) return false;
    return isValid(node->left, min, node->val) &&
           isValid(node->right, node->val, max);
}
```

### Common Patterns Summary

| Task | Approach |
|------|----------|
| Search / Insert | Compare and go left or right |
| Validate BST | Pass down valid range (min, max) |
| Kth smallest | Inorder traversal, count to k |
| Kth largest | Reverse inorder, count to k |
| LCA in BST | Compare both nodes with current |
| Build balanced BST | Pick middle element as root |
| Closest value | Binary search, track closest |
| Range queries | Prune branches outside range |
| Convert to greater tree | Reverse inorder with running sum |

### Time Complexity

| Operation | Balanced BST | Skewed BST |
|-----------|--------------|------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Inorder | O(n) | O(n) |

### Edge Cases

1. **Empty tree**
2. **Single node**
3. **Skewed tree** (all left or all right)
4. **Duplicate values** (usually not allowed in BST)
5. **Integer overflow** when validating (use long or pass node pointers)

---

Good luck! Master Parts 1-2 first for core BST operations and validation. The inorder = sorted property in Part 3 is crucial for many problems. Parts 7-9 cover more advanced applications.
