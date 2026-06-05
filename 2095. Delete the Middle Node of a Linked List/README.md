# Delete the Middle Node of a Linked List

## Idea

Use the **slow and fast pointer** technique.

- `slow` moves one step at a time.
- `fast` moves two steps at a time.
- Keep a `prev` pointer to the node before `slow`.

When `fast` reaches the end:

```text
slow -> middle node
prev -> node before middle
```

Delete the middle node by:

```cpp
prev->next = slow->next;
```

---

# Example 1

## Input

```text
1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
```

### Middle Node

```text
7
```

### Output

```text
1 -> 3 -> 4 -> 1 -> 2 -> 6
```

---

# Example 2

## Input

```text
1 -> 2 -> 3 -> 4
```

### Middle Index

```text
⌊4/2⌋ = 2
```

Node value:

```text
3
```

### Output

```text
1 -> 2 -> 4
```

---

# Example 3

## Input

```text
2 -> 1
```

### Middle Index

```text
⌊2/2⌋ = 1
```

Node value:

```text
1
```

### Output

```text
2
```

---

## Constraints:

- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5

---
