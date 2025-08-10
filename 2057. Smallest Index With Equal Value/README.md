# Smallest Index With Equal Value

## Problem Statement
You are given a **0-indexed** integer array `nums`.  
Return the **smallest index** `i` such that:  

i mod 10 == nums[i]
  
If no such index exists, return `-1`.

Here,  
`x mod y` denotes the remainder when `x` is divided by `y`.

---

## Examples

### Example 1
**Input:**  
`nums = [0,1,2]`  
**Output:**  
`0`  

**Explanation:**  
- `i = 0`: `0 mod 10 = 0 == nums[0]` ✅  
- `i = 1`: `1 mod 10 = 1 == nums[1]` ✅  
- `i = 2`: `2 mod 10 = 2 == nums[2]` ✅  
All indices satisfy the condition, but the **smallest** index is `0`.

---

### Example 2
**Input:**  
`nums = [4,3,2,1]`  
**Output:**  
`2`  

**Explanation:**  
- `i = 0`: `0 != 4` ❌  
- `i = 1`: `1 != 3` ❌  
- `i = 2`: `2 == 2` ✅  
- `i = 3`: `3 != 1` ❌  
The smallest index that works is `2`.

---

### Example 3
**Input:**  
`nums = [1,2,3,4,5,6,7,8,9,0]`  
**Output:**  
`-1`  

**Explanation:**  
No index satisfies the condition.

---

## Constraints
- `1 ≤ nums.length ≤ 100`
- `0 ≤ nums[i] ≤ 9`

---
