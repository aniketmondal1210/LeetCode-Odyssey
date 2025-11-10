# Problem: Implement Promise.all Without Using It

## Problem Statement
You are given an array of asynchronous functions `functions`.  
Each function accepts **no arguments** and returns a **promise**.  

You need to implement a custom function `promiseAll(functions)` that:
- Executes all promises **in parallel**.
- Returns a single **promise** that:
  - **Resolves** with an array of results when **all** promises resolve.
  - **Rejects** with the **first rejection reason** if any promise rejects.
- The **order of results** in the resolved array must match the order of functions.

You must solve this **without using `Promise.all()`**.

---

## Example 1

**Input:**
functions = [
  () => new Promise(resolve => setTimeout(() => resolve(5), 200))
];

**Output:**

{"t": 200, "resolved": [5]}

Explanation:
The single function was resolved at 200ms with value 5.

## Example 2

**Input:**

functions = [
  () => new Promise(resolve => setTimeout(() => resolve(1), 200)),
  () => new Promise((resolve, reject) => setTimeout(() => reject("Error"), 100))
];

**Output:**

{"t": 100, "rejected": "Error"}

Explanation:
One of the promises rejected first, so the final promise also rejected with "Error".

## Example 3

**Input:**

functions = [
  () => new Promise(resolve => setTimeout(() => resolve(4), 50)),
  () => new Promise(resolve => setTimeout(() => resolve(10), 150)),
  () => new Promise(resolve => setTimeout(() => resolve(16), 100))
];

**Output:**

{"t": 150, "resolved": [4, 10, 16]}

Explanation:
All promises resolved successfully, and the final result is [4, 10, 16].

## Constraints

- 1 <= functions.length <= 10

functions is an array of functions that each return a promise.
