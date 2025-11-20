# Maximize Expression a + b - c

## Problem Statement
You are given an integer array `nums`.

Choose **three distinct elements** `a`, `b`, and `c` from `nums` such that the value of:

a + b - c


is maximized.

Return the **maximum possible value** of this expression.

---

## Key Insight
To maximize:

a + b - c


You need:
- `a` = one of the largest numbers  
- `b` = another one of the largest numbers  
- `c` = the smallest number  

Thus the answer is:

max1 + max2 - min1


Where:
- `max1` = largest element  
- `max2` = second-largest element  
- `min1` = smallest element  

All must be from **distinct indices**, which is naturally satisfied by using sorted values.

---

## Example 1
**Input:**

nums = [1, 4, 2, 5]


**Output:**

8


**Explanation:**
Choose:
- a = 4  
- b = 5  
- c = 1  

Expression = 4 + 5 - 1 = **8**

---

## Example 2
**Input:**

nums = [-2, 0, 5, -2, 4]


**Output:**

11


**Explanation:**
Choose:
- a = 5  
- b = 4  
- c = -2  

Expression = 5 + 4 - (-2) = **11**

---

## Constraints

- 3 <= nums.length <= 100
- -100 <= nums[i] <= 100

---
