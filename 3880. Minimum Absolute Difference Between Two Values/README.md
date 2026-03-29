# Minimum Distance Between 1 and 2

## Problem Statement

Given an array `nums` containing only `0`, `1`, and `2`.

A pair `(i, j)` is **valid** if:
- `nums[i] == 1`
- `nums[j] == 2`

Return the **minimum absolute difference** `|i - j|` among all valid pairs.  
If no such pair exists, return `-1`.

---

## Examples

### Example 1

**Input**
```
nums = [1,0,0,2,0,1]
```

**Output**
```
2
```

**Explanation**
Valid pairs:
- (0,3) → distance = 3  
- (5,3) → distance = 2  

Minimum = 2

---

### Example 2

**Input**
```
nums = [1,0,1,0]
```

**Output**
```
-1
```

**Explanation**
No element `2` exists → no valid pair

---

## Constraints:

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 2

---
