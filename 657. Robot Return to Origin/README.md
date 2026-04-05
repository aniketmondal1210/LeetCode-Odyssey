# Robot Return to Origin

## Problem Statement

A robot starts at position:
```
(0, 0)
```

Given a string `moves` consisting of:
```
'U' → Up
'D' → Down
'L' → Left
'R' → Right
```

Determine whether the robot returns back to the **origin (0, 0)** after all moves.

---

# Examples

### Example 1

**Input**
```
moves = "UD"
```

**Movement**
```
U → (0, 1)
D → (0, 0)
```

**Output**
```
true
```

---

### Example 2

**Input**
```
moves = "LL"
```

**Movement**
```
L → (-1, 0)
L → (-2, 0)
```

**Output**
```
false
```

---

## Constraints:

- 1 <= moves.length <= 2 * 104
- moves only contains the characters 'U', 'D', 'L' and 'R'.

---
