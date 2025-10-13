# Divide Array Into Equal Pairs

## Problem Statement

You are given an integer array `nums` consisting of `2 * n` integers.

You need to divide `nums` into `n` pairs such that:

1. Each element belongs to exactly one pair.
2. The elements in each pair are **equal**.

Return `true` if `nums` can be divided into `n` such pairs, otherwise return `false`.

---

## Input

An integer array `nums`.

**Constraints:**

```
nums.length == 2 * n
1 ≤ n ≤ 500
1 ≤ nums[i] ≤ 500
```

---

## Output

Return a boolean value — `True` if it’s possible to divide `nums` into equal pairs, else `False`.

---

## Examples

### Example 1

**Input:**

```
nums = [3, 2, 3, 2, 2, 2]
```

**Output:**

```
true
```

**Explanation:**

```
Total elements = 6 → n = 3
Possible pairs: (2,2), (2,2), (3,3)
All conditions satisfied → true
```

---

### Example 2

**Input:**

```
nums = [1, 2, 3, 4]
```

**Output:**

```
false
```

**Explanation:**

```
Cannot form equal pairs → false
```

---
