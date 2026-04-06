# Mirror Frequency Difference

## Problem Statement

Given a string `s` of lowercase letters and digits:

- Each character has a **mirror**:
  - Letters:  
    ```
    'a' ↔ 'z', 'b' ↔ 'y', ...
    ```
  - Digits:  
    ```
    '0' ↔ '9', '1' ↔ '8', ...
    ```

For each **unique mirror pair (c, m)**:
```
Add |freq(c) - freq(m)|
```

⚠️ Count each pair **only once**

---

# Examples

### Example 1

**Input**
```
s = "ab1z9"
```

**Pairs & Calculation**
```
(a, z) → |1 - 1| = 0
(b, y) → |1 - 0| = 1
(1, 8) → |1 - 0| = 1
(9, 0) → |1 - 0| = 1
```

**Output**
```
3
```

---

### Example 2

**Input**
```
s = "4m7n"
```

**Output**
```
2
```

---

### Example 3

**Input**
```
s = "byby"
```

**Output**
```
0
```

---

## Constraints:

- 1 <= s.length <= 5 * 10^5
- s consists only of lowercase English letters and digits.

---
