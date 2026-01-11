# Count Residue Prefixes

## Problem Statement
You are given a string `s` consisting only of lowercase English letters.

A **prefix** of `s` is a non-empty substring that starts from the beginning of the string.

A prefix is called a **residue** if:

number of distinct characters in the prefix == (length of the prefix) % 3


Your task is to **count how many prefixes of `s` are residues**.

---

## Examples

### Example 1
**Input:**

s = "abc"


**Output:**

2


**Explanation:**
- `"a"` → distinct = 1, length % 3 = 1 ✅
- `"ab"` → distinct = 2, length % 3 = 2 ✅
- `"abc"` → distinct = 3, length % 3 = 0 ❌  
✔ Total residue prefixes = **2**

---

### Example 2
**Input:**

s = "dd"


**Output:**

1


**Explanation:**
- `"d"` → distinct = 1, length % 3 = 1 ✅
- `"dd"` → distinct = 1, length % 3 = 2 ❌  
✔ Total residue prefixes = **1**

---

### Example 3
**Input:**

s = "bob"


**Output:**

2


**Explanation:**
- `"b"` → distinct = 1, length % 3 = 1 ✅
- `"bo"` → distinct = 2, length % 3 = 2 ✅
- `"bob"` → distinct = 2, length % 3 = 0 ❌  
✔ Total residue prefixes = **2**

---

## Constraints

- 1 ≤ s.length ≤ 100
- s contains only lowercase English letters


---
