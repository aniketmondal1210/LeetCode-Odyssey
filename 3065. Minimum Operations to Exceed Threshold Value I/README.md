# Remove Elements to Make All Values ≥ k

## Problem Statement

You are given a 0-indexed integer array `nums`, and an integer `k`.

In one operation, you can remove one occurrence of the **smallest element** of `nums`.

Return the **minimum number of operations** needed so that **all elements** of the array are **greater than or equal to `k`**.

---

## Examples

### Example 1

**Input:**  
`nums = [2,11,10,1,3], k = 10`  
**Output:**  
`3`  
**Explanation:**  
- Remove `1` → `[2,11,10,3]`  
- Remove `2` → `[11,10,3]`  
- Remove `3` → `[11,10]`  
Now all elements are `>= 10`. So answer is `3`.

---

### Example 2

**Input:**  
`nums = [1,1,2,4,9], k = 1`  
**Output:**  
`0`  
**Explanation:**  
All elements are already `>= 1`.

---

### Example 3

**Input:**  
`nums = [1,1,2,4,9], k = 9`  
**Output:**  
`4`  
**Explanation:**  
Only `9` is ≥ `9`, so remove all other 4 elements.

---

## Constraints

- `1 <= nums.length <= 50`  
- `1 <= nums[i] <= 10⁹`  
- `1 <= k <= 10⁹`  
- There is at least one index `i` such that `nums[i] >= k`.

---
