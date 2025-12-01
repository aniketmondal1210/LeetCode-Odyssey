# Sum of All Odd-Length Subarrays

## Problem Statement
Given an array of **positive integers** `arr`, return the **sum of all possible odd-length subarrays**.

A **subarray** is a contiguous part of the array.

---

## Example 1

### Input

arr = [1,4,2,5,3]


### Output

58


### Explanation  
Odd-length subarrays and their sums:

- Length 1:  
  `[1] = 1`  
  `[4] = 4`  
  `[2] = 2`  
  `[5] = 5`  
  `[3] = 3`

- Length 3:  
  `[1,4,2] = 7`  
  `[4,2,5] = 11`  
  `[2,5,3] = 10`

- Length 5:  
  `[1,4,2,5,3] = 15`

Total = **1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58**

---

## Example 2

### Input

arr = [1,2]


### Output

3


### Explanation  
Odd-length subarrays are `[1]` and `[2]`.

---

## Example 3

### Input

arr = [10,11,12]


### Output

66


---

## Constraints

- 1 ≤ arr.length ≤ 100
- 1 ≤ arr[i] ≤ 1000


---
