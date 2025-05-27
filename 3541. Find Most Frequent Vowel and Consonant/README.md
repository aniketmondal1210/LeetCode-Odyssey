# Maximum Vowel and Consonant Frequency Sum

## Problem Statement

You are given a string `s` consisting of lowercase English letters.

Your task is to:

1. Find the vowel (`a`, `e`, `i`, `o`, `u`) with the **maximum frequency**.
2. Find the consonant (all other letters) with the **maximum frequency**.
3. Return the **sum** of both frequencies.

### Notes:
- If there are **no vowels** or **no consonants**, consider their frequency as 0.
- If multiple vowels/consonants have the same frequency, you can choose any of them.

---

## Examples

### Example 1:

**Input:**  
`s = "successes"`  

**Output:**  
`6`

**Explanation:**
- Vowels: `'u' (1)`, `'e' (2)` → max = `2`  
- Consonants: `'s' (4)`, `'c' (2)` → max = `4`  
- `2 + 4 = 6`

---

### Example 2:

**Input:**  
`s = "aeiaeia"`  

**Output:**  
`3`

**Explanation:**
- Vowels: `'a' (3)`, `'e' (2)`, `'i' (2)` → max = `3`  
- No consonants → max = `0`  
- `3 + 0 = 3`

---

## Constraints

- `1 <= s.length <= 100`
- `s` contains only lowercase English letters (`'a'` to `'z'`)
