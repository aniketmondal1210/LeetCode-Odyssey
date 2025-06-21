# Happy Number

## Problem Description
Write an algorithm to determine whether a number `n` is a **happy number**.

A **happy number** is defined by the following process:
1. Start with any positive integer.
2. Replace the number by the **sum of the squares of its digits**.
3. Repeat the process until:
   - the number becomes `1` (where it will stay), or
   - it **loops endlessly** in a cycle that does **not** include `1`.
4. If the number ends in `1`, it is a happy number.

Return `true` if `n` is a happy number, otherwise return `false`.

## Example 1
```
Input: n = 19
Output: true

Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1 → Happy number
```

## Example 2
```
Input: n = 2
Output: false
```

## Constraints
- `1 <= n <= 2^31 - 1`
