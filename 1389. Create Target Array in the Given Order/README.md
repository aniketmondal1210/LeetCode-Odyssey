# Create Target Array in the Given Order

You are given two integer arrays **nums** and **index**.  
You must build a **target** array using the rules:

1. Start with an empty target array.
2. For each `i` from left to right:
   - Insert `nums[i]` at position `index[i]` in the target array.
3. All insert operations are guaranteed valid.

Return the final **target** array.

---

## Examples

### Example 1

Input:
nums = [0,1,2,3,4]

index = [0,1,2,2,1]

Output: [0,4,1,3,2]


### Example 2

Input:

nums = [1,2,3,4,0]

index = [0,1,2,3,0]

Output: [0,1,2,3,4]


### Example 3

Input:

nums = [1]

index = [0]

Output: [1]


---

### Constraints:

- 1 <= nums.length, index.length <= 100
- nums.length == index.length
- 0 <= nums[i] <= 100
- 0 <= index[i] <= i

---
