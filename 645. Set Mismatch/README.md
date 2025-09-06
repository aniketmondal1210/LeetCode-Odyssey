# Find Duplicate and Missing Number (Set Mismatch)

## Problem Statement
You have a set of integers `s` that originally contains all numbers from `1` to `n`.  
Due to an error:
- One number got duplicated,  
- One number got lost.  

You are given an integer array `nums` representing this erroneous set.  
Your task is to return:
- The number that occurs twice (duplicate).  
- The number that is missing.  

---

## Examples

### Example 1
**Input:**

nums = [1, 2, 2, 4]

**Output:**

[2, 3]

**Explanation:**  
- 2 is repeated twice.  
- 3 is missing.  

---

### Example 2
**Input:**

nums = [1, 1]

**Output:**

[1, 2]

**Explanation:**  
- 1 is repeated.  
- 2 is missing.  

---

## Constraints
- 2 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^4

---
