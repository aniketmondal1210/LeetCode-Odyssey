# Least Frequent Digit in an Integer

## Problem Statement
You are given an integer `n`.  
Your task is to find the **digit that occurs least frequently** in its decimal representation.

If **multiple digits** have the same minimum frequency, return the **smallest digit** among them.

Return the chosen digit as an integer.

---

## Examples

### Example 1
**Input:**  

n = 1553322


**Output:**  

1


**Explanation:**  
- Digit frequencies:
  - 1 → 1 time
  - 2 → 2 times
  - 3 → 2 times
  - 5 → 2 times  
- The least frequent digit is `1`.

---

### Example 2
**Input:**  

n = 723344511


**Output:**  

2


**Explanation:**  
- Digit frequencies:
  - 7 → 1 time
  - 2 → 1 time
  - 5 → 1 time
  - Others → more than 1 time  
- Least frequency is `1`. Among `{2, 5, 7}`, the smallest digit is `2`.

---

## Constraints

1 ≤ n ≤ 2^31 − 1

---
