# Invalid Tweets Identification

## Problem Description

You are given a table named `Tweets`.

### Table: `Tweets`
| Column Name | Type    |
| :---        | :---    |
| `tweet_id`  | int     |
| `content`   | varchar |

- `tweet_id` is the primary key for this table.
- `content` consists of alphanumeric characters, `'!'`, or `' '` (spaces) and no other special characters.
- This table contains all tweets in a social media application.

Write an SQL solution to find the IDs of all **invalid tweets**. A tweet is considered invalid if the number of characters used in `content` is **strictly greater than 15**.

Return the result table in **any order**.

---

## Examples

### Example 1

**Input:**

`Tweets` table:
| tweet_id | content                           |
| :---     | :---                              |
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |

**Output:**
| tweet_id |
| :---     |
| 2        |

**Explanation:**
- Tweet 1 has length $11 \le 15$ -> Valid.
- Tweet 2 has length $33 > 15$ -> Invalid.

---
