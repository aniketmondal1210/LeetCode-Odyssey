# Largest Even Number from a Binary String of '1' and '2'

## Problem Statement
You are given a string `s` consisting only of the characters `'1'` and `'2'`.

You are allowed to **delete any number of characters** from the string **without changing the order** of the remaining characters.

Your task is to return the **largest possible resultant string** that represents an **even integer**.

If it is not possible to form an even integer, return an **empty string** `""`.

---

## Examples

### Example 1
**Input:**

s = "1112"


**Output:**

"1112"


**Explanation:**  
The string already ends with `'2'`, so it represents an even number and is already the largest possible.

---

### Example 2
**Input:**

s = "221"


**Output:**

"22"


**Explanation:**  
The string ends with `'1'` (odd).  
By deleting `'1'`, the string becomes `"22"`, which is even and the largest possible.

---

### Example 3
**Input:**

s = "1"


**Output:**

""


**Explanation:**  
There is no `'2'` in the string, so it is impossible to form an even number.

---

## Constraints

- 1 <= s.length <= 100
- s consists only of characters '1' and '2'


---
