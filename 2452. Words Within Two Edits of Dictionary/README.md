# Words Within Two Edits of Dictionary

## Problem Statement

You are given:

- `queries[]` → list of words  
- `dictionary[]` → list of valid words  

All words have the **same length**.

👉 You can change **at most 2 characters** in a query word.

Return all words from `queries` that can match **any word in dictionary** after **≤ 2 edits**.

---

# Examples

### Example 1

**Input**
```
queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]
```

**Output**
```
["word","note","wood"]
```

---

### Example 2

**Input**
```
queries = ["yes"]
dictionary = ["not"]
```

**Output**
```
[]
```

---

## Constraints:

- 1 <= queries.length, dictionary.length <= 100
- n == queries[i].length == dictionary[j].length
- 1 <= n <= 100
- All queries[i] and dictionary[j] are composed of lowercase English letters.

---
