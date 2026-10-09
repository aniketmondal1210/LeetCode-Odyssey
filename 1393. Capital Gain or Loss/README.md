# Capital Gain/Loss

## Problem Description

You are given a table named `Stocks`.

### Table: `Stocks`
| Column Name     | Type    |
| :---            | :---    |
| `stock_name`    | varchar |
| `operation`     | ENUM    |
| `operation_day` | int     |
| `price`         | int     |

- `(stock_name, operation_day)` is the primary key for this table.
- The `operation` column is an `ENUM` value of type `('Sell', 'Buy')`.
- Each row indicates that the stock `stock_name` had an operation on day `operation_day` at price `price`.
- It is guaranteed that each `'Sell'` operation for a stock has a corresponding `'Buy'` operation on a previous day, and vice versa.

Write an SQL query to report the **Capital gain/loss** for each stock.

The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times:
$$\text{Capital Gain/Loss} = \sum \text{Price}_{\text{Sell}} - \sum \text{Price}_{\text{Buy}}$$

Return the result table in **any order**.

---

## Examples

### Example 1

**Input:**

`Stocks` table:
| stock_name   | operation | operation_day | price |
| :---         | :---      | :---          | :---  |
| Leetcode     | Buy       | 1             | 1000  |
| Corona Masks | Buy       | 2             | 10    |
| Leetcode     | Sell      | 5             | 9000  |
| Handbags     | Buy       | 17            | 30000 |
| Corona Masks | Sell      | 3             | 1010  |
| Corona Masks | Buy       | 4             | 1000  |
| Corona Masks | Sell      | 5             | 500   |
| Corona Masks | Buy       | 6             | 1000  |
| Handbags     | Sell      | 29            | 7000  |
| Corona Masks | Sell      | 10            | 10000 |

**Output:**
| stock_name   | capital_gain_loss |
| :---         | :---              |
| Corona Masks | 9500               |
| Leetcode     | 8000               |
| Handbags     | -23000             |

**Explanation:**
- **Leetcode:** Bought at 1000, Sold at 9000 $\rightarrow 9000 - 1000 = 8000$.
- **Handbags:** Bought at 30000, Sold at 7000 $\rightarrow 7000 - 30000 = -23000$.
- **Corona Masks:** $(1010 - 10) + (500 - 1000) + (10000 - 1000) = 9500$.

---
