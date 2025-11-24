# Check if Any Element Has a Prime Frequency

## Problem Statement
You are given an integer array `nums`.

Return **true** if **any element** in the array has a **frequency that is a prime number**.  
Otherwise, return **false**.

A **prime number** is a natural number greater than 1 that has exactly **two factors**:  
`1` and itself.

---

## Example 1
**Input:**  

nums = [1,2,3,4,5,4]

**Output:**  

true

**Explanation:**  
Element `4` appears **twice**, and `2` is prime.

---

## Example 2
**Input:**  

nums = [1,2,3,4,5]

**Output:**  

false

**Explanation:**  
Every element has frequency **1**, which is **not prime**.

---

## Example 3
**Input:**  

nums = [2,2,2,4,4]

**Output:**  

true

**Explanation:**  
- `2` appears **3 times** → 3 is prime  
- `4` appears **2 times** → 2 is prime  
At least one prime frequency exists.

---

## Constraints

- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 100

---
