# Find All Anagrams in a String

## Problem Statement

Given two strings:

- `s` → main string  
- `p` → pattern string  

Return **all starting indices** of substrings in `s` that are **anagrams of `p`**.

An **anagram** is a string formed by rearranging the letters of another string.

---

## Examples

### Example 1

**Input**
```
s = "cbaebabacd"
p = "abc"
```

**Output**
```
[0,6]
```

**Explanation**

Substrings of length 3:

```
index 0 → "cba" → anagram of "abc"
index 6 → "bac" → anagram of "abc"
```

---

### Example 2

**Input**
```
s = "abab"
p = "ab"
```

**Output**
```
[0,1,2]
```

**Explanation**

```
index 0 → "ab"
index 1 → "ba"
index 2 → "ab"
```

All are anagrams of `"ab"`.

---

## Constraints:

- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.

---
