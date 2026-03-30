# Smallest Index with Matching Mirror Character

## Problem Statement

Given a string `s` of length `n`, find the **smallest index `i`** such that:

```
s[i] == s[n - i - 1]
```

If no such index exists, return:
```
-1
```

---

# Examples

### Example 1

**Input**
```
s = "abcacbd"
```

**Check**
```
i = 0 → s[0] = 'a', s[6] = 'd' ❌
i = 1 → s[1] = 'b', s[5] = 'b' ✅
```

**Output**
```
1
```

---

### Example 2

**Input**
```
s = "abc"
```

**Check**
```
i = 0 → 'a' vs 'c' ❌
i = 1 → 'b' vs 'b' ✅
```

**Output**
```
1
```

---

### Example 3

**Input**
```
s = "abcdab"
```

No matching pair exists.

**Output**
```
-1
```

---

## Constraints:

- 1 <= n == s.length <= 100
- s consists of lowercase English letters.

---
