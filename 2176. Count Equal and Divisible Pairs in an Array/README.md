# Count Equal Pairs with Product Divisible by k

## Problem Statement

Given a 0-indexed integer array `nums` of length `n` and an integer `k`, return the number of pairs `(i, j)` where:

- `0 <= i < j < n`
- `nums[i] == nums[j]`
- `(i * j)` is divisible by `k`

---

## Examples

### Example 1:

**Input:**  
`nums = [3, 1, 2, 2, 2, 1, 3]`, `k = 2`  
**Output:**  
`4`  

**Explanation:**  
Valid pairs:
- `(0,6)` → nums[0] == nums[6] == 3, 0 * 6 = 0 → divisible by 2  
- `(2,3)` → nums[2] == nums[3] == 2, 2 * 3 = 6 → divisible by 2  
- `(2,4)` → nums[2] == nums[4] == 2, 2 * 4 = 8 → divisible by 2  
- `(3,4)` → nums[3] == nums[4] == 2, 3 * 4 = 12 → divisible by 2  

---

### Example 2:

**Input:**  
`nums = [1, 2, 3, 4]`, `k = 1`  
**Output:**  
`0`  

**Explanation:**  
There are no duplicate values, so no valid `(i, j)` pairs.

---

## Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i], k <= 100`

---
