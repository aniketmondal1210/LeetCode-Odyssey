# Return to Boundary Count

## Problem Statement

An ant is on a boundary and moves according to an array of non-zero integers `nums`. The ant reads the array from start to end, and:

- If `nums[i] > 0`, it moves **right** by `nums[i]` units.
- If `nums[i] < 0`, it moves **left** by `-nums[i]` units.

Your task is to **return the number of times** the ant **returns to the boundary (position 0)** after completing a move.

🔸 Note:

- The ant starts at position `0` (the boundary).
- We **only check if it's at the boundary after each complete move**.
- The space is infinite in both directions.

---

## Examples

### Example 1:

**Input:**  
`nums = [2, 3, -5]`  
**Output:**  
`1`  
**Explanation:**  
- After step 1: Position = 2  
- After step 2: Position = 5  
- After step 3: Position = 0 ✅ (1 time returned to boundary)

---

### Example 2:

**Input:**  
`nums = [3, 2, -3, -4]`  
**Output:**  
`0`  
**Explanation:**  
The ant never returns to the boundary.

---

## Constraints

- `1 <= nums.length <= 100`
- `-10 <= nums[i] <= 10`
- `nums[i] != 0`

---
