# Count Dominant Indices

## Problem Statement
You are given an integer array `nums` of length `n`.

An element at index `i` is called **dominant** if:

nums[i] > average(nums[i + 1], nums[i + 2], ..., nums[n - 1])


The **rightmost element** is never dominant because there are no elements to its right.

Return the count of dominant indices.

---

## Example 1

**Input:**

nums = [5, 4, 3]


**Output:**

2


**Explanation:**
- At index 0 → 5 > average(4,3) = 3.5 → Dominant
- At index 1 → 4 > average(3) = 3 → Dominant
- Index 2 → No elements to the right → Not dominant

Total dominant indices = 2

---

## Example 2

**Input:**

nums = [4, 1, 2]


**Output:**

1


**Explanation:**
- At index 0 → 4 > average(1,2) = 1.5 → Dominant
- At index 1 → 1 ≤ average(2) = 2 → Not dominant
- Index 2 → Not dominant

Total dominant indices = 1

---

## Constraints

- 1 ≤ nums.length ≤ 100
- 1 ≤ nums[i] ≤ 100


---
