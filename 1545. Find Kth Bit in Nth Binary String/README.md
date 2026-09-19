# Find K-th Bit in N-th Binary String

## Problem Description

Given two positive integers $n$ and $k$, the binary string $S_n$ is constructed as follows:
- $S_1 = 	ext{"0"}$
- $S_i = S_{i-1} + 	ext{"1"} + 	ext{reverse}(	ext{invert}(S_{i-1}))$ for $i > 1$

Where:
- `+` denotes string concatenation.
- `reverse(x)` reverses the string `x`.
- `invert(x)` inverts all bits in `x` (`0` becomes `1`, and `1` becomes `0`).

Return the **$k$-th bit** in $S_n$ (1-indexed). It is guaranteed that $k$ is valid for the given $n$.

---

## Examples

### Example 1
- **Input:** `n = 3`, `k = 1`
- **Output:** `"0"`
- **Explanation:** $S_3 = 	ext{"0111001"}$. The $1^	ext{st}$ bit is `"0"`.

### Example 2
- **Input:** `n = 4`, `k = 11`
- **Output:** `"1"`
- **Explanation:** $S_4 = 	ext{"011100110110001"}$. The $11^	ext{th}$ bit is `"1"`.

---

## Constraints

- $1 \le n \le 20$
- $1 \le k \le 2^n - 1$

---
