# Self-Dividing Numbers

## Definition
A **self-dividing number** is a number that is divisible by every digit it contains.  
Rules:
- The number must not contain the digit `0`.
- For every digit `d` in the number: `num % d == 0`.

### Example
`128` is self-dividing because:
- `128 % 1 == 0`
- `128 % 2 == 0`
- `128 % 8 == 0`

---

## Problem
Given two integers `left` and `right`, return a list of all self-dividing numbers in the range `[left, right]`.

### Example 1
**Input:**  
left = 1  
right = 22  

**Output:**  
`[1,2,3,4,5,6,7,8,9,11,12,15,22]`

### Example 2
**Input:**  
left = 47  
right = 85  

**Output:**  
`[48,55,66,77]`

---

## Constraints
- `1 <= left <= right <= 10^4`

---
