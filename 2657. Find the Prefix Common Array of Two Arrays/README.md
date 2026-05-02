# Prefix Common Array of Two Permutations

## Problem Statement

You are given two permutations:
- `A`
- `B`

👉 Both contain numbers from `1` to `n` exactly once

---

## Goal

Create array `C` such that:

```
C[i] = count of numbers present in BOTH
       A[0..i] and B[0..i]
```

---

# Examples

### Example 1
```
Input:
A = [1,3,2,4]
B = [3,1,2,4]

Output:
[0,2,3,4]
```

---

### Example 2
```
Input:
A = [2,3,1]
B = [3,1,2]

Output:
[0,1,3]
```

---

## Constraints:

- 1 <= A.length == B.length == n <= 50
- 1 <= A[i], B[i] <= n
- It is guaranteed that A and B are both a permutation of n integers.

---
