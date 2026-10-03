# Find Followers Count

## Problem Description

You are given a table named `Followers`.

### Table: `Followers`
| Column Name   | Type |
| :---          | :--- |
| `user_id`     | int  |
| `follower_id` | int  |

- `(user_id, follower_id)` is the primary key (combination of columns with unique values) for this table.
- Each row contains the IDs of a user and a follower in a social media app where `follower_id` follows `user_id`.

Write an SQL query to calculate the **number of followers** for each user.

Return the result table ordered by `user_id` in **ascending order**.

---

## Examples

### Example 1

**Input:**

`Followers` table:
| user_id | follower_id |
| :---    | :---        |
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |

**Output:**
| user_id | followers_count |
| :---    | :---            |
| 0       | 1               |
| 1       | 1               |
| 2       | 2               |

**Explanation:**
- The followers of user `0` are `{1}` (count: 1).
- The followers of user `1` are `{0}` (count: 1).
- The followers of user `2` are `{0, 1}` (count: 2).

---
