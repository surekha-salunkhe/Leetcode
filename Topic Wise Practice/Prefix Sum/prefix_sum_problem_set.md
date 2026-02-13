# Prefix Sum Practice

The prefix sum technique precomputes cumulative sums to answer range queries in O(1). The core idea:

```
prefix[i] = arr[0] + arr[1] + ... + arr[i-1]
sum(i, j) = prefix[j+1] - prefix[i]
```

Build the prefix array once in O(n), then answer unlimited range queries in O(1) each.

---

## Part 1: Basic Prefix Sum

### Problem 1: Range Sum Query (Immutable)

Given an array, answer multiple range sum queries efficiently.

```
nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) → 1      # -2 + 0 + 3
sumRange(2, 5) → -1     # 3 + (-5) + 2 + (-1)
sumRange(0, 5) → -3     # entire array
```

**Build:** `prefix = [0, -2, -2, 1, -4, -2, -3]`

**Query:** `sumRange(i, j) = prefix[j] - prefix[i] + nums[i]`

---

### Problem 2: Running Sum of Array

Return an array where each element is the running sum up to that index.

```
running_sum([1, 2, 3, 4]) → [1, 3, 6, 10]
running_sum([1, 1, 1, 1, 1]) → [1, 2, 3, 4, 5]
running_sum([3, 1, 2, 10, 1]) → [3, 4, 6, 16, 17]
```

---

### Problem 3: Find Pivot Index

Find the index where the sum of elements to the left equals the sum to the right.

```
pivot_index([1, 7, 3, 6, 5, 6]) → 3
# Left: 1+7+3 = 11, Right: 5+6 = 11

pivot_index([1, 2, 3]) → -1
# No such index

pivot_index([2, 1, -1]) → 0
# Left sum = 0, Right sum = 1+(-1) = 0
```

---

### Problem 4: Range Sum Query 2D (Immutable)

Given a 2D matrix, answer multiple rectangular region sum queries.

```
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) → 8    # Sum of shaded region below
sumRegion(1, 1, 2, 2) → 11
sumRegion(1, 2, 2, 4) → 12
```

**Hint:** Build a 2D prefix sum where `prefix[i][j]` = sum of all elements in rectangle (0,0) to (i-1,j-1). Use inclusion-exclusion for queries.

---

### Problem 5: Minimum Value to Get Positive Step by Step Sum

Given an array, find the minimum positive starting value such that the running sum is always ≥ 1.

```
min_start_value([−3, 2, −3, 4, 2]) → 5
# Starting with 5: 5→2→4→1→5→7 (always ≥ 1)

min_start_value([1, 2]) → 1
min_start_value([1, -2, -3]) → 5
```

**Hint:** Find the minimum prefix sum, then determine what starting value keeps it positive.

---

## Part 2: Prefix Sum + Hashmap

This powerful combination solves "count/find subarrays with sum = k" problems.

### Problem 6: Subarray Sum Equals K

Count the number of subarrays that sum to exactly k.

```
subarray_sum([1, 1, 1], 2) → 2           # [1,1] at index 0-1 and 1-2
subarray_sum([1, 2, 3], 3) → 2           # [1,2] and [3]
subarray_sum([1, -1, 0], 0) → 3          # [1,-1], [-1,0], [1,-1,0]
```

**Key insight:** If `prefix[j] - prefix[i] = k`, then `sum(i, j) = k`.
Rearranging: we need `prefix[i] = prefix[j] - k`.

**Pattern:**
```cpp
int count = 0;
unordered_map<int, int> freq;
freq[0] = 1;  // empty prefix
int prefix = 0;

for (int num : nums) {
    prefix += num;
    if (freq.count(prefix - k)) {
        count += freq[prefix - k];
    }
    freq[prefix]++;
}
return count;
```

---

### Problem 7: Continuous Subarray Sum

Check if there exists a subarray of length ≥ 2 whose sum is a multiple of k.

```
check_subarray_sum([23, 2, 4, 6, 7], 6) → True    # [2,4] sums to 6
check_subarray_sum([23, 2, 6, 4, 7], 6) → True    # [23,2,6,4,7] sums to 42
check_subarray_sum([23, 2, 6, 4, 7], 13) → False
```

**Hint:** If two prefix sums have the same remainder mod k, the subarray between them sums to a multiple of k.

---

### Problem 8: Subarray Sums Divisible by K

Count subarrays whose sum is divisible by k.

```
subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5) → 7
# [4,5,0,-2,-3,1], [5], [5,0], [5,0,-2,-3], [0], [0,-2,-3], [-2,-3]
```

---

### Problem 9: Contiguous Array (Equal 0s and 1s)

Find the longest contiguous subarray with equal number of 0s and 1s.

```
find_max_length([0, 1]) → 2
find_max_length([0, 1, 0]) → 2           # [0,1] or [1,0]
find_max_length([0, 0, 1, 0, 0, 0, 1, 1]) → 6   # [0,1,0,0,1,1] has 3 zeros and 3 ones
```

**Trick:** Convert 0s to -1s. Now finding equal 0s and 1s becomes finding a subarray with sum = 0.

---

### Problem 10: Binary Subarrays With Sum

Count subarrays of a binary array that sum to exactly goal.

```
num_subarrays_with_sum([1, 0, 1, 0, 1], 2) → 4
# [1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1]

num_subarrays_with_sum([0, 0, 0, 0, 0], 0) → 15
```

---

### Problem 11: Make Sum Divisible by P

Remove the smallest subarray to make the remaining sum divisible by p. Return its length, or -1 if impossible.

```
min_subarray([3, 1, 4, 2], 6) → 1        # Remove [4], remaining sum = 6
min_subarray([6, 3, 5, 2], 9) → 2        # Remove [5,2], remaining sum = 9
min_subarray([1, 2, 3], 3) → 0           # Already divisible
min_subarray([1, 2, 3], 7) → -1          # Impossible
```

**Hint:** If total sum mod p = r, find the shortest subarray with sum ≡ r (mod p).

---

## Part 3: Counting and Binary Arrays

### Problem 12: Count Number of Nice Subarrays

A subarray is "nice" if it contains exactly k odd numbers.

```
count_nice([1, 1, 2, 1, 1], 3) → 2       # [1,1,2,1], [1,2,1,1]
count_nice([2, 4, 6], 1) → 0
count_nice([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) → 16
```

**Hint:** Convert odds to 1, evens to 0. Now it's "subarrays with sum = k" on a binary array.

---

### Problem 13: Number of Subarrays with Bounded Maximum

Count subarrays where the maximum element is in range [left, right].

```
num_subarray_bounded_max([2, 1, 4, 3], 2, 3) → 3
# [2], [2,1], [3]

num_subarray_bounded_max([2, 9, 2, 5, 6], 2, 8) → 7
```

**Hint:** Use `count(max ≤ right) - count(max ≤ left-1)`.

---

### Problem 14: Sum of All Odd Length Subarrays

Return the sum of all odd-length subarrays.

```
sum_odd_length([1, 4, 2, 5, 3]) → 58
# Length 1: 1+4+2+5+3 = 15
# Length 3: (1+4+2)+(4+2+5)+(2+5+3) = 7+11+10 = 28
# Length 5: 1+4+2+5+3 = 15
# Total = 58

sum_odd_length([1, 2]) → 3
sum_odd_length([10, 11, 12]) → 66
```

**Hint:** For each element, count how many odd-length subarrays include it.

---

### Problem 15: Ways to Split Array Into Three Parts

Split array into three non-empty contiguous parts with equal sums.

```
ways_to_split([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) → 3
ways_to_split([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) → 0
ways_to_split([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]) → 1
```

---

## Part 4: 2D Prefix Sum

### Problem 16: Matrix Block Sum

Given a matrix and integer k, for each cell compute the sum of all elements in the block from (i-k, j-k) to (i+k, j+k), clamped to matrix bounds.

```
mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1

Result: [[12,21,16],[27,45,33],[24,39,28]]
# mat[0][0] block: elements (0,0) to (1,1) → 1+2+4+5 = 12
# mat[1][1] block: elements (0,0) to (2,2) → entire matrix = 45
```

---

### Problem 17: Count Square Submatrices with All Ones

Count the total number of square submatrices with all 1s.

```
count_squares([
  [0, 1, 1, 1],
  [1, 1, 1, 1],
  [0, 1, 1, 1]
]) → 15
# 10 squares of size 1, 4 squares of size 2, 1 square of size 3
```

---

### Problem 18: Largest Plus Sign

Given an n×n grid with some cells set to 0, find the largest "plus sign" of 1s.

```
largest_plus_sign(5, [[4,2]]) → 2
# The grid has a 0 at (4,2). The largest plus has arm length 2.
```

---

### Problem 19: Number of Submatrices That Sum to Target

Count submatrices whose elements sum to target.

```
num_submatrix_sum_target([
  [0, 1, 0],
  [1, 1, 1],
  [0, 1, 0]
], 0) → 4

num_submatrix_sum_target([[1, -1], [-1, 1]], 0) → 5
```

**Hint:** Fix two rows, compress columns into 1D, then use "subarray sum = k" technique.

---

### Problem 20: Max Sum of Rectangle No Larger Than K

Find the max sum of a rectangle with sum ≤ k.

```
max_sum_submatrix([[1, 0, 1], [0, -2, 3]], 2) → 2
# Rectangle [[0,1],[-2,3]] sums to 2
```

---

## Part 5: Prefix Products

### Problem 21: Product of Array Except Self

Return an array where each element is the product of all elements except itself. Solve without division.

```
product_except_self([1, 2, 3, 4]) → [24, 12, 8, 6]
product_except_self([-1, 1, 0, -3, 3]) → [0, 0, 9, 0, 0]
```

**Approach:** Use prefix products (left to right) and suffix products (right to left).

---

### Problem 22: Maximum Product Subarray

Find the contiguous subarray with the largest product.

```
max_product([2, 3, -2, 4]) → 6        # [2,3]
max_product([-2, 0, -1]) → 0
max_product([-2, 3, -4]) → 24         # entire array
```

**Hint:** Track both max and min prefix products (negatives can flip).

---

### Problem 23: Product of the Last K Numbers

Design a data structure that supports:
- `add(num)`: Add a number to the stream
- `getProduct(k)`: Return product of last k numbers

```
add(3), add(0), add(2), add(5), add(4)
getProduct(2) → 20    # 5 * 4
getProduct(3) → 40    # 2 * 5 * 4
getProduct(4) → 0     # includes the 0
```

**Hint:** Reset prefix product when you encounter 0.

---

## Part 6: Difference Arrays

The difference array is the inverse of prefix sum. Useful for range update queries.

### Problem 24: Range Addition

Given array of size n initialized to 0, apply multiple range additions efficiently.

```
n = 5
updates = [[1,3,2], [2,4,3], [0,2,-2]]
# [1,3,2] means add 2 to indices 1 through 3

Result: [-2, 0, 3, 5, 3]
```

**Pattern:**
```cpp
// For range [l, r] add val:
diff[l] += val;
diff[r+1] -= val;

// Then prefix sum the diff array to get result
```

---

### Problem 25: Corporate Flight Bookings

n flights, bookings[i] = [first, last, seats] means seats are booked from flight first to last. Return total seats for each flight.

```
bookings = [[1,2,10], [2,3,20], [2,5,25]], n = 5
Result: [10, 55, 45, 25, 25]
```

---

### Problem 26: Car Pooling

Given trips [numPassengers, from, to] and car capacity, determine if all trips are possible.

```
car_pooling([[2,1,5], [3,3,7]], 4) → False
car_pooling([[2,1,5], [3,3,7]], 5) → True
car_pooling([[3,2,7], [3,7,9], [8,3,9]], 11) → True
```

---

### Problem 27: Brightest Position on Street

Lights at positions with ranges [start, end]. Find the brightest position (most overlapping lights).

```
brightest([[−3,2], [1,2], [3,3]]) → -1
# -1 has light from [-3,2], so brightness 1 at -1, but also 1 at other spots
# Actually: position 1 and 2 have 2 lights
```

---

## Part 7: Challenge Problems

### Problem 28: Maximum Sum Circular Subarray

Find the maximum sum of a contiguous subarray, where the array is circular (end wraps to beginning).

```
max_subarray_circular([1, -2, 3, -2]) → 3         # [3]
max_subarray_circular([5, -3, 5]) → 10            # [5,5] wrapping
max_subarray_circular([-3, -2, -3]) → -2          # [-2]
```

**Hint:** Answer is either max normal subarray OR total sum - min subarray (the wrap-around case).

---

### Problem 29: K-Concatenation Maximum Sum

Given array arr, form a new array by concatenating arr k times. Find max subarray sum.

```
k_concat_max_sum([1, 2], 3) → 9           # [1,2,1,2,1,2]
k_concat_max_sum([1, -2, 1], 5) → 2       # [1,1] from adjacent copies
k_concat_max_sum([-1, -2], 7) → 0         # All negative, take empty
```

---

### Problem 30: Longest Well-Performing Interval

Given hours worked each day, a day is "tiring" if hours > 8. Find the longest interval where tiring days > non-tiring days.

```
longest_well_performing([9, 9, 6, 0, 6, 6, 9]) → 3
# Days 0-2: [9,9,6] has 2 tiring, 1 non-tiring → well-performing
```

**Hint:** Convert to +1 (tiring) and -1 (non-tiring). Find longest subarray with sum > 0.

---

## Strategies for Prefix Sum

1. **Build prefix array with length n+1:** Makes indexing cleaner with `prefix[0] = 0`.

2. **Range sum formula:** `sum(i, j) = prefix[j+1] - prefix[i]`

3. **"Subarray sum = k" pattern:** Use hashmap to find `prefix[i] = prefix[j] - k`. Initialize `map[0] = 1`.

4. **Modular arithmetic:** For "sum divisible by k", track `prefix % k` in hashmap.

5. **Transform the problem:** Convert 0s to -1s for equal count problems. Convert conditions to binary for counting.

6. **2D prefix sum:** Use inclusion-exclusion. Build prefix where `prefix[i][j]` = sum of rectangle (0,0) to (i-1, j-1).

7. **Difference arrays:** For range updates, use `diff[l] += val, diff[r+1] -= val`, then prefix sum.

8. **Prefix + suffix:** For "product except self" style problems, compute both directions separately.

---

## Common Patterns Summary

| Problem Type | Technique |
|--------------|-----------|
| Range sum query | Basic prefix sum |
| Count subarrays with sum = k | Prefix sum + hashmap |
| Sum divisible by k | Prefix mod + hashmap |
| Equal 0s and 1s | Convert to +1/-1, find sum = 0 |
| Range updates | Difference array |
| Product except self | Prefix + suffix products |
| 2D range sum | 2D prefix sum |

---

Good luck! Start with Part 1 to master the basics, then move to the hashmap combination in Part 2 — that's where the real power of prefix sum shines.
