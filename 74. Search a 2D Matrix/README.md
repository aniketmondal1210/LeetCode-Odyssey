# Search Element in a 2D Matrix

## Problem Statement

You are given an `m x n` integer matrix `matrix` with the following two properties:

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix`, or `false` otherwise.

You must write a solution with time complexity `O(log(m * n))`.

---

## Examples

### Example 1  
**Input:**  
`matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]`, `target = 3`  
**Output:**  
`true`  
**Explanation:**  
3 is present in the matrix.

---

### Example 2  
**Input:**  
`matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]`, `target = 13`  
**Output:**  
`false`  
**Explanation:**  
13 is not present in the matrix.

---

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 ≤ m, n ≤ 100`
- `-10^4 ≤ matrix[i][j], target ≤ 10^4`

---

