# Take Gifts From the Richest Pile

## Problem Statement
You are given an integer array `gifts` where `gifts[i]` represents the number of gifts in the i-th pile.

Every second, you perform the following operation:

1. Choose the pile with the **maximum number of gifts**.
   - If multiple piles have the same maximum value, choose any one.
2. Replace the number of gifts in that pile with:

floor(sqrt(original_value))


After performing this operation for `k` seconds, return the **total number of gifts remaining**.

---

## Example 1

**Input:**

gifts = [25, 64, 9, 4, 100]
k = 4


**Output:**

29


**Explanation:**
Operations:
1. Pick 100 → floor(sqrt(100)) = 10  
2. Pick 64 → floor(sqrt(64)) = 8  
3. Pick 25 → floor(sqrt(25)) = 5  
4. Pick 10 → floor(sqrt(10)) = 3  

Final array:

[5, 8, 9, 4, 3]


Total remaining gifts:

5 + 8 + 9 + 4 + 3 = 29


---

## Example 2

**Input:**

gifts = [1, 1, 1, 1]
k = 4


**Output:**

4


**Explanation:**
Each pile has 1 gift.  
floor(sqrt(1)) = 1  
No change occurs.  
Total remains 4.

---

## Constraints

- 1 ≤ gifts.length ≤ 10³
- 1 ≤ gifts[i] ≤ 10⁹
- 1 ≤ k ≤ 10³


---
