# Two Pointers Practice

The two-pointer technique uses two indices to traverse a data structure, often reducing O(n²) brute force to O(n). The key variations:

- **Opposite ends:** Start one pointer at the beginning, one at the end, move them toward each other
- **Same direction (slow/fast):** Both start at the beginning, move at different speeds or conditions
- **Two arrays:** One pointer per array, advance based on comparisons

---

## Part 1: Opposite Ends

### Problem 1: Two Sum (Sorted Array)

Given a **sorted** array and a target sum, find two numbers that add up to the target. Return their indices (1-indexed).

```
two_sum([2, 7, 11, 15], 9) → [1, 2]       # 2 + 7 = 9
two_sum([2, 3, 4], 6) → [1, 3]            # 2 + 4 = 6
two_sum([-1, 0, 2, 3], 2) → [2, 3]        # 0 + 2 = 2
two_sum([-1, 0, 2, 3], 2) → [2, 3]        # -1 + 3 = 2 [1, 4]
```

**Key insight:** If `arr[left] + arr[right] < target`, you need a bigger sum — move `left` right. If the sum is too big, move `right` left.

---

### Problem 2: Valid Palindrome

Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.

```
is_palindrome("A man, a plan, a canal: Panama") → True
is_palindrome("race a car") → False
is_palindrome(" ") → True
```

---

### Problem 3: Reverse String In-Place

Reverse an array of characters in-place (no extra array).

```
reverse(['h','e','l','l','o']) → ['o','l','l','e','h']
reverse(['a','b']) → ['b','a']
```

---

### Problem 4: Reverse Words in a String (In-Place)

Given a character array representing a sentence, reverse the order of words in-place.

```
reverse_words(['t','h','e',' ','s','k','y',' ','i','s',' ','b','l','u','e'])
→ ['b','l','u','e',' ','i','s',' ','s','k','y',' ','t','h','e']
```

**Hint:** Reverse the entire array, then reverse each word individually.

---

### Problem 5: Container With Most Water

Given an array of heights representing vertical lines, find two lines that together with the x-axis form a container holding the most water.

```
max_water([1,8,6,2,5,4,8,3,7]) → 49    # Lines at indices 1 and 8 (heights 8 and 7)
max_water([1,1]) → 1
max_water([4,3,2,1,4]) → 16           # Lines at indices 0 and 4
```

**Key insight:** Start with the widest container. The only way to potentially find more water is to move the shorter line inward.

---

### Problem 6: Three Sum

Given an array, find all unique triplets that sum to zero.

```
three_sum([-1, 0, 1, 2, -1, -4]) → [[-1, -1, 2], [-1, 0, 1]]
three_sum([0, 1, 1]) → []
three_sum([0, 0, 0]) → [[0, 0, 0]]
```

**Approach:** Sort the array. For each element, use two pointers on the remaining elements to find pairs that sum to its negation. Skip duplicates carefully.

---

### Problem 7: Three Sum Closest

Given an array and a target, find three numbers whose sum is closest to the target. Return the sum.

```
three_sum_closest([-1, 2, 1, -4], 1) → 2      # -1 + 2 + 1 = 2
three_sum_closest([0, 0, 0], 1) → 0
```

---

### Problem 8: Four Sum

Given an array and a target, find all unique quadruplets that sum to the target.

```
four_sum([1, 0, -1, 0, -2, 2], 0) → [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
four_sum([2, 2, 2, 2, 2], 8) → [[2, 2, 2, 2]]
```

---

### Problem 9: Trapping Rain Water

Given an array of heights representing an elevation map, compute how much water can be trapped after rain.

```
trap([0,1,0,2,1,0,1,3,2,1,2,1]) → 6
trap([4,2,0,3,2,5]) → 9
```

```
|
|   █
█ █ █ █
█ █ █ █ █ █
```

**Hint:** Water at position i = min(max_left, max_right) - height[i]. Two pointers can compute this in one pass.

---

## Part 2: Same Direction (Slow/Fast)

### Problem 10: Remove Duplicates from Sorted Array

Remove duplicates in-place from a sorted array. Return the new length. Elements beyond that length don't matter.

```
remove_duplicates([1,1,2]) → 2           # Array becomes [1, 2, ...]
remove_duplicates([0,0,1,1,1,2,2,3,3,4]) → 5   # [0, 1, 2, 3, 4, ...]
```

**Pattern:** `slow` marks where to write the next unique element. `fast` scans ahead.

---

### Problem 11: Remove Duplicates II (Allow Two)

Same as above, but each element may appear at most **twice**.

```
remove_duplicates_ii([1,1,1,2,2,3]) → 5       # [1, 1, 2, 2, 3, ...]
remove_duplicates_ii([0,0,1,1,1,1,2,3,3]) → 7 # [0, 0, 1, 1, 2, 3, 3, ...]
```

---

### Problem 12: Move Zeroes

Move all zeroes to the end while maintaining the relative order of non-zero elements. Do it in-place.

```
move_zeroes([0,1,0,3,12]) → [1,3,12,0,0]
move_zeroes([0]) → [0]
move_zeroes([1,2,3]) → [1,2,3]
```

---

### Problem 13: Remove Element

Remove all occurrences of a value in-place. Return the new length.

```
remove_element([3,2,2,3], 3) → 2         # [2, 2, ...]
remove_element([0,1,2,2,3,0,4,2], 2) → 5 # [0, 1, 3, 0, 4, ...]
```

---

### Problem 14: Sort Colors (Dutch National Flag)

Sort an array containing only 0s, 1s, and 2s in-place. One pass, constant space.

```
sort_colors([2,0,2,1,1,0]) → [0,0,1,1,2,2]
sort_colors([2,0,1]) → [0,1,2]
```

**Hint:** Use three pointers — `low`, `mid`, `high`. Elements before `low` are 0s, after `high` are 2s.

---

### Problem 15: Partition Array

Rearrange an array so all elements less than a pivot come before elements greater than or equal to it. Return the index of the first element >= pivot.

```
partition([3, 1, 4, 1, 5, 9, 2, 6], 5) → 5
# One valid result: [3, 1, 4, 1, 2, 9, 5, 6], returns 5
```

---

### Problem 16: Linked List Cycle

Determine if a linked list has a cycle.

```
head = 3 → 2 → 0 → -4 ↩ (back to 2)
has_cycle(head) → True

head = 1 → 2 → None
has_cycle(head) → False
```

**Approach:** Fast pointer moves 2 steps, slow pointer moves 1 step. If they meet, there's a cycle.

---

### Problem 17: Linked List Cycle II

If a linked list has a cycle, return the node where the cycle begins. If no cycle, return null.

```
head = 3 → 2 → 0 → -4 ↩ (back to 2)
detect_cycle(head) → node with value 2
```

**Hint:** After fast and slow meet, reset one pointer to head. Move both at the same speed — they'll meet at the cycle start.

---

### Problem 18: Find the Middle of a Linked List

Return the middle node. If two middle nodes, return the second one.

```
1 → 2 → 3 → 4 → 5       → returns node 3
1 → 2 → 3 → 4 → 5 → 6   → returns node 4
```

---

### Problem 19: Remove Nth Node From End

Remove the nth node from the end of a linked list in one pass.

```
1 → 2 → 3 → 4 → 5, n=2  → 1 → 2 → 3 → 5
1 → 2, n=1              → 1
```

**Hint:** Advance `fast` by n steps first, then move both until `fast` reaches the end.

---

## Part 3: Two Arrays

### Problem 20: Merge Sorted Arrays

Merge two sorted arrays into the first array. The first array has enough space.

```
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3
merge(nums1, m, nums2, n) → [1, 2, 2, 3, 5, 6]
```

**Key insight:** Fill from the end to avoid overwriting elements.

---

### Problem 21: Intersection of Two Sorted Arrays

Return the intersection of two sorted arrays. Each element should appear as many times as it shows in both.

```
intersect([1,2,2,1], [2,2]) → [2, 2]
intersect([4,9,5], [9,4,9,8,4]) → [4, 9]  # (order may vary)
intersect([1,1,2,2], [2,2]) → [2,2]
intersect([4,5,9], [4,4,8,9,9]) → [4,9]
```

---

### Problem 22: Is Subsequence

Check if string `s` is a subsequence of string `t`.

```
is_subsequence("abc", "ahbgdc") → True
is_subsequence("axc", "ahbgdc") → False
is_subsequence("", "ahbgdc") → True
```

---

### Problem 23: Compare Version Numbers

Compare two version strings. Return -1 if version1 < version2, 1 if version1 > version2, 0 if equal.

```
compare_version("1.01", "1.001") → 0      # 1.1 vs 1.1
compare_version("1.0", "1.0.0") → 0       # trailing zeros don't matter
compare_version("0.1", "1.1") → -1
compare_version("1.0.1", "1") → 1
```

---

### Problem 24: Backspace String Compare

Given two strings with `#` representing backspace, check if they're equal after processing.

```
backspace_compare("ab#c", "ad#c") → True      # Both become "ac"
backspace_compare("ab##", "c#d#") → True      # Both become ""
backspace_compare("a#c", "b") → False
```

**Challenge:** Solve with O(1) space by traversing from the end.

---

## Part 4: Challenge Problems

### Problem 25: Sort Array By Parity

Rearrange so all even numbers come before all odd numbers.

```
sort_by_parity([3,1,2,4]) → [2,4,3,1]  # or [4,2,1,3], etc.
```

---

### Problem 26: Squares of a Sorted Array

Given a sorted array (may have negatives), return an array of squares in sorted order.

```
sorted_squares([-4,-1,0,3,10]) → [0,1,9,16,100]
sorted_squares([-7,-3,2,3,11]) → [4,9,9,49,121]
```

**Key insight:** The largest square is either at the left end (large negative) or right end (large positive).

---

### Problem 27: Longest Mountain in Array

Find the length of the longest mountain subarray. A mountain has strictly increasing then strictly decreasing elements, with at least 3 elements total.

```
longest_mountain([2,1,4,7,3,2,5]) → 5    # [1,4,7,3,2]
longest_mountain([2,2,2]) → 0
```

---

### Problem 28: Boats to Save People

People with given weights, boats with a weight limit. Each boat carries at most 2 people. Find minimum boats needed.

```
num_boats([1,2], 3) → 1                  # Both fit
num_boats([3,2,2,1], 3) → 3              # (1,2), (2), (3)
num_boats([3,5,3,4], 5) → 4              # Each alone
```

**Approach:** Sort. Try to pair the lightest with the heaviest.

---

### Problem 29: Minimize Maximum Pair Sum

Pair up all elements in an even-length array. Minimize the maximum pair sum.

```
min_max_pair_sum([3,5,2,3]) → 7          # Pairs: (2,5), (3,3) → max is 7
min_max_pair_sum([3,5,4,2,4,6]) → 8      # Pairs: (2,6), (3,5), (4,4) → max is 8
```

---

### Problem 30: Valid Triangle Number

Count triplets that can form a valid triangle (sum of any two sides > third side).

```
triangle_number([2,2,3,4]) → 3           # (2,2,3), (2,3,4), (2,3,4)
triangle_number([4,2,3,4]) → 4
```

**Hint:** Sort first. For a valid triangle with sorted sides a ≤ b ≤ c, you only need to check a + b > c.

---

## Strategies for Two Pointers

1. **When to use opposite ends:** Sorted arrays, palindrome checks, finding pairs with a target sum.

2. **When to use slow/fast:** In-place modifications, removing elements, cycle detection, finding middle.

3. **When to use two arrays:** Merging, intersection, subsequence checking.

4. **Sorting often helps.** Many two-pointer problems require or benefit from sorted input.

5. **Think about what each pointer represents.** What invariant does it maintain? What condition triggers movement?

6. **Handle duplicates carefully.** In problems like Three Sum, skipping duplicates is crucial for correctness and avoiding TLE.

---

Good luck! Start with Part 1 — the patterns there form the foundation for everything else.
