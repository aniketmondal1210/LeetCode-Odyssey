# Key Changes

## Problem

You are given a **0-indexed string** `s` typed by a user.

Changing a key is defined as using a key different from the last used key. For example:

- `s = "ab"` has a change of key.
- `s = "bBBb"` does not have any change of key.

Return the **number of times the user had to change the key**.

### Note

Modifiers like `Shift` or `Caps Lock` are not counted as changing the key. For example, typing `'a'` followed by `'A'` is **not** considered a change of key.

## Examples

### Example 1

```text
Input: s = "aAbBcC"
Output: 2
```

**Explanation:**

- From `s[0] = 'a'` to `s[1] = 'A'`, there is no change of key.
- From `s[1] = 'A'` to `s[2] = 'b'`, there is a change of key.
- From `s[2] = 'b'` to `s[3] = 'B'`, there is no change of key.
- From `s[3] = 'B'` to `s[4] = 'c'`, there is a change of key.
- From `s[4] = 'c'` to `s[5] = 'C'`, there is no change of key.

### Example 2

```text
Input: s = "AaAaAaaA"
Output: 0
```

**Explanation:**

There is no change of key since only the letters `'a'` and `'A'` are pressed, which correspond to the same key.

## Constraints

- `1 <= s.length <= 100`
- `s` consists of only uppercase and lowercase English letters.
