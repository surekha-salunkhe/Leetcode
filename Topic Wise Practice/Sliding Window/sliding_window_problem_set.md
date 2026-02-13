# Sliding Window Practice

The sliding window technique maintains a "window" over a contiguous portion of an array or string, expanding or shrinking it as needed. Two main types:

- **Fixed-size window:** Window size is constant (e.g., "find max sum of k consecutive elements")
- **Variable-size window:** Window grows/shrinks based on a condition (e.g., "find smallest subarray with sum ≥ target")

---

## Part 1: Fixed-Size Window

### Problem 1: Maximum Sum of K Consecutive Elements

Given an array and integer k, find the maximum sum of any k consecutive elements.

```
max_sum([2, 1, 5, 1, 3, 2], 3) → 9         # [5, 1, 3]
max_sum([2, 3, 4, 1, 5], 2) → 7            # [3, 4]
max_sum([1, 1, 1, 1, 1], 3) → 3
```

**Pattern:** Compute sum of first k elements. Then slide: add the next element, subtract the element leaving the window.

---

### Problem 2: Maximum Average Subarray

Find the contiguous subarray of length k with the maximum average.

```
max_average([1, 12, -5, -6, 50, 3], 4) → 12.75    # [12, -5, -6, 50] = 51/4
max_average([5], 1) → 5.0
```

---

### Problem 3: Contains Duplicate II

Check if there are two distinct indices i and j such that `nums[i] == nums[j]` and `|i - j| <= k`.

```
contains_nearby_duplicate([1,2,3,1], 3) → True      # indices 0 and 3
contains_nearby_duplicate([1,0,1,1], 1) → True      # indices 2 and 3
contains_nearby_duplicate([1,2,3,1,2,3], 2) → False
```

**Hint:** Maintain a set of elements in the current window of size k.

---

### Problem 4: Number of Subarrays of Size K with Average ≥ Threshold

Count subarrays of exactly size k whose average is greater than or equal to threshold.

```
num_subarrays([2,2,2,2,5,5,5,8], 3, 4) → 3
# Subarrays: [2,5,5], [5,5,5], [5,5,8] all have avg >= 4

num_subarrays([11,13,17,23,29,31,7,5,2,3], 3, 5) → 6
```

---

### Problem 5: Maximum Number of Vowels in a Substring

Find the maximum number of vowels in any substring of length k.

```
max_vowels("abciiidef", 3) → 3              # "iii"
max_vowels("aeiou", 2) → 2
max_vowels("leetcode", 3) → 2               # "lee" or "eet"
max_vowels("rhythms", 4) → 0
```

---

### Problem 6: Minimum Difference Between Highest and Lowest of K Scores

Given an array of scores, choose any k scores and minimize the difference between the highest and lowest.

```
min_difference([90], 1) → 0
min_difference([9, 4, 1, 7], 2) → 2         # Choose [7, 9], diff = 2
min_difference([87063,61094,44530,21297,95857,93551,9918], 6) → 74560
```

**Hint:** Sort first, then use fixed-size window.

---

### Problem 7: Find All Anagrams in a String

Find all start indices of anagrams of pattern `p` in string `s`.

```
find_anagrams("cbaebabacd", "abc") → [0, 6]
# "cba" at index 0, "bac" at index 6

find_anagrams("abab", "ab") → [0, 1, 2]
```

**Hint:** Maintain character frequency counts for the window and pattern. Compare counts as you slide.

---

### Problem 8: Permutation in String

Check if any permutation of `s1` exists as a substring in `s2`.

```
check_inclusion("ab", "eidbaooo") → True    # "ba" is a permutation of "ab"
check_inclusion("ab", "eidboaoo") → False
```

---

### Problem 9: Sliding Window Maximum

Return the maximum element in each sliding window of size k.

```
max_sliding_window([1,3,-1,-3,5,3,6,7], 3) → [3,3,5,5,6,7]
# Window positions:
# [1  3  -1] -3  5  3  6  7  → 3
#  1 [3  -1  -3] 5  3  6  7  → 3
#  1  3 [-1  -3  5] 3  6  7  → 5
#  1  3  -1 [-3  5  3] 6  7  → 5
#  1  3  -1  -3 [5  3  6] 7  → 6
#  1  3  -1  -3  5 [3  6  7] → 7

max_sliding_window([1], 1) → [1]
```

**Challenge:** Solve in O(n) using a deque (monotonic queue).

---

## Part 2: Variable-Size Window (Shrink to Valid)

These problems expand the window, then shrink it when a condition is violated.

### Problem 10: Minimum Size Subarray Sum

Find the minimal length of a subarray whose sum is ≥ target. Return 0 if none exists.

```
min_subarray_len(7, [2,3,1,2,4,3]) → 2      # [4,3]
min_subarray_len(4, [1,4,4]) → 1            # [4]
min_subarray_len(11, [1,1,1,1,1,1,1,1]) → 0
```

**Pattern:** Expand right until sum ≥ target, then shrink from left while still valid, tracking minimum length.

---

### Problem 11: Longest Substring Without Repeating Characters

Find the length of the longest substring without duplicate characters.

```
length_of_longest("abcabcbb") → 3           # "abc"
length_of_longest("bbbbb") → 1              # "b"
length_of_longest("pwwkew") → 3             # "wke"
length_of_longest("") → 0
```

---

### Problem 12: Longest Substring with At Most K Distinct Characters

Find the length of the longest substring containing at most k distinct characters.

```
longest_k_distinct("eceba", 2) → 3          # "ece"
longest_k_distinct("aa", 1) → 2             # "aa"
longest_k_distinct("aabacbebebe", 3) → 7    # "cbebebe"
```

---

### Problem 13: Fruit Into Baskets

You have a row of trees, each with a type of fruit. You have two baskets, each can hold one type. Starting from any tree, pick consecutive trees. Find the maximum number of fruits you can collect.

```
total_fruit([1,2,1]) → 3                    # All trees
total_fruit([0,1,2,2]) → 3                  # [1,2,2]
total_fruit([1,2,3,2,2]) → 4                # [2,3,2,2]
total_fruit([3,3,3,1,2,1,1,2,3,3,4]) → 5    # [1,2,1,1,2]
```

**This is "longest subarray with at most 2 distinct elements" in disguise.**

---

### Problem 14: Max Consecutive Ones III

Given a binary array, you can flip at most k 0s to 1s. Find the longest sequence of consecutive 1s.

```
longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) → 6
# Flip zeros at indices 5 and 10: [1,1,1,0,0,1,1,1,1,1,1]

longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) → 10
```

**Reframe:** Find the longest subarray with at most k zeros.

---

### Problem 15: Longest Repeating Character Replacement

Given a string and integer k, you can change at most k characters. Find the length of the longest substring with all identical characters.

```
character_replacement("ABAB", 2) → 4        # Replace both As or both Bs
character_replacement("AABABBA", 1) → 4     # Replace one B → "AABAB[B→A]A" or "AAA[A]BBA"
```

**Key insight:** A window is valid if `window_length - count_of_most_frequent_char <= k`.

---

### Problem 16: Subarray Product Less Than K

Count subarrays where the product of all elements is less than k.

```
num_subarray_product([10, 5, 2, 6], 100) → 8
# [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]

num_subarray_product([1, 2, 3], 0) → 0
```

**Counting trick:** When the window is valid, all subarrays ending at right are valid. That's `right - left + 1` subarrays.

---

## Part 3: Variable-Size Window (Expand to Valid)

These problems shrink the window, then expand it when a condition is satisfied.

### Problem 17: Minimum Window Substring

Find the minimum window in `s` that contains all characters of `t` (including duplicates).

```
min_window("ADOBECODEBANC", "ABC") → "BANC"
min_window("a", "a") → "a"
min_window("a", "aa") → ""                  # Need two 'a's
```

**Pattern:** Expand until window contains all of t, then shrink from left while still valid, tracking minimum.

---

### Problem 18: Substring with Concatenation of All Words

Find all starting indices where a concatenation of all words (in any order) appears in s. All words have the same length.

```
find_substring("barfoothefoobarman", ["foo","bar"]) → [0, 9]
# "barfoo" at 0, "foobar" at 9

find_substring("wordgoodgoodgoodbestword", ["word","good","best","word"]) → []

find_substring("barfoofoobarthefoobarman", ["bar","foo","the"]) → [6, 9, 12]
```

---

### Problem 19: Smallest Range Covering Elements from K Lists

Given k sorted lists, find the smallest range that includes at least one element from each list.

```
smallest_range([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]) → [20, 24]
# 24 from list 0, 20 from list 1, 22 from list 2
```

---

## Part 4: String-Specific Problems

### Problem 20: Longest Substring with At Least K Repeating Characters

Find the length of the longest substring where every character appears at least k times.

```
longest_substring("aaabb", 3) → 3           # "aaa"
longest_substring("ababbc", 2) → 5          # "ababb"
longest_substring("weitong", 2) → 0
```

**Hint:** This one is tricky for pure sliding window. Consider iterating over the number of unique characters (1 to 26) and using sliding window for each.

---

### Problem 21: Count Number of Nice Subarrays

A subarray is "nice" if it contains exactly k odd numbers. Count nice subarrays.

```
count_nice([1,1,2,1,1], 3) → 2              # [1,1,2,1], [1,2,1,1]
count_nice([2,4,6], 1) → 0
count_nice([2,2,2,1,2,2,1,2,2,2], 2) → 16
```

**Hint:** Use the "at most k" trick: `exactly_k = at_most_k - at_most_(k-1)`.

---

### Problem 22: Subarrays with K Different Integers

Count subarrays with exactly k distinct integers.

```
subarrays_with_k([1,2,1,2,3], 2) → 7
# [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

subarrays_with_k([1,2,1,3,4], 3) → 3
# [1,2,1,3], [2,1,3], [1,3,4]
```

**Same trick:** `exactly_k = at_most_k - at_most_(k-1)`.

---

### Problem 23: Longest Subarray of 1's After Deleting One Element

Given a binary array, delete exactly one element. Find the longest subarray of 1s.

```
longest_subarray([1,1,0,1]) → 3             # Delete the 0
longest_subarray([0,1,1,1,0,1,1,0,1]) → 5   # Delete 0 at index 4
longest_subarray([1,1,1]) → 2               # Must delete one element
```

**Hint:** Similar to "Max Consecutive Ones III" with k=1, but you must use the deletion.

---

### Problem 24: Get Equal Substrings Within Budget

Given two strings of equal length and a max cost, find the longest substring of `s` that can be changed to the corresponding substring of `t` with cost ≤ maxCost. Cost of changing s[i] to t[i] is `|s[i] - t[i]|`.

```
equal_substring("abcd", "bcdf", 3) → 3
# "abc" → "bcd" costs |a-b| + |b-c| + |c-d| = 1+1+1 = 3

equal_substring("abcd", "cdef", 3) → 1
# Each change costs 2, so max length is 1

equal_substring("abcd", "acde", 0) → 1
# Only 'c' matches 'c'
```

---

## Part 5: Challenge Problems

### Problem 25: Minimum Number of K Consecutive Bit Flips

Given a binary array, a k-bit flip changes k consecutive bits (0→1, 1→0). Return the minimum number of flips to make all elements 1, or -1 if impossible.

```
min_k_bit_flips([0,1,0], 1) → 2             # Flip index 0 and 2
min_k_bit_flips([1,1,0], 2) → -1            # Impossible
min_k_bit_flips([0,0,0,1,0,1,1,0], 3) → 3
```

---

### Problem 26: Grumpy Bookstore Owner

Owner is grumpy on some minutes (customers during grumpy minutes don't count as satisfied). Using a secret technique, owner can be not grumpy for k consecutive minutes. Maximize satisfied customers.

```
grumpy_customers([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3) → 16
# customers:    1  0  1  2  1  1  7  5
# grumpy:       0  1  0  1  0  1  0  1
# Use technique on minutes 3-5: all customers during [2,1,1] become satisfied
# Total: 1 + 1 + 1 + 2 + 1 + 1 + 7 + 5 = 16... wait let me recalc
# Without technique: 1 + 1 + 1 + 7 = 10 (non-grumpy minutes)
# Technique on [3,4,5]: gain 2 + 1 + 1 = 4 → total 14
# Better: technique on [5,6,7]: gain 1 + 0 + 5 = 6 → total 16
```

---

### Problem 27: Maximum Points from Cards

Cards in a row with point values. Take exactly k cards from either end. Maximize total points.

```
max_score([1,2,3,4,5,6,1], 3) → 12          # Take 1, 6, 5 from right: 1+6+5=12?
                                            # Or 1 from left, 1+6 from right = 8
                                            # Actually: 6+5+1 from right = 12
max_score([9,7,7,9,7,7,9], 7) → 55          # Take all
max_score([1,1000,1], 1) → 1                # Must take from end
```

**Reframe:** You're leaving a contiguous subarray of size n-k in the middle. Minimize that subarray's sum.

---

### Problem 28: Minimum Operations to Reduce X to Zero

Given an array and integer x, remove elements from either end to make them sum to exactly x. Return minimum operations, or -1 if impossible.

```
min_operations([1,1,4,2,3], 5) → 2          # Remove 2,3 from right
min_operations([5,6,7,8,9], 4) → -1
min_operations([3,2,20,1,1,3], 10) → 5      # Remove 3,2 from left, 1,1,3 from right
```

**Reframe:** Find the longest subarray with sum = total - x.

---

### Problem 29: Minimum Swaps to Group All 1's Together

Given a binary array, find the minimum swaps needed to group all 1s together in any position.

```
min_swaps([1,0,1,0,1]) → 1                  # Swap to get [1,1,1,0,0]
min_swaps([0,0,0,1,0]) → 0                  # Already grouped
min_swaps([1,0,1,0,1,0,0,1,1,0,1]) → 3
```

**Hint:** Window size = total count of 1s. Find window with maximum 1s (minimum 0s to swap out).

---

### Problem 30: Frequency of the Most Frequent Element

You can increment any element (by 1) at most k times total. Find the maximum possible frequency of any element.

```
max_frequency([1,2,4], 5) → 3               # Increment 1→4, 2→4: cost = 3+2 = 5
max_frequency([1,4,8,13], 5) → 2            # Increment 4→8: cost = 4
max_frequency([3,9,6], 2) → 1
```

**Hint:** Sort first. Use sliding window where the cost to make all elements equal to the rightmost is `(right - left + 1) * nums[right] - window_sum`.

---

## Sliding Window Strategies

1. **Fixed vs Variable:** Know which type you need. Fixed = constant window size. Variable = grow/shrink based on conditions.

2. **The expand-then-shrink pattern:**

   ```
   for right in range(n):
       # expand: add nums[right] to window
       while window_is_invalid:
           # shrink: remove nums[left] from window
           left += 1
       # update answer
   ```

3. **Track window state efficiently:** Use hashmaps for character counts, running sums, or frequency maps. Avoid recomputing from scratch.

4. **The "exactly k" trick:** If you can solve "at most k", then `exactly_k = at_most_k - at_most_(k-1)`.

5. **Reframing problems:** Many problems are sliding window in disguise. "Take from ends" often means "leave a window in the middle."

6. **When to use a deque:** For "maximum/minimum in window" with O(1) updates, use a monotonic deque.

---

Good luck! Start with Part 1 to get the fixed-size pattern down, then move to variable-size in Parts 2-3.
