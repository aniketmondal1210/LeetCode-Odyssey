# Equal Score String Split

## Problem Statement

You are given a string `s` consisting of lowercase English letters.

The **score** of a string is defined as the **sum of the positions** of its characters in the alphabet, where `'a' = 1`, `'b' = 2`, ..., `'z' = 26`.

Determine whether there exists an index `i` such that the string can be split into two non-empty substrings `s[0..i]` and `s[i+1..n-1]` having **equal scores**.

Return **true** if such a split exists, otherwise **false**.

---

## Input

* A lowercase English string `s`.

**Constraints:**

```
2 ≤ s.length ≤ 100
s consists of lowercase English letters.
```

---

## Output

Return `true` if there exists a valid split, otherwise `false`.

---

## Examples

### Example 1

**Input:**

```
s = "adcb"
```

**Output:**

```
true
```

**Explanation:**

```
Split at index 1 → "ad" | "cb"
Score("ad") = 1 + 4 = 5
Score("cb") = 3 + 2 = 5
Both sides are equal → return true
```

---

### Example 2

**Input:**

```
s = "bace"
```

**Output:**

```
false
```

**Explanation:**

```
No split produces equal scores.
```

---
