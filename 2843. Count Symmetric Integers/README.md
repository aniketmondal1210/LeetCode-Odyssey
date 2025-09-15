# Count Symmetric Integers in a Range

We are given two positive integers `low` and `high`.  

An integer `x` of length `2 * n` is called **symmetric** if:  
- The sum of the **first n digits** equals the sum of the **last n digits**.  
- Numbers with an **odd number of digits** are **never symmetric**.  

The task is to return the count of symmetric integers in the range `[low, high]`.

---

## Example 1
**Input:**  
`low = 1, high = 100`  

**Output:**  
`9`  

**Explanation:**  
The symmetric integers are:  
`11, 22, 33, 44, 55, 66, 77, 88, 99`.

---

## Example 2
**Input:**  
`low = 1200, high = 1230`  

**Output:**  
`4`  

**Explanation:**  
The symmetric integers are:  
`1203, 1212, 1221, 1230`.

---

## Constraints
- `1 ≤ low ≤ high ≤ 10^4`

---
