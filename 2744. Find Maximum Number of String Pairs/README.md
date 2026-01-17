# Maximum Number of Reverse String Pairs

## Problem Statement
You are given a **0-indexed array `words`** consisting of **distinct strings**.

A pair `(i, j)` is considered **valid** if:
- `0 ≤ i < j < words.length`
- `words[i]` is equal to the **reverse** of `words[j]`
- Each string can be used in **at most one pair**

Return the **maximum number of such pairs** that can be formed.

---

## Examples

### Example 1
**Input:**

words = ["cd","ac","dc","ca","zz"]


**Output:**

2


**Explanation:**
- `"cd"` ↔ `"dc"`
- `"ac"` ↔ `"ca"`
- `"zz"` cannot be paired

Maximum pairs = **2**

---

### Example 2
**Input:**

words = ["ab","ba","cc"]


**Output:**

1


**Explanation:**
- `"ab"` ↔ `"ba"`
- `"cc"` has no reverse partner

Maximum pairs = **1**

---

### Example 3
**Input:**

words = ["aa","ab"]


**Output:**

0


**Explanation:**
No string has its reverse present.

---

## Constraints

- 1 ≤ words.length ≤ 50
- words[i].length = 2
- words contain only lowercase English letters
- All words are distinct


---
