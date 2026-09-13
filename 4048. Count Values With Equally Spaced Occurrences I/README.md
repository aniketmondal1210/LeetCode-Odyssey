# Count Distinct Special Integers

## Problem Description

You are given an integer array `nums`. 

An integer `x` is called **special** if it meets both of the following conditions:
1. `x` appears **exactly three times** in `nums`.
2. All three occurrences of `x` are **equally spaced** in `nums`. That is, if the occurrences of `x` are at indices $i_1 < i_2 < i_3$, then:

$$i_2 - i_1 = i_3 - i_2$$

Return the number of **distinct special integers** in `nums`.

---

## Examples

### Example 1
- **Input:** `nums = [1, 8, 1, 5, 1, 5, 8, 5]`
- **Output:** `2`
- **Explanation:** 
  - `1` occurs at indices `[0, 2, 4]`. $2 - 0 = 4 - 2 = 2$ (Special).
  - `5` occurs at indices `[3, 5, 7]`. $5 - 3 = 7 - 5 = 2$ (Special).
  - `8` occurs only twice at indices `[1, 6]` (Not Special).
  - Total distinct special integers = `2`.

### Example 2
- **Input:** `nums = [8, 8, 8, 8]`
- **Output:** `0`
- **Explanation:** `8` occurs 4 times, which is not *exactly* 3 times.

### Example 3
- **Input:** `nums = [8, 6, 6, 8, 8]`
- **Output:** `0`
- **Explanation:** 
  - `8` occurs at indices `[0, 3, 4]`. $3 - 0 \neq 4 - 3$ (Not equally spaced).
  - `6` occurs only 2 times.

---

## Constraints

- $3 \le \text{nums.length} \le 100$
- $1 \le \text{nums}[i] \le 100$

---
