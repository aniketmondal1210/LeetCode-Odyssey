# Problem: Check if an Integer is a Harshad Number

## Problem Statement
An integer is considered a **Harshad number** if it is divisible by the sum of its digits.  

Given an integer `x`, return the sum of its digits if `x` is a Harshad number. Otherwise, return `-1`.

## Constraints
- `1 <= x <= 100`

## Examples

### Example 1
- **Input:** `x = 18`
- **Output:** `9`
- **Explanation:**  
  - The sum of digits of `18` is `9` (`1 + 8 = 9`).
  - `18` is divisible by `9`, so `18` is a Harshad number.
  - Return `9`.

### Example 2
- **Input:** `x = 23`
- **Output:** `-1`
- **Explanation:**  
  - The sum of digits of `23` is `5` (`2 + 3 = 5`).
  - `23` is **not** divisible by `5`, so `23` is **not** a Harshad number.
  - Return `-1`.
