# Maximum Product of Two Digits

## Problem Statement

You are given a **positive integer** `n`.

Your task is to return the **maximum product** of any two **digits** in `n`.

- You may use the same digit twice **only** if it appears more than once in `n`.
- Digits are derived from the base-10 representation of the number.

---

## Examples

### Example 1
**Input:**  
`n = 31`  
**Output:**  
`3`  
**Explanation:**  
Digits: `[3, 1]`  
Possible products: `3 * 1 = 3`  
Maximum product: `3`

---

### Example 2  
**Input:**  
`n = 22`  
**Output:**  
`4`  
**Explanation:**  
Digits: `[2, 2]`  
Possible products: `2 * 2 = 4`  
Maximum product: `4`

---

### Example 3  
**Input:**  
`n = 124`  
**Output:**  
`8`  
**Explanation:**  
Digits: `[1, 2, 4]`  
Products: `1*2=2`, `1*4=4`, `2*4=8`  
Maximum: `8`

---

## Constraints

- `10 <= n <= 10^9`

---
