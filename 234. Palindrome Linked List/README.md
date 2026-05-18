# Palindrome Linked List

## Problem Statement

Given the head of a singly linked list, return:

- `true` → if the linked list is a palindrome
- `false` → otherwise

A palindrome reads the same forward and backward.

---

# Examples

### Example 1

```text
Input:
head = [1,2,2,1]

Output:
true
```

### Explanation

```text
Forward  : 1 → 2 → 2 → 1
Backward : 1 → 2 → 2 → 1

Both are same.
```

---

### Example 2

```text
Input:
head = [1,2]

Output:
false
```

### Explanation

```text
Forward  : 1 → 2
Backward : 2 → 1

Not same.
```

---

## Constraints:

- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9
 

## Follow up: Could you do it in O(n) time and O(1) space?
