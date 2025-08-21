# Check if Number Has Equal Digit Count and Digit Value

## Problem
You are given a `0-indexed` string `num` of length `n` consisting of digits.  

Return **true** if for every index `i` in the range `0 <= i < n`,  
the digit `i` occurs `num[i]` times in `num`, otherwise return **false**.

---

## Constraints
- `n == num.length`
- `1 ≤ n ≤ 10`
- `num` consists of digits only

---

## Examples

### Example 1
**Input**

num = "1210"

**Output**

true

**Explanation**  
- num[0] = '1' → digit `0` occurs once ✅  
- num[1] = '2' → digit `1` occurs twice ✅  
- num[2] = '1' → digit `2` occurs once ✅  
- num[3] = '0' → digit `3` occurs zero times ✅  

Hence return **true**.

---

### Example 2
**Input**

num = "030"

**Output**

false

**Explanation**  
- num[0] = '0' → digit `0` occurs **2 times**, but expected 0 ❌  
- num[1] = '3' → digit `1` occurs **0 times**, but expected 3 ❌  

Hence return **false**.

---
