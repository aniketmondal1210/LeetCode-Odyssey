# Special Array

## Problem

Given an array `nums` of non-negative integers, return the unique number
`x` such that exactly `x` numbers in `nums` are greater than or equal to
`x`. If no such `x` exists, return `-1`.

## Examples

### Example 1

``` text
Input: nums = [3,5]
Output: 2
```

There are exactly 2 numbers (`3` and `5`) that are greater than or equal
to `2`.

### Example 2

``` text
Input: nums = [0,0]
Output: -1
```

No value of `x` satisfies the condition.

### Example 3

``` text
Input: nums = [0,4,3,0,4]
Output: 3
```

There are exactly 3 values greater than or equal to `3`: `4`, `3`, and
`4`.

## Constraints

-   `1 <= nums.length <= 100`
-   `0 <= nums[i] <= 1000`

## Key Observation

The answer `x` cannot be greater than `len(nums)`, because there are
only `n` elements. Therefore, we only need to check values from `0` to
`n`.

For every candidate `x`, count how many elements satisfy:

``` python
num >= x
```

If that count is exactly `x`, then `x` is the answer. Otherwise,
continue checking.

## Python Solution

``` python
def special_array(nums):
    n = len(nums)

    for x in range(n + 1):
        count = 0

        for num in nums:
            if num >= x:
                count += 1

        if count == x:
            return x

    return -1
```

## Walkthrough

For:

``` text
nums = [0,4,3,0,4]
```

There are `5` elements, so we check `x` from `0` to `5`.

For `x = 3`:

``` text
0 >= 3  -> No
4 >= 3  -> Yes
3 >= 3  -> Yes
0 >= 3  -> No
4 >= 3  -> Yes
```

Exactly 3 numbers are greater than or equal to 3. Therefore:

``` text
Answer = 3
```

## Why Check `x` Only Up to `n`?

If `x > n`, it is impossible to have exactly `x` numbers greater than or
equal to `x`, because the array contains only `n` elements.

Thus:

``` python
for x in range(n + 1):
```

is sufficient.

## Complexity

There are at most `n + 1` candidate values, and for each candidate we
scan the array.

-   **Time:** `O(n^2)`
-   **Space:** `O(1)`

With `n <= 100`, this is easily fast enough.

## Alternative Using Sorting

The problem can also be solved after sorting the array. However, because
the constraints are small, the direct counting approach is simpler and
easier to understand.

## Key Takeaway

The condition is simply:

``` text
number of elements >= x == x
```

Since `x` must be between `0` and `len(nums)`, try every possible `x`,
count the qualifying elements, and return the first one that matches. If
none matches, return `-1`.
