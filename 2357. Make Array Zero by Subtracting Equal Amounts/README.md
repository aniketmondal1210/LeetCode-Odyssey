# Minimum Operations to Make Array Zero

## Problem Statement

Given a non-negative integer array **nums**, in one operation:

1. Choose a positive integer **x** such that:
   ```
   x ≤ smallest non-zero element in nums
   ```
2. Subtract **x** from all **positive elements** in the array.

Return the **minimum number of operations** required to make all elements **0**.

---

# Examples

### Example 1

**Input**
```
nums = [1,5,0,3,5]
```

**Process**
```
Step 1: x = 1 → [0,4,0,2,4]
Step 2: x = 2 → [0,2,0,0,2]
Step 3: x = 2 → [0,0,0,0,0]
```

**Output**
```
3
```

---

### Example 2

**Input**
```
nums = [0]
```

**Output**
```
0
```

---

## Constraints:

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

---
