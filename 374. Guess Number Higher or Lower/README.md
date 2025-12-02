# Guess the Number (Using the `guess()` API)

## Problem Statement
You are playing a number guessing game.  
I choose a number between **1 and n**, and your task is to **find the exact number**.

You are given a predefined API:

int guess(int num)


It returns:

- `-1` → Your guess is **higher** than the number I picked.  
- `1`  → Your guess is **lower** than the number I picked.  
- `0`  → Your guess is **correct**.

Your goal:  
Return **the number I picked**, using the fewest guesses possible.

This is a classic **binary search** problem.

---

## Example 1
**Input:**  

n = 10, pick = 6

**Output:**  

6


## Example 2
**Input:**  

n = 1, pick = 1

**Output:**  

1


## Example 3
**Input:**  

n = 2, pick = 1

**Output:**  

1


---

## Constraints

1 ≤ n ≤ 2^31 − 1
1 ≤ pick ≤ n

---
