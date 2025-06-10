# Concatenation of Binary Representations

## Problem Statement

Given an integer `n`, return the decimal value of the binary string formed by concatenating the binary representations of numbers from `1` to `n` in order, modulo **10⁹ + 7**.

---

## Examples

### Example 1
**Input:**  
`n = 1`  
**Output:**  
`1`  
**Explanation:**  
"1" in binary → 1 in decimal.

### Example 2
**Input:**  
`n = 3`  
**Output:**  
`27`  
**Explanation:**  
Binary representations: "1", "10", "11" → Concatenated: "11011" → Decimal: 27.

### Example 3
**Input:**  
`n = 12`  
**Output:**  
`505379714`  
**Explanation:**  
Concatenated binary: "1101110010111011110001001101010111100" → Decimal value modulo 10⁹ + 7 is 505379714.

---

## Constraints

- `1 <= n <= 10⁵`
