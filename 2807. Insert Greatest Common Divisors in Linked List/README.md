# Insert Greatest Common Divisors in Linked List

## Problem

Given the head of a linked list, insert a new node between every pair of adjacent nodes.

The value of each inserted node should be the **Greatest Common Divisor (GCD)** of the values of the two adjacent nodes.

Return the head of the modified linked list.

---

## Examples

### Example 1

**Input**

```text
head = [18,6,10,3]
```

**Output**

```text
[18,6,6,2,10,1,3]
```

**Explanation**

- GCD(18, 6) = 6
- GCD(6, 10) = 2
- GCD(10, 3) = 1

After inserting these values, the list becomes:

```text
18 -> 6 -> 6 -> 2 -> 10 -> 1 -> 3
```

---

### Example 2

**Input**

```text
head = [7]
```

**Output**

```text
[7]
```

**Explanation**

There is only one node, so no new nodes are inserted.

---

## Constraints:

- The number of nodes in the list is in the range [1, 5000].
- 1 <= Node.val <= 1000

---
