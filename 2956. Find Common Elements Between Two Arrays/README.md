# Count Common Elements Between Two Arrays

## Problem Statement
You are given two integer arrays `nums1` and `nums2` of sizes `n` and `m`, respectively.

You need to calculate:
- **answer1**: the number of indices `i` such that `nums1[i]` exists in `nums2`
- **answer2**: the number of indices `i` such that `nums2[i]` exists in `nums1`

Return the result as:

[answer1, answer2]


---

## Example 1
**Input:**

nums1 = [2, 3, 2]
nums2 = [1, 2]


**Output:**

[2, 1]


**Explanation:**
- In `nums1`, elements at indices `0` and `2` (value `2`) exist in `nums2`
- In `nums2`, element at index `1` (value `2`) exists in `nums1`

---

## Example 2
**Input:**

nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]


**Output:**

[3, 4]


**Explanation:**
- Elements at indices `1`, `2`, and `3` in `nums1` exist in `nums2`
- Elements at indices `0`, `1`, `3`, and `4` in `nums2` exist in `nums1`

---

## Example 3
**Input:**

nums1 = [3, 4, 2, 3]
nums2 = [1, 5]


**Output:**

[0, 0]


**Explanation:**
No common elements exist between the two arrays.

---

## Constraints

- n == nums1.length
- m == nums2.length
- 1 ≤ n, m ≤ 100
- 1 ≤ nums1[i], nums2[i] ≤ 100


---
