# Reverse First K Characters of a String

## Problem Statement
You are given a string `s` and an integer `k`.

Your task is to **reverse the first `k` characters** of the string and return the resulting string.  
The remaining characters (after the first `k`) should stay in the same order.

---

## Examples

### Example 1
**Input:**

s = "abcd"
k = 2


**Output:**

"bacd"


**Explanation:**  
The first `k = 2` characters `"ab"` are reversed to `"ba"`.  
The remaining part `"cd"` stays unchanged.

---

### Example 2
**Input:**

s = "xyz"
k = 3


**Output:**

"zyx"


**Explanation:**  
All characters are reversed since `k` equals the string length.

---

### Example 3
**Input:**

s = "hey"
k = 1


**Output:**

"hey"


**Explanation:**  
Reversing a single character does not change the string.

---

## Constraints

- 1 <= s.length <= 100
- s consists of lowercase English letters
- 1 <= k <= s.length


---
