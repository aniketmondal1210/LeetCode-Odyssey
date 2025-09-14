# Find Minimum in Rotated Sorted Array

We are given a rotated sorted array `nums` of unique integers.  
The task is to return the **minimum element** of this array.  

The solution must run in **O(log n)** time.

---

## Example 1
**Input:**  
`nums = [3, 4, 5, 1, 2]`  
**Output:**  
`1`  
**Explanation:**  
The original array was `[1, 2, 3, 4, 5]`, rotated 3 times.

---

## Example 2
**Input:**  
`nums = [4, 5, 6, 7, 0, 1, 2]`  
**Output:**  
`0`  
**Explanation:**  
The original array was `[0, 1, 2, 4, 5, 6, 7]`, rotated 4 times.

---

## Example 3
**Input:**  
`nums = [11, 13, 15, 17]`  
**Output:**  
`11`  
**Explanation:**  
The original array was `[11, 13, 15, 17]`, rotated 4 times.

---

## Constraints
- `1 <= n <= 5000`  
- `-5000 <= nums[i] <= 5000`  
- All elements are **unique**  
- Array is sorted in ascending order and rotated between `1` and `n` times  

---
