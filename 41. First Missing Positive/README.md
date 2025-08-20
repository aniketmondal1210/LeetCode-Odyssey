# First Missing Positive

## Problem
Given an **unsorted integer array** `nums`, return the **smallest positive integer** that is not present in `nums`.  

You must implement an algorithm that runs in **O(n)** time and uses **O(1)** auxiliary space.

---

## Input
- `nums`: an array of integers (may contain negative numbers, zeros, and duplicates).  

---

## Output
- The smallest positive integer that is missing from `nums`.  

---

## Constraints
- `1 <= nums.length <= 10^5`  
- `-2^31 <= nums[i] <= 2^31 - 1`  

---

## Examples

### Example 1
**Input**  

nums = [1,2,0]

**Output**  

3

**Explanation**  
The numbers `1` and `2` exist, so the next missing positive is `3`.  

---

### Example 2
**Input**  

nums = [3,4,-1,1]

**Output**  

2

**Explanation**  
The smallest missing positive is `2`.  

---

### Example 3
**Input**  

nums = [7,8,9,11,12]

**Output**  

1

**Explanation**  
All numbers are greater than `1`, so the answer is `1`.  

---
