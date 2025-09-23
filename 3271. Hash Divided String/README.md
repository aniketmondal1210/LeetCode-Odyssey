# String Hashing Problem

## Problem Statement
You are given:
- A string `s` of length `n`.
- An integer `k`, where `n` is divisible by `k`.

Your task is to **hash the string** into a new string `result` of length `n/k`.

### Hashing Process
1. Split `s` into `n/k` substrings, each of length `k`.
2. For each substring:
   - Convert each character into its alphabetical index (`'a' = 0`, `'b' = 1`, … `'z' = 25`).
   - Compute the **sum** of all indices.
   - Take modulo 26 of this sum.
   - Map the value back to a character.
   - Append the character to `result`.

Return `result`.

---

## Examples

### Example 1
**Input:**

s = "abcd", k = 2

**Output:**

"bf"

**Explanation:**
- Substring "ab": (0 + 1) % 26 = 1 → `'b'`
- Substring "cd": (2 + 3) % 26 = 5 → `'f'`

---

### Example 2
**Input:**

s = "mxz", k = 3

**Output:**

"i"

**Explanation:**
- Substring "mxz": (12 + 23 + 25) = 60, 60 % 26 = 8 → `'i'`

---

## Constraints
- 1 ≤ k ≤ 100  
- k ≤ s.length ≤ 1000  
- s.length is divisible by k  
- s consists only of lowercase English letters  

---
