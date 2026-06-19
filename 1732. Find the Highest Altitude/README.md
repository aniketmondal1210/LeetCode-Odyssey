# Find the Highest Altitude

## Problem

A biker starts at altitude:

```text
0
```

You are given an array `gain[]` where:

```text
gain[i]
```

represents the change in altitude between point `i` and point `i + 1`.

Return the **highest altitude** reached during the trip.

---

## Example 1

### Input

```text
gain = [-5, 1, 5, 0, -7]
```

### Output

```text
1
```

### Explanation

Altitudes:

```text
0
0 + (-5) = -5
-5 + 1 = -4
-4 + 5 = 1
1 + 0 = 1
1 + (-7) = -6
```

Altitude sequence:

```text
[0, -5, -4, 1, 1, -6]
```

Highest altitude:

```text
1
```

---

## Example 2

### Input

```text
gain = [-4, -3, -2, -1, 4, 3, 2]
```

### Output

```text
0
```

### Explanation

Altitudes:

```text
[0, -4, -7, -9, -10, -6, -3, -1]
```

Highest altitude:

```text
0
```

---

## Constraints:

- n == gain.length
- 1 <= n <= 100
- -100 <= gain[i] <= 100

---
