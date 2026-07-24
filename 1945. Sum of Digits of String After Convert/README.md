# Sum of Digits of String After Convert

## Problem

You are given:

- A string `s` consisting of lowercase English letters.
- An integer `k`.

Perform the following operations:

1. Convert each letter to its alphabetical position:
   - `'a' -> 1`
   - `'b' -> 2`
   - ...
   - `'z' -> 26`
2. Concatenate these numbers to form an integer.
3. Replace the integer with the **sum of its digits**.
4. Repeat the digit-sum operation exactly **k** times.

Return the final integer.

---

## Examples

### Example 1

**Input**

```text
s = "iiii"
k = 1
```

**Output**

```text
36
```

**Explanation**

```text
i -> 9

9999

9 + 9 + 9 + 9 = 36
```

---

### Example 2

**Input**

```text
s = "leetcode"
k = 2
```

**Output**

```text
6
```

**Explanation**

```text
l -> 12
e -> 5
e -> 5
t -> 20
c -> 3
o -> 15
d -> 4
e -> 5

12552031545

First transform:
1+2+5+5+2+0+3+1+5+4+5 = 33

Second transform:
3+3 = 6
```

---

### Example 3

**Input**

```text
s = "zbax"
k = 2
```

**Output**

```text
8
```

**Explanation**

```text
z -> 26
b -> 2
a -> 1
x -> 24

262124

First transform:
2+6+2+1+2+4 = 17

Second transform:
1+7 = 8
```

---

## Constraints:

- 1 <= s.length <= 100
- 1 <= k <= 10
- s consists of lowercase English letters.

---
