# Make Strings Equal with Distance-2 Swaps

## Problem Statement

You are given two strings `s1` and `s2` of length **4**.

You can perform the operation:
```
Swap characters at indices i and j such that (j - i = 2)
```

Return:
```
true  → if s1 can be converted to s2  
false → otherwise
```

---

# Key Insight

Allowed swaps:
```
(0 ↔ 2) and (1 ↔ 3)
```

So positions are divided into **2 independent groups**:
```
Group 1 → indices [0, 2]
Group 2 → indices [1, 3]
```

You can only rearrange characters **within the same group**.

---

# Condition to be TRUE

For both strings:

```
Characters at indices (0,2) must match (order doesn't matter)
Characters at indices (1,3) must match (order doesn't matter)
```

---

# Examples

### Example 1

**Input**
```
s1 = "abcd"
s2 = "cdab"
```

Group comparison:
```
s1 → (a,c) and (b,d)
s2 → (c,a) and (d,b)
```

Both groups match → TRUE

**Output**
```
true
```

---

### Example 2

**Input**
```
s1 = "abcd"
s2 = "dacb"
```

Group mismatch → FALSE

**Output**
```
false
```

---

## Constraints:

- s1.length == s2.length == 4
- s1 and s2 consist only of lowercase English letters.

---
