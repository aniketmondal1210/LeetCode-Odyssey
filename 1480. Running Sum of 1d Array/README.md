# Problem: Running Sum of 1D Array
Given an array `nums`, we define a **running sum** of an array such that:
```
runningSum[i] = sum(nums[0] + nums[1] + ... + nums[i])
```
Return the running sum of `nums`.

## Input
- `nums`: A list of integers.

## Output
- A list where each element is the running sum up to that index.

## Example 1
```
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: [1, 1+2, 1+2+3, 1+2+3+4]
```

## Example 2
```
Input: nums = [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]
```

## Example 3
```
Input: nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
```

## Constraints
- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`
