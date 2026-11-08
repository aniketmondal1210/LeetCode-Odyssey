# Lemonade Change

## Problem Description

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by `bills`). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

*Note:* You do not have any change in hand at first.

Return `true` if you can provide every customer with the correct change, or `false` otherwise.

---

## Examples

### Example 1
- **Input:** `bills = [5, 5, 5, 10, 20]`
- **Output:** `true`
- **Explanation:** 
  - From the first 3 customers, collect three $5 bills.
  - Fourth customer pays $10; give back $5.
  - Fifth customer pays $20; give back a $10 and a $5 bill.
  - Everyone receives correct change.

### Example 2
- **Input:** `bills = [5, 5, 10, 10, 20]`
- **Output:** `false`
- **Explanation:** 
  - After collecting two $5 bills and giving change for the next two $10 bills, you are left with two $10 bills and no $5 bills.
  - The last customer pays $20, requiring $15 change, which cannot be provided using two $10 bills.

---

## Constraints

- $1 \le \text{bills.length} \le 10^5$
- `bills[i]` is either $5, $10, or $20.

---
