# Closest Prime Numbers in Range

## Problem Statement

Given two integers `left` and `right`, find two prime numbers `num1` and `num2` such that:

- `left ≤ num1 < num2 ≤ right`
- Both are **prime numbers**
- `num2 - num1` is **minimum**
- If multiple pairs have same minimum gap → return the one with **smallest num1**
- If no such pair exists → return `[-1, -1]`

---

## 🧪 Example 1

**Input**

left = 10, right = 19


**Output**

[11, 13]


**Explanation**

Primes in range:

11, 13, 17, 19


Closest gaps:

13 - 11 = 2
19 - 17 = 2


Return `[11, 13]` since `11` is smaller.

---

## 🧪 Example 2

**Input**

left = 4, right = 6


**Output**

[-1, -1]


Only one prime (5), so no pair exists.

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n log log n)`
- **Space Complexity:** `O(n)`
- Where `n = right`

---

## Constraints

- 1 ≤ left ≤ right ≤ 10^6

---
