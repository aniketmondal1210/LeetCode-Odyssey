# Add `last()` Method to All Arrays

## Problem Statement
Enhance all JavaScript arrays so that you can call a method `array.last()` on any array.  
The method should return:

- The **last element** of the array.
- `-1` if the array is **empty**.

You may assume the array is the output of `JSON.parse`.

---

## Example 1
**Input:**
nums = [null, {}, 3];

**Output:**

3

Explanation:
Calling nums.last() returns the last element → 3.

## Example 2

**Input:**

nums = [];

**Output:**

-1

Explanation:
The array has no elements, so nums.last() returns -1.

## Constraints
- arr is a valid JSON array  
- 0 <= arr.length <= 1000
