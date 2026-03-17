# Total Number of Commas from 1 to n

## Problem Statement

Given an integer **n**, count the **total number of commas** used when writing all numbers from:

```
1 to n (inclusive)
```

using **standard number formatting**.

### Standard Formatting Rule

- A **comma is inserted after every 3 digits from the right**.
- Numbers with **fewer than 4 digits have no commas**.

---

# Examples

### Example 1

**Input**
```
n = 1002
```

Numbers with commas:

```
1,000
1,001
1,002
```

Each contains **1 comma**.

Total commas:

```
3
```

**Output**
```
3
```

---

### Example 2

**Input**
```
n = 998
```

All numbers are **less than 1000**, so:

```
No commas used
```

**Output**
```
0
```

---

## Constraints:

- 1 <= n <= 10^5

---
