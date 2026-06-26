# Find Common Characters

## Problem

Given an array of strings `words`, return an array containing **all characters that appear in every string**, including duplicates.

If a character appears `k` times in **every** string, it should appear `k` times in the answer.

The order of the returned characters does not matter.

---

## Example 1

### Input

```text
words = ["bella", "label", "roller"]
```

### Output

```text
["e", "l", "l"]
```

### Explanation

Character frequencies:

| Character | bella | label | roller | Minimum |
|-----------|:-----:|:-----:|:------:|:-------:|
| e | 1 | 1 | 1 | 1 |
| l | 2 | 2 | 2 | 2 |
| a | 1 | 1 | 0 | 0 |
| b | 1 | 1 | 0 | 0 |
| r | 0 | 0 | 2 | 0 |
| o | 0 | 0 | 1 | 0 |

Common characters:

```text
e, l, l
```

---

## Example 2

### Input

```text
words = ["cool", "lock", "cook"]
```

### Output

```text
["c", "o"]
```

### Explanation

Only `'c'` and `'o'` appear in every string.

---

## Constraints:

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters.

---
