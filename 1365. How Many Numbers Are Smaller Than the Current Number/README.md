# How Many Numbers Are Smaller Than the Current Number

## Problem Description
Given the array `nums`, for each element `nums[i]`, find out how many numbers in the array are **strictly smaller** than it.

Return the answer as an array `result` such that `result[i]` is the count of numbers smaller than `nums[i]`.

## Input
- `nums`: A list of integers.

## Output
- A list of integers representing the count of smaller numbers for each element in the original list.

## Example 1
```
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Explanation:
- nums[0] = 8 → four numbers are smaller: [1, 2, 2, 3]
- nums[1] = 1 → no numbers are smaller
- nums[2] = 2 → one number is smaller: [1]
- nums[3] = 2 → one number is smaller: [1]
- nums[4] = 3 → three numbers are smaller: [1, 2, 2]
```

## Example 2
```
Input: nums = [6,5,4,8]
Output: [2,1,0,3]
```

## Example 3
```
Input: nums = [7,7,7,7]
Output: [0,0,0,0]
```

## Constraints
- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`
