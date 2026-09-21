# Count Intersecting Interval Pairs

## Problem Description

Given a 2D integer array `intervals` of $n$ elements, where `intervals[i] = [start_i, end_i]` represents a closed interval, return the **number of pairs of indices $(i, j)$** such that $0 \le i < j < n$ and `intervals[i]` and `intervals[j]` intersect.

Two intervals $[a, b]$ and $[c, d]$ **intersect** if they share at least one point in common:

$$\max(a, c) \le \min(b, d)$$

---

## Examples

### Example 1
- **Input:** `intervals = [[1, 2], [2, 3], [3, 4]]`
- **Output:** `2`
- **Explanation:**
  - `[1, 2]` and `[2, 3]` intersect at point `2`.
  - `[2, 3]` and `[3, 4]` intersect at point `3`.

### Example 2
- **Input:** `intervals = [[1, 5], [2, 4], [3, 6]]`
- **Output:** `3`
- **Explanation:**
  - `[1, 5]` and `[2, 4]` intersect.
  - `[1, 5]` and `[3, 6]` intersect.
  - `[2, 4]` and `[3, 6]` intersect.

### Example 3
- **Input:** `intervals = [[1, 2], [3, 4], [5, 6]]`
- **Output:** `0`
- **Explanation:** No pairs intersect.

---

## Constraints

- $2 \le n = 	ext{intervals.length} \le 100$
- `intervals[i] = [start_i, end_i]`
- $0 \le 	ext{start}_i \le 	ext{end}_i \le 100$

---
