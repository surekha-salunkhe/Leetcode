# Recursion Practice: Printing Patterns

These problems will help you build intuition for how recursion works, especially how the call stack "remembers" state on the way back up. **No loops allowed** — use only recursion.

---

## Part 1: Basic Printing

### Problem 1: Print 1 to N

Write a recursive function that prints numbers from 1 to n, each on a new line.

```
print_ascending(5)
```
**Output:**
```
1
2
3
4
5
```

---

### Problem 2: Print N to 1

Write a recursive function that prints numbers from n down to 1.

```
print_descending(5)
```
**Output:**
```
5
4
3
2
1
```

**Think about it:** What's the only difference between this and Problem 1 in terms of where the print statement goes?

---

### Problem 3: Print 1 to N to 1

Write a recursive function that prints 1 to n, then n down to 1. You should print **each number twice** (once going up, once coming down).

```
print_mountain(4)
```
**Output:**
```
1
2
3
4
4
3
2
1
```

**Key insight:** You only need ONE recursive call. Think about printing *before* and *after* the recursive call.

---

### Problem 4: Print 1 to N to 1 (Single Peak)

Same as Problem 3, but print n only **once** (the peak appears just once).

```
print_mountain_single_peak(4)
```
**Output:**
```
1
2
3
4
3
2
1
```

---

## Part 2: Triangle Patterns

### Problem 5: Right Triangle of Stars

Print a right-aligned triangle with n rows. Row i has i stars.

```
right_triangle(5)
```
**Output:**
```
*
**
***
****
*****
```

**Hint:** You might want a helper function that prints k stars on one line.

---

### Problem 6: Inverted Triangle

Print an inverted triangle — n stars on the first row, 1 star on the last.

```
inverted_triangle(5)
```
**Output:**
```
*****
****
***
**
*
```

---

### Problem 7: Number Triangle

Print a triangle where row i contains the numbers 1 through i.

```
number_triangle(5)
```
**Output:**
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

### Problem 8: Reverse Number Triangle

Print a triangle where row i contains numbers from i down to 1.

```
reverse_number_triangle(5)
```
**Output:**
```
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
```

---

## Part 3: Centered Patterns

### Problem 9: Centered Pyramid

Print a centered pyramid with n rows. Row i has (2i - 1) stars, centered with spaces.

```
centered_pyramid(5)
```
**Output:**
```
    *
   ***
  *****
 *******
*********
```

**Hint:** Row i needs (n - i) leading spaces and (2i - 1) stars.

---

### Problem 10: Diamond

Print a diamond shape — a pyramid followed by an inverted pyramid. The middle row should appear only once.

```
diamond(5)
```
**Output:**
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

---

### Problem 11: Hollow Diamond

Same as Problem 10, but only print the border — the inside is hollow.

```
hollow_diamond(5)
```
**Output:**
```
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
```

---

## Part 4: Challenge Problems

### Problem 12: Pascal's Triangle

Print the first n rows of Pascal's triangle. Each number is the sum of the two numbers above it.

```
pascals_triangle(6)
```
**Output:**
```
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1
```

**Hint:** Write a recursive function `C(n, k)` that computes "n choose k" using the identity:
```
C(n, k) = C(n-1, k-1) + C(n-1, k)
```
Base cases: `C(n, 0) = 1` and `C(n, n) = 1`

---

### Problem 13: Sierpiński Triangle (Text Version)

Print a Sierpiński triangle of order n using characters. Order 0 is a single `*`. Each higher order combines three copies of the previous order.

```
sierpinski(0)
```
**Output:**
```
*
```

```
sierpinski(1)
```
**Output:**
```
 *
* *
```

```
sierpinski(2)
```
**Output:**
```
   *
  * *
 *   *
* * * *
```

```
sierpinski(3)
```
**Output:**
```
       *
      * *
     *   *
    * * * *
   *       *
  * *     * *
 *   *   *   *
* * * * * * * *
```

**Hint:** Think of it as placing three smaller triangles: one on top, two on the bottom (left and right). You might want to build a 2D grid and fill it in recursively.

---

## Hints & Strategies

1. **Identify your base case first.** What's the simplest version of the problem? Usually n = 0 or n = 1.

2. **Decide where to print.** Printing *before* the recursive call processes top-down. Printing *after* processes bottom-up. Printing both gives you the "mountain" effect.

3. **Use helper functions.** If you need to print a row of k stars, write a separate recursive function for that.

4. **Trust the recursion.** If your recursive call correctly handles n-1, you just need to handle the current step.

5. **Trace small examples by hand.** Draw the call stack for n = 3 to see what happens.

---

## Bonus Challenges

Once you've completed these, try:

- Modify Problem 5-8 to use tail recursion
- Add memoization to Problem 12 (Pascal's Triangle)
- Implement Problem 13 using string concatenation instead of a 2D grid
- Create your own pattern and implement it recursively!

---

Good luck! Remember: if you're stuck, start with the smallest case and work your way up.
