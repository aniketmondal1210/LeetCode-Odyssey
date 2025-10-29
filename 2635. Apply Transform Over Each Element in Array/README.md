# Custom Map Function — `map(arr, fn)`

## Problem Statement
Given an integer array **arr** and a **mapping function fn**, return a **new array** with the transformation applied to each element.

The resulting array should satisfy the condition:

returnedArray[i] = fn(arr[i], i)

You must **implement this without using the built-in `Array.map()`** method.

---

## 🧠 Example

### **Example 1**
**Input:**
arr = [1, 2, 3]

fn = function plusone(n) { return n + 1; }

Output:

[2, 3, 4]

Explanation:

Each element is increased by one.

map([1,2,3], plusone) → [2,3,4]

Example 2

Input:

arr = [1, 2, 3]

fn = function plusI(n, i) { return n + i; }

Output:

[1, 3, 5]

Explanation:

Each element is increased by its index.

map([1,2,3], plusI) → [1,3,5]

Example 3

Input:

arr = [10, 20, 30]

fn = function constant() { return 42; }

Output:

[42, 42, 42]

Explanation:

The function always returns 42 for any input.
