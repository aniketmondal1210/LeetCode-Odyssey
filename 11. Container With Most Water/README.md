# Container With Most Water

## Problem Description

You are given an integer array `height` of length $n$. There are $n$ vertical lines drawn such that the two endpoints of the $i\text{-th}$ line are at $(i, 0)$ and $(i, \text{height}[i])$.

Find two lines that, together with the x-axis, form a container that stores the **maximum amount of water**.

> **Note:** You may not slant the container.

---

## Examples

### Example 1
- **Input:** `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- **Output:** `49`
- **Explanation:** The maximum area is formed between line at index `1` ($\text{height} = 8$) and index `8` ($\text{height} = 7$).
  $$\text{Area} = \min(8, 7) \times (8 - 1) = 7 \times 7 = 49$$

### Example 2
- **Input:** `height = [1, 1]`
- **Output:** `1`
- **Explanation:** 
  $$\text{Area} = \min(1, 1) \times (1 - 0) = 1 \times 1 = 1$$

---

## Constraints

- $n = \text{height.length}$
- $2 \le n \le 10^5$
- $0 \le \text{height}[i] \le 10^4$

---
