# Count Beautiful Pairs in an Array

## Problem Statement
You are given a **0-indexed integer array** `nums`.

A pair of indices `(i, j)` where  
`0 ≤ i < j < nums.length`  
is called **beautiful** if:

- The **first digit** of `nums[i]` and  
- The **last digit** of `nums[j]`  

are **coprime**.

Two integers `x` and `y` are coprime if:

gcd(x, y) == 1


Your task is to **return the total number of beautiful pairs** in the array.

---

## Examples

### Example 1
**Input:**

nums = [2, 5, 1, 4]


**Output:**

5


**Explanation:**
Beautiful pairs are:
- (0,1): gcd(2,5) = 1
- (0,2): gcd(2,1) = 1
- (1,2): gcd(5,1) = 1
- (1,3): gcd(5,4) = 1
- (2,3): gcd(1,4) = 1  

Total = **5**

---

### Example 2
**Input:**

nums = [11, 21, 12]


**Output:**

2


**Explanation:**
Beautiful pairs are:
- (0,1): gcd(1,1) = 1
- (0,2): gcd(1,2) = 1  

Total = **2**

---

## Constraints

- 2 ≤ nums.length ≤ 100
- 1 ≤ nums[i] ≤ 9999
- nums[i] % 10 ≠ 0

---
