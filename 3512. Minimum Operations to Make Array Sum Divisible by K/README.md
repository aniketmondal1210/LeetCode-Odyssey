# Make Array Sum Divisible by K (Minimum Operations)

## Problem Statement
You are given an integer array `nums` and an integer `k`.  
You may perform the following operation **any number of times**:

- Select an index `i` and replace `nums[i]` with `nums[i] - 1`.

Each operation decreases the sum of the array by **1**.

Return the **minimum number of operations** needed so that the **sum of the array becomes divisible by `k`**.

---

## Key Insight
Let:

sum = total sum of nums
rem = sum % k


If `rem == 0`, the sum is already divisible by `k`, so answer = **0**.

Otherwise, we need to reduce the array sum by `rem` using operations.  
Since **each operation reduces the sum by exactly 1**, the minimum operations required is:

operations = rem


This is always possible because you can keep decreasing any elements until needed.

---

## Examples

### Example 1
**Input:**  

nums = [3,9,7], k = 5

**Output:**  

4


**Explanation:**  
Sum = 3 + 9 + 7 = 19  
19 % 5 = 4  
We need 4 operations → reduce sum by 4  
Perform 4 operations on 9 → becomes 5  
New sum = 15 → divisible by 5.

---

### Example 2
**Input:**  

nums = [4,1,3], k = 4

**Output:**  

0


**Explanation:**  
Sum = 8  
8 % 4 = 0 → already divisible.

---

### Example 3
**Input:**  

nums = [3,2], k = 6

**Output:**  

5


**Explanation:**  
Sum = 5  
5 % 6 = 5 → need 5 operations  
After decreasing both elements appropriately → sum becomes 0.

---
