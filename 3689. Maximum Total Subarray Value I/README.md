# Maximum Total Value from K Subarrays

## Problem Statement
You are given:
- An integer array `nums` of length `n`
- An integer `k`

You must choose **exactly `k` non-empty subarrays** `nums[l..r]`.  
Subarrays **may overlap**, and you may even choose the **same subarray multiple times**.

This subarray is simply the full range covering the global maximum and global minimum.

---

## Example 1

**Input:**  

nums = [1,3,2], k = 2


- Global max = 3  
- Global min = 1  
- Best value = 3 - 1 = 2  

Total = `2 * 2 = 4`

**Output:**

4


---

## Example 2

**Input:**  

nums = [4,2,5,1], k = 3


- Global max = 5  
- Global min = 1  
- Best value = 5 - 1 = 4  

Total = `4 * 3 = 12`

**Output:**

12


---

## Constraints

- 1 ≤ n ≤ 5 × 10⁴
- 0 ≤ nums[i] ≤ 10⁹
- 1 ≤ k ≤ 10⁵


---
