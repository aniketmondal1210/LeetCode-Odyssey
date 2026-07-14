# Sort Array by Increasing Frequency

## Problem

Given an integer array `nums`, sort the array according to the following rules:

1. Sort by **frequency in increasing order**.
2. If two numbers have the same frequency, sort them by **value in decreasing order**.

Return the sorted array.

---

## Examples

### Example 1

**Input**

```text
nums = [1,1,2,2,2,3]
```

**Output**

```text
[3,1,1,2,2,2]
```

**Explanation**

Frequencies:

```text
3 → 1
1 → 2
2 → 3
```

Numbers with smaller frequencies come first.

---

### Example 2

**Input**

```text
nums = [2,3,1,3,2]
```

**Output**

```text
[1,3,3,2,2]
```

**Explanation**

Frequencies:

```text
1 → 1
2 → 2
3 → 2
```

Since `2` and `3` have the same frequency, the larger value (`3`) comes first.

---

### Example 3

**Input**

```text
nums = [-1,1,-6,4,5,-6,1,4,1]
```

**Output**

```text
[5,-1,4,4,-6,-6,1,1,1]
```

**Explanation**

Frequencies:

```text
5  → 1
-1 → 1
4  → 2
-6 → 2
1  → 3
```

For equal frequencies:

- `5 > -1`, so `5` comes first.
- `4 > -6`, so `4` comes before `-6`.

---

## Constraints:

- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100

---
