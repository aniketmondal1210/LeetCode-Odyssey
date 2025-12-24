# Count Elements With Both Smaller and Greater Elements

## Problem Statement
You are given an integer array `nums`.

Return the **number of elements** in the array that have:
- at least one **strictly smaller** element, and
- at least one **strictly greater** element  
appearing somewhere in `nums`.

---

## Examples

### Example 1
**Input:**  

nums = [11, 7, 2, 15]


**Output:**  

2


**Explanation:**  
- `7` has `2` strictly smaller and `11` strictly greater  
- `11` has `7` strictly smaller and `15` strictly greater  

So, the answer is `2`.

---

### Example 2
**Input:**  

nums = [-3, 3, 3, 90]


**Output:**  

2


**Explanation:**  
- Both `3`s have `-3` strictly smaller and `90` strictly greater  
- Hence, both occurrences are counted  

Answer = `2`.

---

## Approach
1. Find the **minimum** value in the array.
2. Find the **maximum** value in the array.
3. Count how many elements are:

min < element < max

4. Return the count.

---

## Constraints

1 ≤ nums.length ≤ 100
-10⁵ ≤ nums[i] ≤ 10⁵

---
