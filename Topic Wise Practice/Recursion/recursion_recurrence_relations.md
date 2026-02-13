# Recursion Practice: Recurrence Relations

These problems require you to identify and implement a recursive formula. For each problem, think about:
1. What are the base case(s)?
2. How can I express the answer for n in terms of smaller subproblems?

Many of these benefit from memoization — try solving them first without it, then add memoization and observe the speedup.

---

## Part 1: Counting Steps

### Problem 1: Staircase Climbing

You're climbing a staircase with n steps. Each time, you can climb either 1 or 2 steps. How many distinct ways can you reach the top?

```
climb_stairs(1) → 1       # Just one 1-step
climb_stairs(2) → 2       # (1+1) or (2)
climb_stairs(3) → 3       # (1+1+1), (1+2), (2+1)
climb_stairs(4) → 5       # (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)
climb_stairs(5) → 8
```

**Think about it:** To reach step n, you either came from step n-1 (taking 1 step) or step n-2 (taking 2 steps). What does that tell you about the recurrence?

---

### Problem 2: Staircase Climbing (Generalized)

Now you can climb 1, 2, or 3 steps at a time. How many ways to reach step n?

```
climb_stairs_3(1) → 1
climb_stairs_3(2) → 2
climb_stairs_3(3) → 4     # (1+1+1), (1+2), (2+1), (3)
climb_stairs_3(4) → 7
climb_stairs_3(5) → 13
```

**Extension:** Generalize to k possible step sizes: `climb_stairs_k(n, steps)` where `steps` is a list like `[1, 2, 3]`.

---

### Problem 3: Grid Paths

You're in the top-left corner of an m × n grid. You can only move right or down. How many unique paths lead to the bottom-right corner?

```
grid_paths(1, 1) → 1      # Already there
grid_paths(2, 2) → 2      # Right-Down or Down-Right
grid_paths(2, 3) → 3
grid_paths(3, 3) → 6
grid_paths(3, 7) → 28
```

**Recurrence:** To reach cell (m, n), you either came from (m-1, n) or (m, n-1).

---

### Problem 4: Grid Paths with Obstacles

Same as Problem 3, but some cells are blocked. Given a grid where 0 = open and 1 = blocked, count the paths.

```
grid = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]
grid_paths_obstacles(grid) → 2
```

---

## Part 2: Counting Structures

### Problem 5: Tiling a 2×n Board

How many ways can you tile a 2×n board using 2×1 dominoes?

```
┌─┬─┐    or    ┌───┐
│ │ │          ├───┤
└─┴─┘          └───┘
vertical       horizontal pair
```

```
tile_2xn(1) → 1           # One vertical domino
tile_2xn(2) → 2           # Two vertical or two horizontal
tile_2xn(3) → 3
tile_2xn(4) → 5
tile_2xn(5) → 8
```

**Think about it:** Look at the rightmost column. Either it has one vertical domino (leaving a 2×(n-1) board) or two horizontal dominoes (leaving a 2×(n-2) board).

---

### Problem 6: Tiling a 3×n Board

How many ways can you tile a 3×n board using 2×1 dominoes? (Only possible when n is even.)

```
tile_3xn(0) → 1           # Empty board, one way (do nothing)
tile_3xn(2) → 3
tile_3xn(4) → 11
tile_3xn(6) → 41
```

**Hint:** This one is trickier. You'll need to track "partial" states where one cell sticks out. Consider defining auxiliary functions.

---

### Problem 7: Balanced Parentheses

How many ways can you arrange n pairs of parentheses so they're balanced?

```
count_parens(0) → 1       # "" (empty)
count_parens(1) → 1       # "()"
count_parens(2) → 2       # "(())", "()()"
count_parens(3) → 5       # "((()))", "(()())", "(())()", "()(())", "()()()"
count_parens(4) → 14
```

These are the **Catalan numbers**. The recurrence is:
```
C(n) = Σ C(i) × C(n-1-i)  for i from 0 to n-1
```

**Intuition:** The first `(` must match with some `)`. If it matches with the `)` at position 2i+1, there are i pairs inside and n-1-i pairs outside.

---

### Problem 8: Binary Search Trees

How many structurally different binary search trees can store n distinct keys?

```
count_bst(0) → 1          # Empty tree
count_bst(1) → 1          # Just root
count_bst(2) → 2          # Root with left child, or root with right child
count_bst(3) → 5
count_bst(4) → 14
```

**Hint:** This is also the Catalan numbers! If you pick key k as root, keys 1..k-1 go in the left subtree and keys k+1..n go in the right subtree.

---

## Part 3: Partitions and Combinations

### Problem 9: Integer Partitions

How many ways can you write n as a sum of positive integers (order doesn't matter)?

```
partitions(1) → 1         # 1
partitions(2) → 2         # 2, 1+1
partitions(3) → 3         # 3, 2+1, 1+1+1
partitions(4) → 5         # 4, 3+1, 2+2, 2+1+1, 1+1+1+1
partitions(5) → 7         # 5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1
```

**Hint:** Define `partitions(n, max_part)` — the number of ways to partition n using parts ≤ max_part. Then:
- Either you use at least one `max_part`, leaving `partitions(n - max_part, max_part)`
- Or you don't use `max_part` at all, giving `partitions(n, max_part - 1)`

---

### Problem 10: Subset Sum Count

Given a list of positive integers and a target sum, count how many subsets sum to exactly the target.

```
subset_sum_count([1, 2, 3, 4, 5], 5) → 3    # {5}, {1,4}, {2,3}
subset_sum_count([1, 1, 1, 1], 2) → 6       # All pairs of 1s
subset_sum_count([3, 34, 4, 12, 5, 2], 9) → 2   # {3,4,2}, {4,5}
```

**Recurrence:** For each element, either include it (and solve for target - element) or exclude it (and solve for same target).

---

### Problem 11: Coin Change (Count Ways)

Given coin denominations and a target amount, count the number of ways to make change. Order doesn't matter (1+2 and 2+1 are the same).

```
coin_change_ways([1, 2, 5], 5) → 4
# 5, 2+2+1, 2+1+1+1, 1+1+1+1+1

coin_change_ways([1, 2], 4) → 3
# 2+2, 2+1+1, 1+1+1+1
```

**Hint:** Similar to integer partitions — process coins in order to avoid counting permutations.

---

### Problem 12: Coin Change (Minimum Coins)

Given coin denominations and a target amount, find the minimum number of coins needed. Return -1 if impossible.

```
min_coins([1, 2, 5], 11) → 3        # 5+5+1
min_coins([2], 3) → -1              # Impossible
min_coins([1, 3, 4], 6) → 2         # 3+3 (not 4+1+1)
```

**Recurrence:** `min_coins(amount) = 1 + min(min_coins(amount - c) for each coin c)`

---

## Part 4: Sequences and Strings

### Problem 13: Tribonacci

Like Fibonacci, but each term is the sum of the previous three.

```
T(0) = 0, T(1) = 1, T(2) = 1
T(n) = T(n-1) + T(n-2) + T(n-3) for n > 2

tribonacci(0) → 0
tribonacci(1) → 1
tribonacci(2) → 1
tribonacci(4) → 4         # 0, 1, 1, 2, 4
tribonacci(10) → 149
```

---

### Problem 14: Derangements

A derangement is a permutation where no element stays in its original position. Count derangements of n elements.

```
derangements(0) → 1       # Empty derangement
derangements(1) → 0       # Can't derange a single element
derangements(2) → 1       # [2, 1]
derangements(3) → 2       # [2,3,1], [3,1,2]
derangements(4) → 9
derangements(5) → 44
```

**Recurrence:** `D(n) = (n-1) × (D(n-1) + D(n-2))`

**Intuition:** Element 1 can go to any of (n-1) positions. Say it goes to position k. Now element k either:
- Goes to position 1 (swap) — leaves D(n-2) derangements for the rest
- Doesn't go to position 1 — effectively a derangement of n-1 elements

---

### Problem 15: Longest Common Subsequence (Length)

Find the length of the longest common subsequence of two strings.

```
lcs("ABCDGH", "AEDFHR") → 3      # "ADH"
lcs("AGGTAB", "GXTXAYB") → 4    # "GTAB"
lcs("ABC", "AC") → 2            # "AC"
lcs("ABC", "DEF") → 0
```

**Recurrence:**
- If the last characters match: `lcs(s1, s2) = 1 + lcs(s1[:-1], s2[:-1])`
- If they don't: `lcs(s1, s2) = max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))`

---

### Problem 16: Edit Distance

Find the minimum number of operations (insert, delete, replace) to transform one string into another.

```
edit_distance("kitten", "sitting") → 3
# kitten → sitten (replace k with s)
# sitten → sittin (replace e with i)
# sittin → sitting (insert g)

edit_distance("sunday", "saturday") → 3
edit_distance("", "abc") → 3
```

**Recurrence:**
- If last characters match: `edit(s1, s2) = edit(s1[:-1], s2[:-1])`
- Otherwise: `edit(s1, s2) = 1 + min(edit(s1[:-1], s2), edit(s1, s2[:-1]), edit(s1[:-1], s2[:-1]))`

---

## Part 5: Challenge Problems

### Problem 17: Egg Drop

You have k identical eggs and an n-story building. Find the minimum number of trials needed to determine the critical floor (the highest floor from which an egg can be dropped without breaking).

```
egg_drop(1, 10) → 10      # With 1 egg, must try floors 1, 2, ..., 10
egg_drop(2, 10) → 4
egg_drop(2, 100) → 14
egg_drop(3, 100) → 9
```

**Recurrence:** If you drop from floor x:
- Egg breaks: search floors 1 to x-1 with k-1 eggs
- Egg survives: search floors x+1 to n with k eggs

`egg_drop(k, n) = 1 + min over x of max(egg_drop(k-1, x-1), egg_drop(k, n-x))`

---

### Problem 18: Matrix Chain Multiplication

Given dimensions of matrices, find the minimum number of scalar multiplications needed to compute their product.

Matrices: A1 (10×30), A2 (30×5), A3 (5×60)
- (A1 × A2) × A3 = 10×30×5 + 10×5×60 = 1500 + 3000 = 4500
- A1 × (A2 × A3) = 30×5×60 + 10×30×60 = 9000 + 18000 = 27000

```
# dims[i-1] × dims[i] gives dimensions of matrix i
matrix_chain([10, 30, 5, 60]) → 4500
matrix_chain([40, 20, 30, 10, 30]) → 26000
```

**Recurrence:** Try every possible split point k:
`cost(i, j) = min over k of (cost(i, k) + cost(k+1, j) + dims[i-1] × dims[k] × dims[j])`

---

### Problem 19: Optimal BST

Given keys with search frequencies, construct a BST that minimizes expected search cost.

```
keys = [10, 20, 30]
freq = [3, 2, 5]    # key 30 is searched most often

optimal_bst_cost(keys, freq) → 17
# Optimal tree has 30 as root, 10 and 20 as left subtree
# Cost: 5×1 + 3×2 + 2×3 = 5 + 6 + 6 = 17
```

---

## Strategies for Recurrence Relations

1. **Identify the last step.** What was the last choice made? How does it split into subproblems?

2. **Draw small cases.** Work out n = 0, 1, 2, 3 by hand. The pattern often becomes clear.

3. **Watch for overlapping subproblems.** If you call the same subproblem multiple times, memoize.

4. **Consider state carefully.** Sometimes you need extra parameters (e.g., `partitions(n, max_part)` instead of just `partitions(n)`).

5. **Check for classic sequences.** Fibonacci, Catalan, and other named sequences appear in disguise.

---

## Memoization Exercise

Pick 3 problems above and implement them:
1. First with naive recursion — note how slow they get for larger inputs
2. Then with memoization — observe the dramatic speedup
3. Optionally, convert to bottom-up DP (iterative with a table)

Good candidates: Grid Paths, Coin Change, Edit Distance, Egg Drop

---

Good luck! Start with the problems in Part 1 — they build intuition that carries through to the harder ones.
