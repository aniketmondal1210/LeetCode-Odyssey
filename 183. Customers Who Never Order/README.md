# Customers Who Never Order

## Problem Description

You are given two tables: `Customers` and `Orders`.

### Table: `Customers`
| Column Name | Type    |
| :---        | :---    |
| `id`        | int     |
| `name`      | varchar |

- `id` is the primary key for this table.
- Each row contains the ID and name of a customer.

### Table: `Orders`
| Column Name  | Type |
| :---         | :--- |
| `id`         | int  |
| `customerId` | int  |

- `id` is the primary key for this table.
- `customerId` is a foreign key referencing `id` from the `Customers` table.
- Each row indicates an order ID and the customer who placed it.

Write an SQL query to find all customers who **never ordered anything**. Return the result table in any order with column alias `Customers`.

---

## Examples

### Example 1

**Input:**

`Customers` table:
| id | name  |
| :--- | :--- |
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |

`Orders` table:
| id | customerId |
| :--- | :--- |
| 1  | 3          |
| 2  | 1          |

**Output:**
| Customers |
| :--- |
| Henry     |
| Max       |

---
