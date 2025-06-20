# Rotate String

## Problem Description
Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of shifts.

A **shift** on `s` consists of moving the **leftmost character** of `s` to the **rightmost** position.

### Example 1
```
Input: s = "abcde", goal = "cdeab"
Output: true
```

### Example 2
```
Input: s = "abcde", goal = "abced"
Output: false
```

## Explanation
- "abcde" → "bcdea" → "cdeab" (goal reached after 2 shifts)
- In the second example, no number of shifts will result in "abced"

## Constraints
- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist only of lowercase English letters
