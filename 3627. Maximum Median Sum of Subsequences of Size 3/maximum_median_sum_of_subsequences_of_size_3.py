class Solution:
    def maximumMedianSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        k = n // 3
        return sum(nums[k::2])
