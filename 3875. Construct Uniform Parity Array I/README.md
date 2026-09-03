# Make Array Parity Same

## Problem Description

You are given an array `nums1` of $n$ distinct integers.

You want to construct another array `nums2` of length $n$ such that the elements in `nums2` are either **all odd** or **all even**.

For each index $i$, you must choose exactly one of the following operations:
- $\text{nums2}[i] = \text{nums1}[i]$
- $\text{nums2}[i] = \text{nums1}[i] - \text{nums1}[j]$, for some index $j \neq i$

Return `true` if it is possible to construct such an array `nums2`, otherwise return `false`.

---

## Examples

### Example 1
- **Input:** `nums1 = [2, 3]`
- **Output:** `true`
- **Explanation:**
  - Choose $\text{nums2}[0] = \text{nums1}[0] - \text{nums1}[1] = 2 - 3 = -1$ (Odd)
  - Choose $\text{nums2}[1] = \text{nums1}[1] = 3$ (Odd)
  - $\text{nums2} = [-1, 3]$ (All elements are odd). Return `true`.

### Example 2
- **Input:** `nums1 = [4, 6]`
- **Output:** `true`
- **Explanation:**
  - Choose $\text{nums2}[0] = \text{nums1}[0] = 4$ (Even)
  - Choose $\text{nums2}[1] = \text{nums1}[1] = 6$ (Even)
  - $\text{nums2} = [4, 6]$ (All elements are even). Return `true`.

---

## Constraints

- $1 \le n = \text{nums1.length} \le 100$
- $1 \le \text{nums1}[i] \le 100$
- `nums1` consists of distinct integers.

---
