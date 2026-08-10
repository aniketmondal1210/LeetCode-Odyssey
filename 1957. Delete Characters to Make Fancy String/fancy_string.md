# Problem: Fancy String

## Problem Statement

A **fancy string** is a string where no **three consecutive characters are equal**.

Given a string `s`, delete the **minimum** possible number of characters from `s` to make it fancy.

Return the final string after the deletion.

It can be shown that the answer will always be **unique**.

---

## Example 1

**Input:**

```text
s = "leeetcode"
```

**Output:**

```text
"leetcode"
```

**Explanation:**

Remove one `'e'` from the first group of `'e'` characters to create:

```text
"leetcode"
```

No three consecutive characters are equal, so return `"leetcode"`.

---

## Example 2

**Input:**

```text
s = "aaabaaaa"
```

**Output:**

```text
"aabaa"
```

**Explanation:**

Remove one `'a'` from the first group of `'a'` characters:

```text
"aaabaaaa" -> "aabaaaa"
```

Then remove two `'a'` characters from the second group:

```text
"aabaaaa" -> "aabaa"
```

No three consecutive characters are equal, so return `"aabaa"`.

---

## Example 3

**Input:**

```text
s = "aab"
```

**Output:**

```text
"aab"
```

**Explanation:**

No three consecutive characters are equal, so no deletion is required.

---

## Approach

Traverse the string from left to right and build the result.

For each character:

1. Add the character to the result if the last two characters in the result are not the same as the current character.
2. If the last two characters are already equal to the current character, skip it.
3. Continue until the entire string has been processed.

This keeps at most two consecutive occurrences of the same character while deleting the minimum possible number of characters.

---

## Complexity

### Time Complexity

```text
O(n)
```

The string is traversed once.

### Auxiliary Space

```text
O(n)
```

The result string can contain up to `n` characters.

---

## Constraints

```text
1 <= s.length <= 10^5
```

`s` consists only of lowercase English letters.
