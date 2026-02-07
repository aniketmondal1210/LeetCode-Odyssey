# Next Greater Element I

## Problem Statement
The **next greater element** of an element `x` in an array is the first greater element that appears to the **right of x** in the same array.

You are given two distinct 0-indexed integer arrays:
- `nums1`
- `nums2`

Where:
- `nums1` is a subset of `nums2`
- All elements in both arrays are unique

For each element in `nums1`, find its **next greater element in `nums2`**.  
If no such element exists, return `-1` for that position.

Return an array `ans` where:

ans[i] = next greater element of nums1[i] in nums2


---

## Example 1
**Input:**

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]


**Output:**

[-1, 3, -1]


**Explanation:**
- 4 → No greater element to the right → -1  
- 1 → Next greater element is 3  
- 2 → No greater element to the right → -1  

---

## Example 2
**Input:**

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]


**Output:**

[3, -1]


**Explanation:**
- 2 → Next greater element is 3  
- 4 → No greater element → -1  

---

## Constraints

- 1 ≤ nums1.length ≤ nums2.length ≤ 1000
- 0 ≤ nums1[i], nums2[i] ≤ 10⁴
- All integers in nums1 and nums2 are unique
- All elements of nums1 appear in nums2


---

## Follow-up
Can you solve this in: O(nums1.length + nums2.length)


---
