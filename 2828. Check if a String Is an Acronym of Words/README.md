# Check If String Is an Acronym of Words

## Problem Statement

Given an array of strings `words` and a string `s`, determine if `s` is an **acronym** of `words`.

A string `s` is considered an acronym of `words` if it can be formed by **concatenating the first character of each string** in `words`, in order.

---

## Examples

### Example 1:
**Input:**  
`words = ["alice", "bob", "charlie"]`  
`s = "abc"`  
**Output:**  
`true`  
**Explanation:**  
The first characters are 'a', 'b', and 'c', forming "abc".

---

### Example 2:
**Input:**  
`words = ["an", "apple"]`  
`s = "a"`  
**Output:**  
`false`  
**Explanation:**  
The first characters are 'a' and 'a', forming "aa", which does not match "a".

---

### Example 3:
**Input:**  
`words = ["never","gonna","give","up","on","you"]`  
`s = "ngguoy"`  
**Output:**  
`true`  
**Explanation:**  
The acronym formed is "ngguoy", which matches `s`.

---

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 10`
- `1 <= s.length <= 100`
- All elements of `words` and the string `s` consist of lowercase English letters only.

---
