# Determine if Two Halves of a String Are Alike

## Problem Statement

You are given a string `s` of **even length**. Split this string into two halves of equal lengths:
- Let `a` be the first half
- Let `b` be the second half

Two strings are said to be **alike** if they have the **same number of vowels**.

Return `True` if `a` and `b` are alike. Otherwise, return `False`.

---

## Examples

### Example 1:
**Input:**  
`s = "book"`  
**Output:**  
`True`  
**Explanation:**  
- First half: `"bo"` → 1 vowel  
- Second half: `"ok"` → 1 vowel  
- Since both halves have the same number of vowels, return `True`.

---

### Example 2:
**Input:**  
`s = "textbook"`  
**Output:**  
`False`  
**Explanation:**  
- First half: `"text"` → 1 vowel  
- Second half: `"book"` → 2 vowels  
- Return `False` since the counts differ.

---

## Constraints

- `2 ≤ s.length ≤ 1000`
- `s.length` is even
- `s` consists only of **uppercase and lowercase English letters**

---
