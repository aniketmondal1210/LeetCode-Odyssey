# Check if an Integer is Good

## Problem

Given a positive integer `n`:

- `digitSum` = sum of all digits of `n`
- `squareSum` = sum of squares of all digits of `n`

An integer is called **good** if:

```text
squareSum - digitSum >= 50
```

Return:

```text
true  -> if n is good
false -> otherwise
```

---

## Example 1

### Input

```text
n = 1000
```

### Output

```text
false
```

### Explanation

Digits:

```text
1, 0, 0, 0
```

digitSum:

```text
1 + 0 + 0 + 0 = 1
```

squareSum:

```text
1² + 0² + 0² + 0² = 1
```

Difference:

```text
1 - 1 = 0
```

Since:

```text
0 < 50
```

Answer:

```text
false
```

---

## Example 2

### Input

```text
n = 19
```

### Output

```text
true
```

### Explanation

Digits:

```text
1, 9
```

digitSum:

```text
1 + 9 = 10
```

squareSum:

```text
1² + 9² = 1 + 81 = 82
```

Difference:

```text
82 - 10 = 72
```

Since:

```text
72 >= 50
```

Answer:

```text
true
```

---

## Constraints:

- 1 <= n <= 10^9

---
