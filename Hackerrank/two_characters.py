# Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters.

# Example
# Delete a, to leave bcdbd. Now, remove the character c to leave the valid string bdbd with a length of 4. Removing either b or d at any point would not result in a valid string. Return .
# Given a string , convert it to the longest possible string  made up only of alternating characters. Return the length of string . If no string  can be formed, return .
# Function Description
# Complete the alternate function in the editor below.
# alternate has the following parameter(s):
# string s: a string
# Returns.
# int: the length of the longest valid string, or  if there are none
# Input Format
# The first line contains a single integer that denotes the length of .
# The second line contains string .

# Constraints
# Sample Input
# STDIN       Function
# -----       --------
# 10          length of s = 10
# beabeefeab  s = 'beabeefeab'
# Sample Output
# 5
# Explanation
# The characters present in  are a, b, e, and f. This means that  must consist of two of those characters and we must delete two others. Our choices for characters to leave are [a,b], [a,e], [a, f], [b, e], [b, f] and [e, f].
# If we delete e and f, the resulting string is babab. This is a valid  as there are only two distinct characters (a and b), and they are alternating within the string.
# If we delete a and f, the resulting string is bebeeeb. This is not a valid string  because there are consecutive e's present. Removing them would leave consecutive b's, so this fails to produce a valid string .
# Other cases are solved similarly.
# babab is the longest string we can create.

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def isalternating(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True
    
def alternate(s):
    # Write your code here
    unique_char = set(s)
    max_length = 0
    
    for i in unique_char:
        for j in unique_char:
            if i != j:
                filtered_char = [c for c in s if c == i or c == j]
                if isalternating(filtered_char):
                    max_length = max(max_length, len(filtered_char))
    return max_length

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     l = int(input().strip())
#     s = input()
#     result = alternate(s)
#     fptr.write(str(result) + '\n')
#     fptr.close()

if __name__ == '__main__':
    l = int(input("Enter length of string: ").strip())
    s = input("Enter string: ")
    result = alternate(s)
    print("Maximum alternating length:", result)
