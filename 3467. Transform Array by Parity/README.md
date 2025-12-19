# Transform Array by Parity and Sort

## Problem Statement
You are given an integer array `nums`.  
Transform the array by performing the following operations **in the given order**:

1. Replace each **even** number with `0`.
2. Replace each **odd** number with `1`.
3. Sort the modified array in **non-decreasing order**.

Return the resulting array.

---

## Example 1

### Input

nums = [4, 3, 2, 1]


### Output

[0, 0, 1, 1]


### Explanation
- Even numbers (4, 2) → `0`
- Odd numbers (3, 1) → `1`

After replacement:

[0, 1, 0, 1]


After sorting:

[0, 0, 1, 1]


---

## Example 2

### Input

nums = [1, 5, 1, 4, 2]


### Output

[0, 0, 1, 1, 1]


### Explanation
- Even numbers (4, 2) → `0`
- Odd numbers (1, 5, 1) → `1`

After replacement:

[1, 1, 1, 0, 0]


After sorting:

[0, 0, 1, 1, 1]

---

### Constraints

- 1 ≤ nums.length ≤ 100
- 1 ≤ nums[i] ≤ 1000

---
