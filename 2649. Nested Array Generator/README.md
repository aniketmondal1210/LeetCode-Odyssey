# Inorder Traversal of a Multi-Dimensional Array

## Problem

Given a multi-dimensional array of integers, return a **generator** that yields all integers in the same order as an inorder traversal.

A multi-dimensional array may contain:

- Integers
- Other multi-dimensional arrays

Traversal rule:

```text
Process elements from left to right.
If an element is an integer, yield it.
If an element is an array, recursively traverse it.
```

---

## Example 1

### Input

```javascript
arr = [[[6]], [1, 3], []]
```

### Output

```javascript
[6, 1, 3]
```

### Explanation

Traversal:

```text
[[[6]]] -> 6
[1,3]   -> 1, 3
[]      -> nothing
```

Result:

```text
6, 1, 3
```

---

## Example 2

### Input

```javascript
arr = []
```

### Output

```javascript
[]
```

### Explanation

The array contains no integers, so nothing is yielded.

---

## Constraints:

- 0 <= arr.flat().length <= 10^5
- 0 <= arr.flat()[i] <= 10^5
- maxNestingDepth <= 10^5
 
---

## Can you solve this without creating a new flattened version of the array?

---
