# Two Sum II - Input Array Is Sorted

## Problem

Given a **1-indexed** array of integers `numbers` that is already sorted in non-decreasing order, find two numbers that add up to `target`.

Return the 1-based indices `[index1, index2]` where `index1 < index2`.

The array contains exactly one solution, and the same element cannot be used twice.

The solution must use **constant extra space**.

## Examples

### Example 1

```text
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

Explanation: `2 + 7 = 9`, so the 1-based indices are `[1, 2]`.

### Example 2

```text
Input: numbers = [2,3,4], target = 6
Output: [1,3]
```

Explanation: `2 + 4 = 6`, so the 1-based indices are `[1, 3]`.

### Example 3

```text
Input: numbers = [-1,0], target = -1
Output: [1,2]
```

Explanation: `-1 + 0 = -1`, so the indices are `[1, 2]`.

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- Exactly one solution exists.
- The same element cannot be used twice.
