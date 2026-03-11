# Ransom Note

## Problem Statement

Given two strings:

- `ransomNote`
- `magazine`

Return **true** if `ransomNote` can be constructed using the letters from `magazine`, otherwise return **false**.

### Rules

- Each letter in `magazine` can be used **only once**.
- Both strings contain **lowercase English letters**.

---

## Examples

### Example 1

**Input**
```
ransomNote = "a"
magazine = "b"
```

**Output**
```
false
```

**Explanation**

`magazine` does not contain the letter **a**.

---

### Example 2

**Input**
```
ransomNote = "aa"
magazine = "ab"
```

**Output**
```
false
```

**Explanation**

`magazine` has only **one 'a'**, but `ransomNote` requires **two 'a's**.

---

### Example 3

**Input**
```
ransomNote = "aa"
magazine = "aab"
```

**Output**
```
true
```

**Explanation**

`magazine` contains enough letters to build `ransomNote`.

---

##   Constraints:

- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters.

---
