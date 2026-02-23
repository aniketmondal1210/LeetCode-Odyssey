# Circular Sentence

## Problem Statement

A sentence is a list of words separated by a single space (no leading/trailing spaces).

A sentence is **circular** if:

1. The last character of each word equals the first character of the next word.
2. The last character of the last word equals the first character of the first word.

Return `true` if the sentence is circular, otherwise return `false`.

---

## Example 1

**Input**

sentence = "leetcode exercises sound delightful"


**Output**

true


---

## Example 2

**Input**

sentence = "eetcode"


**Output**

true


---

## Example 3

**Input**

sentence = "Leetcode is cool"


**Output**

false


---

## Constraints

- 1 <= sentence.length <= 500
- Only letters and single spaces
- No leading or trailing spaces

---
