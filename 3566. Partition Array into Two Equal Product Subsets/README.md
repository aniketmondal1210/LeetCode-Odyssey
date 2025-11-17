# Problem: Partition Array Into Two Subsets With Product Equal to Target

## Problem Statement
You are given:
- An integer array **nums** of *distinct positive integers*
- An integer **target**

Determine whether you can split the array into **two non-empty disjoint subsets** such that:

product(subset1) = target
product(subset2) = target


Each element must belong to exactly one subset.

Return:
- `true` → if such a partition exists
- `false` → otherwise

---

## Key Insight
If both subsets must have product = **target**, then the **product of all numbers** must be:

product(nums) = target × target = target²


So a necessary condition is:

product(nums) == target²


If this is false → answer is automatically **false**.

---

Next requirement:
We must find a **subset** whose product = target.

If such a subset exists AND the remaining elements also multiply to target → answer is **true**.

Because elements are **distinct**, and length ≤ 12 → we can use **backtracking or bitmask enumeration** (2ⁿ = 4096 max).

---

## Example 1

**Input:**

nums = [3,1,6,8,4], target = 24


**Output:**

true


**Explanation:**  
Two subsets are:
- [3, 8] → 3 × 8 = 24  
- [1, 6, 4] → 1 × 6 × 4 = 24  

Condition satisfied.

---

## Example 2

**Input:**

nums = [2,5,3,7], target = 15


**Output:**

false


**Explanation:**  
No subset has product = 15.  
Hence no valid partition exists.

---

## Constraints

- 3 ≤ nums.length ≤ 12
- 1 ≤ target ≤ 10¹⁵
- 1 ≤ nums[i] ≤ 100
- All elements distinct


---
