# Sum of Elements with Frequency Divisible by k

## Problem Statement

Given an integer array `nums` and an integer `k`, return the **sum of all elements** in `nums` whose frequency is **divisible by k**.

If no such elements exist, return **0**.

Note: An element is included in the sum **as many times as it appears** if its total frequency is divisible by `k`.

---

## Input

* An integer array `nums`.
* An integer `k`.

**Constraints:**

```
1 ≤ nums.length ≤ 100
1 ≤ nums[i] ≤ 100
1 ≤ k ≤ 100
```

---

## Output

Return an integer — the sum of all elements whose frequency is divisible by `k`.

---

## 💡 Examples

### Example 1

**Input:**

```
nums = [1, 2, 2, 3, 3, 3, 3, 4]
k = 2
```

**Output:**

```
16
```

**Explanation:**

```
1 → appears 1 time (not divisible by 2)
2 → appears 2 times (divisible by 2)
3 → appears 4 times (divisible by 2)
4 → appears 1 time (not divisible by 2)
Sum = 2 + 2 + 3 + 3 + 3 + 3 = 16
```

---

### Example 2

**Input:**

```
nums = [1, 2, 3, 4, 5]
k = 2
```

**Output:**

```
0
```

**Explanation:**

```
No elements have a frequency divisible by 2 → sum = 0
```

---

### Example 3

**Input:**

```
nums = [4, 4, 4, 1, 2, 3]
k = 3
```

**Output:**

```
12
```

**Explanation:**

```
4 → appears 3 times (divisible by 3)
1, 2, 3 → appear once each (not divisible by 3)
Sum = 4 + 4 + 4 = 12
```

---
