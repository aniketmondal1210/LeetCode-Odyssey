# Minimum Element After Digit Sum Replacement

## Problem Statement
You are given an integer array `nums`.

Replace each element in `nums` with the **sum of its digits**, and return the **minimum element** after all replacements.

---

## Examples

### Example 1
**Input:**

nums = [10, 12, 13, 14]

**Output:**

1

**Explanation:**  
After replacing each element with the sum of its digits:  
`[10, 12, 13, 14] → [1, 3, 4, 5]`  
Minimum element = `1`.

---

### Example 2
**Input:**

nums = [1, 2, 3, 4]

**Output:**

1

**Explanation:**  
After replacing: `[1, 2, 3, 4] → [1, 2, 3, 4]`  
Minimum element = `1`.

---

### Example 3
**Input:**

nums = [999, 19, 199]

**Output:**

10

**Explanation:**  
After replacing: `[999, 19, 199] → [27, 10, 19]`  
Minimum element = `10`.

---

## Constraints

1 <= nums.length <= 100
1 <= nums[i] <= 10^4

---
