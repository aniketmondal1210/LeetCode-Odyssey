class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxi_sum = sum(nums[-k:])
        mini_sum = sum(nums[:k])
        return abs(maxi_sum - mini_sum)
