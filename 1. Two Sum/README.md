# Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the **indices of the two numbers** such that they add up to `target`.

You may assume:

- Each input has exactly one solution.
- You may not use the same element twice.
- The answer can be returned in any order.

## Examples

### Example 1

```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9
```

### Example 2

```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3

```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Approach

A brute-force solution checks every pair of numbers, which takes `O(n^2)` time.

A better approach uses a **hash map** to store numbers we have already seen along with their indices.

For each number `nums[i]`:

1. Calculate the required number:
   `complement = target - nums[i]`
2. Check whether `complement` is already in the hash map.
3. If it is, return the stored index and the current index.
4. Otherwise, store `nums[i]` and its index in the hash map.

This lets us find the answer in one pass through the array.

## Python Solution

```python
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
```

## Walkthrough

For:

```text
nums = [2, 7, 11, 15]
target = 9
```

| Index | Number | Complement | Seen | Action |
|------:|-------:|-----------:|------|--------|
| 0 | 2 | 7 | `{}` | Store `2: 0` |
| 1 | 7 | 2 | `{2: 0}` | Found `2`, return `[0, 1]` |

Therefore:

```text
Output: [0, 1]
```

## Complexity

- **Time:** `O(n)` average case
- **Space:** `O(n)`

The `O(n)` solution is better than the `O(n^2)` brute-force approach requested in the follow-up.

## Key Idea

The important observation is:

```text
nums[i] + complement = target
```

Therefore:

```text
complement = target - nums[i]
```

By storing previously visited numbers in a hash map, we can check whether the required complement exists in `O(1)` average time.
