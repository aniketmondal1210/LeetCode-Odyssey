# Count Pairs Forming Target by Concatenation

## Problem Statement

Given an array of **digit strings `nums`** and a string `target`, return the number of pairs `(i, j)` such that:

```
i ≠ j
nums[i] + nums[j] == target
```

---

# Examples

### Example 1

**Input**
```
nums = ["777","7","77","77"]
target = "7777"
```

**Valid Pairs**
```
(0,1) → "777" + "7"
(1,0) → "7" + "777"
(2,3) → "77" + "77"
(3,2) → "77" + "77"
```

**Output**
```
4
```

---

### Example 2

**Input**
```
nums = ["123","4","12","34"]
target = "1234"
```

**Valid Pairs**
```
(0,1)
(2,3)
```

**Output**
```
2
```

---

### Example 3

**Input**
```
nums = ["1","1","1"]
target = "11"
```

All ordered pairs (i ≠ j):

```
6
```

---

## Constraints:

- 2 <= nums.length <= 100
- 1 <= nums[i].length <= 100
- 2 <= target.length <= 100
- nums[i] and target consist of digits.
- nums[i] and target do not have leading zeros.

---
