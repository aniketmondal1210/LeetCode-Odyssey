# Count Special Subarrays of Length 3

## Problem Statement
You are given an integer array `nums`.

Your task is to **count the number of subarrays of length exactly 3** such that:

> The sum of the **first and third elements** of the subarray is **exactly half of the middle element**.

Formally, for a subarray `[nums[i], nums[i+1], nums[i+2]]`, it must satisfy:

nums[i] + nums[i+2] == nums[i+1] / 2


---

## Examples

### Example 1
**Input:**

nums = [1, 2, 1, 4, 1]


**Output:**

1


**Explanation:**
Possible subarrays of length 3:
- `[1, 2, 1]` → `1 + 1 = 2`, but `2 / 2 = 1` ❌
- `[2, 1, 4]` → `2 + 4 = 6`, but `1 / 2 = 0.5` ❌
- `[1, 4, 1]` → `1 + 1 = 2` and `4 / 2 = 2` ✅  

Only one valid subarray exists.

---

### Example 2
**Input:**

nums = [1, 1, 1]


**Output:**

0


**Explanation:**
- `[1, 1, 1]` → `1 + 1 = 2`, but `1 / 2 = 0.5` ❌  

No valid subarray.

---

## Constraints

- 3 <= nums.length <= 100
- -100 <= nums[i] <= 100

---
