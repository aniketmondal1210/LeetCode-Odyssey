# Absolute Difference Between k Largest and k Smallest Elements

You are given an integer array `nums` and an integer `k`.

Your task is to compute the **absolute difference** between:
- the sum of the **k largest elements**, and
- the sum of the **k smallest elements** in the array.

Return the resulting integer.

---

## Examples

### Example 1

Input:

nums = [5, 2, 2, 4]

k = 2

Output:

5


**Explanation:**
- k largest elements → `4` and `5`, sum = `9`
- k smallest elements → `2` and `2`, sum = `4`
- Absolute difference → `|9 - 4| = 5`

---

### Example 2

Input:

nums = [100]

k = 1

Output:

0


**Explanation:**
- Both largest and smallest elements are `100`
- Absolute difference → `|100 - 100| = 0`

---

### Constraints:

- 1 <= n == nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= n

---
