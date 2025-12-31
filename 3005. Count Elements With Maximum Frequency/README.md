# Total Frequencies of Elements With Maximum Frequency

## Problem Statement
You are given an array `nums` consisting of **positive integers**.

Your task is to:
- Find the **maximum frequency** of any element in the array.
- Return the **total count of elements** whose frequency equals this maximum frequency.

📌 **Note:**  
The frequency of an element is the number of times it appears in the array.

---

## Examples

### Example 1
**Input:**

nums = [1, 2, 2, 3, 1, 4]


**Output:**

4


**Explanation:**  
- Frequency of `1` = 2  
- Frequency of `2` = 2  
- Frequency of `3` = 1  
- Frequency of `4` = 1  

The maximum frequency is `2`.  
Elements with this frequency are `1` and `2`.  
Total elements = `2 + 2 = 4`.

---

### Example 2
**Input:**

nums = [1, 2, 3, 4, 5]


**Output:**

5


**Explanation:**  
All elements occur exactly once.  
Maximum frequency = `1`.  
All 5 elements have this frequency → result is `5`.

---

## Constraints

- 1 ≤ nums.length ≤ 100
- 1 ≤ nums[i] ≤ 100

---
