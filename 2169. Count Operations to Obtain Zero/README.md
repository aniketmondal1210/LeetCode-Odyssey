# Count Operations to Make Either Number Zero

## Problem Statement

You are given two non-negative integers `num1` and `num2`.

In one operation:
- If `num1 >= num2`, you must subtract `num2` from `num1`.
- Otherwise, subtract `num1` from `num2`.

Return the **number of operations required** to make **either `num1 = 0` or `num2 = 0`**.

---

## Examples

### Example 1:

**Input:**  
`num1 = 2`, `num2 = 3`  

**Output:**  
`3`  

**Explanation:**  
- Operation 1: `num1 = 2`, `num2 = 3` → `num2 = 3 - 2 = 1`
- Operation 2: `num1 = 2`, `num2 = 1` → `num1 = 2 - 1 = 1`
- Operation 3: `num1 = 1`, `num2 = 1` → `num1 = 1 - 1 = 0`  
Now `num1 = 0`, so we stop.  
Total operations = **3**

---

### Example 2:

**Input:**  
`num1 = 10`, `num2 = 10`  

**Output:**  
`1`  

**Explanation:**  
- Operation 1: `num1 = 10`, `num2 = 10` → `num1 = 10 - 10 = 0`  
Now `num1 = 0`, so we stop.  
Total operations = **1**

---

## Constraints:

- 0 ≤ num1, num2 ≤ 10⁵
