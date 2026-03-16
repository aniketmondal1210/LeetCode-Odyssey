# Smallest Absent Positive Integer Greater Than Average

## Problem Statement

Given an integer array **nums**, return the **smallest positive integer** that:

1. Is **not present in the array**.
2. Is **strictly greater than the average** of the array.

### Average Formula

```
average = sum of all elements / number of elements
```
---

# Examples

### Example 1

**Input**
```
nums = [3,5]
```

**Average**
```
(3 + 5) / 2 = 4
```

Numbers greater than **4**:
```
5, 6, 7...
```

But **5 exists**, so the smallest absent positive integer is:

```
6
```

**Output**
```
6
```

---

### Example 2

**Input**
```
nums = [-1,1,2]
```

**Average**
```
(-1 + 1 + 2) / 3 = 0.667
```

Positive integers greater than **0.667**:
```
1,2,3...
```

But:
```
1 exists
2 exists
3 does not exist
```

**Output**
```
3
```

---

### Example 3

**Input**
```
nums = [4,-1]
```

**Average**
```
(4 + (-1)) / 2 = 1.5
```

Positive integers greater than **1.5**:
```
2,3,4...
```

```
2 does not exist
```

**Output**
```
2
```

---

## Constraints:

- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100​​​​​​​

---
