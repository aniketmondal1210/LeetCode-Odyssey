# Sequential Digits

## Problem

An integer has **sequential digits** if every digit is exactly **one greater** than the previous digit.

Given two integers `low` and `high`, return a **sorted list** of all sequential digit numbers in the inclusive range `[low, high]`.

---

## Examples

### Example 1

**Input**

```text
low = 100
high = 300
```

**Output**

```text
[123, 234]
```

**Explanation**

The sequential digit numbers between `100` and `300` are:

- `123`
- `234`

---

### Example 2

**Input**

```text
low = 1000
high = 13000
```

**Output**

```text
[1234, 2345, 3456, 4567, 5678, 6789, 12345]
```

**Explanation**

These are all the sequential digit numbers within the given range.

---

## Constraints:

- 10 <= low <= high <= 10^9

---
