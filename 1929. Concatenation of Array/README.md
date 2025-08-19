# Concatenation of Array

## Problem
Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where:  

- `ans[i] == nums[i]`  
- `ans[i + n] == nums[i]` for `0 <= i < n`  

Specifically, `ans` is the concatenation of two `nums` arrays.  

Return the array `ans`.  

---

## Input
- An array of integers `nums` of size `n`.  

---

## Output
- The array `ans` of size `2n`.  

---

## Constraints
- `n == nums.length`  
- `1 <= n <= 1000`  
- `1 <= nums[i] <= 1000`  

---

## Examples

### Example 1
**Input**  

nums = [1, 2, 1]

**Output**  

[1, 2, 1, 1, 2, 1]

**Explanation**  
Concatenation: `[nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]`.  

---

### Example 2
**Input**  

nums = [1, 3, 2, 1]

**Output**  

[1, 3, 2, 1, 1, 3, 2, 1]

**Explanation**  
Concatenation: `[nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]`.  

---
