# Check if a 3-Digit Number is Fascinating

## Problem Statement
You are given a **3-digit integer** `n`.  
A number is called **fascinating** if, after concatenating `n`, `2 * n`, and `3 * n`, the resulting number contains **all digits from 1 to 9 exactly once** and **no zeros**.

Return `true` if the number is fascinating, otherwise `false`.

---

## Examples

### Example 1
**Input:**

n = 192

**Output:**

true

**Explanation:**  
Concatenation → `192` + `384` + `576` = `192384576`  
This contains all digits 1–9 exactly once → ✅ Fascinating number.

---

### Example 2
**Input:**

n = 100

**Output:**

false

**Explanation:**  
Concatenation → `100200300` contains `0`s and missing digits → ❌ Not fascinating.

---

## 🧾 Constraints
- 100 ≤ n ≤ 999

---
