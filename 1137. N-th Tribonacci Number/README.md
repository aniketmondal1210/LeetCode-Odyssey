# Tribonacci Sequence

The **Tribonacci sequence** `Tn` is defined as follows:  

- `T0 = 0`  
- `T1 = 1`  
- `T2 = 1`  
- For `n >= 0`:  

Tn+3 = Tn + Tn+1 + Tn+2


Given an integer `n`, return the value of `Tn`.

---

## Examples

### Example 1
**Input:**  

n = 4


**Output:**  

4


**Explanation:**  
- `T3 = 0 + 1 + 1 = 2`  
- `T4 = 1 + 1 + 2 = 4`  

---

### Example 2
**Input:**  

n = 25


**Output:**  

1389537


---

## Constraints
- 0 ≤ n ≤ 37  
- The answer fits in a 32-bit integer (≤ 2³¹ − 1).  

---
