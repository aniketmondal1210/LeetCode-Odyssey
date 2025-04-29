# Problem: Binary Date Representation

## Problem Statement

You are given a string `date` representing a Gregorian calendar date in the `yyyy-mm-dd` format.

The goal is to convert the date into its binary representation, obtained by converting the **year**, **month**, and **day** to their binary forms **without leading zeroes**, and writing them down in `year-month-day` format.

### Input

- A string `date` of length 10.
- `date[4] == date[7] == '-'`, and all other `date[i]`s are digits.
- The input represents a valid Gregorian calendar date between **Jan 1st, 1900** and **Dec 31st, 2100** (inclusive).

### Output

- A string representing the binary form of the date in `year-month-day` format, using **binary numbers without leading zeros**.

---

## Examples

### Example 1

**Input:**  
`date = "2080-02-29"`

**Output:**  
`100000100000-10-11101`

**Explanation:**  
- 2080 in binary is `100000100000`  
- 02 in binary is `10`  
- 29 in binary is `11101`

### Example 2

**Input:**  
`date = "1900-01-01"`

**Output:**  
`11101101100-1-1`

**Explanation:**  
- 1900 in binary is `11101101100`  
- 01 in binary is `1`  
- 01 in binary is `1`

---
