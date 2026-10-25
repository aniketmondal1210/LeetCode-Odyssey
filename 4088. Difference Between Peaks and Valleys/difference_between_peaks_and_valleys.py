class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        result = 0
        for i in range(1, len(nums) - 1):
            if nums[i-1] < nums[i] > nums[i+1]:
                result += nums[i]
            elif nums[i-1] > nums[i] < nums[i+1]:
                result -= nums[i]
        return result
