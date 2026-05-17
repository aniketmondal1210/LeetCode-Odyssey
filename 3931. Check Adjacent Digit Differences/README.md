# Check Adjacent Digit Difference

## Problem Statement

Given a string `s` consisting of digits:

Return:

- `true` → if the absolute difference between every pair of adjacent digits is at most `2`
- `false` → otherwise

---

# Examples

### Example 1

```text
Input:
s = "132"

Output:
true
```

### Explanation

```text
|1 - 3| = 2
|3 - 2| = 1

Both differences are <= 2
```

---

### Example 2

```text
Input:
s = "129"

Output:
false
```

### Explanation

```text
|1 - 2| = 1
|2 - 9| = 7

7 > 2
So answer is false.
```

---

## Constraints:

- 2 <= s.length <= 100
- s consists only of digits.
 
---
