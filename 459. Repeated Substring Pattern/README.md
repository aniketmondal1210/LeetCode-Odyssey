# Repeated Substring Pattern

## Problem Statement

Given a string `s`, check whether it can be formed by taking a substring of it and appending multiple copies of that substring together.

Return:

- `true` → If possible  
- `false` → Otherwise  

---

## Examples

### Example 1

**Input**

s = "abab"

**Output**
true

**Explanation**  
"ab" + "ab"

---

### Example 2

**Input**

s = "aba"

**Output**

false


---

### Example 3

**Input**

s = "abcabcabcabc"

**Output**

true

**Explanation**  
"abc" repeated 4 times  
or  
"abcabc" repeated 2 times  

---

## Constraints

- 1 <= s.length <= 10^4
- s consists of lowercase English letters.

---
