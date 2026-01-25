class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        for i in range(len(nums)//2):
            result.append(nums[i] + nums[-(i+1)])
        return max(result)
