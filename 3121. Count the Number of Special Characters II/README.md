# Count Special Letters in a String

## Problem Statement

A letter is called **special** if:

- It appears in both lowercase and uppercase.
- Every lowercase occurrence appears before the first uppercase occurrence.

Return the number of special letters in the string.

---

# Example 1

```text
Input:
word = "aaAbcBC"

Output:
3
```

### Explanation

```text
'a' -> lowercase appears before uppercase 'A'
'b' -> lowercase appears before uppercase 'B'
'c' -> lowercase appears before uppercase 'C'
```

So answer = 3.

---

# Example 2

```text
Input:
word = "abc"

Output:
0
```

### Explanation

```text
No uppercase letters exist.
```

---

# Example 3

```text
Input:
word = "AbBCab"

Output:
0
```

### Explanation

```text
Lowercase letters appear after uppercase letters,
so they are not special.
```

---

## Constraints:

- 1 <= word.length <= 2 * 10^5
- word consists of only lowercase and uppercase English letters.

---
