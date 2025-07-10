# Reverse Degree of a String

## Problem Statement

Given a string `s`, calculate its **reverse degree**.

### Definition:
- The **reverse degree** is calculated as follows:
  - For each character in the string, find its **position in the reversed alphabet**:
    - `'a' = 26`, `'b' = 25`, ..., `'z' = 1`
  - Multiply this with the character's **position in the string** (1-indexed).
  - Sum all such products for all characters.

Return the total **reverse degree** of the string `s`.

---

## Examples

### Example 1:

**Input:**  
`s = "abc"`

**Output:**  
`148`

**Explanation:**
```
  | Letter |  Reversed Alphabet Index | String Index | Product |
  |--------|--------------------------|--------------|---------|
  | a      | 26                       | 1            | 26      |
  | b      | 25                       | 2            | 50      |
  | c      | 24                       | 3            | 72      |
```
**Total Reverse Degree:** `26 + 50 + 72 = 148`

---

### Example 2:

**Input:**  
`s = "zaza"`

**Output:**  
`160`

**Explanation:**
```
  | Letter |  Reversed Alphabet Index | String Index | Product |
  |--------|--------------------------|--------------|---------|
  | z      | 1                        | 1            | 1       |
  | a      | 26                       | 2            | 52      |
  | z      | 1                        | 3            | 3       |
  | a      | 26                       | 4            | 104     |
```
**Total Reverse Degree:** `1 + 52 + 3 + 104 = 160`

---

## Constraints

- `1 <= s.length <= 1000`
- `s` contains only **lowercase English letters**.
