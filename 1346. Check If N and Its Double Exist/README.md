# Check If N and Its Double Exist

## Problem Statement

Given an array `arr` of integers, check if there exist two indices `i` and `j` such that:

- `i != j`
- `0 <= i, j < arr.length`
- `arr[i] == 2 * arr[j]`

---

## Examples

### Example 1:
**Input:**  
`arr = [10, 2, 5, 3]`  
**Output:**  
`true`  
**Explanation:**  
`arr[0] = 10` and `arr[2] = 5`, so `10 == 2 * 5`.

---

### Example 2:
**Input:**  
`arr = [3, 1, 7, 11]`  
**Output:**  
`false`  
**Explanation:**  
No such pair exists where one is double the other.

---

## Constraints

- `2 <= arr.length <= 500`
- `-10³ <= arr[i] <= 10³`

---
