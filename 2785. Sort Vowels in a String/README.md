# Sort Vowels in a String

## Problem Statement

Given a **0-indexed string `s`**, create a new string `t` such that:

1. **Consonants remain in the same positions**.
2. **Vowels are sorted in nondecreasing order of ASCII values**.

### Vowels
```
a, e, i, o, u, A, E, I, O, U
```

### Consonants
All other English letters.

---

## Examples

### Example 1

**Input**
```
s = "lEetcOde"
```

**Output**
```
"lEOtcede"
```

**Explanation**

Vowels in the string:
```
E, e, O, e
```

Sorted by ASCII:
```
E, O, e, e
```

Replace them in vowel positions while keeping consonants fixed.

---

### Example 2

**Input**
```
s = "lYmpH"
```

**Output**
```
"lYmpH"
```

**Explanation**

There are **no vowels**, so the string remains unchanged.

---

## Constraints:

- 1 <= s.length <= 105
- s consists only of letters of the English alphabet in uppercase and lowercase.

---
