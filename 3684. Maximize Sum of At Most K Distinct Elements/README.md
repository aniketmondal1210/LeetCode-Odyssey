# Select At Most K Distinct Elements With Maximum Sum

## Problem Statement
You are given:
- A positive integer array `nums`
- An integer `k`

You must **choose at most `k` elements** from `nums` such that:
- All chosen elements are **distinct**
- Their **sum is maximized**

Finally, return the chosen elements in **strictly descending order**.

---

## Examples

### Example 1
**Input:**

nums = [84, 93, 100, 77, 90], k = 3

**Output:**

[100, 93, 90]


**Explanation:**  
Choosing the three largest distinct values gives the maximum sum.

---

### Example 2
**Input:**

nums = [84, 93, 100, 77, 93], k = 3

**Output:**

[100, 93, 84]


**Explanation:**  
Even though `93` appears twice, it can be chosen only once.

---

### Example 3
**Input:**

nums = [1,1,1,2,2,2], k = 6

**Output:**

[2,1]


**Explanation:**  
Only two distinct numbers exist. We choose both.

---

## Constraints

- 1 ≤ nums.length ≤ 100
- 1 ≤ nums[i] ≤ 10^9
- 1 ≤ k ≤ nums.length


---
