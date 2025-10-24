# Counter Function

## Problem Statement
Given an integer `n`, return a **counter function** that:
- Initially returns `n`
- Then returns `n + 1`, `n + 2`, and so on, each time it is called.

---

## Input
- An integer `n` (the starting number)
- A list of operations — all are `"call"`

**Constraints:**

-1000 ≤ n ≤ 1000

0 ≤ calls.length ≤ 1000


---

## Output
- A list of integers — the results of calling the counter function sequentially.

---

## Examples

### Example 1
**Input:**

n = 10
["call", "call", "call"]

**Output:**

[10, 11, 12]

**Explanation:**
- 1st call → 10  
- 2nd call → 11  
- 3rd call → 12  

---

### Example 2
**Input:**

n = -2
["call", "call", "call", "call", "call"]

**Output:**

[-2, -1, 0, 1, 2]


---
