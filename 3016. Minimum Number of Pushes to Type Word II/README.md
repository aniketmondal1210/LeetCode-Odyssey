# Minimum Number of Pushes to Type Word II

## Problem Statement

You are given a string `word` consisting of lowercase English letters.

A telephone keypad has **8 usable keys** (`2` to `9`). You may remap the letters to these keys in any way, subject to:

- Every letter is assigned to exactly one key.
- A key may contain any number of letters.
- The **first** letter on a key requires **1 push**, the **second** requires **2 pushes**, and so on.

Your task is to determine the **minimum total number of key presses** needed to type `word`.

---

## Examples

### Example 1

**Input**

```text
word = "abcde"
```

**Output**

```text
5
```

**Explanation**

Each letter can be placed as the first letter on a different key.

```text
a → 1 push
b → 1 push
c → 1 push
d → 1 push
e → 1 push

Total = 5
```

---

### Example 2

**Input**

```text
word = "xyzxyzxyzxyz"
```

**Output**

```text
12
```

**Explanation**

Frequencies:

```text
x = 4
y = 4
z = 4
```

Assign each to the first position of a different key.

```text
4 × 1 + 4 × 1 + 4 × 1 = 12
```

---

### Example 3

**Input**

```text
word = "aabbccddeeffgghhiiiiii"
```

**Output**

```text
24
```

**Explanation**

Frequency table:

```text
i = 6
a,b,c,d,e,f,g,h = 2 each
```

Assign the highest-frequency letters to positions requiring the fewest pushes.

One optimal assignment:

```text
i → 1 push
a,b,c,d,e,f,g → 1 push
h → 2 pushes

Total = 6×1 + 7×2×1 + 2×2 = 24
```

---

## Constraints:

- 1 <= word.length <= 10^5
- word consists of lowercase English letters.

---
