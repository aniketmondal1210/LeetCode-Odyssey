# Create Counter with Increment, Decrement, and Reset

## Problem Statement
Write a function `createCounter(init)` that accepts an **initial integer `init`** and returns an **object** with the following three functions:

1. `increment()` — increases the current value by 1 and returns it.  
2. `decrement()` — decreases the current value by 1 and returns it.  
3. `reset()` — resets the current value to `init` and returns it.

---

## Input
- `init`: integer (initial value of the counter)  
- A list of operations containing `"increment"`, `"decrement"`, or `"reset"`

**Constraints:**

-1000 ≤ init ≤ 1000

0 ≤ calls.length ≤ 1000

calls[i] ∈ {"increment", "decrement", "reset"}


---

## Output
- A list of integers — results from performing each operation sequentially.

---

## Examples

### Example 1
**Input:**

init = 5
calls = ["increment", "reset", "decrement"]

**Output:**

[6, 5, 4]

**Explanation:**

counter.increment() -> 6
counter.reset() -> 5
counter.decrement() -> 4


---

### Example 2
**Input:**

init = 0
calls = ["increment", "increment", "decrement", "reset", "reset"]

**Output:**

[1, 2, 1, 0, 0]


---
