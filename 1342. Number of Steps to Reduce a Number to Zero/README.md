# Number of Steps to Reduce a Number to Zero

## Problem Statement

Given an integer `num`, return the number of steps to reduce it to zero.

In one step:
- If the current number is even, divide it by 2.
- If the current number is odd, subtract 1 from it.

## Examples

### Example 1:
Input:  
`num = 14`  
Output:  
`6`  
Explanation:  
- Step 1) 14 is even; divide by 2 → 7  
- Step 2) 7 is odd; subtract 1 → 6  
- Step 3) 6 is even; divide by 2 → 3  
- Step 4) 3 is odd; subtract 1 → 2  
- Step 5) 2 is even; divide by 2 → 1  
- Step 6) 1 is odd; subtract 1 → 0

### Example 2:
Input:  
`num = 8`  
Output:  
`4`  
Explanation:  
- Step 1) 8 is even; divide by 2 → 4  
- Step 2) 4 is even; divide by 2 → 2  
- Step 3) 2 is even; divide by 2 → 1  
- Step 4) 1 is odd; subtract 1 → 0

### Example 3:
Input:  
`num = 123`  
Output:  
`12`

## Constraints

- `0 <= num <= 10^6`
