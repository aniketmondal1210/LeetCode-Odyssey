# Chunk an Array Into Subarrays of Given Size

## Problem Statement
Given an array **arr** and an integer **size**, return a **chunked array**.

A chunked array:
- Contains subarrays each of length **size**
- The last subarray may be shorter if not enough elements remain
- Must be generated **without using lodash (_.chunk)**

---

## Example 1

**Input:**

arr = [1,2,3,4,5], size = 1


**Output:**

[[1],[2],[3],[4],[5]]


**Explanation:** Each element becomes its own chunk.

---

## Example 2

**Input:**

arr = [1,9,6,3,2], size = 3


**Output:**

[[1,9,6],[3,2]]


**Explanation:** The last chunk has fewer than 3 elements.

---

## Example 3

**Input:**

arr = [8,5,3,2,6], size = 6


**Output:**

[[8,5,3,2,6]]


**Explanation:** Size exceeds array length → all elements go in one chunk.

---

## Example 4

**Input:**

arr = [], size = 1


**Output:**

[]


**Explanation:** No elements → empty result.

---

## Constraints

- arr is a valid JSON array
- 2 ≤ arr.length ≤ 10⁵
- 1 ≤ size ≤ arr.length + 1


---
