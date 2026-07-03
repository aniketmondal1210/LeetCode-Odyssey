class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        result = []
        for j in nums:
            if j != 0:
                result.append(j)
        zero_count = nums.count(0)
        for k in range(zero_count):
            result.append(0)
        return result
