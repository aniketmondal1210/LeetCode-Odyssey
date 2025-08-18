# Largest Good Integer

## Problem
You are given a string `num` representing a large integer.  
An integer is **good** if it meets the following conditions:
1. It is a substring of `num` with length **3**.  
2. It consists of only one unique digit.  

Return the **maximum good integer** as a string, or an empty string `""` if no such integer exists.

---

## Note
- A substring is a contiguous sequence of characters within a string.  
- There may be leading zeroes in `num` or in a good integer.  

---

## Input
- A single string `num` of length between **3 and 1000**.  
- `num` consists only of digits (`0-9`).  

---

## Output
- A string representing the largest good integer, or `""` if none exists.  

---

## Examples

### Example 1
**Input**  

6777133339

**Output**  

777

**Explanation**  
Good integers: `"777"` and `"333"`.  
The largest is `"777"`.  

---

### Example 2
**Input**  

2300019

**Output**  

000

**Explanation**  
Only one good integer exists: `"000"`.  

---

### Example 3
**Input**  

42352338

**Output**  

""

**Explanation**  
No substring of length 3 has the same digit.  

---

## Constraints
- `3 ≤ num.length ≤ 1000`  
- `num` only consists of digits.  

---
