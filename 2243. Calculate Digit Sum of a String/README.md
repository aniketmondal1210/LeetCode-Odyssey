# Calculate Digit Sum of a String

## Problem Description

You are given a string `s` consisting of digits and an integer `k`. A round can be completed if the length of `s` is greater than `k`. In one round:
1. Divide `s` into consecutive groups of size `k` (the last group can be smaller).
2. Replace each group with a string representing the sum of all its digits.
3. Merge consecutive groups together to form a new string. If the length of the string is still greater than `k`, repeat from step 1.

Return `s` after all rounds have been completed.

---

## Examples

### Example 1
- **Input:** `s = "11111222223"`, `k = 3`
- **Output:** `"135"`
- **Explanation:** 
  - **Round 1:** Groups are `"111"`, `"112"`, `"222"`, and `"23"`. Sums are `3`, `4`, `6`, and `5`. String becomes `"3465"`.
  - **Round 2:** Groups are `"346"` and `"5"`. Sums are `13` and `5`. String becomes `"135"`.
  - Length is now $\le k$, so the process terminates.

### Example 2
- **Input:** `s = "00000000"`, `k = 3`
- **Output:** `"000"`
- **Explanation:** Groups are `"000"`, `"000"`, and `"00"`. Sums are `0`, `0`, and `0`. String becomes `"000"`, whose length equals `k`.

---

## Constraints

- $1 \le \text{s.length} \le 100$
- $2 \le k \le 100$
- `s` consists of digits only.

---
