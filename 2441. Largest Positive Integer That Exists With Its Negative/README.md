# Largest Positive Integer That Exists With Its Negative

## Problem Statement

You are given an **integer array `nums`** that **does not contain any zeroes**.  
Find the **largest positive integer `k`** such that **`-k` also exists** in the array.

Return the **positive integer `k`**. If there is no such integer, return **-1**.

---

## Examples

### Example 1:
**Input:**  
`nums = [-1, 2, -3, 3]`  
**Output:**  
`3`  
**Explanation:**  
Both 3 and -3 exist, so the answer is 3.

---

### Example 2:
**Input:**  
`nums = [-1, 10, 6, 7, -7, 1]`  
**Output:**  
`7`  
**Explanation:**  
1 and -1 exist, 7 and -7 exist. The largest among them is **7**.

---

### Example 3:
**Input:**  
`nums = [-10, 8, 6, 7, -2, -3]`  
**Output:**  
`-1`  
**Explanation:**  
No positive integer `k` such that `-k` also exists.

---

## Constraints

- `1 <= nums.length <= 1000`  
- `-1000 <= nums[i] <= 1000`  
- `nums[i] != 0`

---
