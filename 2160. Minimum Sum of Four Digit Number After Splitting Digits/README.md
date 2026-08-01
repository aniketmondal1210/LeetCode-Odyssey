# Minimum Sum of Two Numbers Formed from Four Digits

## Problem Statement

You are given a positive integer `num` consisting of **exactly four digits**.

Split the four digits into two new integers `new1` and `new2` such that:

- Every digit is used exactly once.
- Leading zeros are allowed.
- Return the **minimum possible value of `new1 + new2`**.

---

## Examples

### Example 1

**Input**

```text
num = 2932
```

**Output**

```text
52
```

**Explanation**

Digits:

```text
2, 2, 3, 9
```

After sorting:

```text
2, 2, 3, 9
```

Form the numbers:

```text
new1 = 23
new2 = 29
```

Sum:

```text
23 + 29 = 52
```

This is the minimum possible sum.

---

### Example 2

**Input**

```text
num = 4009
```

**Output**

```text
13
```

**Explanation**

Digits:

```text
4, 0, 0, 9
```

After sorting:

```text
0, 0, 4, 9
```

Form the numbers:

```text
new1 = 04 = 4
new2 = 09 = 9
```

Sum:

```text
4 + 9 = 13
```

---

## Constraints:

- 1000 <= num <= 9999

---
