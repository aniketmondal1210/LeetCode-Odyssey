# Check if Two Chessboard Squares Have the Same Color

## Problem Statement

You are given two strings, `coordinate1` and `coordinate2`, representing the coordinates of squares on an 8 x 8 chessboard.

Return `true` if both squares have the **same color**, and `false` otherwise.

A square is **black** or **white** depending on the sum of its row and column index (both starting from 1).  
A square is:
- **Black** if the sum is even
- **White** if the sum is odd

---

## Examples

### Example 1:
**Input:**  
`coordinate1 = "a1"`  
`coordinate2 = "c3"`  
**Output:**  
`true`  
**Explanation:**  
Both `"a1"` and `"c3"` are black squares.

---

### Example 2:
**Input:**  
`coordinate1 = "a1"`  
`coordinate2 = "h3"`  
**Output:**  
`false`  
**Explanation:**  
`"a1"` is black, `"h3"` is white.

---

## Constraints

- `coordinate1.length == coordinate2.length == 2`
- `'a' <= coordinate1[0], coordinate2[0] <= 'h'`
- `'1' <= coordinate1[1], coordinate2[1] <= '8'`

---
