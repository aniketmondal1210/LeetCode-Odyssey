# Categorize Box Based on Dimensions and Mass

## Problem Statement
You are given four integers: `length`, `width`, `height`, and `mass`, representing the dimensions and mass of a box.  
Your task is to return a string representing the category of the box.

The categorization rules are as follows:

- The box is **"Bulky"** if:
  - Any of the dimensions of the box is greater than or equal to `10^4`, **or**
  - The volume of the box is greater than or equal to `10^9`.
- The box is **"Heavy"** if:
  - The mass of the box is greater than or equal to `100`.
- If the box is both **"Bulky"** and **"Heavy"**, return `"Both"`.
- If the box is neither **"Bulky"** nor **"Heavy"**, return `"Neither"`.
- If the box is **"Bulky"** but not **"Heavy"**, return `"Bulky"`.
- If the box is **"Heavy"** but not **"Bulky"**, return `"Heavy"`.

⚠️ Note: The volume of the box is calculated as:  

volume = length * width * height


---

## Example 1
**Input:**

length = 1000, width = 35, height = 700, mass = 300


**Output:**

"Heavy"


**Explanation:**  
- None of the dimensions are ≥ 10^4.  
- Volume = 1000 × 35 × 700 = 24,500,000 ≤ 10^9 → Not Bulky.  
- Mass = 300 ≥ 100 → Heavy.  
Hence, the box is `"Heavy"`.

---

## Example 2
**Input:**

length = 200, width = 50, height = 800, mass = 50


**Output:**

"Neither"


**Explanation:**  
- None of the dimensions are ≥ 10^4.  
- Volume = 200 × 50 × 800 = 8,000,000 ≤ 10^9 → Not Bulky.  
- Mass = 50 < 100 → Not Heavy.  
Hence, the box is `"Neither"`.

---

## Constraints
- `1 <= length, width, height <= 10^5`
- `1 <= mass <= 10^3`

---
