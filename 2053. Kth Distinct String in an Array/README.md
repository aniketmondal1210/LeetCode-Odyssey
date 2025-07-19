# Kth Distinct String in an Array

## Problem Statement

A **distinct string** is a string that appears **only once** in the array.

Given an array of strings `arr` and an integer `k`, return the **kth distinct string** present in `arr`.  
If there are fewer than `k` distinct strings, return an empty string `""`.

**Note:** The strings are considered in the **order of their appearance** in the array.

---

## Examples

### Example 1
**Input:**  
`arr = ["d","b","c","b","c","a"], k = 2`  
**Output:**  
`"a"`  
**Explanation:**  
Distinct strings: `["d", "a"]`  
`"a"` is the 2nd distinct string.

---

### Example 2  
**Input:**  
`arr = ["aaa","aa","a"], k = 1`  
**Output:**  
`"aaa"`  
**Explanation:**  
All strings are distinct. The 1st one is `"aaa"`.

---

### Example 3  
**Input:**  
`arr = ["a","b","a"], k = 3`  
**Output:**  
`""`  
**Explanation:**  
Only `"b"` is distinct. Fewer than 3 distinct strings, so return `""`.

---

## Constraints

- `1 ≤ k ≤ arr.length ≤ 1000`
- `1 ≤ arr[i].length ≤ 5`
- `arr[i]` consists of **lowercase English letters** only

---
