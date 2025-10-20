# Count Number of Segments in a String

## Problem Statement
You are given a string `s`.  
Your task is to return the **number of segments** in the string.

A **segment** is defined as a contiguous sequence of **non-space characters**.

---

## Input
A single string `s` that may contain:
- Letters (uppercase or lowercase)
- Digits
- Symbols (`!@#$%^&*()_+-=',.:`)
- Spaces `' '`

**Constraints:**

0 ≤ s.length ≤ 300


---

## Output
Return an integer — the **number of segments** in the string.

---

## Explanation
Segments are words separated by **one or more spaces**.  
To count segments, simply split the string by spaces and count non-empty parts.

---

## Examples

### Example 1
**Input:**

s = "Hello, my name is John"

**Output:**

5

**Explanation:**
Segments are `["Hello,", "my", "name", "is", "John"]`.

---

### Example 2
**Input:**

s = "Hello"

**Output:**

1

**Explanation:**
Only one segment — `"Hello"`.

---
