# Centered Subarrays

## Problem Statement

You are given an integer array `nums`.

A **subarray** of `nums` is called **centered** if the **sum of its elements** is equal to **at least one element inside that same subarray**.

Return the **number of centered subarrays** in `nums`.

---

## Examples

### Example 1

**Input**
```
nums = [-1, 1, 0]
```

**Output**
```
5
```

**Explanation**

Centered subarrays:

```
[-1]        → sum = -1  (present in subarray)
[1]         → sum = 1   (present in subarray)
[0]         → sum = 0   (present in subarray)
[1, 0]      → sum = 1   (present in subarray)
[-1, 1, 0]  → sum = 0   (present in subarray)
```

Total = **5**

---

### Example 2

**Input**
```
nums = [2, -3]
```

**Output**
```
2
```

**Explanation**

Centered subarrays:

```
[2]
[-3]
```

Both single-element subarrays are centered.

---

## Constraints:

- 1 <= nums.length <= 500
- -10^5 <= nums[i] <= 10^5

---
