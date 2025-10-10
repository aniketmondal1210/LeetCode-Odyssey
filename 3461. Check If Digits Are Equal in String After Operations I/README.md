# Check Equal Last Two Digits After Modulo Sum Operation

## Problem Statement

You are given a string `s` consisting of digits. Perform the following operation repeatedly until the string has **exactly two digits**:

* For each pair of consecutive digits in `s`, starting from the first digit, calculate a new digit as the **sum of the two digits modulo 10**.
* Replace `s` with the sequence of newly calculated digits, maintaining the order in which they are computed.

Return `true` if the final two digits in `s` are the same; otherwise, return `false`.

---

## Input

A string `s` consisting of digits.

**Constraints:**

```
3 ≤ s.length ≤ 100
s consists only of digits.
```

---

## Output

Return `true` if the final two digits in the string are the same after performing the given operation repeatedly; otherwise, return `false`.

---

## Examples

### Example 1

**Input:**

```
s = "3902"
```

**Output:**

```
true
```

**Explanation:**

```
Initial: 3902
(3+9)%10=2, (9+0)%10=9, (0+2)%10=2 → s = 292
(2+9)%10=1, (9+2)%10=1 → s = 11
Digits are equal → true
```

---

### Example 2

**Input:**

```
s = "34789"
```

**Output:**

```
false
```

**Explanation:**

```
Initial: 34789
→ (3+4)%10=7, (4+7)%10=1, (7+8)%10=5, (8+9)%10=7 → s = 7157
→ (7+1)%10=8, (1+5)%10=6, (5+7)%10=2 → s = 862
→ (8+6)%10=4, (6+2)%10=8 → s = 48
Since 4 ≠ 8 → false
```

---
