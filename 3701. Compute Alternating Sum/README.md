# Alternating Sum of Array

## Problem Statement

You are given an integer array `nums`.

The **alternating sum** of `nums` is the value obtained by adding elements at even indices and subtracting elements at odd indices.

Formally, it is calculated as:

```
nums[0] - nums[1] + nums[2] - nums[3] + ...
```

Return an integer denoting the alternating sum of `nums`.

---

## Input

An integer array `nums`.

**Constraints:**

```
1 <= nums.length <= 100
1 <= nums[i] <= 100
```

---

## Output

Return the integer value representing the alternating sum of the array.

---

## Examples

### Example 1

**Input:**

```
nums = [1, 3, 5, 7]
```

**Output:**

```
-4
```

**Explanation:**

```
Even indices → nums[0] = 1, nums[2] = 5
Odd indices  → nums[1] = 3, nums[3] = 7
Alternating sum = 1 - 3 + 5 - 7 = -4
```

---

### Example 2

**Input:**

```
nums = [100]
```

**Output:**

```
100
```

**Explanation:**

```
Only one element at even index (0): 100
Alternating sum = 100
```

---
