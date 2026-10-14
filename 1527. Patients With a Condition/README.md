# Patients With a Condition

## Problem Description

You are given a table named `Patients`.

### Table: `Patients`
| Column Name    | Type    |
| :---           | :---    |
| `patient_id`   | int     |
| `patient_name` | varchar |
| `conditions`   | varchar |

- `patient_id` is the primary key for this table.
- `conditions` contains 0 or more condition codes separated by spaces.
- Type I Diabetes always starts with the `DIAB1` prefix.

Write an SQL solution to find the `patient_id`, `patient_name`, and `conditions` of patients who have Type I Diabetes.

Return the result table in **any order**.

---

## Examples

### Example 1

**Input:**

`Patients` table:
| patient_id | patient_name | conditions   |
| :---       | :---         | :---         |
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |

**Output:**
| patient_id | patient_name | conditions   |
| :---       | :---         | :---         |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |

**Explanation:**
- Bob and George both have condition codes starting with or containing `DIAB1`.

---
