class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        return sum(1 for i in range(1, len(nums)) if nums[i] == nums[i-1])
