# Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

# Its length is at least .
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@#$%^&*()-+
# She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

# Note: Here's the set of types of characters in a form you can paste in your solution:

# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"

# Example
# This password is 5 characters long and is missing an uppercase and a special character. The minimum number of characters to add is .
# This password is 5 characters long and has at least one of each character type. The minimum number of characters to add is .
# Function Description
# Complete the minimumNumber function in the editor below.
# minimumNumber has the following parameters:
# int n: the length of the password
# string password: the password to test

# Returns
# int: the minimum number of characters to add
# Input Format
# The first line contains an integer , the length of the password.
# The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

# Constraints
# All characters in  are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ].
# Sample Input 0
# 3
# Ab1
# Sample Output 0
# 3
# Explanation 0
# She can make the password strong by adding  characters, for example, $hk, turning the password into Ab1$hk which is strong.
#  characters aren't enough since the length must be at least .

# Sample Input 1
# 11
# #HackerRank
# Sample Output 1
# 1
# Explanation 1
# The password isn't strong, but she can make it strong by adding a single digit.
# --------------------------------------------------------------------------------------------------------------------------------------
# #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # numbers = "0123456789"
    # lower_case = "abcdefghijklmnopqrstuvwxyz"
    # upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # special_characters = "!@#$%^&*()-+"
    
    # count = 0
    # if not any(char in numbers for char in password):
    #     count += 1
    # if not any(char in lower_case for char in password):
    #     count += 1
    # if not any(char in upper_case for char in password):
    #     count += 1
    # if not any(char in special_characters for char in password):
    #     count += 1
        
    # return max(count, 6 - n)
  
    digit_check = re.search(r'\d', password)
    lower_check = re.search(r'[a-z]', password)
    upper_check = re.search(r'[A-Z]', password)
    special_check = re.search(r'[!@#$%^&*()\-\+]', password)

    count = 0
    if not digit_check:
        count += 1
    if not lower_check:
        count += 1
    if not upper_check:
        count += 1
    if not special_check:
        count += 1
    return max(count, 6 - n)
        
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(input().strip())
#     password = input()
#     answer = minimumNumber(n, password)
#     fptr.write(str(answer) + '\n')
#     fptr.close()

if __name__ == '__main__':
    n = int(input("Enter password length: ").strip())
    password = input("Enter password: ")
    answer = minimumNumber(n, password)
    print("Minimum characters to add:", answer)
