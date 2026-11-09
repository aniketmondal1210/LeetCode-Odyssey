# Maximum Split of Positive Even Integers

## Problem Description

You are given an integer `finalSum`. Split it into a sum of a maximum number of unique positive even integers.

Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for `finalSum`, return an empty list. You may return the integers in any order.

---

## Examples

### Example 1
- **Input:** `finalSum = 12`
- **Output:** `[2, 4, 6]`
- **Explanation:** Valid splits include `(12)`, `(2 + 10)`, `(2 + 4 + 6)`, and `(4 + 8)`. `(2 + 4 + 6)` contains the maximum number of integers (3).

### Example 2
- **Input:** `finalSum = 7`
- **Output:** `[]`
- **Explanation:** There are no valid splits into even integers for an odd sum.

### Example 3
- **Input:** `finalSum = 28`
- **Output:** `[6, 8, 2, 12]` (or any valid split with 4 integers)
- **Explanation:** `(6 + 8 + 2 + 12)` has the maximum number of integers, which is 4.

---

## Constraints

- $1 \le \text{finalSum} \le 10^{10}$

---
