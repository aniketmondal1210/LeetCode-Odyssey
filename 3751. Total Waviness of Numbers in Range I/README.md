# Total Waviness in a Number Range

## Problem Statement
You are given two integers `num1` and `num2` representing an inclusive range `[num1, num2]`.

The **waviness** of a number is defined as the total count of its **peaks** and **valleys**:

- A digit is a **peak** if it is strictly greater than both of its immediate neighbors.  
- A digit is a **valley** if it is strictly less than both of its immediate neighbors.  
- The **first and last digits** of a number can never be peaks or valleys.  
- Any number with **fewer than 3 digits** has a waviness of **0**.

Return the **total sum of waviness** for all numbers in the range `[num1, num2]`.

---

## Example 1
**Input:**  

num1 = 120, num2 = 130

**Output:**  

3


**Explanation:**  
Numbers with waviness:  
- 120 → 2 is a peak → waviness = 1  
- 121 → 2 is a peak → waviness = 1  
- 130 → 3 is a peak → waviness = 1  
All others contribute 0.  
Total waviness = 3.

---

## Example 2
**Input:**  

num1 = 198, num2 = 202

**Output:**  

3


**Explanation:**  
- 198 → 9 is a peak → waviness = 1  
- 201 → 0 is a valley → waviness = 1  
- 202 → 0 is a valley → waviness = 1  
Total = 3.

---

## Example 3
**Input:**  

num1 = 4848, num2 = 4848

**Output:**  

2


**Explanation:**  
- 4848 → digits: 4,8,4,8  
  - 8 (2nd digit) is a peak  
  - 4 (3rd digit) is a valley  
Waviness = 2.

---

## Constraints

1 <= num1 <= num2 <= 100000

---
