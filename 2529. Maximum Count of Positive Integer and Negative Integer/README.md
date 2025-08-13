# Maximum Count of Positive or Negative Integers

## Problem
Given a sorted array `nums` in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

- `0` is neither positive nor negative.
- `pos` = number of positive integers in `nums`
- `neg` = number of negative integers in `nums`
- Return `max(pos, neg)`

---

## Examples

### Example 1
**Input:**

nums = [-2, -1, -1, 1, 2, 3]

**Output:**

3

**Explanation:**
There are 3 positive integers and 3 negative integers. The maximum count among them is `3`.

---

### Example 2
**Input:**

nums = [-3, -2, -1, 0, 0, 1, 2]

**Output:**

3

**Explanation:**
There are 3 negative integers and 2 positive integers. The maximum count is `3`.

---

### Example 3
**Input:**

nums = [5, 20, 66, 1314]

**Output:**

4

**Explanation:**
There are 4 positive integers and 0 negative integers. The maximum count is `4`.

---

## Constraints
- 1 ≤ `nums.length` ≤ 2000  
- -2000 ≤ `nums[i]` ≤ 2000  
- `nums` is sorted in **non-decreasing** order.

---

## Follow-up
Can you solve the problem in **O(log n)** time using **binary search** to find the boundaries of negatives and positives?

---
