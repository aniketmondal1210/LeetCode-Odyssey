# Determine Color of Chessboard Square

## Problem Statement

You are given `coordinates`, a string that represents the coordinates of a square on a standard 8x8 chessboard.

Your task is to **return `true` if the square is white**, and **`false` if the square is black**.

A chessboard alternates colors, and the bottom-left square ("a1") is always black.

---

## Examples

### Example 1:
**Input:**  
`coordinates = "a1"`  
**Output:**  
`false`  
**Explanation:**  
Square "a1" is black.

---

### Example 2:
**Input:**  
`coordinates = "h3"`  
**Output:**  
`true`  
**Explanation:**  
Square "h3" is white.

---

### Example 3:
**Input:**  
`coordinates = "c7"`  
**Output:**  
`false`  
**Explanation:**  
Square "c7" is black.

---

## Constraints

- `coordinates.length == 2`
- `'a' <= coordinates[0] <= 'h'`
- `'1' <= coordinates[1] <= '8'`

---
