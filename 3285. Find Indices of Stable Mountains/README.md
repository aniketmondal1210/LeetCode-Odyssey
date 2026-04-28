# Find Stable Mountains

## Problem Statement

You are given:
- An array `height[]`
- An integer `threshold`

A mountain `i` is **stable** if:

```
height[i - 1] > threshold
```

👉 Note:
- Index `0` is **never stable**

---

## Return

👉 A list of indices of all **stable mountains**

---

# Examples

### Example 1

**Input**
```
height = [1,2,3,4,5], threshold = 2
```

**Output**
```
[3,4]
```

---

### Example 2

**Input**
```
height = [10,1,10,1,10], threshold = 3
```

**Output**
```
[1,3]
```

---

### Example 3

**Input**
```
height = [10,1,10,1,10], threshold = 10
```

**Output**
```
[]
```

---

## Constraints:

- 2 <= n == height.length <= 100
- 1 <= height[i] <= 100
- 1 <= threshold <= 100

---
