# Number of Colored Cells After N Minutes

## Problem Statement
There exists an infinitely large **two-dimensional grid** of uncolored unit cells.

You are given a positive integer `n`, representing the number of minutes. The coloring process follows these rules:

- At minute **1**, color **one arbitrary cell** blue.
- At every subsequent minute, color **all uncolored cells that touch (share an edge)** with a blue cell.

Return the **total number of colored cells** after `n` minutes.

---

## Examples

### Example 1
**Input:**  

n = 1


**Output:**  

1


**Explanation:**  
Only one cell is colored at minute 1.

---

### Example 2
**Input:**  

n = 2


**Output:**  

5


**Explanation:**  
- Minute 1 → 1 cell  
- Minute 2 → 4 surrounding cells + center cell  
Total = `5`

## Constraints

- 1 ≤ n ≤ 10⁵

---
