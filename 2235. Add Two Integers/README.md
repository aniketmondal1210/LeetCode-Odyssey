# Problem: Sum of Two Integers

## Problem Statement
Given two integers `num1` and `num2`, return the sum of the two integers.

## Constraints
- The integers are within the range: `-100 <= num1, num2 <= 100`.

## Examples
### Example 1
- **Input:** `num1 = 12`, `num2 = 5`
- **Output:** `17`
- **Explanation:** The sum of `12` and `5` is `17`, so `17` is returned.

### Example 2
- **Input:** `num1 = -10`, `num2 = 4`
- **Output:** `-6`
- **Explanation:** The sum of `-10` and `4` is `-6`, so `-6` is returned.

## Solution
To solve this problem, simply add `num1` and `num2` using the `+` operator and return the result.

```python
def sum_numbers(num1: int, num2: int) -> int:
    return num1 + num2

# Example usage:
print(sum_numbers(12, 5))  # Output: 17
print(sum_numbers(-10
