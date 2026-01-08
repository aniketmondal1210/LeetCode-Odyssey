# Smallest Number Containing Digits from Two Arrays

## Problem Statement
You are given two arrays `nums1` and `nums2`, each containing **unique digits**.

Your task is to return the **smallest possible number** that contains **at least one digit from each array**.

---

## Key Observations
- If there is **any common digit** between `nums1` and `nums2`, that digit alone forms the smallest possible number.
- If there is **no common digit**, then:
  - Pick the smallest digit from `nums1`.
  - Pick the smallest digit from `nums2`.
  - Combine them to form the smallest two-digit number.

---

## Examples

### Example 1
**Input:**

nums1 = [4,1,3]
nums2 = [5,7]


**Output:**

15


**Explanation:**  
- No common digit exists.
- Smallest digit in `nums1` is `1`.
- Smallest digit in `nums2` is `5`.
- Smallest number formed is `15`.

---

### Example 2
**Input:**

nums1 = [3,5,2,6]
nums2 = [3,1,7]


**Output:**

3


**Explanation:**  
- Digit `3` exists in both arrays.
- Using a single digit is smaller than any two-digit number.

---

## Constraints

- 1 <= nums1.length, nums2.length <= 9
- 1 <= nums1[i], nums2[i] <= 9
- All digits in each array are unique


---
