# Number of Arithmetic Triplets

## Problem Description

You are given a **0-indexed**, **strictly increasing** integer array `nums` and a positive integer `diff`. A triplet `(i, j, k)` is an **arithmetic triplet** if the following conditions are met:

1. $i < j < k$
2. $\text{nums}[j] - \text{nums}[i] == \text{diff}$
3. $\text{nums}[k] - \text{nums}[j] == \text{diff}$

Return the **number of unique arithmetic triplets**.

---

## Examples

### Example 1
- **Input:** `nums = [0, 1, 4, 6, 7, 10]`, `diff = 3`
- **Output:** `2`
- **Explanation:**
  - `(1, 2, 4)` is an arithmetic triplet: $\text{nums}[2] - \text{nums}[1] = 4 - 1 = 3$ and $\text{nums}[4] - \text{nums}[2] = 7 - 4 = 3$.
  - `(2, 4, 5)` is an arithmetic triplet: $\text{nums}[4] - \text{nums}[2] = 7 - 4 = 3$ and $\text{nums}[5] - \text{nums}[4] = 10 - 7 = 3$.

### Example 2
- **Input:** `nums = [4, 5, 6, 7, 8, 9]`, `diff = 2`
- **Output:** `2`
- **Explanation:**
  - `(0, 2, 4)` is an arithmetic triplet: $\text{nums}[2] - \text{nums}[0] = 6 - 4 = 2$ and $\text{nums}[4] - \text{nums}[2] = 8 - 6 = 2$.
  - `(1, 3, 5)` is an arithmetic triplet: $\text{nums}[3] - \text{nums}[1] = 7 - 5 = 2$ and $\text{nums}[5] - \text{nums}[3] = 9 - 7 = 2$.

---

## Constraints

- $3 \le {nums.length} \le 200$
- $0 \le {nums}[i] \le 200$
- $1 \le {diff} \le 50$
- `nums` is **strictly increasing**.

---
