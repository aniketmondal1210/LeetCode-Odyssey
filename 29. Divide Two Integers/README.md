# Divide Two Integers (Without *, /, %)

## Problem Statement

Given two integers:
- `dividend`
- `divisor`

👉 Perform division **without using**:
```
*, /, %
```

👉 Return:
```
quotient (truncate toward zero)
```

---

## Constraints Handling

- 32-bit range:
```
[-2^31, 2^31 - 1]
```

- Overflow case:
```
dividend = INT_MIN (-2^31)
divisor = -1
→ return INT_MAX (2^31 - 1)
```

---

# Examples

### Example 1
```
Input:  dividend = 10, divisor = 3
Output: 3
```

---

### Example 2
```
Input:  dividend = 7, divisor = -3
Output: -2
```

---

## Constraints:

- -2^31 <= dividend, divisor <= 2^31 - 1
- divisor != 0

---
