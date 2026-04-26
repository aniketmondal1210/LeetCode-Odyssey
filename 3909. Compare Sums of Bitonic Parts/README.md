# Compare Sums in Bitonic Array

## Problem Statement

You are given a **bitonic array** `nums`.

👉 Split it into:

- **Ascending part** → from index `0` to peak (inclusive)  
- **Descending part** → from peak to `n-1` (inclusive)  

⚠️ Peak element is included in both parts.

---

## Return

```
0  → if ascending sum > descending sum  
1  → if descending sum > ascending sum  
-1 → if both sums are equal  
```

---

## Examples

### Example 1

**Input**
```
nums = [1,3,2,1]
```

**Output**
```
1
```

---

### Example 2

**Input**
```
nums = [2,4,5,2]
```

**Output**
```
0
```

---

### Example 3

**Input**
```
nums = [1,2,4,3]
```

**Output**
```
-1
```

---

## Constraints:

- 3 <= n == nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- nums is a bitonic array.

---
