# Remove Stars from String

## Problem Statement

Given a string `s` containing lowercase letters and `*`:

For every `*`:
- Remove the **closest non-star character to its left**
- Remove the `*` itself

Return the final string after all stars are removed.

---

# Examples

### Example 1

**Input**
```
s = "leet**cod*e"
```

**Process**
```
leet**cod*e
→ remove 't' → lee*cod*e
→ remove 'e' → lecod*e
→ remove 'd' → lecoe
```

**Output**
```
lecoe
```

---

### Example 2

**Input**
```
s = "erase*****"
```

**Process**
```
erase → completely removed
```

**Output**
```
""
```

---

## Constraints:

- 1 <= s.length <= 10^5
- s consists of lowercase English letters and stars *.
- The operation above can be performed on s.

---
