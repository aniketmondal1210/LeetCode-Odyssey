# Maximum Value of an Alphanumeric String

## Problem Statement
The **value** of an alphanumeric string is defined as follows:

- If the string consists of **digits only**, its value is its **numeric representation in base 10**.
- Otherwise (if it contains **any letter**), its value is the **length of the string**.

You are given an array `strs` of alphanumeric strings.  
Return the **maximum value** among all strings in the array.

---

## Examples

### Example 1
**Input:**

strs = ["alic3","bob","3","4","00000"]


**Output:**

5


**Explanation:**
- `"alic3"` → contains letters → value = length = 5  
- `"bob"` → letters only → value = length = 3  
- `"3"` → digits only → value = 3  
- `"4"` → digits only → value = 4  
- `"00000"` → digits only → numeric value = 0  

Maximum value = **5**

---

### Example 2
**Input:**

strs = ["1","01","001","0001"]


**Output:**

1


**Explanation:**
All strings consist of digits only and evaluate to the number **1**.

---

## Constraints

- 1 <= strs.length <= 100
- 1 <= strs[i].length <= 9
- strs[i] consists of only lowercase English letters and digits


---
