# Largest Number With Same Parity Swaps

## Problem Description

You are given a positive integer `num`. You may swap any two digits of `num` that have the same parity (i.e., both are odd digits or both are even digits). Return the largest possible value of `num` after any number of swaps.

---

## Examples

### Example 1
- **Input:** `num = 1234`
- **Output:** `3412`
- **Explanation:** 
  - Swap digit `3` with `1` to get `3214`.
  - Swap digit `2` with `4` to get `3412`.
  - This yields the largest possible arrangement while respecting parity constraints.

### Example 2
- **Input:** `num = 65875`
- **Output:** `87655`
- **Explanation:** 
  - Swap `8` and `6` (even digits).
  - Swap first `5` and `7` (odd digits).
  - The resulting maximum number is `87655`.

---

## Constraints

- $1 \le \text{num} \le 10^9$

---
