# Remove Duplicates from Sorted Array

## Problem Statement
You are given an integer array `nums` **sorted in non-decreasing order**.

Your task is to **remove duplicates in-place** such that each unique element appears **only once**, while maintaining the **relative order** of elements.

Let the number of unique elements be `k`.

- The function should return `k`.
- The **first `k` elements** of `nums` should contain the unique elements in sorted order.
- Elements beyond index `k - 1` are irrelevant and can be ignored.

---

## Custom Judge Behavior
The judge will validate your solution using the following logic:

```java
int[] nums = [...];          // Input array
int[] expectedNums = [...];  // Expected unique elements

int k = removeDuplicates(nums);

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, the solution is accepted.
```

## Examples

### Example 1

Input:

`nums = [1,1,2]`

Output:

`k = 2`
`nums = [1,2,_]`

Explanation:
The unique elements are `1` and `2`.
The function returns `2`, and the first two positions contain the unique values.

### Example 2

Input:

`nums = [0,0,1,1,1,2,2,3,3,4]`

Output:

`k = 5`
`nums = [0,1,2,3,4,_,_,_,_,_]`

Explanation:
The unique elements are `0`, `1`, `2`, `3`, `4`.
The function returns `5`, and the first five positions are updated accordingly.

## Constraints

- 1 ≤ nums.length ≤ 3 × 10⁴
- -100 ≤ nums[i] ≤ 100
- nums is sorted in non-decreasing order

---
