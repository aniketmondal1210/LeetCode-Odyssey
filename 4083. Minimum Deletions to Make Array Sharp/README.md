# Minimum Deletions to Make Array Sharp

## Problem Description

You are given an integer array `nums`. You may delete any number of elements from `nums`. The remaining elements keep their original order.

The resulting array `a` is **sharp** if the bitwise XOR of every pair of adjacent elements is non-zero. That is, `a[i] XOR a[i + 1] != 0` for every index `i` such that `0 <= i < a.length - 1`. An array with at most one element is sharp.

Return the minimum number of deletions needed to make `nums` sharp.

---

## Examples

### Example 1
- **Input:** `nums = [1, 1, 2, 2, 2, 3]`
- **Output:** `3`
- **Explanation:** Deleting one `1` and two `2`s leaves `[1, 2, 3]`, where `1 XOR 2 == 3` and `2 XOR 3 == 1` are both non-zero.

### Example 2
- **Input:** `nums = [4, 4, 9, 4]`
- **Output:** `1`
- **Explanation:** Deleting either of the two `4`s leaves `[4, 9, 4]`, where adjacent XORs are non-zero.

---

## Constraints

- $2 \le 	{nums.length} \le 100$
- $1 \le 	{nums}[i] \le 100$

---
