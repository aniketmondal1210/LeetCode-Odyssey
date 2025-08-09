# Find Number Neither Minimum Nor Maximum

## Problem Statement
Given an integer array `nums` containing **distinct positive integers**, return **any number** from the array that is **neither the minimum nor the maximum** value in the array.  

If there is no such number, return **-1**.

---

## Examples

### Example 1:
**Input:**  
nums = [3, 2, 1, 4]

**Output:**  
2

**Explanation:**  
The minimum value is `1` and the maximum value is `4`.  
Either `2` or `3` can be returned.

---

### Example 2:
**Input:**  
nums = [1, 2]

**Output:**  
-1

**Explanation:**  
There is no element in the array that is neither min nor max.

---

### Example 3:
**Input:**  
nums = [2, 1, 3]

**Output:**  
2

**Explanation:**  
`2` is neither the minimum nor the maximum value.

---

## Constraints
- `1 ≤ nums.length ≤ 100`
- `1 ≤ nums[i] ≤ 100`
- All values in `nums` are distinct.

---
