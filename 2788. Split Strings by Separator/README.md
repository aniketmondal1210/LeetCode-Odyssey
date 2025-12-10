# Split Strings by Separator

Given an array of strings `words` and a character `separator`, split each string using the separator and return **all non-empty resulting strings**, preserving order.

---

## Examples

### Example 1

Input:

words = ["one.two.three", "four.five", "six"]

separator = "."

Output:

["one", "two", "three", "four", "five", "six"]


### Example 2

Input:

words = ["$easy$", "$problem$"]

separator = "$"

Output:

["easy", "problem"]


### Example 3

Input:

words = ["|||"]

separator = "|"

Output:

[]


---

### Constraints:

- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- characters in words[i] are either lowercase English letters or characters from the string ".,|$#@" (excluding the quotes)
- separator is a character from the string ".,|$#@" (excluding the quotes)

---
