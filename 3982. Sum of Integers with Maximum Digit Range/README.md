# Sum of Integers with Maximum Digit Range

## Problem

You are given an integer array `nums`.

The **digit range** of an integer is defined as:

```text
largest digit − smallest digit
```

For example:

```text
5724 → largest = 7, smallest = 2
Digit Range = 7 − 2 = 5
```

Return the **sum of all integers** whose digit range is equal to the **maximum digit range** among all integers in the array.

---

## Examples

### Example 1

**Input**

```text
nums = [5724,111,350]
```

**Output**

```text
6074
```

**Explanation**

| Number | Largest Digit | Smallest Digit | Digit Range |
|--------|---------------|----------------|------------:|
| 5724 | 7 | 2 | 5 |
| 111 | 1 | 1 | 0 |
| 350 | 5 | 0 | 5 |

The maximum digit range is **5**.

Numbers with this digit range are:

```text
5724 + 350 = 6074
```

---

### Example 2

**Input**

```text
nums = [90,900]
```

**Output**

```text
990
```

**Explanation**

| Number | Largest Digit | Smallest Digit | Digit Range |
|--------|---------------|----------------|------------:|
| 90 | 9 | 0 | 9 |
| 900 | 9 | 0 | 9 |

The maximum digit range is **9**.

Therefore:

```text
90 + 900 = 990
```

---

## Constraints:

- 1 <= nums.length <= 100
- 10 <= nums[i] <= 10^5

---
