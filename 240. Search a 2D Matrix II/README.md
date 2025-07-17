# Search a 2D Matrix II

## Problem Statement

Write an efficient algorithm to search for a value `target` in an `m x n` integer matrix `matrix`. The matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

---

## Examples

### Example 1  
**Input:**  
`matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`  
`target = 5`  
**Output:**  
`true`

---

### Example 2  
**Input:**  
`matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`  
`target = 20`  
**Output:**  
`false`

---

## Constraints

- `m == matrix.length`  
- `n == matrix[i].length`  
- `1 <= m, n <= 300`  
- `-10^9 <= matrix[i][j] <= 10^9`  
- Each row is sorted in ascending order.  
- Each column is sorted in ascending order.  
- `-10^9 <= target <= 10^9`

---

## Approach

Start from the **top-right** element:
- If current element == target → return `true`
- If current element > target → move **left**
- If current element < target → move **down**

Repeat until out of bounds.

---
