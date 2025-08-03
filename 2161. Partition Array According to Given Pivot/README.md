# Rearrange Array Elements Around Pivot

## Problem Statement

You are given a 0-indexed integer array `nums` and an integer `pivot`. Rearrange `nums` such that the following conditions are satisfied:

1. Every element less than `pivot` appears before every element greater than `pivot`.
2. Every element equal to `pivot` appears **in between** the elements less than and greater than `pivot`.
3. The **relative order** of the elements less than `pivot` and the elements greater than `pivot` is maintained.

Return the array after rearrangement.

---

## Input

- `nums`: List[int] – the array of integers.
- `pivot`: int – the pivot value that must be placed between smaller and larger values.

## Output

- List[int] – the rearranged array satisfying all the conditions.

---

## Constraints

- 1 ≤ nums.length ≤ 10⁵  
- -10⁶ ≤ nums[i] ≤ 10⁶  
- `pivot` is guaranteed to be one of the elements in `nums`.

---

## Examples

### Example 1

**Input:**  
nums = [9, 12, 5, 10, 14, 3, 10]  
pivot = 10  

**Output:**  
[9, 5, 3, 10, 10, 12, 14]

**Explanation:**  
- Elements < pivot: [9, 5, 3]  
- Elements == pivot: [10, 10]  
- Elements > pivot: [12, 14]  
Final array: [9, 5, 3, 10, 10, 12, 14]

---

### Example 2

**Input:**  
nums = [-3, 4, 3, 2]  
pivot = 2  

**Output:**  
[-3, 2, 4, 3]

**Explanation:**  
- Elements < pivot: [-3]  
- Elements == pivot: [2]  
- Elements > pivot: [4, 3]  
Final array: [-3, 2, 4, 3]

---
