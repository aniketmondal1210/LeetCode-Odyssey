class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_copy = nums[:]
        count = 0
        for i in nums_copy:
            if i < k:
                nums.remove(i)
                count += 1
        return count
