# Longest Uncommon Subsequence

## Problem Statement
Given two strings `a` and `b`, return the **length of the longest uncommon subsequence** between them.

An **uncommon subsequence** is a string that:
- Is a subsequence of **exactly one** of the two strings
- Is **not** a subsequence of the other string

If no such uncommon subsequence exists, return `-1`.

---

## Example 1
**Input:**

a = "aba"
b = "cdc"


**Output:**

3


**Explanation:**
- `"aba"` is a subsequence of `"aba"` but not `"cdc"`
- `"cdc"` is a subsequence of `"cdc"` but not `"aba"`
The longest uncommon subsequence has length 3.

---

## Example 2
**Input:**

a = "aaa"
b = "bbb"


**Output:**

3


**Explanation:**
Both `"aaa"` and `"bbb"` are uncommon subsequences.
The maximum length is 3.

---

## Example 3
**Input:**

a = "aaa"
b = "aaa"


**Output:**

-1


**Explanation:**
Every subsequence of `a` is also a subsequence of `b`, and vice versa.
Therefore, no uncommon subsequence exists.

---

## Constraints

- 1 ≤ a.length, b.length ≤ 100
- a and b consist of lowercase English letters


---
