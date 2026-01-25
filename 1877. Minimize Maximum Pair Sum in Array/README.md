# Minimize the Maximum Pair Sum

## Problem Statement
You are given an integer array `nums` of **even length** `n`.

You need to pair up all elements of `nums` into `n / 2` pairs such that:
- Each element is used **exactly once**
- The **maximum pair sum** is as small as possible

The **pair sum** of a pair `(a, b)` is `a + b`.

Return the **minimum possible value of the maximum pair sum** after optimal pairing.

---

## Examples

### Example 1
**Input:**

nums = [3, 5, 2, 3]


**Output:**

7


**Explanation:**
Optimal pairing:
- (3, 3) → sum = 6
- (5, 2) → sum = 7  

Maximum pair sum = `max(6, 7) = 7`

---

### Example 2
**Input:**

nums = [3, 5, 4, 2, 4, 6]


**Output:**

8


**Explanation:**
Optimal pairing:
- (2, 6) → sum = 8
- (3, 5) → sum = 8
- (4, 4) → sum = 8  

Maximum pair sum = `8`

---

## Constraints

- 2 ≤ n ≤ 10^5
- n is even
- 1 ≤ nums[i] ≤ 10^5

---
