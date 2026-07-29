# Sort Integers by Power Value

## Problem

The **power** of an integer `x` is the number of steps required to transform it into `1` using the following rules:

- If `x` is even, `x = x / 2`
- If `x` is odd, `x = 3 * x + 1`

Given three integers `lo`, `hi`, and `k`:

1. Compute the power value for every integer in the range `[lo, hi]`.
2. Sort the integers by:
   - Increasing power value.
   - If powers are equal, increasing integer value.
3. Return the **kth** integer in the sorted list.

---

## Examples

### Example 1

**Input**

```text
lo = 12
hi = 15
k = 2
```

**Output**

```text
13
```

**Explanation**

```text
Power(12) = 9
Power(13) = 9
Power(14) = 17
Power(15) = 17

Sorted order:
[12, 13, 14, 15]

The 2nd element is 13.
```

---

### Example 2

**Input**

```text
lo = 7
hi = 11
k = 4
```

**Output**

```text
7
```

**Explanation**

```text
Power values:

7  -> 16
8  -> 3
9  -> 19
10 -> 6
11 -> 14

Sorted order:
[8, 10, 11, 7, 9]

The 4th element is 7.
```

---

## Constraints:

- 1 <= lo <= hi <= 1000
- 1 <= k <= hi - lo + 1

---
