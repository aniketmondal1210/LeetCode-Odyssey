# Count Number of Pairs with Absolute Difference K

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of **pairs** `(i, j)` where `i < j` such that:

nums[i] - nums[j]| == k

The absolute value `|x|` is defined as:
- `x` if `x >= 0`
- `-x` if `x < 0`

---

## Examples

### Example 1:

**Input:**  
`nums = [1, 2, 2, 1]`, `k = 1`

**Output:**  
`4`

**Explanation:**  
The pairs with absolute difference 1 are:
- (0, 1)
- (0, 2)
- (1, 3)
- (2, 3)

---

### Example 2:

**Input:**  
`nums = [1, 3]`, `k = 3`

**Output:**  
`0`

**Explanation:**  
No pairs have an absolute difference of 3.

---

### Example 3:

**Input:**  
`nums = [3, 2, 1, 5, 4]`, `k = 2`

**Output:**  
`3`

**Explanation:**  
The valid pairs are:
- (0, 2): |3 - 1| = 2
- (1, 4): |2 - 4| = 2
- (2, 3): |1 - 5| = 4 → ❌  
- (2, 4): |1 - 4| = 3 → ❌  
- (3, 4): |5 - 4| = 1 → ❌  
Valid ones are:
- (0, 2)
- (1, 3)
- (2, 4)

---

## Constraints:

- 1 ≤ `nums.length` ≤ 200  
- 1 ≤ `nums[i]` ≤ 100  
- 1 ≤ `k` ≤ 99
