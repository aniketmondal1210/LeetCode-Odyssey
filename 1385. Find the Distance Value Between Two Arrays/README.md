# Distance Value Between Two Arrays

You are given two integer arrays `arr1` and `arr2`, and an integer `d`.

The **distance value** is defined as the number of elements `arr1[i]` such that **there is no element** `arr2[j]` satisfying:

|arr1[i] − arr2[j]| ≤ d

Return the distance value.

---

## Examples

### Example 1

Input:
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2

Output:
2


**Explanation:**
- For `4`: no element in `arr2` has absolute difference ≤ 2
- For `5`: no element in `arr2` has absolute difference ≤ 2
- For `8`: there exist elements (`10`, `9`, `8`) with difference ≤ 2  
So, count = 2

---

### Example 2

Input:
arr1 = [1, 4, 2, 3]
arr2 = [-4, -3, 6, 10, 20, 30]
d = 3

Output:
2


---

### Example 3

Input:
arr1 = [2, 1, 100, 3]
arr2 = [-5, -2, 10, -3, 7]
d = 6

Output:
1

---

### Constraints

- 1 ≤ arr1.length, arr2.length ≤ 500
- -1000 ≤ arr1[i], arr2[j] ≤ 1000
- 0 ≤ d ≤ 100

---
