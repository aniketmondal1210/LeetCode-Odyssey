# Kids With the Greatest Number of Candies

## Problem Description
You are given an integer array `candies`, where `candies[i]` represents the number of candies the `i-th` kid has. You are also given an integer `extraCandies`, representing the number of extra candies you can give.

Return a boolean array `result` where `result[i]` is `true` if, after giving the `i-th` kid **all** the extraCandies, they will have the **greatest number** of candies among all kids, or `false` otherwise.

## Input
- `candies`: A list of integers representing each kid's candies.
- `extraCandies`: An integer representing the extra candies available.

## Output
- A list of booleans indicating whether each kid can have the greatest number of candies.

## Example 1
```
Input: candies = [2, 3, 5, 1, 3], extraCandies = 3
Output: [true, true, true, false, true]

Explanation:
- Kid 1: 2 + 3 = 5 → greatest
- Kid 2: 3 + 3 = 6 → greatest
- Kid 3: 5 + 3 = 8 → greatest
- Kid 4: 1 + 3 = 4 → not greatest
- Kid 5: 3 + 3 = 6 → greatest
```

## Example 2
```
Input: candies = [4, 2, 1, 1, 2], extraCandies = 1
Output: [true, false, false, false, false]

Explanation:
- Kid 1 remains the greatest regardless of where the candy goes.
```

## Example 3
```
Input: candies = [12, 1, 12], extraCandies = 10
Output: [true, false, true]
```

## Constraints
- `n == candies.length`
- `2 <= n <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`
