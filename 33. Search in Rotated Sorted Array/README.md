# Search in Rotated Sorted Array

## Problem Statement

You are given an integer array `nums` sorted in ascending order with distinct values. Before being passed to your function, `nums` might have been rotated at an unknown pivot index `k` (`1 <= k < nums.length`), resulting in a rotated array.

For example, the sorted array `[0,1,2,4,5,6,7]` might be rotated at index `3` to become `[4,5,6,7,0,1,2]`.

Given the rotated array `nums` and an integer `target`, return the index of `target` if it exists in `nums`, otherwise return `-1`.

You must design an algorithm with `O(log n)` runtime complexity.

---

## Examples

### Example 1
**Input:**  
`nums = [4,5,6,7,0,1,2]`, `target = 0`  
**Output:**  
`4`

### Example 2
**Input:**  
`nums = [4,5,6,7,0,1,2]`, `target = 3`  
**Output:**  
`-1`

### Example 3
**Input:**  
`nums = [1]`, `target = 0`  
**Output:**  
`-1`

---

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique.
- `nums` is sorted in ascending order, possibly rotated.
- `-10^4 <= target <= 10^4`
