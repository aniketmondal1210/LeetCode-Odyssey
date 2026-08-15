# Problem: Elevator Request Time

## Problem Statement

You are given an integer `n` denoting the number of floors in a building, where the floors are numbered from `0` to `n - 1`.

You are also given an integer array `requests`, where `requests` represents the sequence of floor requests.

An elevator starts at floor `0` and follows these rules:

- The elevator moves one floor per second.
- The elevator serves requests in the given order.
- If the elevator is already on the requested floor, no movement is needed.
- After serving a request, the elevator immediately starts moving toward the next request.

Return the **total time** in seconds required to serve all requests.

---

## Example 1

**Input:**

```text
n = 5
requests = [2, 1, 4, 3]
```

**Output:**

```text
7
```

**Explanation:**

The elevator starts at floor `0`.

```text
Request 2: 0 -> 2 = 2 seconds
Request 1: 2 -> 1 = 1 second
Request 4: 1 -> 4 = 3 seconds
Request 3: 4 -> 3 = 1 second
```

Total time:

```text
2 + 1 + 3 + 1 = 7 seconds
```

---

## Example 2

**Input:**

```text
n = 3
requests = [2, 0, 0]
```

**Output:**

```text
4
```

**Explanation:**

The elevator starts at floor `0`.

```text
Request 2: 0 -> 2 = 2 seconds
Request 0: 2 -> 0 = 2 seconds
Request 0: 0 -> 0 = 0 seconds
```

Total time:

```text
2 + 2 + 0 = 4 seconds
```

---

## Approach

Keep track of the elevator's current floor, initially `0`.

For each requested floor:

1. Calculate the absolute difference between the current floor and the requested floor.
2. Add this difference to the total time.
3. Update the current floor to the requested floor.

The time required to move between two floors is:

```text
abs(currentFloor - requestedFloor)
```

---

## Complexity

### Time Complexity

```text
O(m)
```

where `m` is the number of requests.

### Auxiliary Space

```text
O(1)
```

---

## Constraints

```text
1 <= n <= 100
1 <= requests.length <= 100
0 <= requests[i] <= n - 1
```
