# Shortest Distance in Circular String Array

## Problem Statement

You are given:

- A circular array `words`
- A string `target`
- A starting index `startIndex`

👉 You can move:
- **Forward** → `(i + 1) % n`
- **Backward** → `(i - 1 + n) % n`

Return the **minimum steps** required to reach any index where `words[i] == target`.

If target does not exist → return `-1`.

---

# Examples

### Example 1

**Input**
```
words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1
```

**Output**
```
1
```

---

### Example 2

**Input**
```
words = ["a","b","leetcode"]
target = "leetcode"
startIndex = 0
```

**Output**
```
1
```

---

### Example 3

**Input**
```
words = ["i","eat","leetcode"]
target = "ate"
startIndex = 0
```

**Output**
```
-1
```

---

## Constraints:

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] and target consist of only lowercase English letters.
- 0 <= startIndex < words.length

---
