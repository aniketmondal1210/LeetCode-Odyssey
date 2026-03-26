# Count Consistent Strings

## Problem Statement

Given:
- A string `allowed` (distinct characters)
- An array of strings `words`

A string is **consistent** if **all its characters are present in `allowed`**.

Return the **number of consistent strings**.

---

# Examples

### Example 1

**Input**
```
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
```

**Consistent Strings**
```
"aaab", "baa"
```

**Output**
```
2
```

---

### Example 2

**Input**
```
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
```

All strings are valid.

**Output**
```
7
```

---

### Example 3

**Input**
```
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
```

**Consistent Strings**
```
"cc", "acd", "ac", "d"
```

**Output**
```
4
```

---

## Constraints:

- 1 <= words.length <= 10^4
- 1 <= allowed.length <= 26
- 1 <= words[i].length <= 10
- The characters in allowed are distinct.
- words[i] and allowed contain only lowercase English letters.

---
