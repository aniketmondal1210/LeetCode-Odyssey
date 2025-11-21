# Minimum Remaining Length After Removing Balanced Substrings

## Problem Statement
You are given a string `s` consisting only of the characters `'a'` and `'b'`.

You may repeatedly remove **any substring** in which the number of `'a'` characters is **equal** to the number of `'b'` characters.  
After each removal, the remaining parts are concatenated together.

Return the **minimum possible length** of the string after performing any number of such operations.

---

## Example 1
**Input:**  

s = "aabbab"

**Output:**  

0

**Explanation:**  
The whole string contains three `'a'` and three `'b'`, so it can be removed entirely.

---

## Example 2
**Input:**  

s = "aaaa"

**Output:**  

4

**Explanation:**  
No substring has equal `'a'` and `'b'`, so nothing can be removed.

---

## Example 3
**Input:**  

s = "aaabb"

**Output:**  

1

**Explanation:**  
- Remove substring `"ab"` → remaining `"aab"`
- Remove substring `"ab"` → remaining `"a"`
- No further removals possible.

---

## Key Insight
A removable substring must have equal `'a'` and `'b'`.  
Thus, you can remove as many `'a'`–`'b'` pairs as possible.

The minimum remaining length is:

abs(count(a) - count(b))


---

## Constraints

- 1 <= s.length <= 100000
- s[i] ∈ {'a', 'b'}

---
