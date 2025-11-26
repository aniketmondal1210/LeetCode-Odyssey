# Check Divisibility by Digit Sum + Digit Product

## Problem Statement
You are given a positive integer `n`.  
Determine whether `n` is divisible by the following value:

digit_sum(n) + digit_product(n)


Where:

- **digit sum** = sum of digits of `n`
- **digit product** = product of digits of `n`

Return **true** if `n` is divisible by this total, otherwise return **false**.

---

## Example 1
**Input:**  

n = 99

**Output:**  

true

**Explanation:**  
Digits → 9 and 9  
Sum = 9 + 9 = 18  
Product = 9 × 9 = 81  
Total = 18 + 81 = 99  
99 is divisible by 99 → **true**

---

## Example 2
**Input:**  

n = 23

**Output:**  

false

**Explanation:**  
Digits → 2 and 3  
Sum = 5  
Product = 6  
Total = 11  
23 is **not** divisible by 11 → **false**

---

## Constraints

1 ≤ n ≤ 10⁶

---
