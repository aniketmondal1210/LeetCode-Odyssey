# String Score Based on Vowels and Consonants

## Problem Statement
You are given a string `s` consisting of:
- lowercase English letters (`a`–`z`)
- spaces
- digits (`0`–`9`)

Let:
- `v` = number of **vowels** in `s`
- `c` = number of **consonants** in `s`

A vowel is one of:  
`a, e, i, o, u`

Any other lowercase English letter is considered a consonant.

### Score Definition
- If `c > 0`  

score = floor(v / c)

- If `c == 0`  

score = 0


Return the **score** of the string.

---

## Examples

### Example 1
**Input**

s = "cooear"


**Output**

2


**Explanation**
- Vowels: `o, o, e, a` → `v = 4`
- Consonants: `c, r` → `c = 2`
- Score = `floor(4 / 2) = 2`

---

### Example 2
**Input**

s = "axeyizou"


**Output**

1


**Explanation**
- Vowels: `a, e, i, o, u` → `v = 5`
- Consonants: `x, y, z` → `c = 3`
- Score = `floor(5 / 3) = 1`

---

### Example 3
**Input**

s = "au 123"


**Output**

0


**Explanation**
- Vowels: `a, u` → `v = 2`
- Consonants: none → `c = 0`
- Score = `0`

---

## Constraints

- 1 <= s.length <= 100
- s consists of lowercase English letters, spaces, and digits


---
