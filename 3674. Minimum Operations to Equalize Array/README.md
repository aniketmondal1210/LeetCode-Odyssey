# Minimum Operations to Make All Array Elements Equal

## Problem Description

You are given an integer array `nums` of length $n$.

In one operation, you can choose any subarray `nums[l...r]` ($0 \le l \le r < n$) and replace each element in that subarray with the **bitwise AND** of all elements in that subarray.

Return the **minimum number of operations** required to make all elements of `nums` equal.

---

## Examples

### Example 1
- **Input:** `nums = [1, 2]`
- **Output:** `1`
- **Explanation:**
  - Choose `nums[0...1]`: $(1 \ \text{AND} \ 2) = 0$.
  - The array becomes `[0, 0]`. All elements are equal in 1 operation.

### Example 2
- **Input:** `nums = [5, 5, 5]`
- **Output:** `0`
- **Explanation:**
  - All elements are already equal (`[5, 5, 5]`), so $0$ operations are required.

---

## Constraints

- $1 \le n = {nums.length} \le 100$
- $1 \le \text{nums}[i] \le 10^5$

---
