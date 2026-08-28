# Prefix and Suffix Pairs

## Problem

You are given a 0-indexed string array `words`.

Define a function `isPrefixAndSuffix(str1, str2)` that returns `true` if `str1` is both a prefix and a suffix of `str2`.

Return the number of index pairs `(i, j)` such that:

- `i < j`
- `words[i]` is both a prefix and a suffix of `words[j]`

## Examples

### Example 1

```text
Input: words = ["a","aba","ababa","aa"]
Output: 4
```

The valid pairs are:

```text
(0, 1)
(0, 2)
(0, 3)
(1, 2)
```

### Example 2

```text
Input: words = ["pa","papa","ma","mama"]
Output: 2
```

The valid pairs are:

```text
(0, 1)
(2, 3)
```

### Example 3

```text
Input: words = ["abab","ab"]
Output: 0
```

There are no valid pairs because `"abab"` cannot be a prefix and suffix of `"ab"`.

## Constraints

- `1 <= words.length <= 50`
- `1 <= words[i].length <= 10`
- `words[i]` consists only of lowercase English letters.
