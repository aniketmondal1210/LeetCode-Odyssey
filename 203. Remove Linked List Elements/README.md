# Remove Linked List Elements

## Problem

Given the head of a linked list and an integer `val`, remove all nodes whose value is equal to `val`.

Return the head of the modified linked list.

---

## Example 1

### Input

```text
head = [1,2,6,3,4,5,6]
val = 6
```

### Output

```text
[1,2,3,4,5]
```

### Explanation

Both nodes with value `6` are removed.

---

## Example 2

### Input

```text
head = []
val = 1
```

### Output

```text
[]
```

---

## Example 3

### Input

```text
head = [7,7,7,7]
val = 7
```

### Output

```text
[]
```

### Explanation

All nodes are removed.

---

## Constraints:

- The number of nodes in the list is in the range [0, 10^4].
- 1 <= Node.val <= 50
- 0 <= val <= 50

---
