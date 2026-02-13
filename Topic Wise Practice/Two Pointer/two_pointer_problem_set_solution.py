# Two Pointers Practice Solutions
## Part 1: Opposite Ends [1-9]
## Part 2: Same Direction (Slow/Fast) [10-19]
## Part 3: Two Arrays [20-24]
## Part 4: Challenge Problems [25-30]


# PART 1: Opposite Ends #####################################

###########################################################
# ## Problem 1: Two Sum (Sorted Array)
# # Given a sorted array and a target sum, find two numbers that add up to the target.
# # Return their indices (1-indexed).

# def two_sum(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         sum_n = nums[left] + nums[right]

#         if sum_n == target:
#             return [left + 1, right + 1] 
#         elif sum_n < target:
#             left += 1
#         else:
#             right -= 1

#     return []

# if __name__ == "__main__":
#     print(two_sum([2, 7, 11, 15], 9))
#     print(two_sum([2, 3, 4], 6))
#     print(two_sum([-1, 0, 2, 3], 2))

# # Hint: If arr[left] + arr[right] < target, move left right. If sum is too big, move right left.

###########################################################
# ## Problem 2: Valid Palindrome
# # Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.

# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1

#     if len(s) == 0:
#         return True
    
#     # ignoring case -> remove lower 
    
#     # s = ''.join(i.lower() for i in s if i.isalnum())

#     # while left < right:
#     #     if s[left] != s[right]:
#     #         return False
        
#     #     left += 1
#     #     right -= 1
#     # return True

#     # O(n) time and O(n) space as new string created
   
#     while left < right:
#         while left < right and not s[left].isalnum():
#             left +=1 
#         while left < right and not s[right].isalnum():
#             right -= 1
        
#         if s[left].lower() != s[right].lower():
#             return False
        
#         left += 1
#         right -=1 
#     return True

# if __name__ == "__main__":
#     print(is_palindrome("A man, a plan, a canal: Panama"))
#     print(is_palindrome("race a car"))
#     print(is_palindrome(" "))

# # Hint: Use two pointers from opposite ends, skip non-alphanumeric characters.

###########################################################
# ## Problem 3: Reverse String In-Place
# # Reverse an array of characters in-place (no extra array).

# def reverse(s):
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         temp = s[left]
#         s[left] = s[right]
#         s[right] = temp

#         left += 1
#         right -= 1
#     return s

# if __name__ == "__main__":
#     print(reverse(['h','e','l','l','o']))
#     print(reverse(['a','b']))

# # Hint: Swap elements from opposite ends, moving toward the middle.

###########################################################
# ## Problem 4: Reverse Words in a String (In-Place)
# # Given a character array representing a sentence, reverse the order of words in-place.

# # I did part 1 then I wrote the logic for 2nd and got stuck when I had to create a helper function to reverse each word

# def reverse_words(word):

#     def reverse_array(arr, left, right):
#         while left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1

#     n = len(word)
#     reverse_array(word, 0, n - 1)
    
#     l = 0
#     for i in range(n + 1):
#         if i == n or word[i] == ' ':
#             reverse_array(word, l, i - 1)
#             l = i + 1
#     return word

# if __name__ == "__main__":
#     print(reverse_words(['t','h','e',' ','s','k','y',' ','i','s',' ','b','l','u','e']))

# # Hint: Reverse the entire array first, then reverse each word individually.

###########################################################
# ## Problem 5: Container With Most Water
# # Given an array of heights, find two lines that together with the x-axis form a container 
# # holding the most water.

# def max_water(arr):
#     left = 0
#     right = len(arr) - 1
#     max_area = 0

#     while left < right:
#         #area = height * width
#         #here I would consider min since that's the height the container would hold
#         height = min(arr[left], arr[right])
#         area = height * (right - left)
#         max_area = max(max_area, area)

#         if arr[left] < arr[right]:
#             left += 1
#         else:
#             right -= 1
            
#     return max_area

# if __name__ == "__main__":
#     print(max_water([1,8,6,2,5,4,8,3,7]))
#     print(max_water([1,1]))
#     print(max_water([4,3,2,1,4]))

# # Hint: Start with widest container. Move the pointer with the shorter height inward.

###########################################################
# ## Problem 6: Three Sum
# # Given an array, find all unique triplets that sum to zero.

# def three_sum(nums):
#     nums.sort()
#     res = []

#     n = len(nums)

#     for i in range(n):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#         left = i + 1
#         right = n - 1

#         while left < right:
#             total = nums[i] + nums[left] + nums[right]

#             if total == 0:
#                 res.append([nums[i], nums[left], nums[right]])
#                 left += 1
#                 right -= 1

#                 while left < right and nums[left] == nums[left - 1]:
#                     left += 1

#                 while left < right and nums[right] == nums[right + 1]:
#                     right -= 1

#             elif total < 0:
#                 left += 1
#             else:
#                 right -= 1
#     return res

# if __name__ == "__main__":
#     print(three_sum([-1, 0, 1, 2, -1, -4]))
#     print(three_sum([0, 1, 1]))
#     print(three_sum([0, 0, 0]))

# #Thinking process: 
# # Step 1: What is being asked?
# # Return 3 numbers
# # Their sum = 0
# # Triplets must be unique
# # Order inside a triplet doesn’t matter
# # Step 2: Brute force i, j, k (O(n^3))
# # Step 3: Sorting? Fix one, two pointer
# # Step 4: total == 0 record,
# # total < 0 (need bigger, move left), 
# # total > 0 (need smaller, move right)
# # Step 5: Uniqueness (no duplicate),
# # same[arr] i > 0 then curr and last if equal continue
# # same[left] after record, check left curr and past, move left
# # same[right] after record, check right and next right, move right

# # Hint: Sort first. Fix one element, use two pointers on remaining elements. 
# # Skip duplicates carefully.

###########################################################
# ## Problem 7: Three Sum Closest
# # Given an array and a target, find three numbers whose sum is closest to the target. 
# # Return the sum.

# def three_sum_closest(nums, target):
#     nums.sort()
#     n = len(nums)
#     closest_sum = nums[0] +  nums[1] + nums[2]
#     for i in range(n-2):
#         left = i+1
#         right = n - 1
#         while left < right:
#             current_sum = nums[i] + nums[left] + nums[right]
#             if abs(current_sum - target) < abs(closest_sum - target):
#                 closest_sum = current_sum
#             if current_sum < target:
#                 left += 1
#             elif current_sum > target:
#                 right -= 1
#             else:
#                 return current_sum
#     return closest_sum

# if __name__ == "__main__":
#     print(three_sum_closest([-1, 2, 1, -4], 1))
#     print(three_sum_closest([0, 0, 0], 1))

# # Thinking
# # Step 1: output, pick 3 numbers, sum closest to target, return sum (not triplet) only best answer needed
# # Step 2: Brute force: i, j, k, keep track of min diff (O(n^3))
# # Step 3: sort, fix one, two pointer
# # Step 4: Keep track of closest sum = 0, 1, 2, left and right
# # Step 5: while, current_sum = i + left = right
# # Step 6: if abs (curr-target) < abs (clos - target)
# # Step 7: If current_sum < target, (need bigger sum), move left.
# # If current_sum > target, (need smaller sum), move right.
# # If current_sum == target , perfect → return curr_sum.

# # Hint: Similar to Three Sum, but track the closest sum found so far using absolute difference.

###########################################################
# ## Problem 8: Four Sum
# # Given an array and a target, find all unique quadruplets that sum to the target.

# def four_sum(nums, target):
#     # -2, -1, 0, 0, 1, 2    -2,-1,1,2   -2,0,0,2  -1,0,0,1
#     nums.sort()
#     n = len(nums)
#     res = []

#     for i in range(n-3):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue

#         for j in range(i+1, n - 2):
#             if j > i+1 and nums[j] == nums[j-1]:
#                 continue
            
#             left = j + 1
#             right = n - 1

#             while left < right:
#                 sum_total = nums[i] + nums[j] + nums[left] + nums[right]

#                 if sum_total == target:
#                     res.append([nums[i], nums[j], nums[left], nums[right]])

#                     left += 1
#                     right -= 1

#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1
#                 elif sum_total < target:
#                     left += 1
#                 else:
#                     right -=1
#     return res


# if __name__ == "__main__":
#     print(four_sum([1, 0, -1, 0, -2, 2], 0))
#     print(four_sum([2, 2, 2, 2, 2], 8))

# # Hint: Similar to Three Sum, but fix two elements instead of one. 
# # Sort first, use nested loops with two pointers for the last two elements.

###########################################################
# ## Problem 9: Trapping Rain Water
# # Given an array of heights representing an elevation map, compute how much water can be 
# # trapped after rain.


# def trap(height):

#     n = len(height)
#     left = 0
#     right = n - 1

#     left_max = 0
#     right_max = 0

#     total_water = 0

#     while left < right:
#         if height[left] < height[right]:
#             left_max = max(left_max, height[left])
#             total_water += left_max - height[left]
#             left += 1
#         else:
#             right_max = max(right_max, height[right])
#             total_water += right_max - height[right]
#             right -= 1
    
#     return total_water

# if __name__ == "__main__":
#     print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
#     print(trap([4,2,0,3,2,5]))
    
# # Hint: Water at position i = min(max_left, max_right) - height[i]. 
# # Use two pointers to track max heights from both sides in one pass.
###########################################################

## PART 2: Same Direction (Slow/Fast) ####################

###########################################################
# ## Problem 10: Remove Duplicates from Sorted Array
# # Remove duplicates in-place from a sorted array. Return the new length.
# # Hint: slow marks where to write next unique element. fast scans ahead.

# def remove_duplicates(nums):
#     if not nums:
#         return 0 
    
#     n = len(nums)
#     slow = 1 #acts as count

#     for fast in range(1, n):
#         if nums[fast] != nums[fast - 1]:
#             nums[slow] = nums[fast]
#             slow += 1
        
#     return slow

# if __name__ == "__main__":
#     print(remove_duplicates([1,1,2]))
#     print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))

###########################################################
# ## Problem 11: Remove Duplicates II (Allow Two)
# # Same as above, but each element may appear at most twice.
# # Hint: Check if current element equals the element two positions back in the result.

# def remove_duplicates_ii(nums):
#     n = len(nums)
#     if n <=2:
#         return n

#     slow = 2

#     for fast in range(2, n):
#         if nums[fast] != nums[slow - 2]:
#             nums[slow] = nums[fast]
#             slow += 1
        
#     return slow

# if __name__ == "__main__":
#     print(remove_duplicates_ii([1,1,1,2,2,3]))
#     print(remove_duplicates_ii([0,0,1,1,1,1,2,3,3]))

###########################################################
# ## Problem 12: Move Zeroes
# # Move all zeroes to the end while maintaining relative order of non-zero elements. 
# # Do it in-place.
# # Hint: Use slow pointer to track where to place next non-zero. Swap with fast pointer.

# def move_zeroes(nums):

#     n = len(nums)

#     slow = 0

#     for fast in range(n):
#         if nums[fast]!= 0:
#             nums[slow], nums[fast] = nums[fast], nums[slow]
#             slow += 1
    
#     return nums
    

# if __name__ == "__main__":
#     print(move_zeroes([0,1,0,3,12]))
#     print(move_zeroes([0]))
#     print(move_zeroes([1,2,0,3,0,5]))

###########################################################
# ## Problem 13: Remove Element
# # Remove all occurrences of a value in-place. Return the new length.
# # Hint: Similar to move zeroes, but remove specific value instead.

# def remove_element(nums, val):
#     n = len(nums)

#     slow = 0

#     for fast in range(n):
#         if nums[fast] != val:
#             nums[slow], nums[fast] = nums[fast], nums[slow]
#             slow += 1
        
#     return slow

# if __name__ == "__main__":
#     print(remove_element([3,2,2,3], 3))
#     print(remove_element([0,1,2,2,3,0,4,2], 2))

###########################################################
# ## Problem 14: Sort Colors (Dutch National Flag)
# # Sort an array containing only 0s, 1s, and 2s in-place. One pass, constant space.
# # Hint: Use three pointers - low, mid, high. Elements before low are 0s, after high are 2s.
# # [0 ... low-1]     → all 0s
# # [low ... mid-1]   → all 1s
# # [mid ... high]    → unknown
# # [high+1 ... end]  → all 2s
# def sort_colors(nums):
#     n = len(nums)
#     low = mid = 0
#     high = n - 1
    
#     while mid <= high:
#         if nums[mid] == 0:
#             nums[low], nums[mid] = nums[mid], nums[low]
#             low += 1
#             mid += 1
#         elif nums[mid] == 1:
#             mid += 1
#         else:
#             nums[high], nums[mid] = nums[mid], nums[high]
#             high -= 1 
#     return nums

# if __name__ == "__main__":
#     print(sort_colors([2,0,2,1,1,0]))
#     print(sort_colors([2,0,1]))

###########################################################
# ## Problem 15: Partition Array
# # Rearrange array so all elements less than pivot come before elements >= pivot.
# # Return the index of the first element >= pivot.
# # Hint: Similar to quicksort partition. Use slow pointer for boundary, fast to scan.

# def partition(nums, pivot):
#     n = len(nums)
#     slow = 0

#     for fast in range(n):
#         if nums[fast] < pivot:
#             nums[slow], nums[fast] = nums[fast], nums[slow]
#             slow += 1

#     return slow 

# if __name__ == "__main__":
#     print(partition([3, 1, 4, 1, 5, 9, 2, 6], 5))

###########################################################
# ## Problem 16: Linked List Cycle
# # Determine if a linked list has a cycle.
# # Hint: Floyd's cycle detection - fast pointer moves 2 steps, slow moves 1. 
# # If they meet, there's a cycle.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def has_cycle(head):

#     if not head:
#         return False
    
#     slow = head
#     fast = head
    
#     while fast and fast.next:

#         slow = slow.next
#         fast = fast.next.next 

#         if slow == fast:
#             return True

#     return False

# if __name__ == "__main__":
#     # Test case 1: 3 -> 2 -> 0 -> -4 (back to 2)
#     head = ListNode(3)
#     node2 = ListNode(2)
#     node3 = ListNode(0)
#     node4 = ListNode(-4)
#     head.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node2
#     print(has_cycle(head))  # True
    
#     # Test case 2: 1 -> 2 -> None
#     head2 = ListNode(1, ListNode(2))
#     print(has_cycle(head2))  # False

###########################################################
# ## Problem 17: Linked List Cycle II
# # If a linked list has a cycle, return the node where the cycle begins. 
# # If no cycle, return null.
# # Hint: After fast and slow meet, reset one pointer to head. 
# # Move both at same speed - they meet at cycle start.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def detect_cycle(head):
#     if not head:
#         return None
    
#     slow = fast = head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             slow = head
#             while slow != fast:
#                 slow = slow.next
#                 fast = fast.next
#             return slow
#     return None

# if __name__ == "__main__":
#     # Test case: 3 -> 2 -> 0 -> -4 (back to 2)
#     head = ListNode(3)
#     node2 = ListNode(2)
#     node3 = ListNode(0)
#     node4 = ListNode(-4)
#     head.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node2
#     result = detect_cycle(head)
#     print(result.val if result else None)  # 2
###########################################################
# ## Problem 18: Find the Middle of a Linked List
# # Return the middle node. If two middle nodes, return the second one.
# # Hint: Slow moves 1 step, fast moves 2 steps. When fast reaches end, slow is at middle.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def middle_node(head):
    
#     if not head:
#         return None
    
#     slow = fast = head

#     while fast and fast.next:

#         slow = slow.next
#         fast = fast.next.next

#     return slow

# if __name__ == "__main__":
#     # Test case 1: 1 -> 2 -> 3 -> 4 -> 5
#     head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#     result = middle_node(head)
#     print(result.val)  # 3
    
#     # Test case 2: 1 -> 2 -> 3 -> 4 -> 5 -> 6
#     head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
#     result2 = middle_node(head2)
#     print(result2.val)  # 4
    

# ###########################################################
# ## Problem 19: Remove Nth Node From End
# # Remove the nth node from the end of a linked list in one pass.
# # Hint: Advance fast by n steps first, then move both until fast reaches the end.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def remove_nth_from_end(head, n):
#     if not head:
#         return None
    
#     dummy = ListNode(0, head) # create a copy for removal to handle edge cases
#     slow = fast = dummy

#     for _ in range(n + 1):
#         fast = fast.next
    
#     while fast:
#         slow = slow.next
#         fast = fast.next
    
#     slow.next = slow.next.next # to remove

#     return dummy.next

# if __name__ == "__main__":
#     # Test case 1: 1 -> 2 -> 3 -> 4 -> 5, n=2
#     head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#     result = remove_nth_from_end(head, 2)
#     # Print result
#     curr = result
#     while curr:
#         print(curr.val, end=" -> " if curr.next else "")
#         curr = curr.next
#     print()  # Output: 1 -> 2 -> 3 -> 5

#     # Test case 2: 1 -> 2, n=1
#     head2 = ListNode(1, ListNode(2))
#     result2 = remove_nth_from_end(head2, 1)
#     curr = result2
#     while curr:
#         print(curr.val, end=" -> " if curr.next else "")
#         curr = curr.next
#     print()  # Output: 1
#     print(result)
#     # Output: 1 -> 2 -> 3 -> 5

###########################################################
## PART 3: Two Arrays #####################################

###########################################################
# ## Problem 20: Merge Sorted Arrays
# # Merge two sorted arrays into the first array (which has enough space).
# # Hint: Fill from the end to avoid overwriting elements. Compare from back to front.

# def merge(nums1, m, nums2, n):
    
#     p1 = m - 1
#     p2 = n - 1
#     p = m + n -1

#     while p1 >=0 and p2 >=0:
#         if nums1[p1] > nums2[p2]:
#             nums1[p] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#         p -= 1

#     while p2 >=0:
#         nums1[p] = nums2[p2]
#         p2 -=1 
#         p -=1 
#     return nums1

# if __name__ == "__main__":
#     nums1 = [1, 2, 3, 0, 0, 0]
#     nums2 = [2, 5, 6]
#     merge(nums1, 3, nums2, 3)
#     print(nums1)

###########################################################
# ## Problem 21: Intersection of Two Sorted Arrays
# # Return the intersection of two sorted arrays. Each element appears as many times as 
# # it shows in both arrays.
# # Hint: Two pointers, one for each array. When elements match, add to result.

# def intersect(nums1, nums2):
    
#     n = len(nums1)
#     m = len(nums2)
#     left = right = 0
#     res = []
#     while left < n and right < m:
#         if nums1[left] == nums2[right]:
#             res.append(nums1[left])
#             left += 1
#             right += 1
#         elif nums1[left] < nums2[right]:
#             left += 1
#         else:
#             right += 1
        
#     return res


# if __name__ == "__main__":
#     print(intersect([1,1,2,2], [2,2]))
#     print(intersect([4,5,9], [4,4,8,9,9]))

###########################################################
# ## Problem 22: Is Subsequence
# # Check if string s is a subsequence of string t.
# # Hint: Use pointer for s and t. Advance t always, advance s only when characters match.

# def is_subsequence(s, t):
    
#     left = 0 
#     right = 0

#     while left < len(s) and right < len(t):
#         if s[left] == t[right]:
#             left += 1
#         right += 1
    
#     if left == len(s):
#         return True
#     else:
#         return False

# if __name__ == "__main__":
#     print(is_subsequence("abc", "ahbgdc"))
#     print(is_subsequence("axc", "ahbgdc"))
#     print(is_subsequence("", "ahbgdc"))

###########################################################
# ## Problem 23: Compare Version Numbers
# # Compare two version strings. Return -1 if v1 < v2, 1 if v1 > v2, 0 if equal.
# # Hint: Split by '.', use two pointers to compare each part. Handle trailing zeros.

# def compare_version(version1, version2):
#     v1 = [int(i) for i in version1.split('.')]
#     v2 = [int(i) for i in version2.split('.')]

#     # print(v1, v2)
#     n = max(len(v1), len(v2))
#     for i in range(n): #0, 1, 2
#         num1 = v1[i] if i < len(v1) else 0
#         num2 = v2[i] if i < len(v2) else 0

#         if num1 > num2:
#             return 1
#         elif num1 < num2:
#             return -1
    
#     return 0


# if __name__ == "__main__":
#     print(compare_version("1.01", "1.001"))
#     print(compare_version("1.0", "1.0.0"))
#     print(compare_version("0.1", "1.1"))
#     print(compare_version("1.0.1", "1"))

###########################################################
## Problem 24: Backspace String Compare
# Given two strings with '#' representing backspace, check if they're equal after processing.
# Hint: Traverse from the end. Count backspaces and skip characters accordingly. O(1) space.

#Thinking 
# Naive idea (discard quickly)
# Build final strings using stacks.
# Compare them.
# Works, but uses extra space.
# Interviewer hint says: O(1) space → think pointers, not stacks.

#Scan from end, as backspace will delete before it
#Skip char easily from back
#Two pointers i for s, j for t
#skip_s, skip_t, no. of char to skip due to #
#move left: if # increase skip count, if skip > 0 -> skip that char, else stop real char
#compare: if both valid char - must match
#if one ends before other - not equal
#continue until both strings done

# “Backspace removes before → walk from end → count '#' → skip chars → compare.”

def backspace_compare(s, t):
    i, j = len(s) - 1, len(t) - 1

    while i >= 0 or j >= 0:
        # Find next valid character in s
        skip_s = 0
        while i >= 0:
            if s[i] == '#':
                skip_s += 1
                i -= 1
            elif skip_s > 0:
                skip_s -= 1
                i -= 1
            else:
                break

        # Find next valid character in t
        skip_t = 0
        while j >= 0:
            if t[j] == '#':
                skip_t += 1
                j -= 1
            elif skip_t > 0:
                skip_t -= 1
                j -= 1
            else:
                break

        # Compare characters
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        # If one string is finished but the other is not
        if (i >= 0) != (j >= 0):
            return False

        i -= 1
        j -= 1

    return True

if __name__ == "__main__":
    print(backspace_compare("ab#c", "ad#c"))
    print(backspace_compare("ab##", "c#d#"))
    print(backspace_compare("a#c", "b"))

###########################################################
## PART 4: Challenge Problems #############################

###########################################################
### Problem 25: Sort Array By Parity
# Rearrange so all even numbers come before all odd numbers.
# Hint: Two pointers from opposite ends. Swap when left is odd and right is even.

# def sort_by_parity(nums):
#     pass

# if __name__ == "__main__":
#     print(sort_by_parity([3,1,2,4]))

###########################################################
### Problem 26: Squares of a Sorted Array
# Given a sorted array (may have negatives), return array of squares in sorted order.
# Hint: Largest square is either at left end (large negative) or right end (large positive).
# Use two pointers and fill result from the end.

# def sorted_squares(nums):
#     pass

# if __name__ == "__main__":
#     print(sorted_squares([-4,-1,0,3,10]))
#     print(sorted_squares([-7,-3,2,3,11]))

###########################################################
### Problem 27: Longest Mountain in Array
# Find the length of the longest mountain subarray (strictly increasing then strictly 
# decreasing, at least 3 elements).
# Hint: For each potential peak, expand left and right while maintaining the pattern.

# def longest_mountain(arr):
#     pass

# if __name__ == "__main__":
#     print(longest_mountain([2,1,4,7,3,2,5]))
#     print(longest_mountain([2,2,2]))

###########################################################
### Problem 28: Boats to Save People
# People with given weights, boats with weight limit. Each boat carries at most 2 people.
# Find minimum boats needed.
# Hint: Sort first. Try to pair lightest with heaviest using two pointers.

# def num_boats(people, limit):
#     pass

# if __name__ == "__main__":
#     print(num_boats([1,2], 3))
#     print(num_boats([3,2,2,1], 3))
#     print(num_boats([3,5,3,4], 5))

###########################################################
### Problem 29: Minimize Maximum Pair Sum
# Pair up all elements in an even-length array. Minimize the maximum pair sum.
# Hint: Sort array. Pair smallest with largest, second smallest with second largest, etc.

# def min_max_pair_sum(nums):
#     pass

# if __name__ == "__main__":
#     print(min_max_pair_sum([3,5,2,3]))
#     print(min_max_pair_sum([3,5,4,2,4,6]))

###########################################################
### Problem 30: Valid Triangle Number
# Count triplets that can form a valid triangle (sum of any two sides > third side).
# Hint: Sort first. For each c (largest side), use two pointers for a and b. 
# Only need to check a + b > c when sorted.

# def triangle_number(nums):
#     pass

# if __name__ == "__main__":
#     print(triangle_number([2,2,3,4]))
#     print(triangle_number([4,2,3,4]))

###########################################################
