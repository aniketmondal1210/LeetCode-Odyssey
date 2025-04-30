# Problem: Count Numbers with Even Number of Digits

Given an array `nums` of integers, return how many of them contain an **even number of digits**.

---

## Input

- An array `nums` of integers.
- Constraints:
  - `1 <= nums.length <= 500`
  - `1 <= nums[i] <= 10^5`

---

## Output

- An integer representing how many numbers in the array contain an even number of digits.

---

## Examples

### Example 1

**Input:**  
`nums = [12, 345, 2, 6, 7896]`

**Output:**  
`2`

**Explanation:**  
- `12` has 2 digits → even  
- `345` has 3 digits → odd  
- `2` has 1 digit → odd  
- `6` has 1 digit → odd  
- `7896` has 4 digits → even  
✅ Only `12` and `7896` contain an even number of digits.

---

### Example 2

**Input:**  
`nums = [555, 901, 482, 1771]`

**Output:**  
`1`

**Explanation:**  
- Only `1771` has an even number of digits (4 digits).

---
