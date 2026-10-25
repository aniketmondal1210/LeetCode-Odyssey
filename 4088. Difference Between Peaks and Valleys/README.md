# Difference Between Peaks and Valleys

## Problem Description

You are given an integer array `nums` of length `n`.

An index `i` is called a **peak** if all of the following conditions hold:
- $0 < i < n - 1$
- $\text{nums}[i] > \text{nums}[i - 1]$
- $\text{nums}[i] > \text{nums}[i + 1]$

An index `i` is called a **valley** if all of the following conditions hold:
- $0 < i < n - 1$
- $\text{nums}[i] < \text{nums}[i - 1]$
- $\text{nums}[i] < \text{nums}[i + 1]$

Return an integer denoting the difference between the sum of all peak values and the sum of all valley values.

---

## Examples

### Example 1
- **Input:** `nums = [1, 5, 2, 4, 1, 3, 0]`
- **Output:** `9`
- **Explanation:** 
  - Peak values are `nums[1] = 5`, `nums[3] = 4`, and `nums[5] = 3`. (Sum = 12)
  - Valley values are `nums[2] = 2` and `nums[4] = 1`. (Sum = 3)
  - Difference = $12 - 3 = 9$.

### Example 2
- **Input:** `nums = [-5, -6, -1, -2, 5, 3, 2]`
- **Output:** `12`
- **Explanation:** 
  - Peak values are `nums[2] = -1` and `nums[4] = 5`. (Sum = 4)
  - Valley values are `nums[1] = -6` and `nums[3] = -2`. (Sum = -8)
  - Difference = $4 - (-8) = 12$.

### Example 3
- **Input:** `nums = [6, 5, 2, 5, 5, 3, 6]`
- **Output:** `-5`
- **Explanation:** 
  - No peak values exist. (Sum = 0)
  - Valley values are `nums[2] = 2` and `nums[5] = 3`. (Sum = 5)
  - Difference = $0 - 5 = -5$.

---

## Constraints

- $3 \le n == \text{nums.length} \le 100$
- $-100 \le \text{nums}[i] \le 100$

---
