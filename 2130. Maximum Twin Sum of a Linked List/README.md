# Maximum Twin Sum of a Linked List

## Problem

In a linked list of even length `n`, the **ith** node (0-indexed) is the twin of the **(n - 1 - i)th** node.

The **twin sum** is defined as the sum of a node and its twin.

Given the head of the linked list, return the **maximum twin sum**.

---

## Examples

### Example 1

**Input**

```text
head = [5,4,2,1]
```

**Output**

```text
6
```

**Explanation**

Twin pairs are:

- 5 + 1 = 6
- 4 + 2 = 6

Maximum twin sum = **6**.

---

### Example 2

**Input**

```text
head = [4,2,2,3]
```

**Output**

```text
7
```

**Explanation**

Twin pairs are:

- 4 + 3 = 7
- 2 + 2 = 4

Maximum twin sum = **7**.

---

### Example 3

**Input**

```text
head = [1,100000]
```

**Output**

```text
100001
```

**Explanation**

Only one twin pair exists:

- 1 + 100000 = **100001**

---

## Constraints:

- The number of nodes in the list is an even integer in the range [2, 10^5].
- 1 <= Node.val <= 10^5

---
