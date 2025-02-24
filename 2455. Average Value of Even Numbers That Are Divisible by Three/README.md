# Problem: Average Value of Even Numbers Divisible by 3

## Problem Statement
Given an integer array `nums` of positive integers, return the average value of all even integers that are divisible by `3`.

The average of `n` elements is the sum of the `n` elements divided by `n`, rounded down to the nearest integer.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,3,6,10,12,15]`
- **Output:** `9`
- **Explanation:** The even numbers that are divisible by `3` are `6` and `12`. Their average is `(6 + 12) / 2 = 9`.

### Example 2
- **Input:** `nums = [1,2,4,7,10]`
- **Output:** `0`
- **Explanation:** There are no even numbers divisible by `3`, so return `0`.
