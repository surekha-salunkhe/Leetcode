# Linked List Practice: Pointers and Modification

Linked list problems test your ability to manipulate pointers carefully. The key skills:

- Traversing with pointers
- Modifying next pointers without losing nodes
- Using dummy nodes to simplify edge cases
- Two-pointer techniques (slow/fast, previous/current)

---

## Part 1: Basic Traversal and Modification

### Problem 1: Reverse Linked List

Reverse a singly linked list.

```
Input:  1 → 2 → 3 → 4 → 5 → NULL
Output: 5 → 4 → 3 → 2 → 1 → NULL
```

**Pattern:** Track three pointers: `prev`, `curr`, `next`. At each step, reverse the link.

```cpp
ListNode* reverse(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* next = curr->next;  // save next
        curr->next = prev;            // reverse link
        prev = curr;                  // advance prev
        curr = next;                  // advance curr
    }
    return prev;
}
```

---

### Problem 2: Delete Node in a Linked List

Delete a node (not the tail) given only access to that node.

```
Input:  4 → 5 → 1 → 9, node = 5
Output: 4 → 1 → 9
```

**Trick:** Copy the next node's value into current node, then skip the next node.

---

### Problem 3: Remove Linked List Elements

Remove all nodes with a given value.

```
Input:  1 → 2 → 6 → 3 → 4 → 5 → 6, val = 6
Output: 1 → 2 → 3 → 4 → 5
```

**Hint:** Use a dummy head to handle the case where head itself needs removal.

---

### Problem 4: Remove Duplicates from Sorted List

Delete all duplicates in a sorted list (keep one of each).

```
Input:  1 → 1 → 2 → 3 → 3
Output: 1 → 2 → 3
```

---

### Problem 5: Remove Duplicates from Sorted List II

Delete all nodes that have duplicates (keep none of them).

```
Input:  1 → 2 → 3 → 3 → 4 → 4 → 5
Output: 1 → 2 → 5

Input:  1 → 1 → 1 → 2 → 3
Output: 2 → 3
```

---

### Problem 6: Middle of the Linked List

Return the middle node. If two middle nodes, return the second.

```
Input:  1 → 2 → 3 → 4 → 5
Output: Node 3

Input:  1 → 2 → 3 → 4 → 5 → 6
Output: Node 4
```

**Pattern:** Slow pointer moves 1 step, fast pointer moves 2 steps. When fast reaches end, slow is at middle.

---

### Problem 7: Linked List Cycle

Determine if a linked list has a cycle.

```
Input:  3 → 2 → 0 → -4 → (back to 2)
Output: True
```

**Pattern:** Fast/slow pointers. If they meet, there's a cycle.

---

### Problem 8: Linked List Cycle II

Return the node where the cycle begins, or null if no cycle.

```
Input:  3 → 2 → 0 → -4 → (back to 2)
Output: Node 2
```

**Pattern:** After fast and slow meet, reset one to head. Move both at same speed — they meet at cycle start.

---

### Problem 9: Intersection of Two Linked Lists

Find the node where two lists intersect, or null if they don't.

```
List A:      4 → 1 ↘
                    8 → 4 → 5
List B: 5 → 6 → 1 ↗
Output: Node 8
```

**Hint:** After reaching the end of one list, continue from the head of the other. They'll meet at intersection or both reach null.

---

### Problem 10: Palindrome Linked List

Check if a linked list is a palindrome.

```
Input:  1 → 2 → 2 → 1
Output: True

Input:  1 → 2
Output: False
```

**Approach:** Find middle, reverse second half, compare both halves.

---

## Part 2: Insertion and Deletion

### Problem 11: Delete the Middle Node

Delete the middle node of the list.

```
Input:  1 → 3 → 4 → 7 → 1 → 2 → 6
Output: 1 → 3 → 4 → 1 → 2 → 6  (removed 7)

Input:  1 → 2 → 3 → 4
Output: 1 → 2 → 4  (removed 3)
```

**Hint:** Use slow/fast, but track the node before slow.

---

### Problem 12: Remove Nth Node From End

Remove the nth node from the end in one pass.

```
Input:  1 → 2 → 3 → 4 → 5, n = 2
Output: 1 → 2 → 3 → 5

Input:  1, n = 1
Output: []
```

**Pattern:** Move fast pointer n steps ahead first. Then move both until fast reaches end.

---

### Problem 13: Insert into a Sorted Circular Linked List

Insert a value into a sorted circular list, maintaining sorted order.

```
Input:  3 → 4 → 1 → (back to 3), insert 2
Output: 3 → 4 → 1 → 2 → (back to 3)
        or equivalently starting from 1: 1 → 2 → 3 → 4 → (back to 1)
```

---

### Problem 14: Delete N Nodes After M Nodes

Given m and n, keep m nodes then delete next n nodes, repeat.

```
Input:  1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9, m = 2, n = 1
Output: 1 → 2 → 4 → 5 → 7 → 8
```

---

### Problem 15: Remove Zero Sum Consecutive Nodes

Remove all consecutive sequences of nodes that sum to 0.

```
Input:  1 → 2 → -3 → 3 → 1
Output: 3 → 1  (1+2+(-3) = 0, removed)

Input:  1 → 2 → 3 → -3 → 4
Output: 1 → 2 → 4

Input:  1 → 2 → 3 → -3 → -2
Output: 1
```

---

## Part 3: Reversal Variations

### Problem 16: Reverse Linked List II

Reverse nodes from position left to right (1-indexed).

```
Input:  1 → 2 → 3 → 4 → 5, left = 2, right = 4
Output: 1 → 4 → 3 → 2 → 5
```

**Key:** Find the node before position left, reverse the sublist, reconnect.

---

### Problem 17: Reverse Nodes in k-Group

Reverse every k consecutive nodes. Remaining nodes (< k) stay as is.

```
Input:  1 → 2 → 3 → 4 → 5, k = 2
Output: 2 → 1 → 4 → 3 → 5

Input:  1 → 2 → 3 → 4 → 5, k = 3
Output: 3 → 2 → 1 → 4 → 5
```

---

### Problem 18: Swap Nodes in Pairs

Swap every two adjacent nodes.

```
Input:  1 → 2 → 3 → 4
Output: 2 → 1 → 4 → 3

Input:  1 → 2 → 3
Output: 2 → 1 → 3
```

---

### Problem 19: Reverse Alternate K Nodes

Reverse first k nodes, skip next k nodes, repeat.

```
Input:  1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9, k = 3
Output: 3 → 2 → 1 → 4 → 5 → 6 → 9 → 8 → 7
```

---

### Problem 20: Reverse Even Length Groups

Nodes are in groups of increasing size (1, 2, 3, ...). Reverse groups with even length.

```
Input:  5 → 2 → 6 → 3 → 9 → 1 → 7 → 3 → 8 → 4
Groups: [5] [2,6] [3,9,1] [7,3,8,4]
Sizes:   1    2      3       4
Reverse: no   yes    no      yes
Output: 5 → 6 → 2 → 3 → 9 → 1 → 4 → 8 → 3 → 7
```

---

## Part 4: Reordering

### Problem 21: Reorder List

Reorder L0 → L1 → ... → Ln to L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

```
Input:  1 → 2 → 3 → 4
Output: 1 → 4 → 2 → 3

Input:  1 → 2 → 3 → 4 → 5
Output: 1 → 5 → 2 → 4 → 3
```

**Approach:** Find middle, reverse second half, merge alternately.

---

### Problem 22: Odd Even Linked List

Group all odd-indexed nodes together followed by even-indexed nodes.

```
Input:  1 → 2 → 3 → 4 → 5
Output: 1 → 3 → 5 → 2 → 4

Input:  2 → 1 → 3 → 5 → 6 → 4 → 7
Output: 2 → 3 → 6 → 7 → 1 → 5 → 4
```

---

### Problem 23: Partition List

Partition list around value x: all nodes < x come before nodes ≥ x, preserving original order within each partition.

```
Input:  1 → 4 → 3 → 2 → 5 → 2, x = 3
Output: 1 → 2 → 2 → 4 → 3 → 5
```

**Hint:** Build two separate lists (less than x, greater or equal), then connect them.

---

### Problem 24: Rotate List

Rotate the list to the right by k places.

```
Input:  1 → 2 → 3 → 4 → 5, k = 2
Output: 4 → 5 → 1 → 2 → 3

Input:  0 → 1 → 2, k = 4
Output: 2 → 0 → 1
```

**Hint:** k may be larger than list length. Connect tail to head (make circular), then break at the right spot.

---

### Problem 25: Split Linked List in Parts

Split list into k consecutive parts, as equal as possible. Earlier parts should be at most 1 node larger.

```
Input:  1 → 2 → 3, k = 5
Output: [[1], [2], [3], [], []]

Input:  1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10, k = 3
Output: [[1,2,3,4], [5,6,7], [8,9,10]]
```

---

## Part 5: Merging

### Problem 26: Merge Two Sorted Lists

Merge two sorted lists into one sorted list.

```
Input:  1 → 2 → 4, 1 → 3 → 4
Output: 1 → 1 → 2 → 3 → 4 → 4
```

---

### Problem 27: Merge k Sorted Lists

Merge k sorted linked lists into one sorted list.

```
Input:  [1 → 4 → 5, 1 → 3 → 4, 2 → 6]
Output: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

**Approaches:**

- Merge pairs iteratively (divide and conquer)
- Use a min-heap

---

### Problem 28: Add Two Numbers

Two numbers represented as linked lists (digits in reverse order). Return their sum as a linked list.

```
Input:  2 → 4 → 3 (342)
        5 → 6 → 4 (465)
Output: 7 → 0 → 8 (807)
```

---

### Problem 29: Add Two Numbers II

Same as above, but digits are in forward order. Don't reverse the lists.

```
Input:  7 → 2 → 4 → 3 (7243)
        5 → 6 → 4 (564)
Output: 7 → 8 → 0 → 7 (7807)
```

**Hint:** Use stacks, or pad the shorter list with zeros.

---

### Problem 30: Sort List

Sort a linked list in O(n log n) time and O(1) space.

```
Input:  4 → 2 → 1 → 3
Output: 1 → 2 → 3 → 4

Input:  -1 → 5 → 3 → 4 → 0
Output: -1 → 0 → 3 → 4 → 5
```

**Approach:** Merge sort. Find middle, split, recursively sort both halves, merge.

---

## Part 6: Special Structures

### Problem 31: Copy List with Random Pointer

Clone a list where each node has a next pointer and a random pointer to any node (or null).

```
Input:  Nodes with val and random pointers
Output: Deep copy of the list
```

**Approach:** Interleave cloned nodes, set random pointers, then separate the lists.

---

### Problem 32: Flatten a Multilevel Doubly Linked List

Nodes have next, prev, and child pointers. Flatten so children are inserted between node and its next.

```
Input:  1 ↔ 2 ↔ 3 ↔ 4 ↔ 5 ↔ 6
            |
            7 ↔ 8 ↔ 9 ↔ 10
                |
               11 ↔ 12

Output: 1 ↔ 2 ↔ 7 ↔ 8 ↔ 11 ↔ 12 ↔ 9 ↔ 10 ↔ 3 ↔ 4 ↔ 5 ↔ 6
```

---

### Problem 33: Convert Binary Search Tree to Sorted Doubly Linked List

Convert a BST to a circular doubly linked list in-place. Left pointer = prev, right pointer = next.

```
Input:     4
         /   \
        2     5
       / \
      1   3

Output: 1 ↔ 2 ↔ 3 ↔ 4 ↔ 5 ↔ (back to 1)
```

---

### Problem 34: LRU Cache

Design a data structure with O(1) get and put operations. Evict least recently used item when capacity is exceeded.

```
LRUCache cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
```

**Approach:** Doubly linked list + hashmap. List maintains usage order, map provides O(1) lookup.

---

### Problem 35: Design Linked List

Implement a linked list with these operations:

- `get(index)`: Get value at index
- `addAtHead(val)`: Add node at head
- `addAtTail(val)`: Add node at tail
- `addAtIndex(index, val)`: Add before the index-th node
- `deleteAtIndex(index)`: Delete the index-th node

---

## Strategies and Patterns

### The Dummy Node Trick

When the head might change (deletions, insertions at head), use a dummy node:

```cpp
ListNode dummy(0);
dummy.next = head;
// ... modify list ...
return dummy.next;
```

### Two Pointer Patterns

| Pattern                        | Use Case                  |
| ------------------------------ | ------------------------- |
| Slow (1 step) / Fast (2 steps) | Find middle, detect cycle |
| Fast ahead by n                | Remove nth from end       |
| Previous / Current             | Reversal, deletion        |
| Two lists                      | Merge, intersection       |

### Reversal Template

```cpp
ListNode* prev = nullptr;
ListNode* curr = head;
while (curr) {
    ListNode* next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
}
return prev;
```

### Common Edge Cases

1. **Empty list** (`head == nullptr`)
2. **Single node** (`head->next == nullptr`)
3. **Two nodes** (especially for reversal problems)
4. **Operation at head** (dummy node helps)
5. **Operation at tail** (need to track previous)

### Visualization Tip

When stuck, draw the list and trace pointers step by step. Label each pointer clearly:

```
prev    curr    next
  ↓       ↓       ↓
  1   →   2   →   3   →   4   →   NULL
```

---

Good luck! Start with Part 1 to master the basic patterns, especially reversal — it's the foundation for many harder problems.
