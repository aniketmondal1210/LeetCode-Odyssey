# Remove All Trailing Vowels

## Problem Statement

Given a string `s` consisting of lowercase English letters, return the string obtained after removing **all trailing vowels**.

Vowels are:
```
a, e, i, o, u
```

Trailing vowels mean vowels appearing at the **end** of the string.

---

## Constraints

```
1 <= s.length <= 100
s consists only of lowercase English letters.
```

---

## Examples

### Example 1

**Input**
```
s = "idea"
```

**Output**
```
"id"
```

**Explanation**

Trailing vowels: `"e"` and `"a"`  
After removing them → `"id"`

---

### Example 2

**Input**
```
s = "day"
```

**Output**
```
"day"
```

**Explanation**

No trailing vowels → string remains unchanged.

---

### Example 3

**Input**
```
s = "aeiou"
```

**Output**
```
""
```

**Explanation**

All characters are trailing vowels → result is empty string.

---


## Constraints:

- 1 <= s.length <= 100
- s consists of only lowercase English letters.

---
