# Minimum Moves to Make All Array Elements Equal

## Problem Statement
You are given an integer array `nums`.

In one move, you may increase the value of any single element `nums[i]` by `1`.

Your task is to return the **minimum total number of moves** required so that **all elements in the array become equal**.

---

## Key Insight
To minimize the number of moves, all elements must be increased to the **maximum value** already present in the array.

Thus, the minimum moves =  

sum(max(nums) - nums[i]) for all i


---

## Example 1
**Input:**

nums = [2, 1, 3]


**Output:**

3


**Explanation:**
- 2 → 3 (1 move)  
- 1 → 2 → 3 (2 moves)  
Total = **3 moves**

---

## Example 2
**Input:**

nums = [4, 4, 5]


**Output:**

2


**Explanation:**
- 4 → 5 (1 move)  
- 4 → 5 (1 move)  
Total = **2 moves**

---

## Constraints

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100


---
