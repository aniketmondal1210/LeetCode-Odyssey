# Decompose Integer into Base-10 Components

## Problem Statement
You are given a positive integer `n`.  

A **base-10 component** is defined as:  
- The product of a **single digit (1–9)** and a **non-negative power of 10**.  

Examples of base-10 components:
- ✅ `500 = 5 × 10²`
- ✅ `30 = 3 × 10¹`
- ✅ `7 = 7 × 10⁰`
- ❌ `537` (not a single digit × power of 10)
- ❌ `11`  

Your task is to:
- Express `n` as a sum of the **fewest base-10 components possible**.
- Return the list of components in **descending order**.

---

## Examples

### Example 1
**Input**

n = 537

**Output**

[500, 30, 7]

**Explanation**  
537 = 500 + 30 + 7, which uses 3 components. No fewer components are possible.

---

### Example 2
**Input**

n = 102

**Output**

[100, 2]

**Explanation**  
102 = 100 + 2 → 2 components. (102 itself is not valid because it’s not a single-digit × power of 10).

---

### Example 3
**Input**

n = 6

**Output**

[6]

**Explanation**  
6 = 6 × 10⁰ → already a valid base-10 component.

---

## Constraints
- `1 <= n <= 10^9`

---

## Approach
1. Convert the integer into its digits.
2. For each non-zero digit at position `i`, form the component:

digit × (10^position)

3. Collect all non-zero components.
4. Sort them in descending order.
5. Return the result.

---
