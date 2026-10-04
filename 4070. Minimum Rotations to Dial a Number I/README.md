# Minimum Rotations to Dial Digits

## Problem Description

You are given a string `s` of length 10 consisting of digits `'0'` through `'9'`.

A circular dial contains digits `0` to `9` in order, where `0` and `9` are adjacent. The pointer initially points to `0`.

To dial each digit in `s` sequentially, you rotate the pointer to the target digit in either clockwise or counterclockwise direction to minimize the distance. Dialing a digit that the pointer already points to requires `0` rotations.

Return the **minimum total number of rotations** needed to dial all digits in `s`.

---

## Distance Formula

For any two adjacent pointer positions $a$ and $b$ on a 10-digit circular dial, the minimum distance is given by:

$$	ext{distance}(a, b) = \min(|a - b|, 10 - |a - b|)$$

---

## Examples

### Example 1
- **Input:** `s = "0192837465"`
- **Output:** `25`
- **Explanation:**
  - $0 	o 0$: $\min(|0-0|, 10-0) = 0$
  - $0 	o 1$: $\min(|0-1|, 10-1) = 1$
  - $1 	o 9$: $\min(|1-9|, 10-8) = 2$
  - $9 	o 2$: $\min(|9-2|, 10-7) = 3$
  - $2 	o 8$: $\min(|2-8|, 10-6) = 4$
  - $8 	o 3$: $\min(|8-3|, 10-5) = 5$
  - $3 	o 7$: $\min(|3-7|, 10-4) = 4$
  - $7 	o 4$: $\min(|7-4|, 10-3) = 3$
  - $4 	o 6$: $\min(|4-6|, 10-2) = 2$
  - $6 	o 5$: $\min(|6-5|, 10-1) = 1$
  - **Total:** $0 + 1 + 2 + 3 + 4 + 5 + 4 + 3 + 2 + 1 = 25$.

### Example 2
- **Input:** `s = "1200210200"`
- **Output:** `12`
- **Explanation:** Total rotations = $1 + 1 + 2 + 0 + 2 + 1 + 1 + 2 + 2 + 0 = 12$.

---

## Constraints

- `s.length == 10`
- `s` consists only of digits `'0'` through `'9'`.

---
