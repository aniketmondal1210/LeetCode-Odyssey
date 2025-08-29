# K-th Largest Integer in an Array

## Problem Statement
You are given an array of strings `nums` where each string represents an integer (without leading zeros), and an integer `k`.  
Return the string that represents the **k-th largest integer** in `nums`.

- Duplicate numbers are treated **distinctly**.  
  Example: If `nums = ["1","2","2"]`,  
  - "2" is the 1st largest,  
  - the other "2" is the 2nd largest,  
  - "1" is the 3rd largest.

---

## Examples

### Example 1
**Input:**  

nums = ["3","6","7","10"], k = 4

**Output:**  

"3"

**Explanation:**  
Sorted order: ["3","6","7","10"].  
The 4th largest is `"3"`.

---

### Example 2
**Input:**  

nums = ["2","21","12","1"], k = 3

**Output:**  

"2"

**Explanation:**  
Sorted order: ["1","2","12","21"].  
The 3rd largest is `"2"`.

---

### Example 3
**Input:**  

nums = ["0","0"], k = 2

**Output:**  

"0"

**Explanation:**  
Sorted order: ["0","0"].  
The 2nd largest is `"0"`.

---

## Constraints
- 1 ≤ k ≤ nums.length ≤ 10⁴  
- 1 ≤ nums[i].length ≤ 100  
- Each `nums[i]` consists of digits only  
- No leading zeros  

---
