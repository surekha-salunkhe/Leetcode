## Part 1: Stack Basics — Matching and Validation [1-7]
## Part 2: Stack for Simplification [8-14]
## Part 3: Monotonic Stack [15-24]
## Part 4: Queue Basics [25-30]
## Part 5: Monotonic Deque [31-33]
## Part 6: Special Stack Problems[34-40]

#######################################################################
## Part 1: Stack Basics — Matching and Validation [1-7]
### Problem 1: Valid Parentheses

# Check if a string of brackets is valid. 
# Every open bracket must have a matching close bracket in the correct order.

# ```
# is_valid("()") → True
# is_valid("()[]{}") → True
# is_valid("(]") → False
# is_valid("([)]") → False
# is_valid("{[]}") → True
# ```

# **Pattern:** Push open brackets onto stack. 
# When you see a close bracket, pop and check if it matches.

# def my_func(s):
#     valid = {'{':'}', '[':']', '(': ')'}
#     stack = [] 

#     for i in s:
#         if i in valid:
#             print(i)
#             stack.append(i)
#         elif not stack or valid[stack.pop()] != i:
#             return False
#     return not stack

# def main():
#     input_str = "([()})"
#     ans = my_func(input_str)
#     print(ans)
#     # return 0

# if __name__ == "__main__":
#     main()

#############################################################

# ### Problem 2: Minimum Add to Make Parentheses Valid

# # Return the minimum number of parentheses to add to make the string valid.

# # ```
# # min_add("())") → 1        # Need one '(' at start
# # min_add("(((") → 3        # Need three ')'
# # min_add("()") → 0
# # min_add("()))((") → 4     # Need 2 '(' and 2 ')'
# # ```

# def my_func(s):
#     open_count = 0
#     additions = 0

#     for i in s:
#         if i == '(':
#             open_count += 1
#         else:
#             if open_count > 0:
#                 open_count -= 1
#             else:
#                 additions += 1
#     return additions + open_count

# def main():
#     inp_str = "()))(("
#     ans = my_func(inp_str)
#     print(ans)
#     # return 0

# if __name__ == "__main__":
#     main()

#############################################################
### Problem 3: Minimum Remove to Make Valid Parentheses

# Remove the minimum number of parentheses to make the string valid. 
# Return any valid result.

# ```
# min_remove("lee(t(c)o)de)") → "lee(t(c)o)de"
# min_remove("a)b(c)d") → "ab(c)d"
# min_remove("))((") → ""


def my_func(s):
    stack = []
    remove = {}

    for i in range(len(s)):
        if s[i] == '()':
            if stack:
                stack.pop()
        if i == ')':
            if not stack:
                remove.add()
def main():
    inp_str = "lee(t(c)o)de)"
    ans = my_func(inp_str)
    print(ans)
    return 0

if __name__ == "__main__":
    main()