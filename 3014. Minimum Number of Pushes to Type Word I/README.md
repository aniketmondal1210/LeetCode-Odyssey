# Minimum Number of Pushes to Type Word I

## Problem Statement

You are given a string `word` containing **distinct lowercase English letters**.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key `2` is mapped with `["a","b","c"]`, where:

- Press once → `a`
- Press twice → `b`
- Press three times → `c`

You are allowed to **remap** the letters to keys numbered `2` to `9` (8 keys total). Each letter must be assigned to exactly one key, and each key can contain any number of letters.

Return the **minimum number of key presses** required to type `word`.

---

## Examples

### Example 1

**Input:**
```text
word = "abcde"
```

**Output:**
```text
5
```

**Explanation:**

Assign each letter to a different key as the first letter on that key.

- a → 1 push
- b → 1 push
- c → 1 push
- d → 1 push
- e → 1 push

Total = **5**

---

### Example 2

**Input:**
```text
word = "xycdefghij"
```

**Output:**
```text
12
```

**Explanation:**

There are 10 distinct letters.

- First 8 letters can occupy the first position of the 8 keys → 8 pushes.
- Remaining 2 letters occupy the second position → 2 pushes each.

Total = **8 + 2 + 2 = 12**

---

## Constraints:

- 1 <= word.length <= 26
- word consists of lowercase English letters.
- All letters in word are distinct.

---
