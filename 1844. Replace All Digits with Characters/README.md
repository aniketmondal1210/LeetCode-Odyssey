# Replace Digits with Shifted Characters

## Problem Statement

Given a string `s`:
- **Even indices → lowercase letters**
- **Odd indices → digits**

Replace each digit at index `i` with:
```
shift(s[i-1], s[i])
```

Where:
- `shift(c, x)` → returns the character **x positions after `c`**

---

# Examples

### Example 1

**Input**
```
s = "a1c1e1"
```

**Steps**
```
s[1] → shift('a',1) = 'b'
s[3] → shift('c',1) = 'd'
s[5] → shift('e',1) = 'f'
```

**Output**
```
abcdef
```

---

### Example 2

**Input**
```
s = "a1b2c3d4e"
```

**Steps**
```
s[1] → shift('a',1) = 'b'
s[3] → shift('b',2) = 'd'
s[5] → shift('c',3) = 'f'
s[7] → shift('d',4) = 'h'
```

**Output**
```
abbdcfdhe
```

---

## Constraints:

- 1 <= s.length <= 100
- s consists only of lowercase English letters and digits.
- shift(s[i-1], s[i]) <= 'z' for all odd indices i.

---
