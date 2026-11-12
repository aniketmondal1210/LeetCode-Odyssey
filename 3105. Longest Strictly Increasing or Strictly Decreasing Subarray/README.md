# Longest Strictly Increasing or Strictly Decreasing Subarray

## Problem Description

You are given an array of integers `nums`. Return the length of the longest subarray of `nums` which is either **strictly increasing** or **strictly decreasing**.

---

## Examples

### Example 1
- **Input:** `nums = [1, 4, 3, 3, 2]`
- **Output:** `2`
- **Explanation:** 
  - Strictly increasing subarrays include `[1, 4]`.
  - Strictly decreasing subarrays include `[4, 3]` and `[3, 2]`.
  - The maximum length among these is `2`.

### Example 2
- **Input:** `nums = [3, 3, 3, 3]`
- **Output:** `1`
- **Explanation:** All adjacent elements are equal, so the longest strictly increasing or decreasing subarray has a length of `1`.

### Example 3
- **Input:** `nums = [3, 2, 1]`
- **Output:** `3`
- **Explanation:** The entire array `[3, 2, 1]` is strictly decreasing, giving a length of `3`.

---

## Constraints

- $1 \le \text{nums.length} \le 50$
- $1 \le \text{nums}[i] \le 50$

---
