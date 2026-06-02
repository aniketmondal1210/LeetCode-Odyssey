# Keep Each Element at Most k Times

## Problem Statement

Given a sorted array `nums`, keep each distinct element at most `k` times while preserving the original order.

Return the resulting array.

---

# Example 1

## Input

```text
nums = [1,1,1,2,2,3]
k = 2
```

## Output

```text
[1,1,2,2,3]
```

### Explanation

```text
1 appears 3 times → keep 2
2 appears 2 times → keep 2
3 appears 1 time  → keep 1
```

---

# Example 2

## Input

```text
nums = [1,2,3]
k = 1
```

## Output

```text
[1,2,3]
```

---

## Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
- 1 <= k <= nums.length
 

## Follow-up:

Can you solve this in-place using O(1) extra space?
Note that the space used for returning or resizing the result does not count toward the space complexity mentioned above, as some languages do not support in-place resizing.
 
---
