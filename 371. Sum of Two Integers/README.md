# Sum of Two Integers Without Using + and -

## Problem Statement

Given two integers `a` and `b`, return **the sum** of the two integers **without using** the operators `+` and `-`.

---

## Examples

### Example 1

**Input:**  
`a = 1`, `b = 2`  
**Output:**  
`3`  

### Example 2

**Input:**  
`a = 2`, `b = 3`  
**Output:**  
`5`  

---

## Explanation

You can compute the sum using **bitwise operations**:

- Use XOR (`^`) to add bits without carrying.
- Use AND (`&`) followed by a left shift (`<<`) to calculate the carry.
- Repeat the steps until carry becomes 0.

---

## Constraints

- `-1000 <= a, b <= 1000`
