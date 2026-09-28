# Maximum Nesting Depth of the Parentheses

## Problem Description

Given a **valid parentheses string (VPS)** `s`, return the **nesting depth** of `s`. The nesting depth is the maximum number of nested parentheses in the string.

A string is a Valid Parentheses String (VPS) defined as:
- An empty string `""`, or a single character not equal to `'('` or `')'`.
- A string that can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are VPS.
- A string that can be written as `(A)`, where `A` is a VPS.

---

## Examples

### Example 1
- **Input:** `s = "(1+(2*3)+((8)/4))+1"`
- **Output:** `3`
- **Explanation:** Digit `8` is inside $3$ nested parentheses in the string.

### Example 2
- **Input:** `s = "(1)+((2))+(((3)))"`
- **Output:** `3`
- **Explanation:** Digit `3` is inside $3$ nested parentheses in the string.

### Example 3
- **Input:** `s = "()(())((()()))"`
- **Output:** `3`

---

## Constraints

- $1 \le \text{s.length} \le 100$
- `s` consists of digits `0-9` and characters `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.
- It is guaranteed that parentheses expression `s` is a VPS.

---
