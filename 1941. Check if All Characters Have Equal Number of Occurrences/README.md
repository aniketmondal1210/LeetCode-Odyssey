# Check if a String is Good

## Problem Statement

Given a string `s`, return `true` if `s` is a **good string**, or `false` otherwise.

A string is considered **good** if **all the characters** that appear in `s` have the **same frequency** (i.e., the same number of occurrences).

---

## Examples

### Example 1:

**Input:**  
`s = "abacbc"`

**Output:**  
`true`

**Explanation:**  
The characters that appear in `s` are `'a'`, `'b'`, and `'c'`.  
All characters occur **2 times** in the string.

---

### Example 2:

**Input:**  
`s = "aaabb"`

**Output:**  
`false`

**Explanation:**  
Characters `'a'` and `'b'` occur **3** and **2** times respectively, which are not equal.

---

## Constraints:

- 1 ≤ `s.length` ≤ 1000  
- `s` consists of lowercase English letters.
