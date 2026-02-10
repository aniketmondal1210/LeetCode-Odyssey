# Maximum Frequency Difference (Odd - Even)

## Problem Statement
You are given a string `s` consisting of lowercase English letters.

Your task is to compute the maximum difference:

diff = freq(a1) - freq(a2)


Such that:
- `a1` has an **odd frequency**
- `a2` has an **even frequency**

Return the maximum possible difference.

---

## Example 1

**Input:**

s = "aaaaabbc"


**Output:**

3


**Explanation:**
- `'a'` appears 5 times (odd)
- `'b'` appears 2 times (even)

Maximum difference = 5 - 2 = 3

---

## Example 2

**Input:**

s = "abcabcab"


**Output:**

1


**Explanation:**
- `'a'` appears 3 times (odd)
- `'c'` appears 2 times (even)

Maximum difference = 3 - 2 = 1

---

## Constraints

- 3 ≤ s.length ≤ 100
- s consists only of lowercase English letters
- s contains at least one character with odd frequency
- s contains at least one character with even frequency


---
