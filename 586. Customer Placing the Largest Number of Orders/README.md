# Customer Placing the Largest Number of Orders

## Problem Description

Given an `Orders` table containing `order_number` (primary key) and `customer_number`, find the `customer_number` for the customer who has placed the largest number of orders.

Test cases guarantee that a unique customer has the maximum order count in the base problem.

---

## Examples

### Example 1
- **Input (`Orders` table):**

| order_number | customer_number |
| :---: | :---: |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 3 |

- **Output:**

| customer_number |
| :---: |
| 3 |

- **Explanation:** Customer `3` has `2` orders, while customers `1` and `2` each have `1` order. Thus, `3` has the largest number of orders.

---
