# First Unique Even Integer in Array

## Problem Statement

Given an integer array **nums**, return the **first even integer** (earliest by index) that **appears exactly once**.

If no such integer exists, return:

```
-1
```

### Conditions

- An integer is **even** if it is divisible by **2**.
- The number must **appear exactly once** in the array.

---

# Examples

### Example 1

**Input**
```
nums = [3,4,2,5,4,6]
```

**Output**
```
2
```

**Explanation**

Even numbers:
```
4, 2, 4, 6
```

Frequency:

```
4 → 2 times
2 → 1 time
6 → 1 time
```

Both **2** and **6** appear once, but **2 occurs first**, so the answer is:

```
2
```

---

### Example 2

**Input**
```
nums = [4,4]
```

**Output**
```
-1
```

**Explanation**

```
4 appears twice
```

No even number appears exactly once.

---

## Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

---
