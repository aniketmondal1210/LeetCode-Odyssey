# Friends in Their Finishing Order

## Problem Statement

You are given:

- `order[]` → contains integers from `1` to `n` exactly once (race finishing order).
- `friends[]` → IDs of your friends (sorted in strictly increasing order).

Return an array containing your friends' IDs in their finishing order.

---

## Example 1

**Input:**

order = [3,1,2,5,4]
friends = [1,3,4]


**Output:**

[3,1,4]


**Explanation:**
Race finishing order is `[3,1,2,5,4]`.  
Friends appearing in this order are `[3,1,4]`.

---

## Example 2

**Input:**

order = [1,4,5,3,2]
friends = [2,5]


**Output:**

[5,2]


**Explanation:**
Race finishing order is `[1,4,5,3,2]`.  
Friends appearing in this order are `[5,2]`.

---

## Constraints

- `1 ≤ n ≤ 100`
- `friends.length ≤ min(8, n)`
- `order` contains numbers from `1` to `n` exactly once
- `friends` is strictly increasing

---
