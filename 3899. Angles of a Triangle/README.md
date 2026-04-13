# Triangle Angles from Given Sides

## Problem Statement

You are given an array `sides` of length 3.

👉 Determine:
- If a **valid triangle** can be formed (positive area)
- If yes → return the **3 internal angles (in degrees)** sorted in **non-decreasing order**
- Otherwise → return an empty array

---

# Triangle Validity Condition

A triangle exists **only if**:

```
a + b > c
b + c > a
a + c > b
```

---

# Examples

### Example 1

**Input**
```
sides = [3, 4, 5]
```

**Output**
```
[36.86990, 53.13010, 90.00000]
```

---

### Example 2

**Input**
```
sides = [2, 4, 2]
```

**Output**
```
[]
```

---

## Constraints:

- sides.length == 3
- 1 <= sides[i] <= 1000

---
