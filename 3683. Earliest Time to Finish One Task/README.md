# Earliest Task Finish Time

## Problem Statement

You are given a 2D array `tasks` where:

```
tasks[i] = [si, ti]
```

- `si` → start time  
- `ti` → time taken  

Each task finishes at:
```
finish time = si + ti
```

Return the **earliest finish time** among all tasks.

---

# Examples

### Example 1

**Input**
```
tasks = [[1,6],[2,3]]
```

**Finish Times**
```
1 + 6 = 7
2 + 3 = 5
```

**Earliest = 5**

**Output**
```
5
```

---

### Example 2

**Input**
```
tasks = [[100,100],[100,100],[100,100]]
```

**Finish Times**
```
100 + 100 = 200
```

**Output**
```
200
```

---

## Constraints:

- 1 <= tasks.length <= 100
- tasks[i] = [si, ti]
- 1 <= si, ti <= 100

---
