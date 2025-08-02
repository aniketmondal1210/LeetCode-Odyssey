# Find the Element Repeated N Times

## Problem Statement

You are given an integer array `nums` with the following properties:

- `nums.length == 2 * n`
- `nums` contains `n + 1` **unique elements**
- **Exactly one element** in `nums` is repeated **n times**

Your task is to return the element that is repeated `n` times.

---

## Input

- An integer array `nums` of length `2 * n`

## Output

- Return the integer that appears **n times** in the array.

---

## Examples

### Example 1

**Input:**  
`nums = [1, 2, 3, 3]`  
**Output:**  
`3`  
**Explanation:**  
Element `3` appears twice in array of length 4, and all other elements are unique.

---

### Example 2

**Input:**  
`nums = [2, 1, 2, 5, 3, 2]`  
**Output:**  
`2`  
**Explanation:**  
Element `2` appears three times in array of length 6.

---

### Example 3

**Input:**  
`nums = [5, 1, 5, 2, 5, 3, 5, 4]`  
**Output:**  
`5`  
**Explanation:**  
Element `5` appears four times in array of length 8.

---

## Constraints

- 2 ≤ n ≤ 5000  
- `nums.length == 2 * n`  
- 0 ≤ `nums[i]` ≤ 10⁴  
- `nums` contains `n + 1` unique elements and **exactly one element appears `n` times**

---
