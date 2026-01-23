# Maximum Absolute Difference in a Circular Array

## Problem Statement
You are given a **circular array** `nums`.  
Your task is to find the **maximum absolute difference between adjacent elements**.

👉 In a **circular array**, the **first and last elements are also adjacent**.

---

## Examples

### Example 1
**Input:**

nums = [1, 2, 4]


**Output:**

3


**Explanation:**  
Adjacent pairs (considering circular nature):
- |1 − 2| = 1  
- |2 − 4| = 2  
- |4 − 1| = 3  

Maximum difference = **3**

---

### Example 2
**Input:**

nums = [-5, -10, -5]


**Output:**

5


**Explanation:**  
Adjacent pairs:
- |-5 − (-10)| = 5  
- |-10 − (-5)| = 5  
- |-5 − (-5)| = 0  

Maximum difference = **5**

---

## Constraints

- 2 ≤ nums.length ≤ 100
- -100 ≤ nums[i] ≤ 100


---
