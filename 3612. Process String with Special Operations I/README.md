# Process String with Special Operations

## Problem Statement
You are given a string `s` that contains:
- lowercase English letters,
- and special characters: `*`, `#`, `%`.

Build a new string **result** by processing the characters **from left to right** using these rules:

### Rules
| Character | Operation |
|----------|-----------|
| lowercase letter | Append to result |
| `*` | Remove the last character (if it exists) |
| `#` | Duplicate the current result and append it (result = result + result) |
| `%` | Reverse the current result |

Return the **final string** after processing all characters.

---

## Example 1
**Input:**  

s = "a#b%*"

**Output:**  

"ba"


**Step-by-step Processing:**

| i | s[i] | Operation | Result |
|---|------|-----------|--------|
| 0 | a | append | `"a"` |
| 1 | # | duplicate | `"aa"` |
| 2 | b | append | `"aab"` |
| 3 | % | reverse | `"baa"` |
| 4 | * | pop last | `"ba"` |

Final result: `"ba"`

---

## Example 2
**Input:**  

s = "z*#"

**Output:**  

""`


**Processing:**

| i | s[i] | Operation | Result |
|---|------|-----------|--------|
| 0 | z | append | `"z"` |
| 1 | * | remove last | `""` |
| 2 | # | duplicate | `""` |

Final result: `""`

---

## Constraints

- 1 ≤ s.length ≤ 20
- s contains lowercase letters or characters *, #, %


---
