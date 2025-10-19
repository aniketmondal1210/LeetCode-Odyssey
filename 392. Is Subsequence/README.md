# Check if a String is a Subsequence of Another

## Problem Statement
You are given two strings `s` and `t`.  
Return **true** if `s` is a subsequence of `t`, or **false** otherwise.

A **subsequence** of a string is formed by deleting some (possibly none) characters from the original string without changing the order of the remaining characters.

---

## Input
- Two lowercase English strings `s` and `t`.

**Constraints:**

0 ≤ s.length ≤ 100

0 ≤ t.length ≤ 10⁴


---

## Output
- Return `true` if `s` is a subsequence of `t`.
- Return `false` otherwise.

---

## Explanation
- A subsequence must maintain the **relative order** of characters.
- You can skip characters in `t`, but you cannot rearrange them.

---

## Examples

### Example 1
**Input:**

s = "abc"
t = "ahbgdc"

**Output:**

true

**Explanation:**
Characters `a`, `b`, and `c` appear in order in `t`.

---

### Example 2
**Input:**

s = "axc"
t = "ahbgdc"

**Output:**

false

**Explanation:**
Character `x` does not appear after `a` in `t`.

---
