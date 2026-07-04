# Second Highest Salary

## Problem

Given the `Employee` table:

| Column | Type |
|--------|------|
| id | int |
| salary | int |

Find the **second highest distinct salary**.

- If there is no second highest distinct salary, return **NULL**.

---

## Example 1

**Input**

Employee

| id | salary |
|----|--------|
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |

**Output**

| SecondHighestSalary |
|---------------------|
| 200 |

---

## Example 2

**Input**

Employee

| id | salary |
|----|--------|
| 1 | 100 |

**Output**

| SecondHighestSalary |
|---------------------|
| NULL |

---
