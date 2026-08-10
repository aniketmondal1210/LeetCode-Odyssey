# Minimum Sum After Applying Discounts

## Problem Statement

You are given two integer arrays `prices` and `discounts`.

- `prices[i]` represents the price of the `i`th item.
- `discounts[j]` represents a discount percentage.

You may apply discounts subject to the following rules:

- Each discount can be applied to at most one item.
- Each item can receive at most one discount.
- An item may also receive no discount.
- If a discount of `d` percent is applied to an item with price `p`, its final price becomes:

```text
(p * (100 - d)) / 100
```

The final price is not rounded.

Return the minimum possible sum of final prices after assigning discounts optimally.

Answers within `10^-5` of the actual answer will be accepted.

---

## Example 1

**Input:**

```text
prices = [10, 30, 21]
discounts = [50, 60]
```

**Output:**

```text
32.50000
```

**Explanation:**

Apply `discounts[1] = 60` to `prices[1] = 30`:

```text
30 * (100 - 60) / 100 = 12
```

Apply `discounts[0] = 50` to `prices[2] = 21`:

```text
21 * (100 - 50) / 100 = 10.5
```

`prices[0] = 10` receives no discount, so it remains `10`.

The total is:

```text
12 + 10.5 + 10 = 32.5
```

Therefore, the minimum possible sum is:

```text
32.50000
```

---

## Example 2

**Input:**

```text
prices = [100, 70]
discounts = [10, 40, 50]
```

**Output:**

```text
92.00000
```

**Explanation:**

Apply `discounts[2] = 50` to `prices[0] = 100`:

```text
100 * (100 - 50) / 100 = 50
```

Apply `discounts[1] = 40` to `prices[1] = 70`:

```text
70 * (100 - 40) / 100 = 42
```

The total is:

```text
50 + 42 = 92
```

Therefore, the minimum possible sum is:

```text
92.00000
```

---

## Example 3

**Input:**

```text
prices = [7, 3, 9]
discounts = [100, 100]
```

**Output:**

```text
3.00000
```

**Explanation:**

Apply `discounts[0] = 100` to `prices[2] = 9`:

```text
9 * (100 - 100) / 100 = 0
```

Apply `discounts[1] = 100` to `prices[0] = 7`:

```text
7 * (100 - 100) / 100 = 0
```

`prices[1] = 3` receives no discount, so it remains `3`.

The total is:

```text
0 + 0 + 3 = 3
```

Therefore, the minimum possible sum is:

```text
3.00000
```

---

## Constraints

- 1 <= prices.length, discounts.length <= 10^5
- 1 <= prices[i] <= 10^5
- 1 <= discounts[j] <= 100

---
