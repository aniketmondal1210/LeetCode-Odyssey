# Problem: Find Nearest Reachable Drone

## Problem Statement

You are given a 2D integer array `drones`, where:

```text
drones[i] = [xi, yi, rangei]
```

represents the x-coordinate, y-coordinate, and travel range of the `ith` drone.

You are also given an integer array:

```text
target = [tx, ty]
```

representing the coordinates of the target.

A drone `drones[i]` can reach the target if the **Manhattan distance** between its coordinates and the target coordinates is **less than or equal to** its `rangei`.

Return the **index** of the reachable drone with the **minimum Manhattan distance** to the target.

If there is a tie, return the **smallest index**.

If no drone can reach the target, return `-1`.

The **Manhattan distance** between two coordinates `(xi, yi)` and `(xj, yj)` is:

```text
|xi - xj| + |yi - yj|
```

---

## Example 1

**Input:**

```text
drones = [[0, 0, 8], [2, 2, 9]]
target = [3, 4]
```

**Output:**

```text
1
```

**Explanation:**

For drone `0`:

```text
|0 - 3| + |0 - 4| = 7
```

The distance `7` is within its range `8`.

For drone `1`:

```text
|2 - 3| + |2 - 4| = 3
```

The distance `3` is within its range `9`.

Since drone `1` has the smaller Manhattan distance, the answer is:

```text
1
```

---

## Example 2

**Input:**

```text
drones = [[2, 1, 5], [4, 4, 5], [6, 6, 8]]
target = [5, 5]
```

**Output:**

```text
1
```

**Explanation:**

For drone `0`:

```text
|2 - 5| + |1 - 5| = 7
```

Since `7 > 5`, it cannot reach the target.

For drone `1`:

```text
|4 - 5| + |4 - 5| = 2
```

Since `2 <= 5`, it can reach the target.

For drone `2`:

```text
|6 - 5| + |6 - 5| = 2
```

Since `2 <= 8`, it can also reach the target.

Both drone `1` and drone `2` have the minimum distance `2`. Since the smaller index is `1`, the answer is:

```text
1
```

---

## Example 3

**Input:**

```text
drones = [[4, 4, 5]]
target = [8, 6]
```

**Output:**

```text
-1
```

**Explanation:**

The Manhattan distance is:

```text
|4 - 8| + |4 - 6| = 6
```

Since `6 > 5`, the drone cannot reach the target.

No drone can reach the target, so the answer is:

```text
-1
```

---

## Approach

Traverse all drones and calculate the Manhattan distance from each drone to the target.

For each drone:

1. Calculate:

```text
distance = |xi - tx| + |yi - ty|
```

2. Check whether:

```text
distance <= rangei
```

3. If the drone can reach the target:
   - Compare its distance with the minimum distance found so far.
   - Update the answer if its distance is smaller.
   - If the distance is equal, keep the smaller index.

If no reachable drone is found, return `-1`.

---

## Complexity

### Time Complexity

```text
O(n)
```

where `n` is the number of drones.

### Auxiliary Space

```text
O(1)
```

Only a constant amount of extra space is required.

---

## Constraints

```text
1 <= drones.length <= 100
drones[i] = [xi, yi, rangei]
target = [tx, ty]
-25 <= xi, yi, tx, ty <= 25
1 <= rangei <= 100
```
