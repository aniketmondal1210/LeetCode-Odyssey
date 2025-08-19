# Shuffle the Array

## Problem
You are given an array `nums` consisting of `2n` elements in the form:

[x1, x2, ..., xn, y1, y2, ..., yn]

Your task is to return the array in the form:

[x1, y1, x2, y2, ..., xn, yn]


---

## Input
- An array `nums` of length `2n`.
- An integer `n`.

---

## Output
- The rearranged array in the format `[x1, y1, x2, y2, ..., xn, yn]`.

---

## Constraints
- `1 <= n <= 500`  
- `nums.length == 2n`  
- `1 <= nums[i] <= 1000`  

---

## Examples

### Example 1
**Input**  

nums = [2,5,1,3,4,7], n = 3

**Output**  

[2,3,5,4,1,7]

**Explanation**  
`x = [2,5,1]` and `y = [3,4,7]` → shuffle → `[2,3,5,4,1,7]`.

---

### Example 2
**Input**  

nums = [1,2,3,4,4,3,2,1], n = 4

**Output**  

[1,4,2,3,3,2,4,1]


---

### Example 3
**Input**  

nums = [1,1,2,2], n = 2

**Output**  

[1,2,1,2]


---
