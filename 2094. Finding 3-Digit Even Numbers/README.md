# Finding Distinct 3-Digit Even Numbers

## Problem Description

You are given an integer array `digits`, where each element is a single digit (`0-9`). The array may contain duplicates.

Find all unique 3-digit integers that satisfy the following requirements:
1. The integer consists of the concatenation of three elements from `digits` in any arbitrary order.
2. The integer **does not** have leading zeros (i.e., must be $\ge 100$).
3. The integer is **even** (i.e., ends in `0, 2, 4, 6,` or `8`).

Return a sorted array of all unique integers that satisfy these conditions.

---

## Examples

### Example 1
- **Input:** `digits = [2, 1, 3, 0]`
- **Output:** `[102, 120, 130, 132, 210, 230, 302, 310, 312, 320]`
- **Explanation:** All unique even 3-digit numbers formed without leading zeros using available digits.

### Example 2
- **Input:** `digits = [2, 2, 8, 8, 2]`
- **Output:** `[222, 228, 282, 288, 822, 828, 882]`
- **Explanation:** The digit `8` appears twice, so it can be used at most twice per number.

### Example 3
- **Input:** `digits = [3, 7, 5]`
- **Output:** `[]`
- **Explanation:** No even integers can be formed using odd digits only.

---

## Constraints

- $3 \le \text{digits.length} \le 100$
- $0 \le \text{digits}[i] \le 9$

---
