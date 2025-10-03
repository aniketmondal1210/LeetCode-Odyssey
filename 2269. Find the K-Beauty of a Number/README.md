# K-Beauty of a Number

## Problem Statement
The **k-beauty** of an integer `num` is defined as the number of substrings of `num` (when read as a string) that satisfy:
1. The substring has a **length of k**.  
2. The substring, when converted to an integer, is a **divisor of num**.  
3. `0` is not considered a divisor.

Your task is to compute the **k-beauty** of a given number.

---

## Examples

### Example 1
**Input**

num = 240, k = 2

**Output**

2

**Explanation**  
- Substrings of length 2: `"24"`, `"40"`  
- `"24"` → 24 divides 240  
- `"40"` → 40 divides 240  
✅ Count = 2  

---

### Example 2
**Input**

num = 430043, k = 2

**Output**

2

**Explanation**  
- Substrings of length 2: `"43"`, `"30"`, `"00"`, `"04"`, `"43"`  
- `"43"` → divisor of 430043  
- `"30"` → not a divisor  
- `"00"` → invalid (0 not divisor)  
- `"04"` → not a divisor  
- `"43"` → divisor again  
✅ Count = 2  

---

## Constraints
- `1 <= num <= 10^9`
- `1 <= k <= num.length` (where num is treated as a string)

---
