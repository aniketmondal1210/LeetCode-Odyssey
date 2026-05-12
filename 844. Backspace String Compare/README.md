# Backspace String Compare

## Problem Statement

Given two strings `s` and `t`:

- `#` represents a backspace character.
- Return `true` if both strings become equal after processing backspaces.
- Otherwise return `false`.

---

# Examples

### Example 1

```text
Input:
s = "ab#c"
t = "ad#c"

Output:
true
```

### Explanation

```text
"ab#c" -> "ac"
"ad#c" -> "ac"
```

Both are equal.

---

### Example 2

```text
Input:
s = "ab##"
t = "c#d#"

Output:
true
```

### Explanation

```text
Both become ""
```

---

### Example 3

```text
Input:
s = "a#c"
t = "b"

Output:
false
```

---

## Constraints:

- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.
 
## Follow up: Can you solve it in O(n) time and O(1) space?
