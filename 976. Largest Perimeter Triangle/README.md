# Largest Perimeter Triangle

## Problem Description

Given an integer array `nums`, return the largest perimeter of a triangle with a non-zero area formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return `0`.

---

## Examples

### Example 1
- **Input:** `nums = [2, 1, 2]`
- **Output:** `5`
- **Explanation:** Side lengths `1`, `2`, and `2` satisfy the triangle inequality ($1 + 2 > 2$), yielding a perimeter of $1 + 2 + 2 = 5$.

### Example 2
- **Input:** `nums = [1, 2, 1, 10]`
- **Output:** `0`
- **Explanation:** No combination of three side lengths (`[1, 1, 2]`, `[1, 1, 10]`, or `[1, 2, 10]`) satisfies $a + b > c$, so no non-degenerate triangle can be formed.

---

## Constraints

- $3 \le \text{nums.length} \le 10^4$
- $1 \le \text{nums}[i] \le 10^6$

---
