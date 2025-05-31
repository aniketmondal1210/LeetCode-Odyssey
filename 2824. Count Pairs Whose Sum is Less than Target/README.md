# Count Pairs Whose Sum is Less than Target

## Problem Statement

Given a 0-indexed integer array `nums` of length `n` and an integer `target`, return the number of pairs `(i, j)` where `0 <= i < j < n` and `nums[i] + nums[j] < target`.

---

## Examples

### Example 1

**Input:**  
`nums = [-1,1,2,3,1]`, `target = 2`  
**Output:**  
`3`  
**Explanation:**  
There are 3 pairs of indices that satisfy the conditions:  
- `(0, 1)` → `-1 + 1 = 0 < 2`  
- `(0, 2)` → `-1 + 2 = 1 < 2`  
- `(0, 4)` → `-1 + 1 = 0 < 2`

---

### Example 2

**Input:**  
`nums = [-6,2,5,-2,-7,-1,3]`, `target = -2`  
**Output:**  
`10`  
**Explanation:**  
There are 10 valid pairs:  
- `(0, 1)` → `-6 + 2 = -4 < -2`  
- `(0, 3)` → `-6 + (-2) = -8 < -2`  
- `(0, 4)` → `-6 + (-7) = -13 < -2`  
- `(0, 5)` → `-6 + (-1) = -7 < -2`  
- `(0, 6)` → `-6 + 3 = -3 < -2`  
- `(1, 4)` → `2 + (-7) = -5 < -2`  
- `(3, 4)` → `-2 + (-7) = -9 < -2`  
- `(3, 5)` → `-2 + (-1) = -3 < -2`  
- `(4, 5)` → `-7 + (-1) = -8 < -2`  
- `(4, 6)` → `-7 + 3 = -4 < -2`

---

## Constraints

- `1 <= nums.length == n <= 50`
- `-50 <= nums[i], target <= 50`
