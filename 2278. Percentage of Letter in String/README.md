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

## Approach
1. Initialize an empty list `running_sum`.
2. Traverse the input array `nums` while keeping a cumulative sum.
3. Append the cumulative sum at each step to `running_sum`.
4. Return the resulting list.

---

# Percentage of Letter in String

## Problem Description
Given a string `s` and a character `letter`, return the percentage of characters in `s` that are equal to `letter`, rounded down to the nearest whole percent.

## Input
- `s`: A string of lowercase English letters.
- `letter`: A single lowercase English letter.

## Output
- An integer representing the percentage (rounded down) of `letter` occurrences in `s`.

## Example 1
```
Input: s = "foobar", letter = "o"
Output: 33
Explanation: 2 out of 6 characters are 'o' → 2/6 * 100 = 33.33 → 33%
```

## Example 2
```
Input: s = "jjjj", letter = "k"
Output: 0
Explanation: 0 out of 4 characters are 'k' → 0/4 * 100 = 0%
```

## Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters.
- `letter` is a lowercase English letter.
