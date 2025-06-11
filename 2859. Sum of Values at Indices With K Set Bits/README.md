# Sum of Elements With Exactly K Set Bits at Indices

## Problem Statement

You are given a 0-indexed integer array `nums` and an integer `k`.  
Return the sum of elements in `nums` whose indices have exactly `k` set bits in their binary representation.

A **set bit** in an integer is a bit with value `1` in its binary representation.

---

## Examples

### Example 1

**Input:**  
`nums = [5,10,1,5,2]`, `k = 1`  
**Output:**  
`13`  
**Explanation:**  
Binary of indices:  
- 0 → `000` → 0 set bits  
- 1 → `001` → 1 set bit  
- 2 → `010` → 1 set bit  
- 3 → `011` → 2 set bits  
- 4 → `100` → 1 set bit  

Indices 1, 2, and 4 have exactly 1 set bit → `nums[1] + nums[2] + nums[4] = 10 + 1 + 2 = 13`

---

### Example 2

**Input:**  
`nums = [4,3,2,1]`, `k = 2`  
**Output:**  
`1`  
**Explanation:**  
Binary of indices:  
- 0 → `00` → 0 set bits  
- 1 → `01` → 1 set bit  
- 2 → `10` → 1 set bit  
- 3 → `11` → 2 set bits  

Only index 3 has 2 set bits → `nums[3] = 1`

---

## Constraints

- `1 <= nums.length <= 1000`  
- `1 <= nums[i] <= 10⁵`  
- `0 <= k <= 10`
