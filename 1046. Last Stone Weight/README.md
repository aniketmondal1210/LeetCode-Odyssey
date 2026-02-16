# Last Stone Weight

## 📌 Problem Statement

You are given an integer array `stones` where `stones[i]` represents the weight of the `i`th stone.

We play a game:

- On each turn, pick the **two heaviest stones**.
- Let their weights be `x` and `y` where `x ≤ y`.

After smashing:
- If `x == y` → both stones are destroyed.
- If `x != y` → stone `x` is destroyed and stone `y` becomes `y - x`.

At the end, **at most one stone remains**.

Return the weight of the last remaining stone.  
If no stones remain, return `0`.

---

## 🧪 Examples

### Example 1

**Input**

stones = [2,7,4,1,8,1]


**Output**

1


**Explanation**

7 & 8 → 1 → [2,4,1,1,1]

2 & 4 → 2 → [2,1,1,1]

2 & 1 → 1 → [1,1,1]

1 & 1 → 0 → [1]


Final remaining stone = **1**

---

### Example 2

**Input**

stones = [1]


**Output**

1


---

## Constraints

- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000

---
