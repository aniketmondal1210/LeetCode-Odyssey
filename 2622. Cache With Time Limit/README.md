# Time Limited Cache

## Problem Statement
You need to design a class that allows storing **key-value pairs** where each key has an **expiration time** (in milliseconds).  
After the expiration time passes, the key becomes **inaccessible**.

The class should support the following methods:

1. **`set(key, value, duration)`**
   - Stores the key-value pair for `duration` milliseconds.
   - Returns `true` if the same **unexpired key** already exists.
   - Returns `false` otherwise.
   - If the key exists, both the value and duration should be overwritten.

2. **`get(key)`**
   - Returns the **value** if the key exists and has not expired.
   - Returns `-1` if the key has expired or does not exist.

3. **`count()`**
   - Returns the **number of unexpired keys** currently in the cache.

---

## Example 1

**Input**

actions = ["TimeLimitedCache", "set", "get", "count", "get"]
values = [[], [1, 42, 100], [1], [], [1]]
timeDelays = [0, 0, 50, 50, 150]


**Output**

[null, false, 42, 1, -1]


**Explanation**
- `t = 0`: Cache created.
- `t = 0`: `(1, 42)` set for 100ms. Returns `false` (key didn’t exist).
- `t = 50`: `get(1)` → returns `42`.
- `t = 50`: `count()` → returns `1`.
- `t = 150`: `get(1)` → returns `-1` (key expired).

---

## Example 2

**Input**

actions = ["TimeLimitedCache", "set", "set", "get", "get", "get", "count"]
values = [[], [1, 42, 50], [1, 50, 100], [1], [1], [1], []]
timeDelays = [0, 0, 40, 50, 120, 200, 250]


**Output**

[null, false, true, 50, 50, -1, 0]


**Explanation**
- `t = 0`: `(1, 42)` set for 50ms → returns `false`.
- `t = 40`: `(1, 50)` set for 100ms → returns `true` (previous value still valid).
- `t = 50`: `get(1)` → returns `50`.
- `t = 120`: `get(1)` → returns `50`.
- `t = 140`: Key expires.
- `t = 200`: `get(1)` → returns `-1`.
- `t = 250`: `count()` → returns `0`.

---

## Constraints

0 <= key, value <= 10^9
0 <= duration <= 1000
1 <= actions.length <= 100
actions.length === values.length === timeDelays.length
0 <= timeDelays[i] <= 1450


---
