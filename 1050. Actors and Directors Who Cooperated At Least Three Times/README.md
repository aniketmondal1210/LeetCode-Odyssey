# Actors and Directors Who Cooperated At Least Three Times

## Problem Description

You are given a table named `ActorDirector`.

### Table: `ActorDirector`
| Column Name   | Type    |
| :---          | :---    |
| `actor_id`    | int     |
| `director_id` | int     |
| `timestamp`   | int     |

- `timestamp` is the primary key for this table.
- Each row indicates that an actor with ID `actor_id` directed or worked with director `director_id` at a given `timestamp`.

Write an SQL solution to find all pairs `(actor_id, director_id)` where the actor has cooperated with the director **at least three times**.

Return the result table in **any order**.

---

## Examples

### Example 1

**Input:**

`ActorDirector` table:
| actor_id | director_id | timestamp |
| :---     | :---        | :---      |
| 1        | 1           | 0         |
| 1        | 1           | 1         |
| 1        | 1           | 2         |
| 1        | 2           | 3         |
| 1        | 2           | 4         |
| 2        | 1           | 5         |
| 2        | 1           | 6         |

**Output:**
| actor_id | director_id |
| :---     | :---        |
| 1        | 1           |

**Explanation:**
- Pair `(1, 1)` cooperated 3 times (timestamps 0, 1, 2).
- Pair `(1, 2)` cooperated 2 times.
- Pair `(2, 1)` cooperated 2 times.
- Only `(1, 1)` meets the condition of at least 3 cooperations.

---
