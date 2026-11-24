# Minimum Range After Sum Replacements

## Problem Description

Given three integers `a`, `b`, and `c`, you may perform the following operation any number of times (including zero):

- Choose one of the three integers and replace it with the sum of the other two integers. The other two integers remain unchanged.

The **range** of three integers is defined as $\max(a, b, c) - \min(a, b, c)$. Return the minimum range that can be obtained after performing the operation any number of times.

---

## Examples

### Example 1
- **Input:** `a = 9`, `b = 2`, `c = 5`
- **Output:** `5`
- **Explanation:** Replacing `9` with `2 + 5 = 7` yields `(7, 2, 5)`, whose range is `7 - 2 = 5`.

### Example 2
- **Input:** `a = 5`, `b = 7`, `c = 6`
- **Output:** `2`
- **Explanation:** With zero operations, the range is `7 - 5 = 2`, which is already optimal.

### Example 3
- **Input:** `a = 3`, `b = 3`, `c = 3`
- **Output:** `0`
- **Explanation:** All three values are equal, so the range is `3 - 3 = 0`.

---

## Constraints

- $1 \le a, b, c \le 100$

---
