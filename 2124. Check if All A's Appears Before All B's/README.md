# Check if All 'a's Appear Before All 'b's

## Problem Statement
You are given a string `s` consisting only of the characters `'a'` and `'b'`.  
Return `true` if every `'a'` appears before every `'b'` in the string. Otherwise, return `false`.

---

## Examples

### Example 1
**Input:**

s = "aaabbb"

**Output:**

true

**Explanation:**  
The `'a'` characters are at indices `[0, 1, 2]`, while the `'b'` characters are at indices `[3, 4, 5]`.  
Every `'a'` appears before every `'b'`.

---

### Example 2
**Input:**

s = "abab"

**Output:**

false

**Explanation:**  
There is an `'a'` at index `2` and a `'b'` at index `1`.  
So, not all `'a'` come before `'b'`.

---

### Example 3
**Input:**

s = "bbb"

**Output:**

true

**Explanation:**  
There are no `'a'` characters, so the condition is satisfied.

---

## Constraints
- 1 <= s.length <= 100 
- s[i] is either 'a' or 'b'.

---
