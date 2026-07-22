# Find the Key of Three Numbers

## Problem

You are given three positive integers `num1`, `num2`, and `num3`.

The **key** is a four-digit number formed as follows:

1. If any number has fewer than **4 digits**, pad it with leading zeros.
2. For each of the four digit positions, take the **minimum** digit among the corresponding digits of the three numbers.
3. Return the resulting number **without leading zeros** (if any).

---

## Examples

### Example 1

**Input**

```text
num1 = 1
num2 = 10
num3 = 1000
```

**Output**

```text
0
```

**Explanation**

After padding:

```text
num1 = 0001
num2 = 0010
num3 = 1000
```

Take the minimum digit at each position:

```text
min(0,0,1) = 0
min(0,0,0) = 0
min(0,1,0) = 0
min(1,0,0) = 0
```

Key:

```text
0000 → 0
```

---

### Example 2

**Input**

```text
num1 = 987
num2 = 879
num3 = 798
```

**Output**

```text
777
```

**Explanation**

After padding:

```text
0987
0879
0798
```

Minimum digits:

```text
0 7 7 7
```

Key:

```text
0777 → 777
```

---

### Example 3

**Input**

```text
num1 = 1
num2 = 2
num3 = 3
```

**Output**

```text
1
```

**Explanation**

After padding:

```text
0001
0002
0003
```

Minimum digits:

```text
0001 → 1
```

---

## Constraints:

- 1 <= num1, num2, num3 <= 9999

---
