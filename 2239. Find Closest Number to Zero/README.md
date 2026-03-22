# Closest Number to Zero

## Problem Statement

Given an integer array **nums**, return the number that is:

1. **Closest to 0**
2. If multiple numbers have the same distance, return the **largest value**

---

# Examples

### Example 1

**Input**
```
nums = [-4,-2,1,4,8]
```

**Distances**
```
|-4| = 4
|-2| = 2
|1|  = 1
|4|  = 4
|8|  = 8
```

Closest → `1`

**Output**
```
1
```

---

### Example 2

**Input**
```
nums = [2,-1,1]
```

**Distances**
```
|2|  = 2
|-1| = 1
|1|  = 1
```

Tie between `-1` and `1`, choose **larger → 1**

**Output**
```
1
```

---

## Constraints:

- 1 <= n <= 1000
- -10^5 <= nums[i] <= 10^5

---
