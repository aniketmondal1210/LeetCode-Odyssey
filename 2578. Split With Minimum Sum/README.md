# Minimum Sum of Two Numbers

## Problem Statement

Given a positive integer `num`, split it into two non-negative integers `num1` and `num2` such that:

- The concatenation of `num1` and `num2` is a permutation of `num`.
- The sum of the number of occurrences of each digit in `num1` and `num2` is equal to the number of occurrences of that digit in `num`.
- `num1` and `num2` can contain leading zeros.

Return the **minimum possible sum** of `num1` and `num2`.

### Notes

- It is guaranteed that `num` does not contain any leading zeros.
- The order of occurrence of the digits in `num1` and `num2` may differ from the order of occurrence of the digits in `num`.

---

## Example 1

**Input:**

```text
num = 4325
```

**Output:**

```text
59
```

**Explanation:**

We can split `4325` so that:

```text
num1 = 24
num2 = 35
```

The sum is:

```text
24 + 35 = 59
```

This is the minimum possible sum.

---

## Example 2

**Input:**

```text
num = 687
```

**Output:**

```text
75
```

**Explanation:**

We can split `687` so that:

```text
num1 = 68
num2 = 7
```

The sum is:

```text
68 + 7 = 75
```

This is the minimum possible sum.

---

## Constraints

```text
10 <= num <= 10^9
```
