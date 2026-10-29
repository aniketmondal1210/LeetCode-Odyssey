# Maximum Product of Word Lengths

## Problem Description

Given a string array `words`, return the maximum value of `length(word[i]) * length(word[j])` where the two words do not share common letters. If no such two words exist, return `0`.

---

## Examples

### Example 1
- **Input:** `words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]`
- **Output:** `16`
- **Explanation:** The two words can be `"abcw"` and `"xtfn"`. Their lengths are $4 \times 4 = 16$, and they do not share any common letters.

### Example 2
- **Input:** `words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]`
- **Output:** `4`
- **Explanation:** The two words can be `"ab"` and `"cd"`. Their lengths are $2 \times 2 = 4$.

### Example 3
- **Input:** `words = ["a", "aa", "aaa", "aaaa"]`
- **Output:** `0`
- **Explanation:** No such pair of words exists that does not share common letters.

---

## Constraints

- $2 \le \text{words.length} \le 1000$
- $1 \le \text{words}[i]\text{.length} \le 1000$
- `words[i]` consists only of lowercase English letters.

---
