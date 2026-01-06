# Sum of Squares of Distinct Counts of All Subarrays

## Problem Statement
You are given a **0-indexed integer array** `nums`.

For any subarray `nums[i..j]` (where `0 ≤ i ≤ j < nums.length`), the **distinct count** is defined as the number of **distinct values** present in that subarray.

Your task is to **return the sum of the squares of distinct counts of all possible non-empty subarrays** of `nums`.

---

## Definitions
- **Subarray**: A contiguous non-empty sequence of elements within an array.
- **Distinct Count**: Number of unique elements in a subarray.

---

## Examples

### Example 1
**Input:**

nums = [1, 2, 1]


**Output:**

15


**Explanation:**

All possible subarrays and their distinct counts:

| Subarray   | Distinct Count | Square |
|------------|---------------|--------|
| [1]        | 1             | 1      |
| [2]        | 1             | 1      |
| [1]        | 1             | 1      |
| [1, 2]     | 2             | 4      |
| [2, 1]     | 2             | 4      |
| [1, 2, 1]  | 2             | 4      |

**Total Sum:**  
`1 + 1 + 1 + 4 + 4 + 4 = 15`

---

### Example 2
**Input:**

nums = [1, 1]


**Output:**

3


**Explanation:**

| Subarray | Distinct Count | Square |
|--------|---------------|--------|
| [1]    | 1             | 1      |
| [1]    | 1             | 1      |
| [1,1]  | 1             | 1      |

**Total Sum:**  
`1 + 1 + 1 = 3`

---

## Constraints

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100


---
