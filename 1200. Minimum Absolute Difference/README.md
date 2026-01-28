# Minimum Absolute Difference Pairs

## Problem Statement
Given an array of **distinct integers** `arr`, find all pairs of elements with the **minimum absolute difference** among all possible pairs.

Return the list of pairs in **ascending order** (with respect to pairs), where each pair `[a, b]` satisfies:
- `a < b`
- `b - a` equals the minimum absolute difference in the array

---

## Examples

### Example 1
**Input**

arr = [4, 2, 1, 3]

**Output**

[[1, 2], [2, 3], [3, 4]]


### Example 2
**Input**

arr = [1, 3, 6, 10, 15]

**Output**

[[1, 3]]


### Example 3
**Input**

arr = [3, 8, -10, 23, 19, -4, -14, 27]

**Output**

[[-14, -10], [19, 23], [23, 27]]


---

## Constraints:

- 2 <= arr.length <= 10^5
- -10^6 <= arr[i] <= 10^6

---
