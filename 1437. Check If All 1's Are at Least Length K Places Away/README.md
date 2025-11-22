# Check If All 1's Are at Least K Places Apart

## Problem Statement
You are given a **binary array** `nums` and an integer `k`.  
Return **true** if **every pair of 1's** in the array is separated by **at least `k` zeros**.  
Otherwise, return **false`.

---

## Example 1
**Input:**  

nums = [1,0,0,0,1,0,0,1], k = 2

**Output:**  

true

**Explanation:**  
- Distance between 1st and 2nd `1` = 3 ≥ 2  
- Distance between 2nd and 3rd `1` = 3 ≥ 2  
All conditions satisfied.

---

## Example 2
**Input:**  

nums = [1,0,0,1,0,1], k = 2

**Output:**  

false

**Explanation:**  
The second and third `1` are only **1** place apart (index 3 and 5), which is less than `k = 2`.

---

## Approach
- Track the index of the **previous 1**.
- For each new `1`, check:  

current_index - previous_index - 1 >= k

- Update previous index.
- If any pair violates the condition, return false.

Time Complexity: `O(n)`  
Space Complexity: `O(1)`

---

## Constraints

- 1 <= nums.length <= 100000
- 0 <= k <= nums.length
- nums[i] is 0 or 1
