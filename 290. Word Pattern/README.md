# Word Pattern Matching

## Problem Statement

Given:
- A string `pattern`
- A string `s` (space-separated words)

Return `true` if `s` follows the same pattern.

### ✅ Conditions (Bijection Required)

- Each character in `pattern` maps to exactly one **unique word** in `s`.
- Each word in `s` maps to exactly one **unique character** in `pattern`.
- No two characters map to the same word.
- No two words map to the same character.

---

## Example 1

**Input**

pattern = "abba"
s = "dog cat cat dog"


**Output**

true


**Explanation**

'a' → dog
'b' → cat


---

## Example 2

**Input**

pattern = "abba"
s = "dog cat cat fish"


**Output**

false


---

## Example 3

**Input**

pattern = "aaaa"
s = "dog cat cat dog"


**Output**

false


---

## Constraints

- 1 <= pattern.length <= 300
- 1 <= s.length <= 3000
- pattern → lowercase letters only
- s → lowercase words separated by single space

---
