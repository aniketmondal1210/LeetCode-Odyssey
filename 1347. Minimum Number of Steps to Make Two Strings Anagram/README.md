# Minimum Steps to Make Two Strings Anagrams

## Problem Statement

You are given two strings of the same length `s` and `t`.

In one step, you can choose **any character** of `t` and replace it with **another character**.

Return the **minimum number of steps** required to make `t` an anagram of `s`.

An **anagram** of a string is a string that contains the same characters with a different or the same ordering.

---

## Example 1

**Input:**

```text
s = "bab"
t = "aba"
```

**Output:**

```text
1
```

**Explanation:**

Replace the first `a` in `t` with `b`:

```text
"aba" -> "bba"
```

Now `"bba"` is an anagram of `"bab"`.

Therefore, the minimum number of steps is `1`.

---

## Example 2

**Input:**

```text
s = "leetcode"
t = "practice"
```

**Output:**

```text
5
```

**Explanation:**

The characters `p`, `r`, `a`, `i`, and `c` in `t` need to be replaced with appropriate characters to make `t` an anagram of `s`.

Therefore, the minimum number of steps is `5`.

---

## Example 3

**Input:**

```text
s = "anagram"
t = "mangaar"
```

**Output:**

```text
0
```

**Explanation:**

`"anagram"` and `"mangaar"` already contain the same characters with the same frequencies.

Therefore, they are already anagrams and no replacements are needed.

---

## Constraints

```text
1 <= s.length <= 5 * 10^4
s.length == t.length
```

`s` and `t` consist of lowercase English letters only.
