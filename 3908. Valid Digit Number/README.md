# Valid Number Based on Digit Condition

## Problem Statement

You are given:
- An integer `n`
- A digit `x`

A number is **valid** if:

1. It contains **at least one occurrence** of digit `x`
2. It **does NOT start** with digit `x`

👉 Return `true` if valid, else `false`

---

# Examples

### Example 1

**Input**
```
n = 101, x = 0
```

**Output**
```
true
```

---

### Example 2

**Input**
```
n = 232, x = 2
```

**Output**
```
false
```

---

### Example 3

**Input**
```
n = 5, x = 1
```

**Output**
```
false
```

---

## Constraints:

- 0 <= n <= 10^5​​​​​​​
- 0 <= x <= 9

---
