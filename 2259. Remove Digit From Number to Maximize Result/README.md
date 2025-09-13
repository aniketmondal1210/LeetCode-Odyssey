# Remove Digit to Maximize Number

## Problem Statement
You are given a string `number` representing a positive integer and a character `digit`.  
You must remove **exactly one occurrence** of `digit` from `number` such that the resulting string (when interpreted as a decimal number) is **maximized**.  

It is guaranteed that `digit` occurs at least once in `number`.

---

## Examples

### Example 1
**Input:**  

number = "123", digit = "3"

**Output:**  

"12"

**Explanation:**  
There is only one `'3'` in `"123"`. Removing it gives `"12"`.

---

### Example 2
**Input:**  

number = "1231", digit = "1"

**Output:**  

"231"

**Explanation:**  
- Removing the **first '1'** → `"231"`  
- Removing the **second '1'** → `"123"`  
Since `231 > 123`, the answer is `"231"`.

---

### Example 3
**Input:**  

number = "551", digit = "5"

**Output:**  

"51"

**Explanation:**  
Removing either the **first** or **second** `'5'` results in `"51"`.

---

## Constraints
- `2 <= number.length <= 100`  
- `number` consists of digits from `'1'` to `'9'`.  
- `digit` is a digit from `'1'` to `'9'`.  
- `digit` occurs at least once in `number`.  

---
