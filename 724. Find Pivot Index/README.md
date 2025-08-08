# Find Pivot Index

## Problem Statement
Given an integer array `nums`, find the **pivot index**.  
The pivot index is the index where the **sum of all numbers strictly to the left** is equal to the **sum of all numbers strictly to the right**.

- If the index is at the **left edge**, the left sum is `0` (no elements on the left).
- If the index is at the **right edge**, the right sum is `0` (no elements on the right).
- Return the **leftmost** pivot index if multiple exist.
- If no pivot index exists, return `-1`.

---

## Examples

### Example 1:
**Input:**  
`nums = [1, 7, 3, 6, 5, 6]`  
**Output:**  
`3`  
**Explanation:**  
- Left sum = `1 + 7 + 3 = 11`  
- Right sum = `5 + 6 = 11`  
- Index `3` is the pivot.

---

### Example 2:
**Input:**  
`nums = [1, 2, 3]`  
**Output:**  
`-1`  
**Explanation:**  
No index satisfies the condition.

---

### Example 3:
**Input:**  
`nums = [2, 1, -1]`  
**Output:**  
`0`  
**Explanation:**  
- Left sum = `0`  
- Right sum = `1 + (-1) = 0`  
- Index `0` is the pivot.

---

## Constraints
- `1 ≤ nums.length ≤ 10⁴`
- `-1000 ≤ nums[i] ≤ 1000`

---
