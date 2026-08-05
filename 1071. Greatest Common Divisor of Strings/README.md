# Greatest Common Divisor of Strings

## Problem Statement

For two strings `s` and `t`, we say that **`t` divides `s`** if `s` can be formed by concatenating one or more copies of `t`.

Given two strings `str1` and `str2`, return the **largest string** `x` such that `x` divides both `str1` and `str2`.

If no such string exists, return an empty string `""`.

---

## Examples

### Example 1

**Input**

```text
str1 = "ABCABC"
str2 = "ABC"
```

**Output**

```text
"ABC"
```

**Explanation**

```text
"ABCABC" = "ABC" + "ABC"
"ABC"    = "ABC"
```

So, `"ABC"` divides both strings.

---

### Example 2

**Input**

```text
str1 = "ABABAB"
str2 = "ABAB"
```

**Output**

```text
"AB"
```

**Explanation**

```text
"ABABAB" = "AB" + "AB" + "AB"
"ABAB"   = "AB" + "AB"
```

---

### Example 3

**Input**

```text
str1 = "LEET"
str2 = "CODE"
```

**Output**

```text
""
```

**Explanation**

There is no common string that can repeatedly form both strings.

---

### Example 4

**Input**

```text
str1 = "AAAAAB"
str2 = "AAA"
```

**Output**

```text
""
```

---

## Constraints:

- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.

---
