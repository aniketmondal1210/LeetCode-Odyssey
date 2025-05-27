# Number of Employees Who Met the Target

## Problem Statement

There are `n` employees in a company, numbered from `0` to `n - 1`.  
Each employee `i` has worked for `hours[i]` hours in the company.

The company requires each employee to work for **at least** `target` hours.

You are given:
- A 0-indexed array `hours` of non-negative integers of length `n`
- A non-negative integer `target`

Return the number of employees who worked at least `target` hours.

## Examples

### Example 1:
**Input:**  
`hours = [0,1,2,3,4]`, `target = 2`  
**Output:**  
`3`  
**Explanation:**  
Employees who worked at least 2 hours: indices 2, 3, and 4.

### Example 2:
**Input:**  
`hours = [5,1,4,2,2]`, `target = 6`  
**Output:**  
`0`  
**Explanation:**  
No employee worked at least 6 hours.

## Constraints

- `1 <= n == hours.length <= 50`
- `0 <= hours[i], target <= 10^5`
