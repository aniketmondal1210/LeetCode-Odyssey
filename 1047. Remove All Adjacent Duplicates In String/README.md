# Remove All Adjacent Duplicates in String

## Problem Statement

Given a string `s` consisting of lowercase English letters:

- Remove adjacent duplicate characters repeatedly.
- Continue until no adjacent duplicates remain.

Return the final string.

---

# Examples

### Example 1

```text
Input:
s = "abbaca"

Output:
"ca"
```

### Explanation

```text
abbaca
-> aaca   (remove "bb")
-> ca     (remove "aa")
```

---

### Example 2

```text
Input:
s = "azxxzy"

Output:
"ay"
```

### Explanation

```text
azxxzy
-> azzy   (remove "xx")
-> ay     (remove "zz")
```

---

## Constraints:

- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

---
