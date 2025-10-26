# Reduce Function Implementation (Without Using Built-in Reduce)

## Problem Statement
Given:
- An integer array `nums`
- A reducer function `fn`
- An initial value `init`

Return the **final result** obtained by executing `fn` sequentially on each element of `nums`, using the result from the previous operation.

If the array is empty, simply return `init`.

---

## Logic
The process follows this sequence:

val = fn(init, nums[0])
val = fn(val, nums[1])
val = fn(val, nums[2])
...
return val


If `nums` is empty → return `init`.

---

## Examples

### Example 1
**Input:**

nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr; }
init = 0

**Output:**

10

**Explanation:**

0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10


---

### Example 2
**Input:**

nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr * curr; }
init = 100

**Output:**

130

**Explanation:**

100 + 1² = 101
101 + 2² = 105
105 + 3² = 114
114 + 4² = 130


---

### Example 3
**Input:**

nums = []
fn = function sum(accum, curr) { return 0; }
init = 25

**Output:**

25

**Explanation:**  
Empty array → return initial value.

---

## Constraints

0 ≤ nums.length ≤ 1000
0 ≤ nums[i] ≤ 1000
0 ≤ init ≤ 1000


---
