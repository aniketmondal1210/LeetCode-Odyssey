# Find the Concatenation Value of an Array

## Idea

Use two pointers:

- `i` → first element
- `j` → last element

For each pair:

```text
concatenation(a, b)
= a followed by digits of b
```

Mathematically:

```text
concat(a, b) = a * 10^(digits in b) + b
```

If only one element remains, add it directly.

---

# Example 1

## Input

```text
nums = [7,52,2,4]
```

### Operations

```text
7 and 4  -> 74
52 and 2 -> 522
```

### Sum

```text
74 + 522 = 596
```

## Output

```text
596
```

---

# Example 2

## Input

```text
nums = [5,14,13,8,12]
```

### Operations

```text
5 and 12  -> 512
14 and 8  -> 148
13        -> 13
```

### Sum

```text
512 + 148 + 13 = 673
```

## Output

```text
673
```

---

## Constraints:

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4

---
