# Smallest Number with Digit Product Divisible by t

## Problem Statement
You are given two integers `n` and `t`.  
Return the **smallest integer greater than or equal to `n`** such that the **product of its digits** is divisible by `t`.

---

## Examples

### Example 1
**Input:**  

n = 10, t = 2

**Output:**  

10

**Explanation:**  
Digits of 10 → `1` and `0`.  
Product = `1 * 0 = 0`, and `0` is divisible by `2`.  
Hence, the smallest valid number is `10`.

---

### Example 2
**Input:**  

n = 15, t = 3

**Output:**  

16

**Explanation:**  
Digits of 15 → `1 * 5 = 5` (not divisible by 3)  
Digits of 16 → `1 * 6 = 6` (divisible by 3)  
Hence, the answer is `16`.

---

## Constraints
- `1 <= n <= 100`
- `1 <= t <= 10`

---
