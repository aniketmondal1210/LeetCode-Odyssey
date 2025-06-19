Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it.  
That is, for each `nums[i]` you have to count the number of valid `j`'s such that `j != i` and `nums[j] < nums[i]`.

Return the answer in an array.

---

### Example 1:

**Input:**  
`nums = [8,1,2,2,3]`  
**Output:**  
`[4,0,1,1,3]`  
**Explanation:**  
- For `nums[0]=8`: four smaller numbers → 1, 2, 2, 3  
- For `nums[1]=1`: no smaller number  
- For `nums[2]=2`: one smaller number → 1  
- For `nums[3]=2`: one smaller number → 1  
- For `nums[4]=3`: three smaller numbers → 1, 2, 2

---

### Example 2:

**Input:**  
`nums = [6,5,4,8]`  
**Output:**  
`[2,1,0,3]`

---

### Example 3:

**Input:**  
`nums = [7,7,7,7]`  
**Output:**  
`[0,0,0,0]`

---

### Constraints:
- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`
