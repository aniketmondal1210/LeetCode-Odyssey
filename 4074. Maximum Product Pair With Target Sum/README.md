# Maximum Product Valid Pair

## Problem Description

You are given an integer array `nums` and an integer `target`.

A pair of distinct indices $(i, j)$ is valid if:
- `nums[i] + nums[j] == target`
- `nums[i] > nums[j]`

Return a valid pair `[i, j]` whose product `nums[i] * nums[j]` is maximum among all valid pairs. If no valid pair exists, return `[-1, -1]`.

If multiple valid pairs achieve the maximum product, you may return any of them.

---

## Examples

### Example 1
- **Input:** `nums = [1, 2, 3, 4]`, `target = 5`
- **Output:** `[2, 1]`
- **Explanation:** Valid pairs are `(3, 0)` with product $4 	imes 1 = 4$ and `(2, 1)` with product $3 	imes 2 = 6$. The second pair has the larger product.

### Example 2
- **Input:** `nums = [-3, -1, 4, 2]`, `target = 1`
- **Output:** `[3, 1]`
- **Explanation:** Valid pairs are `(2, 0)` with product $-12$ and `(3, 1)` with product $-2$. Since $-2 > -12$, the pair at indices `(3, 1)` is chosen.

### Example 3
- **Input:** `nums = [3, 3, 5]`, `target = 6`
- **Output:** `[-1, -1]`
- **Explanation:** No valid pair exists since `nums[0]` and `nums[1]` equal 3 and violate the strict inequality `nums[i] > nums[j]`.

---

## Constraints

- $2 \le 	{nums.length} \le 100$
- $-100 \le 	{nums}[i], 	{target} \le 100$

---
