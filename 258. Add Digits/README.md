# Problem: Add Digits Until One Digit Remains

## Problem Statement
Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

## Constraints
- `0 <= num <= 2^31 - 1`
- The solution should aim for an **O(1) runtime complexity** (i.e., no loops or recursion).

## Examples

### Example 1
- **Input:** `num = 38`
- **Output:** `2`
- **Explanation:** The process is:
  - `38 → 3 + 8 = 11`
  - `11 → 1 + 1 = 2`
  - Since `2` is a single digit, we return `2`.

### Example 2
- **Input:** `num = 0`
- **Output:** `0`
- **Explanation:** Since `0` is already a single digit, we return `0`.

## Follow-up
Can you solve this problem in **O(1) runtime complexity** without using loops or recursion?
