# Password Strength Calculation

## Problem Statement

Calculate the strength of the password using these rules:

- `1` point for each distinct lowercase letter
- `2` points for each distinct uppercase letter
- `3` points for each distinct digit
- `5` points for each distinct special character from `"!@#$"`

Each distinct character contributes only once.

---

# Example 1

```text
Input:
password = "aA1!"

Output:
11
```

### Explanation

```text
'a' -> 1 point
'A' -> 2 points
'1' -> 3 points
'!' -> 5 points

Total = 11
```

---

# Example 2

```text
Input:
password = "bbB11#"

Output:
11
```

### Explanation

```text
Distinct characters:
'b' -> 1
'B' -> 2
'1' -> 3
'#' -> 5

Total = 11
```

## Constraints:

- 1 <= password.length <= 10^5
- password consists of lowercase and uppercase English letters, digits, and special characters from "!@#$".

---
