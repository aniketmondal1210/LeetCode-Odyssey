class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] > (sum(nums[i:]) // len(nums[i:])):
                count += 1
        return count
