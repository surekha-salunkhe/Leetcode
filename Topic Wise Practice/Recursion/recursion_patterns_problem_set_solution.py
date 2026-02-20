## Part 1: Basic Printing

# ### Problem 1: Print 1 to N
# # Write a recursive function that prints numbers from 1 to n, each on a new line.
# ```
# print_ascending(5)
# ```
# **Output:**
# ```
# 1
# 2
# 3
# 4
# 5
# ```
# def recur(n):
#     if n == 0:
#         return
    
#     recur(n - 1)
#     print(n)

# recur(5)
#########################################################
# ### Problem 2: Print N to 1
# #Write a recursive function that prints numbers from n down to 1.
# ```
# print_descending(5)
# ```
# **Output:**
# ```
# 5
# 4
# 3
# 2
# 1
# ```

# **Think about it:** 
# What's the only difference between this and Problem 1 in terms of where the print statement goes?

# def my_func(n):
#     if n == 0:
#         return
#     print(n)
#     my_func(n-1)

# def main():
#     my_func(5)

# if __name__ == "__main__":
#     main()
#####################################################
# ### Problem 3: Print 1 to N to 1

# Write a recursive function that prints 1 to n, then n down to 1. You should print **each number twice** (once going up, once coming down).

# ```
# print_mountain(4)
# ```
# **Output:**
# ```
# 1
# 2
# 3
# 4
# 4
# 3
# 2
# 1
# def my_func(n, current=1):
#     if n == 0:
#         return    
#     if current > n:
#         return
    
#     print(current)           
#     my_func(n, current + 1)
#     print(current) 
    
# def main():
#     my_func(4)
    
# if __name__ == "__main__":
#     main()
#########################################################
# ### Problem 4: Print 1 to N to 1 (Single Peak)

# Same as Problem 3, but print n only **once** (the peak appears just once).

# ```
# print_mountain_single_peak(4)
# ```
# **Output:**
# ```
# 1
# 2
# 3
# 4
# 3
# 2
# 1
# ```
# ---

# def my_func(n,current = 1):
#     if n == 0:
#         return
    
#     if current > n:
#         return
#     print(current)
#     my_func(n, current+1) 
#     if current != n:
#         print(current)

# def main():
#     my_func(4)
    
# if __name__ == "__main__":
#     main()

###########################################################
# ## Part 2: Triangle Patterns

# ### Problem 5: Right Triangle of Stars

# Print a right-aligned triangle with n rows. Row i has i stars.

# ```
# right_triangle(5)
# ```
# **Output:**
# ```
# *
# **
# ***
# ****
# *****
# ```

# **Hint:** You might want a helper function that prints k stars on one line.
# def my_func(k):

#     if k ==0:
#         return
#     my_func(k-1)
#     print('*' * k)
    

# def main():
#     my_func(5)
    
# if __name__ == "__main__":
#     main()

###################################################
### Problem 6: Inverted Triangle

# Print an inverted triangle — n stars on the first row, 1 star on the last.

# ```
# inverted_triangle(5)
# ```
# **Output:**
# ```
# *****
# ****
# ***
# **
# *
# def my_func(k):
#     if k == 0:
#         return 
#     print('*' * k)
#     my_func(k-1)

# def main():
#     my_func(5)

# if __name__ == "__main__":
#     main()
########################################################
### Problem 7: Number Triangle

# Print a triangle where row i contains the numbers 1 through i.

# ```
# number_triangle(5)
# ```
# **Output:**
# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def print_range(k):
    for i in range(1, k + 1):
        print(i, end= " ")
    print()
         

def my_func(k):
    if k == 0:
        return
    my_func(k - 1)
    print_range(k)
 

def main():
    my_func(5)

if __name__ == "__main__":
    main()
########################################################
