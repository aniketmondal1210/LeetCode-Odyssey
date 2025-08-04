# Keep Multiplying Found Values by Two

## Problem Statement

You are given an array of integers `nums`, and an integer `original`. Your task is to repeatedly do the following:

- If `original` exists in `nums`, then multiply it by 2.
- If not, stop the process and return the current value of `original`.

Repeat this as long as the current value of `original` is found in `nums`.

---

## Examples

### Example 1:
**Input:**  
nums = [5, 3, 6, 1, 12]  
original = 3  
**Output:**  
24  
**Explanation:**  
- 3 is found in nums → 3 × 2 = 6  
- 6 is found in nums → 6 × 2 = 12  
- 12 is found in nums → 12 × 2 = 24  
- 24 is not found → return 24

### Example 2:
**Input:**  
nums = [2, 7, 9]  
original = 4  
**Output:**  
4  
**Explanation:**  
- 4 is not found → return 4

---

## Constraints

- 1 ≤ nums.length ≤ 1000  
- 1 ≤ nums[i], original ≤ 1000

---
