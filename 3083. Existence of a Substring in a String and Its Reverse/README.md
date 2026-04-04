# Substring of Length 2 Present in Reverse

## Problem Statement

Given a string `s`, check if there exists any **substring of length 2** that is also present in the **reverse of s**.

Return:
```
true  → if exists
false → otherwise
```

---

# Examples

### Example 1

**Input**
```
s = "leetcode"
```

Substrings of length 2:
```
le, ee, et, tc, co, od, de
```

Reverse:
```
"edocteel"
```

Common substring:
```
ee
```

**Output**
```
true
```

---

### Example 2

**Input**
```
s = "abcba"
```

Reverse:
```
"abcba"
```

All substrings match.

**Output**
```
true
```

---

### Example 3

**Input**
```
s = "abcd"
```

Reverse:
```
"dcba"
```

No matching substring of length 2.

**Output**
```
false
```

---

## Constraints:

- 1 <= s.length <= 100
- s consists only of lowercase English letters.

---
