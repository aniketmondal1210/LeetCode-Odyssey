# Delete Node in a Linked List (Without Head Access)

## Problem Statement

You are given:

- A singly linked list (but **no access to head**)
- A node `node` that must be deleted

👉 Delete the given node such that:
- Its value no longer exists in the list
- List size decreases by 1
- Order of other nodes remains unchanged

---

# Important Constraints

```
- Node is NOT the last node
- All values are unique
```

---

# Examples

### Example 1

**Input**
```
4 -> 5 -> 1 -> 9, node = 5
```

**Output**
```
4 -> 1 -> 9
```

---

### Example 2

**Input**
```
4 -> 5 -> 1 -> 9, node = 1
```

**Output**
```
4 -> 5 -> 9
```

---

## Constraints:

- The number of the nodes in the given list is in the range [2, 1000].
- -1000 <= Node.val <= 1000
- The value of each node in the list is unique.
- The node to be deleted is in the list and is not a tail node.

---
