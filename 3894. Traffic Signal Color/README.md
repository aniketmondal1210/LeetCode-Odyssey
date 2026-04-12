# Traffic Signal State

## Problem Statement

You are given an integer `timer` representing the remaining time (in seconds) on a traffic signal.

Determine the current state of the signal based on the following rules:

- If `timer == 0` → `"Green"`
- If `timer == 30` → `"Orange"`
- If `30 < timer <= 90` → `"Red"`
- Otherwise → `"Invalid"`

---

# Examples

### Example 1

**Input**
```
timer = 60
```

**Output**
```
"Red"
```

---

### Example 2

**Input**
```
timer = 5
```

**Output**
```
"Invalid"
```

---

## Constraints:

- 0 <= timer <= 1000

---
