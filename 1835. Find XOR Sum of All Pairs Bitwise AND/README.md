# XOR Sum of All Pairs (Bitwise AND + XOR)

## Problem
The **XOR sum** of a list is the bitwise XOR of all its elements.  
If the list has only one element, its XOR sum is that element itself.

You are given two 0-indexed arrays `arr1` and `arr2` consisting of non-negative integers.  

Consider the list formed by computing:

arr1[i] AND arr2[j] for every pair (i, j)

where `0 <= i < arr1.length` and `0 <= j < arr2.length`.  

Return the **XOR sum** of this list.

---

## Examples

### Example 1
**Input:**

arr1 = [1, 2, 3], arr2 = [6, 5]

**Output:**

0

**Explanation:**
- List = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5]  
- List = [0, 1, 2, 0, 2, 1]  
- XOR sum = 0 ⊕ 1 ⊕ 2 ⊕ 0 ⊕ 2 ⊕ 1 = 0  

---

### Example 2
**Input:**

arr1 = [12], arr2 = [4]

**Output:**

4

**Explanation:**
- List = [12 AND 4] = [4]  
- XOR sum = 4  

---

## Constraints
- 1 ≤ arr1.length, arr2.length ≤ 100,000  
- 0 ≤ arr1[i], arr2[j] ≤ 1e9  

---
