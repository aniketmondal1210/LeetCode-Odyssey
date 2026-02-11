# Longest Balanced Subarray (Distinct Even = Distinct Odd)

## Problem Statement
You are given an integer array `nums`.

A subarray is called **balanced** if:

Number of distinct even numbers

Number of distinct odd numbers


Return the **length of the longest balanced subarray**.

---

## Example 1

**Input:**

nums = [2, 5, 4, 3]


**Output:**

4


**Explanation:**
Subarray `[2, 5, 4, 3]`  
Distinct evens → `{2, 4}` → 2  
Distinct odds → `{5, 3}` → 2  
Balanced → Length = 4

---

## Example 2

**Input:**

nums = [3, 2, 2, 5, 4]


**Output:**

5


**Explanation:**
Subarray `[3, 2, 2, 5, 4]`  
Distinct evens → `{2, 4}` → 2  
Distinct odds → `{3, 5}` → 2  
Balanced → Length = 5

---

## Example 3

**Input:**

nums = [1, 2, 3, 2]


**Output:**

3


**Explanation:**
Subarray `[2, 3, 2]`  
Distinct evens → `{2}` → 1  
Distinct odds → `{3}` → 1  
Balanced → Length = 3

---

## Constraints

- 1 ≤ nums.length ≤ 1500
- 1 ≤ nums[i] ≤ 10⁵


---
