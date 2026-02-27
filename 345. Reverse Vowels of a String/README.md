# Reverse Vowels of a String

## Problem Statement

Given a string `s`, reverse **only the vowels** in the string and return the modified string.

Vowels are:
```
a, e, i, o, u
```
They may appear in both **lowercase and uppercase**.

---

## Examples

### Example 1

**Input**
```
s = "IceCreAm"
```

**Output**
```
"AceCreIm"
```

**Explanation**

Vowels in order: `['I', 'e', 'e', 'A']`  
After reversing: `['A', 'e', 'e', 'I']`

---

### Example 2

**Input**
```
s = "leetcode"
```

**Output**
```
"leotcede"
```

---

---

## Time Complexity

```
O(n)
```
Each character is visited at most once.

---

## Auxiliary Space

```
O(n)
```
(Used for character array conversion)

---
