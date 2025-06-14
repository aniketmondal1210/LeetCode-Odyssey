# Remove Element

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are **not equal to `val`**.

To get accepted, you must:

- Change the array `nums` such that the **first `k` elements** of `nums` contain the elements which are not equal to `val`.
- The remaining elements of `nums` are not important.
- Return `k`.

---

## Custom Judge

The judge will test your solution using the following:

```java
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // Expected answer with correct length
                            // Sorted and no values equal to val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

---

## Examples

### Example 1

**Input:**  
`nums = [3,2,2,3], val = 3`  
**Output:**  
`2, nums = [2,2,_,_]`  
**Explanation:**  
Your function should return `k = 2`, with the first two elements of `nums` being `2`.  
The remaining elements are ignored.

---

### Example 2

**Input:**  
`nums = [0,1,2,2,3,0,4,2], val = 2`  
**Output:**  
`5, nums = [0,1,4,0,3,_,_,_]`  
**Explanation:**  
Your function should return `k = 5`, with the first five elements of `nums` being any combination of `0,1,4,0,3`.  
The remaining values do not matter.

---

## Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`
