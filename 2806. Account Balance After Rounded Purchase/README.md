# Final Bank Balance After Purchase

## Problem Statement
You start with a bank account balance of **100 dollars**.  
You are given an integer **purchaseAmount** — the cost of an item you wish to buy.

Before making the purchase, you must:
1. **Round `purchaseAmount`** to the **nearest multiple of 10**.  
   - If the last digit is 5 or more → round **up**.  
   - Otherwise → round **down**.
2. Subtract this **rounded amount** from your initial balance (100).

Return the **final account balance** after the purchase.

---

## Examples

### Example 1
**Input:**

purchaseAmount = 9

**Output:**

90

**Explanation:**  
Nearest multiple of 10 to 9 is 10 → new balance = 100 - 10 = **90**.

---

### Example 2
**Input:**

purchaseAmount = 15

**Output:**

80

**Explanation:**  
Nearest multiple of 10 to 15 is 20 → new balance = 100 - 20 = **80**.

---

### Example 3
**Input:**

purchaseAmount = 10

**Output:**

90

**Explanation:**  
10 is already a multiple of 10 → new balance = 100 - 10 = **90**.

---

## Constraints

0 <= purchaseAmount <= 100
