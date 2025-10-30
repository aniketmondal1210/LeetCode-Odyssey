# Custom Filter Function — `filter(arr, fn)`

## Problem Statement
Given an integer array **arr** and a **filtering function fn**, return a **filtered array** `filteredArr`.

The `fn` function takes **one or two arguments**:
- `arr[i]` → element from the array  
- `i` → index of the element  

The **filtered array** should only contain elements from **arr** for which the expression  
`fn(arr[i], i)` evaluates to a **truthy** value.  

A **truthy** value is any value where `Boolean(value)` returns **true**.

You must solve this **without using the built-in `Array.filter()`** method.

---

## Example

### **Example 1**
**Input:**
arr = [0, 10, 20, 30]

fn = function greaterThan10(n) { return n > 10; }

Output:

[20, 30]

Explanation:
The function filters out values that are not greater than 10.

Example 2

Input:

arr = [1, 2, 3]
fn = function firstIndex(n, i) { return i === 0; }

Output:

[1]

Explanation:
The function filters out all elements except the one at index 0.

Example 3

Input:

arr = [-2, -1, 0, 1, 2]

fn = function plusOne(n) { return n + 1; }

Output:

[-2, 0, 1, 2]

Explanation:

fn returns falsy (0) for the element -1, so that value is excluded from the output.
