# Mismatched Segments Between Two Strings

## Problem Description

Given two strings `s1` and `s2` of equal length `n`, a **mismatched segment** is a maximal contiguous index range `[l, r]` (`0 <= l <= r < n`) such that `s1[i] != s2[i]` for every `i` in `[l, r]`.

Return a list/array of pairs `[sub1, sub2]` for every mismatched segment in increasing order of starting index `l`, where `sub1 = s1[l..r]` and `sub2 = s2[l..r]`. If all characters match across both strings, return an empty list/array.

---

## Examples

### Example 1
- **Input:** `s1 = "earth"`, `s2 = "empty"`
- **Output:** `[["ar", "mp"], ["h", "y"]]`
- **Explanation:**
  - Indices `1..2`: `'a' != 'm'` and `'r' != 'p'` $\rightarrow$ `["ar", "mp"]`.
  - Index `4`: `'h' != 'y'` $\rightarrow$ `["h", "y"]`.
  - Indices `0` and `3` match (`'e' == 'e'` and `'t' == 't'`), separating the mismatched segments.

### Example 2
- **Input:** `s1 = "action"`, `s2 = "nation"`
- **Output:** `[["ac", "na"]]`
- **Explanation:** Indices `0..1` differ (`'a' != 'n'` and `'c' != 'a'`), while indices `2..5` (`"tion"`) match.

### Example 3
- **Input:** `s1 = "hot"`, `s2 = "hot"`
- **Output:** `[]`
- **Explanation:** No indices have differing characters, so no mismatched segments exist.

---

## Constraints

- $1 \le \text{s1.length} == \text{s2.length} \le 100$
- `s1` and `s2` consist only of lowercase English letters (`'a'`–`'z'`).

---
