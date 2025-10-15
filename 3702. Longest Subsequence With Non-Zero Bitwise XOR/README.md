# Longest Subsequence with Non-Zero XOR

## Problem Statement

You are given an integer array `nums`.

Your task is to find the **length of the longest subsequence** whose **bitwise XOR** is **non-zero**. If no such subsequence exists, return `0`.

---

## Input

* An integer array `nums`.

**Constraints:**

```
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
```

---

## Output

Return an integer representing the length of the longest subsequence whose XOR is non-zero.

---

## Examples

### Example 1

**Input:**

```
nums = [1, 2, 3]
```

**Output:**

```
2
```

**Explanation:**

```
One longest subsequence is [2, 3].
2 XOR 3 = 1 (non-zero)
```

---

### Example 2

**Input:**

```
nums = [2, 3, 4]
```

**Output:**

```
3
```

**Explanation:**

```
The longest subsequence is [2, 3, 4].
2 XOR 3 XOR 4 = 5 (non-zero)
```

---
