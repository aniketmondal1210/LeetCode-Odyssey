# Mirror Distance of a Number

## Problem Statement
You are given an integer `n`.

The **mirror distance** of `n` is defined as:

abs(n - reverse(n))


where:
- `reverse(n)` is the integer formed by reversing the digits of `n`
- `abs(x)` denotes the absolute value of `x`

Return the **mirror distance** of `n`.

---

## Examples

### Example 1
**Input:**  

n = 25

**Output:**  

27

**Explanation:**  
- `reverse(25) = 52`  
- `abs(25 - 52) = 27`

---

### Example 2
**Input:**  

n = 10

**Output:**  

9

**Explanation:**  
- `reverse(10) = 01 = 1`  
- `abs(10 - 1) = 9`

---

### Example 3
**Input:**  

n = 7

**Output:**  

0

**Explanation:**  
- `reverse(7) = 7`  
- `abs(7 - 7) = 0`

---

## Constraints

1 ≤ n ≤ 10⁹

---
