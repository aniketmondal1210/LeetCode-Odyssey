# Minimum Cost to Split Integer into Ones

## Problem Statement

You are given an integer `n`.

In one operation, you may split an integer `x` into two positive integers `a` and `b` such that:

```
a + b = x
```

The cost of this operation is:

```
a * b
```

Return the **minimum total cost** required to split the integer `n` into `n` ones.

---

## Examples

### Example 1

**Input**
```
n = 3
```

**Output**
```
3
```

**Explanation**

One optimal sequence:

| x | a | b | Cost (a*b) |
|---|---|---|------------|
| 3 | 1 | 2 | 2 |
| 2 | 1 | 1 | 1 |

Total Cost = 2 + 1 = **3**

---

### Example 2

**Input**
```
n = 4
```

**Output**
```
6
```

**Explanation**

One optimal sequence:

| x | a | b | Cost (a*b) |
|---|---|---|------------|
| 4 | 2 | 2 | 4 |
| 2 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 |

Total Cost = 4 + 1 + 1 = **6**

---

## Constraints:

- 1 <= n <= 500

---
