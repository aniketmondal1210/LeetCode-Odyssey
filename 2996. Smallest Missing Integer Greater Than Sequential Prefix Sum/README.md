# Problem: Smallest Missing Integer After Sequential Prefix

## Problem Statement

You are given a **0-indexed** array of integers `nums`.

A prefix `nums[0..i]` is **sequential** if, for all `1 <= j <= i`:

```text
nums[j] = nums[j - 1] + 1
```

In particular, the prefix consisting only of `nums[0]` is sequential.

Find the **longest sequential prefix** of `nums`.

Let `sum` be the sum of all elements in this longest sequential prefix.

Return the **smallest integer `x`** that:

```text
x >= sum
```

and `x` does not occur in `nums`.

---

## Example 1

**Input:**

```text
nums = [1, 2, 3, 2, 5]
```

**Output:**

```text
6
```

**Explanation:**

The longest sequential prefix is:

```text
[1, 2, 3]
```

Its sum is:

```text
1 + 2 + 3 = 6
```

`6` is not present in the array, so the smallest missing integer greater than or equal to `6` is:

```text
6
```

---

## Example 2

**Input:**

```text
nums = [3, 4, 5, 1, 12, 14, 13]
```

**Output:**

```text
15
```

**Explanation:**

The longest sequential prefix is:

```text
[3, 4, 5]
```

Its sum is:

```text
3 + 4 + 5 = 12
```

The values `12`, `13`, and `14` are present in the array.

Therefore, the smallest missing integer greater than or equal to `12` is:

```text
15
```

---

## Constraints

```text
1 <= nums.length <= 50
1 <= nums[i] <= 50
```
