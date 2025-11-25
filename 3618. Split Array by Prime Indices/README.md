# Split Array by Prime Indices

## Problem Statement
You are given an integer array `nums`.

Split `nums` into two arrays **A** and **B** using the rule:

- Elements at **prime indices** go into array **A**  
- All other elements go into array **B**

Here, array indices follow **0-based indexing**.

Return:

| sum(A) - sum(B) |


If an array is empty, its sum is considered **0**.

---

## Prime Index Definition (0-based)
Prime numbers start from **2**, so valid prime indices are:

2, 3, 5, 7, 11, ...


---

## Example 1
**Input:**

nums = [2, 3, 4]


**Processing:**
- Prime index: **2** → goes to A → `[4]`
- Non-prime indices: **0,1** → go to B → `[2,3]`

**Sum:**
- sum(A) = 4  
- sum(B) = 5  

**Output:**

1


---

## Example 2
**Input:**

nums = [-1, 5, 7, 0]


**Processing:**
- Prime indices: **2, 3** → A = `[7, 0]`
- Others: **0, 1** → B = `[-1, 5]`

**Sum:**
- sum(A) = 7  
- sum(B) = 4  

**Output:**

3

---

## Constraints

- 1 ≤ nums.length ≤ 100000
- −10⁹ ≤ nums[i] ≤ 10⁹

---
