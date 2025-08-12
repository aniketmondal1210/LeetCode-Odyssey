# Check if String is a Prefix String of Words

## Problem
Given a string `s` and an array of strings `words`, determine whether `s` is a **prefix string** of `words`.

A string `s` is a prefix string of `words` if `s` can be formed by concatenating the first **k** strings in `words` (for some positive `k` ≤ `words.length`).

Return `true` if `s` is a prefix string of `words`, otherwise return `false`.

---

## Examples

### Example 1
**Input:**

s = "iloveleetcode"
words = ["i", "love", "leetcode", "apples"]

**Output:**

true

**Explanation:**

s can be made by concatenating "i" + "love" + "leetcode".


---

### Example 2
**Input:**

s = "iloveleetcode"
words = ["apples", "i", "love", "leetcode"]

**Output:**

false

**Explanation:**

It's impossible to form s from the start of words.


---

## Constraints
- 1 ≤ `words.length` ≤ 100  
- 1 ≤ `words[i].length` ≤ 20  
- 1 ≤ `s.length` ≤ 1000  
- `words[i]` and `s` consist only of lowercase English letters.

---
