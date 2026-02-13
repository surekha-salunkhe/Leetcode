# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
# Example
# The string contains all letters in the English alphabet, so return pangram.
# Function Description
# Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.
# pangrams has the following parameter(s):
# string s: a string to test
# Returns
# string: either pangram or not pangram
# Input Format
# A single line with string .

# Constraints
# Each character of , 
# Sample Input
# Sample Input 0
# We promptly judged antique ivory buckles for the next prize
# Sample Output 0
# pangram
# Sample Explanation 0
# All of the letters of the alphabet are present in the string.

# Sample Input 1
# We promptly judged antique ivory buckles for the prize
# Sample Output 1
# not pangram
# Sample Explanation 0
# The string lacks an x.
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# #!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    a = set(s.lower())
    # b = set(string.ascii_lowercase)
    b = set('abcdefghijklmnopqrstuvwxyz')
    
    # if b.issubset(a):
    #     return 'pangram'
    # else:
    #     return 'not pangram'
    for i in a:
        if i in b:
            b.remove(i)
        if not b:
            return 'pangram'
    return 'not pangram'

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = input()
#     result = pangrams(s)
#     fptr.write(result + '\n')
#     fptr.close()

if __name__ == '__main__':
    s = input("Enter string: ")
    result = pangrams(s)
    print(result)
