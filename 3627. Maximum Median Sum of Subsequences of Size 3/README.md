# Maximum Sum of Medians

## Problem Description

You are given an integer array `nums` with a length divisible by `3`. 

You want to make the array empty in steps. In each step, you can select any three elements from the array, compute their median, and remove the selected elements from the array. The median of an odd-length sequence is defined as the middle element of the sequence when it is sorted in non-decreasing order.

Return the maximum possible sum of the medians computed from the selected elements.

---

## Examples

### Example 1
- **Input:** `nums = [2, 1, 3, 2, 1, 3]`
- **Output:** `5`
- **Explanation:** 
  - First step: select elements at indices `2, 4, and 5` (median `3`). Remaining: `[2, 1, 2]`.
  - Second step: select elements at indices `0, 1, and 2` (median `2`). Array becomes empty.
  - Sum of medians: $3 + 2 = 5$.

### Example 2
- **Input:** `nums = [1, 1, 10, 10, 10, 10]`
- **Output:** `20`
- **Explanation:** 
  - Sum of medians: $10 + 10 = 20$.

---

## Constraints

- $1 \le \text{nums.length} \le 5 \times 10^5$
- `nums.length % 3 == 0`
- $1 \le \text{nums}[i] \le 10^9$

---
