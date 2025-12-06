# Transform Array Using k Operations  
You are given:  
- An integer array **nums**  
- An integer **k**  
- An integer **multiplier**  

You must perform **k operations**, and in each operation:

1. Find the **minimum value** `x` in `nums`.  
2. If multiple elements equal `x`, choose the **first occurrence**.  
3. Replace that value with `x * multiplier`.  

Return the **final array** after all operations.

---

## 🧮 Example 1

Input:
nums = [2,1,3,5,6], k = 5, multiplier = 2

Operations:
1 → [2, 2, 3, 5, 6]

2 → [4, 2, 3, 5, 6]

3 → [4, 4, 3, 5, 6]

4 → [4, 4, 6, 5, 6]

5 → [8, 4, 6, 5, 6]

Output:
[8,4,6,5,6]


---

## 🧮 Example 2

Input:
nums = [1,2], k = 3, multiplier = 4

Operations:
1 → [4, 2]

2 → [4, 8]

3 → [16, 8]

Output:
[16,8]


---
