# Complete Prime Number

A number **num** is called a **Complete Prime Number** if:

- Every **prefix** of the number is prime.
- Every **suffix** of the number is prime.
- Single-digit numbers count only if the digit itself is prime.

---

## Examples

### Example 1

Input: num = 23
Output: true
Explanation: Prefixes → 2, 23 (prime).
Suffixes → 3, 23 (prime).


### Example 2

Input: num = 39
Output: false
Explanation: Prefixes → 3 (prime), 39 (not prime).
Suffixes → 9 (not prime), 39 (not prime).


### Example 3

Input: num = 7
Output: true
Explanation: 7 is prime.


---

### Constraints:

- 1 <= num <= 10^9

---
