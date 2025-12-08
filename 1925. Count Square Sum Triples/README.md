# Count Square Triples (Pythagorean Triples within Range)

A **square triple** `(a, b, c)` is a triple of integers that satisfies:

a^2 + b^2 = c^2


Given an integer `n`, return the **number of square triples** such that:

1 ≤ a, b, c ≤ n


Note that `(a, b, c)` and `(b, a, c)` are considered **different** if `a != b` (order matters for `a` and `b`).

---

## Examples

### Example 1

Input: n = 5

Output: 2

Explanation: The square triples are (3,4,5) and (4,3,5).


### Example 2

Input: n = 10

Output: 4

Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).


---

### Constraints:

- 1 <= n <= 250

---
