# Reverse Words with Matching Vowel Count

You are given a string `s` consisting of lowercase English words separated by a single space.

### Task
1. Count the number of vowels in the **first word**.
2. For each **subsequent word**:
   - If it has the **same number of vowels** as the first word, reverse it.
   - Otherwise, leave it unchanged.
3. Return the final modified string.

Vowels are: **a, e, i, o, u**

---

## Examples

### Example 1

Input:
s = "cat and mice"

Output:
"cat dna mice"


**Explanation:**
- "cat" → 1 vowel  
- "and" → 1 vowel → reversed → "dna"  
- "mice" → 2 vowels → unchanged  

---

### Example 2

Input:
s = "book is nice"

Output:
"book is ecin"


**Explanation:**
- "book" → 2 vowels  
- "is" → 1 vowel → unchanged  
- "nice" → 2 vowels → reversed → "ecin"  

---

### Example 3

Input:
s = "banana healthy"

Output:
"banana healthy"


**Explanation:**
- "banana" → 3 vowels  
- "healthy" → 2 vowels → unchanged  

---

### Constraints

- 1 <= s.length <= 10^5
- Only lowercase English letters and spaces
- Words are separated by exactly one space
- No leading or trailing spaces

---
