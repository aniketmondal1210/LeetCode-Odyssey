# Find Smallest Letter Greater Than Target

## Problem Statement
You are given a character array `letters` sorted in **non-decreasing order** and a character `target`.

Your task is to return the **smallest character** in `letters` that is **lexicographically greater** than `target`.

- If no such character exists, return the **first character** of the array.
- The array contains **at least two different characters**.

---

## Examples

### Example 1
**Input:**  

letters = ["c","f","j"], target = "a"


**Output:**  

"c"


**Explanation:**  
The smallest character greater than `'a'` is `'c'`.

---

### Example 2
**Input:**  

letters = ["c","f","j"], target = "c"


**Output:**  

"f"


**Explanation:**  
The smallest character greater than `'c'` is `'f'`.

---

### Example 3
**Input:**  

letters = ["x","x","y","y"], target = "z"


**Output:**  

"x"


**Explanation:**  
No character is greater than `'z'`, so return the first element.

---

## Constraints

- 2 ≤ letters.length ≤ 10⁴
- letters[i] is a lowercase English letter
- letters is sorted in non-decreasing order
- letters contains at least two different characters
- target is a lowercase English letter

---
