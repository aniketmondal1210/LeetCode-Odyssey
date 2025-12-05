# Count Partitions With Even Sum Difference

## Problem
You are given an integer array `nums` of length `n`.

A **partition** is an index `i` where `0 <= i < n - 1`, which splits the array into:

- Left subarray → indices `[0, i]`
- Right subarray → indices `[i + 1, n - 1]`

You must count the number of partitions where:

(sum of left) - (sum of right) is even


---

### Example 1

Input: nums = [10,10,3,7,6]
Output: 4


### Example 2

Input: nums = [1,2,2]
Output: 0


### Example 3

Input: nums = [2,4,6,8]
Output: 3

---
