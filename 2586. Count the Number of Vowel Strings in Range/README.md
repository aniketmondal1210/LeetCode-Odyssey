# Count Vowel Strings in Range

## Problem Statement

You are given:

- An array of strings `words`
- Two integers `left` and `right`

A string is called a **vowel string** if:

- It starts with a vowel (`a, e, i, o, u`)
- It ends with a vowel

👉 Return the number of such strings in the index range `[left, right]`.

---

# Examples

### Example 1

**Input**
```
words = ["are","amy","u"], left = 0, right = 2
```

**Output**
```
2
```

---

### Example 2

**Input**
```
words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
```

**Output**
```
3
```

---

## Constraints:

- 1 <= words.length <= 1000
- 1 <= words[i].length <= 10
- words[i] consists of only lowercase English letters.
- 0 <= left <= right < words.length

---
