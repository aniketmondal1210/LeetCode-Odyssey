# Classes More Than 5 Students

## Problem Description

You are given a table named `Courses`.

### Table: `Courses`
| Column Name | Type    |
| :---        | :---    |
| `student`   | varchar |
| `class`     | varchar |

- `(student, class)` is the primary key (combination of columns with unique values) for this table.
- Each row indicates the name of a student and the class in which they are enrolled.

Write an SQL query to find all the classes that have **at least five students**.

Return the result table in **any order**.

---

## Examples

### Example 1

**Input:**

`Courses` table:
| student | class    |
| :---    | :---     |
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |

**Output:**
| class |
| :---  |
| Math  |

**Explanation:**
- `Math` has 6 enrolled students ($\ge 5$), so it is included.
- `English`, `Biology`, and `Computer` each have 1 student ($< 5$), so they are excluded.

---
