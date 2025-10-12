# Binary Substring Coverage

## Problem Statement

Given a binary string `s` and a positive integer `n`, return `true` if the **binary representations** of all integers in the range `[1, n]` are substrings of `s`. Otherwise, return `false`.

A **substring** is a contiguous sequence of characters within a string.

---

## Input

* A binary string `s`.
* A positive integer `n`.

**Constraints:**

```
1 ≤ s.length ≤ 1000
s[i] ∈ {'0', '1'}
1 ≤ n ≤ 10^9
```

---

## Output

Return `true` if all binary representations from `1` to `n` are substrings of `s`, else return `false`.

---

## Examples

### Example 1

**Input:**

```
s = "0110", n = 3
```

**Output:**

```
true
```

**Explanation:**

```
Binary representations:
1 → "1" ✓
2 → "10" ✓
3 → "11" ✓
All found in "0110".
```

---

### Example 2

**Input:**

```
s = "0110", n = 4
```

**Output:**

```
false
```

**Explanation:**

```
Binary representations:
1 → "1" ✓
2 → "10" ✓
3 → "11" ✓
4 → "100" ✗
"100" not found in "0110" → false
```

---
