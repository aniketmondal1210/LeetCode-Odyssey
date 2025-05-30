# Difference Between Element Sum and Digit Sum of an Array

## Problem Statement

You are given a positive integer array `nums`.

- The **element sum** is the sum of all the elements in `nums`.
- The **digit sum** is the sum of all the digits (not necessarily distinct) that appear in the elements of `nums`.

Return the **absolute difference** between the element sum and the digit sum of `nums`.

Note: The absolute difference between two integers `x` and `y` is defined as `|x - y|`.

---

## Examples

### Example 1

**Input:**  
`nums = [1,15,6,3]`  
**Output:**  
`9`  
**Explanation:**  
- Element sum = 1 + 15 + 6 + 3 = 25  
- Digit sum = 1 + 1 + 5 + 6 + 3 = 16  
- Absolute difference = |25 - 16| = **9**

---

### Example 2

**Input:**  
`nums = [1,2,3,4]`  
**Output:**  
`0`  
**Explanation:**  
- Element sum = 1 + 2 + 3 + 4 = 10  
- Digit sum = 1 + 2 + 3 + 4 = 10  
- Absolute difference = |10 - 10| = **0**

---

## Constraints

- `1 <= nums.length <= 2000`
- `1 <= nums[i] <= 2000`

---
