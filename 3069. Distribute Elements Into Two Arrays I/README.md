# Distribute Elements Into Two Arrays I

## Problem

You are given a **1-indexed** array `nums` of distinct integers.

Create two arrays:

- `arr1`
- `arr2`

Follow these rules:

1. Append `nums[1]` to `arr1`.
2. Append `nums[2]` to `arr2`.
3. For every `i ≥ 3`:
   - If the last element of `arr1` is greater than the last element of `arr2`, append `nums[i]` to `arr1`.
   - Otherwise, append `nums[i]` to `arr2`.

Finally, return the array formed by concatenating:

```text
arr1 + arr2
```

---

## Example 1

### Input

```text
nums = [2,1,3]
```

### Output

```text
[2,3,1]
```

### Explanation

Initially:

```text
arr1 = [2]
arr2 = [1]
```

Since:

```text
2 > 1
```

append `3` to `arr1`.

```text
arr1 = [2,3]
arr2 = [1]
```

Result:

```text
[2,3,1]
```

---

## Example 2

### Input

```text
nums = [5,4,3,8]
```

### Output

```text
[5,3,4,8]
```

### Explanation

After first two operations:

```text
arr1 = [5]
arr2 = [4]
```

For `3`:

```text
5 > 4
```

append to `arr1`.

```text
arr1 = [5,3]
```

For `8`:

```text
3 < 4
```

append to `arr2`.

```text
arr2 = [4,8]
```

Result:

```text
[5,3,4,8]
```

---

## Constraints:

- 3 <= n <= 50
- 1 <= nums[i] <= 100
- All elements in nums are distinct.

---
