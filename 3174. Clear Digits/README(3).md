# Remove Digits

## Problem Statement

You are given a string `s`.

Your task is to remove **all** digits by repeatedly performing the following operation:

- Delete the **first digit** and the **closest non-digit character to its left**.

Return the resulting string after removing all digits.

### Note

The operation cannot be performed on a digit that does not have any non-digit character to its left.

The input is guaranteed to be such that all digits can be deleted.

---

## Example 1

**Input:**

```text
s = "abc"
```

**Output:**

```text
"abc"
```

**Explanation:**

There are no digits in the string, so no operations are performed.

Therefore, the resulting string is:

```text
"abc"
```

---

## Example 2

**Input:**

```text
s = "cb34"
```

**Output:**

```text
""
```

**Explanation:**

First, we apply the operation to the first digit `3`.

The closest non-digit character to its left is `b`.

```text
"cb34" -> "c4"
```

Next, we apply the operation to the digit `4`.

The closest non-digit character to its left is `c`.

```text
"c4" -> ""
```

Therefore, the resulting string is an empty string.

---

## Constraints

```text
1 <= s.length <= 100
```

`s` consists only of lowercase English letters and digits.

The input is generated such that it is possible to delete all digits.
