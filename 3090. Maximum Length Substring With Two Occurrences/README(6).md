# Maximum Length Substring With At Most Two Occurrences

## Problem Statement

Given a string `s`, return the **maximum** length of a substring such that it contains **at most two occurrences of each character**.

---

## Example 1

**Input:**

```text
s = "bcbbbcba"
```

**Output:**

```text
4
```

**Explanation:**

The following substring has a length of `4` and contains at most two occurrences of each character:

```text
"bcbb"
```

Therefore, the maximum valid length is:

```text
4
```

---

## Example 2

**Input:**

```text
s = "aaaa"
```

**Output:**

```text
2
```

**Explanation:**

The substring:

```text
"aa"
```

contains exactly two occurrences of `a`.

Any substring longer than `2` would contain more than two occurrences of `a`.

Therefore, the maximum valid length is:

```text
2
```

---

## Constraints

```text
2 <= s.length <= 100
```

`s` consists only of lowercase English letters.
