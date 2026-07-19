# Faulty Keyboard

## Problem

Your laptop keyboard is faulty:

- Whenever you type the character `'i'`, the current text on the screen is **reversed**.
- The character `'i'` itself is **not** added to the screen.
- Any other character is appended normally.

Given a string `s`, simulate typing each character and return the final string displayed on the screen.

---

## Examples

### Example 1

**Input**

```text
s = "string"
```

**Output**

```text
"rtsng"
```

**Explanation**

```text
Type 's' → "s"
Type 't' → "st"
Type 'r' → "str"
Type 'i' → reverse → "rts"
Type 'n' → "rtsn"
Type 'g' → "rtsng"
```

Final string:

```text
"rtsng"
```

---

### Example 2

**Input**

```text
s = "poiinter"
```

**Output**

```text
"ponter"
```

**Explanation**

```text
Type 'p' → "p"
Type 'o' → "po"
Type 'i' → reverse → "op"
Type 'i' → reverse → "po"
Type 'n' → "pon"
Type 't' → "pont"
Type 'e' → "ponte"
Type 'r' → "ponter"
```

Final string:

```text
"ponter"
```

---

## Constraints:

- 1 <= s.length <= 100
- s consists of lowercase English letters.
- s[0] != 'i'

---
