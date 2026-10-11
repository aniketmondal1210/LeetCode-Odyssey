# Article Views I

## Problem Description

You are given a table named `Views`.

### Table: `Views`
| Column Name | Type |
| :---        | :--- |
| `article_id`| int  |
| `author_id` | int  |
| `viewer_id` | int  |
| `view_date` | date |

- There is no primary key for this table; it may contain duplicate rows.
- Each row indicates that a viewer viewed an article written by an author on a specific date.
- `author_id = viewer_id` indicates that the author viewed their own article.

Write an SQL solution to find all authors who viewed at least one of their own articles.

Return the result table sorted by `id` in **ascending order**.

---

## Examples

### Example 1

**Input:**

`Views` table:
| article_id | author_id | viewer_id | view_date  |
| :---       | :---      | :---      | :---       |
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |

**Output:**
| id |
| :- |
| 4  |
| 7  |

**Explanation:**
- Author `4` viewed their own article `3` (viewer_id = 4).
- Author `7` viewed their own article `2` (viewer_id = 7).

---
