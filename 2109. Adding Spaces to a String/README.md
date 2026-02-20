# Adding Spaces to a String

## Problem Statement

You are given:

- A **0-indexed string** `s`
- A **0-indexed integer array** `spaces`

Each value in `spaces` represents an index in the original string where a space should be inserted **before** that character.

Return the modified string after inserting all spaces.

---

## 🧪 Example 1

**Input**

s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]


**Output**

"Leetcode Helps Me Learn"


---

## 🧪 Example 2

**Input**

s = "icodeinpython"
spaces = [1, 5, 7, 9]


**Output**

"i code in py thon"


---

## 🧪 Example 3

**Input**

s = "spacing"
spaces = [0,1,2,3,4,5,6]


**Output**

" s p a c i n g"


---

## Constraints

- 1 <= s.length <= 3 * 10^5
- 1 <= spaces.length <= 3 * 10^5
- 0 <= spaces[i] <= s.length - 1
- spaces is strictly increasing

---
