# Merge Two 2D Arrays by Summing Values

## Problem Description

You are given two 2D integer arrays `nums1` and `nums2`, where each element is `[id, val]`:
- `nums1` contains unique IDs sorted in strictly ascending order by `id`.
- `nums2` contains unique IDs sorted in strictly ascending order by `id`.

Merge the two arrays into a single 2D array sorted in ascending order by `id` such that:
- Only IDs present in at least one of `nums1` or `nums2` appear in the result.
- Each ID appears once with its value equal to the sum of its values across both arrays (treating a missing ID in either array as having value `0`).

---

## Examples

### Example 1
- **Input:** `nums1 = [[1, 2], [2, 3], [4, 5]]`, `nums2 = [[1, 4], [3, 2], [4, 1]]`
- **Output:** `[[1, 6], [2, 3], [3, 2], [4, 6]]`
- **Explanation:**
  - `id = 1`: `2 + 4 = 6`
  - `id = 2`: `3 + 0 = 3`
  - `id = 3`: `0 + 2 = 2`
  - `id = 4`: `5 + 1 = 6`

### Example 2
- **Input:** `nums1 = [[2, 4], [3, 6], [5, 5]]`, `nums2 = [[1, 3], [4, 3]]`
- **Output:** `[[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]`
- **Explanation:** There are no overlapping IDs, so all entries appear in sorted order by `id`.

---

## Constraints

- $1 \le \text{nums1.length}, \text{nums2.length} \le 200$
- $\text{nums1}[i].\text{length} == \text{nums2}[j].\text{length} == 2$
- $1 \le \text{id}_i, \text{val}_i \le 1000$
- Both arrays contain unique IDs and are in strictly ascending order by `id`.

---
