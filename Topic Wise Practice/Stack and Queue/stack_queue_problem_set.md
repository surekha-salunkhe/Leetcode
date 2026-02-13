# Stacks and Queues Practice

**Stack:** LIFO (Last In, First Out). Use when you need to process things in reverse order or track "most recent" state.

**Queue:** FIFO (First In, First Out). Use when you need to process things in the order they arrived.

---

## Part 1: Stack Basics — Matching and Validation

### Problem 1: Valid Parentheses

Check if a string of brackets is valid. Every open bracket must have a matching close bracket in the correct order.

```
is_valid("()") → True
is_valid("()[]{}") → True
is_valid("(]") → False
is_valid("([)]") → False
is_valid("{[]}") → True
```

**Pattern:** Push open brackets onto stack. When you see a close bracket, pop and check if it matches.

---

### Problem 2: Minimum Add to Make Parentheses Valid

Return the minimum number of parentheses to add to make the string valid.

```
min_add("())") → 1        # Need one '(' at start
min_add("(((") → 3        # Need three ')'
min_add("()") → 0
min_add("()))((") → 4     # Need 2 '(' and 2 ')'
```

---

### Problem 3: Minimum Remove to Make Valid Parentheses

Remove the minimum number of parentheses to make the string valid. Return any valid result.

```
min_remove("lee(t(c)o)de)") → "lee(t(c)o)de"
min_remove("a)b(c)d") → "ab(c)d"
min_remove("))((") → ""
```

---

### Problem 4: Longest Valid Parentheses

Find the length of the longest valid parentheses substring.

```
longest_valid("(()") → 2          # "()"
longest_valid(")()())") → 4       # "()()"
longest_valid("") → 0
longest_valid("()(()") → 2
```

---

### Problem 5: Score of Parentheses

`()` has score 1. `AB` has score A + B. `(A)` has score 2 × A.

```
score("()") → 1
score("(())") → 2           # 2 × 1
score("()()") → 2           # 1 + 1
score("(()(()))") → 6       # 2 × (1 + 2) = 6
```

---

### Problem 6: Remove Outermost Parentheses

Remove the outermost parentheses of every primitive valid parentheses substring.

```
remove_outer("(()())(())") → "()()()"
remove_outer("(()())(())(()(()))") → "()()()()(())"
remove_outer("()()") → ""
```

---

### Problem 7: Check If Word Is Valid After Substitutions

Starting with empty string, you can insert "abc" anywhere. Check if a string could be formed this way.

```
is_valid("aabcbc") → True     # "" → "abc" → "aabcbc"
is_valid("abcabcababcc") → True
is_valid("abccba") → False
is_valid("cababc") → False
```

**Hint:** Similar to valid parentheses — when you see 'c', check if top two are 'a' and 'b'.

---

## Part 2: Stack for Simplification

### Problem 8: Remove All Adjacent Duplicates In String

Repeatedly remove adjacent duplicates until no more exist.

```
remove_duplicates("abbaca") → "ca"
# "abbaca" → "aaca" → "ca"

remove_duplicates("azxxzy") → "ay"
```

**Pattern:** Push characters. If top matches current, pop instead of push.

---

### Problem 9: Remove All Adjacent Duplicates In String II

Remove k adjacent duplicates repeatedly.

```
remove_duplicates("deeedbbcccbdaa", 3) → "aa"
# "deeedbbcccbdaa" → "deedbbcccbdaa" → ... → "aa"

remove_duplicates("abcd", 2) → "abcd"
remove_duplicates("pbbcggttciiippooaais", 2) → "ps"
```

**Hint:** Stack of (character, count) pairs.

---

### Problem 10: Simplify Path

Simplify a Unix-style absolute path.

```
simplify("/home/") → "/home"
simplify("/../") → "/"
simplify("/home//foo/") → "/home/foo"
simplify("/a/./b/../../c/") → "/c"
simplify("/a/../../b/../c//.//") → "/c"
```

**Pattern:** Split by '/', use stack for directories. ".." pops, "." does nothing.

---

### Problem 11: Decode String

Decode a string with pattern k[encoded_string].

```
decode("3[a]2[bc]") → "aaabcbc"
decode("3[a2[c]]") → "accaccacc"
decode("2[abc]3[cd]ef") → "abcabccdcdcdef"
```

---

### Problem 12: Basic Calculator II

Evaluate expression with +, -, \*, / (no parentheses). Integer division truncates toward zero.

```
calculate("3+2*2") → 7
calculate(" 3/2 ") → 1
calculate(" 3+5 / 2 ") → 5
```

---

### Problem 13: Basic Calculator

Evaluate expression with +, -, and parentheses.

```
calculate("1 + 1") → 2
calculate(" 2-1 + 2 ") → 3
calculate("(1+(4+5+2)-3)+(6+8)") → 23
```

---

### Problem 14: Evaluate Reverse Polish Notation

Evaluate an expression in postfix notation.

```
eval_rpn(["2","1","+","3","*"]) → 9     # ((2+1)*3)
eval_rpn(["4","13","5","/","+"]) → 6   # (4+(13/5))
eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) → 22
```

---

## Part 3: Monotonic Stack

A monotonic stack maintains elements in sorted order (either increasing or decreasing). Powerful for "next greater/smaller element" problems.

### Problem 15: Next Greater Element I

For each element in nums1, find the next greater element in nums2 (where it appears).

```
next_greater([4,1,2], [1,3,4,2]) → [-1,3,-1]
# 4 is in nums2, nothing greater to its right → -1
# 1 is in nums2, next greater is 3
# 2 is in nums2, nothing greater to its right → -1
```

**Pattern:** Process nums2 with a monotonic decreasing stack. When you pop, you've found the next greater.

---

### Problem 16: Next Greater Element II (Circular)

Find the next greater element for each position in a circular array.

```
next_greater_circular([1,2,1]) → [2,-1,2]
next_greater_circular([1,2,3,4,3]) → [2,3,4,-1,4]
```

**Hint:** Process the array twice (or use modulo).

---

### Problem 17: Daily Temperatures

Given daily temperatures, find how many days until a warmer day (0 if none).

```
daily_temperatures([73,74,75,71,69,72,76,73]) → [1,1,4,2,1,1,0,0]
daily_temperatures([30,40,50,60]) → [1,1,1,0]
daily_temperatures([30,60,90]) → [1,1,0]
```

---

### Problem 18: Online Stock Span

Design a class that returns the span of a stock price (consecutive days with price ≤ today, including today).

```
StockSpanner()
next(100) → 1
next(80) → 1
next(60) → 1
next(70) → 2      # 70 ≥ 60
next(60) → 1
next(75) → 4      # 75 ≥ 60, 70, 60
next(85) → 6      # 85 ≥ 75, 60, 70, 60, 80
```

---

### Problem 19: Largest Rectangle in Histogram

Find the largest rectangle that can be formed in a histogram.

```
largest_rectangle([2,1,5,6,2,3]) → 10   # 5×2 rectangle at heights 5,6
largest_rectangle([2,4]) → 4
```

**Classic monotonic stack problem.** For each bar, find how far left and right it can extend.

---

### Problem 20: Maximal Rectangle

Find the largest rectangle containing only 1s in a binary matrix.

```
maximal_rectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]) → 6
```

**Hint:** Build histogram for each row, then apply largest rectangle in histogram.

---

### Problem 21: Trapping Rain Water (Stack Approach)

Calculate how much water can be trapped.

```
trap([0,1,0,2,1,0,1,3,2,1,2,1]) → 6
trap([4,2,0,3,2,5]) → 9
```

**Stack approach:** Maintain decreasing stack. When a taller bar comes, calculate water trapped.

---

### Problem 22: Remove K Digits

Remove k digits to make the smallest possible number.

```
remove_k_digits("1432219", 3) → "1219"
remove_k_digits("10200", 1) → "200"
remove_k_digits("10", 2) → "0"
```

**Pattern:** Use monotonic increasing stack. Remove larger digits when a smaller one comes.

---

### Problem 23: 132 Pattern

Check if there exists i < j < k such that nums[i] < nums[k] < nums[j].

```
find132([1,2,3,4]) → False
find132([3,1,4,2]) → True     # 1 < 2 < 4
find132([-1,3,2,0]) → True    # -1 < 2 < 3
```

**Hint:** Traverse from right. Stack tracks potential "3"s, variable tracks max "2".

---

### Problem 24: Sum of Subarray Minimums

Find the sum of min(subarray) for all subarrays.

```
sum_subarray_mins([3,1,2,4]) → 17
# Subarrays: [3]=3, [1]=1, [2]=2, [4]=4, [3,1]=1, [1,2]=1, [2,4]=2, [3,1,2]=1, [1,2,4]=1, [3,1,2,4]=1
# Sum = 3+1+2+4+1+1+2+1+1+1 = 17
```

**Hint:** For each element, count how many subarrays it's the minimum of.

---

## Part 4: Queue Basics

### Problem 25: Implement Queue using Stacks

Implement a queue using only two stacks.

```
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();   // returns 1
queue.pop();    // returns 1
queue.empty();  // returns false
```

**Pattern:** One stack for push, one for pop. Transfer when needed.

---

### Problem 26: Implement Stack using Queues

Implement a stack using only queues.

```
MyStack stack = new MyStack();
stack.push(1);
stack.push(2);
stack.top();    // returns 2
stack.pop();    // returns 2
stack.empty();  // returns false
```

---

### Problem 27: Number of Recent Calls

Count requests in the last 3000 milliseconds.

```
RecentCounter counter = new RecentCounter();
counter.ping(1);      // returns 1
counter.ping(100);    // returns 2
counter.ping(3001);   // returns 3
counter.ping(3002);   // returns 3  (request at 1 is outside [2, 3002])
```

**Pattern:** Queue of timestamps. Remove timestamps older than t - 3000.

---

### Problem 28: Moving Average from Data Stream

Calculate the moving average of the last k numbers.

```
MovingAverage m = new MovingAverage(3);
m.next(1) → 1.0           // 1/1
m.next(10) → 5.5          // (1+10)/2
m.next(3) → 4.67          // (1+10+3)/3
m.next(5) → 6.0           // (10+3+5)/3
```

---

### Problem 29: Design Circular Queue

Implement a circular queue with fixed capacity.

```
MyCircularQueue q = new MyCircularQueue(3);
q.enQueue(1)  → true
q.enQueue(2)  → true
q.enQueue(3)  → true
q.enQueue(4)  → false   // Queue is full
q.Rear()      → 3
q.isFull()    → true
q.deQueue()   → true
q.enQueue(4)  → true
q.Rear()      → 4
```

---

### Problem 30: Design Circular Deque

Implement a double-ended circular queue.

```
MyCircularDeque deque = new MyCircularDeque(3);
deque.insertLast(1)   → true
deque.insertLast(2)   → true
deque.insertFront(3)  → true
deque.insertFront(4)  → false  // Full
deque.getRear()       → 2
deque.isFull()        → true
deque.deleteLast()    → true
deque.insertFront(4)  → true
deque.getFront()      → 4
```

---

## Part 5: Monotonic Deque

### Problem 31: Sliding Window Maximum

Find the maximum in each sliding window of size k.

```
max_sliding_window([1,3,-1,-3,5,3,6,7], 3) → [3,3,5,5,6,7]
# Window [1,3,-1] max=3
# Window [3,-1,-3] max=3
# Window [-1,-3,5] max=5
# ...
```

**Pattern:** Monotonic decreasing deque. Front is always the max. Remove from back if smaller than current.

---

### Problem 32: Shortest Subarray with Sum at Least K

Find the shortest subarray with sum ≥ k. Array may have negative numbers.

```
shortest_subarray([1], 1) → 1
shortest_subarray([1,2], 4) → -1
shortest_subarray([2,-1,2], 3) → 3
shortest_subarray([84,-37,32,40,95], 167) → 3
```

**Hint:** Prefix sum + monotonic deque.

---

### Problem 33: Constrained Subsequence Sum

Find maximum sum of a subsequence where adjacent elements are at most k indices apart.

```
constrained_subset_sum([10,2,-10,5,20], 2) → 37    # [10,2,5,20]
constrained_subset_sum([-1,-2,-3], 1) → -1
constrained_subset_sum([10,-2,-10,-5,20], 2) → 23  # [10,-2,-5,20]? No, [10,20]
```

---

## Part 6: Special Stack Problems

### Problem 34: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in O(1).

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   // returns -3
minStack.pop();
minStack.top();      // returns 0
minStack.getMin();   // returns -2
```

**Pattern:** Store (value, current_min) pairs, or use two stacks.

---

### Problem 35: Max Stack

Design a stack that supports push, pop, top, peekMax, and popMax.

```
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top();      // returns 5
stack.popMax();   // returns 5
stack.top();      // returns 1
stack.peekMax();  // returns 5
stack.pop();      // returns 1
stack.top();      // returns 5
```

---

### Problem 36: Validate Stack Sequences

Given pushed and popped sequences, check if this is a valid sequence of stack operations.

```
validate_stack([1,2,3,4,5], [4,5,3,2,1]) → True
# push 1,2,3,4 → pop 4 → push 5 → pop 5,3,2,1

validate_stack([1,2,3,4,5], [4,3,5,1,2]) → False
```

---

### Problem 37: Asteroid Collision

Asteroids moving in a row. Positive = right, negative = left. When they collide, smaller one explodes. If equal, both explode. Find the final state.

```
asteroid_collision([5,10,-5]) → [5,10]        # 10 and -5 collide, 10 wins
asteroid_collision([8,-8]) → []               # Both explode
asteroid_collision([10,2,-5]) → [10]          # 2 and -5 collide, -5 wins, then 10 and -5, 10 wins
asteroid_collision([-2,-1,1,2]) → [-2,-1,1,2] # No collision (moving away)
```

---

### Problem 38: Backspace String Compare

Compare two strings where '#' means backspace.

```
backspace_compare("ab#c", "ad#c") → True      # Both become "ac"
backspace_compare("ab##", "c#d#") → True      # Both become ""
backspace_compare("a#c", "b") → False
```

**O(1) space approach:** Process from the end using two pointers.

---

### Problem 39: Exclusive Time of Functions

Given function call logs, compute exclusive time for each function.

```
exclusive_time(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])
→ [3, 4]
# Function 0: 0-1 (before 1 starts) + 6 (after 1 ends) = 3
# Function 1: 2-5 = 4
```

---

### Problem 40: Baseball Game

Calculate score based on operations: integer (add score), '+' (sum of last two), 'D' (double last), 'C' (remove last).

```
cal_points(["5","2","C","D","+"]) → 30
# "5" → [5]
# "2" → [5,2]
# "C" → [5] (remove 2)
# "D" → [5,10] (double 5)
# "+" → [5,10,15] (5+10)
# Sum = 30
```

---

## Strategies and Patterns

### When to Use Stack

| Pattern                  | Use Case                                 |
| ------------------------ | ---------------------------------------- |
| Matching pairs           | Parentheses, tags, brackets              |
| Reverse order processing | Undo, back button, expression evaluation |
| Nearest greater/smaller  | Monotonic stack                          |
| Nested structures        | Decode strings, nested lists             |
| Track recent state       | Min stack, calculators                   |

### When to Use Queue

| Pattern                | Use Case                     |
| ---------------------- | ---------------------------- |
| Process in order       | BFS, task scheduling         |
| Sliding window max/min | Monotonic deque              |
| Stream processing      | Moving average, recent calls |
| Buffer                 | Producer-consumer            |

### Monotonic Stack Template

```cpp
// Next greater element (to the right)
vector<int> nextGreater(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> st;  // stores indices

    for (int i = 0; i < n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i]) {
            result[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }
    return result;
}
```

### Monotonic Deque Template

```cpp
// Sliding window maximum
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;  // stores indices, decreasing order of values
    vector<int> result;

    for (int i = 0; i < nums.size(); i++) {
        // Remove elements outside window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }
        // Remove smaller elements (they'll never be max)
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }
        dq.push_back(i);

        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }
    return result;
}
```

### Common Edge Cases

1. **Empty stack/queue** — check before pop/peek
2. **Single element**
3. **All same elements**
4. **Nested structures** (multiple levels deep)
5. **Unbalanced input** (more opens than closes or vice versa)

---

Good luck! Start with Part 1 for matching problems, then Part 3 for monotonic stack — that's where stacks really shine for array problems.
