# Minimum Number of Chairs in a Waiting Room

## Problem Description

You are given a string `s`. Simulate events at each second $i$:
- If `s[i] == 'E'`, a person enters the waiting room and takes one of the chairs in it.
- If `s[i] == 'L'`, a person leaves the waiting room, freeing up a chair.

Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.

---

## Examples

### Example 1
- **Input:** `s = "EEEEEEE"`
- **Output:** `7`
- **Explanation:** After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.

### Example 2
- **Input:** `s = "ELELEEL"`
- **Output:** `2`
- **Explanation:** The maximum number of people in the waiting room at any given time is 2.

### Example 3
- **Input:** `s = "ELEELEELLL"`
- **Output:** `3`
- **Explanation:** The peak number of people concurrently in the waiting room is 3.

---

## Constraints

- $1 \le  {s.length} \le 50$
- `s` consists only of the letters `'E'` and `'L'`.
- `s` represents a valid sequence of entries and exits.

---
