# Sort by Binary Reflection

## Problem Statement

Given an integer array `nums`, sort it based on the **binary reflection** of each element.

### Binary Reflection Definition
1. Convert number to binary
2. Reverse the binary string
3. Convert it back to decimal

### Sorting Rules
- Sort in **ascending order of reflected value**
- If two numbers have the same reflection → **smaller number comes first**

---

## Example 1

**Input**

nums = [4, 5, 4]


**Output**

[4, 4, 5]


**Explanation**

| Number | Binary | Reversed | Decimal |
|--------|--------|----------|--------|
| 4 | 100 | 001 | 1 |
| 5 | 101 | 101 | 5 |
| 4 | 100 | 001 | 1 |

Sorted by reflection → `[4, 4, 5]`

---

## Example 2

**Input**

nums = [3, 6, 5, 8]


**Output**

[8, 3, 6, 5]


**Explanation**

| Number | Binary | Reversed | Decimal |
|--------|--------|----------|--------|
| 3 | 11 | 11 | 3 |
| 6 | 110 | 011 | 3 |
| 5 | 101 | 101 | 5 |
| 8 | 1000 | 0001 | 1 |

Sorted → `[8, 3, 6, 5]`

---

## Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 10^9

---
