# Permutation Difference Between Two Strings

## Problem Statement
You are given two strings **s** and **t** such that:
- Every character occurs **at most once** in `s`
- `t` is a **permutation** of `s`

The **permutation difference** between `s` and `t` is defined as:

> The sum of the absolute differences between the index of each character in `s` and the index of the same character in `t`.

Your task is to **return the permutation difference** between `s` and `t`.

---

## Examples

### Example 1
**Input:**

s = "abc"

t = "bac"


**Output:**

2


**Explanation:**

|index(a in s) - index(a in t)| = |0 - 1| = 1

|index(b in s) - index(b in t)| = |1 - 0| = 1

|index(c in s) - index(c in t)| = |2 - 2| = 0

Total = 1 + 1 + 0 = 2


---

### Example 2
**Input:**

s = "abcde"

t = "edbac"


**Output:**

12


**Explanation:**

|0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0|

= 3 + 1 + 2 + 2 + 4

= 12


---

## Constraints

- 1 <= s.length <= 26
- Each character occurs at most once in s
- t is a permutation of s
- s consists only of lowercase English letters


---
