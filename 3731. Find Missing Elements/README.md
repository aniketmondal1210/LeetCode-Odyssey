# Find Missing Numbers in a Range

## Problem Statement
You are given an integer array `nums` consisting of **unique integers**.

Originally, `nums` contained every integer within a certain range. However, some integers might have gone missing from the array.

The **smallest** and **largest** integers of the original range are still present in `nums`.

Your task is to return a **sorted list** of all the missing integers in this range.  
If no integers are missing, return an **empty list**.

---

## Example 1
**Input:**  

nums = [1, 4, 2, 5]


**Output:**  

[3]


**Explanation:**  
The full range should be `[1, 2, 3, 4, 5]`.  
Only `3` is missing.

---

## Example 2
**Input:**  

nums = [7, 8, 6, 9]


**Output:**  

[]


**Explanation:**  
The full range is `[6, 7, 8, 9]`.  
No integers are missing.

---

## Example 3
**Input:**  

nums = [5, 1]


**Output:**  

[2, 3, 4]


**Explanation:**  
The full range should be `[1, 2, 3, 4, 5]`.  
The missing integers are `2`, `3`, and `4`.

---

## Your Task
You don’t need to read input or print anything.  
Complete the function **`findMissing(nums)`** which takes an integer array `nums` and returns a list of all missing integers in sorted order.

---

## Expected Time Complexity

O(n)


## Expected Auxiliary Space

O(1)


---

## Constraints

2 ≤ nums.length ≤ 100
1 ≤ nums[i] ≤ 100
All elements of nums are unique.


---
