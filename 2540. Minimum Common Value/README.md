# Minimum Common Element in Two Sorted Arrays

## Problem Statement
Given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing** order,  
return the **minimum integer common** to both arrays.  
If there is **no** common integer, return `-1`.

An integer is considered *common* if it appears **at least once** in both arrays.

---

## Examples

### Example 1
**Input:**  
`nums1 = [1, 2, 3]`  
`nums2 = [2, 4]`  
**Output:**  
`2`  

**Explanation:**  
The common integers are `{2}` → smallest is `2`.

---

### Example 2
**Input:**  
`nums1 = [1, 2, 3, 6]`  
`nums2 = [2, 3, 4, 5]`  
**Output:**  
`2`  

**Explanation:**  
The common integers are `{2, 3}` → smallest is `2`.

---

## Constraints
- `1 ≤ nums1.length, nums2.length ≤ 10^5`
- `1 ≤ nums1[i], nums2[j] ≤ 10^9`
- Arrays are sorted in **non-decreasing order**

---
