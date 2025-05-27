# Difference Between Sum of Non-Multiples and Multiples of `m`

## Problem Statement

You are given positive integers `n` and `m`.

Define two values:

- **num1**: Sum of all integers from `1` to `n` (inclusive) **not divisible** by `m`.
- **num2**: Sum of all integers from `1` to `n` (inclusive) **divisible** by `m`.

Return the value of `num1 - num2`.

---

## Examples

### Example 1:
**Input:**  
`n = 10`, `m = 3`  
**Output:**  
`19`  
**Explanation:**  
- Not divisible by 3: [1, 2, 4, 5, 7, 8, 10] → sum = 37  
- Divisible by 3: [3, 6, 9] → sum = 18  
- `37 - 18 = 19`

---

### Example 2:
**Input:**  
`n = 5`, `m = 6`  
**Output:**  
`15`  
**Explanation:**  
- Not divisible by 6: [1, 2, 3, 4, 5] → sum = 15  
- Divisible by 6: [] → sum = 0  
- `15 - 0 = 15`

---

### Example 3:
**Input:**  
`n = 5`, `m = 1`  
**Output:**  
`-15`  
**Explanation:**  
- Not divisible by 1: [] → sum = 0  
- Divisible by 1: [1, 2, 3, 4, 5] → sum = 15  
- `0 - 15 = -15`

---

## Constraints

- `1 <= n, m <= 1000`
