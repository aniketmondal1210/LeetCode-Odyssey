# Most Frequent Even Element

## Problem Statement

Given an integer array **nums**, return the **most frequent even element**.

### Rules

1. Only consider **even numbers**.
2. If multiple elements have the same frequency:
   ```
   return the smallest one
   ```
3. If **no even element exists**, return:
   ```
   -1
   ```

---

# Examples

### Example 1

**Input**
```
nums = [0,1,2,2,4,4,1]
```

**Even Elements**
```
0, 2, 2, 4, 4
```

**Frequencies**
```
0 → 1
2 → 2
4 → 2
```

Tie between **2 and 4**, return **smallest**:

```
2
```

**Output**
```
2
```

---

### Example 2

**Input**
```
nums = [4,4,4,9,2,4]
```

**Frequencies**
```
4 → 4 times
2 → 1 time
```

**Output**
```
4
```

---

### Example 3

**Input**
```
nums = [29,47,21,41,13,37,25,7]
```

No even numbers:

```
-1
```

---

## Constraints:

- 1 <= nums.length <= 2000
- 0 <= nums[i] <= 10^5

---
