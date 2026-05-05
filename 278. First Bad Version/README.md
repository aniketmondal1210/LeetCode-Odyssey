# First Bad Version

## Problem Statement

You have versions:
```
[1, 2, 3, ..., n]
```

👉 There exists a version `bad` such that:
```
All versions ≥ bad are BAD
```

👉 You are given API:
```
bool isBadVersion(version)
```

👉 Find the **first bad version** with **minimum API calls**

---

# Examples

### Example 1
```
Input:  n = 5, bad = 4
Output: 4
```

---

### Example 2
```
Input:  n = 1, bad = 1
Output: 1
```

---

## Constraints:

- 1 <= bad <= n <= 2^31 - 1

---
