# Problem: Cancellable Function Execution

## Problem Statement
You are given:
- A function `fn`
- An array of arguments `args`
- A timeout `t` in milliseconds

You need to return a **cancel function** `cancelFn`.

Initially, the execution of `fn` should be **delayed by `t` milliseconds**.  
If the `cancelFn` is called **before** the delay finishes, the execution of `fn` should be **canceled**.  
If the `cancelFn` is **not called** before `t` milliseconds, `fn` should be executed with the given arguments.

---

## Example 1
**Input:**

fn = (x) => x * 5
args = [2]
t = 20


**Output:**

[{"time": 20, "returned": 10}]


**Explanation:**
const cancelTimeMs = 50;
const cancelFn = cancellable((x) => x * 5, [2], 20);
setTimeout(cancelFn, cancelTimeMs);

    fn(2) executes at 20ms → returns 10

    Cancellation at 50ms happens after execution, so it has no effect.

## Example 2

**Input:**

fn = (x) => x**2
args = [2]
t = 100

**Output:**

[]
**Explanation:**

const cancelTimeMs = 50;
const cancelFn = cancellable((x) => x**2, [2], 100);
setTimeout(cancelFn, cancelTimeMs);

    Cancellation at 50ms occurs before the function executes at 100ms,
    so fn(2) is never called.

## Example 3

**Input:**

fn = (x1, x2) => x1 * x2
args = [2, 4]
t = 30

**Output:**

[{"time": 30, "returned": 8}]

**Explanation:**

const cancelTimeMs = 100;
const cancelFn = cancellable((x1, x2) => x1 * x2, [2, 4], 30);
setTimeout(cancelFn, cancelTimeMs);

    fn(2,4) executes at 30ms, returning 8

    Cancellation at 100ms happens afterward, so it has no effect.

## Your Task

Implement the function:

function cancellable(fn, args, t)

which returns a cancelFn.
If cancelFn() is invoked before t milliseconds, cancel the pending execution of fn.

## Constraints

fn is a function
args is a valid JSON array
1 ≤ args.length ≤ 10
20 ≤ t ≤ 1000
10 ≤ cancelTimeMs ≤ 1000

## Expected Time Complexity

O(1)

## Expected Auxiliary Space

O(1)
