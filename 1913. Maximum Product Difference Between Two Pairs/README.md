# Maximum Product Difference Between Two Pairs

## Problem Statement

The product difference between two pairs `(a, b)` and `(c, d)` is defined as:

(a * b) - (c * d)

Given an integer array `nums`, choose four **distinct indices** `w`, `x`, `y`, and `z` such that the product difference between pairs `(nums[w], nums[x])` and `(nums[y], nums[z])` is maximized.

Return the **maximum** such product difference.

## Examples

### Example 1:

Input:  
`nums = [5,6,2,7,4]`  
Output:  
`34`  
Explanation:  
Choose (6, 7) and (2, 4):  
`(6 * 7) - (2 * 4) = 42 - 8 = 34`

### Example 2:

Input:  
`nums = [4,2,5,9,7,4,8]`  
Output:  
`64`  
Explanation:  
Choose (9, 8) and (2, 4):  
`(9 * 8) - (2 * 4) = 72 - 8 = 64`

## Constraints

- `4 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^4`

## Optimal Approach

Sort the array and select:
- The **two largest elements** for the first product.
- The **two smallest elements** for the second product.

This ensures the maximum product difference.
