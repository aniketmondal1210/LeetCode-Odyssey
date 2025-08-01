# Count Patterns as Substrings in Word

## Problem Statement

Given an array of strings `patterns` and a string `word`, return the number of strings in `patterns` that exist as a **substring** in `word`.

A substring is a contiguous sequence of characters within a string.

---

## Examples

### Example 1:
**Input:**  
`patterns = ["a","abc","bc","d"]`, `word = "abc"`  
**Output:**  
`3`  
**Explanation:**
- "a", "abc", and "bc" appear as substrings in "abc".
- "d" does not appear.

---

### Example 2:
**Input:**  
`patterns = ["a","b","c"]`, `word = "aaaaabbbbb"`  
**Output:**  
`2`  
**Explanation:**  
- "a" and "b" are substrings of "aaaaabbbbb".
- "c" is not.

---

### Example 3:
**Input:**  
`patterns = ["a","a","a"]`, `word = "ab"`  
**Output:**  
`3`  
**Explanation:**  
Each "a" appears in "ab", counted 3 times.

---

## Constraints

- `1 <= patterns.length <= 100`
- `1 <= patterns[i].length <= 100`
- `1 <= word.length <= 100`
- `patterns[i]` and `word` consist of lowercase English letters.

---
