# Alice and Bob Game on Array

## Problem Statement
You are given a **0-indexed integer array `nums`** of even length and an initially empty array `arr`.  
Alice and Bob play a game following these rules:

### Game Rules
- In each round:
  1. **Alice removes the minimum element** from `nums`.
  2. **Bob removes the minimum element** from the remaining `nums`.
  3. **Bob appends his removed element to `arr` first**.
  4. **Alice appends her removed element to `arr` next**.
- The game continues until `nums` becomes empty.

Your task is to **return the final array `arr`** after the game ends.

---

## Examples

### Example 1
**Input:**

nums = [5, 4, 2, 3]


**Output:**

[3, 2, 5, 4]


**Explanation:**
- Round 1:
  - Alice removes `2`
  - Bob removes `3`
  - Bob appends `3`, Alice appends `2` → `arr = [3, 2]`
- Round 2:
  - Alice removes `4`
  - Bob removes `5`
  - Bob appends `5`, Alice appends `4` → `arr = [3, 2, 5, 4]`

---

### Example 2
**Input:**

nums = [2, 5]


**Output:**

[5, 2]


**Explanation:**
- Round 1:
  - Alice removes `2`
  - Bob removes `5`
  - Bob appends `5`, Alice appends `2` → `arr = [5, 2]`

---

## Constraints

- 2 ≤ nums.length ≤ 100
- 1 ≤ nums[i] ≤ 100
- nums.length is even

---
