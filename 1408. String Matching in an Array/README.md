# String Matching in an Array

## Problem Description

Given an array of strings `words`, return all strings in `words` that are a substring of another word. You can return the answer in any order.

---

## Examples

### Example 1
- **Input:** `words = ["mass", "as", "hero", "superhero"]`
- **Output:** `["as", "hero"]`
- **Explanation:** `"as"` is a substring of `"mass"` and `"hero"` is a substring of `"superhero"`.

### Example 2
- **Input:** `words = ["leetcode", "et", "code"]`
- **Output:** `["et", "code"]`
- **Explanation:** `"et"` and `"code"` are substrings of `"leetcode"`.

### Example 3
- **Input:** `words = ["blue", "green", "bu"]`
- **Output:** `[]`
- **Explanation:** No string in `words` is a substring of another string.

---

## Constraints

- $1 \le 	{words.length} \le 100$
- $1 \le 	{words}[i].	{length} \le 30$
- `words[i]` contains only lowercase English letters.
- All the strings of `words` are unique.

---
