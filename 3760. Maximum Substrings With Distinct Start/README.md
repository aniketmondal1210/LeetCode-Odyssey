# Maximum Substrings With Distinct Starting Characters

## Problem Statement
You are given a string `s` consisting of lowercase English letters.

Return the **maximum number of substrings** you can split `s` into such that:

- Each substring starts with a **distinct character**
- No two substrings start with the **same** character

---

## Key Insight
Each substring's starting character must be **unique**.

So, the maximum number of substrings you can create is simply:

number of distinct characters in s


Because:
- Each distinct character can start **at most one** substring.
- You can always split the string so that each distinct character serves as the beginning of exactly one substring.

---

## Examples

### Example 1
**Input:**  

s = "abab"

**Output:**  

2


**Explanation:**  
Distinct starting characters possible: `a`, `b`  
One way to split → `"a"`, `"bab"`

---

### Example 2
**Input:**  

s = "abcd"

**Output:**  

4


**Explanation:**  
All characters are distinct → 4 possible substrings.

---

### Example 3
**Input:**  

s = "aaaa"

**Output:**  

1


**Explanation:**  
Only one distinct starting character: `'a'`.

---

## Constraints

- 1 <= s.length <= 100000
- s contains only lowercase English letters.

---
