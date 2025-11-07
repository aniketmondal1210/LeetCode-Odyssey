# Time Limited Function

## Problem Statement
Given an **asynchronous function** `fn` and a time `t` in milliseconds,  
return a **new time-limited version** of the input function.

The returned function should:
1. **Resolve** with the result if `fn` completes within the time limit `t`.
2. **Reject** with the string `"Time Limit Exceeded"` if execution exceeds the limit.

---

## Example 1
**Input:**
fn = async (n) => { 
  await new Promise(res => setTimeout(res, 100)); 
  return n * n; 
}
inputs = [5]
t = 50

**Output:**

{"rejected": "Time Limit Exceeded", "time": 50}

Explanation:
The function takes 100ms to resolve, but the limit is 50ms.
Hence, it rejects with "Time Limit Exceeded" after 50ms.

## Example 2

**Input:**

fn = async (n) => { 
  await new Promise(res => setTimeout(res, 100)); 
  return n * n; 
}
inputs = [5]
t = 150

**Output:**

{"resolved": 25, "time": 100}

Explanation:
The function resolves successfully within the time limit.

## Example 3

**Input:**

fn = async (a, b) => { 
  await new Promise(res => setTimeout(res, 120)); 
  return a + b; 
}
inputs = [5, 10]
t = 150

**Output:**

{"resolved": 15, "time": 120}

Explanation:
The function completes before 150ms, returning 15.

## Example 4

**Input:**

fn = async () => { 
  throw "Error";
}
inputs = []
t = 1000

**Output:**

{"rejected": "Error", "time": 0}

Explanation:
The function throws an error immediately.
