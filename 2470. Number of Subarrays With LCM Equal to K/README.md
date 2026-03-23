# Count Subarrays with LCM = k

## Problem Statement

Given an array `nums` and integer `k`, return the number of **subarrays** whose **LCM (Least Common Multiple)** equals `k`.

---

# Examples

### Example 1

**Input**
```
nums = [3,6,2,7,1], k = 6
```

**Output**
```
4
```

**Explanation**

Valid subarrays:
```
[3,6]
[6]
[6,2]
[3,6,2]
```

---

### Example 2

**Input**
```
nums = [3], k = 2
```

**Output**
```
0
```

**Explanation**
No subarray has LCM = 2.

---

## Constraints:

- 1 <= nums.length <= 1000
- 1 <= nums[i], k <= 1000

---
