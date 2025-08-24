# Check if Search Word is Prefix of Any Word in a Sentence

## Problem
You are given:
- A **sentence** consisting of words separated by a single space.  
- A **searchWord**.  

You must check if **searchWord** is a **prefix** of any word in `sentence`.  

- Return the **1-indexed position** of the first word where `searchWord` is a prefix.  
- If no such word exists, return **-1**.  

**Note:** A prefix of a string `s` is any leading contiguous substring of `s`.

---

## Constraints
- `1 <= sentence.length <= 100`
- `1 <= searchWord.length <= 10`
- `sentence` consists of lowercase English letters and spaces.
- `searchWord` consists of lowercase English letters.

---

## Examples

### Example 1
**Input**

sentence = "i love eating burger"
searchWord = "burg"

**Output**

4

**Explanation:**  
"burg" is prefix of `"burger"`, which is the **4th word**.

---

### Example 2
**Input**

sentence = "this problem is an easy problem"
searchWord = "pro"

**Output**

2

**Explanation:**  
"pro" is prefix of `"problem"` which occurs at indices 2 and 6, but we return **2** (first occurrence).

---

### Example 3
**Input**

sentence = "i am tired"
searchWord = "you"

**Output**

-1

**Explanation:**  
"you" is not a prefix of any word.

---
