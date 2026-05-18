# Valid Palindrome

## Problem Statement

A string is called a palindrome if:

- All uppercase letters are converted to lowercase
- All non-alphanumeric characters are removed
- The string reads the same forward and backward

Return:

- `true` → if the string is a palindrome
- `false` → otherwise

---

# Examples

### Example 1

```text
Input:
s = "A man, a plan, a canal: Panama"

Output:
true
```

### Explanation

```text
After removing non-alphanumeric characters
and converting to lowercase:

"amanaplanacanalpanama"

It reads same forward and backward.
```

---

### Example 2

```text
Input:
s = "race a car"

Output:
false
```

### Explanation

```text
Processed string:

"raceacar"

Not a palindrome.
```

---

### Example 3

```text
Input:
s = " "

Output:
true
```

### Explanation

```text
After removing spaces:
""

Empty string is considered palindrome.
```

---

## Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

---
