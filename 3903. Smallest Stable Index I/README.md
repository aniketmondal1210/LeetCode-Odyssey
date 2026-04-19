# Find Smallest Stable Index

## Problem Statement

You are given:

- An integer array `nums`
- An integer `k`

For each index `i`, define:

```
instability(i) = max(nums[0..i]) - min(nums[i..n-1])
```

👉 An index is **stable** if:
```
instability(i) <= k
```

Return the **smallest such index**, or `-1` if none exists.

---

# Examples

### Example 1

**Input**
```
nums = [5,0,1,4], k = 3
```

**Output**
```
3
```

---

### Example 2

**Input**
```
nums = [3,2,1], k = 1
```

**Output**
```
-1
```

---

### Example 3

**Input**
```
nums = [0], k = 0
```

**Output**
```
0
```

---

## Constraints:

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 10^9
- 0 <= k <= 10^9

---
