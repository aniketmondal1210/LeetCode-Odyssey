# Find Leftmost Middle Index

## Problem Statement

Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

- A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

- If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

---

## Examples

### Example 1:
**Input:**  
`nums = [2,3,-1,8,4]`  
**Output:**  
`3`  
**Explanation:**  
Left sum before index `3`: 2 + 3 + (-1) = 4  
Right sum after index `3`: 4  
Since both sums match, index `3` is returned.

---

### Example 2:
**Input:**  
`nums = [1,-1,4]`  
**Output:**  
`2`  
**Explanation:**  
Left sum before index `2`: 1 + (-1) = 0  
Right sum after index `2`: 0

---

### Example 3:
**Input:**  
`nums = [2,5]`  
**Output:**  
`-1`  
**Explanation:**  
No index satisfies the condition.

---

## Constraints

- `1 <= nums.length <= 100`
- `-1000 <= nums[i] <= 1000`

---
