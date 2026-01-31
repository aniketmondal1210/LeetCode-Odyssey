# Reverse Letters and Special Characters Separately

## Problem Statement
You are given a string `s` consisting of **lowercase English letters** and **special characters**.

You must perform the following operations **in order**:

1. **Reverse only the lowercase letters** and place them back into the positions originally occupied by letters.
2. **Reverse only the special characters** and place them back into the positions originally occupied by special characters.
3. Return the resulting string.

---

## Examples

### Example 1
**Input**

s = ")ebc#da@f("


**Output**

"(fad@cb#e)"


**Explanation**
- Letters extracted: `['e','b','c','d','a','f']`
- Reversed letters: `['f','a','d','c','b','e']`
- Special characters extracted: `[')', '#', '@', '(']`
- Reversed specials: `['(', '@', '#', ')']`

Reinserting them into their original positions produces:

"(fad@cb#e)"


---

### Example 2
**Input**

s = "z"


**Output**

"z"


**Explanation**
Only one letter exists, so reversing does not change the string.

---

### Example 3
**Input**

s = "!@#$%^&*()"


**Output**

")(*&^%$#@!"


**Explanation**
There are no letters. All characters are special characters, so reversing them reverses the entire string.

---

## Constraints

- 1 <= s.length <= 100
- s consists only of lowercase English letters and special characters: !@#$%^&*()


---
