# Shuffle String

## Problem Statement

Given:
```
string s
array indices[]
```

Each character at index `i` in `s` should move to position `indices[i]`.

Return the shuffled string.

---

# Examples

### Example 1

**Input**
```
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
```

**Output**
```
"leetcode"
```

---

### Example 2

**Input**
```
s = "abc"
indices = [0,1,2]
```

**Output**
```
"abc"
```

---

## Constraints:

- s.length == indices.length == n
- 1 <= n <= 100
- s consists of only lowercase English letters.
- 0 <= indices[i] < n
- All values of indices are unique.

---
