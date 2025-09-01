# Bitwise XOR of Duplicates

## Problem Statement
You are given an integer array `nums`, where **each number appears either once or twice**.  

Return the **bitwise XOR** of all numbers that appear **twice**, or `0` if no number appears twice.

---

## Examples

### Example 1
**Input:**  

nums = [1,2,1,3]

**Output:**  

1

**Explanation:**  
The only number that appears twice is `1`.  
So result = `1`.

---

### Example 2
**Input:**  

nums = [1,2,3]

**Output:**  

0

**Explanation:**  
No duplicates in the array.  
So result = `0`.

---

### Example 3
**Input:**  

nums = [1,2,2,1]

**Output:**  

3

**Explanation:**  
Duplicates = `{1, 2}`  
XOR = `1 ⊕ 2 = 3`.

---

## Constraints
- 1 ≤ `nums.length` ≤ 50  
- 1 ≤ `nums[i]` ≤ 50  
- Each number appears **either once or twice**  

---
