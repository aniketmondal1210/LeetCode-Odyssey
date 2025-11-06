# Problem: Implement a Cancellable Repeated Function Caller

## Problem Statement
You are given:
- A function `fn`
- An array of arguments `args`
- An interval time `t` (in milliseconds)

You must return a **cancel function (`cancelFn`)** that stops the repeated calls after a certain time.

The function `fn` should:
- Be called **immediately** with the arguments `args`
- Then called **again every `t` milliseconds**
- Continue until `cancelFn` is called (after a specified cancel time)

---

## Example 1

**Input**
fn = (x) => x * 2
args = [4]
t = 35
const cancelTimeMs = 190;

Execution

const cancelFn = cancellable(fn, args, t);
setTimeout(cancelFn, cancelTimeMs);

**Output**

[
  {"time": 0, "returned": 8},
  {"time": 35, "returned": 8},
  {"time": 70, "returned": 8},
  {"time": 105, "returned": 8},
  {"time": 140, "returned": 8},
  {"time": 175, "returned": 8}
]

Explanation

    The function fn(4) returns 8.

    It runs immediately at 0ms, then every 35ms until 190ms.

    Cancelled at 190ms.

# Example 2
**Input**

fn = (x1, x2) => x1 * x2
args = [2, 5]
t = 30
const cancelTimeMs = 165;

**Output**

[
  {"time": 0, "returned": 10},
  {"time": 30, "returned": 10},
  {"time": 60, "returned": 10},
  {"time": 90, "returned": 10},
  {"time": 120, "returned": 10},
  {"time": 150, "returned": 10}
]

Explanation

    fn(2,5) returns 10.

    It runs every 30ms until cancelled at 165ms.

# Example 3
**Input**

fn = (x1, x2, x3) => x1 + x2 + x3
args = [5, 1, 3]
t = 50
const cancelTimeMs = 180;

**Output**

[
  {"time": 0, "returned": 9},
  {"time": 50, "returned": 9},
  {"time": 100, "returned": 9},
  {"time": 150, "returned": 9}
]

## Constraints

- fn is a function
- args is a valid JSON array
- 1 <= args.length <= 10
- 30 <= t <= 100
- 10 <= cancelTimeMs <= 500
