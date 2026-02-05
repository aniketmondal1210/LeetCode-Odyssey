# Sort Characters by Frequency

## Problem Statement
You are given a string `s`.  
Your task is to sort the characters of the string in **decreasing order based on their frequency**.

- The frequency of a character is the number of times it appears in the string.
- If multiple valid answers exist, return **any one** of them.
- Characters with the same frequency must appear **together**.
- Uppercase and lowercase characters are treated as **different**.

---

## Example 1
**Input:**

s = "tree"


**Output:**

"eert"


**Explanation:**
- `'e'` appears twice
- `'r'` and `'t'` appear once  
So `'e'` must come before `'r'` and `'t'`.  
`"eetr"` is also a valid answer.

---

## Example 2
**Input:**

s = "cccaaa"


**Output:**

"aaaccc"


**Explanation:**
- `'c'` and `'a'` both appear three times  
Both `"cccaaa"` and `"aaaccc"` are valid.  
`"cacaca"` is invalid because identical characters must be grouped.

---

## Example 3
**Input:**

s = "Aabb"


**Output:**

"bbAa"


**Explanation:**
- `'b'` appears twice
- `'A'` and `'a'` appear once  
Uppercase and lowercase letters are treated as different characters.  
`"bbaA"` is also valid, but `"Aabb"` is incorrect.

---

## Constraints

- 1 ≤ s.length ≤ 5 × 10⁵
- s consists of uppercase letters, lowercase letters, and digits


---
