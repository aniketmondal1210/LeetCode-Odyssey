# Count Strings Appearing Exactly Once in Each Array

## Problem Statement
You are given two string arrays `words1` and `words2`.  
Return the number of strings that appear **exactly once** in each of the two arrays.

---

## Examples

### Example 1
**Input:**

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

**Output:**

2

**Explanation:**
- `"leetcode"` appears once in both arrays ✅
- `"amazing"` appears once in both arrays ✅
- `"is"` appears twice in `words1`, so ❌
- `"as"` does not appear in `words2`, so ❌  
Thus, the answer is `2`.

---

### Example 2
**Input:**

words1 = ["b","bb","bbb"]
words2 = ["a","aa","aaa"]

**Output:**

0

**Explanation:**  
No word appears exactly once in both arrays.

---

### Example 3
**Input:**

words1 = ["a","ab"]
words2 = ["a","a","a","ab"]

**Output:**

1

**Explanation:**  
Only `"ab"` appears exactly once in each array.

---

## Constraints
- `1 <= words1.length, words2.length <= 1000`
- `1 <= words1[i].length, words2[j].length <= 30`
- Strings consist only of lowercase English letters.

---
