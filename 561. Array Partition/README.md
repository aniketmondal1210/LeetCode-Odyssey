# Array Partition (Maximize Sum of Pair Minimums)

## Problem Description

Given an integer array `nums` of `2n` integers, group these elements into `n` pairs $(a_1, b_1), (a_2, b_2), \dots, (a_n, b_n)$ such that the sum of $\min(a_i, b_i)$ across all `n` pairs is maximized. Return this maximum possible sum.

---

## Examples

### Example 1
- **Input:** `nums = [1, 4, 3, 2]`
- **Output:** `4`
- **Explanation:** Pairing as `(1, 2)` and `(3, 4)` gives $\min(1, 2) + \min(3, 4) = 1 + 3 = 4$, which is the maximum achievable sum.

### Example 2
- **Input:** `nums = [6, 2, 6, 5, 1, 2]`
- **Output:** `9`
- **Explanation:** Pairing as `(1, 2)`, `(2, 5)`, and `(6, 6)` gives $1 + 2 + 6 = 9$.

---

## Constraints

- $1 \le n \le 10^4$
- $\text{nums.length} == 2n$
- $-10^4 \le \text{nums}[i] \le 10^4$

---
