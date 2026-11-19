# Check If a String Can Break Another String

## Problem Description

Given two strings `s1` and `s2` of the same size `n`, determine whether some permutation of `s1` can break some permutation of `s2`, or vice-versa.

A string `x` can break string `y` (both of length `n`) if `x[i] >= y[i]` in alphabetical order for every index `i` from `0` to `n - 1`.

---

## Examples

### Example 1
- **Input:** `s1 = "abc"`, `s2 = "xya"`
- **Output:** `true`
- **Explanation:** `"ayx"` is a permutation of `"xya"`, and for every index `i`, `'a' >= 'a'`, `'y' >= 'b'`, and `'x' >= 'c'`, so `"ayx"` breaks `"abc"`.

### Example 2
- **Input:** `s1 = "abe"`, `s2 = "acd"`
- **Output:** `false`
- **Explanation:** No permutation of `"abe"` dominates a permutation of `"acd"` at every index, and no permutation of `"acd"` dominates a permutation of `"abe"` at every index.

### Example 3
- **Input:** `s1 = "leetcodee"`, `s2 = "interview"`
- **Output:** `true`

---

## Constraints

- `s1.length == n`
- `s2.length == n`
- $1 \le n \le 10^5$
- Both strings consist only of lowercase English letters.

---
