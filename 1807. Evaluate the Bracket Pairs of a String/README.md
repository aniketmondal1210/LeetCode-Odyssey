# Evaluate the Bracket Pairs of a String

## Problem Description

You are given a string `s` that contains some bracket pairs, where each pair contains a non-empty key (e.g., `"(name)is(age)yearsold"`).

You are also given a 2D string array `knowledge`, where each `knowledge[i] = [key_i, value_i]` indicates that the key `key_i` has a value of `value_i`.

Your task is to evaluate all of the bracket pairs in `s`:
- Replace `key_i` and its surrounding brackets `(...)` with its corresponding `value_i`.
- If the key is not present in `knowledge`, replace `(key_i)` with a question mark `?`.
- Each key appears at most once in `knowledge`.
- There are no nested brackets in `s`.

Return the resulting string after evaluating all bracket pairs.

---

## Examples

### Example 1
- **Input:** `s = "(name)is(age)yearsold"`, `knowledge = [["name","bob"],["age","two"]]`
- **Output:** `"bobistwoyearsold"`
- **Explanation:**
  - `"(name)"` $\rightarrow$ `"bob"`
  - `"(age)"` $\rightarrow$ `"two"`

### Example 2
- **Input:** `s = "hi(name)"`, `knowledge = [["a","b"]]`
- **Output:** `"hi?"`
- **Explanation:** Key `"name"` is not present in `knowledge`, so `"(name)"` is replaced with `"?"`.

### Example 3
- **Input:** `s = "(a)(a)(a)aaa"`, `knowledge = [["a","yes"]]`
- **Output:** `"yesyesyesaaa"`
- **Explanation:** All occurrences of `"(a)"` are replaced with `"yes"`. Unbracketed `"a"`s remain unchanged.

---

## Constraints

- $1 \le \text{s.length} \le 10^5$
- $0 \le \text{knowledge.length} \le 10^5$
- $\text{knowledge}[i].\text{length} == 2$
- $1 \le \text{key}_i.\text{length}, \text{value}_i.\text{length} \le 10$
- `s` consists of lowercase English letters and round brackets `'('` and `')'`.
- Every `'('` in `s` has a corresponding closing `')'`.
- No nested brackets in `s`.
- Each key in `knowledge` is unique.

---
