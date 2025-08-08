# Count Strings That Are a Prefix of a Given String

## Problem Statement
You are given:  
- An array of strings `words` (only lowercase English letters).  
- A string `s` (only lowercase English letters).  

Return the **number of strings** in `words` that are a **prefix** of `s`.

A **prefix** of a string is a substring that occurs at the **beginning** of the string.  
A substring is a contiguous sequence of characters within a string.

---

## Examples

### Example 1:
**Input:**  
`words = ["a","b","c","ab","bc","abc"]`  
`s = "abc"`  
**Output:**  
`3`  
**Explanation:**  
The strings in `words` that are prefixes of `"abc"` are:  
- `"a"`  
- `"ab"`  
- `"abc"`

---

### Example 2:
**Input:**  
`words = ["a","a"]`  
`s = "aa"`  
**Output:**  
`2`  
**Explanation:**  
Both `"a"` occurrences in `words` are prefixes of `"aa"`.  
Duplicates are counted individually.

---

## Constraints
- `1 ≤ words.length ≤ 1000`
- `1 ≤ words[i].length, s.length ≤ 10`
- `words[i]` and `s` consist of lowercase English letters only.

---
