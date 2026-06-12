# Snail Traversal Array

## Problem

Enhance all arrays with a method:

```javascript
snail(rowsCount, colsCount)
```

that converts a 1D array into a 2D matrix using **snail traversal order**.

### Rules

- If:

```text
rowsCount * colsCount !== nums.length
```

return:

```javascript
[]
```

- Fill columns alternately:
  - First column: top → bottom
  - Second column: bottom → top
  - Third column: top → bottom
  - and so on...

---

## Example 1

### Input

```javascript
nums = [19,10,3,7,9,8,5,2,1,17,16,14,12,18,6,13,11,20,4,15]
rowsCount = 5
colsCount = 4
```

### Output

```javascript
[
 [19,17,16,15],
 [10,1,14,4],
 [3,2,12,20],
 [7,5,18,11],
 [9,8,6,13]
]
```

---

## Example 2

### Input

```javascript
nums = [1,2,3,4]
rowsCount = 1
colsCount = 4
```

### Output

```javascript
[[1,2,3,4]]
```

---

## Example 3

### Input

```javascript
nums = [1,3]
rowsCount = 2
colsCount = 2
```

### Output

```javascript
[]
```

### Explanation

```text
2 × 2 = 4 ≠ 2
```

Invalid dimensions.

---

## Constraints:

- 0 <= nums.length <= 250
- 1 <= nums[i] <= 1000
- 1 <= rowsCount <= 250
- 1 <= colsCount <= 250

---
