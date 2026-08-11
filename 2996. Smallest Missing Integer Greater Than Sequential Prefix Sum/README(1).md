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

## Approach

1. Start with the first element of `nums` as the sum of the sequential prefix.
2. Traverse the array from the second element.
3. Continue adding elements while each element is exactly `1` greater than the previous element.
4. Stop when the sequential property is broken.
5. Store the sum of the longest sequential prefix.
6. Use a set to store all elements of `nums`.
7. Starting from the calculated sum, increment the value until a number not present in the set is found.
8. Return that number.

---

## Complexity

### Time Complexity

```text
O(n)
```

The array is traversed to find the sequential prefix and to build the set. The search for the missing value is also bounded by the constraints.

### Auxiliary Space

```text
O(n)
```

A set is used to store the elements of `nums`.

---

## Constraints

```text
1 <= nums.length <= 50
1 <= nums[i] <= 50
```
