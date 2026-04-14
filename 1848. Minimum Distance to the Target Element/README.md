# Minimum Distance to Target Index

## Problem Statement

You are given:

- An integer array `nums`
- An integer `target`
- An integer `start`

👉 Find an index `i` such that:
```
nums[i] == target
```

and the value:
```
abs(i - start)
```
is **minimum**.

Return this minimum distance.

---

# Examples

### Example 1

**Input**
```
nums = [1,2,3,4,5], target = 5, start = 3
```

**Output**
```
1
```

---

### Example 2

**Input**
```
nums = [1], target = 1, start = 0
```

**Output**
```
0
```

---

### Example 3

**Input**
```
nums = [1,1,1,1,1], target = 1, start = 0
```

**Output**
```
0
```

---

## Constraints:

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4
- 0 <= start < nums.length
- target is in nums.

---
