# Custom Sort Array Using Function

## Problem Statement

You are given an array `arr` and a function `fn`. Return a sorted array `sortedArr`, where `sortedArr` must be sorted in **ascending order** based on the result of applying `fn` to each element of `arr`.

You can assume:
- `fn` always returns a number.
- The return values from `fn` are **unique** for each element of the array (i.e., no two elements will have the same value after applying `fn`).

---

## Examples

### Example 1:
**Input:**  
`arr = [5, 4, 1, 2, 3]`  
`fn = lambda x: x`  
**Output:**  
`[1, 2, 3, 4, 5]`  
**Explanation:**  
Sorting based on `x` itself.

---

### Example 2:
**Input:**  
`arr = [{"x": 1}, {"x": 0}, {"x": -1}]`  
`fn = lambda d: d["x"]`  
**Output:**  
`[{"x": -1}, {"x": 0}, {"x": 1}]`  
**Explanation:**  
Sorting based on the `"x"` property.

---

### Example 3:
**Input:**  
`arr = [[3, 4], [5, 2], [10, 1]]`  
`fn = lambda x: x[1]`  
**Output:**  
`[[10, 1], [5, 2], [3, 4]]`  
**Explanation:**  
Sorted based on the second element in each sublist.

---

## Constraints

- `arr` is a valid JSON array
- `fn` is a function that returns a number
- `1 <= arr.length <= 5 * 10^5`

---
