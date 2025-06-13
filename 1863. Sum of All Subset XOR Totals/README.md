# XOR Sum of All Subsets

## Problem Statement

The **XOR total** of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

Given an array `nums`, return the **sum of all XOR totals** for **every subset** of `nums`.

> Note:  
> - Subsets with the same elements should be counted multiple times.  
> - A subset can be formed by deleting some (possibly zero) elements from the original array.

---

## Examples

### Example 1

**Input:**  
`nums = [1, 3]`  

**Output:**  
`6`

**Explanation:**  
Subsets of `[1, 3]`:  
- `[]` → XOR = `0`  
- `[1]` → XOR = `1`  
- `[3]` → XOR = `3`  
- `[1, 3]` → XOR = `1 ^ 3 = 2`  
Sum = `0 + 1 + 3 + 2 = 6`

---

### Example 2

**Input:**  
`nums = [5, 1, 6]`  

**Output:**  
`28`

**Explanation:**  
Subsets:  
- `[]` → XOR = `0`  
- `[5]` → `5`  
- `[1]` → `1`  
- `[6]` → `6`  
- `[5,1]` → `5 ^ 1 = 4`  
- `[5,6]` → `5 ^ 6 = 3`  
- `[1,6]` → `1 ^ 6 = 7`  
- `[5,1,6]` → `5 ^ 1 ^ 6 = 2`  
Sum = `0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28`

---

### Example 3

**Input:**  
`nums = [3, 4, 5, 6, 7, 8]`  

**Output:**  
`480`

---

## Constraints

- `1 <= nums.length <= 12`  
- `1 <= nums[i] <= 20`
