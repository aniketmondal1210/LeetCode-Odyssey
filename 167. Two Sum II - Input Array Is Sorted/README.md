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

## Approach: Two Pointers

Because the array is already sorted, we can use two pointers:

- `left` starts at the beginning of the array.
- `right` starts at the end of the array.

At every step, calculate:

```text
current_sum = numbers[left] + numbers[right]
```

Then:

1. If `current_sum == target`, we found the answer.
2. If `current_sum < target`, increase `left` to get a larger sum.
3. If `current_sum > target`, decrease `right` to get a smaller sum.

Continue until the two pointers meet.

## Python Solution

```python
def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

## Walkthrough

For:

```text
numbers = [2, 7, 11, 15]
target = 9
```

Initially:

```text
left = 0  -> 2
right = 3 -> 15
```

Sum:

```text
2 + 15 = 17
```

Since `17 > 9`, move `right` left.

Now:

```text
2 + 11 = 13
```

Again, the sum is too large, so move `right` left.

Now:

```text
2 + 7 = 9
```

We found the target.

The internal indices are `0` and `1`, but the problem uses **1-based indexing**, so return:

```text
[1, 2]
```

## Why Two Pointers Work

The array is sorted, which gives us a useful property:

- Moving `left` to the right makes the sum larger or equal.
- Moving `right` to the left makes the sum smaller or equal.

Therefore, we can eliminate impossible pairs without checking every combination.

A brute-force approach would take `O(n^2)` time, while the two-pointer approach only scans the array once.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

This satisfies the requirement of using only constant extra space.

## Key Takeaway

For a **sorted array** where we need to find two numbers with a specific sum, the **two-pointer technique** is usually the optimal approach when constant extra space is required.

Remember the pointer rules:

```text
sum == target  -> return answer
sum < target   -> move left forward
sum > target   -> move right backward
```

Because the problem is **1-indexed**, return `left + 1` and `right + 1`.
