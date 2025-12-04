# Maximum Score After k Operations

## Problem
You are given:
- an integer array `nums`  
- an integer `k`

You must perform the following operation **exactly k times**:

1. Select the **maximum element** `m` from `nums`.
2. Remove `m`.
3. Insert `m + 1` back into the array.
4. Increase your **score by m**.

Return the **maximum score** after `k` operations.

---

## Key Insight
To maximize score, always choose the **largest available number**.

This is a classic max-heap problem:
- Push all elements into a **max-heap**.
- Repeat `k` times:
  - Extract max `m`
  - Add `m` to score
  - Push `m + 1` back into heap

---

## Example
### Example 1

nums = [1,2,3,4,5], k = 3

Steps:
- Pick 5 → score = 5 → push 6
- Pick 6 → score = 11 → push 7
- Pick 7 → score = 18 → push 8  
**Output = 18**

### Example 2

nums = [5,5,5], k = 2

Steps:
- Pick 5 → score = 5 → push 6
- Pick 6 → score = 11  
**Output = 11**

---

## Constraints
- `1 ≤ nums.length ≤ 100`
- `1 ≤ nums[i] ≤ 100`
- `1 ≤ k ≤ 100`

---
