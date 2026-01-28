# Uncommon Words from Two Sentences

## Problem Statement
A **sentence** is a string of single-space separated words where each word consists only of lowercase English letters.

A **word is uncommon** if:
- It appears **exactly once** in **one** of the sentences, and
- It **does not appear** in the other sentence.

Given two sentences `s1` and `s2`, return a list of all **uncommon words**.  
The answer may be returned in **any order**.

---

## Examples

### Example 1
**Input:**

s1 = "this apple is sweet"
s2 = "this apple is sour"


**Output:**

["sweet", "sour"]


**Explanation:**
- `"sweet"` appears once in `s1` and not in `s2`
- `"sour"` appears once in `s2` and not in `s1`

---

### Example 2
**Input:**

s1 = "apple apple"
s2 = "banana"


**Output:**

["banana"]


**Explanation:**
- `"apple"` appears more than once in `s1`, so it is not uncommon
- `"banana"` appears exactly once in `s2` and not in `s1`

---

## Constraints:

- 1 <= s1.length, s2.length <= 200
- s1 and s2 consist of lowercase English letters and spaces.
- s1 and s2 do not have leading or trailing spaces.
- All the words in s1 and s2 are separated by a single space.

---
