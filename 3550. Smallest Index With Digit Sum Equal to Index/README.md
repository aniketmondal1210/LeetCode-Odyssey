# Smallest Index with Digit Sum Equal to Index

## Problem Statement
You are given an integer array **nums**.  
Your task is to return the **smallest index** `i` such that:

sum_of_digits(nums[i]) == i


If no such index exists, return **-1**.

---

## Example 1

**Input:**

nums = [1, 3, 2]


**Output:**

2


**Explanation:**  
- nums[2] = 2 → digit sum = 2 → equals index 2 → valid  
Thus, answer = 2.

---

## Example 2

**Input:**

nums = [1, 10, 11]


**Output:**

1


**Explanation:**  
- nums[1] = 10 → 1 + 0 = 1 → matches index 1  
- nums[2] = 11 → 1 + 1 = 2 → matches index 2  
Smallest valid index is 1.

---

## Example 3

**Input:**

nums = [1, 2, 3]


**Output:**

-1


**Explanation:**  
No index satisfies the condition.

---
