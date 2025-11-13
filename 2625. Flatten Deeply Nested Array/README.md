# Flatten a Multi-Dimensional Array up to Given Depth

## Problem Statement

Given a **multi-dimensional array `arr`** and a **depth `n`**, return a *flattened* version of that array.

Flattening means removing sub-array nesting and replacing them with their actual elements — but **only if** the current nesting depth is **less than `n`**.

- Elements in the outermost array have depth `0`.
- You **must not** use the built-in `Array.flat()` method.

---

## Example 1

**Input:**
arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
n = 0;

**Output:**

[1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

Explanation:
At n = 0, no flattening is done.
All arrays remain as they are.

## Example 2

**Input:**

arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
n = 1;

**Output:**

[1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]

Explanation:
Only arrays at depth 0 are flattened (since 0 < 1).
Inner subarrays such as [9, 10, 11] (depth 1) remain untouched.

## Example 3

**Input:**

arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
n = 2;

**Output:**

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Explanation:
All arrays up to depth 1 are flattened because their depth is less than 2.

## Constraints

- 0 <= total numbers in arr <= 10^5
- 0 <= total subarrays in arr <= 10^5
- maxDepth <= 1000
- 1000 <= each number <= 1000
0 <= n <= 1000
