# Count Good Substrings of Length Three

## Problem Statement
A string is considered **good** if it contains **no repeated characters**.

You are given a string `s`.  
Your task is to return the **number of good substrings of length exactly 3** in `s`.

> **Note:**  
If the same substring appears multiple times, **each occurrence should be counted**.

A **substring** is a contiguous sequence of characters within a string.

---

## Examples

### Example 1
**Input:**

s = "xyzzaz"


**Output:**

1


**Explanation:**
Substrings of length 3 are:
- `"xyz"` → good
- `"yzz"` → not good (repeated `z`)
- `"zza"` → not good
- `"zaz"` → not good

Only `"xyz"` is a good substring.

---

### Example 2
**Input:**

s = "aababcabc"


**Output:**

4


**Explanation:**
Substrings of length 3 are:
- `"aab"` → not good
- `"aba"` → not good
- `"bab"` → not good
- `"abc"` → good
- `"bca"` → good
- `"cab"` → good
- `"abc"` → good

Total good substrings = **4**

---

## Constraints

- 1 <= s.length <= 100
- s consists of lowercase English letters

---
