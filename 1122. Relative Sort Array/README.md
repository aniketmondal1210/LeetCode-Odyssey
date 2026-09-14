# Relative Sort Array

## Problem Description

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also present in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` is the same as in `arr2`. Elements that do not appear in `arr2` should be placed at the end of `arr1` in **ascending order**.

---

## Examples

### Example 1
- **Input:** `arr1 = [2,3,1,3,2,4,6,7,9,2,19]`, `arr2 = [2,1,4,3,9,6]`
- **Output:** `[2,2,2,1,4,3,3,9,6,7,19]`
- **Explanation:** 
  - Elements `2, 1, 4, 3, 9, 6` are placed first in the order specified by `arr2`, matching their frequencies in `arr1`.
  - Remaining elements `7` and `19` (not in `arr2`) are appended at the end in sorted order.

### Example 2
- **Input:** `arr1 = [28,6,22,8,44,17]`, `arr2 = [22,28,8,6]`
- **Output:** `[22,28,8,6,17,44]`
- **Explanation:** `22, 28, 8, 6` match `arr2` order, while `17, 44` are appended sorted at the end.

---

## Constraints

- $1 \le \text{arr1.length}, \text{arr2.length} \le 1000$
- $0 \le \text{arr1}[i], \text{arr2}[i] \le 1000$
- All elements of `arr2` are distinct.
- Each `arr2[i]` is present in `arr1`.

---
