# Problem: Palindrome Number

## Problem Statement
Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

### Example 1:
**Input:**  
`x = 121`  
**Output:**  
`true`  
**Explanation:**  
121 reads the same from left to right and right to left.

### Example 2:
**Input:**  
`x = -121`  
**Output:**  
`false`  
**Explanation:**  
From left to right, it reads `-121`. From right to left, it becomes `121-`, which is not a palindrome.

### Example 3:
**Input:**  
`x = 10`  
**Output:**  
`false`  
**Explanation:**  
Reads `01` from right to left, which is not the same as `10`.

---

## Constraints:
- `-2³¹ <= x <= 2³¹ - 1`

## Follow-up:
Can you solve it without converting the integer to a string?
