# Minimum Positive Subarray Sum (Length Between L and R)

## Problem Statement
You are given:
- An integer array `nums`
- Two integers `l` and `r`

Your task is to find the **minimum sum** of a subarray such that:
- The subarray length is between `l` and `r` (inclusive)
- The subarray sum is **greater than 0**

If no such subarray exists, return `-1`.

A **subarray** is a contiguous, non-empty sequence of elements within the array.

---

## Examples

### Example 1
**Input**

nums = [3, -2, 1, 4]
l = 2, r = 3


**Output**

1


**Explanation**

Valid subarrays (length 2 to 3, sum > 0):
- `[3, -2]` → sum = 1 ✅
- `[1, 4]` → sum = 5
- `[3, -2, 1]` → sum = 2
- `[-2, 1, 4]` → sum = 3  

Minimum positive sum = **1**

---

### Example 2
**Input**

nums = [-2, 2, -3, 1]
l = 2, r = 3


**Output**

-1


**Explanation**

No subarray of length between `l` and `r` has a sum greater than 0.

---

### Example 3
**Input**

nums = [1, 2, 3, 4]
l = 2, r = 4


**Output**

3


**Explanation**

The subarray `[1, 2]` has the smallest positive sum.

---

## Constraints

- 1 <= nums.length <= 100
- 1 <= l <= r <= nums.length
- -1000 <= nums[i] <= 1000


---
