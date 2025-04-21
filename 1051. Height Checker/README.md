# Height Checker Task

## Problem Description
A school is organizing an annual photo of all the students. The students are expected to stand in a single line in **non-decreasing order** of height.

You are given an array `heights`, representing the **current order** in which the students are standing.
Your task is to return the number of indices where the **current order does not match the expected order** (i.e., the order if the students were sorted by height).

## Inputs
- `heights`: A list of integers where `heights[i]` represents the height of the `i-th` student.

## Output
- An integer representing the number of indices where `heights[i] != expected[i]`.

## Example 1
```
Input: heights = [1, 1, 4, 2, 1, 3]
Output: 3

Explanation:
heights:  [1, 1, 4, 2, 1, 3]
expected: [1, 1, 1, 2, 3, 4]
Indices 2, 4, and 5 do not match.
```

## Example 2
```
Input: heights = [5, 1, 2, 3, 4]
Output: 5

Explanation:
heights:  [5, 1, 2, 3, 4]
expected: [1, 2, 3, 4, 5]
All indices do not match.
```

## Example 3
```
Input: heights = [1, 2, 3, 4, 5]
Output: 0

Explanation:
heights:  [1, 2, 3, 4, 5]
expected: [1, 2, 3, 4, 5]
All indices match.
```

## Constraints
- `1 <= heights.length <= 100`
- `1 <= heights[i] <= 100`
