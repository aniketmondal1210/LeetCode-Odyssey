# Check if Array Can Form an Arithmetic Progression

## Problem Statement

A sequence of numbers is called an **arithmetic progression** if the **difference between any two consecutive elements is the same**.

Given an array of numbers `arr`, **return `true` if the array can be rearranged to form an arithmetic progression**, otherwise return `false`.

---

## Examples

### Example 1:

**Input:**  
`arr = [3, 5, 1]`  

**Output:**  
`true`  

**Explanation:**  
We can reorder the elements as `[1, 3, 5]` or `[5, 3, 1]` with differences `2` and `-2` respectively between each consecutive element.

---

### Example 2:

**Input:**  
`arr = [1, 2, 4]`  

**Output:**  
`false`  

**Explanation:**  
There is no way to reorder the elements to obtain an arithmetic progression.

---

## Constraints:

- 2 ≤ arr.length ≤ 1000  
- -10⁶ ≤ arr[i] ≤ 10⁶
