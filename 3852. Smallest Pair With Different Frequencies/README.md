# Smallest Pair with Different Frequencies

## Problem Statement

Given an integer array `nums`, find two **distinct values** `x` and `y` such that:

- `x < y`
- `freq(x) ≠ freq(y)`

Among all valid pairs:

1. Choose the pair with the **smallest possible x**
2. If multiple pairs have the same x, choose the one with the **smallest possible y**

Return:

```
[x, y]
```

If no such pair exists, return:

```
[-1, -1]
```

---

## Examples

### Example 1

**Input**
```
nums = [1,1,2,2,3,4]
```

**Output**
```
[1,3]
```

**Explanation**

Frequencies:
```
1 → 2
2 → 2
3 → 1
4 → 1
```

- Smallest value = 1 (frequency 2)
- Smallest value greater than 1 with different frequency = 3 (frequency 1)

Answer = `[1, 3]`

---

### Example 2

**Input**
```
nums = [1,5]
```

**Output**
```
[-1,-1]
```

Both have frequency 1 → no valid pair.

---

### Example 3

**Input**
```
nums = [7]
```

**Output**
```
[-1,-1]
```

Only one value → no valid pair.

---

## Constraints

```
1 <= nums.length <= 100
1 <= nums[i] <= 100
```

---
