# Convert Binary Number in a Linked List to Integer

## Problem

Given the head of a linked list where each node contains either `0` or `1`, the linked list represents a binary number.

The **most significant bit (MSB)** is at the head of the list.

Return the decimal value of the binary number.

---

## Example 1

### Input

```text
head = [1,0,1]
```

### Output

```text
5
```

### Explanation

Binary number:

```text
101₂
```

Decimal value:

```text
1×2² + 0×2¹ + 1×2⁰
= 4 + 0 + 1
= 5
```

---

## Example 2

### Input

```text
head = [0]
```

### Output

```text
0
```

---

## Constraints:

- The Linked List is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.

---
