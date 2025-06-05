# Count of Even and Odd Indexed Set Bits

## Problem Statement

You are given a positive integer `n`.

Let `even` denote the number of **even indices** in the **binary representation** of `n` with value `1`.  
Let `odd` denote the number of **odd indices** in the binary representation of `n` with value `1`.

> Note: Bits are indexed from **right to left**, starting at index 0.

Return the array `[even, odd]`.

---

## Examples

**Example 1:**

Input:  
`n = 50`  
Output:  
`[1, 2]`  
Explanation:  
Binary of 50 is `110010`.  
Indices with 1s: 1, 4, 5 → index 4 is even, indices 1 and 5 are odd → [1, 2]

---

**Example 2:**

Input:  
`n = 2`  
Output:  
`[0, 1]`  
Explanation:  
Binary of 2 is `10`.  
Index 1 has a 1 → only one odd index → [0, 1]

---

## Constraints

- `1 <= n <= 1000`
