# Count Consistent Subarrays

## Problem Description

You are given an integer array `nums`. A subarray is called **consistent** if the bitwise AND of all its elements is equal to the minimum value of the subarray.

Return the number of consistent subarrays in `nums`.

---

## Examples

### Example 1
- **Input:** `nums = [5, 3, 1, 2]`
- **Output:** `6`
- **Explanation:** 
  - Subarrays `[5]`, `[3]`, `[1]`, `[2]`, `[3, 1]`, and `[5, 3, 1]` all satisfy the condition where their bitwise AND equals their minimum value.

### Example 2
- **Input:** `nums = [1, 1, 1]`
- **Output:** `6`
- **Explanation:** For every subarray, both the bitwise AND and the minimum value are equal to `1`.

### Example 3
- **Input:** `nums = [0]`
- **Output:** `1`
- **Explanation:** The only subarray is `[0]`, whose bitwise AND and minimum value are both `0`.

---

## Constraints

- $1 \le \text{nums.length} \le 100$
- $0 \le \text{nums}[i] \le 100$

---
