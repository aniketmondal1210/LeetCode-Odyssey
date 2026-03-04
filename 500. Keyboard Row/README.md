# Keyboard Row Words

## Problem Statement

Given an array of strings `words`, return the words that can be typed using letters from **only one row** of the American keyboard.

Keyboard rows:

- First row: `"qwertyuiop"`
- Second row: `"asdfghjkl"`
- Third row: `"zxcvbnm"`

Notes:
- Case-insensitive (uppercase and lowercase are treated the same).
- Return all valid words.

---

## Examples

### Example 1

**Input**
```
words = ["Hello","Alaska","Dad","Peace"]
```

**Output**
```
["Alaska","Dad"]
```

**Explanation**
- "Alaska" → all letters in second row  
- "Dad" → all letters in second row  
- Others use multiple rows  

---

### Example 2

**Input**
```
words = ["omk"]
```

**Output**
```
[]
```

---

### Example 3

**Input**
```
words = ["adsdf","sfd"]
```

**Output**
```
["adsdf","sfd"]
```

---

## Constraints:

- 1 <= words.length <= 20
- 1 <= words[i].length <= 100
- words[i] consists of English letters (both lowercase and uppercase). 

---
