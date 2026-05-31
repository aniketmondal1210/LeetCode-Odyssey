# Score of an Integer

## Problem Statement

Given an integer `n`, its score is defined as:

```text
Σ (digit × frequency of that digit)
```

for all distinct digits present in `n`.

Return the score.

---

# Example 1

## Input

```text
n = 122
```

## Explanation

```text
Digit 1 appears 1 time:
1 × 1 = 1

Digit 2 appears 2 times:
2 × 2 = 4

Score = 1 + 4 = 5
```

## Output

```text
5
```

---

# Example 2

## Input

```text
n = 101
```

## Explanation

```text
Digit 0 appears 1 time:
0 × 1 = 0

Digit 1 appears 2 times:
1 × 2 = 2

Score = 0 + 2 = 2
```

## Output

```text
2
```

---

## Constraints:

- 1 <= n <= 10^9

---
