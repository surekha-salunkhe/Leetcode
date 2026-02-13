# HashSet & HashMap Practice: Existence and Lookup

The core power of hash-based structures is **O(1) average lookup**. This problem set focuses on the fundamental pattern: checking if an element exists.

**HashSet:** Store elements, check membership. No duplicates.
**HashMap:** Store key-value pairs, lookup values by key.

---

## Part 1: HashSet — Does It Exist?

### Problem 1: Contains Duplicate

Return true if any value appears at least twice in the array.

```
contains_duplicate([1, 2, 3, 1]) → True
contains_duplicate([1, 2, 3, 4]) → False
contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) → True
```

**Pattern:** Add elements to a set. If you try to add one that's already there, you found a duplicate.

---

### Problem 2: Missing Number

Given an array containing n distinct numbers in the range [0, n], find the missing one.

```
missing_number([3, 0, 1]) → 2
missing_number([0, 1]) → 2
missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) → 8
```

**Hint:** Put all numbers in a set, then check which number from 0 to n is missing.

---

### Problem 3: Single Number

Every element appears twice except for one. Find that single one.

```
single_number([2, 2, 1]) → 1
single_number([4, 1, 2, 1, 2]) → 4
single_number([1]) → 1
```

**Hint:** If a number is in the set, remove it. If not, add it. What remains?

---

### Problem 4: Intersection of Two Arrays

Return the intersection (unique common elements) of two arrays.

```
intersection([1, 2, 2, 1], [2, 2]) → [2]
intersection([4, 9, 5], [9, 4, 9, 8, 4]) → [9, 4]
```

---

### Problem 5: Happy Number

A number is "happy" if repeatedly summing the squares of its digits eventually reaches 1. Return true if n is happy.

```
is_happy(19) → True
# 1² + 9² = 82
# 8² + 2² = 68
# 6² + 8² = 100
# 1² + 0² + 0² = 1 ✓

is_happy(2) → False   # Eventually loops
```

**Hint:** Use a set to detect cycles. If you see the same number twice, it's not happy.

---

### Problem 6: Isomorphic Strings

Two strings are isomorphic if characters in s can be replaced to get t (one-to-one mapping, preserving order).

```
is_isomorphic("egg", "add") → True       # e→a, g→d
is_isomorphic("foo", "bar") → False      # o can't map to both a and r
is_isomorphic("paper", "title") → True   # p→t, a→i, e→l, r→e
is_isomorphic("badc", "baba") → False    # d→b and c→a, but b already maps to b
```

**Hint:** Track which characters have been mapped (in both directions).

---

### Problem 7: Word Pattern

Check if a pattern matches a string of words (bijective mapping).

```
word_pattern("abba", "dog cat cat dog") → True
word_pattern("abba", "dog cat cat fish") → False
word_pattern("aaaa", "dog cat cat dog") → False
word_pattern("abba", "dog dog dog dog") → False
```

---

### Problem 8: Valid Sudoku

Determine if a 9×9 Sudoku board is valid. Only filled cells need to be validated (no duplicates in rows, columns, or 3×3 boxes).

```
Each row must contain 1-9 with no duplicates
Each column must contain 1-9 with no duplicates
Each 3×3 box must contain 1-9 with no duplicates
```

**Hint:** Use sets to track seen numbers for each row, column, and box.

---

### Problem 9: Longest Consecutive Sequence

Find the length of the longest consecutive elements sequence. Must run in O(n).

```
longest_consecutive([100, 4, 200, 1, 3, 2]) → 4
# Sequence: [1, 2, 3, 4]

longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) → 9
# Sequence: [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

**Hint:** Put all numbers in a set. For each number, only start counting if `num - 1` is NOT in the set (this ensures you start from the beginning of a sequence).

---

### Problem 10: Jewels and Stones

Given a string of jewel types and a string of stones you have, count how many of your stones are jewels.

```
count_jewels("aA", "aAAbbbb") → 3      # 'a' and 'A' are jewels
count_jewels("z", "ZZ") → 0
```

---

## Part 2: HashMap — Lookup by Key

### Problem 11: Two Sum

Find two indices whose values add up to target.

```
two_sum([2, 7, 11, 15], 9) → [0, 1]    # 2 + 7 = 9
two_sum([3, 2, 4], 6) → [1, 2]         # 2 + 4 = 6
two_sum([3, 3], 6) → [0, 1]
```

**Pattern:** For each number, check if `target - num` exists in the map. Store `{num: index}`.

---

### Problem 12: First Unique Character

Find the index of the first non-repeating character in a string. Return -1 if none.

```
first_unique("leetcode") → 0           # 'l' is first unique
first_unique("loveleetcode") → 2       # 'v' is first unique
first_unique("aabb") → -1
```

**Hint:** Count frequencies first, then scan again to find the first with count = 1.

---

### Problem 13: Valid Anagram

Check if two strings are anagrams (same characters, same frequencies).

```
is_anagram("anagram", "nagaram") → True
is_anagram("rat", "car") → False
is_anagram("listen", "silent") → True
```

---

### Problem 14: Ransom Note

Check if you can construct ransom note from magazine letters (each letter used once).

```
can_construct("a", "b") → False
can_construct("aa", "ab") → False
can_construct("aa", "aab") → True
```

---

### Problem 15: Find All Anagrams in a String

Find all start indices of anagrams of p in s.

```
find_anagrams("cbaebabacd", "abc") → [0, 6]
# "cba" at index 0, "bac" at index 6

find_anagrams("abab", "ab") → [0, 1, 2]
```

**Hint:** Use a frequency map and sliding window of size len(p).

---

### Problem 16: Group Anagrams

Group strings that are anagrams of each other.

```
group_anagrams(["eat","tea","tan","ate","nat","bat"])
→ [["bat"], ["nat","tan"], ["ate","eat","tea"]]
```

**Hint:** Use sorted string (or character count tuple) as the key.

---

### Problem 17: Majority Element

Find the element that appears more than n/2 times.

```
majority_element([3, 2, 3]) → 3
majority_element([2, 2, 1, 1, 1, 2, 2]) → 2
```

---

### Problem 18: Find the Difference

Two strings s and t where t is s with one extra letter shuffled. Find the extra letter.

```
find_the_difference("abcd", "abcde") → 'e'
find_the_difference("", "y") → 'y'
find_the_difference("a", "aa") → 'a'
```

---

### Problem 19: Intersection of Two Arrays II

Return the intersection including duplicates (each element appears as many times as it shows in both).

```
intersect([1, 2, 2, 1], [2, 2]) → [2, 2]
intersect([4, 9, 5], [9, 4, 9, 8, 4]) → [4, 9]
```

**Hint:** Count frequencies in one array, then iterate through the other, decrementing counts.

---

### Problem 20: Roman to Integer

Convert a Roman numeral to an integer.

```
roman_to_int("III") → 3
roman_to_int("LVIII") → 58      # L=50, V=5, III=3
roman_to_int("MCMXCIV") → 1994  # M=1000, CM=900, XC=90, IV=4
```

**Hint:** Map symbols to values. If a smaller value precedes a larger, subtract it.

---

## Part 3: Frequency Counting

### Problem 21: Top K Frequent Elements

Return the k most frequent elements.

```
top_k_frequent([1, 1, 1, 2, 2, 3], 2) → [1, 2]
top_k_frequent([1], 1) → [1]
top_k_frequent([1, 2], 2) → [1, 2]
```

---

### Problem 22: Sort Characters By Frequency

Sort a string by character frequency (descending).

```
frequency_sort("tree") → "eert" or "eetr"
frequency_sort("cccaaa") → "aaaccc" or "cccaaa"
frequency_sort("Aabb") → "bbAa" or "bbaA"
```

---

### Problem 23: Find All Numbers Disappeared in Array

Given array of n integers where each is in range [1, n], find all numbers in [1, n] that don't appear.

```
find_disappeared([4, 3, 2, 7, 8, 2, 3, 1]) → [5, 6]
find_disappeared([1, 1]) → [2]
```

---

### Problem 24: Find All Duplicates in Array

Elements appear once or twice. Find all elements that appear twice.

```
find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) → [2, 3]
find_duplicates([1, 1, 2]) → [1]
find_duplicates([1]) → []
```

---

### Problem 25: Unique Number of Occurrences

Check if the number of occurrences of each value is unique.

```
unique_occurrences([1, 2, 2, 1, 1, 3]) → True
# 1 appears 3 times, 2 appears 2 times, 3 appears 1 time
# Counts [3, 2, 1] are all unique

unique_occurrences([1, 2]) → False
# Both appear 1 time, not unique

unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) → True
```

---

## Part 4: Index Tracking

### Problem 26: Contains Duplicate II

Check if there are two equal elements within k indices of each other.

```
contains_nearby_duplicate([1, 2, 3, 1], 3) → True      # indices 0 and 3
contains_nearby_duplicate([1, 0, 1, 1], 1) → True      # indices 2 and 3
contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) → False
```

**Hint:** Map each number to its last seen index.

---

### Problem 27: Shortest Word Distance

Given a list of words and two words, find the shortest distance between them.

```
shortest_distance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice") → 3
shortest_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding") → 1
```

---

### Problem 28: Logger Rate Limiter

Design a logger that returns true if a message should be printed (hasn't been printed in the last 10 seconds).

```
logger = Logger()
logger.should_print(1, "foo")  → True   # First time
logger.should_print(2, "bar")  → True
logger.should_print(3, "foo")  → False  # Within 10 seconds
logger.should_print(8, "bar")  → False
logger.should_print(10, "foo") → False
logger.should_print(11, "foo") → True   # 10 seconds passed
```

---

### Problem 29: Find Common Characters

Find characters that appear in all strings (including duplicates).

```
common_chars(["bella", "label", "roller"]) → ["e", "l", "l"]
common_chars(["cool", "lock", "cook"]) → ["c", "o"]
```

**Hint:** Track minimum frequency of each character across all strings.

---

### Problem 30: N-Repeated Element in Size 2N Array

In an array of size 2n, there are n+1 unique elements. One appears n times, others appear once. Find the repeated one.

```
repeated_n_times([1, 2, 3, 3]) → 3
repeated_n_times([2, 1, 2, 5, 3, 2]) → 2
repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]) → 5
```

---

## Strategies

### When to Use HashSet

- Check if element exists → O(1)
- Remove duplicates
- Find unique elements
- Detect cycles (seen before?)
- Set operations (intersection, union)

### When to Use HashMap

- Count frequencies → `map[x]++`
- Store index of element → `map[x] = i`
- Store value for lookup → `map[key] = value`
- Group items by key → `map[key].append(item)`
- Check complement exists → `target - x in map?`

### Common Patterns

```cpp
// Pattern 1: Check existence while iterating
unordered_set<int> seen;
for (int x : arr) {
    if (seen.count(x)) {
        // Found duplicate or complement
    }
    seen.insert(x);
}

// Pattern 2: Count frequencies
unordered_map<int, int> freq;
for (int x : arr) {
    freq[x]++;
}

// Pattern 3: Store indices
unordered_map<int, int> index;
for (int i = 0; i < arr.size(); i++) {
    if (index.count(target - arr[i])) {
        // Found pair at indices index[target - arr[i]] and i
    }
    index[arr[i]] = i;
}

// Pattern 4: Track last seen position
unordered_map<int, int> last_seen;
for (int i = 0; i < arr.size(); i++) {
    if (last_seen.count(arr[i]) && i - last_seen[arr[i]] <= k) {
        // Found duplicate within k distance
    }
    last_seen[arr[i]] = i;
}
```

---

## Complexity Reminder

| Operation | HashSet  | HashMap  |
| --------- | -------- | -------- |
| Insert    | O(1) avg | O(1) avg |
| Lookup    | O(1) avg | O(1) avg |
| Delete    | O(1) avg | O(1) avg |
| Space     | O(n)     | O(n)     |

Worst case is O(n) due to hash collisions, but rare in practice.

---

Good luck! Start with Part 1 for set-based existence checks, then Part 2 for map-based lookups. The patterns here form the building blocks for more advanced techniques.
