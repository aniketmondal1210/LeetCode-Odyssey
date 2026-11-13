# Maximum Possible Sum after Rearranging Digits

## Problem Description

You are given an integer array `nums` of length `n` and an integer `k`. 

In one operation, you may choose any element of `nums` and rearrange its decimal digits in any order to form a new integer. Return the maximum possible sum of the array after performing at most `k` operations.

---

## Examples

### Example 1
- **Input:** `nums = [123, 45], k = 1`
- **Output:** `366`
- **Explanation:** 
  - Choose `nums[0] = 123` and rearrange its digits to form `321`.
  - The array becomes `[321, 45]`. Total sum: $321 + 45 = 366$.

### Example 2
- **Input:** `nums = [102, 90, 14], k = 2`
- **Output:** `341`
- **Explanation:** 
  - Choose `nums[0] = 102` and rearrange to form `210`.
  - Choose `nums[2] = 14` and rearrange to form `41`.
  - The array becomes `[210, 90, 41]`. Total sum: $210 + 90 + 41 = 341$.

---

## Constraints

- $1 \le n == \text{nums.length} \le 10^5$
- $1 \le \text{nums}[i] \le 10^9$
- $1 \le k \le n$

---
