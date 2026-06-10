# Sum of Compatible Integers

## Problem

Given two integers `n` and `k`, a positive integer `x` is called **compatible** if:

1. `abs(n - x) <= k`
2. `(n & x) == 0`

Return the **sum of all compatible integers**.

> `&` denotes the bitwise AND operator.

---

## Examples

### Example 1

**Input**

```text
n = 2, k = 3
```

**Output**

```text
10
```

**Explanation**

Valid values of `x` are:

```text
x = 1  -> |2 - 1| = 1, 2 & 1 = 0
x = 4  -> |2 - 4| = 2, 2 & 4 = 0
x = 5  -> |2 - 5| = 3, 2 & 5 = 0
```

Sum:

```text
1 + 4 + 5 = 10
```

---

### Example 2

**Input**

```text
n = 5, k = 1
```

**Output**

```text
0
```

**Explanation**

Possible values are in the range:

```text
[4, 6]
```

None satisfy:

```text
(5 & x) == 0
```

So the answer is `0`.

---

## Constraints:

- 1 <= n <= 100
- 1 <= k <= 100

---
