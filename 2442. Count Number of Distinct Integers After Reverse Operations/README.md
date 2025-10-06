# Count Distinct Integers After Reversing Digits

## Problem Statement
You are given an array `nums` consisting of **positive integers**.  
For each integer in `nums`, **reverse its digits** and **add it to the end of the array**.  
You must perform this operation **only on the original elements**.  
Finally, return the **number of distinct integers** in the final array.

---

## Examples

### Example 1
**Input:**

nums = [1, 13, 10, 12, 31]

**Process:**
- Reverse of each: [1, 31, 1, 21, 13]  
- Final array: [1, 13, 10, 12, 31, 1, 31, 1, 21, 13]  
- Distinct elements: {1, 10, 12, 13, 21, 31}

**Output:**

6


---

### Example 2
**Input:**

nums = [2, 2, 2]

**Process:**
- Reverse of each: [2, 2, 2]  
- Final array: [2, 2, 2, 2, 2, 2]  
- Distinct elements: {2}

**Output:**

1


---

## Constraints
- 1 ≤ `nums.length` ≤ 10⁵  
- 1 ≤ `nums[i]` ≤ 10⁶  
- **Expected Time Complexity:** O(n)  
- **Expected Auxiliary Space:** O(n)

---
