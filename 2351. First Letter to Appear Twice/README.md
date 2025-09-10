# First Letter to Appear Twice

You are given a string `s` consisting of lowercase English letters.  
Return the **first letter to appear twice**.  

---

## Note
- A letter `a` appears twice before another letter `b` **if the second occurrence of `a` is before the second occurrence of `b`**.  
- The string will always contain at least one letter that appears twice.  

---

## Examples

### Example 1
**Input:**

s = "abccbaacz"


**Output:**

c


**Explanation:**  
- `'a'` appears at indices `[0, 5, 6]`  
- `'b'` appears at indices `[1, 4]`  
- `'c'` appears at indices `[2, 3, 7]`  
- `'z'` appears at index `[8]`  
- The second occurrence of `'c'` happens first (at index `3`), so the answer is `"c"`.  

---

### Example 2
**Input:**

s = "abcdd"


**Output:**

d


**Explanation:**  
The only character that repeats is `'d'`.  

---

## Constraints
- 2 ≤ s.length ≤ 100  
- s consists of lowercase English letters.  
- s has at least one repeated letter.  

---
