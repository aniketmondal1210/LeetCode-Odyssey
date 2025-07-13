# Find the Transformation Integer `x`

## Problem Statement

You are given two arrays of **equal length**, `nums1` and `nums2`.

Each element in `nums1` has been increased (or decreased, if negative) by an integer `x` such that:

- `nums1[i] + x == nums2[i]` for all valid `i`

Two arrays are considered equal when they contain the **same integers with the same frequencies**.

Your task is to **return the integer `x`**.

---

## Examples

### Example 1
**Input:**  
`nums1 = [2, 6, 4]`  
`nums2 = [9, 7, 5]`  
**Output:**  
`3`  
**Explanation:**  
Adding 3 to each element of `nums1` gives `[5, 9, 7]` → after sorting: `[5, 7, 9]`  
Same as `nums2` sorted → `[5, 7, 9]`.

---

### Example 2
**Input:**  
`nums1 = [10]`  
`nums2 = [5]`  
**Output:**  
`-5`  
**Explanation:**  
`10 + (-5) = 5`

---

### Example 3
**Input:**  
`nums1 = [1, 1, 1, 1]`  
`nums2 = [1, 1, 1, 1]`  
**Output:**  
`0`  
**Explanation:**  
No change needed. `x = 0`

---

## Constraints

- `1 <= nums1.length == nums2.length <= 100`
- `0 <= nums1[i], nums2[i] <= 1000`
- The input is guaranteed to have **a unique integer `x`** that transforms `nums1` into `nums2`.
