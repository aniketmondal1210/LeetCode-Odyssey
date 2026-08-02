# Maximum Strength of a Pair

## Problem Statement

You are given an integer array `nums`.

Choose **exactly one pair** of distinct indices `(i, j)`.

The **strength** of the pair is defined as:

\[
\frac{nums[i] \times nums[j]}{\gcd(nums[i], nums[j])^2}
\]

where `gcd(a, b)` is the greatest common divisor of `a` and `b`.

Return the **maximum strength** among all possible pairs.

---

## Examples

### Example 1

**Input**

```text
nums = [2,3,5]
```

**Output**

```text
15
```

**Explanation**

Possible strengths:

```text
(2,3) = 6 / 1² = 6
(2,5) = 10 / 1² = 10
(3,5) = 15 / 1² = 15
```

Maximum = **15**

---

### Example 2

**Input**

```text
nums = [4,6,8]
```

**Output**

```text
12
```

**Explanation**

```text
(4,6) = 24 / 2² = 6
(4,8) = 32 / 4² = 2
(6,8) = 48 / 2² = 12
```

Maximum = **12**

---

### Example 3

**Input**

```text
nums = [3,3]
```

**Output**

```text
1
```

**Explanation**

```text
Strength = (3 × 3) / 3²
         = 9 / 9
         = 1
```

---

## Constraints:

- 2 <= nums.length <= 2000
- 1 <= nums[i] <= 10^5

---
