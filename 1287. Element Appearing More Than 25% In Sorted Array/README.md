# Element Appearing More Than 25% in Sorted Array

## Problem Statement

Given an **integer array sorted in non-decreasing order**, there is **exactly one integer** in the array that occurs **more than 25% of the time**.  
**Return that integer.**

---

## Examples

### Example 1:

**Input:**  
`arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]`

**Output:**  
`6`

**Explanation:**  
`6` appears 4 times out of 9 elements, which is more than 25%.

---

### Example 2:

**Input:**  
`arr = [1, 1]`

**Output:**  
`1`

**Explanation:**  
`1` appears 2 times out of 2 elements, which is 100%.

---

## Constraints:

- 1 ≤ arr.length ≤ 10⁴  
- 0 ≤ arr[i] ≤ 10⁵  
- The input is **guaranteed** to have exactly one such element.
