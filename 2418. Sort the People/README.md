# Sort the People by Height

## Problem Statement
You are given:
- An array of strings `names`
- An array of integers `heights`

Both arrays have the same length `n`.

For each index `i`:
- `names[i]` represents the name of the `i`-th person
- `heights[i]` represents the height of the `i`-th person

Your task is to return the `names` array **sorted in descending order of heights**.

---

## Example 1
**Input:**

names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]


**Output:**

["Mary", "Emma", "John"]


**Explanation:**  
Mary is the tallest (180), followed by Emma (170), and then John (165).

---

## Example 2
**Input:**

names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]


**Output:**

["Bob", "Alice", "Bob"]


**Explanation:**  
The first Bob is the tallest (185), followed by Alice (155), and then the second Bob (150).

---

## Constraints

- n == names.length == heights.length
- 1 ≤ n ≤ 10³
- 1 ≤ names[i].length ≤ 20
- 1 ≤ heights[i] ≤ 10⁵
- names[i] consists of lowercase and uppercase English letters
- All values in heights are distinct


---
