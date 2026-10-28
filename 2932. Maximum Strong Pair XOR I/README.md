# Maximum Strong Pair XOR I

## Problem Description

You are given a 0-indexed integer array `nums`. A pair of integers `x` and `y` is called a **strong pair** if it satisfies the condition:

$$\vert{}x - y\vert{} \le \min(x, y)$$

You need to select two integers from `nums` such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.

Return the maximum XOR value out of all possible strong pairs in the array `nums`. Note that you can pick the same integer twice to form a pair.

---

## Examples

### Example 1
- **Input:** `nums = [1, 2, 3, 4, 5]`
- **Output:** `7`
- **Explanation:** There are 11 strong pairs. The maximum XOR possible from these pairs is $3 \oplus 4 = 7$.

### Example 2
- **Input:** `nums = [10, 100]`
- **Output:** `0`
- **Explanation:** The strong pairs are `(10, 10)` and `(100, 100)`. The maximum XOR possible is $10 \oplus 10 = 0$.

### Example 3
- **Input:** `nums = [5, 6, 25, 30]`
- **Output:** `7`
- **Explanation:** The strong pairs include `(25, 30)`, yielding $25 \oplus 30 = 7$.

---

## Constraints

- $1 \le \text{nums.length} \le 50$
- $1 \le \text{nums}[i] \le 100$

---
