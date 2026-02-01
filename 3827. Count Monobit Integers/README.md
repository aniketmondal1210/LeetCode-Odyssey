# Count Monobit Integers

## Problem Statement
You are given an integer **n**.

An integer is called **Monobit** if **all bits in its binary representation are the same**  
(i.e., the binary representation contains only `0`s or only `1`s).

Return the **count of Monobit integers** in the range **[0, n]** (inclusive).

---

## Examples

### Example 1
**Input**

n = 1


**Output**

2


**Explanation**
Binary representations in range:
- `0` → `"0"` (monobit)
- `1` → `"1"` (monobit)

Total = 2

---

### Example 2
**Input**

n = 4


**Output**

3


**Explanation**
Binary representations:
- `0` → `"0"` ✓
- `1` → `"1"` ✓
- `2` → `"10"` ✗
- `3` → `"11"` ✓
- `4` → `"100"` ✗

Valid monobit integers: `0, 1, 3`  
Total = 3

---

## Key Observation
A number is **Monobit** if:
- It is `0`, OR
- It has the form `2^k - 1` (binary representation is all `1`s)

Examples of `2^k - 1`:
- `1  = 1`
- `3  = 11`
- `7  = 111`
- `15 = 1111`

---

## Constraints

- 0 <= n <= 1000


---
