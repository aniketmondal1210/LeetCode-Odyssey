# Find Words That Can Be Formed by Characters

## Problem Description

You are given an array of strings `words` and a string `chars`.

A string in `words` is considered **good** if it can be formed using the characters from `chars` (each character in `chars` can only be used once per word).

Return the **sum of lengths** of all good strings in `words`.

---

## Examples

### Example 1
- **Input:** `words = ["cat", "bt", "hat", "tree"]`, `chars = "atach"`
- **Output:** `6`
- **Explanation:** 
  - `"cat"` can be formed using characters from `"atach"`. Length = 3.
  - `"bt"` cannot be formed (missing `'b'`).
  - `"hat"` can be formed. Length = 3.
  - `"tree"` cannot be formed (missing `'r'`, `'e'`).
  - Total length = $3 + 3 = 6$.

### Example 2
- **Input:** `words = ["hello", "world", "leetcode"]`, `chars = "welldonehoneyr"`
- **Output:** `10`
- **Explanation:** 
  - `"hello"` and `"world"` can both be formed.
  - Total length = $5 + 5 = 10$.

---

## Constraints

- $1 \le \text{words.length} \le 1000$
- $1 \le \text{words}[i].\text{length}, \text{chars.length} \le 100$
- `words[i]` and `chars` consist of lowercase English letters.

---
