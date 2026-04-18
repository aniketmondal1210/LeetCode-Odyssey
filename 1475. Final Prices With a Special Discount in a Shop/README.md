# Final Prices With Special Discount

## Problem Statement

You are given an array `prices` where:

```
prices[i] = price of ith item
```

👉 For each item `i`, find the **next item `j` (j > i)** such that:
```
prices[j] <= prices[i]
```

If found:
```
final price = prices[i] - prices[j]
```

Otherwise:
```
final price = prices[i]
```

Return the final prices array.

---

# Examples

### Example 1

**Input**
```
prices = [8,4,6,2,3]
```

**Output**
```
[4,2,4,2,3]
```

---

### Example 2

**Input**
```
prices = [1,2,3,4,5]
```

**Output**
```
[1,2,3,4,5]
```

---

### Example 3

**Input**
```
prices = [10,1,1,6]
```

**Output**
```
[9,0,1,6]
```

---

## Constraints:

- 1 <= prices.length <= 500
- 1 <= prices[i] <= 1000

---
