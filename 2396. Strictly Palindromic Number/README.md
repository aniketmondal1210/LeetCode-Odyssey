# Strictly Palindromic Number

## Problem Statement

An integer `n` is **strictly palindromic** if, for every base `b` between **2** and **n - 2** (inclusive), the string representation of `n` in base `b` is palindromic.

Return `true` if `n` is strictly palindromic and `false` otherwise.

A string is **palindromic** if it reads the same forward and backward.

---

## Input

An integer `n`.

**Constraints:**

```
4 ≤ n ≤ 10^5
```

---

## Output

Return `true` if `n` is strictly palindromic, otherwise `false`.

---

## Examples

### Example 1

**Input:**

```
n = 9
```

**Output:**

```
false
```

**Explanation:**

```
Base 2:  9 = 1001  → Palindromic
Base 3:  9 = 100   → Not Palindromic
Hence, 9 is not strictly palindromic.
```

---

### Example 2

**Input:**

```
n = 4
```

**Output:**

```
false
```

**Explanation:**

```
Base 2:  4 = 100  → Not Palindromic
Therefore, 4 is not strictly palindromic.
```

---
