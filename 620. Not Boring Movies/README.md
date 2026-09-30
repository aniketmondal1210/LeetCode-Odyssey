# Not Boring Movies

## Problem Description

You are given a table named `Cinema`.

### Table: `Cinema`
| Column Name   | Type    |
| :---          | :---    |
| `id`          | int     |
| `movie`       | varchar |
| `description` | varchar |
| `rating`      | float   |

- `id` is the primary key for this table.
- Each row contains information about the name of a movie, its genre/description, and its rating (range $[0, 10]$ with 2 decimal places).

Write an SQL query to report all movies with:
1. An **odd-numbered `id`** (`id % 2 != 0`).
2. A description that is **not equal to `"boring"`**.

Return the result table ordered by `rating` in **descending order**.

---

## Examples

### Example 1

**Input:**

`Cinema` table:
| id | movie      | description | rating |
| :--- | :--- | :--- | :--- |
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |

**Output:**
| id | movie      | description | rating |
| :--- | :--- | :--- | :--- |
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |

**Explanation:**
- Movies with odd IDs: `1`, `3`, and `5`.
- Movie with `id = 3` has `description = 'boring'`, so it is excluded.
- Remaining odd-ID movies (`5` and `1`) are sorted by `rating` in descending order ($9.1 > 8.9$).

---
