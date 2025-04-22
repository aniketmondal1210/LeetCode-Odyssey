# Sum of Unique Elements

## Problem Description
You are given an integer array `nums`. The **unique elements** of the array are those that appear **exactly once**.

Return the **sum** of all the unique elements in `nums`.

## Inputs
- `nums`: A list of integers.

## Output
- An integer representing the sum of elements that occur exactly once.

## Example 1
```
Input: nums = [1, 2, 3, 2]
Output: 4

Explanation:
Unique elements = [1, 3]
Sum = 1 + 3 = 4
```

## Example 2
```
Input: nums = [1, 1, 1, 1, 1]
Output: 0

Explanation:
No unique elements.
```

## Example 3
```
Input: nums = [1, 2, 3, 4, 5]
Output: 15

Explanation:
All elements are unique.
Sum = 1 + 2 + 3 + 4 + 5 = 15
```

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
