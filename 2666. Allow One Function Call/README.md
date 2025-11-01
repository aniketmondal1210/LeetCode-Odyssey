# Function Composition

## Problem Statement
Given an array of functions `[f1, f2, f3, ..., fn]`, return a **new function** `fn` that is the **composition** of all the given functions.

The function composition of `[f(x), g(x), h(x)]` is:

fn(x) = f(g(h(x)))

If the list of functions is **empty**, return the **identity function**:

f(x) = x

Each function accepts **one integer** as input and returns **one integer** as output.

---

## Examples

### **Example 1**
**Input:**
functions = [x => x + 1, x => x * x, x => 2 * x]
x = 4

Output:

65

Explanation:

Evaluating from right to left:

    2 × 4 = 8

    8 × 8 = 64

    64 + 1 = 65

Result → 65

Example 2

Input:

functions = [x => 10 * x, x => 10 * x, x => 10 * x]

x = 1

Output:

1000

Explanation:

Evaluating from right to left:

    10 × 1 = 10

    10 × 10 = 100

    10 × 100 = 1000

Result → 1000

Example 3

Input:

functions = []

x = 42

Output:

42

Explanation:

With no functions, the identity function f(x) = x returns the same input.
