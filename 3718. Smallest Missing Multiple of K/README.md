# Smallest Missing Multiple of k

## Problem Statement
Given an integer array `nums` and an integer `k`, return the **smallest positive multiple** of `k` that is **missing** from `nums`.

A multiple of `k` is any positive integer divisible by `k`.

---

## Input
- `nums`: List of integers  
- `k`: An integer

**Constraints:**

1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 100


---

## Output
Return the **smallest positive multiple of k** not present in `nums`.

---

## Explanation
We check for multiples of `k`:  
`k, 2k, 3k, 4k, ...`  
and find the first one **not** in the list.

---

## Examples

### Example 1
**Input:**

nums = [8,2,3,4,6]
k = 2

**Output:**

10

**Explanation:**
Multiples of 2 → 2, 4, 6, 8, 10, 12...  
Missing multiple → **10**

---

### Example 2
**Input:**

nums = [1,4,7,10,15]
k = 5

**Output:**

5

**Explanation:**
Multiples of 5 → 5, 10, 15, 20...  
Missing multiple → **5**

---
