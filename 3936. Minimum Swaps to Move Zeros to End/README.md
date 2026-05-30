# Minimum Operations to Move All Zeros to the End

## Problem Statement

Given an integer array `nums`, in one operation you can swap any two distinct indices.

Return the **minimum number of swaps** required to move all `0`s to the end of the array.

---

# Key Observation

Let:

- `k` = number of zeros in the array.
- In the final array, the last `k` positions must all contain zeros.

Every zero that is **not already in the last `k` positions** must be moved there.

A single swap can place exactly one such misplaced zero into its correct region.

Therefore:

```text
Minimum swaps =
Number of zeros outside the last k positions
```

---

# Example 1

## Input

```text
nums = [0,1,0,3,12]
```

### Analysis

```text
Number of zeros = 2

Last 2 positions:
[3,12]

Zeros in last 2 positions = 0

Misplaced zeros = 2
```

## Output

```text
2
```

---

# Example 2

## Input

```text
nums = [0,1,0,2]
```

### Analysis

```text
Number of zeros = 2

Last 2 positions:
[0,2]

Zeros already there = 1

Misplaced zeros = 2 - 1 = 1
```

## Output

```text
1
```

---

# Example 3

## Input

```text
nums = [1,2,0]
```

### Analysis

```text
Number of zeros = 1

Last 1 position:
[0]

Zero already at the end.
```

## Output

```text
0
```

---

## Constraints:

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

---
