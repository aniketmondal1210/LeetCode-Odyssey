# Minimize String Length

## Problem

Given a string `s`, you have two types of operation:

1. Choose an index `i` in the string, and let `c` be the character in position `i`. Delete the closest occurrence of `c` to the left of `i` (if it exists).
2. Choose an index `i` in the string, and let `c` be the character in position `i`. Delete the closest occurrence of `c` to the right of `i` (if it exists).

Your task is to minimize the length of `s` by performing the above operations zero or more times.

Return an integer denoting the length of the minimized string.

## Examples

### Example 1

```text
Input: s = "aaabc"
Output: 3
```

Explanation:

1. Operation 2: choose `i = 1`, so `c` is `'a'`. Remove `s[2]`, the closest `'a'` to the right of `s[1]`.
   `s` becomes `"aabc"`.
2. Operation 1: choose `i = 1`, so `c` is `'a'`. Remove `s[0]`, the closest `'a'` to the left of `s[1]`.
   `s` becomes `"abc"`.

### Example 2

```text
Input: s = "cbbd"
Output: 3
```

Explanation:

1. Operation 1: choose `i = 2`, so `c` is `'b'`. Remove `s[1]`, the closest `'b'` to the left.
   `s` becomes `"cbd"`.

### Example 3

```text
Input: s = "baadccab"
Output: 4
```

Explanation:

1. Operation 1: choose `i = 6`, so `c` is `'a'`. Remove `s[2]`, the closest `'a'` to the left.
   `s` becomes `"badccab"`.
2. Operation 2: choose `i = 0`, so `c` is `'b'`. Remove `s[6]`, the closest `'b'` to the right.
   `s` becomes `"badcca"`.
3. Operation 2: choose `i = 3`, so `c` is `'c'`. Remove `s[4]`, the closest `'c'` to the right.
   `s` becomes `"badca"`.
4. Operation 1: choose `i = 4`, so `c` is `'a'`. Remove `s[1]`, the closest `'a'` to the left.
   `s` becomes `"bdca"`.

## Constraints

- `1 <= s.length <= 100`
- `s` contains only lowercase English letters.
