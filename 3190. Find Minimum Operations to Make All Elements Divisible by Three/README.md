# Minimum Operations to Make All Elements Divisible by 3

## Problem Statement
You are given an integer array `nums`.  
In **one operation**, you may **add 1** or **subtract 1** from any element.

Return the **minimum number of operations** required so that **every element becomes divisible by 3**.

---

## Key Insight
For any number `x`, the cost to make it divisible by 3 depends on `x % 3`:

| x % 3 | Meaning | Minimum operations |
|-------|----------|--------------------|
| 0 | Already divisible | 0 |
| 1 | Needs either +2 or -1 | 1 |
| 2 | Needs either +1 or -2 | 1 |

Thus, the total cost is:

Sum of (1 for each number where num % 3 != 0)


---

## Example 1
**Input**

nums = [1,2,3,4]


**Operations**
- 1 → 0 (subtract 1)
- 2 → 3 (add 1)
- 4 → 3 (subtract 1)

**Output**

3


---

## Example 2
**Input**

nums = [3,6,9]


**Output**

0

All elements are already divisible by 3.

---

## Constraints

- 1 ≤ nums.length ≤ 50
- 1 ≤ nums[i] ≤ 50


---
