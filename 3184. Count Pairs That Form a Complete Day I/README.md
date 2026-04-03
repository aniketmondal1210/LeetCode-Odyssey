# Count Pairs Forming Complete Days

## Problem Statement

Given an array `hours`, count pairs `(i, j)` such that:

```
i < j AND (hours[i] + hours[j]) % 24 == 0
```

A **complete day** = multiple of 24.

---

# Examples

### Example 1

**Input**
```
hours = [12,12,30,24,24]
```

**Valid Pairs**
```
(0,1) → 12 + 12 = 24
(3,4) → 24 + 24 = 48
```

**Output**
```
2
```

---

### Example 2

**Input**
```
hours = [72,48,24,3]
```

**After Mod 24**
```
[0, 0, 0, 3]
```

**Valid Pairs**
```
(0,1), (0,2), (1,2)
```

**Output**
```
3
```

---

# Key Idea

Instead of full values, use:
```
remainder = hours[i] % 24
```

We need:
```
(r1 + r2) % 24 == 0
```

So:
```
r2 = (24 - r1) % 24
```

---

## Constraints:

- 1 <= hours.length <= 100
- 1 <= hours[i] <= 10^9

---
