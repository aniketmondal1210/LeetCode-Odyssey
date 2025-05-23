# Count Negative Numbers in a Sorted Matrix

## Problem Statement

Given an `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in `grid`.

## Examples

### Example 1:
Input:  
`grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]`  
Output:  
`8`  
Explanation: There are 8 negative numbers in the matrix.

### Example 2:
Input:  
`grid = [[3,2],[1,0]]`  
Output:  
`0`  
Explanation: All numbers are non-negative.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `-100 <= grid[i][j] <= 100`

## Follow up

Could you find an `O(n + m)` solution?
