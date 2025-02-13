# Problem: Multiply Strings

## Problem Statement
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

You **must not** use any built-in BigInteger library or convert the inputs to integers directly.

## Constraints
- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zeros, except when the number is `0`.

## Examples

### Example 1
- **Input:** `num1 = "2"`, `num2 = "3"`
- **Output:** `"6"`

### Example 2
- **Input:** `num1 = "123"`, `num2 = "456"`
- **Output:** `"56088"`

## Approach
To multiply two numbers represented as strings:
1. Reverse both strings for easier index manipulation.
2. Use an array to store intermediate multiplication results.
3. Iterate through each digit in `num1` and `num2`, multiply them, and store the result at the appropriate position in the array.
4. Handle carries and convert the final array into a string result.

## Complexity Analysis
- **Time Complexity:** `O(m * n)`, where `m` and `n` are the lengths of `num1` and `num2`.
- **Space Complexity:** `O(m + n)`, to store the result.

---
