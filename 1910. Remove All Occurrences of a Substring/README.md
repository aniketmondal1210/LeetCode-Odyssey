# Remove All Occurrences of a Substring

## Problem

Given two strings `s` and `part`, repeatedly perform the following operation until `part` no longer appears in `s`:

1. Find the **leftmost occurrence** of the substring `part`.
2. Remove that occurrence from `s`.

Return the final string after all occurrences have been removed.

A **substring** is a contiguous sequence of characters within a string.

---

## Examples

### Example 1

**Input**

```text
s = "daabcbaabcbc"
part = "abc"
```

**Output**

```text
"dab"
```

**Explanation**

```text
daabcbaabcbc
  ↓ remove "abc"
dabaabcbc

dabaabcbc
    ↓ remove "abc"
dababc

dababc
   ↓ remove "abc"
dab
```

No more occurrences of `"abc"` remain.

---

### Example 2

**Input**

```text
s = "axxxxyyyyb"
part = "xy"
```

**Output**

```text
"ab"
```

**Explanation**

```text
axxxxyyyyb
    ↓
axxxyyyb

axxxyyyb
   ↓
axxyyb

axxyyb
  ↓
axyb

axyb
 ↓
ab
```

No more occurrences of `"xy"` remain.

---

## Constraints:

- 1 <= s.length <= 1000
- 1 <= part.length <= 1000
- s​​​​​​ and part consists of lowercase English letters.

---
