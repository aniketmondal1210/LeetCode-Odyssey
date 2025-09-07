# Largest Number At Least Twice of Others

## Problem Statement
You are given an integer array `nums` where the largest integer is unique.  
Determine whether the largest element in the array is **at least twice** as much as every other number in the array.  

- If it is, return the **index of the largest element**.  
- Otherwise, return **-1**.  

---

## Examples

### Example 1:
**Input:**  

nums = [3, 6, 1, 0]

**Output:**  

1

**Explanation:**  
6 is the largest integer. For every other number in the array `x`,  
`6 >= 2 * x`.  
The index of `6` is `1`, so we return `1`.

---

### Example 2:
**Input:**  

nums = [1, 2, 3, 4]

**Output:**  

-1

**Explanation:**  
The largest number is `4`.  
But `4 < 2 * 3`. Hence, return `-1`.

---

## Constraints
- 2 <= nums.length <= 50
- 0 <= nums[i] <= 100
- The largest element in `nums` is **unique**  

---
