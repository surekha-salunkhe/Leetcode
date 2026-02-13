# ulius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
# Example
# The alphabet is rotated by , matching the mapping above. The encrypted string is .
# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
# Function Description
# Complete the caesarCipher function in the editor below.
# caesarCipher has the following parameter(s):
# string s: cleartext
# int k: the alphabet rotation factor
# Returns
# string: the encrypted string
# Input Format
# The first line contains the integer, , the length of the unencrypted string.
# The second line contains the unencrypted string, .
# The third line contains , the number of letters to rotate the alphabet by.

# Constraints
#  is a valid ASCII string without any spaces.
# Sample Input
# 11
# middle-Outz
# 2
# Sample Output
# okffng-Qwvb
# Explanation
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab
# m -> o
# i -> k
# d -> f
# d -> f
# l -> n
# e -> g
# -    -
# O -> Q
# u -> w
# t -> v
# z -> b
# ------------------------------------------------------------------------------------------------------------------------------------------------
# #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    result = ""
    k = k % 26
    for char in s:
        if char.islower():
            result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            result += char
    return result

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(input().strip())
#     s = input()
#     k = int(input().strip())
#     result = caesarCipher(s, k)
#     fptr.write(result + '\n')
#     fptr.close()

if __name__ == '__main__':
    n = int(input("Enter length of string: ").strip())
    s = input("Enter string: ")
    k = int(input("Enter rotation key: ").strip())
    result = caesarCipher(s, k)
    print("Ciphered string:", result)