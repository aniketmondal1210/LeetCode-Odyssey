# Search in Rotated Sorted Array II

## Problem Statement

You are given an **integer array `nums`** sorted in **non-decreasing order**, which has been **rotated at an unknown pivot index `k`**, such that the resulting array is:

[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]

You are also given an integer `target`. Your task is to **return true if `target` is in `nums`**, or `false` if it is not.

> ⚠️ Note: The array may contain **duplicate values**.

---

## Examples

### Example 1:
**Input:**  
`nums = [2,5,6,0,0,1,2]`, `target = 0`  
**Output:**  
`true`

---

### Example 2:
**Input:**  
`nums = [2,5,6,0,0,1,2]`, `target = 3`  
**Output:**  
`false`

---

## Constraints

- `1 <= nums.length <= 5000`  
- `-10⁴ <= nums[i] <= 10⁴`  
- `nums` is guaranteed to be rotated at some pivot  
- `-10⁴ <= target <= 10⁴`

---

## Follow Up

This problem is similar to **Search in Rotated Sorted Array**, but `nums` may contain **duplicates**.

### Would this affect the runtime complexity? How and why?
