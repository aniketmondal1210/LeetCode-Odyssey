# Number of Students Doing Homework at a Given Time

## Problem

Given two integer arrays `startTime` and `endTime` and an integer `queryTime`.

The `ith` student started doing their homework at `startTime[i]` and finished it at `endTime[i]`.

Return the number of students doing their homework at `queryTime`.

A student is doing homework at `queryTime` if:

`startTime[i] <= queryTime <= endTime[i]`

The interval is **inclusive**, meaning a student who starts or finishes exactly at `queryTime` is counted.

## Examples

### Example 1

```text
Input:
startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4

Output:
1
```

**Explanation:**  
Only the third student is doing homework at time `4`, because their homework interval is `[3,7]`.

### Example 2

```text
Input:
startTime = [4]
endTime = [4]
queryTime = 4

Output:
1
```

**Explanation:**  
The only student's homework interval is `[4,4]`, so they are counted.

## Constraints

- `startTime.length == endTime.length`
- `1 <= startTime.length <= 100`
- `1 <= startTime[i] <= endTime[i] <= 1000`
- `1 <= queryTime <= 1000`
