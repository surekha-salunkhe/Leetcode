## Part 1: HashSet — Does It Exist? [1-10]
## Part 2: HashMap — Lookup by Key [11-20]
## Part 3: Frequency Counting [21-25]
## Part 4: Index Tracking [26-30]

###########################################################
### Problem 1: Contains Duplicate
# Return true if any value appears at least twice.
# Hint: Use a set to track seen numbers.

# def contains_duplicate(nums):
#     sets = set()

#     for i in nums:
#         if i in sets:
#             return True
#         else:
#           sets.add(i)
#     return False


# if __name__ == "__main__":
#     print(contains_duplicate([1,2,3,1]))
#     print(contains_duplicate([1,2,3,4]))
#     print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


###########################################################
### Problem 2: Missing Number
# Numbers are in range [0, n]. One is missing.
# Hint: Put in set, scan from 0..n.

# def missing_number(nums):
#     sets = set(nums)

#     for i in range(len(nums) + 1):
#         if i not in sets:
#             return i
#     return -1

# if __name__ == "__main__":
#     print(missing_number([3,0,1]))
#     print(missing_number([0,1]))
#     print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))


###########################################################
### Problem 3: Single Number
# Every element appears twice except one.
# Hint: Add/remove from set.

# def single_number(nums):
#     sets = set()

#     for i in nums:
#         if i in sets:
#             sets.remove(i)
#         else:
#             sets.add(i)
#     return sets.pop()

# if __name__ == "__main__":
#     print(single_number([2,2,1]))
#     print(single_number([4,1,2,1,2]))
#     print(single_number([1]))
###########################################################
### Problem 4: Intersection of Two Arrays
# Return unique intersection.
# Hint: Convert to sets.

# def intersection(nums1, nums2):

#     # Approach 1
#     # sets1 = set(nums1)
#     # sets2 = set(nums2)
#     # return list(sets1.intersection(sets2))
#     # return list(set(nums1) & set(nums2))

#     #Approach 2
#     sets = set(nums1)
#     result = set()

#     for i in nums2:
#         if i in sets:
#             result.add(i)
#     return list(result)
    
#     #O(n+m) time and O(n) space
#     # if space constraints then have to go with sort + two pointer

# if __name__ == "__main__":
#     print(intersection([1,2,2,1], [2,2]))
#     print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
###########################################################
### Problem 5: Happy Number
# Detect cycle while summing squares of digits.
# Hint: Use a set.

# def is_happy(n):
#     sets = set()

#     while n != 1:
#         if n in sets:
#             return False # cycle detected like example 2
#         sets.add(n)
#         total = 0
#         while n > 0:
#             digit = n % 10
#             total += digit * digit
#             n //= 10
        
#         n = total
#     return True

# if __name__ == "__main__":
#     print(is_happy(19)) # 82, 68, 100, 1
#     print(is_happy(2)) #2, 4, 8, 16, 37, 58, 89, 145, 42, 20, 2


###########################################################
### Problem 6: Isomorphic Strings
# Characters must map one-to-one.
# Hint: Two hashmaps.

# def is_isomorphic(s, t):
#     dict1 = {}
#     dict2 = {}

#     if len(s) != len(t):
#         return False
    
#     for i in range(len(s)):
#         c1 = s[i]
#         c2 = t[i]

#         if c1 in dict1:
#             if dict1[c1] != c2: # g == g
#                 return False
#         else:
#             dict1[c1] = c2 # e: a, g: d

#         if c2 in dict2:
#             if dict2[c2] != c1: # g == g
#                 return False
#         else:
#             dict2[c2] = c1 # a: e, d: g
    
#     return True


# if __name__ == "__main__":
#     print(is_isomorphic("egg", "add"))
#     print(is_isomorphic("foo", "bar"))
#     print(is_isomorphic("paper", "title"))
#     print(is_isomorphic("badc", "baba")) # {b:b. a:a, d:b c:a}, {b:b, a:a, b:d, a:c}

###########################################################
### Problem 7: Word Pattern
# Pattern letters must map to words.
# Hint: Two dictionaries.

# def word_pattern(pattern, s):
#     dict1 = {}
#     dict2 = {}

#     s = s.split(" ")
    
#     if len(pattern) != len(s):
#         return False
    
#     for i in range(len(s)):
#         c1 = pattern[i] #a
#         c2 = s[i] #dog

#         if c1 in dict1:
#             if dict1[c1] != c2: #cat == cat, dog != fish = False
#                 return False
#         else:
#             dict1[c1] = c2 # a: dog, b: cat

#         if c2 in dict2:
#             if dict2[c2] != c1: #b == b
#                 return False
#         else:
#             dict2[c2] = c1 # dog: a, cat: b
        
#     return True

# if __name__ == "__main__":
#     print(word_pattern("abba", "dog cat cat dog"))
#     print(word_pattern("abba", "dog cat cat fish"))
#     print(word_pattern("aaaa", "dog cat cat dog"))
#     print(word_pattern("abba", "dog dog dog dog"))


###########################################################
# ### Problem 8: Valid Sudoku
# # Check rows, cols, boxes.
# # Hint: Sets per row/col/box.

# def is_valid_sudoku(board):
#     sets_row = [set() for _ in range(9)]
#     sets_col = [set() for _ in range(9)]
#     sets_box = [set() for _ in range(9)]

#     row = len(board)
#     col = len(board[0])

#     for r in range(row):
#         for c in range(col):

#             if board[r][c] == '.':
#                 continue

#             val = board[r][c]
#             box_id = (r // 3) * 3 + (c // 3)

#             if val in sets_row[r] or val in sets_col[c] or val in sets_box[box_id]:
#                 return False

#             sets_row[r].add(val)
#             sets_col[c].add(val)
#             sets_box[box_id].add(val)
#     return True

# # Think in two steps:
# # Divide by 3 → find which box row/col
# # Flatten 2D → 1D with row*3 + col (I treat the boxes in row-major order)

# if __name__ == "__main__":

#     # Valid board
#     board1 = [
#         ["5","3",".",".","7",".",".",".","."],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]
#     ]

#     # Invalid board (duplicate 5 in first row)
#     board2 = [
#         ["5","3",".",".","7",".",".",".","5"],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]
#     ]

#     # When implemented, these should print:
#     # True
#     # False

#     print(is_valid_sudoku(board1))
#     print(is_valid_sudoku(board2))

###########################################################
# ### Problem 9: Longest Consecutive Sequence
# # O(n) using set.
# # Hint: Start when num-1 not present.

# def longest_consecutive(nums):
#     sets = set(nums)
#     max_len = 0

#     for i in sets:
#         if (i - 1) not in sets:
#             curr = i
#             length = 1

#             while curr + 1 in sets:
#                 curr += 1
#                 length += 1
            
#             max_len = max(max_len, length)
#     return max_len


# # Put all numbers in a set: num_set = set(nums)
# # For each number num:
# # Only start counting if num - 1 is not in the set (this ensures we start at the beginning of a consecutive sequence)
# # Expand the sequence:
# # Keep checking num + 1, num + 2, … in the set and increment length
# # Keep track of the max length.

# if __name__ == "__main__":
#     print(longest_consecutive([100,4,200,1,3,2]))
#     print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

###########################################################
# ## Problem 10: Jewels and Stones
# # Count chars in stones that are jewels.
# # Hint: Jewel set.

# def count_jewels(jewels, stones):
#     jewels_set = set(jewels)
#     count = 0
#     for i in stones:
#         if i in jewels_set:
#             count += 1
    
#     return count

# if __name__ == "__main__":
#     print(count_jewels("aA", "aAAbbbb"))
#     print(count_jewels("z", "ZZ"))


###########################################################
# ## Problem 11: Two Sum
# # Return indices.
# # Hint: HashMap storing seen numbers.

# def two_sum(nums, target):
#     nums_dict = {} # 2: 0, 7: 1, 

#     for i in range(len(nums)):
#         comp = target - nums[i]

#         if comp in nums_dict:
#             return [nums_dict[comp], i]
        
#         nums_dict[nums[i]] = i
    
#     return []

# if __name__ == "__main__":
#     print(two_sum([2,7,11,15], 9))
#     print(two_sum([3, 2, 4], 6))
#     print(two_sum([3, 3], 6))


###########################################################
### Problem 12: First Unique Character
# Return index of first char with freq 1.

# def first_unique(s):
#     s_dict =  {}

#     for i in s:
#         s_dict[i] = s_dict.get(i, 0) + 1
    
#     for i in range(len(s)):
#         if s[i] in s_dict and s_dict[s[i]] == 1:
#             return i
        
#     return -1

# if __name__ == "__main__":
#     print(first_unique("leetcode"))
#     print(first_unique("loveleetcode"))
#     print(first_unique("aabb"))


###########################################################
## Problem 13: Valid Anagram
# Same frequencies.

# def is_anagram(s, t):
#     if len(s) != len(t):
#         return False

#     # dict1 = {}
#     # dict2 = {}

#     # for i in s:
#     #     dict1[i] = dict1.get(i, 0) + 1
    
#     # for i in t:
#     #     dict2[i] = dict2.get(i, 0) + 1
    
#     # for k, v in dict1.items():
#     #     if k not in dict2:
#     #         return False
#     #     if dict1[k] != dict2[k]:
#     #         return False

#     # return True
    

# # Instead of two dict, just used 1 dict and keep count track if present reduce count and if < 0 return false
#     count  = {}

#     for i in s:
#         count[i] = count.get(i, 0) + 1
    
#     for i in t:
#         if i not in count:
#             return False
#         count[i] -= 1
#         if count[i] < 0:
#             return False
#     return True

# if __name__ == "__main__":
#     print(is_anagram("anagram", "nagaram"))
#     print(is_anagram("rat", "car"))
#     print(is_anagram("listen", "silentt"))

###########################################################
## Problem 14: Ransom Note
# Check if you can construct ransom note from magazine letters (each letter used once).
# Can magazine form ransom?
# Hint: Frequency map.

# def can_construct(ransom, magazine):
#     dict1 = {}


#     for i in magazine:
#         dict1[i] = dict1.get(i, 0) + 1
    
#     for i in ransom:
#         if i not in dict1:
#             return False
#         dict1[i] -= 1
#         if dict1[i] < 0:
#             return False
    
#     return True

# if __name__ == "__main__":

#     print(can_construct("a", "b"))
#     print(can_construct("aa", "ab"))
#     print(can_construct("aa", "aab"))

###########################################################
# ## Problem 15: Find All Anagrams in String
# # Find all start indices of anagrams of p in s.
# # Sliding window.
# # Hint: Window frequency. - Use a frequency map and sliding window of size len(p).

# def find_anagrams(s, p):
#     count = {}

#     if len(s) < len(p):
#         return []
    
#     res = []
    
#     for i in p:
#         count[i] = count.get(i, 0) + 1
#     # a:1, b: 1, c: 1

#     left = 0
#     matches = 0
#     window = {}
#     req_match = len(p)
#     for right in range(len(s)):
#         char = s[right]
#         window[char] = window.get(char, 0) + 1

#         # check if current char count is equal to og string count
#         if char in count and window[char] == count[char]:
#             matches += 1

#         #let reduce window if > len(p)
#         if (right - left + 1) > len(p):
#             left_char = s[left]
#             #we need to shrink window by reducing left match and removing left
#             #1st check if present in og and reduce matches
#             if left_char in count and window[left_char] == count[left_char]:
#                 matches -=1 
#             #2nd reduce from windows dict and if 0 del it
#             window[left_char] -=1
#             if window[left_char] == 0:
#                 del window[left_char]
#             left += 1
        
#         #if matched, add starting index
#         if matches == req_match:
#             res.append(left)
#     return res
                 
# if __name__ == "__main__":
#     print(find_anagrams("cbaebabacd", "abc"))  # → [0, 6]
#     print(find_anagrams("abab", "ab"))         # → [0, 1, 2]

###########################################################
## Problem 16: Group Anagrams 
# Group strings that are anagrams of each other.
# **Hint:** Use sorted string (or character count tuple) as the key.

# def group_anagrams(words):
#     pass

# if __name__ == "__main__":
#     print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
#     # → [["bat"], ["nat","tan"], ["ate","eat","tea"]]
###########################################################
# ## Problem 17: Majority Element
# # Find the element that appears more than n/2 times. 

# def majority_element(nums):
    
#     # n = len(nums)

#     # count = {}
#     # for i in nums:
#     #     count[i] = count.get(i, 0) + 1
    
#     # for k, v in count.items():
#     #     if v > n//2:
#     #         return k
    
#     # return 0

#     candidate  = None
#     count = 0
#     for i in nums:

#         if count == 0:
#             candidate = i
#         count += 1 if i == candidate else -1 

#     return candidate
        
#         # if i == candidate:
#         #     count += 1
#         # else:
#         #     count -= 1
        
#         # if count == 0:
#         #     candidate = i
#         #     count += 1

# if __name__ == "__main__":
#     print(majority_element([3, 2, 3]))                 # → 3
#     print(majority_element([2, 2, 1, 1, 1, 2, 2]))    # → 2


###########################################################
### Problem 18: Find the Difference
# t has one extra char.

# def find_the_difference(s, t):
#     pass
# if __name__ == "__main__":
#     print(find_the_difference("abcd", "abcde"))  # → 'e'
#     print(find_the_difference("", "y"))          # → 'y'
#     print(find_the_difference("a", "aa"))        # → 'a'


###########################################################
### Problem 19: Intersection of Two Arrays II
# With duplicates.
# Hint: Count map.

# def intersect(nums1, nums2):
#     pass

# if __name__ == "__main__":
#     print(intersect([1, 2, 2, 1], [2, 2]))        # → [2, 2]
#     print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # → [4, 9]

###########################################################
### Problem 20: Roman to Integer
# Convert roman numerals.

# def roman_to_int(s):
#     pass

# if __name__ == "__main__":
#     print(roman_to_int("III"))       # → 3
#     print(roman_to_int("LVIII"))     # → 58
#     print(roman_to_int("MCMXCIV"))   # → 1994
###########################################################
### Problem 21: Top K Frequent Elements
# Bucket or heap.

# def top_k_frequent(nums, k):
#     pass

# if __name__ == "__main__":
#     print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # → [1, 2]
#     print(top_k_frequent([1], 1))                 # → [1]
#     print(top_k_frequent([1, 2], 2))              # → [1, 2]

###########################################################
### Problem 22: Sort Characters By Frequency
# Descending freq.

# def frequency_sort(s):
#     pass

# if __name__ == "__main__":
#     print(frequency_sort("tree"))      # → "eert" or "eetr"
#     print(frequency_sort("cccaaa"))    # → "aaaccc" or "cccaaa"
#     print(frequency_sort("Aabb"))      # → "bbAa" or "bbaA"
###########################################################
### Problem 23: Find Disappeared Numbers
# Range [1,n].

# def find_disappeared(nums):
#     pass

# if __name__ == "__main__":
#     print(find_disappeared([4, 3, 2, 7, 8, 2, 3, 1]))  # → [5, 6]
#     print(find_disappeared([1, 1]))                    # → [2]

###########################################################
### Problem 24: Find Duplicates
# Appear twice.

# def find_duplicates(nums):
#     pass

# if __name__ == "__main__":
#     print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # → [2, 3]
#     print(find_duplicates([1, 1, 2]))                 # → [1]
#     print(find_duplicates([1]))                       # → []

###########################################################
### Problem 25: Unique Number of Occurrences
# All counts unique.

# def unique_occurrences(nums):
#     pass

# if __name__ == "__main__":
#     print(unique_occurrences([1, 2, 2, 1, 1, 3]))               # → True
#     print(unique_occurrences([1, 2]))                            # → False
#     print(unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])) # → True


###########################################################
### Problem 26: Contains Duplicate II
# Same value within k distance.
# Hint: Map value -> last index.

# def contains_nearby_duplicate(nums, k):
#     pass

# if __name__ == "__main__":
#     print(contains_nearby_duplicate([1, 2, 3, 1], 3))      # → True
#     print(contains_nearby_duplicate([1, 0, 1, 1], 1))      # → True
#     print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)) # → False


###########################################################
### Problem 27: Shortest Word Distance
# Track last seen indices.

# def shortest_distance(words, w1, w2):
#     pass

# if __name__ == "__main__":
#     print(shortest_distance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")) # → 3
#     print(shortest_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))    # → 1

###########################################################
### Problem 28: Logger Rate Limiter
# Track last printed timestamp.

# class Logger:
#     def __init__(self):
#         pass
#
#     def should_print(self, timestamp, message):
#         pass



# if __name__ == "__main__":
#     logger = Logger()
#     print(logger.should_print(1, "foo"))   # → True
#     print(logger.should_print(2, "bar"))   # → True
#     print(logger.should_print(3, "foo"))   # → False
#     print(logger.should_print(8, "bar"))   # → False
#     print(logger.should_print(10, "foo"))  # → False
#     print(logger.should_print(11, "foo"))  # → True
###########################################################
### Problem 29: Find Common Characters
# Min frequency across words.

# def common_chars(words):
#     pass

# if __name__ == "__main__":
#     print(common_chars(["bella", "label", "roller"]))  # → ["e", "l", "l"]
#     print(common_chars(["cool", "lock", "cook"]))     # → ["c", "o"]


###########################################################
### Problem 30: N-Repeated Element in 2N Array
# One element repeated N times.
# Hint: Use set.

# def repeated_n_times(nums):
#     pass

# if __name__ == "__main__":
#     print(repeated_n_times([1, 2, 3, 3]))               # → 3
#     print(repeated_n_times([2, 1, 2, 5, 3, 2]))         # → 2
#     print(repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]))   # → 5
###########################################################
