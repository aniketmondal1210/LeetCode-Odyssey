# Rearrange Array by Even & Odd Indices

## Problem Statement

Given a **0-indexed array `nums`**, rearrange it such that:

1. **Odd indices** → sorted in **non-increasing (descending)** order  
2. **Even indices** → sorted in **non-decreasing (ascending)** order  

Return the final array.

---

# Examples

### Example 1

**Input**
```
nums = [4,1,2,3]
```

**Step 1 (Odd indices → descending)**  
Indices: 1, 3 → values: 1, 3  
Sorted → 3, 1  

Array becomes:
```
[4,3,2,1]
```

**Step 2 (Even indices → ascending)**  
Indices: 0, 2 → values: 4, 2  
Sorted → 2, 4  

Final array:
```
[2,3,4,1]
```

**Output**
```
[2,3,4,1]
```

---

### Example 2

**Input**
```
nums = [2,1]
```

**Output**
```
[2,1]
```

---

## Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

---
