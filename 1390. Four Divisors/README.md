# Sum of Divisors of Integers with Exactly Four Divisors

## Problem Statement
You are given an integer array `nums`.  
Your task is to return the **sum of divisors** of those numbers in the array that have **exactly four divisors**.  

If no number in the array has exactly four divisors, return `0`.

---

## Example

**Input**

nums = [21, 4, 7]


**Output**

32


**Explanation**
- `21` has 4 divisors: {1, 3, 7, 21} → sum = 32  
- `4` has 3 divisors: {1, 2, 4} → not counted  
- `7` has 2 divisors: {1, 7} → not counted  
So the final answer is `32`.

---

**Input**

nums = [21, 21]


**Output**

64


---

**Input**

nums = [1, 2, 3, 4, 5]


**Output**

0


---

## Constraints
- `1 <= nums.length <= 10^4`  
- `1 <= nums[i] <= 10^5`

---
