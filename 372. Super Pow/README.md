# Super Power: Compute a^b mod 1337

## Problem Statement

Your task is to calculate `a^b mod 1337`, where `a` is a positive integer, and `b` is an extremely large positive integer represented as an array of digits.

---

## Examples

### Example 1

**Input:**  
`a = 2`, `b = [3]`  
**Output:**  
`8`  
**Explanation:**  
`2^3 = 8`

---

### Example 2

**Input:**  
`a = 2`, `b = [1,0]`  
**Output:**  
`1024`  
**Explanation:**  
`2^10 = 1024`

---

### Example 3

**Input:**  
`a = 1`, `b = [4,3,3,8,5,2]`  
**Output:**  
`1`  
**Explanation:**  
Any power of 1 is 1.

---

## Constraints

- `1 <= a <= 2³¹ - 1`  
- `1 <= b.length <= 2000`  
- `0 <= b[i] <= 9`  
- `b` does not contain leading zeros
