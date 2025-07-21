# Number of Distinct Averages

## Problem Statement

You are given a 0-indexed integer array `nums` of even length.

As long as `nums` is not empty, you must repetitively:

1. Find the **minimum number** in `nums` and remove it.
2. Find the **maximum number** in `nums` and remove it.
3. Calculate the **average** of the two removed numbers using:  
   `(a + b) / 2`

Return the **number of distinct averages** calculated during the process.

**Note:**  
When there is a tie for the minimum or maximum number, you can remove any one of them.

---

## Examples

### Example 1:
**Input:**  
nums = [4, 1, 4, 0, 3, 5]  
**Output:**  
2  
**Explanation:**  
1. Remove 0 and 5 → average = 2.5  
2. Remove 1 and 4 → average = 2.5  
3. Remove 3 and 4 → average = 3.5  
Distinct averages: 2.5, 3.5 → return 2

---

### Example 2:
**Input:**  
nums = [1, 100]  
**Output:**  
1  
**Explanation:**  
Only one average is calculated: (1 + 100) / 2 = 50.5 → return 1

---

## Constraints

- 2 ≤ nums.length ≤ 100  
- nums.length is even  
- 0 ≤ nums[i] ≤ 100  

---
