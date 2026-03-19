# Minimum Bit Changes to Convert n → k

## Problem Statement

You are given two integers **n** and **k**.

You can perform the following operation:

- Choose any bit in **n** that is **1** and change it to **0**.

Return the **minimum number of changes** required to make **n = k**.

If it is **impossible**, return:

```
-1
```

---

# Key Observations

1. You can only:
   ```
   1 → 0
   ```
   (cannot turn 0 → 1)

2. So:
   - If **k has a 1 where n has 0 → impossible**
   - Otherwise, count how many bits need to be turned off

---

# Core Logic

Check:

```
(n & k) == k
```

- If NOT → return `-1`
- If YES → count bits where:
  ```
  n = 1 and k = 0
  ```

That is:

```
count of set bits in (n ^ k)
```

---

# Examples

### Example 1

**Input**
```
n = 13 (1101)
k = 4  (0100)
```

**Steps**

```
1101 → 0100
Change 2 bits
```

**Output**
```
2
```

---

### Example 2

**Input**
```
n = 21
k = 21
```

**Output**
```
0
```

---

### Example 3

**Input**
```
n = 14 (1110)
k = 13 (1101)
```

Here:
```
k has a 1 where n has 0 → impossible
```

**Output**
```
-1
```

---

## Constraints:

- 1 <= n, k <= 10^6

---
