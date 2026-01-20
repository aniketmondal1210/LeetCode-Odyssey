# Rearrange Array by Sign

## Problem Statement
You are given a **0-indexed integer array `nums`** of even length consisting of an **equal number of positive and negative integers**.

Your task is to rearrange the array such that:

1. Every **consecutive pair** of integers has **opposite signs**.
2. For integers with the **same sign**, their **relative order is preserved**.
3. The rearranged array **must start with a positive integer**.

Return the modified array after rearranging the elements.

> ⚠️ It is **not required** to do the modification in-place.

---

## Examples

### Example 1
**Input**

nums = [3,1,-2,-5,2,-4]


**Output**

[3,-2,1,-5,2,-4]


**Explanation**
- Positive numbers: `[3, 1, 2]`
- Negative numbers: `[-2, -5, -4]`
- Alternating while preserving order gives:

[3, -2, 1, -5, 2, -4]


---

### Example 2
**Input**

nums = [-1, 1]


**Output**

[1, -1]


**Explanation**
- One positive and one negative element.
- The array must start with a positive number.

---

## Constraints

- 2 <= nums.length <= 2 * 10^5
- nums.length is even
- 1 <= |nums[i]| <= 10^5
- Equal number of positive and negative integers


---
