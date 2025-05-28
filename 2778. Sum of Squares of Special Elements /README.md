# Sum of Squares of Special Elements

## Problem Statement

You are given a 1-indexed integer array `nums` of length `n`.

An element `nums[i]` is called **special** if `i` divides `n`, i.e., `n % i == 0`.

Return the **sum of the squares** of all special elements of `nums`.

## Examples

### Example 1:
Input:  
`nums = [1, 2, 3, 4]`  
Output:  
`21`  
Explanation:  
Special indices: 1, 2, 4 (since 1, 2, 4 divide 4).  
Sum of squares: `1^2 + 2^2 + 4^2 = 1 + 4 + 16 = 21`

---

### Example 2:
Input:  
`nums = [2, 7, 1, 19, 18, 3]`  
Output:  
`63`  
Explanation:  
Special indices: 1, 2, 3, 6 (since 1, 2, 3, 6 divide 6).  
Sum of squares: `2^2 + 7^2 + 1^2 + 3^2 = 4 + 49 + 1 + 9 = 63`

## Constraints

- `1 <= nums.length == n <= 50`
- `1 <= nums[i] <= 50`

## Approach

1. Iterate through indices from 1 to `n`.
2. Check if `n % i == 0`.
3. If yes, include `nums[i-1]^2` in the sum.
4. Return the final result.
