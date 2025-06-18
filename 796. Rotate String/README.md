Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of **shifts** on `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

---

### Example 1:

**Input:**  
`s = "abcde"`, `goal = "cdeab"`  
**Output:**  
`true`

**Explanation:**  
"abcde" → "bcdea" → "cdeab" after two shifts.

---

### Example 2:

**Input:**  
`s = "abcde"`, `goal = "abced"`  
**Output:**  
`false`

**Explanation:**  
No amount of shifts on "abcde" will result in "abced".

---

### Constraints:
- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist of lowercase English letters.
