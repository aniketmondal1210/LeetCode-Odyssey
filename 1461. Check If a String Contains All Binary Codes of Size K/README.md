# Check If a Binary String Contains All Codes of Size K

## Problem Statement

Given a binary string `s` and an integer `k`, return **true** if every possible binary code of length `k` exists as a substring of `s`. Otherwise, return **false**.

---

## Examples

### Example 1

**Input**
```
s = "00110110", k = 2
```

**Output**
```
true
```

**Explanation**

All possible binary codes of length 2 are:
```
00, 01, 10, 11
```
All are present in `s`.

---

### Example 2

**Input**
```
s = "0110", k = 1
```

**Output**
```
true
```

---

### Example 3

**Input**
```
s = "0110", k = 2
```

**Output**
```
false
```

`"00"` is missing.

---

## Constraints:

- 1 <= s.length <= 5 * 105
- s[i] is either '0' or '1'.
- 1 <= k <= 20

---
