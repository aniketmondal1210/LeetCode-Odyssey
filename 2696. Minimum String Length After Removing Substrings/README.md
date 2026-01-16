# Minimum String Length After Removing Substrings

## Problem Statement
You are given a string `s` consisting only of **uppercase English letters**.

You can perform the following operation any number of times:

- Remove **any occurrence** of the substring `"AB"` or `"CD"` from the string.

After removing a substring, the remaining parts of the string are concatenated, which may form new `"AB"` or `"CD"` substrings.

Your task is to return the **minimum possible length** of the resulting string after performing optimal operations.

---

## Examples

### Example 1
**Input:**

s = "ABFCACDB"


**Output:**

2


**Explanation:**
Possible sequence of operations:
1. Remove `"AB"` → `FCACDB`
2. Remove `"CD"` → `FCAB`
3. Remove `"AB"` → `FC`

Final string length = **2**, which is the minimum possible.

---

### Example 2
**Input:**

s = "ACBBD"


**Output:**

5


**Explanation:**
There are no `"AB"` or `"CD"` substrings in the string, so no operations can be performed.
Final length remains **5**.

---

## Constraints

- 1 <= s.length <= 100
- s consists only of uppercase English letters


---
