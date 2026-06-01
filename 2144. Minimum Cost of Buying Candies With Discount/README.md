# Minimum Cost to Buy All Candies

## Key Observation

To maximize the discount, the **most expensive candies should be free** whenever possible.

Sort the costs in **descending order**.

Then process candies in groups of 3:

```text
Buy first candy
Buy second candy
Get third candy free
```

So, after sorting, every 3rd candy (index 2, 5, 8, ...) is free.

---

# Example 1

## Input

```text
cost = [1,2,3]
```

## Sorted

```text
[3,2,1]
```

```text
Buy 3
Buy 2
Free 1
```

## Cost

```text
3 + 2 = 5
```

## Output

```text
5
```

---

# Example 2

## Input

```text
cost = [6,5,7,9,2,2]
```

## Sorted

```text
[9,7,6,5,2,2]
```

```text
Buy 9, 7
Free 6

Buy 5, 2
Free 2
```

## Cost

```text
9 + 7 + 5 + 2 = 23
```

## Output

```text
23
```

---

## Constraints:

- 1 <= cost.length <= 100
- 1 <= cost[i] <= 100

---
