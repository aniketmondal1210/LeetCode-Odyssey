# Student Attendance Record Check

## Problem Statement
You are given a string `s` representing a student's attendance record.  
Each character can be:

- `'A'` → Absent  
- `'L'` → Late  
- `'P'` → Present  

The student is **eligible for an attendance award** if **both** conditions are met:

1. The student is absent (`'A'`) for **strictly fewer than 2 days**.
2. The student is **never late for 3 or more consecutive days**.

Return `true` if the student is eligible, otherwise return `false`.

---

## Examples

### Example 1
**Input**

s = "PPALLP"

**Output**

true

**Explanation**  
- Absences = 1 (< 2)  
- No occurrence of `"LLL"`  

---

### Example 2
**Input**

s = "PPALLL"

**Output**

false

**Explanation**  
- The student is late for 3 consecutive days (`"LLL"`)

---

## Constraints:

- 1 <= s.length <= 1000
- s[i] is either 'A', 'L', or 'P'.

---
