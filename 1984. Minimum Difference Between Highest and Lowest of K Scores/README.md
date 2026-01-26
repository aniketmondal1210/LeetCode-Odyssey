# Minimum Difference Between Highest and Lowest of K Scores

## Problem Statement
You are given:
- A 0-indexed integer array `nums`, where `nums[i]` represents the score of the *i-th* student
- An integer `k`

You must **pick scores of any `k` students** such that the **difference between the highest and lowest scores** among the selected students is **minimized**.

Return this **minimum possible difference**.

---

## Examples

### Example 1
**Input**

nums = [90], k = 1

**Output**

0


**Explanation**  
Only one score is selected, so the difference is `90 - 90 = 0`.

---

### Example 2
**Input**

nums = [9,4,1,7], k = 2

**Output**

2


**Explanation**  
After sorting: `[1,4,7,9]`  
Possible differences for `k = 2`:
- `4 - 1 = 3`
- `7 - 4 = 3`
- `9 - 7 = 2` ← minimum

---

## Constraints

- 1 <= k <= nums.length <= 1000
- 0 <= nums[i] <= 10^5


---
