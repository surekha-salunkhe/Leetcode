
## Part 1: Fixed-Size Window [1-9]
## Part 2: Variable-Size Window (Shrink to Valid) [10-16]
## Part 3: Variable-Size Window (Expand to Valid) [17-19]
## Part 4: String-Specific Problems [20-24]
## Part 5: Challenge Problems [25-30]



# # Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above. We will now formally solve it.
# # def sw(nums, k):
# #     curr = 0
# #     res = 0
# #     left = 0
    
# #     for right in range(len(nums)):
# #         curr += nums[right]
# #         while curr > k:
# #             curr -= nums[left]
# #             left += 1
# #         res = max(res, right - left + 1)
# #     return res

# # Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

# # def sw(str):
# #     count_zero = 0
# #     left = 0
# #     res = 0
    
# #     for right in range(len(str)):
# #         if str[right] == '0':
# #             count_zero += 1
# #         while count_zero > 1:
# #             if str[left] == '0':
# #                 count_zero -= 1
# #             left += 1
# #         res = max(res,right - left+ 1)
# #     return res


# # Example 3: 713. Subarray Product Less Than K.
# # Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

# # def sw(nums, k):
# #     if k <= 1:
# #         return 0
    
# #     res = left = 0
# #     curr = 1
# #     for right in range(len(nums)):
# #         curr *= nums[right]
# #         while curr >= k:
# #             curr //= nums[left]
# #             left += 1
# #         res += (right - left + 1)
# #     return res

# # Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

# def sw(nums, k):
#     curr = 0
    
#     for i in range(k): # sum of 1st k elements
#         curr += nums[i]
    
#     res = curr
#     for i in range(k, len(nums)):
#         curr += nums[i] - nums[i - k] #add next, remove prev
#         res = max(res, curr)
#     return res
    
# if __name__ == "__main__":

#     # print(sw([3, 1, 2, 7, 4, 2, 1, 1, 5],8))
#     # print(sw("1101100111"))
#     # print(sw([10, 5, 2, 6],100))
#     print(sw([3, -1, 4, 12, -8, 5, 6], 4))
    
#########################################################################
### Problem 5: Maximum Number of Vowels in a Substring

# Find the maximum number of vowels in any substring of length k.

# ```
# max_vowels("abciiidef", 3) → 3              # "iii"
# max_vowels("aeiou", 2) → 2
# max_vowels("leetcode", 3) → 2               # "lee" or "eet"
# max_vowels("rhythms", 4) → 0
# ```


# def my_func(s, k):
#     vowels = {'a', 'e', 'i', 'o', 'u'}

#     left = max_count  = 0
#     count_vowels = 0

#     for right in range(len(s)):
#         if s[right] in vowels:
#             count_vowels += 1

#         if right -left + 1 > k:
#             if s[left] in vowels:
#                 count_vowels -=1
#             left += 1
        
#         if right - left + 1 == k:
#             max_count = max(max_count, count_vowels)
#     return max_count

# def main():
#     ans = my_func("leetcode", 3)
#     print(ans)
#     return 0

# if __name__ == "__main__":
#     main()
##########################################################################
### Problem 6: Minimum Difference Between Highest and Lowest of K Scores

# Given an array of scores, choose any k scores and minimize the difference between the highest and lowest.

# ```
# min_difference([90], 1) → 0
# min_difference([9, 4, 1, 7], 2) → 2         # Choose [7, 9], diff = 2
# min_difference([87063,61094,44530,21297,95857,93551,9918], 6) → 74560
# ```

# **Hint:** Sort first, then use fixed-size window.


def my_func(arr, k):
    if len(arr) == 1:
        return 0
    
    arr.sort()

    # 1, 4, 7, 9

    left = min_diff = 0

    for right in range(1,len(arr),k):
        print(right)


def main():
    arr = [9, 4, 1, 7]
    ans = my_func(arr, 2)
    print(ans)
    return 0

if __name__ == "__main__":
    main()

    
    
    
    
