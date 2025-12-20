# Day of the Year

## Problem Statement
You are given a string `date` representing a **Gregorian calendar date** in the format:

YYYY-MM-DD


Your task is to return the **day number of the year** for the given date.

---

## Examples

### Example 1
**Input:**  

date = "2019-01-09"

**Output:**  

9

**Explanation:**  
January 9th is the 9th day of the year.

---

### Example 2
**Input:**  

date = "2019-02-10"

**Output:**  

41

**Explanation:**  
- January has 31 days  
- February 10 → 10 days  
- Total = 31 + 10 = 41

---

### Constraints

- date.length == 10
- date[4] == date[7] == '-'
- 1900 ≤ year ≤ 2019

---
