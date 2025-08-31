# Rectangle with Longest Diagonal

## Problem Statement
You are given a **2D integer array** `dimensions`, where:

- `dimensions[i][0]` → length of rectangle `i`
- `dimensions[i][1]` → width of rectangle `i`

Your task:  
Return the **area of the rectangle** having the **longest diagonal**.  

- If multiple rectangles share the same longest diagonal, return the one with the **largest area**.

---

## Examples

### Example 1
**Input:**  

dimensions = [[9,3],[8,6]]

**Output:**  

48

**Explanation:**  
- For `[9,3]`, diagonal = `sqrt(9² + 3²) = sqrt(90) ≈ 9.49`  
- For `[8,6]`, diagonal = `sqrt(8² + 6²) = sqrt(100) = 10`  
Longest diagonal is from `[8,6]`.  
Area = `8 * 6 = 48`.

---

### Example 2
**Input:**  

dimensions = [[3,4],[4,3]]

**Output:**  

12

**Explanation:**  
Both diagonals = `sqrt(3² + 4²) = sqrt(25) = 5`.  
Both areas = `12`.  
Answer = `12`.

---

## Constraints
- 1 ≤ `dimensions.length` ≤ 100  
- `dimensions[i].length == 2`  
- 1 ≤ `dimensions[i][0], dimensions[i][1]` ≤ 100  

---
