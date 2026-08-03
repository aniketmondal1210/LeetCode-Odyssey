# Count Valid Subarrays Based on Even/Odd Ratio

## Problem Statement

You are given:

- An integer array `nums`.
- Two integers `a` and `b`.

For every subarray:

- Let `x` be the number of **even** elements.
- Let `y` be the number of **odd** elements.

The subarray is **valid** if:

- `y > 0`
- \(\frac{x}{y} \le \frac{a}{b}\)

Return the number of valid subarrays.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2,1,2]
a = 3
b = 2
```

**Output**

```text
7
```

**Explanation**

Valid subarrays:

| Subarray | Even | Odd | Ratio |
|----------|-----:|----:|------:|
| [1] | 0 | 1 | 0 |
| [1,2] | 1 | 1 | 1 |
| [1,2,1] | 1 | 2 | 1/2 |
| [1,2,1,2] | 2 | 2 | 1 |
| [2,1] | 1 | 1 | 1 |
| [1] | 0 | 1 | 0 |
| [1,2] | 1 | 1 | 1 |

Answer = **7**

---

### Example 2

**Input**

```text
nums = [2,2,1]
a = 2
b = 1
```

**Output**

```text
3
```

**Explanation**

Valid subarrays:

```text
[2,2,1]
[2,1]
[1]
```

Answer = **3**

---

### Example 3

**Input**

```text
nums = [2,2,2]
a = 1
b = 1
```

**Output**

```text
0
```

**Explanation**

Every subarray has `0` odd numbers, so none are valid.

---

## Constraints:

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- 1 <= a, b <= 1000

---
