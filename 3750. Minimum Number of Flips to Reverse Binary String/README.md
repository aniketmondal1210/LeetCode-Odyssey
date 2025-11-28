# Minimum Bit Flips to Make Binary String Equal to Its Reverse

## Problem Statement
You are given a positive integer `n`.  
Let `s` be the binary representation of `n` **without leading zeros**.

The **reverse** of `s` is the string obtained by writing the characters of `s` in the opposite order.  
You may flip any bit in `s` (change `0 → 1` or `1 → 0`). Each flip affects exactly one bit.

Return the **minimum number of flips** required to make `s` equal to the reverse of its original form.

---

## Examples

**Example 1**  
Input: `n = 7`  
Binary: `"111"` → reverse `"111"` → no mismatches → Output: `0`

**Example 2**  
Input: `n = 10`  
Binary: `"1010"` → reverse `"0101"`  
Pairs: (index 0,3) `1 vs 0` mismatch → 2 flips  
       (index 1,2) `0 vs 1` mismatch → 2 flips  
Total flips = `4`

---

## Constraints

- `1 <= n < 10^9`
