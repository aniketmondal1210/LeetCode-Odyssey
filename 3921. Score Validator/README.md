# Cricket Events Score Calculator

## Problem Statement

You are given a string array `events`.

Initially:

```text
score = 0
counter = 0
```

Each event can be:

| Event | Action |
|------|------|
| `"0"` `"1"` `"2"` `"3"` `"4"` `"6"` | Add value to score |
| `"W"` | Increase counter by 1 |
| `"WD"` | Add 1 to score |
| `"NB"` | Add 1 to score |

Process events from left to right.

Stop when:
- all events are processed, OR
- `counter == 10`

Return:

```text
[score, counter]
```

---

# Examples

### Example 1

```text
Input:
events = ["1","4","W","6","WD"]

Output:
[12,1]
```

---

### Explanation

| Event | Score | Counter |
|---|---|---|
| "1" | 1 | 0 |
| "4" | 5 | 0 |
| "W" | 5 | 1 |
| "6" | 11 | 1 |
| "WD" | 12 | 1 |

Final Answer:

```text
[12,1]
```

---

### Example 2

```text
Input:
events = ["WD","NB","0","4","4"]

Output:
[10,0]
```

---

### Example 3

```text
Input:
events = ["W","W","W","W","W","W","W","W","W","W","W"]

Output:
[0,10]
```

---

# Constraints

```text
- 1 <= events.length <= 1000
- events[i] is one of "0", "1", "2", "3", "4", "6", "W", "WD", or "NB".
```

---
