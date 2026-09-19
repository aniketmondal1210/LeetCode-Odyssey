# Top K Frequent Words

## Problem Description

Given an array of strings `words` and an integer `k`, return the `k` **most frequent strings**.

Return the answer sorted by **frequency from highest to lowest**. If multiple words have the same frequency, sort them by their **lexicographical (alphabetical) order**.

---

## Examples

### Example 1
- **Input:** `words = ["i", "love", "leetcode", "i", "love", "coding"]`, `k = 2`
- **Output:** `["i", "love"]`
- **Explanation:** `"i"` and `"love"` are the two most frequent words (frequency of 2 each). `"i"` comes before `"love"` due to a lower alphabetical order.

### Example 2
- **Input:** `words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]`, `k = 4`
- **Output:** `["the", "is", "sunny", "day"]`
- **Explanation:** `"the"`, `"is"`, `"sunny"`, and `"day"` are the four most frequent words, with frequencies 4, 3, 2, and 1 respectively.

---

## Constraints

- $1 \le {words.length} \le 500$
- $1 \le {words}[i].length \le 10$
- `words[i]` consists of lowercase English letters.
- $k$ is in the range $[1, \text{number of unique words}]$.

---
