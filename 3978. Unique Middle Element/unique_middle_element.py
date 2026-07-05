class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid_idx = len(nums)//2
        mid_val = nums[mid_idx]
        return nums.count(mid_val) == 1
