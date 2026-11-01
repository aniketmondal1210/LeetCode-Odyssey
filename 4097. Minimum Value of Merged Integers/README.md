# Minimum Number Game (or Min Merged Integer)

## Problem Description

You are given an integer array `nums` of even length `n`. You have to merge the elements of `nums` in pairs by merging `nums[0]` with `nums[1]`, `nums[2]` with `nums[3]`, and so on.

To merge two integers, concatenate all the decimal digits of the first integer followed by all the decimal digits of the second integer. Return the minimum value among all the resulting merged integers.

---

## Examples

### Example 1
- **Input:** `nums = [23, 55, 42, 21]`
- **Output:** `2355`
- **Explanation:** 
  - Merging `23` and `55` gives `2355`.
  - Merging `42` and `21` gives `4221`.
  - The minimum value is $\min(2355, 4221) = 2355$.

### Example 2
- **Input:** `nums = [34, 7, 11, 11]`
- **Output:** `347`
- **Explanation:** 
  - Merging `34` and `7` gives `347`.
  - Merging `11` and `11` gives `1111`.
  - The minimum value is $\min(347, 1111) = 347$.

### Example 3
- **Input:** `nums = [9, 20]`
- **Output:** `920`
- **Explanation:** Only one pair `(9, 20)`, giving `920`.

---

## Constraints

- $2 \le n = \text{nums.length} \le 100$
- $n$ is even
- $1 \le \text{nums}[i] \le 1000$

---
