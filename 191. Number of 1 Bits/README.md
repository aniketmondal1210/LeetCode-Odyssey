# Number of Set Bits (Hamming Weight)

## Problem Statement

Given a positive integer `n`, write a function that returns the number of **set bits** (1s) in its binary representation. This is also known as the **Hamming weight**.

## Examples

### Example 1:
Input:  
`n = 11`  
Output:  
`3`  
Explanation: Binary representation of 11 is `1011`, which has three set bits.

### Example 2:
Input:  
`n = 128`  
Output:  
`1`  
Explanation: Binary representation is `10000000`, which has one set bit.

### Example 3:
Input:  
`n = 2147483645`  
Output:  
`30`  
Explanation: Binary representation has thirty `1`s.

## Constraints

- `1 <= n <= 2^31 - 1`

## Follow-up

If this function is called many times:
- Precompute the set bits for all 8-bit numbers (0 to 255) and store them in a lookup table.
- Then compute the Hamming weight of a 32-bit number by summing the set bits from each of its 4 bytes using the table.
- This reduces computation time significantly for repeated calls.
