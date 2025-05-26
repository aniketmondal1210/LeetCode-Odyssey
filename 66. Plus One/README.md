# Plus One

## Problem Statement

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. The digits are ordered from most significant to least significant (left to right). The integer does **not** contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

## Examples

### Example 1
**Input:**  
`digits = [1,2,3]`  
**Output:**  
`[1,2,4]`  
**Explanation:**  
123 + 1 = 124 → `[1,2,4]`

### Example 2  
**Input:**  
`digits = [4,3,2,1]`  
**Output:**  
`[4,3,2,2]`  
**Explanation:**  
4321 + 1 = 4322 → `[4,3,2,2]`

### Example 3  
**Input:**  
`digits = [9]`  
**Output:**  
`[1,0]`  
**Explanation:**  
9 + 1 = 10 → `[1,0]`

## Constraints

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading 0's.
