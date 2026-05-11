# Split a String in Balanced Strings

## Problem Statement

A balanced string contains an equal number of:

```text
'L' and 'R'
```

Given a balanced string `s`, split it into the maximum number of balanced substrings.

Return that maximum count.

---

# Examples

### Example 1

```text
Input:
s = "RLRRLLRLRL"

Output:
4
```

### Explanation

Possible split:

```text
"RL" | "RRLL" | "RL" | "RL"
```

Each substring has equal number of `L` and `R`.

---

### Example 2

```text
Input:
s = "RLRRRLLRLL"

Output:
2
```

### Explanation

Possible split:

```text
"RL" | "RRRLLRLL"
```

---

### Example 3

```text
Input:
s = "LLLLRRRR"

Output:
1
```

---

## Constraints:

- 2 <= s.length <= 1000
- s[i] is either 'L' or 'R'.
- s is a balanced string.

---
